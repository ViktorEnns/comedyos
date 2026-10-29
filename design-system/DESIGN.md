---
version: "2.0"
name: "comedyos-typographic-ledger"
description: "An archival, late-night literary monograph and precision typographic ledger for stand-up comedians. Deep warm charcoal canvas (#1A1918), 4-tier warm bone luminance, 0.5px sub-pixel hairlines, dotted index leaders, and tactile 2px-chamfered controls—zero SaaS card boxes, zero drop shadows."
inspiration_sources:
  - "Variant 8a6a23bf (COMEDYOS Archive v1.0 — 3-Pane Editorial Workspace)"
  - "Variant 568d8c7f (ComedyOS System Specimen v1.0 — Form & Ledger Grammar)"
  - "Stripe Press & Craig Mod Literary Monographs (Editorial Numerals & Dot Leaders)"
  - "Linear & iA Writer (Sub-pixel 0.5px Hairline Discipline & Distraction-Free Focus)"

colors:
  canvas: "#1A1918"
  surface-hover: "#201F1E"
  surface-whisper: "rgba(35, 34, 32, 0.30)"
  ink-primary: "#F5F2ED"
  ink-secondary: "#8C8782"
  ink-prose: "#A19F9A"
  ink-muted: "#5C5A55"
  ink-recessed: "#4A4845"
  hairline: "rgba(245, 242, 237, 0.10)"
  hairline-solid: "#33312E"
  hairline-dot: "rgba(245, 242, 237, 0.20)"
  hairline-btn: "rgba(245, 242, 237, 0.25)"
  hairline-btn-hover: "rgba(245, 242, 237, 0.75)"
  accent-sage: "#9FAF9A"
  accent-sage-border: "rgba(159, 175, 154, 0.65)"
  accent-sage-fill: "rgba(159, 175, 154, 0.06)"
  accent-sage-fill-hover: "rgba(159, 175, 154, 0.14)"
  accent-brass: "#B4A28A"
  alert-terracotta: "#E26D5C"

typography:
  fontFamily:
    serif: "'Crimson Pro', Georgia, serif"
    sans: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    mono: "'JetBrains Mono', monospace"
  scales:
    display-hero: { fontFamily: "serif", fontSize: "clamp(48px, 5vw, 72px)", fontWeight: "300", lineHeight: "1.02", letterSpacing: "-0.025em", color: "ink-primary" }
    page-title: { fontFamily: "serif", fontSize: "48px", fontWeight: "300", lineHeight: "1.1", letterSpacing: "-0.02em", color: "ink-primary" }
    section-heading: { fontFamily: "serif", fontSize: "24px", fontWeight: "300", lineHeight: "1.25", letterSpacing: "-0.01em", color: "ink-primary" }
    section-numeral: { fontFamily: "serif", fontSize: "20px", fontWeight: "300", fontStyle: "italic", lineHeight: "1.0", color: "accent-brass" }
    exhibit-quote: { fontFamily: "serif", fontSize: "clamp(24px, 2.5vw, 36px)", fontWeight: "300", fontStyle: "italic", lineHeight: "1.25", color: "ink-primary" }
    script-input: { fontFamily: "serif", fontSize: "19px", fontWeight: "300", lineHeight: "1.55", color: "ink-primary" }
    body-prose: { fontFamily: "sans", fontSize: "14px", fontWeight: "300", lineHeight: "1.625", letterSpacing: "0em", color: "ink-secondary" }
    nav-item: { fontFamily: "sans", fontSize: "11px", fontWeight: "400", lineHeight: "1.4", letterSpacing: "0.025em", color: "ink-secondary" }
    small-caps-rubric: { fontFamily: "sans", fontSize: "10px", fontWeight: "500", fontVariant: "small-caps", letterSpacing: "0.15em", color: "ink-secondary" }
    micro-label: { fontFamily: "sans", fontSize: "9px", fontWeight: "500", fontVariant: "small-caps", letterSpacing: "0.20em", color: "ink-recessed" }
    mono-metric: { fontFamily: "mono", fontSize: "11px", fontWeight: "300", fontVariantNumeric: "tabular-nums", letterSpacing: "0.04em", color: "ink-muted" }

spacing:
  scale: ["8px", "12px", "16px", "24px", "32px", "40px", "48px", "64px", "80px", "96px"]
  masthead-height: "64px"
  left-rail-width: "256px"
  right-rail-width: "192px"
  reading-well-max-width: "672px"

