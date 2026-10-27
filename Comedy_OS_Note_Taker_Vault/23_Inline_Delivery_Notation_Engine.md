---
id: FEAT-TEXT-023
title: Inline Delivery Notation Engine
type: system-feature
status: active
tags: [comedy-os, notation, stage-cues, delivery, syntax]
---

# 🎭 Inline Delivery Notation Engine

> **Stand-up is 20% words and 80% delivery.** Standard note apps record what to say, but fail miserably at capturing **how to say it**.

## 1. Notation Syntax Reference

> **[NOTE — HIGH-CONTRAST STAGE TELEPROMPTER CANCELLED]:** High-contrast on-stage teleprompter mode is cancelled (and will only return if requested by users). Comics do not carry phones onto the stage; phones remain in the pocket, handbag, or green room recording audio. Notation is strictly for **desk writing, pre-show backstage review, and Comparator post-set analysis**.

| Syntax Token | Meaning | Editor / Review Render |
|---|---|---|
| `[p: 2s]` or `[pause: 2s]` | Timed Beat Pause | `⏳ (2s)` yellow highlighted block |
| `**WORD**` | Punch Stress / Vocal Spike | Glowing bold orange typography |
| `[tag: XYZ]` or `+tag XYZ` | Modular Punch Tag | Indigo badge pill |
| `[act: glance left]` | Physical Stage Act-Out | Soft cyan italic stage direction |
| `[mic: drop / mouth close]` | Mic Technique Cue | Small badge indicator |
| `[callback: Bit-Airport]` | Planned Callback Link | Obsidian Wikilink with auto-completion |

## 2. Example Raw Script vs. Rendered Teleprompter View

### Raw Input:
```markdown
My dad doesn't text. He sends telegrams disguised as iMessage.
[p: 1.5s]
**ALL CAPS**.
[act: squint at phone with aggressive thumb typing]
"ARRIVING AT AIRPORT. STOP. BRING WARM JACKET. STOP. DISAPPOINTED IN YOU. STOP."
+tag "Didn't even know you could buy punctuation on an iPhone."
```

### Parsed AST (Abstract Syntax Tree):
```json
{
  "premise": "My dad doesn't text. He sends telegrams disguised as iMessage.",
  "beats": [
    {"type": "pause", "duration_seconds": 1.5},
    {"type": "vocal_stress", "content": "ALL CAPS"},
    {"type": "act_out", "cue": "squint at phone with aggressive thumb typing"},
    {"type": "punchline", "content": "ARRIVING AT AIRPORT..."},
    {"type": "tag", "tag_id": "tag_dad_punctuation", "content": "Didn't even know you could buy punctuation on an iPhone."}
  ]
}
```

## 3. Downstream Consumers
- [[30_The_Comparator_Bridge|The Comparator Bridge]]: Uses delivery notation to verify if the comic remembered the pauses and act-outs onstage.
