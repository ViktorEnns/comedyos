# ComedyOS Master Design Governance ("Best of Both Worlds" Synthesis)

> **Synthesis Authority:** Combines the **Google AI Studio Gallery Editorial Extraction** (`gallery-editorial-system`) with the **Forensic Variant DOM/CSS Extraction** (`8a6a23bf`, `568d8c7f`, `782176fa`).
> Use this single source of truth to instruct Antigravity, Gemini Pro, and Gemini Flash to build or modify any ComedyOS interface or website with 1:1 fidelity.

---

## Part 1: Comparative Audit — AI Studio Extract vs. Variant DOM Extract

### 1.1 Where Both Extractions Independently Converged
- **Core Metaphor:** Both rejected SaaS dashboard chrome in favor of an archival, late-night monograph aesthetic (*"The Interface is the Gallery; Content is the Exhibit"* / *"The Typographic Ledger"*).
- **Canvas & Ink:** Both locked onto `--bg: #1A1918` (deep warm charcoal) and `--ink: #F5F2ED` (warm bone ink), banning pure `#000000` and `#FFFFFF`.
- **Font Pairing & Role Decoupling:** Both mandated `Crimson Pro` (`200–300`, normal & italic) strictly for Display, Headings, and Verbatim Quotes, paired with `Inter` (`300` for body prose, `500` for tracked small-caps labels) and `JetBrains Mono` / `tabular-nums` for counters and timestamps.
- **Dot Leaders (`.leader` / `.dot-leader`):** Both identified the horizontal dotted leader connecting left-aligned `Crimson Pro` titles to right-aligned tabular metadata as the signature structural motif.
- **Tactile `2px`-Radius Hairline Buttons:** Both discovered that bare text links feel broken while solid pastel bricks feel cheap—converging on `border-radius: 2px`, a `1px solid` hairline stroke, `11px` uppercase/small-caps tracking, and a `6%–10%` translucent sage fill for primary CTAs.

### 1.2 Where They Diverged (And Why)
| Dimension | Google AI Studio Extract | Variant Raw DOM Extract (`568d8c7f` / `782176fa`) | Synthesis Resolution ("Best of Both Worlds") |
| :--- | :--- | :--- | :--- |
| **Button Scope** | Applied `.btn` (`1px solid rgba(245,242,237,0.25)`, `2px` radius, `7px 16px` padding) to **all** clickable actions. Explicitly banned bare underlined text buttons (`ANTI-PATTERN 2: The Invisible Button Flaw`). | Used `.btn-architectural` (`2px` radius) only on the Hero CTA, while keeping Variant's raw `border-b border-[#F5F2ED]` bare underline on secondary actions. | **Adopt AI Studio's Universal `.btn` Contract.** Variant's own bare underline buttons fail usability on interactive pages (*"the buttons do not look like buttons"*). Every functional button must use `.btn` or `.btn-primary`. Bare underlines are reserved strictly for active tab indicators. |
| **Left-Border Callout Boxes** | Explicitly banned colored left-border callout boxes with background tints (`ANTI-PATTERN 3: The Thick Left Accent Border`). | Retained Variant `568d8c7f`'s `bg-[#232220]/30 border-l-2 border-[#9FAF9A]` callout block. | **Adopt AI Studio's Ban on Left-Border Tinted Boxes.** Even at 30% opacity, a tinted box with a colored left stripe reads as a Bootstrap/LLM cliché and adds visual boxiness. Use unboxed typography with a `1px` `--hairline` divider instead. |
| **Status Dots** | Explicitly banned status dots next to static text (`ANTI-PATTERN 4: Faux-Telemetry Dots`). | Included Variant `568d8c7f`'s `6px` status dot next to queue counters. | **Adopt AI Studio's Ban on Status Dots.** Remove all decorative status dots next to text counters. |
| **Accent Budget** | Mandated **Invariant 5 (Restrained Accent Budget):** `#9FAF9A` sage is the sole accent color; max 1 focal accent group per view. | Mixed `#9FAF9A` sage, `#B4A28A` brass numerals (`1.1`, `1.2`), and `#E26D5C` terracotta simultaneously. | **Adopt AI Studio's Single-Accent Budget.** Demote section numerals (`1.1`, `1.2`) to `--ink-faint` (`rgba(245,242,237,0.45)`) so `#9FAF9A` sage is the undisputed focal accent. Allow `#E26D5C` terracotta **only** inside a literal diff strikethrough. |
| **Form Inputs & Spacing Scale** | Mentioned underline search in one sentence; omitted stacked `9px` field labels, textarea specs, and the Base-8/16 modular spacing scale. | Extracted complete **Form Control Anatomy** (stacked `9px` small-caps label + `Crimson Pro` `19px` input + `1px` bottom hairline), **Base-8/16 Spatial Scale**, and **Variant Iframe Extraction Protocol**. | **Adopt Variant DOM Extract's Form & Spatial Specs.** Codify the full `.input-group` anatomy, the `{8, 16, 24, 32, 48, 64, 96}px` modular rhythm, and the `/design/<uuid>.html` extraction workflow. |
| **Viewport Discipline** | Mandated `100vh` `overflow-hidden` single-viewport fit (`INVARIANT 4`), based on Variant `8a6a23bf` (the 3-pane reader app). | Built for multi-section scrollable pages (`568d8c7f` & `782176fa`) with hidden scrollbars (`scrollbar-width: none`). | **Dual-Mode Viewport Contract:** Enforce strict `100vh` `overflow-hidden` for **Workspace/App Views**, and `100vh`-proportioned exhibit sections with hidden scrollbars (`scrollbar-width: none`) for **Multi-Section Landing/Specimen Pages**. |

