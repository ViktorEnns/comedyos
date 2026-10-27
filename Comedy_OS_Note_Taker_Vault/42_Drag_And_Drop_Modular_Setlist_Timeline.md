---
id: FEAT-DATA-042
title: Drag-and-Drop Modular Setlist Timeline
type: system-feature
status: active
tags: [comedy-os, setlist-builder, timeline, modular-cards, stage-prep]
---

# 🎛️ Drag-and-Drop Modular Setlist Timeline

> **Set Construction in 60 Seconds:** Construct a 15, 30, or 60-minute set by snapping modular bit cards into a dynamic time-budgeted timeline.

```
┌────────────────────────────────────────────────────────────────────────┐
│ 🎛️ SETLIST: Austin Mothership Main Room • 15:00 Budget                │
├────────────────────────────────────────────────────────────────────────┤
│ 1. [00:00 - 02:30]  [[Bit-Austin-Traffic]]       (Stage Ready) 🟢 A-Tier│
│ 2. [02:30 - 06:15]  [[Bit-Airport-TSA]]          (Stage Ready) 🟢 A-Tier│
│    └── Tag: "Oliver Twist Pants"                 [Ad-lib new!] 💡      │
│ 3. [06:15 - 09:45]  [[Bit-Dentist-Gums]]         (Testing)     🟡 B-Tier│
│ 4. [09:45 - 14:30]  [[Bit-Dad-Telegrams-Closer]] (Stage Ready) 🟢 A-Tier│
│ 5. [14:30 - 15:00]  Buffer / Crowd Outro         ⏱️ Remaining: 00:30   │
└────────────────────────────────────────────────────────────────────────┘
```

## 1. Modular Architecture
- **Time Budget Engine:** Each card holds historical stage duration statistics. As you reorder cards, total runtime dynamically updates.
- **Opener / Closer Balance Warning:** Flags setlists lacking an A-Tier closer or opening on an untested Draft.
- **Pre-Show Backstage Review *(High-Contrast Stage Mode Cancelled)*:** Pull up the setlist for a quick glance backstage right before heading to the mic.
  - **Product Decision Note:** *"High-Contrast Stage Mode"* (reading off the phone on stage) is **cancelled** and will only return if users explicitly request it. Comedians do not perform with phones in their hands or anywhere on stage; the phone is busy recording the set in the pocket, handbag, or green room.
