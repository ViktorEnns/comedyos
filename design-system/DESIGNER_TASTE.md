# ComedyOS Designer Taste & Visual Reference Bible (`DESIGNER_TASTE.md`)

> **Purpose:** This living document codifies the visual, spatial, and interactive **Designer Taste** for ComedyOS. Every AI agent (Gemini Flash, Argon, or Claude) working on ComedyOS UI must consult this document before writing CSS or HTML to prevent generic "AI-slop" patterns and maintain surgical fidelity to our reference benchmarks.

---

## 1. The 5 Reference Pillars of ComedyOS Taste

ComedyOS is a **high-craft editorial workbench and stage telemetry instrument** for stand-up comedians. It synthesizes specific strengths from five reference systems:

| Reference Source | What We Emulate | Where It Applies in ComedyOS |
| :--- | :--- | :--- |
| **1. Variant (`8a6a23bf` & `e4b3ad22`)** | **Typographic Ledger & Spatial Hierarchy:** Warm obsidian canvas (`#1A1918`), bone alabaster ink (`#F5F2ED`), light-weight `Crimson Pro` serif headlines paired with tracked-out `Inter` small-caps eyebrows (`0.16em`), dotted leaders (`.dot-leader`), and crystal-clear mobile single-joke cards where location and hierarchy are immediately obvious. | Global layout shell, left wayfinding rail, top location breadcrumb, and Mobile Set-Builder / Single-Joke Cards. |
| **2. Granola (`notes.granola.ai`)** | **Frictionless Writing & Context Pills:** Distraction-free dark writing canvas (`#1A1918` / `#1C1C1C`), serif document titles with a compact row of subtle metadata pills directly underneath (`[Structured]` · `[Oct 29 · B-104]` · `[6.5 LPM]`), subtle left-margin `#` / structural markers in muted stone (`#5C5A55`), and a non-intrusive floating bottom audio/assistant pill bar. | The Joke Writing Canvas, Brain Dump / Transcript Editor, and Live Set Audio Recorder dock. |
| **3. beUI (`beui.dev`)** | **Inline Linguistic Word Highlighting:** Sharp (`2px` radius), low-opacity (`16%–22%` alpha) tinted rectangular background spans behind specific words inside flowing typography—highlighting linguistic mechanics without breaking reading rhythm. | **The ComedyOS Lexicon & Cadence Highlighter:** Inline highlighting of repeated words, syllable-heavy words (`>3 syl`), filler words, punchline connectors, and rhythmic tags. |
| **4. Little Might (`littlemight.com`)** | **Editorial Breathing Room & Rhythm:** Generous vertical spacing between thoughts, high typographic contrast between section headers and body prose, and clear visual pacing that never crowds the eye. | Onboarding landing experience, Masterclass Archive reading views, and 10-Minute Hyperfocus writing mode. |
| **5. Linear (`linear.app`)** | **Zero-Latency Keyboard Flows & Location Awareness:** Persistent breadcrumb header (`COMEDYOS / WORKBENCH / B-104`), `Cmd+K` command menu, single-key / chord shortcuts (`Alt+S`, `Alt+P`, `G then J`), optimistic local-first state transitions, and compact status indicators. | Global navigation, quick-entry triage, keyboard shortcut harness, and top-right sync indicator pill. |

---

## 2. Granola Writing UI Breakdown & Adaptation

From our inspection of Granola's dark note-taking UI (`Comedian-Nutzer: Forschung zu Persönlichkeit und Design für Comedy OS`):

1. **Document Header Stack:**
   - **Title:** Large, editorial serif (`Crimson Pro`, `28px–36px`, weight `300–400`, `#F5F2ED`, line-height `1.2`).
   - **Metadata Pill Bar (Directly Below Title, `12px` gap):** Compact horizontal strip of pill badges (`height: 24px`, `padding: 0 10px`, `border-radius: 4px`, `border: 1px solid rgba(245,242,237,0.12)`, `background: rgba(245,242,237,0.03)`, `font-size: 11px`, `color: #A19F9A`).
   - In ComedyOS, this metadata bar sits directly beneath the active joke's title and displays:
     - `[⚡ Stage Ready ▾]` (Status selector pill)
     - `[⏱ 01:15 · 8.2 LPM]` (Estimated stage duration & Laughs Per Minute target)
     - `[🎯 Lexicon Filter ▾]` (Toggle inline word highlights)