borders:
  hairline-subpixel: "0.5px solid rgba(245, 242, 237, 0.10)"
  hairline-standard: "1px solid #33312E"
  dot-leader: "1px dotted rgba(245, 242, 237, 0.20)"
  button-tactile: "1px solid rgba(245, 242, 237, 0.25)"

radii:
  none: "0px"
  button: "2px"
  index-badge: "9999px"

shadows:
  default: "none"
---

# ComedyOS Design System (`DESIGN.md` — `getdesign.md` Standard v2.0)

> **Ground-Truth Specimen Files (Local):**
> - [`design-system/specimens/variant-8a6a23bf-archive.html`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/specimens/variant-8a6a23bf-archive.html) (`COMEDYOS Archive v1.0` — 3-Pane Workspace & Typographic Ledger)
> - [`design-system/specimens/variant-568d8c7f-system-specimen.html`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/specimens/variant-568d8c7f-system-specimen.html) (`ComedyOS System Specimen v1.0` — Form Controls, Note Index & Audio Diff)

---

## 1. Visual Theme & Atmosphere

- **Core Metaphor: "The Typographic Ledger & Late-Night Monograph"**
  ComedyOS is an archival writing, performance analysis, and set-building instrument for stand-up comedians. It rejects modern SaaS dashboard conventions (no floating cards, no drop shadows, no glowing gradients, no pill-badge clutter) in favor of the quiet, tactile authority of a **fine-press literary monograph** (Stripe Press, Craig Mod) fused with a **precision acoustic ledger** (Linear, iA Writer).
- **Atmospheric Calm (`#1A1918`):**
  The entire interface sits on an uninterrupted matte warm charcoal field (`#1A1918`). This eliminates screen glare in dark basement comedy clubs and green rooms while giving warm bone typography (`#F5F2ED`) effortless optical presence.
- **Zero Box Soup (>=95% Open Canvas):**
  Regions are never separated by opaque secondary background cards (`#222`, `#282624`). Instead, spatial architecture is achieved through **sub-pixel `0.5px` hairlines** (`rgba(245, 242, 237, 0.10)`), **generous asymmetric whitespace**, **4-tier text luminance**, and **horizontal dotted leaders** (`.dot-leader`).

---

## 2. Color Palette & Roles

Instead of background fills, ComedyOS creates depth through **4 distinct tiers of warm monochrome text luminance** plus **2 disciplined semantic accents**:

| Token | Value | Optical Role & Scarcity Rule |
| :--- | :--- | :--- |
| **`--bg` (Canvas)** | `#1A1918` | Primary background across >=95% of the viewport. Never cover with card fills. |
| **`--surface-hover`** | `#201F1E` | (`rgba(245,242,237,0.03)`) Transient row or button hover whisper. Never static. |
| **`--ink` (Tier 1: Bone)** | `#F5F2ED` | Primary headings (`H1`, `H2`), verbatim joke scripts, active nav items, and inline key terms (`<span class="text-[#F5F2ED]">`) inside muted paragraphs. |
| **`--ink-secondary` (Tier 2: Stone)** | `#8C8782` / `#A19F9A` | Standard body prose (`<p>`), lead italic subtitles, and default navigation links. Keeping prose in `#8C8782` allows `#F5F2ED` inline highlights and serif headings to pop without boxes. |
| **`--ink-muted` (Tier 3: Charcoal)** | `#5C5A55` | `all-small-caps` input labels, timestamps, bit codes, and inactive metadata. |
| **`--ink-recessed` (Tier 4: Ash)** | `#4A4845` | Search input placeholders (`placeholder:text-[#4A4845]`), footer colophons, and tertiary right-rail group headings (`Related`, `Citation Style`). |
| **`--hairline` (Sub-Pixel Rule)** | `rgba(245, 242, 237, 0.10)` | `0.5px` or `1px` single-edge structural pane dividers (`.hairline-b`, `.hairline-r`, `.hairline-l`). Equivalent to `#33312E`. |
| **`--accent-brass` (Archival Brass)** | `#B4A28A` | **Editorial & Reading Signal:** Used in `8a6a23bf` for italic serif section numbers (`2.1`, `2.2`), breadcrumbs (`Manual / 02`), active sidebar link underlines, and text selection highlight (`::selection`). |
| **`--accent-sage` (Surgical Sage)** | `#9FAF9A` | **Interactive & Live Signal:** Used in `568d8c7f` & Workbench for primary CTA button borders/tints, `:focus-within` input underlines, live sync status, and stage-active punchlines. |
| **`--alert-terracotta` (Diff Alert)** | `#E26D5C` | **Destructive / Diff Signal:** Reserved strictly for literal text diff strikethroughs or dropped setup warnings. |

