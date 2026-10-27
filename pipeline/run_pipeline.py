import os
import sys
import argparse
import logging
from pathlib import Path
from typing import Optional, List

# Allow running directly or as module
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from pipeline.config import DEFAULT_MODEL, QUEUE_FILE
from pipeline.discovery import discover_videos, load_queue, save_queue
from pipeline.transcribe import get_video_chunks
from pipeline.extractor import extract_video_craft_insights
from pipeline.vault import write_video_vault_file, update_cumulative_index

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("pipeline")


def extract_video_id_from_url(url_or_id: str) -> str:
    """Extracts 11-char YouTube video ID from various URL formats or raw ID."""
    if len(url_or_id) == 11 and not ("/" in url_or_id or "?" in url_or_id):
        return url_or_id
    import re
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url_or_id)
    if match:
        return match.group(1)
    return url_or_id


def fetch_single_video_metadata(video_id: str) -> dict:
    """Retrieves metadata for a single video using yt-dlp."""
    import yt_dlp
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "nocheckcertificate": True,
        "ignoreerrors": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            if info:
                return {
                    "title": info.get("title") or f"YouTube Video {video_id}",
                    "channel": info.get("channel") or info.get("uploader") or "YouTube",
                    "upload_date": info.get("upload_date") or ""
                }
        except Exception as e:
            logger.warning(f"Could not fetch full metadata for {video_id}: {e}")
    return {"title": f"YouTube Video {video_id}", "channel": "YouTube", "upload_date": ""}


def process_single_video(
    video_id: str,
    title: Optional[str] = None,
    channel: Optional[str] = None,
    upload_date: Optional[str] = None,
    model_name: str = DEFAULT_MODEL,
    start_chunk: int = 0,
    max_consecutive_empty: Optional[int] = None
) -> bool:
    """
    Runs end-to-end processing for a single video:
    1. Transcribe & chunk
    2. Extract craft quotes with Gemini
    3. Save Markdown vault file
    4. Update cumulative index
    """
    if not title or title.startswith("YouTube Video"):
        meta = fetch_single_video_metadata(video_id)
        title = meta["title"]
        channel = channel or meta["channel"]
        upload_date = upload_date or meta["upload_date"]

    logger.info(f"Processing video [{video_id}]: '{title}' ({channel})")

    chunks = get_video_chunks(video_id)
    if not chunks:
        logger.warning(f"No transcript available for video {video_id}. Skipping.")
        return False

    kwargs = {}
    if max_consecutive_empty is not None:
        kwargs["max_consecutive_empty"] = max_consecutive_empty

    extracted_data, exit_status = extract_video_craft_insights(
        video_id=video_id,
        video_title=title,
        channel_name=channel or "YouTube",
        chunks=chunks,
        model_name=model_name,
        start_chunk=start_chunk,
        **kwargs
    )

    vault_path = write_video_vault_file(extracted_data, upload_date=upload_date or "")
    update_cumulative_index()
    logger.info(f"Processed video {video_id} -> {vault_path.name} (status: {exit_status})")
    return exit_status != "STOP_BUDGET_REACHED"