---

## Part 2: The Unified `SKILL.md` & `DESIGN.md` Specification

### 2.1 Mental Model: "The Interface is the Gallery; Content is the Exhibit"
- Treat the screen like a matte, unhurried museum exhibition wall or literary monograph.
- Hierarchy is established through **type scale, 4-tier optical luminance, and macro whitespace**—never through cards, background boxes, drop shadows, pill badges, or decorative status dots.
- Every clickable button has **crisp tactile geometry** (`.btn`: `1px` hairline border, `2px` radius, `7px 16px` padding, uppercase/small-caps tracking) so interactive controls are instantly distinguishable from editorial prose.

### 2.2 Master Token Registry (Global CSS Variables)
```css
:root {
  /* Surfaces (Zero Card Fills) */
  --bg: #1A1918;                           /* Deep matte charcoal gallery canvas (>=96% of viewport) */
  --surface-hover: rgba(245,242,237,0.03); /* Transient row/button hover whisper (#201F1E) */

  /* 4-Tier Optical Luminance Hierarchy */
  --ink: #F5F2ED;                          /* Tier 1: Primary headlines, verbatim quotes, active controls */
  --ink-muted: #A19F9A;                    /* Tier 2: Standard body prose & descriptions (#8C8882 - #A19F9A) */
  --ink-faint: rgba(245,242,237,0.45);     /* Tier 3: Recessed metadata, rubrics, timestamps, field labels (#5C5A55) */
  --placeholder: rgba(245,242,237,0.22);   /* Unfocused input placeholder text (#4A4845) */

  /* Structural Rules & Tactile Strokes */
  --hairline: rgba(245,242,237,0.10);      /* Tier 4: 1px structural dividers & dot leaders (#33312E) */
  --hairline-btn: rgba(245,242,237,0.25);  /* 1px tactile button border stroke */
  --hairline-btn-hover: rgba(245,242,237,0.75);

  /* Restrained Single-Accent Budget */
  --accent: #9FAF9A;                       /* Surgical sage: active states & primary CTA focus */
  --accent-border: rgba(159,175,154,0.65); /* Primary CTA border stroke */
  --accent-fill: rgba(159,175,154,0.06);   /* Primary CTA subtle glass tint (6% opacity) */
  --accent-fill-hover: rgba(159,175,154,0.14);
  --revision: #E26D5C;                     /* Terracotta: reserved strictly for literal text diff strikethroughs */

  /* Font Stacks */
  --font-serif: 'Crimson Pro', Georgia, serif;
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

### 2.3 Typographic Hierarchy & Strict Role Decoupling
| Role | Font Family | Size / Clamp | Weight & Style | Tracking & Leading | Color Token |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Display Hero** | `Crimson Pro` | `clamp(48px, 5vw, 72px)` | `200–300` Normal | `-0.025em` / `1.02` | `--ink` |
| **Exhibit Quote** | `Crimson Pro` | `clamp(24px, 2.5vw, 36px)` | `300` Italic | `-0.01em` / `1.25` | `--ink` |
| **Section Heading** | `Crimson Pro` | `clamp(28px, 2.4vw, 38px)` | `300` Normal | `-0.02em` / `1.15` | `--ink` |
| **Ledger / Item Title** | `Crimson Pro` | `20px–24px` | `300` Normal (`italic` on hover) | `0` / `1.3` | `--ink` |
| **Body Prose** | `Inter` | `14px–15.5px` | `300` Normal | `0` / `1.65` | `--ink-muted` |
| **Eyebrows & Rubrics** | `Inter` | `10px–11px` | `500` `all-small-caps` | `0.16em–0.20em` / `1.4` | `--ink-faint` |
| **Input Micro-Label** | `Inter` | `9px–10px` | `500` `all-small-caps` | `0.16em` / `1.2` | `--ink-faint` |
| **Ledger Counters / IDs** | `JetBrains Mono` | `11px–13px` | `300` `tabular-nums` | `0.04em` / `1.0` | `--ink-faint` |

### 2.4 Modular Spatial Rhythm (Base-8 / Base-16 Grid)
Never invent arbitrary spacing. Use only these intervals:
- **`8px` (`0.5rem`):** Micro-label to input baseline (`pb-2`, `mb-2`).
- **`16px` (`1.0rem`):** Ledger row vertical padding (`py-4`), header bottom padding (`pb-4`).
- **`24px` (`1.5rem`):** Paragraph stack gap and internal component spacing (`gap-6`).
- **`32px` (`2.0rem`):** Left hairline indentation (`pl-8`) and form field group gap (`gap-8`).
- **`48px` (`3.0rem`):** Mandatory distance from a section rubric (`01. Foundations`) to its content grid (`mb-12`).
- **`64px` (`4.0rem`):** Major section bottom padding (`64px`) + bottom margin (`64px`) across a `1px solid var(--hairline)` divider, and 12-column horizontal grid gap (`gap-16`).
- **`96px` (`6.0rem`):** Desktop outer page frame padding (`64px 96px`) and masthead bottom margin (`mb-24`).

### 2.5 Canonical Component Contracts

#### A. The Universal Button Contract (`.btn` & `.btn-primary`)
Every interactive button (Submit, Cycle Stage, Record Audio, Filter, Attach Pass, Undo) MUST use `.btn` so it is immediately recognizable as a clickable control:
```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 7px 16px;
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--hairline-btn);
  border-radius: 2px;
  cursor: pointer;
  transition: all 220ms cubic-bezier(0.25, 0.1, 0.25, 1);
}
.btn:hover {
  border-color: var(--hairline-btn-hover);
  color: #FFFFFF;
  background: rgba(245, 242, 237, 0.04);
}
.btn-primary {
  padding: 10px 20px;
  border-color: var(--accent-border);
  background: var(--accent-fill);
}
.btn-primary:hover {
  border-color: var(--accent);
  background: var(--accent-fill-hover);
}
```

#### B. The Architectural Input Contract (`.input-group`)
Never use background fills or 4-sided borders on `<input>` or `<textarea>`:
```html
<div class="input-line-group">
  <label class="input-micro-label">Email Address</label>
  <input type="email" class="input-editorial" placeholder="alex@comedycellar.com" />
