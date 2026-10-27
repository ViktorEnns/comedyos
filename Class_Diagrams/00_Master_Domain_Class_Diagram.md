---
id: CLASS-MASTER-000
title: Comedy OS - Master Domain Class Diagram (MVP)
type: class-diagram
status: active
canvas: "[[05_Class_Architecture.canvas]]"
tags: [comedy-os, class-diagram, uml, mvp, domain-model, architecture]
---

# 🏛️ Comedy OS: Master Domain Class Diagram (MVP)

> **Purpose:** High-level object-oriented domain model for the **Comedy OS MVP**. This diagram illustrates how the 4 core pillars—**Unified Ingestion**, **Audio Performance Tape**, **The Comparator Bridge**, and the **Atomic Bit Database & Lexicon**—interact as domain entities.

---

## 🗺️ Master Domain UML Class Diagram

```mermaid
classDiagram
    direction TB

    class ComedianUser {
        +UUID id
        +String stageName
        +Number baselineWPM
        +LexiconGraph personalLexicon
        +captureQuickIdea(rawInput) CaptureSnippet
        +startStageRecording(venue) StagePerformanceTape
        +buildSetlist(title, targetSec) ModularSetlist
    }

    class CaptureSnippet {
        +UUID id
        +IngestModality modality
        +String rawText
        +String audioClipUri
        +DateTime capturedAt
        +promoteToBit() AtomicBit
    }

    class AtomicBit {
        +UUID id
        +String title
        +String premise
        +BitState state
        +Number targetDurationSec
        +List~SetupLine~ setups
        +List~Punchline~ punchlines
        +List~BitTag~ tags
        +List~EditDeltaEntry~ continuousEditLog
        +List~StageMilestoneVersion~ stageMilestones
        +ContextHarness contextHarness
        +rollbackToEdit(deltaId) void
        +pinStageMilestone(tape, diff) StageMilestoneVersion
        +transitionState(newState) Boolean
        +calculateHitRate() LaughTier
    }

    class ContextHarness {
        +UUID bitId
        +List~String~ anchorNouns
        +List~String~ conceptualThemes
        +String emotionalTone
        +FloatArray vectorEmbedding
        +matchNaturalQuery(queryText) Float
    }

    class ModularSetlist {
        +UUID id
        +String title
        +Number targetDurationSec
        +Float freshnessRatio
        +List~SetlistSlot~ orderedSlots
        +calculateTotalTime() Number
        +computeFreshnessIndex() Float
    }

    class StagePerformanceTape {
        +UUID id
        +UUID plannedSetlistId
        +String venueName
        +RoomContextTag roomCondition
        +String rawAudioUri
        +Number totalDurationSec
        +WhisperTranscript transcript
        +List~AudienceReactionEvent~ reactions
        +ComposureTelemetry telemetry
    }

    class ComparatorEngine {
        +alignTapeWithScript(tape, setlistOrNull, bitVault) VisualDiffReport
        +autoDetectPerformedBits(transcript, bitVault) ModularSetlist
        +detectDroppedTags(tape, setlist) List~DroppedTagAlert~
        +harvestSkidRecoveries(tape, diff) List~SkidRecoveryHarvest~
    }

    class VisualDiffReport {
        +UUID id
        +UUID tapeId
        +UUID setlistId
        +Float scriptAdherenceScore
        +List~DiffSegment~ segments
        +List~DroppedTagAlert~ droppedTags
        +List~SkidRecoveryHarvest~ harvestedRiffs
    }

    ComedianUser "1" *-- "0..*" CaptureSnippet : captures
    ComedianUser "1" *-- "0..*" AtomicBit : owns in vault
    ComedianUser "1" *-- "0..*" ModularSetlist : assembles
    ComedianUser "1" *-- "0..*" StagePerformanceTape : records

    CaptureSnippet ..> AtomicBit : promotes to
    AtomicBit "1" *-- "1" ContextHarness : indexed by
    ModularSetlist "1" o-- "1..*" AtomicBit : sequences

    StagePerformanceTape "0..*" --> "0..1" ModularSetlist : tests on stage
    ComparatorEngine ..> StagePerformanceTape : analyzes audio & transcript
    ComparatorEngine ..> ModularSetlist : compares against script
    ComparatorEngine --> VisualDiffReport : generates
    VisualDiffReport ..> AtomicBit : updates stats & harvests tags
```

---

## 📂 Detailed Subsystem Class Diagrams (MVP Modules)

1. **[[01_Unified_Ingestion_and_Capture_Classes|01: Unified Ingestion, Morphing CTA & Delivery Notation Classes]]**
   * Covers the single-CTA Morphing Input Bar (Typed vs. Quick Voice Memo), Ghost Mode Distraction Shield, and the Inline Delivery Notation AST (`💥`, `🥊`, `💤`, `🗣️`, `🤸`).
2. **[[02_Audio_DSP_and_Performance_Tape_Classes|02: Audio DSP, Whisper ASR & Composure Telemetry Classes]]**
   * Covers Dual-Band Acoustic Isolation (Voice vs. Crowd Roar), millisecond word timestamps, Laughter Energy scoring, Pacing Flares, and Rushed Recovery detection.
3. **[[03_Comparator_Bridge_and_Diff_Classes|03: Comparator Bridge, Visual Diff & Skid Recovery Classes]]**
   * Covers Semantic vs. Verbatim Diff segments (Green Ad-Libs, Red Omissions), Dropped Tag Alerts, and Automated Skid Recovery Harvesting.
4. **[[04_Atomic_Bit_Database_and_Lexicon_Classes|04: Atomic Bit Database, State Machine, Lexicon & Highlighter Classes]]**
   * Covers the Living Object State Machine (`Draft ➔ Testing ➔ Stage Ready ➔ Retired`), Setlist Timeline, Semantic Context Harness, and Editor Lens Word Highlighting.
5. **[[05_Class_Architecture.canvas|05: Interactive Class Architecture Canvas]]**
   * Visual Obsidian Canvas containing the complete UML class hierarchy.
