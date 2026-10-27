# ComedyOS Design Specification (`DESIGN.md`)

**Source Authority:** Extracted directly from the three Variant reference implementations:
1. **Variant Archive Manual (`8a6a23bf`):** `COMEDYOS Archive v1.0 — Getting Started`
2. **Variant System Specimen (`568d8c7f`):** `ComedyOS — System Specimen v1.0` (`01. Foundations` through `06. Status`)
3. **Variant Foundations Sheet (`782176fa`):** `ComedyOS Design System — 01 Foundations`

---

## 1. Aesthetic Philosophy: "The Typographic Ledger"

ComedyOS is an archival, late-night writing and performance workspace for stand-up comedians. Its visual language is modeled after a **literary monograph and a precision typographic ledger**—never a SaaS marketing dashboard.

- **Atmospheric Calm:** The workspace relies on an uninterrupted warm charcoal field (`#1A1918`) to eliminate glare in dark comedy clubs and basement green rooms.
- **Economy of Structure:** Grouping is achieved through **macro whitespace**, **4-tier typographic luminance**, **left-border indentation**, and **dotted horizontal leaders**.
- **Zero Box Soup:** Contained cards, heavy background fills, and 4-sided borders are avoided. Interactive specimens live directly on the open `#1A1918` canvas.

---

## 2. Color & Luminance System (4-Tier Depth)

Instead of using background boxes to separate UI regions, ComedyOS uses a strict **4-tier luminance hierarchy** on top of `#1A1918`.

| Token Name | Hex / Value | Role & Usage |
| :--- | :--- | :--- |
| **`--bg` (Canvas Black)** | `#1A1918` | Primary background across >=95% of the viewport. Never cover with opaque secondary card fills. |
| **`--surface-whisper`** | `rgba(35, 34, 32, 0.30)` | (`bg-[#232220]/30`) Maximum permitted background tint for callout notes or active blocks. |
| **`--surface-hover`** | `#201F1E` | Transient row highlight on hover (`hover:bg-[#201F1E]`). Never used as a static card fill. |
| **`--primary` (Bone Ink)** | `#F5F2ED` | Tier 1 Focus: Display headings, verbatim joke scripts, active navigation, and primary input values. |
| **`--secondary` (Smoke)** | `#A19F9A` | Tier 2 Prose: Standard body copy, descriptions, and secondary interactive labels. |
| **`--muted` (Charcoal Meta)** | `#5C5A55` | Tier 3 Recession: Section numbers, `all-small-caps` field labels, timestamps, and inactive tabs. Must remain dark enough to recede into `#1A1918`. |
| **`--hairline` (Rule)** | `#33312E` | Tier 4 Structure: `1px` (or `0.5px` `rgba(245, 242, 237, 0.10)`) single-edge structural dividers and `.dot-leader` lines. |
| **`--accent` (Surgical Sage)** | `#9FAF9A` | Active state indicators, verified tags, onstage riffs, and primary interactive focus/hover accents. |
| **`--accent-warm` ( Brass )** | `#B4A28A` | Editorial section numerals (`2.1`, `2.2`), active underline accents, and text selection highlight. |
| **`--alert` (Terracotta)** | `#E26D5C` | Mechanical friction, dropped setups, or required script revisions. |

---

## 3. Typography & Hierarchy

### Font Stack
- **Serif (`--font-serif`):** `'Crimson Pro', Georgia, serif` — Weights `200`, `300`, `400` (Normal & Italic). Used for all headings, verbatim joke material, and primary text inputs.
- **Sans (`--font-sans`):** `'Inter', -apple-system, sans-serif` — Weights `300`, `400`, `500`, `600`. Used for body prose (`font-weight: 300`) and `.small-caps` structural labels (`font-weight: 500`).
- **Mono (`--font-mono`):** `'JetBrains Mono', monospace` — Weight `300` / `400`. Used strictly for bit IDs (`B-402`), timestamps (`04:30`), decibel peaks (`-4.2dB`), and character counters (`2,401 CHARS`).

### Type Scale (From `variant-design-2.html` & `variant-design-3.html`)
1. **Display Large:** `Crimson Pro Light (300)` · `60px–72px` (`3.75rem–4.5rem`) · `line-height: 1.0` · `letter-spacing: -0.025em` · Color: `#F5F2ED`
2. **Display Medium / Quote:** `Crimson Pro Light Italic (300)` · `36px–48px` (`2.25rem–3rem`) · `line-height: 1.15` · Color: `#F5F2ED`
3. **Section Heading (`H1` / `H2`):** `Crimson Pro Light/Regular (300/400)` · `24px–36px` (`1.5rem–2.25rem`) · `line-height: 1.25` · Color: `#F5F2ED`
4. **Verbatim Script / Index Item Title:** `Crimson Pro Light/Regular` · `20px–24px` (`1.25rem–1.5rem`) · `line-height: 1.55` · Color: `#F5F2ED`
5. **Lead Body Prose:** `Inter Light (300)` · `18px` (`1.125rem`) · `line-height: 1.625` · Color: `#A19F9A` (or `#F5F2ED` for primary statements)
6. **Standard UI Prose:** `Inter Light (300)` · `13px–14px` · `line-height: 1.625` · Color: `#A19F9A`
7. **Structural Small-Caps (`.small-caps`):** `Inter Medium (500)` · `font-variant: all-small-caps` · `10px–11px` (and `9px` for input micro-labels) · `letter-spacing: 0.12em–0.15em` · Color: `#5C5A55` (meta) or `#F5F2ED` (active)
8. **Data / Mono (`.mono`):** `JetBrains Mono (300)` · `10px–12px` · Color: `#5C5A55` or `#9FAF9A`

