# ComedyOS Design Invariants (`INVARIANT_DESIGN.md`)

An **Invariant** is a hard architectural constraint that must remain true across every page, component, and responsive breakpoint of ComedyOS. If any invariant is violated, the build fails review regardless of whether the code runs.

---

## Invariant 1: The >=95% Open Canvas Law (No Box Soup)
- **Rule:** At least **95% of the viewport area** must expose the primary `#1A1918` charcoal canvas directly.
- **Constraint:** Interactive product specimens, forms, setlist ledgers, and color token tables **must not** be wrapped in opaque secondary background containers (e.g., `#22211F` or `#282624` cards).
- **Permitted Surface Shifts:**
  1. Transient row hover (`#201F1E`).
  2. Whisper callout tint at **<=30% opacity** (`rgba(35, 34, 32, 0.30)`) with a single `2px` left border (`border-left: 2px solid #9FAF9A`).

## Invariant 2: Spacing-First Hierarchy Escalation
- **Rule:** Context areas and sections must be separated in this strict order of precedence:
  1. **Whitespace & Column Alignment** (`96px` / `64px` / `48px` gaps on the 12-column grid).
  2. **Luminance Contrast** (`#F5F2ED` vs `#A19F9A` vs `#5C5A55`).
  3. **Single-Edge Hairline** (`1px solid #33312E` on `border-bottom` or `border-left` only).
- **Constraint:** A 4-sided border (`border: 1px solid`) is prohibited on content sections, feature blocks, and text inputs. It is allowed only on:
  - Primary architectural CTA buttons (`border-radius: 2px`).
  - `12px × 12px` checkbox squares or `16px × 16px` circular index badges (`A`, `B`, `C`).
  - Single-line undo toast notices.

## Invariant 3: Transparent Bottom-Line Input Architecture
- **Rule:** Every `<input>` and `<textarea>` must have `background: transparent` and zero side or top borders.
- **Constraint:** Every input must be structured as:
  1. A stacked `9px–10px` `all-small-caps` label (`color: #5C5A55; letter-spacing: 0.15em`) above the field.
  2. A `Crimson Pro` (`18px–20px`, `font-weight: 300`) or `Inter` (`12px–13px`, `font-weight: 300`) input element.
  3. A `1px solid #33312E` bottom border (`border-bottom`) that transitions to `#9FAF9A` or `#F5F2ED` on `:focus-within`.

## Invariant 4: Intentional Button Affordance & Crisp Corners
- **Rule:** Every interactive button must be immediately recognizable as an intentional control and never as either (a) a raw, sharp-cornered opaque pastel rectangle or (b) unstyled body text.
- **Constraint:**
  - **Primary CTA Buttons** use a `2px` architectural micro-radius (`border-radius: 2px`), a `1px solid` structural border (`rgba(159, 175, 154, 0.55)`), a subtle translucent sage fill (`rgba(159, 175, 154, 0.10)`), `all-small-caps` typography (`11px`, `letter-spacing: 0.15em`, `font-weight: 500`), and a directional glyph (`→`).
  - **Secondary / Inline Actions** use `all-small-caps` (`11px`, `letter-spacing: 0.15em`, `color: #F5F2ED`) anchored by a `1px solid #F5F2ED` bottom underline (`padding-bottom: 4px`), transitioning to `#9FAF9A` on hover.

## Invariant 5: Mandatory 4-Tier Text Luminance
- **Rule:** All four text luminance tiers must be active simultaneously on every screen to create depth without boxes:
  - **Tier 1 (`#F5F2ED`):** Headings, verbatim joke lines, active controls.
  - **Tier 2 (`#A19F9A`):** Narrative prose and descriptions.
  - **Tier 3 (`#5C5A55`):** Section rubrics (`01. Foundations`), field labels, timestamps, and inactive states.
  - **Tier 4 (`#33312E`):** Structural hairlines and dotted leaders.
- **Constraint:** Never brighten Tier 3 (`#5C5A55`) to `#A19F9A`—doing so flattens the depth hierarchy and makes metadata compete with primary prose.

## Invariant 6: Modular Base-8 / Base-16 Spatial Grid
- **Rule:** All layout spacing must snap to `{8px, 16px, 24px, 32px, 48px, 64px, 96px}`.
- **Constraint:**
  - Major sections are separated by `64px` (`4rem`) padding + `64px` (`4rem`) margin across a single `1px solid #33312E` bottom rule.
  - Section headers (`01. ...`) always have `48px` (`3rem` / `mb-12`) bottom margin before the section grid begins.
  - Desktop two-column splits use `64px` (`gap-16`) or `96px` (`gap-24`) horizontal gutters.

## Invariant 7: Reference-First Precedence
- **Rule:** Whenever a user provides a reference URL or design specimen, the exact CSS rules extracted from that reference take **100% precedence** over any third-party design skill or linter warning.