---

## 3. Typography Rules

### 3.1 Strict Font Role Decoupling
1. **Editorial & Verbatim Serif (`--font-serif: 'Crimson Pro', serif`):**
   - Weights: `200`, `300`, `400` (Normal & Italic).
   - Used for: Brand wordmark (`COMEDYOS`), Page Titles (`text-5xl font-light`), Section Headings (`text-2xl font-light`), Italic Section Numerals (`2.1` in `italic text-xl`), Verbatim Joke Scripts, and Primary Text Inputs (`19px`).
2. **Structural & Narrative Sans (`--font-sans: 'Inter', sans-serif`):**
   - Weights: `300`, `400`, `500`.
   - Used for: Body prose (`14px`, `font-light`, `leading-relaxed` `1.625`), sidebar navigation lists (`11px`, `tracking-wide`), and `.small-caps` structural labels (`9px–11px`, `letter-spacing: 0.10em–0.20em`).
3. **Tabular Telemetry Mono (`--font-mono: 'JetBrains Mono', monospace`):**
   - Weight: `300` / `400` with `font-variant-numeric: tabular-nums`.
   - Used for: Bit IDs (`B-104`), durations (`02:15`), decibel peaks (`-4.2dB`), and word counters (`25 ENTRIES`) so numbers never jitter when updating.

### 3.2 Signature Editorial Lockups (From Variant `8a6a23bf`)
- **The Section Header Lockup (`2.1 The Dataset`):**
  Align an italic `Crimson Pro` brass numeral (`20px`) and a roman `Crimson Pro` light heading (`24px`) on the same typographic baseline:
  ```html
  <div class="flex items-baseline mb-4">
    <span class="font-serif italic text-xl mr-4 text-[#B4A28A]">2.1</span>
    <h2 class="font-serif text-2xl font-light text-[#F5F2ED]">The Dataset</h2>
  </div>
  ```
- **Inline Luminance Highlighting:**
  Inside a body paragraph set in `#8C8782`, emphasize key conceptual terms solely by shifting their color to `#F5F2ED` (or `italic text-[#F5F2ED]`) rather than using bold weights or background code boxes:
  ```html
  <p class="text-sm text-[#8C8782] leading-relaxed">
    Use this resource not as a narrative, but as a <span class="text-[#F5F2ED]">typographic ledger</span> for studying the mechanics of humor.
  </p>
  ```

---

## 4. Component Stylings

### 4.1 Tactile Workspace Buttons (`.btn` & `.btn-primary`)
*Why we upgraded Variant's raw buttons:* Variant `8a6a23bf` had only text navigation links, and `568d8c7f` used bare underlined text for actions, which caused users to miss clickable buttons in interactive tools.
- **Rule:** Navigation rails (Left Sidebar, Top Header, Right TOC, Footer Prev/Next) use clean borderless typography. Every **functional workspace button** (Save, Record, Extract, Split, Sync, Filter) MUST use `.btn`:
```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 6px 14px;
  font-family: var(--font-sans);
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #F5F2ED;
  background: transparent;
  border: 1px solid rgba(245, 242, 237, 0.25);
  border-radius: 2px;
  cursor: pointer;
  transition: all 180ms cubic-bezier(0.25, 0.1, 0.25, 1);
}
.btn:hover {
  border-color: rgba(245, 242, 237, 0.75);
  color: #FFFFFF;
  background: rgba(245, 242, 237, 0.04);
}
.btn-primary {
  border-color: rgba(159, 175, 154, 0.65);
  background: rgba(159, 175, 154, 0.06);
}
.btn-primary:hover {
  border-color: #9FAF9A;
  background: rgba(159, 175, 154, 0.14);
}
```

