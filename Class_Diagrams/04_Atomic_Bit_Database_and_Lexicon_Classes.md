---
id: CLASS-VAULT-004
title: Atomic Bit Database, State Machine, Lexicon & Highlighter Classes
type: class-diagram
status: active
parent: "[[00_Master_Domain_Class_Diagram]]"
tags: [comedy-os, class-diagram, atomic-bit, state-machine, lexicon, context-harness, word-highlighter, versioning]
---

# 🧱 04: Atomic Bit Database, State Machine, Lexicon & Highlighter Classes

> **Architectural Scope:** Models jokes as living domain objects governed by a **Finite State Machine**, dual-tier **FigJam-style Edit Rollback + Stage Milestone Versioning**, **Modular Setlist Timelines**, the **Semantic Context Harness (Lexicon)**, and **MVP Tier-1 Word Highlighting**.

---

## 🗺️ Subsystem Class Diagram

```mermaid
classDiagram
    direction TB

    class AtomicBit {
        +UUID id
        +String title
        +String premise
        +BitState currentState
        +Number targetDurationSec
        +List~String~ setupLines
        +List~Punchline~ punchlines
        +List~BitTag~ tags
        +List~EditDeltaEntry~ continuousEditLog
        +List~StageMilestoneVersion~ stageMilestones
        +ContextHarness contextHarness
        +rollbackToEdit(deltaId) void
        +pinStageMilestone(tape, diff) StageMilestoneVersion
        +evaluateStateTransition() BitState
        +isStaleBankerBit() Boolean
    }

    class EditDeltaEntry {
        +UUID deltaId
        +DateTime timestamp
        +String textPatchDiff
        +String authorAction "Desk Edit / Auto-Save"
    }

    class StageMilestoneVersion {
        +UUID milestoneId
        +String versionLabel "e.g. Stage Run v1, v2"
        +UUID tapeId
        +String venueName
        +DateTime performedAt
        +String frozenScriptSnapshot
        +Float laughDurationSec
        +LaughTier achievedTier
        +Number droppedTagCount
    }

    class BitState {
        <<enumeration>>
        DRAFT
        TESTING
        STAGE_READY
        RETIRED
    }

    class Punchline {
        +UUID id
        +String text
        +String deliveryNotation
        +LaughTier averageTier
        +Float avgLaughSeconds
    }

    class BitTag {
        +UUID id
        +String text
        +Boolean isAdLibHarvest
        +Boolean isEscapeTag
        +String discoveredAtVenue
    }

    class ModularSetlist {
        +UUID id
        +String name
        +Boolean isAutoInferredFromTape
        +Number targetSetSeconds
        +List~SetlistSlot~ slots
        +getSetFreshnessIndex() Float
        +reorderSlot(fromIdx, toIdx) void
    }

    class SetlistSlot {
        +Number positionIndex
        +UUID bitId
        +Number allocatedSeconds
        +String transitionBridgeNote
    }

    class LexiconGraph {
        +UUID userId
        +Map~String,Integer~ wordFrequencyMap
        +List~String~ comicVernacularSet
        +buildContextHarness(bit) ContextHarness
        +searchByNaturalMemory(descriptionQuery) List~AtomicBit~
    }

    class ContextHarness {
        +UUID bitId
        +List~String~ registeredLexiconAnchors
        +List~String~ inferredConceptTags
        +String emotionalSubtext
        +FloatArray semanticVector
    }

    class WordHighlightEngine {
        +EditorLensMode activeLens
        +analyzeTextForHighlights(text, harness) List~WordHighlightToken~
    }

    class EditorLensMode {
        <<enumeration>>
        FLOW_WRITING_ZERO_HIGHLIGHTS
        INSPECTOR_LEXICON_LENS_MVP
    }

    class WordHighlightToken {
        +String word
        +Number charStart
        +Number charEnd
        +HighlightReason reason
    }

    class HighlightReason {
        <<enumeration>>
        TIER_1_LEXICON_ANCHOR_MVP
    }

    AtomicBit --> BitState : governed by
    AtomicBit "1" *-- "1..*" Punchline : delivers
    AtomicBit "1" *-- "0..*" BitTag : layered with
    AtomicBit "1" *-- "0..*" EditDeltaEntry : logs every desk edit
    AtomicBit "1" *-- "0..*" StageMilestoneVersion : pins stage runs
    AtomicBit "1" *-- "1" ContextHarness : fingerprinted by

    ModularSetlist "1" *-- "1..*" SetlistSlot : sequences
    SetlistSlot --> AtomicBit : references

    LexiconGraph ..> ContextHarness : constructs
    WordHighlightEngine --> EditorLensMode : controlled by
    WordHighlightEngine ..> ContextHarness : reads anchor words
    WordHighlightEngine --> WordHighlightToken : emits
    WordHighlightToken --> HighlightReason : styled by
```

---

## 🔍 Key Design Notes

1. **Dual-Tier Versioning (`EditDeltaEntry` vs. `StageMilestoneVersion`):**
   - **Continuous Desk Rollback (`EditDeltaEntry`):** Every text change in the editor is logged as a lightweight delta patch (just like FigJam's undo/activity history), allowing the comic to roll back accidental deletions without cluttering the UI.
   - **Visually Distinct Stage Milestones (`StageMilestoneVersion`):** When a bit is actually tested on a `StagePerformanceTape`, a high-status **Stage Milestone Version** (`Stage Run v1`, `Stage Run v2`) is pinned in the database and highlighted prominently in the version timeline with its venue badge and laugh score.
2. **MVP Scope Discipline for Word Highlighting (`TIER_1_LEXICON_ANCHOR_MVP`):**
   - To keep potential error sources to an absolute minimum in the MVP, `WordHighlightEngine` only highlights **Tier 1 Lexicon Anchor Words** (words registered in the joke's `ContextHarness`) when `INSPECTOR_LEXICON_LENS_MVP` is toggled.
   - Tiers 2–5 (Substitution candidates, overused filler crutches, clean-set profanity flags, and OCR gaps) are cleanly deferred to Post-MVP.
3. **Context-Free Memory Retrieval (`LexiconGraph` + `ContextHarness`):**
   - Calling `searchByNaturalMemory("feeling stripped of dignity at the airport")` matches the `ContextHarness` even if the joke text only contains words like *TSA, belt loops, and socks*.

---

## 🔗 Related Feature Notes
* [[Comedy_OS_Note_Taker_Vault/24_Lexicon_Harness_and_Word_Highlighter|24: Lexicon Context Harness & Word Highlighting]]
* [[Comedy_OS_Note_Taker_Vault/40_Atomic_Bit_Database|40: Atomic Bit Vault & Object Schema]]
* [[Comedy_OS_Note_Taker_Vault/41_Jokes_As_Living_Objects_State_Machine|41: Jokes as Living Objects State Machine]]
* [[Comedy_OS_Note_Taker_Vault/42_Drag_And_Drop_Modular_Setlist_Timeline|42: Drag-and-Drop Modular Setlist Timeline]]
* [[Comedy_OS_Note_Taker_Vault/43_Conversational_Semantic_Search_And_Vector_Embeddings|43: Conversational Semantic Search & Vector Embeddings]]
