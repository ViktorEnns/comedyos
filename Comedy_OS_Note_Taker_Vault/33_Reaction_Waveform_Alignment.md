---
id: FEAT-BRIDGE-033
title: Reaction Alignment - Laugh Spikes vs Spoken Words
type: system-feature
status: active
tags: [comedy-os, waveform, laugh-spikes, hit-rate, audio-sync]
---

# 📈 Reaction Alignment: Laugh Spikes vs Spoken Words

> **Precision Comedy Engineering:** Correlating acoustic energy graphs with millisecond-accurate transcript tokens to calculate true LPM (Laughs Per Minute).

```
Audio dB:
  0 dB ─────────────────────────────────────────────────────────────
-10 dB ───────────████████────────────────────────██████████──────── (LAUGH SPIKE)
-20 dB ──██──────██████████──────██──────────────████████████──────
-40 dB ──██──────██████████──────██──────────────████████████────── (ROOM NOISE)
Words:  "My"    "gums...bled"   [2s]            "Peppermint factory!"
Event:           (Punchline)    (Pause)               (Ad-lib Tag)
Reaction:        Tier B (2.1s)                        Tier A (4.6s)
```

## 1. Calculated Metrics

1. **LPM (Laughs Per Minute):** Number of laughter events with duration > 1.2s per 60 seconds on mic.
2. **Punch-to-Laugh Latency (P-to-L):** Milliseconds elapsed between the final syllable of the punchline and the crowd exceeding +10 dB above noise floor.
   - Ideal P-to-L: 200ms – 600ms (Immediate comprehension).
   - High P-to-L (> 1200ms): Complex premise or delayed processing.
3. **Laugh Duration Decibels (LDD):** $\text{LDD} = \int_{t_{\text{start}}}^{t_{\text{end}}} (\text{dB}(t) - \text{dB}_{\text{floor}}) \, dt$.

## 2. Downstream Database Feedback
- Updates the health metric of the joke in [[41_Jokes_As_Living_Objects_State_Machine|Jokes as Living Objects State Machine]].
- Automatic tier classification (`A`, `B`, `C`, `Flat`).
