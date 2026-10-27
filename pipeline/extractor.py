import json
import logging
import re
import sys
from pathlib import Path
from typing import List, Optional, Literal, Tuple
from pydantic import BaseModel, Field
from google import genai

# Allow running directly or as module
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.config import (
    THEMES,
    DEFAULT_MODEL,
    GEMINI_API_KEY,
    COMEDY_CRAFT_LEXICON,
    MIN_KEYWORD_MATCHES,
    MAX_TOTAL_TOKENS_PER_RUN,
    MAX_CONSECUTIVE_EMPTY_CHUNKS
)
from pipeline.transcribe import format_seconds

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("extractor")

# Global running token counter across the CLI session
total_run_tokens: int = 0


def get_total_run_tokens() -> int:
    """Returns the cumulative token count for the current execution run."""
    return total_run_tokens


def reset_run_tokens() -> None:
    """Resets the cumulative token count."""
    global total_run_tokens
    total_run_tokens = 0


def pre_filter_chunk(text: str) -> bool:
    """
    Zero-token heuristic: returns False if chunk lacks comedy craft vocabulary.
    Inspects text for single-word or multi-word matches from COMEDY_CRAFT_LEXICON.
    """
    text_lower = text.lower()
    matches = 0

    for term in COMEDY_CRAFT_LEXICON:
        if " " in term:
            if term in text_lower:
                matches += 1
        else:
            if re.search(rf"\b{re.escape(term)}\b", text_lower):
                matches += 1

        if matches >= MIN_KEYWORD_MATCHES:
            return True

    return False


class CraftQuote(BaseModel):
    theme: Literal[
        "Writing & Joke Construction",
        "Performance & Stagecraft",
        "Mental Attitudes",
        "Overcoming Bombs/Blocks",
        "Professional Problem-Solving"
    ] = Field(description="The core craft theme this quote addresses.")
    topic: str = Field(description="Short 3-6 word headline summarizing the craft insight.")
    speaker: str = Field(description="Name of the person who spoke the quote.")
    setup_context: str = Field(description="Brief 1-2 sentence context explaining what they were discussing.")
    start_seconds: int = Field(description="Exact starting time of the quote in seconds from video start.")
    end_seconds: int = Field(description="Exact ending time of the quote in seconds from video start.")
    verbatim_quote: str = Field(description="Word-for-word verbatim quote from the transcript text. Do not summarize or smooth colloquialisms.")
    tactical_takeaway: str = Field(description="Concrete, actionable takeaway or lesson for stand-up comedians on craft, technique, or mindset.")


class ChunkExtractionResponse(BaseModel):
    comedian: str = Field(description="Primary comedian speaking or featured in this discussion.")
    host: str = Field(description="Host of the show/podcast (or co-host).")
    quotes: List[CraftQuote] = Field(default_factory=list, description="Extracted craft quotes. Empty if no craft discussion occurred.")


EXTRACTION_SYSTEM_PROMPT = """You are an expert stand-up comedy analyst and archivist.
Your job is to read timestamped transcripts from comedy podcasts and extract high-value VERBATIM quotes where comedians discuss the CRAFT, ART, and MECHANICS of stand-up comedy.

CRITICAL EXTRACTION RULES:
1. ONLY extract quotes focusing strictly on these 5 themes:
   - Writing & Joke Construction (premise generation, editing, punchlines, tags, callbacks, writing routines)
   - Performance & Stagecraft (timing, pauses, rhythm, crowd reading, body language, microphone technique)
   - Mental Attitudes (psychology of performance, overcoming inner critic, confidence, ego vs humility)
   - Overcoming Bombs/Blocks (surviving bombing, recovering from silence, breaking writer's block, handling hecklers)
   - Professional Problem-Solving (touring, special tapings, club politics, industry strategy)
2. DO NOT extract general banter, unrelated stories, gossip, or jokes that are not about the process of comedy.
3. VERBATIM RULE: The `verbatim_quote` MUST be 100% VERBATIM from the transcript text. DO NOT summarize, edit grammar, or smooth out colloquial speech ("like", "you know", "gonna", etc.).
4. Accurate timestamps: Use the embedded [HH:MM:SS] markers in the transcript text to determine exact start_seconds and end_seconds.
5. If the chunk does not contain any discussions about comedy craft, return an empty quotes list (`[]`).
"""


def get_gemini_client() -> genai.Client:
    """Initializes and returns the Google GenAI Client."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set. Please provide it in .env or the environment.")
    return genai.Client(api_key=GEMINI_API_KEY)


def extract_quotes_from_chunk(
    chunk: dict,
    video_id: str,
    video_title: str,
    channel_name: str,
    model_name: str = DEFAULT_MODEL
) -> Tuple[ChunkExtractionResponse, int]:
    """
    Extracts comedy craft quotes from a single transcript chunk using Gemini.
    Returns (ChunkExtractionResponse, tokens_used).
    """
    global total_run_tokens
    client = get_gemini_client()

    prompt = f"""VIDEO METADATA:
- Title: {video_title}
- Channel / Show: {channel_name}
- Chunk Time Range: {chunk['start_timestamp']} to {chunk['end_timestamp']}

TRANSCRIPT TEXT WITH TIMESTAMPS:
{chunk['formatted_text']}

