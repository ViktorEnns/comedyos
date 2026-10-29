---
name: variant-faithful-design
description: Recreate reference UI designs (especially Variant.com designs like 8a6a23bf and 568d8c7f, and the ComedyOS Typographic Ledger / Gallery Editorial aesthetic) with 1:1 structural, typographic, and spatial fidelity using the getdesign.md 2-layer specification standard.
---

# ComedyOS Gallery Editorial & Variant-Faithful Design Skill (`SKILL.md`)

Use this skill whenever building or refining ComedyOS interfaces, landing pages, documentation engines, or recreating Variant.com reference designs.

## 0. Authoritative Reference Files (Read Before Generating UI)
1. **Master `getdesign.md` Specification:** [`design-system/DESIGN.md`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/DESIGN.md) (Contains machine-readable YAML tokens + the 9 canonical `getdesign.md` sections).
2. **Gemini Flash Execution Plan & Forensic Study:** [`design-system/FLASH_DESIGN_SYSTEM_EXECUTION_PLAN.md`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/FLASH_DESIGN_SYSTEM_EXECUTION_PLAN.md) (Contains copy-paste CSS boilerplate and HTML AST templates).
3. **Local Ground-Truth Variant DOM Specimens:**
   - [`design-system/specimens/variant-8a6a23bf-archive.html`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/specimens/variant-8a6a23bf-archive.html) (`COMEDYOS Archive v1.0` — 3-Pane Reader & Typographic Ledger)
   - [`design-system/specimens/variant-568d8c7f-system-specimen.html`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/specimens/variant-568d8c7f-system-specimen.html) (`ComedyOS System Specimen v1.0` — Form Controls & Note Index)

---

## 1. Mental Model: "The Typographic Ledger & Late-Night Monograph"
- Treat the viewport like a matte, unhurried literary monograph or museum exhibition wall (`#1A1918`).
- Hierarchy is established through **type scale, 4-tier optical luminance, sub-pixel `0.5px` hairlines (`rgba(245, 242, 237, 0.10)`), and macro whitespace**—**NEVER** through cards, secondary background boxes (`#22211F`), drop-shadows, `border-l-2`/`border-l-4` callout stripes, or pulsing status dots.
- **Navigation vs. Action Split:**
  - **Navigation Rails** (Left Sidebar, Top Header links, Right TOC, Footer Pagination) use clean, borderless typography (`10px–11px` `Inter`, `.small-caps`).
  - **Workspace Action Buttons** (Save, Record, Extract, Split, Sync, New Entry) MUST use the tactile **`.btn` contract** (`1px solid rgba(245,242,237,0.25)`, `2px` radius, `6px 14px` padding, uppercase `0.16em` tracking) so clickable actions are never confused with static prose.

---

## 2. Pre-Flight Token Checklist
Verify these exact tokens in global CSS before generating any markup:
- `--bg: #1A1918` (deep matte charcoal canvas; >=95% of viewport)
- `--ink: #F5F2ED` (Tier 1 Bone: headings, verbatim scripts, active nav, and inline `<span class="text-[#F5F2ED]">` highlights inside muted prose)
- `--ink-secondary: #8C8782` (Tier 2 Stone: standard body prose `<p>`, lead italic subtitles, default nav/TOC links)
- `--ink-muted: #5C5A55` (Tier 3 Charcoal: `small-caps` input labels, timestamps, bit codes)
- `--ink-recessed: #4A4845` (Tier 4 Ash: search placeholders, bottom colophon, tertiary group headers)
- `--hairline: rgba(245, 242, 237, 0.10)` (`0.5px` structural pane dividers `.hairline-b`, `.hairline-r`, `.hairline-l`)
- `--hairline-dot: rgba(245, 242, 237, 0.20)` (`1px dotted` horizontal `.dot-leader` rules)
- `--accent-brass: #B4A28A` (Editorial & Reading Signal: italic serif section numerals `2.1`, breadcrumbs `Manual / 02`, active link underlines, `::selection`)
- `--accent-sage: #9FAF9A` (Interactive & Live Signal: `.btn-primary`, `:focus-within` input underlines, stage-active punchlines, live sync indicator)