### 4.2 Architectural Bottom-Line Inputs (`.input-line-group`)
Never wrap `<input>` or `<textarea>` in a 4-sided border or grey box:
```html
<div class="input-line-group">
  <label class="input-micro-label">01. Set-up Premise</label>
  <textarea class="input-editorial" rows="2" placeholder="Establish the premise..."></textarea>
</div>
```
- **Wrapper (`.input-line-group`):** `border-bottom: 1px solid rgba(245, 242, 237, 0.10); padding-bottom: 8px; transition: border-color 150ms ease;` (`border-bottom-color: #9FAF9A` on `:focus-within`).
- **Micro-Label (`.input-micro-label`):** `font-size: 9px; font-variant: small-caps; text-transform: uppercase; letter-spacing: 0.16em; color: #5C5A55; margin-bottom: 4px; display: block;`
- **Input/Textarea (`.input-editorial`):** `width: 100%; background: transparent; border: none; outline: none; font-family: 'Crimson Pro', serif; font-size: 19px; font-weight: 300; color: #F5F2ED;` (`placeholder: color #4A4845; font-style: italic`).

### 4.3 The Typographic Ledger & Dot Leader (`.index-row`)
Extracted from Variant `8a6a23bf` (`2.2 Navigating the Craft`) and `568d8c7f` (`03. Note List`):
```html
<div class="flex items-center text-[11px] small-caps py-2 group cursor-pointer">
  <span class="w-4 h-4 rounded-full border border-[rgba(245,242,237,0.1)] flex items-center justify-center mr-3 text-[8px] text-[#8C8782]">A</span>
  <span class="text-[#F5F2ED] group-hover:text-[#B4A28A] transition-colors">Writing &amp; Joke Construction</span>
  <div class="dot-leader"></div>
  <span class="font-mono text-[#8C8782] tabular-nums">25 Entries</span>
</div>
```
- **`.dot-leader` CSS:**
  ```css
  .dot-leader {
    flex-grow: 1;
    border-bottom: 1px dotted rgba(245, 242, 237, 0.20);
    margin: 0 12px;
    position: relative;
    top: -4px;
  }
  ```

### 4.4 Numbered Left Sidebar Navigation (From `8a6a23bf`)
- **Group Rubric:** `10px` `small-caps` `color: #8C8782` `margin-bottom: 16px` (`Library`, `The Craft`).
- **Inactive Item:** `<span class="text-[#8C8782] mr-2">01.</span><span class="group-hover:text-[#B4A28A]">Introduction</span>`
- **Active Item:** `<span class="text-[#B4A28A] mr-2">02.</span><span class="text-[#F5F2ED] font-medium underline underline-offset-4 decoration-[#B4A28A]">Getting Started</span>`

---

## 5. Layout & Spacing Principles

### 5.1 Dual-Mode Viewport Architecture
1. **Mode A — Application & Reader Shell (`8a6a23bf` 3-Pane Pattern):**
   - `body` is locked to `100vh` (`h-screen overflow-hidden flex flex-col`).
   - **Top Masthead:** `height: 64px` (`h-16`), `padding: 0 40px` (`px-10`), `border-bottom: 0.5px solid rgba(245, 242, 237, 0.10)`.
   - **Left Navigation Rail:** `width: 256px` (`w-64`), `padding: 40px` (`p-10`), `border-right: 0.5px solid rgba(245, 242, 237, 0.10)`, `flex-col justify-between`.
   - **Center Editorial Well:** `flex-1 overflow-y-auto px-20 pt-16 pb-8` (with hidden scrollbar) containing `<article class="max-w-2xl mx-auto">`.
   - **Right Context / Inspector Rail:** `width: 192px` (`w-48`), `padding: 40px` (`p-10`), `border-left: 0.5px solid rgba(245, 242, 237, 0.10)`.
2. **Mode B — Multi-Section Specimen / Landing Page (`568d8c7f` Pattern):**
   - Vertical flow (`min-h-screen`) with `64px–96px` outer padding, `max-w-6xl mx-auto`, and `64px` vertical padding + `64px` margin across `1px` bottom hairlines between major sections.

### 5.2 Modular Spatial Rhythm
All spacing values must snap to `{8px, 12px, 16px, 24px, 32px, 40px, 48px, 64px, 80px, 96px}`.
- **Never show native browser scrollbars:** Apply `scrollbar-width: none; -ms-overflow-style: none;` and `::-webkit-scrollbar { display: none; }` globally.

---

## 6. Depth, Elevation & Shadows

- **Zero Elevation Shadows:** `box-shadow`, `drop-shadow`, and `backdrop-filter: blur()` are **strictly prohibited**.
- **Sub-Pixel Line Engraving:** Depth is created by contrasting `0.5px solid rgba(245, 242, 237, 0.10)` structural rules against `1px dotted rgba(245, 242, 237, 0.20)` leaders and `1px solid rgba(245, 242, 237, 0.25)` tactile button borders.

