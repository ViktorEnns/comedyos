---
id: LAYER-BRIDGE-030
title: The Comparator Bridge (The Secret Sauce)
type: architecture-layer
status: active
tags: [comedy-os, comparator, diff-engine, core-differentiator, stage-vs-script]
---

# ⚡ The Comparator Bridge (The Secret Sauce)

> **The Missing Link in Comedy Tech:** Comedians write sets in text apps, record audio on voice memos, and have to manually toggle between the two to learn anything. The Comparator Bridge automatically diffs **what you planned to say** against **what you actually said on stage**.

```mermaid
graph LR
    Written[📝 Written Script & Tags<br/>from Text-Forward Pad] --> Align[⚡ Comparator Engine<br/>Levenshtein + LLM Semantic Match]
    Audio[🎙️ Live Spoken Set Transcript<br/>from Audio Ingestion] --> Align
    Wave[🔊 Acoustic Reaction Waveform<br/>from Crowd Isolation] --> Align

    Align --> Diff[1. Visual Script Diff<br/><i>Green ad-libs, Red forgotten lines</i>]
    Align --> Drops[2. Dropped Tag Alerts<br/><i>Unsaid punchlines & skipped callbacks</i>]
    Align --> Heatmap[3. Reaction Alignment Heatmap<br/><i>Exact seconds of laughter per joke</i>]
```

## 1. Engine Capabilities
1. **Sequence Alignment:** Dynamic programming algorithm aligns transcript phrases with written script notes even if the comic reordered bits on the fly.
2. **Ad-Lib Harvesting:** Automatically flags onstage riffs (green words) so brilliant improvised jokes are never forgotten.
3. **Dropped Premise Recovery:** Marks written jokes that were cut or forgotten under stage pressure (red strikethrough).

## 2. Core Modules
- [[31_Visual_Diff_Report|3.1 Visual Diff Report (Ad-Libs vs Written Script)]]
- [[32_Dropped_Tag_Alerts|3.2 Dropped Tag Alerts & Forgotten Setup Engine]]
- [[33_Reaction_Waveform_Alignment|3.3 Reaction Alignment (Laugh Spikes vs Spoken Words)]]
