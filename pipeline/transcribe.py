import logging
import math
from typing import List, Dict, Optional, Tuple
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    CouldNotRetrieveTranscript
)

from pipeline.config import CHUNK_MIN_WORDS, CHUNK_MAX_WORDS, MAX_CHUNKS_PER_VIDEO

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("transcribe")


def format_seconds(seconds: float) -> str:
    """Formats seconds into HH:MM:SS or MM:SS string."""
    sec = int(round(seconds))
    hrs = sec // 3600
    mins = (sec % 3600) // 60
    secs = sec % 60
    if hrs > 0:
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"


def fetch_transcript(video_id: str) -> Optional[List[dict]]:
    """
    Fetches transcript for video_id using YouTubeTranscriptApi.
    Prioritizes manual English, then auto-generated English.
    Returns list of segment dicts: [{'text': str, 'start': float, 'duration': float}],
    or None if unavailable.
    """
    try:
        api = YouTubeTranscriptApi()
        transcript_obj = api.fetch(video_id, languages=["en", "en-US", "en-GB"])
        raw_data = transcript_obj.to_raw_data()
        logger.info(f"Successfully fetched transcript for {video_id} ({len(raw_data)} segments)")
        return raw_data
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        logger.warning(f"No English transcript found for {video_id}: {e}")
        return None
    except CouldNotRetrieveTranscript as e:
        logger.warning(f"Could not retrieve transcript for {video_id}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error retrieving transcript for {video_id}: {e}")
        return None


def chunk_transcript(
    segments: List[dict],
    min_words: int = CHUNK_MIN_WORDS,
    max_words: int = CHUNK_MAX_WORDS
) -> List[dict]:
    """
    Aggregates transcript segments into chunks of approx. 4,000–6,000 words.
    Embeds timestamps at segment boundaries for accurate LLM extraction.
    """
    if not segments:
        return []

    chunks = []
    current_segments = []
    current_words = 0
    chunk_index = 0

    for seg in segments:
        text = seg.get("text", "").strip()
        if not text:
            continue

        words_in_seg = len(text.split())
        current_segments.append(seg)
        current_words += words_in_seg

        # If we exceeded min_words and have reached a natural break or exceeded max_words
        if current_words >= max_words or (current_words >= min_words and text.endswith((".", "!", "?"))):
            chunk = _build_chunk_dict(chunk_index, current_segments, current_words)
            chunks.append(chunk)
            chunk_index += 1
            current_segments = []
            current_words = 0
            if len(chunks) >= MAX_CHUNKS_PER_VIDEO:
                logger.info(f"Reached MAX_CHUNKS_PER_VIDEO ceiling ({MAX_CHUNKS_PER_VIDEO}). Stopping chunking.")
                break

    # Remainder chunk (if under MAX_CHUNKS_PER_VIDEO)
    if current_segments and len(chunks) < MAX_CHUNKS_PER_VIDEO:
        chunk = _build_chunk_dict(chunk_index, current_segments, current_words)
        chunks.append(chunk)

    logger.info(f"Chunked transcript into {len(chunks)} chunks (total words: {sum(c['word_count'] for c in chunks)})")
    return chunks


def _build_chunk_dict(index: int, segments: List[dict], word_count: int) -> dict:
    """Helper to package segments into a chunk dict with timestamped formatted text."""
    start_sec = segments[0]["start"]
    last_seg = segments[-1]
    end_sec = last_seg["start"] + last_seg.get("duration", 0.0)

    # Format text with periodic or per-sentence timestamp markers:
    # e.g., "[00:15:32] Here is the transcript text..."
    formatted_lines = []
    for s in segments:
        timecode = format_seconds(s["start"])
        formatted_lines.append(f"[{timecode}] {s['text']}")

    formatted_text = "\n".join(formatted_lines)

    return {
        "chunk_index": index,
        "start_seconds": start_sec,
        "end_seconds": end_sec,
        "start_timestamp": format_seconds(start_sec),
        "end_timestamp": format_seconds(end_sec),
        "word_count": word_count,
        "formatted_text": formatted_text,
        "raw_segments": segments
    }


def get_video_chunks(video_id: str) -> Optional[List[dict]]:
    """Fetches transcript and chunks it for a given video_id."""
    segments = fetch_transcript(video_id)
    if not segments:
        return None
    return chunk_transcript(segments)


if __name__ == "__main__":
    import sys
    vid = sys.argv[1] if len(sys.argv) > 1 else "1Z3EzFDVcgo"
    chunks = get_video_chunks(vid)
    if chunks:
        print(f"Generated {len(chunks)} chunks for {vid}. Chunk 0 word count: {chunks[0]['word_count']}")
    else:
        print(f"No chunks generated for {vid}")
