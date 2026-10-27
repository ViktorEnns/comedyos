---
id: ARCH-NOTE-TAKER-000
title: Comedy OS Note Taker - Master Architecture
type: system-architecture
status: active
canvas: "[[Comedy_OS_Architecture.canvas]]"
tags: [comedy-os, architecture, ingestion, comparator, obsidian, master, figjam]
---

# 🎙️ Comedy OS Note Taker: Master Architecture

> **Design Goal:** Eliminate the friction of generic note-taking apps by combining **Google Keep's zero-click capture speed** with **Granola's conversational audio intelligence**, bridged by an **Audio-vs-Text Comparator Engine** and backed by an **Atomic Bit Database**.

---

## 🗺️ Master Visual Architecture (FigJam Flowchart)

```mermaid
flowchart TD
    Root["🎙️ Comedy OS Note Taker<br/><i>System Ingestion & Performance Architecture</i>"]

    Root -->|audio forward| AudioForward["🟢 Audio-Forward Layer<br/><i>(Granola Intelligence)</i>"]
    Root -->|text forward| TextForward["🟡 Text-Forward Layer<br/><i>(Keep Simplicity)</i>"]
    Root -->|Shield| GhostMode["🛡️ 01: Ghost Mode<br/><i>(Distraction Shield)</i>"]

    subgraph Audio_Layer ["1. Audio-Forward Ingestion Layer (Granola Intelligence)"]
        AudioForward --> PerfIngest["<b>The Performance Ingestion Layer:</b><br/>• Before stepping on stage, hit Record<br/>• (or venue GPS / schedule geofence)<br/>• Records room & separates comic from crowd roar<br/>• Transcribes set in near real-time"]
        PerfIngest --> FeatAudio1["🔊 11: Audience Laughter & Silence Isolation<br/><i>Dual-Band DSP Spectrum Analyzer</i>"]
        PerfIngest --> FeatAudio2["🎙️ 12: 1-Tap & Passive Recording<br/><i>Lockscreen Trigger / Venue Geofence</i>"]
        PerfIngest --> FeatAudio3["📝 13: Whisper ASR Speech-To-Text<br/><i>Word-level Millisecond Timestamps</i>"]
        PerfIngest --> FeatAudio4["💬 14: Conversational Chat With Set Tape<br/><i>Granola-Style Q&A Engine</i>"]
        FeatAudio4 --- ChatNote["<b>Talk to your notes:</b><br/><i>Find context, locate past sets, compare<br/>earlier versions of a joke with tonight's run</i>"]
    end

    subgraph Text_Layer ["2. Text-Forward Capture Layer (Keep Simplicity)"]
        TextForward --> InstantCap["<b>The Instant Capture Layer:</b><br/>• 0-click mobile widget: immediate blank line<br/>• No title, no folder selection, no tag prompt<br/>• Type 2 words ('Zoo lions') or 5s voice memo<br/>• Saves instantly to unorganized inbox"]
        InstantCap --> FeatText1["📄 21: Distraction-Free Plaintext & Markdown Pad<br/><i>Off-white, low eyestrain, legal pad lines</i>"]
        InstantCap --> FeatText2["⚡ 22: Zero-Click Floating Capture Widget<br/><i>Desktop & Mobile Quick Overlay</i>"]
        InstantCap --> FeatText3["🎭 23: Inline Delivery Notation Engine<br/><i>Standardized stage & vocal delivery cues</i>"]
        FeatText3 --- NotationNote["<b>Notation:</b><br/><i>Quickly capture & communicate how to perform:<br/>💥 emphasis, 🥊 punch, 💤 pause, 🗣️ voice, 🤸 act out</i>"]
    end

    GhostMode --- GhostNote["<b>Ghost Mode Shield:</b><br/><i>Limit distractions while writing or performing.<br/>Locks device in airplane/DND; stores locally</i>"]

    GhostMode -.->|Shields Ingestion| PerfIngest
    GhostMode -.->|Shields Capture| InstantCap

    subgraph Bridge_Engine ["3. The Comparator Bridge (The Secret Sauce)"]
        PerfIngest --> CompEngine{"⚡ 30: The Comparator Bridge<br/><i>Spoken Audio Tape vs Written Script</i>"}
        InstantCap --> CompEngine

        CompEngine --- CompNote["<b>The Comparator Bridge:</b><br/>• Aligns live stage audio against written Keep notes<br/>• 🟢 Green words = Ad-libs & riffs on stage<br/>• 🔴 Red strikethrough = Forgotten written lines<br/>• Waveform spikes = Exact laugh duration (s)"]

        CompEngine --> DiffReport["🔍 31: Visual Diff Report<br/><i>Ad-Libs vs Written Script Delta</i>"]
        CompEngine --> TagAlerts["⚠️ 32: Dropped Tag Alerts<br/><i>Missed callbacks & forgotten punchlines</i>"]
        CompEngine --> WaveAlign["📈 33: Reaction Waveform Alignment<br/><i>Laugh energy (dB × s) vs words & WPM drift</i>"]
    end

    subgraph Database_Layer ["4. Atomic Bit Database (Living Object Store)"]
        DiffReport & TagAlerts & WaveAlign --> BitVault[("🧱 40: Atomic Bit Database<br/><i>Living Object Store & Version Tree</i>")]

        BitVault --> StateMachine["🔄 41: Jokes As Living Objects<br/><i>Finite State Machine Lifecycle</i>"]
        StateMachine --- StateNote["<b>Object States:</b><br/><code>Draft ➔ Testing ➔ Stage Ready ➔ Retired</code><br/><i>Transitions driven by empirical laugh data</i>"]

        BitVault --> SetlistBuilder["🎛️ 42: Drag & Drop Modular Setlist Timeline<br/><i>Dynamic set balancing & time budgeting</i>"]
        SetlistBuilder --- SetlistNote["<b>The Setlist Builder:</b><br/><i>Granular control: bits as modular cards dragged<br/>into linear 5/15/30/60m timelines</i>"]

        BitVault --> SemanticSearch["🔍 43: Conversational Semantic Search & Embeddings<br/><i>Natural memory retrieval across whole archive</i>"]
        SemanticSearch --- SearchNote["<b>Chat & Semantic Retrieval:</b><br/><i>No folders. Query: 'Did the baggage joke hit harder<br/>in Austin or Denver?' or 'Show A-level laughs from July'</i>"]
    end

    style Root fill:#f1f5f9,stroke:#64748b,stroke-width:3px,color:#0f172a
    style AudioForward fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    style TextForward fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f
    style GhostMode fill:#fce7f3,stroke:#db2777,stroke-width:2px,color:#831843
    style CompEngine fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#7c2d12
    style BitVault fill:#ede9fe,stroke:#7c3aed,stroke-width:3px,color:#4c1d95
```

