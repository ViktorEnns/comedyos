---
id: FEAT-AUDIO-013
title: Whisper ASR Speech-to-Text Pipeline
type: system-feature
status: active
tags: [comedy-os, whisper, asr, ml, speech-to-text, timestamps]
---

# 📝 Whisper ASR Speech-to-Text Pipeline

> **Stand-up is Not Business Speech:** Comedians use rapid pacing, mumbles, regional dialects, abrupt volume drops for effect, deliberate mispronunciations, and crowd banter. Generic speech engines choke on this.

## 1. ASR Engine Architecture

```
Raw Audio Stream (16kHz FLAC)
         │
         ▼
[Whisper Large-v3-Turbo / Local Tiny-En]
         │
         ├── Initial Prompt Injection: "Stand-up comedy set. Comedy club crowd.
         │                             Includes stage tags, callbacks, ad-libs, act-outs."
         │
         ▼
Word-Level Token Stream with Confidence & Timestamps:
[
  {"word": "Why", "start": 12.01, "end": 12.18, "confidence": 0.98},
  {"word": "does", "start": 12.19, "end": 12.30, "confidence": 0.99},
  {"word": "every", "start": 12.31, "end": 12.55, "confidence": 0.97},
  ...
]
```

## 2. Stand-up Specific Fine-Tuning & Prompts
- **Prompt Priming:** Injects the comedian's known [[40_Atomic_Bit_Database|Atomic Bit Vault]] keyword dictionary into Whisper's prompt window (prompt conditioning).
- **Hallucination Filtering:** Strips repeating YouTube-style hallucination loops ("Thank you for watching!", "Subscribe to my channel") during prolonged crowd laughs.
- **Punctuation & Cadence Restoration:** Maps micro-pauses (300ms–800ms) to commas or ellipses, and long dramatic pauses (1.5s+) to explicit `[pause: Xs]` delivery tags.
