---
id: CLASS-WORKBENCH-006
title: Mobile Keep Capture, Desktop Sequential Workbench & Supabase Sync Classes
type: class-diagram
created: 2026-10-26
status: active
parent: "[[00_Master_Domain_Class_Diagram]]"
tags:
  - comedy-os
  - class-diagram
  - uml
  - mobile-keep
  - desktop-workbench
  - supabase
  - sequential-blocks
---

# 🏛️ 06: Mobile Keep Capture, Desktop Sequential Workbench & Supabase Sync Classes

> **Architectural Scope:** Models the decoupled **Mobile Keep Ingestion Client** (Quick Text, Voice Memo ASR, Handwritten Notebook OCR/OXR), the **Dual-Layer Supabase + Offline Repository**, and the **Desktop Two-Stage Sequential Joke Workbench** (Brain Dump $\rightarrow$ Ghost Suggested Setup/Punchline $\rightarrow$ Variable Sequential Bridge/Punch/Tag Chain + Obsidian/Antigravity Split Journal).

---

## 1. UML Class Diagram (`classDiagram`)

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'darkMode': true,
    'background': '#0f172a',
    'mainBkg': '#1e293b',
    'textColor': '#f8fafc',
    'lineColor': '#64748b',
    'fontFamily': 'Inter, system-ui, sans-serif',
    'fontSize': '12px',
    'nodeBorder': '#334155'
  }
}}%%
classDiagram
    direction TB

    class MobileKeepCaptureView {
        +CaptureModality activeTab
        +String quickNoteBuffer
        +List~JournalEntry~ recentCapturesFeed
        +captureQuickText(rawText) Promise~JournalEntry~
        +triggerVoiceMemoCapture() Promise~JournalEntry~
        +triggerCameraOCRScan(imageFile) Promise~JournalEntry~
        +renderKeepFeed() void
    }

    class VoiceMemoService {
        +Boolean isRecording
        +Float elapsedSeconds
        +startRecording() void
        +stopAndTranscribe() Promise~VoiceTranscriptResult~
    }

    class HandwrittenOCRScanner {
        +String endpointUrl "/api/ocr"
        +scanNotebookPhoto(imageBlob) Promise~OCRExtractionResult~
        +preprocessContrast(imageBlob) Blob
    }

    class JournalRepository {
        +SupabaseClient supabase
        +OfflineSyncQueue localQueue
        +Boolean isOnline
        +saveEntry(entry: JournalEntry) Promise~JournalEntry~
        +saveSequentialBlocks(entryId: UUID, blocks: List~JokeBlock~) Promise~void~
        +fetchJournalLedger(filter: JournalFilter) Promise~List~JournalEntry~~
        +subscribeRealtime(onRemoteChange) Subscription
        +exportVaultMarkdown() String
    }

    class OfflineSyncQueue {
        +String storageKey "comedyos_journal_v1"
        +List~PendingMutation~ dirtyQueue
        +writeLocalImmediate(entry: JournalEntry) void
        +flushToSupabase(supabase: SupabaseClient) Promise~Int~
    }

    class JournalEntry {
        +UUID id
        +String displayCode "B-104"
        +String rawText
        +CaptureModality modality
        +EntryStatus status "SEED | STRUCTURED | STAGE_READY"
        +String versionLabel "V1.0"
        +List~JokeBlock~ blocks
        +List~MediaAttachment~ attachments
        +DateTime createdAt
        +DateTime updatedAt
        +isUnstructuredSeed() Boolean
        +promotePhraseToBlock(phrase, targetType, moveFromRaw) JokeBlock
    }

    class JokeBlock {
        <<abstract>>
        +UUID id
        +UUID journalEntryId
        +Int sortOrder
        +BlockType type
        +String content
        +Int wordCount
        +Int syllableCount
        +isGhostSuggested() Boolean
        +computeTelemetry() BlockTelemetry
    }

    class SetupBlock {
        +BlockType type "SETUP"
        +String placeholder "Suggested Set-up..."
    }

    class BridgeBlock {
        +BlockType type "BRIDGE"
        +BridgeCategory category "BRIDGE | DEVELOPMENT | EXPLORATION"
        +DevelopmentSubtype subtype "NONE | MISDIRECT | EXAGGERATION | REPETITION | REIMAGINE | REENACT | THE_BEND | LIST"
        +setVariation(category, subtype) void
    }

    class PunchlineBlock {
        +BlockType type "PUNCHLINE"
        +Int punchIndex "1, 2, 3..."
        +Boolean isAltVariant
        +Boolean isStageActive
        +toggleStageActive() void
    }

    class TagBlock {
        +BlockType type "TAG"
        +Int tagIndex
    }

    class DesktopWorkbenchController {
        +JournalEntry activeEntry
        +JournalEntry pinnedComparisonEntry
        +ExtractMode extractMode "MOVE | COPY"
        +Boolean isJournalSplitOpen
        +onBrainDumpShortcut(keyCombo, selection) void
        +insertSequentialBlockAfter(index: Int, blockType: BlockType) JokeBlock
        +openSplitJournalLedger() void
        +pinEntryForComparison(entryId: UUID) void
        +pullLineFromComparison(text: String, targetType: BlockType) void
    }

    MobileKeepCaptureView --> VoiceMemoService : records audio via
    MobileKeepCaptureView --> HandwrittenOCRScanner : scans notebooks via
    MobileKeepCaptureView --> JournalRepository : saves captures to

    DesktopWorkbenchController --> JournalRepository : syncs & queries
    DesktopWorkbenchController *-- "1" JournalEntry : edits active
    DesktopWorkbenchController o-- "0..1" JournalEntry : compares side-by-side

    JournalRepository *-- OfflineSyncQueue : buffers offline in
    JournalRepository --> JournalEntry : persists & streams

    JournalEntry *-- "0..*" JokeBlock : ordered sequential chain
    JokeBlock <|-- SetupBlock
    JokeBlock <|-- BridgeBlock
    JokeBlock <|-- PunchlineBlock
    JokeBlock <|-- TagBlock
