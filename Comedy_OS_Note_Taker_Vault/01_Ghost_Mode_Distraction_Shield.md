---
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
         │         ──► Pocket / Handbag / Green-Room Audio Capture Lock
         ▼
[Stage Performance & Offline Capture]

> **[PRODUCT DECISION — STAGE MODE CANCELLED]:** "High-Contrast Stage Mode" (reading off the phone on stage/stool) is **cancelled** and will only return if users explicitly request it. Comedians do not perform with phones in their hands or on stage; during a set, the phone is busy recording audio from a pocket, handbag, or green room.
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