TASK:
Analyze the transcript above and extract any verbatim quotes meeting our comedy craft criteria.
"""

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=[EXTRACTION_SYSTEM_PROMPT, prompt],
            config={
                "response_mime_type": "application/json",
                "response_schema": ChunkExtractionResponse,
                "temperature": 0.2,
            }
        )

        tokens_used = 0
        if hasattr(response, "usage_metadata") and response.usage_metadata:
            tokens_used = response.usage_metadata.total_token_count or 0

        total_run_tokens += tokens_used

        parsed = ChunkExtractionResponse.model_validate_json(response.text)
        logger.info(
            f"Chunk {chunk['chunk_index']}: extracted {len(parsed.quotes)} quotes "
            f"({tokens_used} tokens, run total: {total_run_tokens}/{MAX_TOTAL_TOKENS_PER_RUN})"
        )
        return parsed, tokens_used
    except Exception as e:
        logger.error(f"Error during Gemini extraction on chunk {chunk['chunk_index']}: {e}")
        return ChunkExtractionResponse(comedian="Unknown", host="Unknown", quotes=[]), 0


def clean_text_for_matching(text: str) -> str:
    """Normalizes text for fuzzy/verbatim verification."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join(text.split())


def verify_and_enrich_quotes(
    quotes: List[CraftQuote],
    video_id: str,
    raw_transcript_text: str
) -> List[dict]:
    """
    Validates verbatim fidelity against the source transcript and adds deep links.
    Returns enriched quote dictionaries.
    """
    normalized_source = clean_text_for_matching(raw_transcript_text)
    enriched = []

    for q in quotes:
        start_sec = max(0, int(q.start_seconds))
        end_sec = max(start_sec, int(q.end_seconds))
        youtube_deep_link = f"https://youtu.be/{video_id}?t={start_sec}"

        # Verification check
        normalized_quote = clean_text_for_matching(q.verbatim_quote)
        is_verified = normalized_quote in normalized_source

        enriched.append({
            "theme": q.theme,
            "topic": q.topic,
            "speaker": q.speaker,
            "setup_context": q.setup_context,
            "start_seconds": start_sec,
            "end_seconds": end_sec,
            "start_timestamp": format_seconds(start_sec),
            "end_timestamp": format_seconds(end_sec),
            "youtube_link": youtube_deep_link,
            "verbatim_quote": q.verbatim_quote,
            "tactical_takeaway": q.tactical_takeaway,
            "is_verified_verbatim": is_verified
        })

    return enriched


def extract_video_craft_insights(
    video_id: str,
    video_title: str,
    channel_name: str,
    chunks: List[dict],
    model_name: str = DEFAULT_MODEL,
    start_chunk: int = 0,
    max_consecutive_empty: int = MAX_CONSECUTIVE_EMPTY_CHUNKS
) -> Tuple[dict, str]:
    """
    Extracts craft quotes across all chunks of a video and combines them.
    Applies token-guard circuit breaker, consecutive empty exit, and zero-token pre-filter.
    Returns (extracted_data_dict, exit_status_string).
    exit_status_string can be "COMPLETED", "EARLY_EXIT", or "STOP_BUDGET_REACHED".
    """
    global total_run_tokens
    all_quotes = []
    primary_comedian = ""
    primary_host = ""
    consecutive_empty = 0
    exit_status = "COMPLETED"

    full_transcript_text = "\n".join(c["formatted_text"] for c in chunks)
    target_chunks = chunks[start_chunk:]
    if start_chunk > 0:
        logger.info(f"Jumping to start_chunk={start_chunk} (evaluating chunks {start_chunk} to {len(chunks)-1})")

    for idx, chunk in enumerate(target_chunks, start=start_chunk):
        # 1. Hard Budget Check
        if total_run_tokens >= MAX_TOTAL_TOKENS_PER_RUN:
            logger.warning(
                f"🛑 [CIRCUIT BREAKER] Hit budget ceiling ({total_run_tokens}/{MAX_TOTAL_TOKENS_PER_RUN} tokens). Halting run."
            )
            exit_status = "STOP_BUDGET_REACHED"
            break

        # 2. Consecutive Miss Stop
        if consecutive_empty >= max_consecutive_empty:
            logger.info(
                f"⏩ [EARLY EXIT] {consecutive_empty} consecutive chunks had no craft content. Skipping rest of {video_id}."
            )
            exit_status = "EARLY_EXIT"
            break

        # 3. Zero-Token Local Pre-Filter
        if not pre_filter_chunk(chunk["formatted_text"]):
            logger.info(
                f"⏭️ Skipping chunk {idx + 1}/{len(chunks)}: No comedy craft keywords detected (0 tokens used)."
            )
            consecutive_empty += 1
            continue

        # 4. LLM Call
        res, _ = extract_quotes_from_chunk(chunk, video_id, video_title, channel_name, model_name=model_name)
        if res.comedian and res.comedian.lower() not in ("unknown", ""):
            primary_comedian = res.comedian
        if res.host and res.host.lower() not in ("unknown", ""):
            primary_host = res.host

        if not res.quotes:
            consecutive_empty += 1
        else:
            consecutive_empty = 0
            enriched_quotes = verify_and_enrich_quotes(res.quotes, video_id, full_transcript_text)
            all_quotes.extend(enriched_quotes)

    # Fallback comedian/host heuristics from title/channel if empty
    if not primary_comedian or primary_comedian.lower() == "unknown":
        primary_comedian = video_title.split(":")[0].split("-")[0].strip()
    if not primary_host or primary_host.lower() == "unknown":
        primary_host = channel_name

    data = {
        "video_id": video_id,
        "title": video_title,
        "channel": channel_name,
        "comedian": primary_comedian,
        "host": primary_host,
        "quotes": all_quotes,
        "exit_status": exit_status,
        "total_run_tokens": total_run_tokens
    }

    return data, exit_status