---

## 3. Canonical Component Contracts

### 3.1 The 3-Pane Application Shell (From Variant `8a6a23bf`, Upgraded for Responsiveness)
- **Top Masthead:** `h-16 px-6 lg:px-10 hairline-b shrink-0 flex items-center justify-between`
- **Left Library Rail:** `hidden md:flex w-52 lg:w-64 hairline-r p-8 lg:p-10 flex-col justify-between shrink-0`
- **Center Reading / Workbench Well:** `flex-1 px-6 md:px-12 lg:px-20 pt-12 lg:pt-16 pb-12 overflow-y-auto` housing `<article class="max-w-2xl mx-auto">`
- **Right Context / TOC Rail:** `hidden xl:block w-48 hairline-l p-10 shrink-0`

### 3.2 Editorial Section Heading Lockup (`2.1 The Dataset`)
Align an italic `Crimson Pro` brass numeral (`20px`) with a roman `Crimson Pro` light heading (`24px`) on `items-baseline`:
```html
<div class="flex items-baseline mb-4">
  <span class="font-serif italic text-xl mr-4 text-[#B4A28A]">2.1</span>
  <h2 class="font-serif text-2xl font-light text-[#F5F2ED]">The Dataset</h2>
</div>
```

### 3.3 Circular Badge + Dot-Leader Index Row (`2.2 Navigating the Craft`)
```html
<div class="flex items-center text-[11px] small-caps py-1 group cursor-pointer">
  <span class="w-4 h-4 rounded-full border border-[rgba(245,242,237,0.1)] flex items-center justify-center mr-3 text-[8px] text-[#8C8782]">A</span>
  <span class="text-[#F5F2ED] group-hover:text-[#B4A28A] transition-colors">Writing &amp; Joke Construction</span>
  <div class="dot-leader"></div>
  <span class="font-mono text-[#8C8782] tabular-nums">25 Entries</span>
</div>
```

### 3.4 Tactile Workspace Button (`.btn` & `.btn-primary`)
- `.btn`: `border: 1px solid rgba(245,242,237,0.25); border-radius: 2px; padding: 6px 14px; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.16em; background: transparent; color: #F5F2ED;`
- `.btn-primary`: `border-color: rgba(159,175,154,0.65); background: rgba(159,175,154,0.06);`

### 3.5 Architectural Bottom-Line Input (`.input-line-group`)
- Wrapper: `border-bottom: 0.5px solid rgba(245, 242, 237, 0.10); padding-bottom: 8px;` (focuses to `--accent-sage`).
- Micro-Label above: `9px`, `Inter 500`, `small-caps`, `letter-spacing: 0.18em`, `color: #5C5A55`.
- Input/Textarea: `background: transparent; border: none; outline: none; font-family: 'Crimson Pro', serif; font-size: 19px; font-weight: 300; color: #F5F2ED;`.

---

## 4. Constitutional Invariants (Never Violate)
1. **Zero Card Surfaces or Box Containers:** No `#22211F` boxes, no `border-l-2`/`border-l-4` tinted callouts, no `box-shadow`, no `border-radius` > `2px` on rectangles.
2. **Hidden Scrollbars Everywhere:** Always enforce `scrollbar-width: none` and `::-webkit-scrollbar { display: none; }`.
3. **Strict Font Role Decoupling:** `Crimson Pro` for Display, Headings, Numerals (`2.1`), Verbatim Quotes, and Primary Inputs. `Inter` for Body Prose and Small-Caps Labels. `JetBrains Mono` (`tabular-nums`) for IDs, Timestamps, and Counters.
4. **Semantic Dual-Accent Discipline:** `#B4A28A` (Brass) for editorial/reading numerals and active underlines; `#9FAF9A` (Sage) for interactive CTA buttons, input focus, and live sync status.
