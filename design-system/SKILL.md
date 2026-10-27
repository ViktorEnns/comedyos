---
name: variant-faithful-design
description: Recreate reference UI designs (especially Variant.com designs and the ComedyOS Archive aesthetic) with 1:1 structural, typographic, and spatial fidelity. Use whenever the user provides reference URLs, Variant links, screenshots, or asks to build or refine UI/websites matching the ComedyOS design language.
---

# Variant-Faithful Design Recreation Skill (`SKILL.md`)

When given a reference design (such as a `variant.com/shared/<uuid>` link, a live URL, or reference screenshots), your primary objective is **1:1 structural and atmospheric fidelity to the reference**, not generic "best-practice SaaS" substitution.

> [!IMPORTANT]
> **The Reference Overrides Generic Linters:** Never allow a generic design linter (such as `taste-skill`) to strip out the signature DNA of a user-provided reference (e.g., removing `all-small-caps`, brightening intentionally recessed `#5C5A55` metadata, or forcing boxed cards and solid brick buttons where the reference uses open canvas and hairline rules).

---

## Phase 1: Ground-Truth Source Extraction (Mandatory First Step)

Before writing a single line of HTML or CSS, extract the actual source code and computed styles of the reference:

1. **Unwrap Wrapper Iframes (Especially `variant.com`):**
   - A `https://variant.com/shared/<uuid>` URL is a Next.js wrapper shell that embeds an `<iframe>`.
   - **Always fetch the raw design HTML directly** from:
     `https://variant.com/design/<uuid>.html`
   - Never rely solely on above-the-fold screenshots when the underlying HTML/CSS is reachable; screenshots often clip scrollable specimen sections (such as form controls, index lists, and footer states).
2. **Inventory Exact Tokens from Source CSS:**
   - Extract the exact hex/RGBA values for canvas (`#1A1918`), primary ink (`#F5F2ED`), secondary prose (`#A19F9A`), recessed metadata (`#5C5A55`), structural hairlines (`#33312E` or `rgba(245, 242, 237, 0.1)`), and surgical accents (`#9FAF9A`, `#B4A28A`, `#E26D5C`).
   - Extract the exact font families, weights (`200`, `300`, `400`, `500`, `600`), and helper classes (`.serif`, `.small-caps`, `.dot-leader`, `.hairline`).
3. **Catalog Every Atomic Component in the Reference:**
   - How does the reference build a **text input**?
   - How does the reference build a **button** (primary, secondary, active, disabled)?
   - How does the reference separate **sections** and **context areas**?
   - What **spacing multiples** (`mb-12`, `mb-24`, `gap-16`, `gap-24`, `p-12 lg:p-24`) govern the rhythm?

---

## Phase 2: Layout & Surface Hierarchy ("Spacing First, Hairlines Second, Boxes Last")

 LLMs default to "box soup"—wrapping every feature, form, or demo inside a secondary `background: #222` card with `border: 1px solid` and `padding: 32px`. **This immediately cheapens an editorial dark interface.**

Follow this strict 4-step escalation ladder to create grouping and context:

1. **Step 1 — Macro Whitespace & Grid Alignment (Use for 80% of layout structure):**
   - Separate major ideas with `64px` (`4rem`) to `96px` (`6rem`) of open `#1A1918` canvas.
   - Align elements strictly to a 12-column grid (`grid-cols-12 gap-16` or `gap-24`) so the invisible vertical axes of left and right columns create structure without drawing a single line.
2. **Step 2 — 4-Tier Luminance Contrast (Use to separate metadata from content):**
   - Instead of putting metadata inside a badge or pill box, lower its luminance to `#5C5A55` (`all-small-caps`, `10px–11px`, `letter-spacing: 0.12em–0.15em`) so it recedes into the `#1A1918` canvas while `#F5F2ED` titles step forward.
3. **Step 3 — Single-Edge Hairlines & Dot Leaders (Use only after spacing is exhausted):**
   - When two regions or rows require explicit separation, use a **single-edge** `1px` or `0.5px` rule (`border-bottom: 1px solid #33312E` or `border-left: 1px solid #33312E` with `pl-8`), or a horizontal `.dot-leader` (`border-bottom: 1px dotted #33312E`).
   - **Never** wrap a section or interactive specimen in a 4-sided box when a top/bottom hairline or left-border indent (`pl-8 border-l border-[#33312E]`) will do.