</div>
```
```css
.input-line-group {
  border-bottom: 1px solid var(--hairline);
  padding-bottom: 8px;
  transition: border-color 180ms ease;
}
.input-line-group:focus-within {
  border-bottom-color: var(--accent);
}
.input-micro-label {
  display: block;
  font-family: var(--font-sans);
  font-size: 9px;
  font-weight: 500;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink-faint);
  margin-bottom: 4px;
}
.input-editorial {
  width: 100%;
  background: transparent;
  border: none;
  outline: none;
  font-family: var(--font-serif);
  font-size: 19px;
  font-weight: 300;
  color: var(--ink);
}
```

#### C. The Typographic Ledger Row (`.index-row` + `.dot-leader`)
```html
<div class="index-row">
  <span class="index-id">B-402</span>
  <span class="index-title">Hotel Bathroom Landline</span>
  <div class="dot-leader"></div>
  <span class="index-status">Polished</span>
  <span class="index-time">02:15</span>
</div>
```

---

## Part 3: What We Learned From Previous Iterations (Why LLMs Drift Without Guidelines)

Comparing our three waitlist iterations with AI Studio's three iterations reveals a **universal 3-stage failure pattern** when LLMs build dark-mode interfaces:

1. **Stage 1 — The "SaaS Slop" Default (Pre-Training Bias):**
   - Because >90% of dark-mode web code in LLM training data is Tailwind/Bootstrap SaaS dashboards, an unconstrained LLM automatically outputs `rounded-xl` cards, `bg-neutral-900` secondary boxes, filled grey input rectangles, thick `border-l-4` callouts, and pulsing green status dots.
2. **Stage 2 — The "Linter / Over-Correction" Trap:**
   - When told "remove the boxes" or when run through a generic landing-page linter (`taste-skill`), the LLM over-corrects in the wrong direction:
     - It strips borders off buttons too, turning buttons into plain underlined text (`The Invisible Button Flaw`), OR it makes a flat, sharp-edged `0px` pastel brick (`background: #9FAF9A`) that looks like an unstyled HTML block.
     - Generic linters (`taste-skill`) penalize `10px` uppercase metadata and low-contrast `#5C5A55` labels, forcing the LLM to enlarge and brighten all metadata until it competes with primary headings—destroying the atmospheric depth that made boxes unnecessary in the first place.
