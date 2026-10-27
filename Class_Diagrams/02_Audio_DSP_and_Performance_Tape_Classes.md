---
id: CLASS-AUDIO-002
title: Audio DSP, Whisper ASR & Composure Telemetry Classes
type: class-diagram
status: active
parent: "[[00_Master_Domain_Class_Diagram]]"
tags: [comedy-os, class-diagram, audio-dsp, whisper-asr, telemetry, laughter-isolation]
---

# 🔊 02: Audio DSP, Whisper ASR & Composure Telemetry Classes

> **Architectural Scope:** Models the Granola-style performance recording pipeline: **Dual-Band Acoustic Isolation** (separating comic speech from crowd roar), **Whisper ASR millisecond word transcription**, **Post-Set Composure Telemetry**, and **Conversational Set Tape Q&A**.

---

## 🗺️ Subsystem Class Diagram

```mermaid
classDiagram
    direction TB

    class StagePerformanceTape {
        +UUID id
        +String venueName
        +String city
        +DateTime recordedAt
        +RoomContextTag roomCondition
        +String rawAudioFileUri
        +Number durationSeconds
        +WhisperTranscript transcript
        +List~AudienceReactionEvent~ reactionTimeline
        +ComposureTelemetry composureMetrics
        +getLaughsPerMinute() Float
        +getTotalLaughSeconds() Float
    }

    class RoomContextTag {
        <<enumeration>>
        HOT_INTIMATE_CELLAR
        STANDARD_CLUB
        COLD_OPEN_MIC
        ECHO_CORPORATE_HALL
        HOSTILE_CROWD
    }

    class DualBandDSPIsolator {
        +FloatRange vocalBandHz "200Hz - 3.5kHz"
        +FloatRange crowdRoarBandHz "500Hz - 8kHz"
        +Float silenceThresholdDb "-38.0dB"
        +splitAudioStream(rawAudioUri) DualTrackStream
        +extractReactionEvents(crowdTrack) List~AudienceReactionEvent~
    }

    class WhisperTranscript {
        +UUID tapeId
        +String fullText
        +Number averageWPM
        +List~TimestampedWord~ words
        +getWordsInWindow(startMs, endMs) List~TimestampedWord~
    }

    class TimestampedWord {
        +String word
        +Number startMs
        +Number endMs
        +Float confidenceScore
        +Number localWPM
    }

    class AudienceReactionEvent {
        <<abstract>>
        +UUID eventId
        +Number startMs
        +Number endMs
        +Float durationSeconds
        +Float peakDecibels
    }

    class LaughBurstEvent {
        +LaughTier tier
        +Float laughEnergyScore
        +Boolean isDuchenneRoar
        +Boolean isPoliteChuckleOrClapter
    }

    class DeadAirValleyEvent {
        +Boolean isDeliberatePause
        +Boolean isUnintendedBomb
    }

    class ComposureTelemetry {
        +Number baselineWPM
        +Number breathePauseCount
        +List~PacingFlareFlag~ pacingFlares
        +List~RushedRecoveryFlag~ rushedRecoveries
        +analyzeComposure(transcript, reactions) void
    }

    class PacingFlareFlag {
        +Number timestampMs
        +Float wpmSpikePercentage "> 25% spike"
        +String triggeringLineText
    }

    class RushedRecoveryFlag {
        +Number timestampMs
        +Float recoveryLatencyMs "< 800ms"
        +String missedPunchlineText
    }

    class SetTapeChatService {
        +querySetTape(tapeId, userPrompt) ChatResponse
        +compareAcrossVenueRuns(bitId) VenueComparisonSummary
    }

    StagePerformanceTape --> RoomContextTag : calibrated by
    StagePerformanceTape "1" *-- "1" WhisperTranscript : contains
    StagePerformanceTape "1" *-- "0..*" AudienceReactionEvent : logs
    StagePerformanceTape "1" *-- "1" ComposureTelemetry : evaluates

    DualBandDSPIsolator ..> StagePerformanceTape : processes raw audio
    WhisperTranscript "1" *-- "1..*" TimestampedWord : composed of

    AudienceReactionEvent <|-- LaughBurstEvent
    AudienceReactionEvent <|-- DeadAirValleyEvent

    ComposureTelemetry "1" *-- "0..*" PacingFlareFlag : flags
    ComposureTelemetry "1" *-- "0..*" RushedRecoveryFlag : flags
    SetTapeChatService ..> StagePerformanceTape : queries context
```

---

## 🔍 Key Design Notes

1. **Eliminating the Cringe Barrier (`WhisperTranscript` + `SetTapeChatService`):**
   - Instead of forcing the comedian to listen to 15 minutes of raw audio, `WhisperTranscript` provides millisecond-aligned words so the comic can **read** the set or query `SetTapeChatService` (*"Where did I rush during the second bit?"*).
2. **Acoustic Truth vs. Clapter (`LaughBurstEvent`):**
   - Distinguishes genuine `isDuchenneRoar` (> -6dB, sustained > 2.5s) from `isPoliteChuckleOrClapter` (short decay or applause without vocal roar), preventing the destructive belief that *"every noise from the crowd means the joke is ready."*
3. **Post-Set Composure Diagnostics (`ComposureTelemetry`):**
   - Automatically flags **Pacing Flares** (speaking speed spiking by $\ge 25\%$ after dead air) and **Rushed Recoveries** (jumping into the next setup in $< 0.8\text{s}$), turning stage panic into neutral laboratory telemetry.

---

## 🔗 Related Feature Notes
* [[Comedy_OS_Note_Taker_Vault/10_Audio_Forward_Ingestion_Layer|10: Audio-Forward Ingestion Layer]]
* [[Comedy_OS_Note_Taker_Vault/11_Audience_Laughter_and_Silence_Isolation|11: Audience Laughter & Silence Isolation]]
* [[Comedy_OS_Note_Taker_Vault/13_Whisper_ASR_Speech_To_Text|13: Whisper ASR Speech-to-Text]]
* [[Comedy_OS_Note_Taker_Vault/14_Conversational_Chat_With_Set_Tape|14: Conversational Chat With Set Tape]]
* [[Comedy_OS_Note_Taker_Vault/33_Reaction_Waveform_Alignment|33: Reaction Waveform Alignment]]
