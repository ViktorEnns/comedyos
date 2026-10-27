---
title: System Architecture & Data Flow Map
sidebar_position: 2
icon: "🗺️"
---

# 🗺️ Comedy OS — System Data Flow & State Map

This document tracks the high-level semantic data flow, boundary layers, and feature state machines across Comedy OS. It complements the automated import scanner in `DEPENDENCY_GRAPH.md`.

## 1. High-Level System Data Flow

```mermaid
graph TD
  subgraph UI["UI Components"]
    CD["CaptureDrawer"]
    SL["SetlistTimeline"]
    ED["DistractionFreePad"]
  end

  subgraph StateHooks["State & Services"]
    ACS["AudioCaptureService"]
    NLS["NotationLexiconService"]
    SBS["SetlistBuilderService"]
  end

  subgraph Engines["Core Engines & Workers"]
    AE["AudioEngine (Stream ref)"]
    OCRE["OCREngine (Scan parser)"]
    WASM["Whisper ASR Worker"]
  end

  subgraph Storage["Storage & Pipeline Bridge"]
    DB[("SQLite Local DB")]
    FS[("File System (Markdown Vault)")]
    PY["Python Pipeline (Audio & Whisper Sync)"]
  end

  CD --> ACS
  SL --> SBS
  ED --> NLS

  ACS --> AE
  ACS --> WASM
  ED --> DB
  NLS --> DB
  SBS --> DB

  WASM --> DB
  PY --> DB
  PY --> FS
```

## 2. Audio Capture & Transcription State Machine

```mermaid
stateDiagram-v2
  [*] --> Idle : App launched
  Idle --> Recording : onRecordButtonClick
  Recording --> Paused : onPauseClick
  Paused --> Recording : onResumeClick
  Recording --> Processing : onStopClick
  Processing --> Transcribing : AudioBuffer flush
  Transcribing --> Ready : Whisper transcript emitted
  Transcribing --> Error : Whisper failure
  Error --> Ready : Fallback to local audio cache
  Ready --> Idle : Awaiting next capture
```

## 3. Jimmy Carr Joke Circuit State Machine

```mermaid
stateDiagram-v2
  [*] --> DirectSetupFocus : User taps "+ New Joke" / Cmd+N
  DirectSetupFocus --> SetupTyped : Comic writes setup (expectation trap)
  SetupTyped --> BridgeInsertion : Cmd+Shift+B (insert bridge/misdirect)
  BridgeInsertion --> PunchlineDrafting : Tab / Enter
  SetupTyped --> PunchlineDrafting : Enter
  PunchlineDrafting --> VariantStacked : Cmd+Shift+P (add punch alternative)
  PunchlineDrafting --> TagAppended : Cmd+Shift+T (append topper)
  VariantStacked --> StageArmed : Tap [STAGE ACTIVE] toggle
  TagAppended --> StageArmed : Verify laugh wave order
  StageArmed --> VaultSync : Debounced commit to SQLite / Vault
  VaultSync --> [*]
```