def run_queue_processing(
    limit: Optional[int] = None,
    filter_keyword: Optional[str] = None,
    model_name: str = DEFAULT_MODEL,
    start_chunk: int = 0,
    max_consecutive_empty: Optional[int] = None
) -> None:
    """
    Processes pending items from queue.json.
    Halts gracefully if the token budget ceiling is reached, leaving uncompleted videos pending.
    """
    queue = load_queue()
    pending_items = [item for item in queue.values() if item.get("status") == "pending"]

    if filter_keyword:
        keywords = [k.strip().lower() for k in filter_keyword.split(",") if k.strip()]
        pending_items = [
            item for item in pending_items
            if any(
                k in item.get("title", "").lower()
                or k in item.get("query_source", "").lower()
                or k in item.get("channel", "").lower()
                for k in keywords
            )
        ]
        logger.info(f"Filtered pending items by '{filter_keyword}': {len(pending_items)} matching items.")
    else:
        logger.info(f"Found {len(pending_items)} pending items in queue.")

    if not pending_items:
        return

    if limit is not None:
        pending_items = pending_items[:limit]
        logger.info(f"Processing up to {limit} items in this batch.")

    kwargs = {}
    if max_consecutive_empty is not None:
        kwargs["max_consecutive_empty"] = max_consecutive_empty

    processed_count = 0
    for item in pending_items:
        vid_id = item["video_id"]
        title = item.get("title", "Unknown Title")
        channel = item.get("channel", "Unknown Channel")
        upload_date = item.get("upload_date", "")

        try:
            chunks = get_video_chunks(vid_id)
            if not chunks:
                item["status"] = "skipped_no_transcript"
                save_queue(queue)
                continue

            extracted_data, exit_status = extract_video_craft_insights(
                video_id=vid_id,
                video_title=title,
                channel_name=channel,
                chunks=chunks,
                model_name=model_name,
                start_chunk=start_chunk,
                **kwargs
            )

            # Check if token budget ceiling stopped the run
            if exit_status == "STOP_BUDGET_REACHED":
                logger.warning(
                    f"🛑 [CIRCUIT BREAKER] Token budget ceiling reached while processing {vid_id}. "
                    f"Leaving {vid_id} and remaining videos as 'pending'."
                )
                item["status"] = "pending"
                save_queue(queue)
                break

            write_video_vault_file(extracted_data, upload_date=upload_date)
            item["status"] = "completed"
            item["extracted_quotes_count"] = len(extracted_data.get("quotes", []))
            item["exit_status"] = exit_status
            save_queue(queue)
            processed_count += 1
        except Exception as e:
            logger.error(f"Failed processing video {vid_id}: {e}")
            item["status"] = "failed"
            item["error"] = str(e)
            save_queue(queue)

    if processed_count > 0:
        update_cumulative_index()
    logger.info(f"Finished batch. Successfully processed {processed_count} videos.")


def main():
    parser = argparse.ArgumentParser(description="Automated Comedy Podcast Research Pipeline")
    parser.add_argument("--all", action="store_true", help="Run full pipeline: discover, transcribe, extract, and index")
    parser.add_argument("--discover", action="store_true", help="Run discovery and update queue.json only")
    parser.add_argument("--extract", action="store_true", help="Process pending items in queue.json")
    parser.add_argument("--url", type=str, help="Process a single YouTube video URL or ID directly")
    parser.add_argument("--query", type=str, help="Custom search query for discovery")
    parser.add_argument("--filter", type=str, help="Filter pending queue items by keywords (e.g. 'Jimmy Carr,Kevin Smith')")
    parser.add_argument("--limit", type=int, help="Limit number of videos to process in this run")
    parser.add_argument("--max-discover", type=int, default=5, help="Max candidates per query to discover (default: 5)")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"Gemini model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--start-chunk", type=int, default=0, help="Chunk index to start extraction from (default: 0)")
    parser.add_argument("--consecutive-empty", type=int, default=None, help="Override consecutive empty chunks limit (default: 3)")

    args = parser.parse_args()

    # Case 1: Single URL
    if args.url:
        vid_id = extract_video_id_from_url(args.url)
        process_single_video(
            video_id=vid_id,
            model_name=args.model,
            start_chunk=args.start_chunk,
            max_consecutive_empty=args.consecutive_empty
        )
        return

    # Case 2: Discover only
    if args.discover:
        q_list = [args.query] if args.query else None
        discover_videos(queries=q_list, max_per_query=args.max_discover)
        return

    # Case 3: Extract queue only
    if args.extract:
        run_queue_processing(
            limit=args.limit,
            filter_keyword=args.filter,
            model_name=args.model,
            start_chunk=args.start_chunk,
            max_consecutive_empty=args.consecutive_empty
        )
        return

    # Case 4: Full pass (--all or default)
    if args.all or (not args.discover and not args.extract and not args.url):
        logger.info("Starting full pipeline run...")
        q_list = [args.query] if args.query else None
        discover_videos(queries=q_list, max_per_query=args.max_discover)
        run_queue_processing(
            limit=args.limit,
            filter_keyword=args.filter or args.query,
            model_name=args.model,
            start_chunk=args.start_chunk,
            max_consecutive_empty=args.consecutive_empty
        )


if __name__ == "__main__":
    main()