---

## 4. Intentional Spatial Rhythm (Base-8 / Base-16 Modular Scale)

Every margin, padding, and gap must come from this fixed architectural scale—no arbitrary pixel values:

- **`8px` (`0.5rem`):** Micro-label to input field (`mb-2`), bottom hairline padding (`pb-2`).
- **`16px` (`1.0rem`):** Index row vertical padding (`py-4`), paragraph stack gap (`mb-4`).
- **`24px` (`1.5rem`):** Sub-component internal rhythm (`space-y-6`, `gap-6`, `p-6`).
- **`32px` (`2.0rem`):** Left-border annotation indent (`pl-8`), footer top padding (`pt-8`), minor group spacing (`space-y-8`).
- **`48px` (`3.0rem`):** Mandatory distance from a section's `.small-caps` header to its content (`mb-12`), and vertical stack gap between form groups (`space-y-12`).
- **`64px` (`4.0rem`):** Major specimen section padding and margin (`padding-bottom: 4rem; margin-bottom: 4rem; border-bottom: 1px solid #33312E`), and 12-column grid gap (`gap-16`).
- **`96px` (`6.0rem`):** Outer desktop frame padding (`p-12 lg:p-24`), header bottom margin (`mb-24`), and primary two-column split gap (`gap-24`).

---

## 5. Component Specifications

### 5.1 Input Fields & Textareas (`02. Form Controls`)
Inputs are architectural baselines on the canvas—never boxed rectangles.
```html
<div class="input-group">
  <label class="input-label">Email Address</label>
  <input type="email" class="input-serif" placeholder="comic@club.com" />
</div>
```
- **Container (`.input-group`):** `border-bottom: 1px solid #33312E; padding-bottom: 8px; transition: border-color 150ms ease;` (`border-color: #9FAF9A` on `:focus-within`).
- **Label (`.input-label`):** `display: block; font-variant: all-small-caps; font-size: 10px; letter-spacing: 0.15em; color: #5C5A55; margin-bottom: 4px;`
- **Control (`.input-serif`):** `width: 100%; background: transparent; border: none; outline: none; font-family: 'Crimson Pro', serif; font-size: 19px; font-weight: 300; color: #F5F2ED;`
- **Placeholder:** `color: #4A4845; font-style: italic;`

### 5.2 Buttons & Action Controls (`02. Form Controls`)
1. **Primary Architectural CTA Button (Waitlist / Primary Submit):**
   - Designed to look unmistakably like a tactile, precision button without turning into a heavy pastel brick:
   - `display: inline-flex; align-items: center; gap: 10px;`
   - `padding: 10px 20px; border-radius: 2px;` (crisp `2px` micro-chamfer)
   - `background: rgba(159, 175, 154, 0.10);`
   - `border: 1px solid rgba(159, 175, 154, 0.55);`
   - `font-variant: all-small-caps; font-size: 11px; font-weight: 500; letter-spacing: 0.15em; color: #F5F2ED;`
   - **Hover:** `background: rgba(159, 175, 154, 0.22); border-color: #9FAF9A; color: #F5F2ED;`
2. **Editorial Underline Button (Variant Spec Primary Action):**
   - `background: transparent; border: none; border-bottom: 1px solid #F5F2ED; padding-bottom: 4px;`
   - `font-variant: all-small-caps; font-size: 11px; font-weight: 500; letter-spacing: 0.15em; color: #F5F2ED;`
   - **Hover:** `color: #9FAF9A; border-bottom-color: #9FAF9A;`
3. **Secondary Ghost / Tag Control:**
   - `background: transparent; border: none; font-variant: all-small-caps; font-size: 11px; letter-spacing: 0.15em; color: #A19F9A;` (`hover:color: #F5F2ED`, active `color: #9FAF9A`).

### 5.3 The Index List & Dot Leader (`03. Note List`)
Used for setlists, bit archives, and token tables without enclosing them in cards:
```html
<div class="index-row group">
  <span class="index-id">B-402</span>
  <span class="index-title">The Flight Attendant Monologue</span>
  <div class="dot-leader"></div>
  <span class="index-status">Polished</span>
  <span class="index-time">4:30</span>
</div>
```
- **Row:** `display: flex; align-items: flex-end; padding: 16px 0; border-bottom: 1px solid #33312E;` with subtle hover `hover:bg-[#201F1E] px-4 -mx-4 transition-colors`.
- **Dot Leader:** `flex-grow: 1; border-bottom: 1px dotted #33312E; margin: 0 12px 6px 12px;`
- **Hover Interaction:** `.index-title` shifts smoothly to `italic` (`group-hover:italic`) on hover.

### 5.4 Left-Border Stage Directions & Whisper Callouts (`04. Content`)
- **Stage Directions / Annotations:** `padding-left: 32px; border-left: 1px solid #33312E;` (`pl-8 border-l hairline space-y-6`). Zero background fill.
- **Observation / Note to Self Callout:** `background: rgba(35, 34, 32, 0.30); padding: 24px; border-left: 2px solid #9FAF9A;` (`bg-[#232220]/30 p-6 border-l-2 border-accent`). No top, right, or bottom border.
