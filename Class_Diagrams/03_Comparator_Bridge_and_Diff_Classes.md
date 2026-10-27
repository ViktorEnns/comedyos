---
id: CLASS-BRIDGE-003
title: Comparator Bridge, Visual Diff & Skid Recovery Classes
type: class-diagram
status: active
parent: "[[00_Master_Domain_Class_Diagram]]"
tags: [comedy-os, class-diagram, comparator, visual-diff, dropped-tags, skid-recovery]
---

# ⚡ 03: Comparator Bridge, Visual Diff & Skid Recovery Classes

> **Architectural Scope:** Models the "Secret Sauce" of Comedy OS: aligning the **Written Script / Setlist** against the **Spoken Stage Performance Tape**, distinguishing semantic rephrasing from genuine omissions, alerting on **Dropped Tags**, and harvesting improvised **Skid Recovery Riffs**.

---

## 🗺️ Subsystem Class Diagram

```mermaid
classDiagram
    direction TB

    class ComparatorEngine {
        +Float semanticSimilarityThreshold "0.82"
        +generateDiffReport(setlistOrNull, tape, bitVault) VisualDiffReport
        +autoDetectPerformedBits(transcript, bitVault) ModularSetlist
        +alignBitExecution(atomicBit, transcriptWindow) BitExecutionDiff
        +detectDroppedTags(atomicBit, executionDiff) List~DroppedTagAlert~
        +extractSkidRecoveries(executionDiff, reactions) List~SkidRecoveryHarvest~
    }

    class VisualDiffReport {
        +UUID reportId
        +UUID tapeId
        +UUID setlistId
        +DateTime generatedAt
        +List~BitExecutionDiff~ bitDiffs
        +List~DroppedTagAlert~ omittedTagAlerts
        +List~SkidRecoveryHarvest~ adLibHarvests
        +getOverallScriptCompletionRate() Float
    }

    class BitExecutionDiff {
        +UUID bitId
        +Number stageStartMs
        +Number stageEndMs
        +List~DiffSegment~ segments
        +Float cumulativeLaughSeconds
    }

    class DiffSegment {
        +UUID segmentId
        +DiffSegmentType diffType
        +String writtenScriptText
        +String spokenTranscriptText
        +Float associatedLaughSeconds
        +LaughTier achievedTier
    }

    class DiffSegmentType {
        <<enumeration>>
        VERBATIM_DELIVERY
        SEMANTIC_PARAPHRASE
        STAGE_AD_LIB_GREEN
        OMITTED_LINE_RED
    }

    class DroppedTagAlert {
        +UUID alertId
        +UUID bitId
        +UUID droppedTagId
        +String omittedTagText
        +DropReason cause
        +Float estimatedLostLaughSeconds
        +requeueForNextSet() void
    }

    class DropReason {
        <<enumeration>>
        CROWD_APPLAUSE_OVERTALK
        RED_LIGHT_TIME_PRESSURE
        STAGE_MEMORY_SLIP
        PREMISE_BAILOUT
    }

    class SkidRecoveryHarvest {
        +UUID harvestId
        +Number deadAirDurationBeforeMs
        +String improvisedComebackText
        +Float recoveryLaughSeconds
        +promoteToEscapeTag(targetBitId) BitTag
    }

    ComparatorEngine --> VisualDiffReport : produces
    VisualDiffReport "1" *-- "1..*" BitExecutionDiff : contains
    VisualDiffReport "1" *-- "0..*" DroppedTagAlert : surfaces
    VisualDiffReport "1" *-- "0..*" SkidRecoveryHarvest : captures

    BitExecutionDiff "1" *-- "1..*" DiffSegment : composed of
    DiffSegment --> DiffSegmentType : classified as
    DroppedTagAlert --> DropReason : diagnosed with
```

---

## 🔍 Key Design Notes

1. **Solving the Verbatim vs. Organic Riffing Conflict (`SEMANTIC_PARAPHRASE`):**
   - Stand-up comics rarely recite lines word-for-word like stage actors.
   - `ComparatorEngine` uses `semanticSimilarityThreshold` (0.82) to classify natural conversational rephrasing as `SEMANTIC_PARAPHRASE` (rendered in calm plain text) rather than penalizing the comic with a false `OMITTED_LINE_RED`.
2. **One-Tap Ad-Lib Promotion (`STAGE_AD_LIB_GREEN` & `SkidRecoveryHarvest`):**
   - When a comic improvises a new line on stage (`STAGE_AD_LIB_GREEN`) or saves a flatline with a self-aware comeback (`SkidRecoveryHarvest`), they can promote it directly into the `AtomicBit` vault with a single tap.
3. **Diagnostic `DropReason` on `DroppedTagAlert`:**
   - Tells the comic *why* they forgot a tag: either the crowd cheered so loudly they transitioned too early (`CROWD_APPLAUSE_OVERTALK`), or they ran out of clock (`RED_LIGHT_TIME_PRESSURE`).
4. **Unplanned Setlist Auto-Detection (`autoDetectPerformedBits`):**
   - If a comic records a set without pre-selecting a `ModularSetlist`, `ComparatorEngine` scans the spoken `WhisperTranscript` against the `ContextHarness` of all `AtomicBit` objects in their vault, reconstructs the performed setlist order automatically, and still generates the full `VisualDiffReport`.

---

## 🔗 Related Feature Notes
* [[Comedy_OS_Note_Taker_Vault/30_The_Comparator_Bridge|30: The Comparator Bridge Overview]]
* [[Comedy_OS_Note_Taker_Vault/31_Visual_Diff_Report|31: Visual Diff Report]]
* [[Comedy_OS_Note_Taker_Vault/32_Dropped_Tag_Alerts|32: Dropped Tag Alerts]]
* [[Comedy_OS_Note_Taker_Vault/33_Reaction_Waveform_Alignment|33: Reaction Waveform Alignment]]
