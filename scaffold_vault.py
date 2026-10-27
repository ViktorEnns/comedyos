"""Comedy OS: Note Taker Architecture Vault Scaffolder

Generates an Obsidian vault implementing the complete 'Comedy OS Note Taker'
board:
- Audio-Forward (Granola Ingestion)
- Text-Forward (Keep Capture)
- Ghost Mode (Distraction Shield)
- Comparator Engine (Diff & Reaction Alignment)
- Atomic Bit Database (Object-Oriented State Machine)
"""

import os
from pathlib import Path

VAULT_DIR = Path("Comedy_OS_Note_Taker_Vault")

FILES = {
    # -------------------------------------------------------------
    # 0. MASTER ARCHITECTURE & INDEX
    # -------------------------------------------------------------
    "00_Comedy_OS_Note_Taker_Architecture.md": """---
id: ARCH-NOTE-TAKER-000
title: Comedy OS Note Taker - Master Architecture
type: system-architecture
status: active
tags: [comedy-os, architecture, ingestion, comparator, obsidian, master]
---

# 🎙️ Comedy OS Note Taker: System Architecture

> **Design Goal:** Eliminate the friction of generic note-taking apps by combining **Google Keep's zero-click capture speed** with **Granola's conversational audio intelligence**, bridged by an **Audio-vs-Text Comparator Engine** and backed by an **Atomic Bit Database**.

```mermaid
graph TD
    Root["🎙️ Comedy OS Note Taker<br/><i>System Ingestion & Performance Architecture</i>"]

    Root -->|UI switches to audio mode| AudioForward["🟢 Audio-Forward Mode (Granola Style)<br/><i>Capture + Transcription</i>"]
    Root -->|UI switches to text mode| TextForward["🟡 Text-Forward Mode (Keep Style)<br/><i>Instant Capture + Editing</i>"]
    Root -->|Central Shield| GhostMode["🛡️ FEAT: Ghost Mode<br/><i>Offline Storage & Zero Popups</i>"]

    subgraph Audio_Layer ["1. Audio-Forward Ingestion Layer (Granola Intelligence)"]
        AudioForward --> PerfIngest["<b>The Performance Ingestion Layer</b><br/>• Auto-records via venue GPS & schedule<br/>• Isolates comic speech from crowd noise<br/>• Live Whisper ASR transcription"]
        PerfIngest --> FeatAudio1["FEAT Audio: Audience Laughter & Silence Isolation"]
        PerfIngest --> FeatAudio2["1-Tap / Passive Recording"]
        PerfIngest --> FeatAudio3["FEAT Audio: Whisper ASR Speech-to-Text"]
        FeatAudio1 & FeatAudio3 --> ChatTape["💬 Conversational Chat Query with Set Tape<br/><i>'Talk to your notes to find context & compare joke versions'</i>"]
    end

    subgraph Text_Layer ["2. Text-Forward Capture Layer (Keep Simplicity)"]
        TextForward --> InstantCap["<b>The Instant Capture Layer</b><br/>• 0-click mobile widget: immediate blank line<br/>• No title, no folder, no tag prompt<br/>• Type 2 words or 5s memo; saves instantly"]
        InstantCap --> FeatText1["FEAT Text: Distraction-Free Plaintext & Markdown Pad"]
        InstantCap --> FeatText2["Zero-Click Floating Capture Widget"]
        InstantCap --> FeatText3["FEAT: Inline Delivery Notation<br/><i>Pauses, Tags, Vocal Emphasis, Stage Cues</i>"]
        FeatText3 --> NotationSystem["📝 Delivery Notation Engine<br/><i>Quickly capture & communicate how to perform on stage</i>"]
    end

    GhostMode -.->|Suppresses notifications & locks radio| PerfIngest
    GhostMode -.->|Locks DND & Airplane state| InstantCap

    subgraph Bridge_Engine ["3. The Comparator Bridge (The Secret Sauce)"]
        PerfIngest --> CompEngine{"⚡ FEAT: Comparator Engine<br/><i>Typed Text vs Spoken Audio</i>"}
        InstantCap --> CompEngine

        CompNote["<b>The Comparator Bridge</b><br/>• Aligns live stage audio against written notes<br/>• Green words = Onstage ad-libs<br/>• Red strikethrough = Forgotten written lines<br/>• Waveform spikes = Exact laugh duration"]
        CompEngine --- CompNote

        CompEngine --> DiffReport["FEAT Comp Engine: Visual Diff Report<br/><i>Ad-libs vs Written Script</i>"]
        CompEngine --> TagAlerts["FEAT Comp Engine: Dropped Tag Alerts<br/><i>Forgotten setups & unsaid tags</i>"]
        CompEngine --> WaveAlign["FEAT Comp Engine: Reaction Alignment<br/><i>Laugh spikes matched to waveform</i>"]
    end

    subgraph Database_Layer ["4. Atomic Bit Database (Object-Oriented Layer)"]
        DiffReport & TagAlerts & WaveAlign --> BitVault[("🧱 Atomic Bit Vault<br/><i>Living Objects Database</i>")]
        ChatTape --> BitVault

        BitVault --> SetlistBuilder["🎛️ Drag-and-Drop Modular Setlist Timeline<br/><i>Modular bit cards sequenced for 15/30/60m sets</i>"]
        BitVault --> SemanticSearch["🔍 Conversational Semantic Search & Filters<br/><i>Query: 'Show me premises with A-level laughs in Austin'</i>"]
        BitVault --> StateMachine["🔄 Jokes as Living Objects (State Machine)<br/><code>Draft ➔ Testing ➔ Stage Ready ➔ Retired</code>"]
        BitVault --> VectorEmbed["🧠 Background Semantic Vector Embeddings<br/><i>Contextual zero-tag indexing</i>"]
    end
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
""",

    # -------------------------------------------------------------
    # 1. CENTRAL SHIELD: GHOST MODE
    # -------------------------------------------------------------
    "01_Ghost_Mode_Distraction_Shield.md": """---
id: FEAT-GHOST-001
title: Ghost Mode - Offline Storage & Distraction Shield
type: system-feature
status: active
tags: [comedy-os, ghost-mode, offline-first, performance-shield, security]
---

# 🛡️ Ghost Mode: Offline Storage & Zero Popups

> **Comedian Pain Point:** Nothing ruins a set or a backstage green-room flow faster than an OS notification banner, an incoming phone call vibrating your pocket on stage, or a cloud sync timeout spinning during capture.

## 1. System Requirements & Behavior

Ghost Mode acts as an operating-system level shield engaged automatically or via single toggle:

```
[Backstage / Stage Entry]
         │
         ▼
 ┌───────────────┐
 │ GHOST MODE ON │ ──► Android DND Policy (Priority Only / Alarms Suppressed)
 └───────┬───────┘ ──► Cellular / Wi-Fi Sync Deferred to Local SQLite Queue
         │         ──► Zero Popup Dialogs (All non-critical UI toasts silenced)
         │         ──► Display Keep-Awake with OLED True-Black Theme
         ▼
[Stage Performance & Offline Capture]
         │
         ▼
 ┌───────────────┐
 │ GHOST MODE OFF│ ──► Background Delta Sync to Cloud (Firestore + Vertex AI)
 └───────────────┘
```

### Core Guarantees:
1. **Zero Popups / Zero Interruption:**
   - App suppresses all in-app toasts, rate-me prompts, sync error modals, or update notices.
   - Enforces Android `NotificationManager.INTERRUPTION_FILTER_NONE` or `PRIORITY`.
2. **Local-First SQLite Storage:**
   - Every keystroke, voice memo chunk, and timestamp is committed synchronously to an ACID-compliant local database before touching network sockets.
3. **Radio Lock & Battery Conservation:**
   - Network calls go dormant; audio ingestion runs entirely via hardware DSP and on-device whisper/local buffer.

## 2. Technical Implementation Spec

```dart
class GhostModeService {
  static const MethodChannel _channel = MethodChannel('com.comedyos/ghost_mode');

  Future<void> enableGhostMode() async {
    // 1. Request DND and Wakelock
    await _channel.invokeMethod('setDoNotDisturb', {'enabled': true});
    await WakelockPlus.enable();

    // 2. Pause remote syncing engine
    SyncCoordinator.instance.pauseRemoteSync();

    // 3. Switch UI theme to Stage True-Black (0 nits on OLED)
    ThemeController.instance.setStageMode(true);
  }

  Future<void> disableGhostMode() async {
    await WakelockPlus.disable();
    await _channel.invokeMethod('setDoNotDisturb', {'enabled': false});
    ThemeController.instance.setStageMode(false);

    // Trigger atomic background sync
    SyncCoordinator.instance.resumeAndFlush();
  }
}
```

## 3. Related Modules
- [[12_One_Tap_and_Passive_Recording|1-Tap / Passive Recording]]: Automatically arms Ghost Mode when entering venue geofence.
- [[22_Zero_Click_Floating_Capture_Widget|Zero-Click Floating Capture Widget]]: Renders in Ghost Mode without system interruptions.
- [[30_The_Comparator_Bridge|The Comparator Bridge]]: Feeds captured raw performance audio once Ghost Mode sync flushes.
""",

    # -------------------------------------------------------------
    # 2. AUDIO-FORWARD INGESTION LAYER
    # -------------------------------------------------------------
    "10_Audio_Forward_Ingestion_Layer.md": """---
id: LAYER-AUDIO-010
title: Audio-Forward Ingestion Layer (Granola Intelligence)
type: architecture-layer
status: active
tags: [comedy-os, audio, granola-style, transcription, ingestion]
---

# 🟢 Audio-Forward Ingestion Layer (Granola Intelligence)

> **Inspiration:** Like Granola for business meetings, Comedy OS turns ambient, imperfect spoken audio into structured, interactive knowledge—specifically tailored to the high-noise, dynamic acoustics of comedy clubs.

```mermaid
flowchart TD
    A[Live Club Audio Source] --> B[Dual-Channel DSP Stream]
    B --> C[Vocal Isolation Filter]
    B --> D[Audience Reaction Isolator]
    C --> E[Whisper ASR Model]
    E --> F[Millisecond Timestamped Words]
    D --> G[Laugh / Silence Spectral Analyzer]
    F & G --> H[Synchronized Performance Tape]
    H --> I[Conversational Chat Query Engine]
```

## 1. Distinctive Capabilities
1. **Dual-Track Audio Decomposition:** Separates comic mic feed from crowd room reverberation.
2. **Context-Aware Speech-to-Text:** Specialized vocabulary lexicon for comedy slang, premise setups, callbacks, and conversational cadence.
3. **Set Tape Synthesis:** Synchronizes transcript tokens directly with acoustic decibel energy levels.

## 2. Sub-Components
- [[11_Audience_Laughter_and_Silence_Isolation|1.1 Audience Laughter & Silence Isolation]]
- [[12_One_Tap_and_Passive_Recording|1.2 1-Tap & Passive Geofenced Recording]]
- [[13_Whisper_ASR_Speech_To_Text|1.3 Whisper ASR Speech-to-Text Pipeline]]
- [[14_Conversational_Chat_With_Set_Tape|1.4 Conversational Chat Query with Set Tape]]
""",

    "11_Audience_Laughter_and_Silence_Isolation.md": """---
id: FEAT-AUDIO-011
title: Audience Laughter & Silence Isolation
type: system-feature
status: active
tags: [comedy-os, audio-dsp, laughter-detection, acoustic-analysis, metrics]
---

# 🔊 Audience Laughter & Silence Isolation

> **The Metric that Matters:** A comedian doesn't just want words—they need to know **where the crowd erupted, where they chuckled, and where the room went stone dead.**

```mermaid
sequenceDiagram
    participant C as Comic Speech
    participant DSP as Isolation DSP
    participant L as Laughter Detector
    participant T as Timeline Store

    C->>DSP: Raw Audio (Dual Freq Bands)
    DSP->>DSP: Bandpass 200Hz-3.5kHz (Voice) vs 500Hz-8kHz (Crowd Roar)
    DSP->>L: High-energy crowd burst detected
    L->>T: Log Event: Laugh {start: 14.2s, end: 18.5s, peak_db: -4.2dB, score: A}
    DSP->>L: Flatline (< -38dB) after punchline
    L->>T: Log Event: Silence/DeadAir {duration: 3.8s, status: bombed}
```

## 1. Laugh vs. Voice Spectral Gating
- **Speech Band:** Centered in 300 Hz – 3,400 Hz format frequencies with distinct harmonic formants.
- **Laughter Signature:** Non-harmonic, turbulent burst noise characterized by rhythmic 4–6 Hz pulse frequency envelope, spread across 800 Hz – 6,000 Hz.
- **Decibel Classification Tier:**
  - **A-Tier (Roar/Applause):** > 18 dB above room floor, duration > 4.0s.
  - **B-Tier (Solid Laugh):** 10–18 dB above room floor, duration 2.0s – 4.0s.
  - **C-Tier (Chuckle/Titter):** 4–10 dB above room floor, duration 0.8s – 2.0s.
  - **Crickets (Dead Air):** < 3 dB room ambient variation for > 3.0s following speech termination.

## 2. Audio Feature Output Schema
```json
{
  "tape_id": "tape_2026_austin_creek_01",
  "events": [
    {
      "type": "laughter",
      "timestamp_start_ms": 42100,
      "timestamp_end_ms": 46800,
      "duration_ms": 4700,
      "peak_db": -6.1,
      "tier": "A",
      "preceding_word_token_id": "token_airline_peanut_punch"
    },
    {
      "type": "silence",
      "timestamp_start_ms": 48200,
      "timestamp_end_ms": 52400,
      "duration_ms": 4200,
      "tier": "crickets",
      "preceding_word_token_id": "token_airline_pilot_tag"
    }
  ]
}
```

## 3. Integrations
- Feeds directly into [[33_Reaction_Waveform_Alignment|Reaction Waveform Alignment]].
- Triggers [[32_Dropped_Tag_Alerts|Dropped Tag Alerts]] when a silence follows a shortened setup.
""",

    "12_One_Tap_and_Passive_Recording.md": """---
id: FEAT-AUDIO-012
title: 1-Tap & Passive Geofenced Recording
type: system-feature
status: active
tags: [comedy-os, recording, geofence, background-service, hardware]
---

# 🎙️ 1-Tap & Passive Geofenced Recording

> **Friction Kills Archiving:** If a comic has to unlock their phone, enter a passcode, find an app, create a file, and hit record 30 seconds before going on stage, 60% of stage sets will never be captured.

## 1. Ingestion Triggers

### 1. Zero-Friction 1-Tap
- **Android Quick Settings Tile:** A persistent tile labeled `Record Set`. Tap once from the lock screen. Audio starts buffering in under 180ms.
- **Physical Button Remapping:** Double-press Volume Down when inside a known venue launches immediate background recording.

### 2. Geofence & Calendar Auto-Arming
```mermaid
flowchart LR
    G[Venue GPS Detected<br/>e.g., Comedy Mothership] --> C{Calendar Match?<br/>Showtime +/- 15m}
    C -- Yes --> P[Prompt: 'Arm Set Tape?']
    C -- Auto-Approved --> R[Silent Passive Buffer Armed]
    P -- 1-Tap --> R
    R --> S[Stage Level Acoustic Trigger<br/>Mic decibels > threshold]
```

## 2. Background Resilience
- **Rolling Memory Buffer:** Uses an uncompressed 30-second circular buffer in memory so comic never misses the opening line even if tapped late.
- **Crash Recovery:** Writes audio chunks directly to disk every 10 seconds via Android Foreground Service with `FOREGROUND_SERVICE_TYPE_MICROPHONE`.
- Integrates with [[01_Ghost_Mode_Distraction_Shield|Ghost Mode]] to lock out OS notifications during active capture.
""",

    "13_Whisper_ASR_Speech_To_Text.md": """---
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
""",

    "14_Conversational_Chat_With_Set_Tape.md": """---
id: FEAT-AUDIO-014
title: Conversational Chat Query with Set Tape
type: system-feature
status: active
tags: [comedy-os, rag, conversational-query, set-tape, granola-intelligence]
---

# 💬 Conversational Chat Query with Set Tape

> **"Talk to your tape":** Instead of listening to a 45-minute recording from Tuesday night to find out why a transition felt awkward, the comedian asks the tape in plain conversational English.

## 1. Sample Query Dialogues

### Scenario A: Finding Ad-Libs
> **Comic:** *"Did I come up with any new punchlines or riffs during the dentist story in Chicago?"*  
> **Comedy OS:** *"Yes. At 14:32, after the line 'my gums are bleeding', you ad-libbed: 'Looks like a crime scene in a peppermint factory'. That got a 3.4s B-tier laugh. You never wrote that in your notes. Would you like me to add it as a new Tag to [[Bit-Dentist-Gums]]?"*

### Scenario B: Comparative Audience Reaction
> **Comic:** *"How did the airline bit close tonight compared to the Helium set in Philly?"*  
> **Comedy OS:** *"Tonight in Austin, you delivered Tag 3 in 4.2 seconds and got an A-Tier roar (5.1s). In Philly, you paused for 2.8 seconds and crowd laugh was 1.8s. The tighter pause increased laugh duration by 180%."*

```mermaid
flowchart TD
    Q[Comedian Question] --> LLM[Gemini 1.5 Flash / Context Agent]
    Tape[Audio Transcript + Timestamps] --> V[Vector & Timestamp Chunks]
    AudioEvents[Acoustic Laugh Events] --> V
    V --> LLM
    LLM --> Ans[Structured Answer with Direct Audio Seek Links]
    Ans --> Action[Action Button: 'Save Riff as Bit Tag']
```

## 2. Architecture Spec
- Multi-modal retrieval linking the audio segment byte offset, Whisper token indices, and [[11_Audience_Laughter_and_Silence_Isolation|Laugh Score]].
- Quick-listen playback pills: `[▶ Play Clip 14:30 - 14:45]`.
""",

    # -------------------------------------------------------------
    # 3. TEXT-FORWARD CAPTURE LAYER
    # -------------------------------------------------------------
    "20_Text_Forward_Capture_Layer.md": """---
id: LAYER-TEXT-020
title: Text-Forward Capture Layer (Keep Simplicity)
type: architecture-layer
status: active
tags: [comedy-os, text-capture, keep-style, speed, zero-friction]
---

# 🟡 Text-Forward Capture Layer (Keep Simplicity)

> **Inspiration:** Google Keep's lightning speed. When a premise strikes in the subway, at 3 AM in bed, or while listening to a podcast, you have an 8-second cognitive window before the nuance evaporates.

```mermaid
flowchart LR
    A[Idea Strikes] --> B[Tap Widget / Open Screen]
    B --> C[Immediate Blank Canvas<br/>Keyboard Up Instantly]
    C --> D[Type 2 words or whole bit]
    D --> E[Auto-Save on Exit / Blur]
    E --> F[Zero Folders Required<br/>Semantic Index in Background]
```

## 1. Non-Negotiable Tenets
1. **Zero Categorization Friction:** No modal asking "Select Folder", "Choose Category", or "Add Tags".
2. **Instant Blank Line:** App opens directly to the input cursor.
3. **Draft Survival:** If the phone battery dies mid-sentence, every single character typed is persisted in local WAL (Write-Ahead Logging).

## 2. Sub-Components
- [[21_Distraction_Free_Markdown_Pad|2.1 Distraction-Free Plaintext & Markdown Pad]]
- [[22_Zero_Click_Floating_Capture_Widget|2.2 Zero-Click Floating Capture Widget]]
- [[23_Inline_Delivery_Notation_Engine|2.3 Inline Delivery Notation Engine]]
""",

    "21_Distraction_Free_Markdown_Pad.md": """---
id: FEAT-TEXT-021
title: Distraction-Free Plaintext & Markdown Pad
type: system-feature
status: active
tags: [comedy-os, ui, editor, markdown, legal-pad]
---

# 📄 Distraction-Free Plaintext & Markdown Pad

> **Aesthetic Philosophy:** The "Digital Legal Pad". Warm, tactile, unobtrusive, engineered for comedy rhythm.

## 1. Visual & Typography Specifications
- **Vertical Rhythm Base Unit:** 32px line-height grid matching standard yellow legal pad margins.
- **Font Stack:** High-legibility monospaced / humanist hybrid (JetBrains Mono / Inter Display).
- **Zero Border-Soup:** Containers separated by soft background shifts (`#121214` to `#18181B` in dark mode) rather than rigid 1px box borders.
- **No Visible Scrollbars:** Smooth viewport overflow with gradient fade masks on top and bottom edges.

```
┌────────────────────────────────────────────────────────┐
│ 2:15 AM • Coffee Shop Premise                     [●]  │
│                                                        │
│ Baristas who ask your name like they're detectives     │
│ trying to crack an unsolved homicide.                  │
│                                                        │
│ [pause: 1.5s]                                          │
│ "Spell it."                                            │
│ "B-O-B."                                               │
│ "Don't lie to me Bob, if that IS your real name..."    │
│                                                        │
│                                                        │
└────────────────────────────────────────────────────────┘
```

## 2. Markdown Capabilities
- Lightweight inline bolding for punch emphasis (`**BOOM**`).
- Indentation for premise ➔ setup ➔ punchline ➔ tag hierarchy.
- Seamless compatibility with standard Obsidian markdown vaults.
""",

    "22_Zero_Click_Floating_Capture_Widget.md": """---
id: FEAT-TEXT-022
title: Zero-Click Floating Capture Widget
type: system-feature
status: active
tags: [comedy-os, widget, android, quick-capture, flutter]
---

# ⚡ Zero-Click Floating Capture Widget

> **The 1-Second Rule:** The comic shouldn't wait for splash screens, auth checks, or navigation trees.

## 1. Widget Trigger Surface
- **Lockscreen Glanceable Widget:** Single tap reveals a transient floating text overlay above the lockscreen.
- **Edge-Swipe Ribbon:** Pulling from the right bezel opens a floating scratchpad in PIP (Picture-in-Picture) over whatever the comedian was browsing.
- **Auto-IME Focus:** The virtual keyboard is programmatically requested on frame 0.

## 2. Technical Flutter Engine Optimization
```dart
class ZeroClickCaptureActivity extends StatefulWidget {
  @override
  _ZeroClickCaptureState createState() => _ZeroClickCaptureState();
}

class _ZeroClickCaptureState extends State<ZeroClickCaptureActivity> {
  final FocusNode _focusNode = FocusNode();
  final TextEditingController _textController = TextEditingController();

  @override
  void initState() {
    super.initState();
    // Immediate autofocus without waiting for build transition
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _focusNode.requestFocus();
    });
  }

  void _onAutoSave(String text) {
    if (text.trim().isEmpty) return;
    BitVaultRepository.quickInsert(rawContent: text);
  }
}
```
""",

    "23_Inline_Delivery_Notation_Engine.md": """---
id: FEAT-TEXT-023
title: Inline Delivery Notation Engine
type: system-feature
status: active
tags: [comedy-os, notation, stage-cues, delivery, syntax]
---

# 🎭 Inline Delivery Notation Engine

> **Stand-up is 20% words and 80% delivery.** Standard note apps record what to say, but fail miserably at capturing **how to say it**.

## 1. Notation Syntax Reference

| Syntax Token | Meaning | Stage Teleprompter Render |
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
""",

    # -------------------------------------------------------------
    # 4. THE COMPARATOR BRIDGE (THE SECRET SAUCE)
    # -------------------------------------------------------------
    "30_The_Comparator_Bridge.md": """---
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
""",

    "31_Visual_Diff_Report.md": """---
id: FEAT-BRIDGE-031
title: Visual Diff Report - Ad-Libs vs Written Script
type: system-feature
status: active
tags: [comedy-os, visual-diff, ad-libs, stage-review, text-comparison]
---

# 🔍 Visual Diff Report: Ad-Libs vs Written Script

> **Instant Post-Set Debrief:** Within 60 seconds of walking off stage, look at your phone and instantly see the delta of your performance.

## 1. Diff Visual Language

- <span style="background-color: #dcfce7; color: #166534; padding: 2px 6px; border-radius: 4px; font-weight: bold;">Green Highlight</span>: **Stage Ad-Lib / Riff** (Spoken onstage, never written down).
- <span style="background-color: #fee2e2; color: #991b1b; padding: 2px 6px; border-radius: 4px; text-decoration: line-through;">Red Strikethrough</span>: **Forgotten / Skipped Line** (In your written notes, omitted onstage).
- **Plain High-Contrast Text**: Exact verbatim delivery.

## 2. Example Set Report View

> ### Bit: Airline Travel Security (Run at Cap City Comedy, Austin)
> 
> "TSA doesn't actually care about safety. They just want to see how dignified you look <span style="background-color: #fee2e2; color: #991b1b; text-decoration: line-through;">walking around in your socks on a cold tile floor.</span> <span style="background-color: #dcfce7; color: #166534; font-weight: 600;">holding your pants up by your belt loops like an Oliver Twist orphan.</span> *(Laugh: 4.8s — Tier A)*
> 
> You ever look at the TSA agent's face when your bag goes through the scanner? <span style="background-color: #fee2e2; color: #991b1b; text-decoration: line-through;">He looks like an ultrasound technician who just saw a baby with three heads.</span>" *(Skipped entirely!)*

## 3. One-Tap Actions
- **[+ Save Orphan Riff as Tag]**: Promotes the green ad-lib directly into [[40_Atomic_Bit_Database|Atomic Bit Vault]].
- **[Re-Queue Skipped Line for Tomorrow]**: Bumps the skipped punchline to tomorrow's setlist review.
""",

    "32_Dropped_Tag_Alerts.md": """---
id: FEAT-BRIDGE-032
title: Dropped Tag Alerts & Missed Callback Detector
type: system-feature
status: active
tags: [comedy-os, dropped-tags, alerts, performance-analysis, optimization]
---

# ⚠️ Dropped Tag Alerts & Missed Callback Detector

> **Comedian Dilemma:** *"I had 3 killer tags written for that marriage bit, but the audience cheered so loudly I got flustered and transitioned too early."*

```mermaid
flowchart TD
    Script[Written Bit: 1 Setup + 3 Sequential Tags] --> Exec[Stage Audio Transcription]
    Exec --> Match{All 3 Tags Spoken?}
    Match -- Yes --> Good[Tag Completion: 100%]
    Match -- No --> Alert[Trigger Dropped Tag Alert]
    Alert --> Card[Show Card: Tag #2 Was Dropped<br/>'My wife has a black belt in guilt']
    Card --> Options[Option A: Review Audio Moment<br/>Option B: Keep Tag in Active Testing Queue]
```

## 1. Alert Thresholds
- **Time Pressure Drop:** If set running time approached the 15-minute red-light cutoff, Comedy OS annotates: *"Dropped due to time constraint (minute 14:15)."*
- **Momentum Drop:** If a preceding tag scored an A-Tier laugh, the engine notes: *"Crowd over-talked the transition; consider increasing pause to 3.5s before Tag 2."*

## 2. Post-Show Tag Summary Card
```markdown
### ⚠️ 2 Tags Omitted in Tonight's Set
1. **[[Bit-Marriage-Therapy]]**:
   - Missed: *"She cried in cursive."*
   - Impact: Missed estimated 3.0s reaction.
2. **[[Bit-Dog-Park]]**:
   - Missed: *"That golden retriever has an LLC."*
```
""",

    "33_Reaction_Waveform_Alignment.md": """---
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
3. **Laugh Duration Decibels (LDD):** $\\text{LDD} = \\int_{t_{\\text{start}}}^{t_{\\text{end}}} (\\text{dB}(t) - \\text{dB}_{\\text{floor}}) \\, dt$.

## 2. Downstream Database Feedback
- Updates the health metric of the joke in [[41_Jokes_As_Living_Objects_State_Machine|Jokes as Living Objects State Machine]].
- Automatic tier classification (`A`, `B`, `C`, `Flat`).
""",

    # -------------------------------------------------------------
    # 5. ATOMIC BIT DATABASE (OBJECT-ORIENTED LAYER)
    # -------------------------------------------------------------
    "40_Atomic_Bit_Database.md": """---
id: LAYER-DATA-040
title: Atomic Bit Vault & Object Schema
type: architecture-layer
status: active
tags: [comedy-os, bit-vault, schema, object-oriented, atomic-notes]
---

# 🧱 Atomic Bit Vault & Object Schema

> **Jokes as Domain Objects:** In Comedy OS, a joke is not a string in a notes document. It is a structured **Atomic Bit Object** with state, delivery metadata, performance history, audio snippets, and tag connections.

## 1. Bit Data Schema (JSON-LD / Firestore Model)

```typescript
interface AtomicBit {
  id: string; // e.g. "bit_tsa_security_2026"
  title: string; // "TSA Airport Security"
  state: 'draft' | 'testing' | 'stage_ready' | 'retired';
  premise: string; // "TSA is security theater designed to humiliate passengers"
  
  // Delivery Components
  setups: string[];
  punchlines: Array<{
    id: string;
    text: string;
    delivery_notes: string; // "[p: 1.5s] **ALL CAPS**"
    hit_rate_tier: 'A' | 'B' | 'C' | 'untested';
    average_laugh_duration_seconds: number;
  }>;
  
  tags_and_riffs: Array<{
    id: string;
    text: string;
    is_ad_lib_harvest: boolean;
    discovered_at_venue?: string;
  }>;

  // Setlist & Categorization
  target_duration_seconds: number;
  topics: string[]; // ["travel", "paranoia", "government"]
  callbacks_to_bit_ids: string[];
  
  // Performance History Run log
  run_history: Array<{
    tape_id: string;
    venue: string;
    city: string;
    date: string;
    laugh_duration_seconds: number;
    dropped_tags: string[];
  }>;
}
```

## 2. Component Nodes
- [[41_Jokes_As_Living_Objects_State_Machine|4.1 Jokes as Living Objects (Lifecycle State Machine)]]
- [[42_Drag_And_Drop_Modular_Setlist_Timeline|4.2 Drag-and-Drop Modular Setlist Timeline]]
- [[43_Conversational_Semantic_Search_And_Vector_Embeddings|4.3 Semantic Vector Search & Contextual Zero-Tag Indexing]]
""",

    "41_Jokes_As_Living_Objects_State_Machine.md": """---
id: FEAT-DATA-041
title: Jokes as Living Objects - Lifecycle State Machine
type: system-feature
status: active
tags: [comedy-os, state-machine, joke-lifecycle, bit-evolution, quality-gates]
---

# 🔄 Jokes as Living Objects: Lifecycle State Machine

> **The Joke Lifecycle:** Great bits aren't written; they are forged across dozens of open mics, comedy clubs, and tour dates.

```mermaid
stateDiagram-v2
    [*] --> Draft : Instant Capture (Keep Widget)
    Draft --> Testing : Added to Open Mic Setlist
    Testing --> Testing : Comparator detects C/B Laughs (Iterate)
    Testing --> Stage_Ready : 3 consecutive A-Tier runs (>4s laugh)
    Stage_Ready --> Testing : Tag bombed or premise updated
    Stage_Ready --> Retired : Recorded for Special / Tape Burned
    Testing --> Retired : Abandoned (5 consecutive flatlines)
    Retired --> [*]
```

## 1. Lifecycle State Definitions

1. **Draft (Premise Stage):**
   - Raw note from [[20_Text_Forward_Capture_Layer|Text-Forward Capture]].
   - Contains a premise and at least one punchline hypothesis.
2. **Testing (Open Mic / Workout Room):**
   - Active in open mics or low-stakes sets.
   - [[30_The_Comparator_Bridge|Comparator]] actively analyzes punchline-to-laugh ratios and collects ad-libs.
3. **Stage Ready (A-Set Material):**
   - Passed strict quality gate: **$\\ge 3$ verified A-Tier laughter events across 2 different venues**.
   - Timing, pauses, and cadence stabilized.
4. **Retired (Special Burn / Vaulted):**
   - Filmed for YouTube/Netflix special, or retired from rotation. Available for callback references or revival.

## 2. Automated State Transitions
- **Auto-Promotion Prompt:** When the Comparator detects a bit hitting $>4.5\text{s}$ laughter on 3 recordings, app alerts: *"Promote 'Airport TSA' to Stage Ready?"*
""",

    "42_Drag_And_Drop_Modular_Setlist_Timeline.md": """---
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
- **Stage Mode Teleprompter View:** One-click flip to giant high-contrast cheat sheet for backstage glance right before walking out.
""",

    "43_Conversational_Semantic_Search_And_Vector_Embeddings.md": """---
id: FEAT-DATA-043
title: Semantic Vector Search & Contextual Zero-Tag Indexing
type: system-feature
status: active
tags: [comedy-os, semantic-search, vector-embeddings, invisible-librarian, vertex-ai]
---

# 🧠 Semantic Vector Search & Contextual Zero-Tag Indexing

> **The Invisible Librarian:** Traditional note tags (`#dating`, `#airports`, `#family`) break down when you have 500 bits. You don't remember how you tagged it 3 years ago. Semantic Vector Search finds ideas by conceptual meaning.

```mermaid
flowchart TD
    Raw[Comedian's Notes & Bit Cards] --> Embed[Vertex AI / Local ONNX Embedding Engine]
    Embed --> VecStore[(Vector Database - Cosine Index)]
    Query[Natural Language Prompt:<br/>'Show me premises with A-level laughs in Austin about awkward dating']
    Query --> QEmbed[Query Embedding]
    QEmbed --> Search[Semantic Vector Matching + SQL Filters]
    VecStore --> Search
    Search --> Results[Ranked Bits: 'Tinder date in coffee shop', 'The ex-girlfriend dog custody']
```

## 1. Natural Language Search Queries Supported

- *"Show me crowd work riffs about dentists."*
- *"Find bits that kill in Austin but struggled in New York."*
- *"What jokes do I have where I talk about feeling like an imposter?"*
- *"Show me bits with untested tags written in the last 30 days."*

## 2. Technical Stack
- **Embedding Model:** Local on-device lightweight text embeddings (e.g. `bge-small-en-v1.5` ONNX) backed by cloud sync with `text-embedding-004` on Google Cloud / Vertex AI.
- **Zero-Tag Philosophy:** Automatically extracts latent comedy concepts (e.g. Self-Deprecation, Observational, Absurdist, Crowdwork, Storytelling) without requiring user tagging.
""",

    # -------------------------------------------------------------
    # 6. OBSIDIAN CANVAS (VISUAL BOARD)
    # -------------------------------------------------------------
    "Comedy_OS_Architecture.canvas": """{
  "nodes": [
    {"id": "root", "x": 0, "y": 0, "width": 420, "height": 180, "type": "text", "text": "# 🎙️ Comedy OS Note Taker\\n*System Ingestion & Performance Architecture*\\n\\nBridging Keep capture speed with Granola audio intelligence."},
    {"id": "ghost", "x": -500, "y": 0, "width": 380, "height": 180, "type": "file", "file": "01_Ghost_Mode_Distraction_Shield.md"},
    {"id": "audio_layer", "x": 550, "y": -350, "width": 380, "height": 220, "type": "file", "file": "10_Audio_Forward_Ingestion_Layer.md"},
    {"id": "text_layer", "x": 550, "y": 350, "width": 380, "height": 220, "type": "file", "file": "20_Text_Forward_Capture_Layer.md"},
    {"id": "comparator", "x": 1100, "y": 0, "width": 420, "height": 240, "type": "file", "file": "30_The_Comparator_Bridge.md"},
    {"id": "vault", "x": 1650, "y": 0, "width": 420, "height": 240, "type": "file", "file": "40_Atomic_Bit_Database.md"}
  ],
  "edges": [
    {"id": "e1", "fromNode": "root", "fromSide": "left", "toNode": "ghost", "toSide": "right", "label": "Shields Ingestion & Capture"},
    {"id": "e2", "fromNode": "root", "fromSide": "top", "toNode": "audio_layer", "toSide": "left", "label": "Audio-Forward Mode"},
    {"id": "e3", "fromNode": "root", "fromSide": "bottom", "toNode": "text_layer", "toSide": "left", "label": "Text-Forward Mode"},
    {"id": "e4", "fromNode": "audio_layer", "fromSide": "right", "toNode": "comparator", "toSide": "top", "label": "Transcribed Audio & Reactions"},
    {"id": "e5", "fromNode": "text_layer", "fromSide": "right", "toNode": "comparator", "toSide": "bottom", "label": "Written Script & Notation"},
    {"id": "e6", "fromNode": "comparator", "fromSide": "right", "toNode": "vault", "toSide": "left", "label": "Diffs, Laughs & Living Objects"}
  ]
}
"""
}

def scaffold_vault(target_dir: Path = VAULT_DIR):
    """Generates all markdown files and the Obsidian canvas in the target directory."""
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"Scaffolding Obsidian Vault into: {target_dir.resolve()}")

    for filename, content in FILES.items():
        file_path = target_dir / filename
        file_path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"  [+] Created: {filename}")

    print("\nVault generation complete! You can open this directory directly in Obsidian.")

if __name__ == "__main__":
    scaffold_vault()