3. **Stage 3 — The Architectural Synthesis:**
   - True fidelity requires **decoupling container chrome from control affordance**:
     - **Containers & Sections** have **zero** boxes, **zero** background fills, and rely on `64px–96px` whitespace, 4-tier text luminance, and `1px` single-edge hairlines (`rgba(245,242,237,0.10)`).
     - **Buttons** have **explicit tactile geometry** (`.btn` with `1px solid rgba(245,242,237,0.25)`, `2px` radius, `7px 16px` padding).
     - **Inputs** have **transparent backgrounds** anchored by a `1px` bottom baseline and a `9px` tracked micro-label.

---

## Part 4: How to Instruct Gemini Flash for 1:1 Fidelity

Smaller, high-speed models like **Gemini Flash** optimize for token generation speed and strongly gravitate toward high-probability training patterns (Tailwind cards, `rounded-lg`, boxed inputs). Abstract adjectives like *"make it look editorial, minimal, and premium"* **do not work on Gemini Flash**.

To make Gemini Flash 100% faithful to this style, use these **4 Prompt Engineering Mechanisms**:

### Mechanism 1: Provide a Locked `<style>` Boilerplate First ("CSS Slot-Filling")
Never ask Gemini Flash to invent the CSS classes from scratch. Give Flash the locked `:root` variables and the 5 canonical classes (`.serif`, `.eyebrow`, `.btn`, `.btn-primary`, `.input-line-group`, `.index-row`, `.dot-leader`) in the prompt, and instruct it: *"You may ONLY use these pre-defined classes for buttons, inputs, headings, and lists."*

