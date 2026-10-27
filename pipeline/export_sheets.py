import csv
import json
import logging
import re
import sys
from pathlib import Path

# Base paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from pipeline.config import OUTPUT_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("export_sheets")

CSV_OUTPUT_PATH = PROJECT_ROOT / "output" / "standup_craft_quotes.csv"
JSON_OUTPUT_PATH = PROJECT_ROOT / "output" / "standup_craft_quotes.json"


def parse_all_quote_files() -> list[dict]:
    """Scans all Markdown vault files in output/quotes and extracts structured quote rows."""
    if not OUTPUT_DIR.exists():
        return []

    records = []
    for md_file in sorted(OUTPUT_DIR.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")

        # Parse frontmatter
        title_m = re.search(r'title:\s*"([^"]+)"', content)
        title = title_m.group(1) if title_m else md_file.stem

        date_m = re.search(r'date:\s*"([^"]+)"', content)
        date = date_m.group(1) if date_m else ""

        comedian_m = re.search(r'comedian:\s*"([^"]+)"', content)
        comedian = comedian_m.group(1) if comedian_m else ""

        host_m = re.search(r'host:\s*"([^"]+)"', content)
        host = host_m.group(1) if host_m else ""

        channel_m = re.search(r'channel:\s*"([^"]+)"', content)
        channel = channel_m.group(1) if channel_m else ""

        video_id_m = re.search(r'video_id:\s*"([^"]+)"', content)
        video_id = video_id_m.group(1) if video_id_m else ""

        # Extract quote blocks
        quote_blocks = re.findall(
            r'<a id="(quote-\d+)"></a>\s*###\s*\d+\.\s*[^\s]+\s*\[(.*?)\]\s*(.*?)\n'
            r'.*?- \*\*Speaker:\*\*\s*(.*?)\n'
            r'.*?- \*\*Timecode:\*\*\s*`(.*?)`\n'
            r'.*?- \*\*YouTube Deep Link:\*\*\s*\[(.*?)\]\((.*?)\)\n'
            r'(?:.*?- \*\*Context:\*\*\s*(.*?)\n)?'
            r'.*?#### Verbatim Quote\s*\n>\s*"?(.*?)"?\n'
            r'.*?#### Tactical Takeaway\s*\n(.*?)(?=\n---|'
            r'\Z)',
            content,
            re.DOTALL
        )

        for block in quote_blocks:
            anchor_id, theme, topic, speaker, timecode, start_ts, yt_link, context, quote, takeaway = block

            # Compute start seconds
            start_sec = ""
            if "t=" in yt_link:
                start_sec = yt_link.split("t=")[-1]

            records.append({
                "Theme": theme.strip(),
                "Topic": topic.strip(),
                "Speaker": speaker.strip(),
                "Comedian": comedian.strip(),
                "Host": host.strip(),
                "Channel / Show": channel.strip(),
                "Timecode": timecode.strip(),
                "Start Seconds": start_sec,
                "YouTube Deep Link": yt_link.strip(),
                "Context": (context or "").strip(),
                "Verbatim Quote": quote.strip().replace('"', '""'),
                "Tactical Takeaway": takeaway.strip(),
                "Video Title": title.strip(),
                "Upload Date": date.strip(),
                "Video ID": video_id.strip()
            })

    return records


def export_data():
    records = parse_all_quote_files()
    if not records:
        logger.warning("No quotes found to export.")
        return None

    # Write CSV
    headers = [
        "Theme",
        "Topic",
        "Speaker",
        "Comedian",
        "Host",
        "Channel / Show",
        "Timecode",
        "Start Seconds",
        "YouTube Deep Link",
        "Context",
        "Verbatim Quote",
        "Tactical Takeaway",
        "Video Title",
        "Upload Date",
        "Video ID"
    ]

    CSV_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_OUTPUT_PATH, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(records)

    with open(JSON_OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    logger.info(f"Exported {len(records)} quotes to {CSV_OUTPUT_PATH} and {JSON_OUTPUT_PATH}")
    return records


def sync_to_google_sheet(spreadsheet_id: str = None) -> bool:
    """Exports CSV and syncs the data into the connected Google Sheet."""
    import subprocess
    from pipeline.config import SPREADSHEET_ID

    sid = spreadsheet_id or SPREADSHEET_ID
    if not sid:
        logger.error("No SPREADSHEET_ID configured.")
        return False

    records = export_data()
    if not records:
        logger.warning("No records to sync.")
        return False

    try:
        cmd = f'gsheets mutate import-csv {sid} "{CSV_OUTPUT_PATH}" --sheet "Sheet1"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if res.returncode == 0:
            logger.info(f"Successfully synced {len(records)} quotes to Google Sheet ({sid})")
            return True
        else:
            logger.error(f"Failed to sync to Google Sheet: {res.stderr or res.stdout}")
            return False
    except Exception as e:
        logger.error(f"Exception during Google Sheet sync: {e}")
        return False


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Export quotes to CSV/JSON and Google Sheets")
    parser.add_argument("--sync", action="store_true", help="Sync exported CSV into Google Sheet")
    parser.add_argument("--sheet-id", type=str, help="Target Google Spreadsheet ID")
    args = parser.parse_args()

    if args.sync:
        sync_to_google_sheet(args.sheet_id)
    else:
        export_data()

