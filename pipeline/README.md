# 🎙️ Stand-Up Comedy Research Pipeline

An automated research pipeline in Python that discovers comedy podcasts on YouTube, fetches their transcripts with timestamps, and extracts verbatim quotes on stand-up comedy craft into structured Markdown files.

---

## 📁 Architecture & File Layout

```
ComedyOS-2026/
├── pipeline/
│   ├── config.py           # Core settings, queries, craft themes, and thresholds
│   ├── discovery.py        # yt-dlp discovery, clip & duration filtering, queue.json
│   ├── transcribe.py       # youtube-transcript-api timestamped chunking (4k-6k words)
│   ├── extractor.py        # Gemini structured output (verbatim quotes, theme validation)
│   ├── vault.py            # Markdown vault creator and cumulative index builder
│   ├── run_pipeline.py     # Main CLI orchestrator
│   └── README.md           # Documentation & operational guide
├── queue.json              # State machine & deduplication tracker
└── output/
    ├── quotes/             # Individual markdown vault files per episode/clip
    └── index.md            # Cumulative craft knowledge base index categorized by theme
```

---

## 🚀 Quick Start & CLI Usage

### 1. Run the Full Automated Pipeline
Discovers new podcast episodes from target channels/queries, fetches transcripts, extracts quotes, and updates the cumulative index:
```bash
python pipeline/run_pipeline.py --all
```

### 2. Discover Videos Only
Searches YouTube across default queries or a custom query and updates `queue.json` without processing:
```bash
# Default channels/queries (limit 5 per query)
python pipeline/run_pipeline.py --discover

# Custom query with higher limit
python pipeline/run_pipeline.py --discover --query "Louis CK writing process" --max-discover 10
```

### 3. Process Pending Queue Items
Processes pending candidates in batches:
```bash
# Process next 3 pending videos in queue
python pipeline/run_pipeline.py --extract --limit 3
```

### 4. Process Any Single YouTube Video Directly
Instantly runs transcription, extraction, vault generation, and indexing for any URL or video ID:
```bash
python pipeline/run_pipeline.py --url "https://www.youtube.com/watch?v=LVEFC0dxX_I"
```

### 5. Export to CSV & Sync to Google Sheets
Exports all extracted quotes to CSV/JSON and syncs directly into the connected Google Sheet:
```bash
# Export local CSV and JSON
python pipeline/export_sheets.py

# Sync directly to Google Sheet
python pipeline/export_sheets.py --sync
```

---

## 🛡️ Token-Guard Circuit Breakers & Pre-Filtering

To guarantee budget safety and eliminate wasted API spend on rambling banter:
1. **Zero-Token Local Pre-Filter:** `pre_filter_chunk()` scans transcript blocks locally. If a chunk doesn't contain at least 2 terms from `COMEDY_CRAFT_LEXICON` (e.g., *premise, punchline, bomb, heckler, delivery, tight five*), it is skipped with **0 tokens consumed**.
2. **Consecutive Miss Early-Exit:** If 3 consecutive chunks in an episode contain no comedy craft quotes or fail pre-filtering, the pipeline bails early on the remainder of that episode.
3. **Hard Token Budget Ceiling:** Tracks cumulative `response.usage_metadata.total_token_count` across the run. If `MAX_TOTAL_TOKENS_PER_RUN` (250,000 tokens) is reached, execution halts gracefully. The currently interrupted video and remaining uncompleted videos remain safely flagged as `pending` in `queue.json`.
4. **Max Chunks Ceiling:** Videos are capped at a maximum of 8 chunks (~40k words) to avoid unbounded processing on 4+ hour marathon streams.

---

## 🎯 Extraction Themes

The extraction layer enforces 5 strict stand-up comedy craft themes:
1. **📝 Writing & Joke Construction:** Premise generation, tags, punchlines, editing, notebooks, callbacks.
2. **🎤 Performance & Stagecraft:** Microphones, stage movement, crowd dynamics, delivery, timing, pauses.
3. **🧠 Mental Attitudes:** Psychology, handling self-doubt/imposter syndrome, ego vs humility.
4. **💥 Overcoming Bombs/Blocks:** Surviving quiet rooms, bombing, handling hecklers, writer's block.
5. **🛠️ Professional Problem-Solving:** Specials, touring, industry navigation, club sets.

---

## 🔗 YouTube Deep Links & Verbatim Fidelity
* Every quote is extracted **100% verbatim** from the transcript with no paraphrasing or grammar smoothing.
* Exact start and end seconds are mapped directly into clickable YouTube deep links:
  `https://youtu.be/{video_id}?t={start_seconds}`
* All extracted quotes are indexed cumulatively into `output/index.md`.