---

## 🧭 Vault Navigation & System Modules

1. **Central Shield**:
   - [[01_Ghost_Mode_Distraction_Shield|🛡️ Ghost Mode (Offline Storage & Zero Popups)]]

2. **Audio-Forward Layer (Granola Style)**:
   - [[10_Audio_Forward_Ingestion_Layer|🟢 1.0 The Performance Ingestion Layer Overview]]
   - [[11_Audience_Laughter_and_Silence_Isolation|🔊 1.1 Audience Laughter & Silence Isolation]]
   - [[12_One_Tap_and_Passive_Recording|🎙️ 1.2 1-Tap & Passive Geofenced Recording]]
   - [[13_Whisper_ASR_Speech_To_Text|📝 1.3 Whisper ASR Speech-to-Text Pipeline]]
   - [[14_Conversational_Chat_With_Set_Tape|💬 1.4 Conversational Chat Query with Set Tape]]

3. **Text-Forward Capture Layer (Keep Style)**:
   - [[20_Text_Forward_Capture_Layer|🟡 2.0 The Instant Capture Layer Overview]]
   - [[21_Distraction_Free_Markdown_Pad|📄 2.1 Distraction-Free Plaintext & Markdown Pad]]
   - [[22_Zero_Click_Floating_Capture_Widget|⚡ 2.2 Zero-Click Floating Capture Widget]]
   - [[23_Inline_Delivery_Notation_Engine|🎭 2.3 Inline Delivery Notation Engine]]
   - [[25_Jimmy_Carr_Joke_Writing_Architecture|✍️ 2.5 Jimmy Carr Joke Writing Screen & Interaction Architecture]]
   - [[26_Desktop_Workbench_Mobile_Keep_Supabase_Architecture|🏛️ 2.6 Desktop Workbench, Mobile Keep Capture & Supabase Cloud Architecture]]

4. **The Comparator Bridge (The Secret Sauce)**:
   - [[30_The_Comparator_Bridge|⚡ 3.0 The Comparator Bridge Overview]]
   - [[31_Visual_Diff_Report|🔍 3.1 Visual Diff Report (Ad-Libs vs Written Script)]]
   - [[32_Dropped_Tag_Alerts|⚠️ 3.2 Dropped Tag Alerts & Missed Callback Detector]]
   - [[33_Reaction_Waveform_Alignment|📈 3.3 Reaction Alignment (Laugh Spikes vs Spoken Words)]]

5. **Atomic Bit Database (Object-Oriented Layer)**:
   - [[40_Atomic_Bit_Database|🧱 4.0 Atomic Bit Vault & Object Schema]]
   - [[41_Jokes_As_Living_Objects_State_Machine|🔄 4.1 Jokes as Living Objects (Lifecycle State Machine)]]
   - [[42_Drag_And_Drop_Modular_Setlist_Timeline|🎛️ 4.2 Drag-and-Drop Modular Setlist Timeline]]
   - [[43_Conversational_Semantic_Search_And_Vector_Embeddings|🧠 4.3 Semantic Vector Search & Contextual Zero-Tag Indexing]]

6. **UML Class Diagrams (MVP Domain Architecture)**:
   - [[Class_Diagrams/00_Master_Domain_Class_Diagram|🏛️ 00: Master Domain Class Diagram (MVP)]]
   - [[Class_Diagrams/01_Unified_Ingestion_and_Capture_Classes|⚡ 01: Unified Ingestion, Morphing CTA & Delivery Notation Classes]]
   - [[Class_Diagrams/02_Audio_DSP_and_Performance_Tape_Classes|🔊 02: Audio DSP, Whisper ASR & Composure Telemetry Classes]]
   - [[Class_Diagrams/03_Comparator_Bridge_and_Diff_Classes|⚡ 03: Comparator Bridge, Visual Diff & Skid Recovery Classes]]
   - [[Class_Diagrams/04_Atomic_Bit_Database_and_Lexicon_Classes|🧱 04: Atomic Bit Database, State Machine, Lexicon & Highlighter Classes]]
   - [[Class_Diagrams/05_Class_Architecture.canvas|🗺️ 05: Interactive Class Architecture Canvas]]
   - [[Class_Diagrams/06_Mobile_Keep_Desktop_Workbench_Supabase_Classes|🏛️ 06: Mobile Keep Capture, Desktop Sequential Workbench & Supabase Sync Classes]]

---

## 🎨 Interactive Obsidian Canvas
* Open the interactive visual canvas in Obsidian: **[[Comedy_OS_Architecture.canvas]]**.