2. **Left-Gutter Structural Markers:**
   - Instead of wrapping every section in a bordered box, Granola places muted typographic sigils (`#`, `S`, `B`, `P`, `T`) in a `28px` left margin (`color: rgba(245,242,237,0.28)`).
3. **Floating Bottom Audio & AI Dock:**
   - A centered, pill-shaped floating bar at the bottom of the viewport (`max-width: 560px`) containing:
     - Live audio waveform pill (`[ |||·| ^ ]` with green/sage pulse when recording a set or voice memo).
     - Quick command / linguistic query input (`"Trim syllables, find callbacks, or test punchline..."`).
     - Contextual action button (`[✂ Trim Fat]`).

---

## 3. `beui.dev` Inline Word-Highlighting System (The Lexicon Harness)

Comedians edit for **word economy**—counting syllables, cutting filler words, and placing the laugh-trigger word at the very end of the punchline. Inspired by `beui.dev`, ComedyOS highlights words inline using tight, `2px`-chamfered translucent spans:

```css
/* Base Inline Linguistic Token Highlight (beui.dev pattern) */
.word-hl {
  display: inline;
  padding: 1px 5px;
  margin: 0 -1px;
  border-radius: 2px;
  font-weight: inherit;
  transition: background-color 150ms ease, color 150ms ease;
}

/* 1. Repetition / Callback Echo (Sky Tint — tracks repeated key nouns/phrases) */
.word-hl-repeat {
  background-color: rgba(147, 197, 253, 0.18);
  color: #BFDBFE;
  border-bottom: 1px solid rgba(147, 197, 253, 0.45);
}

/* 2. Heavy Multi-Syllable Drag (>3 Syllables — Amber/Peach Tint — slows down punchline) */
.word-hl-heavy {
  background-color: rgba(253, 186, 116, 0.18);
  color: #FED7AA;
  border-bottom: 1px solid rgba(253, 186, 116, 0.45);
}

/* 3. Fluff / Filler Word Alert ("like", "basically", "actually", "just" — Coral Tint) */
.word-hl-filler {
  background-color: rgba(226, 109, 92, 0.18);
  color: #FCA5A5;
  text-decoration: underline wavy rgba(226, 109, 92, 0.55);
}

/* 4. Laugh Trigger / Punch Word (Sage Mint Tint — final impact word) */
.word-hl-punch {
  background-color: rgba(159, 175, 154, 0.22);
  color: #ECFDF5;
  border-bottom: 1px solid rgba(159, 175, 154, 0.65);
}
```

---

## 4. Variant `e4b3ad22` Single-Joke Mobile Cards (Set Builder & Mobile Keep)

On mobile viewports (and in the Set Builder column), jokes must not look like cramped desktop tables. Each joke card follows the **Variant Single-Joke Card Anatomy**:
1. **Top Meta Hairline Row:** Monospace catalog index (`B-104`) on the left · Duration & LPM badge (`01:20 · 7.5 LPM`) on the right.
2. **Primary Hook / Setup Line:** `Crimson Pro` `20px` in `#F5F2ED` (2-line clamp or full expansion).
3. **Active Punchline Preview:** Indented `12px` with a `1px solid var(--accent)` left rule, rendered in italic `Crimson Pro` `18px` (`#9FAF9A`).
4. **Bottom Tactile Action Strip:** Clear `.btn-compact` buttons (`[Stage Mode]`, `[Edit Circuit]`, `[+ Add to Set]`) so the comedian immediately knows what can be tapped.

---

## 5. Anti-Slop & Taste Enforcement Rules

1. **Buttons Must Look Like Buttons:** Never leave interactive controls as unstyled floating text. Every interactive trigger uses `.btn` (`1px solid rgba(245, 242, 237, 0.25)`, `2px` radius, `10px` uppercase tracked `Inter`). Primary actions use `.btn-primary` (sage tint fill + `rgba(159, 175, 154, 0.65)` border).
2. **Always Answer "Where Am I?":** Every screen must display the persistent top wayfinding bar showing:
   - Brand + Active Workspace Switcher (`[Workbench]` · `[Journal Vault]` · `[Set Builder]` · `[Archive]`)
   - Breadcrumb of current item (`B-104 · Undisputed Champion`)
   - Compact right-hand account & cloud sync pill (`● Viktor · Synced`).
3. **Solve Auth Before the Workbench:** Never clutter the writing workbench with giant database configuration forms or login banners. Unauthenticated users see the dedicated **ComedyOS Onboarding & Account Gate** first; once signed in, the workbench is 100% dedicated to writing and performing.
