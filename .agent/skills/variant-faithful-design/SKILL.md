---
name: variant-faithful-design
description: Recreate reference UI designs (especially Variant.com designs and the ComedyOS Gallery Editorial / Typographic Ledger aesthetic) with 1:1 structural, typographic, and spatial fidelity. Synthesizes the Google AI Studio Gallery Editorial Extract and the Forensic Variant DOM Extract.
---

# ComedyOS Gallery Editorial & Variant-Faithful Design Skill (`SKILL.md`)

Use this skill whenever building or refining ComedyOS interfaces, landing pages, documentation engines, or recreating Variant.com reference designs.

## 0. Mental Model: "The Interface is the Gallery; Content is the Exhibit"
- Treat the viewport like a matte, unhurried museum exhibition wall or literary monograph (`#1A1918`).
- Hierarchy is established through **type scale, 4-tier optical luminance, and macro whitespace** (`{8, 16, 24, 32, 48, 64, 96}px`)—**NEVER** through cards, secondary background boxes, drop-shadows, `border-l-2`/`border-l-4` callout stripes, or pulsing status dots.
- Every clickable button MUST have **crisp tactile affordance** (`.btn`: `1px solid` hairline stroke, `2px` radius, `7px 16px` padding, uppercase `0.16em` tracking) so buttons are never confused with static text and never rendered as heavy opaque bricks.

---

## 1. Ground-Truth Extraction Protocol (When Given Reference URLs)
1. **Unwrap `variant.com/shared/<uuid>` Iframes:**
   - Variant shared links wrap the actual design inside `<iframe src="/design/<uuid>.html">`. Always fetch `https://variant.com/design/<uuid>.html` first to inspect the full DOM and CSS before writing code.
2. **Reference DNA Overrides Generic Linters:**
   - Never allow generic third-party linters (`taste-skill`) to strip uppercase/small-caps labels, brighten intentionally recessed `--ink-faint` metadata, or force opaque `data-ui` box containers onto the `#1A1918` canvas.

---

## 2. Pre-Flight Token Checklist
Verify these exact tokens in global CSS before generating any markup:
- `--bg: #1A1918` (deep matte charcoal canvas; >=96% of viewport)
- `--ink: #F5F2ED` (Tier 1: primary headlines, verbatim quotes, active controls)
- `--ink-muted: #A19F9A` (Tier 2: standard body prose, descriptions)
- `--ink-faint: rgba(245, 242, 237, 0.45)` (Tier 3: recessed rubrics, timestamps, `9px` input labels; equivalent to `#5C5A55`)
- `--hairline: rgba(245, 242, 237, 0.10)` (Tier 4: `1px` dividers and `.dot-leader` rules; equivalent to `#33312E`)
- `--hairline-btn: rgba(245, 242, 237, 0.25)` (tactile button stroke)
- `--accent: #9FAF9A` (muted sage; sole focal accent per view)

---

## 3. Canonical Component Contracts

### 3.1 The Button Contract (`.btn` & `.btn-primary`)
Every clickable action (Submit, Navigate, Switch Stage, Record, Filter, Undo) MUST use `.btn`:
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
  border-color: rgba(245, 242, 237, 0.75);
  color: #FFFFFF;
  background: rgba(245, 242, 237, 0.04);
}
.btn-primary {
  padding: 10px 20px;
  border-color: rgba(159, 175, 154, 0.65);
  background: rgba(159, 175, 154, 0.06);
}
.btn-primary:hover {
  border-color: var(--accent);
  background: rgba(159, 175, 154, 0.14);
}
```

### 3.2 The Architectural Input Contract (`.input-line-group`)
Never put a background fill or 4-sided border on `<input>` or `<textarea>`:
- Wrapper: `border-bottom: 1px solid var(--hairline); padding-bottom: 8px;` (focuses to `--accent`).
- Micro-Label above: `9px`, `Inter 500`, `text-transform: uppercase`, `letter-spacing: 0.16em`, `color: var(--ink-faint)`.
- Input element: `background: transparent; border: none; outline: none; font-family: 'Crimson Pro', serif; font-size: 19px; font-weight: 300; color: var(--ink);`.

### 3.3 The Typographic Ledger & Dot Leader (`.index-row`)
- Connect left-aligned `Crimson Pro` titles (`20px`, transitioning to `italic` on hover) to right-aligned `JetBrains Mono` / `tabular-nums` metadata using `.dot-leader` (`flex-grow: 1; border-bottom: 1px dotted var(--hairline); margin: 0 12px 6px 12px;`).

---

## 4. Constitutional Invariants (Never Violate)
1. **Zero Card Surfaces or Box Containers:** No `#22211F` specimen boxes, no `border-l-2`/`border-l-4` tinted callout boxes, no drop shadows.
2. **Universal Tactile Button Affordance:** No bare underlined text buttons (`The Invisible Button Flaw`) and no solid-fill pastel bricks. All buttons use `.btn` (`2px` radius, `1px` stroke).
3. **Strict Font Role Decoupling:** `Crimson Pro` for Display, Headings, Verbatim Quotes, and Primary Inputs. `Inter` for Body Prose and Uppercase/Small-Caps Labels. `JetBrains Mono` for IDs and Timestamps.
4. **Restrained Single-Accent Budget:** `#9FAF9A` sage is the only focal accent color. Never use decorative status dots (`rounded-full`) next to text counters.
5. **Base-8 / Base-16 Spatial Grid:** Snap all spacing strictly to `{8px, 16px, 24px, 32px, 48px, 64px, 96px}`.