### Mechanism 2: Enforce a Regex-Verifiable "Banned CSS Token List"
Gemini Flash responds strongly to explicit negative token constraints placed right before generation. Include a **Hard Ban List**:
- **BANNED PROPERTIES / CLASSES:**
  - Never use `border-radius` greater than `2px` (except `50%` on a `16px` circular index badge).
  - Never use `box-shadow`, `backdrop-filter`, `linear-gradient`, or `animate-pulse`.
  - Never give any `<div>`, `<section>`, `<article>`, `<aside>`, `<form>`, or `<input>` a non-transparent `background-color` (only `body` has `#1A1918` and `.btn-primary` has `rgba(159,175,154,0.06)`).
  - Never use `border-left-width` greater than `1px` (no `border-l-2` or `border-l-4` callout stripes).

### Mechanism 3: Require Few-Shot DOM Templates for Inputs, Buttons, and Rows
Include the exact 4-line HTML snippets for `.btn`, `.input-line-group`, and `.index-row` directly in the prompt so Gemini Flash copies the AST structure verbatim rather than hallucinating `<input class="p-3 bg-zinc-800 rounded">`.

### Mechanism 4: Copy-Paste System Prompt for Gemini Flash
Use the following prompt block whenever delegating UI generation to Gemini Flash:

```markdown
<SYSTEM_INSTRUCTION_FOR_GEMINI_FLASH>
You are generating UI in the strict "ComedyOS Gallery Editorial" design system.
Follow these 6 non-negotiable mechanical rules:

1. CANVAS ONLY (ZERO BOXES): `body` is `#1A1918`. Every `<section>`, `<div>`, `<form>`, `<aside>`, and `<input>` MUST have `background: transparent`. Never create card containers, secondary surface fills (`#222`, `#282624`), or `border-l-2` / `border-l-4` callout boxes.
2. SPACING FIRST, 1PX HAIRLINES SECOND: Separate sections using `64px` padding + `64px` margin and a single bottom hairline (`border-bottom: 1px solid rgba(245,242,237,0.10)`). Use only spacing values from `{8px, 16px, 24px, 32px, 48px, 64px, 96px}`.
3. 4-TIER LUMINANCE:
   - Headings & Verbatim Quotes: `Crimson Pro`, weight 300, color `#F5F2ED` (`--ink`).
   - Body Prose: `Inter`, weight 300, `14px–15px`, color `#A19F9A` (`--ink-muted`).
   - Section Rubrics & Field Labels: `Inter`, weight 500, `10px`, uppercase, `letter-spacing: 0.16em`, color `rgba(245,242,237,0.45)` (`--ink-faint`).
   - Counters & Timestamps: `JetBrains Mono`, `11px`, `tabular-nums`, color `rgba(245,242,237,0.45)`.
4. ALL BUTTONS USE `.btn`: Every `<button>` MUST use `.btn` (`border: 1px solid rgba(245,242,237,0.25); border-radius: 2px; padding: 7px 16px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.16em; background: transparent; color: #F5F2ED;`). Primary CTAs add `.btn-primary` (`border-color: rgba(159,175,154,0.65); background: rgba(159,175,154,0.06); padding: 10px 20px;`). Never output solid-fill pastel bricks or bare unbordered text buttons.
5. ALL INPUTS USE `.input-line-group`: Every `<input>` or `<textarea>` MUST be `background: transparent; border: none; outline: none; font-family: 'Crimson Pro', serif; font-size: 19px; color: #F5F2ED;` inside a wrapper with `border-bottom: 1px solid rgba(245,242,237,0.10); padding-bottom: 8px;` and a `9px` uppercase tracked label above it.
6. SINGLE ACCENT BUDGET: `#9FAF9A` (muted sage) is the ONLY accent color. Never add status dots (`rounded-full`) next to text, pill badges, shadows, or `border-radius` > `2px`.
</SYSTEM_INSTRUCTION_FOR_GEMINI_FLASH>
```
