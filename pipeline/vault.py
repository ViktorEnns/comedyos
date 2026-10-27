import re
import sys
import logging
from pathlib import Path
from typing import List, Dict, Optional

# Allow running directly or as module
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.config import OUTPUT_DIR, INDEX_FILE, THEMES

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("vault")

THEME_ICONS = {
    "Writing & Joke Construction": "📝",
    "Performance & Stagecraft": "🎤",
    "Mental Attitudes": "🧠",
    "Overcoming Bombs/Blocks": "💥",
    "Professional Problem-Solving": "🛠️"
}


def sanitize_filename(name: str) -> str:
    """Creates a clean, safe filename slug."""
    s = re.sub(r"[^\w\s-]", "", name).strip().lower()
    return re.sub(r"[-\s]+", "_", s)


def taggify_theme(theme: str) -> str:
    """Converts a theme string to a clean tag."""
    return re.sub(r"[^\w]+", "-", theme.lower()).strip("-")


def write_video_vault_file(extracted_data: dict, upload_date: str = "") -> Path:
    """
    Writes a Markdown vault file for an extracted video:
    output/quotes/{comedian_or_show}_{video_id}.md
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    video_id = extracted_data["video_id"]
    title = extracted_data.get("title", "Untitled")
    comedian = extracted_data.get("comedian", "Unknown Comedian")
    host = extracted_data.get("host", "Unknown Host")
    channel = extracted_data.get("channel", "Unknown Channel")
    quotes = extracted_data.get("quotes", [])
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    # Generate slug from comedian or channel
    slug_source = comedian if comedian and comedian.lower() != "unknown" else channel
    safe_slug = sanitize_filename(slug_source)
    filename = f"{safe_slug}_{video_id}.md"
    file_path = OUTPUT_DIR / filename

    # Unique tags based on themes present in quotes
    themes_present = list(dict.fromkeys(q["theme"] for q in quotes))
    tags = [taggify_theme(t) for t in themes_present] + ["comedy-craft", "standup"]

    # Build YAML frontmatter
    date_val = upload_date if upload_date else "Unknown"
    frontmatter_lines = [
        "---",
        f'title: "{title.replace('"', '\\"')}"',
        f'date: "{date_val}"',
        f'youtube_url: "{youtube_url}"',
        f'comedian: "{comedian.replace('"', '\\"')}"',
        f'host: "{host.replace('"', '\\"')}"',
        f'channel: "{channel.replace('"', '\\"')}"',
        f'video_id: "{video_id}"',
        "tags:"
    ]
    for tag in tags:
        frontmatter_lines.append(f'  - "{tag}"')
    frontmatter_lines.append("---")
    frontmatter_lines.append("")

    # Markdown body
    body_lines = [
        f"# {title}",
        "",
        f"- **Channel / Show:** {channel}",
        f"- **Comedian:** {comedian} | **Host:** {host}",
        f"- **Source URL:** [{youtube_url}]({youtube_url})",
        "",
        "---",
        "",
        "## Extracted Craft Quotes",
        ""
    ]

    if not quotes:
        body_lines.append("*No direct stand-up comedy craft quotes met the strict extraction criteria in this video.*")
    else:
        for idx, q in enumerate(quotes, 1):
            icon = THEME_ICONS.get(q["theme"], "💡")
            topic_clean = q.get("topic", "Craft Insight")
            anchor_id = f"quote-{idx}"

            body_lines.extend([
                f'<a id="{anchor_id}"></a>',
                f"### {idx}. {icon} [{q['theme']}] {topic_clean}",
                "",
                f"- **Speaker:** {q['speaker']}",
                f"- **Timecode:** `{q['start_timestamp']} - {q['end_timestamp']}`",
                f"- **YouTube Deep Link:** [{q['start_timestamp']}]({q['youtube_link']})",
                f"- **Context:** {q['setup_context']}",
                "",
                "#### Verbatim Quote",
                f'> "{q["verbatim_quote"]}"',
                "",
                "#### Tactical Takeaway",
                f"{q['tactical_takeaway']}",
                "",
                "---",
                ""
            ])

    content = "\n".join(frontmatter_lines) + "\n".join(body_lines)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    logger.info(f"Wrote vault file: {file_path} ({len(quotes)} quotes)")
    return file_path


def parse_vault_file_for_index(md_path: Path) -> List[dict]:
    """Parses a generated quote file to collect quote entries for the cumulative index."""
    try:
        content = md_path.read_text(encoding="utf-8")
    except Exception as e:
        logger.error(f"Failed to read {md_path}: e")
        return []

    # Extract title from frontmatter or heading
    title_match = re.search(r'title:\s*"([^"]+)"', content)
    title = title_match.group(1) if title_match else md_path.stem

    comedian_match = re.search(r'comedian:\s*"([^"]+)"', content)
    comedian = comedian_match.group(1) if comedian_match else "Unknown"

    rel_file = f"quotes/{md_path.name}"

    # Extract quotes
    quote_entries = []
    # Pattern to match each quote header
    # e.g.: ### 1. 📝 [Writing & Joke Construction] Topic
    quote_blocks = re.findall(
        r'<a id="(quote-\d+)"></a>\s*###\s*\d+\.\s*[^\s]+\s*\[(.*?)\]\s*(.*?)\n'
        r'.*?- \*\*Speaker:\*\*\s*(.*?)\n'
        r'.*?- \*\*Timecode:\*\*\s*`(.*?)`\n'
        r'.*?- \*\*YouTube Deep Link:\*\*\s*\[(.*?)\]\((.*?)\)\n'
        r'.*?#### Tactical Takeaway\s*\n(.*?)(?=\n---|'
        r'\Z)',
        content,
        re.DOTALL
    )

    for block in quote_blocks:
        anchor_id, theme, topic, speaker, timecode, start_ts, yt_link, takeaway = block
        quote_entries.append({
            "theme": theme.strip(),
            "topic": topic.strip(),
            "speaker": speaker.strip(),
            "timecode": timecode.strip(),
            "start_timestamp": start_ts.strip(),
            "youtube_link": yt_link.strip(),
            "takeaway": takeaway.strip(),
            "file_link": f"{rel_file}#{anchor_id}",
            "source_title": title,
            "comedian": comedian
        })

    return quote_entries


def update_cumulative_index() -> Path:
    """
    Scans all files in output/quotes and builds the categorized cumulative index in output/index.md.
    """
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    all_quotes = []

    if OUTPUT_DIR.exists():
        for md_file in sorted(OUTPUT_DIR.glob("*.md")):
            all_quotes.extend(parse_vault_file_for_index(md_file))

    # Group by theme
    by_theme: Dict[str, List[dict]] = {theme: [] for theme in THEMES}
    for q in all_quotes:
        th = q.get("theme", "")
        if th in by_theme:
            by_theme[th].append(q)
        else:
            by_theme.setdefault(th, []).append(q)

    # Build index content
    lines = [
        "# 🎙️ Stand-Up Comedy Craft Knowledge Base",
        "",
        "> Automated research archive of verbatim quotes, lessons, and tactical takeaways on stand-up comedy craft from top comedy podcasts.",
        "",
        f"**Total Indexed Quotes:** {len(all_quotes)} | **Total Episodes:** {len(list(OUTPUT_DIR.glob('*.md')) if OUTPUT_DIR.exists() else 0)}",
        "",
        "## Table of Contents",
        ""
    ]

    for theme in THEMES:
        icon = THEME_ICONS.get(theme, "📌")
        count = len(by_theme.get(theme, []))
        anchor = re.sub(r"[^\w]+", "-", theme.lower()).strip("-")
        lines.append(f"- [{icon} {theme}](#{anchor}) ({count})")

    lines.append("\n---\n")

    for theme in THEMES:
        icon = THEME_ICONS.get(theme, "📌")
        quotes_in_theme = by_theme.get(theme, [])
        lines.append(f"## {icon} {theme}")
        lines.append("")

        if not quotes_in_theme:
            lines.append(f"*No quotes indexed for this theme yet.*")
            lines.append("")
            continue

        for q in quotes_in_theme:
            lines.append(
                f"- **[{q['topic']}]({q['file_link']})** — *{q['speaker']}* "
                f"(`{q['start_timestamp']}` [Watch on YouTube]({q['youtube_link']}))"
            )
            lines.append(f"  - 💡 **Takeaway:** {q['takeaway']}")
            lines.append("")

        lines.append("")

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    logger.info(f"Updated cumulative index at {INDEX_FILE} with {len(all_quotes)} quotes across {len(THEMES)} themes.")
    return INDEX_FILE


if __name__ == "__main__":
    update_cumulative_index()