4. **Step 4 — Whisper Surface Tints (Maximum 20%–30% Opacity):**
   - If a callout or active row requires a surface shift, tone it down by at least 50%–70%: use `rgba(35, 34, 32, 0.30)` (`bg-[#232220]/30`) with a `2px` left accent border (`border-l-2 border-[#9FAF9A]`), or a transient row hover `hover:bg-[#201F1E]`.
   - Never place large opaque secondary rectangles (`#22211F`, `#282624`) on the `#1A1918` field.

---

## Phase 3: Component Fidelity Rules (Inputs, Buttons, Corners)

### 1. Input Fields (Never Boxed Rectangles)
- **Forbidden:** Filled grey rectangles (`background: #222; padding: 14px; border-radius: 0`).
- **Required (Variant Pattern):**
  - Transparent background (`background: transparent; border: none; outline: none;`).
  - Wrapped in a container with a single bottom hairline (`border-bottom: 1px solid #33312E; padding-bottom: 8px; transition: border-color 150ms ease;`) that highlights to `#9FAF9A` or `#F5F2ED` on `:focus-within`.
  - Preceded by a stacked micro-label (`font-variant: all-small-caps; font-size: 9px–10px; letter-spacing: 0.15em; color: #5C5A55; display: block; margin-bottom: 4px;`).
  - Input text set in `Crimson Pro` (`18px`, `font-weight: 300`, `color: #F5F2ED`) for primary fields, or `Inter` (`12px–13px`, `font-weight: 300`) for utility/search fields, with a recessed placeholder (`#4A4845` or `#5C5A55`).

### 2. Buttons (Intentional Affordance & Crisp Geometry)
- **Forbidden:** Chunky, sharp-cornered opaque pastel bricks (`background: #9FAF9A; color: #141413; border-radius: 0; font-size: 14px`) or unstyled text that looks indistinguishable from body copy.
- **Required:**
  - **Primary Architectural Button (High-Conversion CTAs):**
    - Must look unmistakably like a crafted, tactile control without overpowering the dark canvas:
    - Use a refined `2px` micro-radius (`border-radius: 2px` — eliminates the "raw unstyled HTML block" look while staying crisp and architectural), a `1px solid` structural border (`border: 1px solid rgba(159, 175, 154, 0.55)` or `1px solid #F5F2ED`), a subtle translucent surface (`background: rgba(159, 175, 154, 0.10)`), and `all-small-caps` typography (`font-variant: all-small-caps; font-size: 11px; letter-spacing: 0.15em; font-weight: 500; color: #F5F2ED; padding: 10px 20px`) paired with a directional arrow (`→`).
    - On hover: `background: rgba(159, 175, 154, 0.20); border-color: #9FAF9A; color: #F5F2ED;`.
  - **Editorial Underline Action (Secondary / Inline Specimen Actions):**
    - Direct from Variant `02. Form Controls`: `font-variant: all-small-caps; font-size: 11px; letter-spacing: 0.15em; color: #F5F2ED; border-bottom: 1px solid #F5F2ED; padding-bottom: 4px;` transitioning to `color: #9FAF9A; border-color: #9FAF9A;` on hover.
  - **Ghost / Filter Tag Action:**
    - `font-variant: all-small-caps; font-size: 10px–11px; letter-spacing: 0.15em; color: #A19F9A;` (`#9FAF9A` when active, `#F5F2ED` on hover).

---

## Phase 4: Pre-Delivery Visual Audit Checklist

Before presenting any rendered page to the user, open the headless browser screenshot and verify:
1. [ ] **Canvas Ratio:** Is at least 95% of the viewport background pure `#1A1918`? (If you see big grey rectangular cards, remove their backgrounds immediately.)
2. [ ] **Input Check:** Are all `<input>` and `<textarea>` elements transparent with a `1px solid #33312E` bottom border and a `9px` `all-small-caps` `#5C5A55` label above them?
3. [ ] **Button Check:** Do primary buttons have a `2px` crisp architectural radius, a `1px` border, `all-small-caps` tracked typography, and clear interactive affordance? Are there zero opaque pastel bricks?
4. [ ] **Spacing Grid Check:** Are all vertical and horizontal gaps strict multiples of the `8px / 16px / 24px / 32px / 48px / 64px / 96px` scale?
5. [ ] **Luminance Depth Check:** Are all four text tiers (`#F5F2ED`, `#A19F9A`, `#5C5A55`, `#33312E`) present so metadata recedes and primary content pops without boxes?
