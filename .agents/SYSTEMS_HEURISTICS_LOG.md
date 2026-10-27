<!-- PROJECT HEURISTICS & ANTI-PATTERNS LOG -->
<!-- Last audited: 2026-10-23 | Keep total file length under 150 lines -->

## Audio Engine & Offline Sync

### 1. Invariants (Hard Rules)
- NEVER bind 60fps audio stream ticks to top-level view state.
- NEVER perform direct SQLite reads inside UI animation render loops.
- ALWAYS store playback scrub positions in mutable refs; commit to SQLite only on gesture release.

### 2. Failure Post-Mortem & Fix
- **Failed Approach:** Naive React useEffect listening directly to audio buffer ticks.
- **Root Failure:** Re-rendered the entire root component tree 60 times/sec, causing severe frame drops.
- **Validated Pattern:** Decouple UI state using a custom pub/sub event bus; throttle updates to 100ms for UI indicators.

### 3. Verification Assertions
- Render count of parent container must remain 1 during active playback.
- Audio buffer sync must gracefully resume when device enters airplane mode.

---

## Gesture UI & Setlist Organization

### 1. Invariants (Hard Rules)
- NEVER mutate the active setlist array in-place during drag-and-drop animations.
- ALWAYS use optimistic local state for list reordering, deferring backend/file writes until touch release.

### 2. Failure Post-Mortem & Fix
- **Failed Approach:** Writing intermediate drag coordinates to local SQLite database via asynchronous transactions.
- **Root Failure:** SQLite file lock blocked gesture frames, causing touch stutter and inverted item drops.
- **Validated Pattern:** Hold dragged indices in memory-only spring animations; serialize new order to disk in a single batch on gesture end.

### 3. Verification Assertions
- List items maintain steady 60fps transform animations during rapid continuous dragging.

---

## Local-First Storage & OPFS Sync

### 1. Invariants (Hard Rules)
- NEVER execute unbatched atomic note writes across multiple web worker boundaries.
- ALWAYS wrap multi-note updates in single transaction blocks with write-ahead logging (WAL) enabled.

### 2. Failure Post-Mortem & Fix
- **Failed Approach:** Individual asynchronous promises dispatched per keystroke to OPFS handle.
- **Root Failure:** File descriptor contention corrupted concurrent index records during rapid typing.
- **Validated Pattern:** Buffer typed delta chunks in memory; flush to OPFS using debounced 400ms atomic transactions.

### 3. Verification Assertions
- Zero data loss or torn writes under continuous fast typing and abrupt tab closure.