```

---

## 2. Class-by-Class Explanation & Architectural Design Choices

1. **`MobileKeepCaptureView` (Mobile-Only Ingestion Client):**
   - Provides three fast capture modes (`Quick Text`, `🎤 Voice Memo`, `📷 OCR Scan Handwritten Note`) and a chronological Google Keep-style list of captured seeds. Zero multi-block editing clutter on mobile.
2. **`VoiceMemoService` & `HandwrittenOCRScanner`:**
   - Handles mobile microphone dictation and camera photos of physical notebook pages, routing them to Cloudflare Pages Functions (`/api/transcribe` and `/api/ocr`) and attaching original media files to Supabase Storage.
3. **`JournalRepository` & `OfflineSyncQueue`:**
   - Dual-layer persistence: writes immediately to `localStorage` (`comedyos_journal_v1`) for zero-latency offline reliability in basement comedy clubs, then syncs to **Supabase PostgreSQL** (`journal_entries` & `joke_blocks`) and broadcasts live updates via **Supabase Realtime**.
4. **`JournalEntry` & Polymorphic `JokeBlock` Subclasses (`SetupBlock`, `BridgeBlock`, `PunchlineBlock`, `TagBlock`):**
   - Models the ordered sequential block chain (`sortOrder: 0..N`). Empty `SetupBlock` and `PunchlineBlock` instances return `isGhostSuggested() === true` (`opacity: 0.36`), while `BridgeBlock` supports `Bridge`, `Exploration`, and `Development` (`Misdirect`, `Exaggeration`, `Repetition`, `Reimagine`, `Reenact`, `The Bend`, `List`) anywhere in the chain.
5. **`DesktopWorkbenchController`:**
   - Powers the Desktop two-stage workflow (`Alt+S`/`Alt+P`/`Alt+B`/`Alt+T` extraction from Brain Dump into the sequential circuit) and the **Obsidian / Antigravity Split-View Journal** where `activeEntry` stays visible on the right while `pinnedComparisonEntry` or the Journal Ledger is open on the left.