---

## 7. Responsive Behavior (Solving Variant `8a6a23bf`'s Fixed-Width Limitation)

Variant `8a6a23bf` hardcoded `w-64`, `px-20`, and `w-48` without responsive breakpoints, which crushes the center reading column on screens under `1100px`. Every ComedyOS implementation MUST apply this **3-Tier Responsive Collapse**:

1. **Desktop Wide (`> 1200px`):** Full 3-pane layout (`256px` Left Rail + `px-20` Center Well + `192px` Right Rail).
2. **Laptop / Tablet Split (`768px – 1200px`):**
   - Hide the Right TOC/Context Rail (`hidden xl:block`).
   - Narrow Left Rail to `200px` (`w-52`) and reduce Center Well horizontal padding from `80px` (`px-20`) to `32px` (`px-8`).
3. **Mobile (`< 768px`):**
   - Unlock `body` height (`overflow-y: auto; height: auto;`).
   - Collapse Left Rail into a toggleable top-sheet or switch to the dedicated **Mobile Keep Capture View** (`px-5 py-4`).

---

## 8. Do's and Don'ts (Hard Guardrails)

### DO:
- **Do** expose the raw `#1A1918` canvas across >=95% of the viewport.
- **Do** set body prose in `#8C8782` / `#A19F9A` so inline `<span class="text-[#F5F2ED]">` phrases and `Crimson Pro` headings stand out naturally.
- **Do** use `.dot-leader` (`1px dotted rgba(245,242,237,0.20)`) to connect left-aligned titles to right-aligned counters.
- **Do** use `.btn` (`2px` radius, `1px` hairline border) on every interactive action button.
- **Do** pair italic `Crimson Pro` brass numerals (`2.1`) with roman `Crimson Pro` headings on `items-baseline`.

### DON'T:
- **Don't** wrap sections, cards, notes, or forms in `#22211F` or `#282624` background boxes.
- **Don't** use `border-radius` > `2px` on any rectangular element (no `rounded-md`, `rounded-lg`, `rounded-xl`).
- **Don't** use `border-l-2` or `border-l-4` colored callout boxes with background tints.
- **Don't** place decorative status dots (`w-2 h-2 rounded-full bg-green-500`) next to text counters.
- **Don't** use solid-fill opaque buttons (`background: #9FAF9A; color: #000`).

---

## 9. Agent Prompt Guide (Copy-Paste Instruction Block)

Include this block when prompting any coding agent (Gemini Flash, Claude, Cursor) to build or modify ComedyOS UI:

```markdown
Read `design-system/DESIGN.md` before writing any HTML/CSS.
Enforce these 6 mechanical constraints:
1. ZERO CARD BOXES: `body` is `#1A1918`. Every `<section>`, `<div>`, `<aside>`, `<article>`, and `<input>` has `background: transparent`.
2. SUB-PIXEL HAIRLINES: Separate layout panes with `0.5px solid rgba(245, 242, 237, 0.10)`. Separate list rows with `.dot-leader` (`1px dotted rgba(245, 242, 237, 0.20)`).
3. 4-TIER LUMINANCE: Headings & inline highlights = `#F5F2ED` (`Crimson Pro` light); Body prose & nav = `#8C8782` (`Inter` light); Metadata = `#5C5A55` (`JetBrains Mono` tabular-nums); Recessed labels/placeholders = `#4A4845` (`9px–10px` `small-caps`).
4. EDITORIAL HEADINGS: Pair italic brass numerals (`<span class="font-serif italic text-xl mr-4 text-[#B4A28A]">2.1</span>`) with `Crimson Pro` light headings (`<h2 class="font-serif text-2xl font-light text-[#F5F2ED]">`) using `flex items-baseline`.
5. TACTILE BUTTONS (`.btn`): Navigation rails use plain text links; all workspace action buttons MUST use `.btn` (`border: 1px solid rgba(245,242,237,0.25); border-radius: 2px; padding: 6px 14px; font-size: 10px; text-transform: uppercase; letter-spacing: 0.16em;`).
6. TRANSPARENT INPUTS (`.input-line-group`): All inputs/textareas have `background: transparent; border: none;` inside a bottom-bordered wrapper (`border-bottom: 1px solid rgba(245,242,237,0.10)`) with a `9px` `small-caps` label above.
```
