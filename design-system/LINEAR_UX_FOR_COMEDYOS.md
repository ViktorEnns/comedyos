# Linear UX Best-Ofs Adapted for ComedyOS (`LINEAR_UX_FOR_COMEDYOS.md`)

> **Purpose:** Linear (`linear.app`) is the gold standard for fast, keyboard-first, low-friction workflow software. Stand-up comedians have high ADHD prevalence and work in **10-minute bursts of hyperfocus**. If an app forces them to hunt through menus or wait for spinners, they abandon it. This specification translates Linear's core UX mechanics directly into ComedyOS.

---

## 1. The 6 Core Linear UX Pillars for ComedyOS

### Pillar 1: Unambiguous Location Awareness (Breadcrumb + Left Rail / Switcher)
- **How Linear Does It:** At any moment in Linear, the top-left header reads `Workspace > Team > Active View > Issue ID` (e.g., `Linear / Core / Triage / LIN-402`), paired with a collapsible sidebar (`[` key) showing *Inbox*, *My Issues*, *Views*, and *Projects*.
- **How ComedyOS Adapts It:**
  - **Top Wayfinding Strip:**
    - Left: `COMEDYOS` brand mark + Segmented View Switcher (`[01 Workbench]` · `[02 Journal Vault]` · `[03 Set Builder]` · `[04 Archive]`).
    - Center-Left Breadcrumb: `/ B-104 · Undisputed Champion · [Structured ▾]`.
    - Right: Compact Sync & Profile Badge (`[● Synced · @viktorenns]`) + `[+ New Joke (C)]`.
  - **Result:** The comedian never wonders *"Where am I right now, and how do I get to my saved jokes or settings?"*

### Pillar 2: The Omni-Command Bar (`Cmd+K` / `Ctrl+K`)
- **How Linear Does It:** Pressing `Cmd+K` opens a centered modal palette with instant fuzzy search across every action, view, and issue—showing keyboard shortcuts on the right edge of every item so users learn shortcuts organically.
- **How ComedyOS Adapts It:**
  - Pressing `Cmd+K` (or clicking `[⌘K Command]` in the header) opens the **ComedyOS Command Ledger**:
    - **Switch View:** `Go to Workbench (G then W)`, `Go to Journal Vault (G then J)`, `Go to Set Builder (G then S)`, `Toggle Mobile Keep Preview (M)`.
    - **Joke Actions:** `Create New Joke (C)`, `Split Setup/Punch at Cursor (Cmd+Enter)`, `Highlight Repeated Words (Alt+1)`, `Highlight Heavy Syllables >3 (Alt+2)`, `Highlight Filler Words (Alt+3)`.
    - **Jump to Bit:** Instant fuzzy search over all jokes in the vault by title, tag, or `B-XXX` code.

### Pillar 3: Single-Key "Verbs" & Vim-Style Navigation Chords
- **How Linear Does It:** When no text input is focused, single keys trigger immediate actions (`C` = Create issue, `/` = Search, `?` = Shortcut help), and `G` + key chords navigate (`G` then `I` = Inbox). When inside an editor, modifier chords (`Alt+...` or `Cmd+...`) perform structural mutations.
- **How ComedyOS Adapts It:**

| Context | Shortcut | Action in ComedyOS |
| :--- | :--- | :--- |
| **Global (Anywhere)** | `Cmd/Ctrl + K` | Open Command Palette & Fuzzy Joke Search |
| **Global (Anywhere)** | `Cmd/Ctrl + J` | Toggle Split Journal Vault Drawer |
| **Global (Outside Input)** | `C` | Commit current joke & open fresh canvas (`+ New Joke`) |
| **Global (Outside Input)** | `1` / `2` / `3` / `4` | Switch top-level view: `1` Workbench, `2` Journal, `3` Set Builder, `4` Archive |
| **Inside Brain Dump** | `Cmd/Ctrl + Enter` | Split raw text at cursor into **Setup** (before) & **Punchline** (after) |
| **Inside Brain Dump** | `Alt + S` | Promote selected phrase (or current line) → **Set-up** |
| **Inside Brain Dump** | `Alt + B` | Promote selected phrase (or current line) → **Bridge** |
| **Inside Brain Dump** | `Alt + P` | Promote selected phrase (or current line) → **Punchline** |
| **Inside Brain Dump** | `Alt + T` | Promote selected phrase (or current line) → **Tag** |
| **Inside Circuit Block** | `Enter` | Spawn next sequential Punchline/Tag block below |

### Pillar 4: Zero-Latency Optimistic Local-First Sync
- **How Linear Does It:** Every keystroke and state change mutates a local IndexedDB/localStorage store in `<16ms` and updates the UI immediately. Background sync to the cloud happens asynchronously without blocking the user.
- **How ComedyOS Adapts It:**
  - `localStorage` (`comedyos_journal_v1`) updates synchronously on every change.
  - Supabase upserts (`journal_entries` + `joke_blocks`) run debounced (`300ms`) in the background.
  - A tiny status dot in the top-right pill transitions quietly: `● Saving...` (amber) → `● Synced` (sage green) → `○ Offline (Saved Locally)` (muted grey).

### Pillar 5: Triage Mode for "10-Minute Hyperfocus" Bursts
- **How Linear Does It:** Linear's *Inbox / Triage* view presents one incoming item at a time with rapid keyboard actions (*Accept*, *Snooze*, *Merge*, *Decline*) so users can process 20 items in 3 minutes.
- **How ComedyOS Adapts It:**
  - Comedians capture messy voice memos and 2 AM text seeds on mobile, then burn out if they see a wall of 100 unorganized notes.
  - **Seed Triage Mode:** Presents one raw mobile seed at a time with 1-click actions: `[Promote to Workbench (Enter)]`, `[Merge into Existing Bit (M)]`, `[Archive / Retire (Del)]`, `[Next Seed (→)]`.

### Pillar 6: Opinionated Lifecycle Statuses (Zero Configuration Fatigue)
- **How Linear Does It:** Enforces a clean, fixed progression: *Triage → Backlog → Todo → In Progress → Done → Canceled*.
- **How ComedyOS Adapts It:**
  - Every joke moves through 4 opinionated stage statuses with distinct visual indicators:
    1. `○ SEED` (Raw mobile note / voice memo / notebook scan)
    2. `◐ STRUCTURED` (Broken into Setup → Bridge → Punchline blocks)
    3. `● STAGE READY` (Trimmed for word economy, tested on stage, active punchline locked)
    4. `✕ RETIRED` (Archived / harvested for parts)
