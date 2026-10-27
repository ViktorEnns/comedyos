import json
import logging
from datetime import datetime
from typing import List, Dict, Optional
import yt_dlp

from pipeline.config import (
    QUEUE_FILE,
    DEFAULT_QUERIES,
    MIN_FULL_EPISODE_DURATION,
    CRAFT_KEYWORDS
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("discovery")


def load_queue() -> Dict[str, dict]:
    """Loads existing queue from queue.json. Returns dict keyed by video_id."""
    if not QUEUE_FILE.exists():
        return {}
    try:
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return {item["video_id"]: item for item in data if "video_id" in item}
            elif isinstance(data, dict):
                return data
            return {}
    except Exception as e:
        logger.error(f"Failed to read {QUEUE_FILE}: {e}")
        return {}


def save_queue(queue: Dict[str, dict]) -> None:
    """Saves queue to queue.json."""
    QUEUE_FILE.parent.mkdir(parents=True, exist_ok=True)
    temp_file = QUEUE_FILE.with_suffix(".tmp")
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(list(queue.values()), f, indent=2, ensure_ascii=False)
    temp_file.replace(QUEUE_FILE)


def matches_craft_criteria(title: str, description: str = "") -> bool:
    """Checks whether the title or description discusses the comedy craft process."""
    combined = f"{title.lower()} {description.lower()}"
    return any(keyword in combined for keyword in CRAFT_KEYWORDS)


def is_candidate_video(entry: dict) -> bool:
    """
    Evaluates whether a video meets discovery criteria:
    - Videos >= 25 mins (full episodes)
    - Shorter clips (<25 mins) if they match craft keywords in title/description
    """
    title = entry.get("title") or ""
    duration = entry.get("duration")

    # Long-form episodes (>= 25 min)
    if duration is not None and duration >= MIN_FULL_EPISODE_DURATION:
        return True

    # Shorter clips (< 25 min or unknown duration) matching craft keywords
    if matches_craft_criteria(title):
        return True

    return False


def search_youtube_query(query: str, max_results: int = 10) -> List[dict]:
    """Uses yt-dlp to search YouTube and retrieve metadata without downloading."""
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
        "nocheckcertificate": True,
        "ignoreerrors": True,
        "no_warnings": True,
    }

    search_term = f"ytsearch{max_results}:{query}"
    logger.info(f"Searching YouTube: '{query}' (limit: {max_results})")

    candidates = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(search_term, download=False)
            if not result or "entries" not in result:
                return candidates

            for entry in result["entries"]:
                if not entry or not entry.get("id"):
                    continue

                if is_candidate_video(entry):
                    video_id = entry["id"]
                    url = entry.get("url") or f"https://www.youtube.com/watch?v={video_id}"
                    if not url.startswith("http"):
                        url = f"https://www.youtube.com/watch?v={video_id}"

                    candidates.append({
                        "video_id": video_id,
                        "title": entry.get("title", "Unknown Title"),
                        "url": url,
                        "channel": entry.get("channel") or entry.get("uploader", "Unknown Channel"),
                        "upload_date": entry.get("upload_date") or "",
                        "duration": entry.get("duration"),
                        "query_source": query,
                        "status": "pending",
                        "discovered_at": datetime.now().isoformat()
                    })
        except Exception as e:
            logger.error(f"Error during search for query '{query}': {e}")

    return candidates


def discover_videos(queries: Optional[List[str]] = None, max_per_query: int = 10) -> int:
    """
    Runs discovery across queries and updates queue.json.
    Returns the count of newly discovered candidates added.
    """
    queries = queries or DEFAULT_QUERIES
    queue = load_queue()
    initial_count = len(queue)
    newly_added = 0

    for query in queries:
        candidates = search_youtube_query(query, max_results=max_per_query)
        for item in candidates:
            vid_id = item["video_id"]
            if vid_id not in queue:
                queue[vid_id] = item
                newly_added += 1
                logger.info(f"Queued new candidate [{vid_id}]: {item['title']} ({item.get('duration')}s)")
            else:
                logger.debug(f"Already in queue: {vid_id}")

    if newly_added > 0:
        save_queue(queue)
        logger.info(f"Saved {newly_added} new candidates to queue. Total candidates: {len(queue)}")
    else:
        logger.info(f"No new candidates found. Total candidates: {len(queue)}")

    return newly_added


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="YouTube Comedy Podcast Discovery")
    parser.add_argument("--query", type=str, help="Single query to discover")
    parser.add_argument("--max", type=int, default=5, help="Max results per query")
    args = parser.parse_args()

    q_list = [args.query] if args.query else DEFAULT_QUERIES
    discover_videos(q_list, max_per_query=args.max)
