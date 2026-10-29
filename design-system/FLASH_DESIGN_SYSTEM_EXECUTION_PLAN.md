# ComedyOS Design System: Forensic Study of Variant `8a6a23bf` & Execution Plan for Gemini Flash

> **Target Executor:** Gemini 3.8 Flash / Antigravity Subagents
> **Architect:** Gemini 4 Argon
> **Reference Authorities:**
> 1. **Variant `8a6a23bf` (`COMEDYOS Archive v1.0`):** [`design-system/specimens/variant-8a6a23bf-archive.html`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/specimens/variant-8a6a23bf-archive.html)
> 2. **Variant `568d8c7f` (`System Specimen v1.0`):** [`design-system/specimens/variant-568d8c7f-system-specimen.html`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/specimens/variant-568d8c7f-system-specimen.html)
> 3. **Methodology Standard:** [`https://getdesign.md/what-is-design-md`](https://getdesign.md/what-is-design-md) (`VoltAgent/awesome-design-md`)
> 4. **Master Specification:** [`design-system/DESIGN.md`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/DESIGN.md)

---

## Part 1: Why We Adopted the `getdesign.md` Methodology

### 1.1 The Problem: Why AI Agents Drift Into "SaaS Slop"
When an AI coding agent (especially high-speed models like Gemini Flash) is asked to build a dark-mode UI without strict structural guardrails, its pre-training weights pull it toward the statistical average of GitHub repositories:
- It invents `#1E1E1E` or `bg-zinc-900` cards with `border-radius: 12px` (`rounded-xl`).
- It wraps inputs in grey boxes with `padding: 12px` and focus rings.
- It adds glowing gradients, drop shadows, pill badges, and green pulsing dots.

### 1.2 How `getdesign.md` Solves This
The `getdesign.md` standard (originated by Google Stitch and standardized by VoltAgent across 550+ production systems) solves LLM drift by structuring `DESIGN.md` as a **two-layer compiler contract**:
1. **Layer 1 — Machine-Readable YAML Frontmatter:** Locks exact hex values, font stacks, type scale objects, spacing arrays, border rules, and radii at the top of the file so the agent never guesses a number.
2. **Layer 2 — 9 Deterministic Prose & AST Sections:**
   - `1. Visual Theme & Atmosphere`
   - `2. Color Palette & Roles (with Scarcity Rules)`
   - `3. Typography Rules & Lockups`
   - `4. Component Stylings (with Verbatim DOM Snippets)`
   - `5. Layout & Spacing Principles`
   - `6. Depth, Elevation & Shadows`
   - `7. Responsive Behavior`
   - `8. Do's and Don'ts (Negative Token Guardrails)`
   - `9. Agent Prompt Guide`

---

## Part 2: Forensic Deconstruction of Variant `8a6a23bf`

We extracted the raw 1,033-line DOM and CSS from `https://variant.com/design/8a6a23bf-cdf7-4fc4-9d01-c0ae48de2c6d.html` ([`variant-8a6a23bf-archive.html`](file:///e:/-&#32;CODE/ComedyOS-2026/design-system/specimens/variant-8a6a23bf-archive.html)). Here is the exact engineering breakdown of how Variant achieved its quiet, editorial authority—and where its flaws lie.

### 2.1 The 6 Design Choices That Make `8a6a23bf` Work So Well

#### 1. The 3-Pane `100vh` App Shell With Zero Surface Shifts
Variant locks `body` to `w-full h-screen flex flex-col overflow-hidden` on `#1A1918`:
- **Top Masthead (`h-16 px-10 hairline-b shrink-0`):** Fixed `64px` height. Left side pairs `<span class="font-serif text-xl font-light tracking-tight">COMEDYOS</span>` with `<span class="text-[10px] small-caps text-[#8C8782] mt-1">Archive v1.0</span>`. Right side holds an inline search icon + unboxed `<input>` and two small-caps links (`Dictionary`, `GitHub`).
- **Left Library Rail (`w-64 hairline-r p-10 flex flex-col justify-between shrink-0`):** `256px` wide, `40px` (`p-10`) padding. Houses two navigation groups (`Library` and `The Craft`) at the top and a recessed `9px` colophon (`ComedyOS Archive / Verbatim Knowledge Base / Est. 2024`) pinned to the bottom.
- **Center Reading Well (`flex-1 px-20 pt-16 pb-8 overflow-y-auto`):** Scrollable center canvas with hidden scrollbars (`scrollbar-width: none`) and generous `80px` (`px-20`) horizontal padding framing a `672px` (`max-w-2xl mx-auto`) `<article>`.
- **Right Context Rail (`w-48 hairline-l p-10 shrink-0`):** `192px` wide, `40px` padding. Houses `On This Page` anchor links (`2.1 The Dataset`, `2.2 Navigating`, `2.3 Exporting`) and bottom metadata (`Related`, `Citation Style`).
- **Key Insight:** All four regions share the **exact same `#1A1918` background**. None of the sidebars use a darker or lighter fill.

#### 2. Sub-Pixel `0.5px` Translucent Hairlines
Instead of `1px solid #333333`, `8a6a23bf` defines:
```css
.hairline-b { border-bottom: 0.5px solid rgba(245, 242, 237, 0.1); }
.hairline-r { border-right: 0.5px solid rgba(245, 242, 237, 0.1); }
.hairline-l { border-left: 0.5px solid rgba(245, 242, 237, 0.1); }
```
Using `0.5px` at `10%` opacity of the primary bone ink (`#F5F2ED`) creates a line that feels like a laser-etched bookbinding rule rather than a web border.

#### 3. Inline Luminance Highlighting (Why Body Prose is `#8C8782`, Not `#F5F2ED`)
In `8a6a23bf`, all body paragraphs (`<p>`) are set in muted warm stone (`#8C8782`), **not** primary white/bone (`#F5F2ED`).
- Why? Because when standard prose sits at ~55% luminance (`#8C8782`), Variant can highlight a key phrase inside a sentence simply by changing its color to `#F5F2ED`:
  ```html
  <p class="text-sm text-[#8C8782] leading-relaxed">
    Use this resource not as a narrative, but as a <span class="text-[#F5F2ED]">typographic ledger</span> for studying the mechanics of humor.
  </p>
  ```
- This eliminates the need for heavy `<strong>` bold tags, colored pill badges, or inline `<code>` boxes.

#### 4. The Fine-Press Section Heading Lockup (`2.1 The Dataset`)
Every section heading pairs an **italic `Crimson Pro` numeral in warm brass (`#B4A28A`)** with a **roman `Crimson Pro` light heading in bone (`#F5F2ED`)** aligned on their typographic baseline (`flex items-baseline`):
```html
<div class="flex items-baseline mb-4">
  <span class="font-serif italic text-xl mr-4 text-[#B4A28A]">2.1</span>
  <h2 class="font-serif text-2xl font-light text-[#F5F2ED]">The Dataset</h2>
</div>
```

#### 5. The Circular Badge + Dot-Leader Index (`2.2 Navigating the Craft`)
Instead of cards or tables, `8a6a23bf` presents its 5 archive categories as a vertical stack (`space-y-3 text-[11px] small-caps`) where each row has:
1. A `16px × 16px` (`w-4 h-4`) circular hairline badge (`rounded-full border border-[rgba(245,242,237,0.1)] text-[8px]`) holding a letter (`A`, `B`, `C`, `D`, `E`).
2. The category title in `#F5F2ED`.
3. A horizontal dotted leader (`.dot-leader`: `border-bottom: 1px dotted rgba(245, 242, 237, 0.2); margin: 0 8px; position: relative; top: -4px;`).
4. The entry count in `#8C8782` (`25 Entries`).

#### 6. Editorial Pagination Footer
At the bottom of the `<article>`, `8a6a23bf` places a ultra-faint top border (`border-t border-[rgba(245,242,237,0.05)] pt-16 pb-12`) with left/right navigation links that pair an italic `Crimson Pro` arrow (`←` / `→` at `text-lg`) with `10px` `small-caps` chapter labels (`01 Introduction` / `03 Categories`).

---

### 2.2 Critical Audit: What Is Imperfect in `8a6a23bf` (And How We Fix It)

While `8a6a23bf` is a masterclass in static editorial layout, it has **5 concrete usability and engineering flaws** when applied to an interactive application like ComedyOS:

| # | Flaw in Raw Variant `8a6a23bf` | Impact on ComedyOS Usability | Our Architectural Fix in ComedyOS `DESIGN.md` v2.0 |
| :---: | :--- | :--- | :--- |
| **1** | **No Tactile Button Component:** `8a6a23bf` has zero `<button>` elements. In line 985, `"Export Dashboard"` is just `<span class="text-[#F5F2ED] italic">` with no button border, cursor, or link! | In an interactive joke writer or workbench, users cannot tell which text is a clickable command vs. static prose (*"The Invisible Button Flaw"*). | **Split Navigation vs. Action Affordance:** Keep `8a6a23bf`'s borderless text links strictly for **Navigation Rails** (Sidebar, TOC, Header, Footer). Enforce the tactile **`.btn` contract** (`1px solid rgba(245,242,237,0.25)`, `2px` radius, `6px 14px` padding, uppercase tracking) on all **Workspace Action Buttons**. |
| **2** | **Non-Responsive Fixed Desktop Widths:** Hardcodes `w-64` (`256px`), `px-20` (`160px` total horizontal padding), and `w-48` (`192px`) with `body { overflow: hidden }`. | On any viewport narrower than `1100px` (laptop split-screen, iPad, mobile), `608px` is consumed by sidebars and padding, crushing the center text column and clipping content without scrollbars. | **3-Tier Responsive Collapse:** `>1200px` = Full 3-pane; `768px–1200px` = Hide Right TOC Rail (`hidden xl:block`) & reduce center padding to `px-8`; `<768px` = Unlock `body` overflow and switch to single-column / Mobile Keep view. |
| **3** | **Zero Focus Feedback on Search Input:** Line 846 `<input>` has `border-none outline-none` with no `:focus` rule. | Clicking into the search input gives zero visual confirmation of focus or field width. | **Focus-Within Hairline:** Wrap header search in `.search-group` with `border-bottom: 1px solid transparent` that transitions to `border-bottom-color: #B4A28A` (or `#9FAF9A`) on `:focus-within`. |
| **4** | **Proportional Numerals in Counters:** `25 Entries` and `03 Entries` use standard `Inter` without `tabular-nums` or monospace. | In live timers (`00:42`), word counts (`142 WORDS`), or bit codes (`B-104`), proportional digits shift width horizontally as numbers change. | **Enforce `JetBrains Mono` / `tabular-nums`:** Apply `font-variant-numeric: tabular-nums` and `--font-mono` to all counters, durations, and bit IDs. |
| **5** | **Unresolved Brass (`#B4A28A`) vs. Sage (`#9FAF9A`) Accent Split:** `8a6a23bf` uses `#B4A28A` warm brass, whereas `568d8c7f` uses `#9FAF9A` surgical sage. | Mixing both randomly makes pages feel undecided. | **Semantic Accent Partitioning:** Assign **`#B4A28A` (Brass)** to *Archival & Editorial Reading Signals* (section numerals `2.1`, active nav underline, text `::selection`). Assign **`#9FAF9A` (Sage)** to *Live Workspace & Interactive Signals* (`.btn-primary`, input focus baseline, stage-active punchline, live Supabase sync). |

---

## Part 3: Synthesis from Kindred Design Systems

To ensure our system is rock-solid across every screen type (Documentation Archive, Joke Workbench, Setlist Builder, Mobile Keep), we pulled four proven mechanisms from kindred editorial/technical systems:

1. **From Stripe Press & Craig Mod Monographs:**
   - **Baseline-Locked Numeral + Heading (`items-baseline`):** Never stack a section number above an `H2` inside a card; place it inline to the left in italic serif (`2.1 The Dataset`).
   - **Bottom-Pinned Colophon (`text-[9px] small-caps text-[#4A4845]`):** Anchors the bottom of the left sidebar with quiet archival metadata (`ComedyOS Archive / Verbatim Knowledge Base`).
2. **From Linear (Dark Mode Precision):**
   - **Sub-Pixel Pane Dividers (`0.5px solid rgba(245,242,237,0.10)`):** Full-bleed vertical and horizontal hairlines that divide a `100vh` viewport into independent scrolling zones (`overflow-y-auto` on center well, `shrink-0` on sidebars).
   - **Inline Keyboard Shortcut Hints (`Alt+S`, `Cmd+J`):** Rendered in `JetBrains Mono` `9px` `color: #5C5A55` inside button labels or progressive rails.
3. **From iA Writer & Obsidian Minimal:**
   - **Unboxed Writing Flow:** Textareas (`Crimson Pro` `19px` `font-light`) sit directly on `#1A1918` anchored only by a bottom hairline (`1px solid rgba(245,242,237,0.10)`), allowing raw brain dumps and structured joke blocks to feel like a single continuous manuscript.
4. **From `getdesign.md` (`VoltAgent/awesome-design-md`):**
   - **Negative Token Linting:** Explicitly banning high-probability LLM CSS tokens (`rounded-lg`, `shadow-md`, `bg-zinc-900`, `border-l-4`) via a pre-commit / post-generation regex check.

---

## Part 4: Execution Plan for Gemini Flash

When Gemini Flash is invoked to build, refactor, or expand any ComedyOS UI screen (e.g., upgrading the Archive Reader, Setlist Timeline, or Joke Workbench), it MUST execute the following **4-Step Deterministic Protocol**.

### Step 1: Inject the Locked CSS Foundation Verbatim
Gemini Flash must **never** improvise global styles. Paste this exact `<style id="comedyos-design-system">` block into the `<head>` of every standalone HTML file or global stylesheet:

```css
/* ==========================================================================
   COMEDYOS DESIGN SYSTEM v2.0 (VARIANT 8a6a23bf + 568d8c7f CANONICAL TOKENS)
   ========================================================================== */
@import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,200;0,300;0,400;1,200;1,300&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@300;400&display=swap');

:root {
  /* Surfaces (Zero Card Fills) */
  --bg: #1A1918;
  --surface-hover: #201F1E;
  --surface-whisper: rgba(35, 34, 32, 0.30);

  /* 4-Tier Warm Monochrome Luminance */
  --ink: #F5F2ED;                /* Tier 1: Primary headings, verbatim scripts, inline highlights */
  --ink-secondary: #8C8782;      /* Tier 2: Body prose, inactive nav links, TOC items */
  --ink-muted: #5C5A55;          /* Tier 3: Small-caps field labels, timestamps, bit codes */
  --ink-recessed: #4A4845;       /* Tier 4: Placeholders, colophon, tertiary group headers */

  /* Sub-Pixel Hairlines & Borders */
  --hairline: rgba(245, 242, 237, 0.10);
  --hairline-faint: rgba(245, 242, 237, 0.05);
  --hairline-dot: rgba(245, 242, 237, 0.20);
  --hairline-btn: rgba(245, 242, 237, 0.25);
  --hairline-btn-hover: rgba(245, 242, 237, 0.75);

  /* Semantic Accents */
  --accent-brass: #B4A28A;       /* Editorial numerals (2.1), active nav underline, ::selection */
  --accent-sage: #9FAF9A;        /* Interactive primary CTA, input focus, live sync state */
  --accent-sage-border: rgba(159, 175, 154, 0.65);
  --accent-sage-fill: rgba(159, 175, 154, 0.06);
  --accent-sage-fill-hover: rgba(159, 175, 154, 0.14);
  --alert-terracotta: #E26D5C;   /* Diff strikethroughs & destructive alerts only */

  /* Typography */
  --font-serif: 'Crimson Pro', Georgia, serif;
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

*, *::before, *::after {
  box-sizing: border-box;
  -ms-overflow-style: none !important;
  scrollbar-width: none !important;
}
*::-webkit-scrollbar {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
}

::selection {
  background: var(--accent-brass);
  color: var(--bg);
}

body {
  margin: 0;
  background-color: var(--bg);
  color: var(--ink);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
}

/* Typography Utilities */
.font-serif { font-family: var(--font-serif); }
.font-sans  { font-family: var(--font-sans); }
.font-mono  { font-family: var(--font-mono); font-variant-numeric: tabular-nums; }

.small-caps {
  font-variant: small-caps;
  letter-spacing: 0.12em;
}
.micro-label {
  font-family: var(--font-sans);
  font-size: 9px;
  font-weight: 500;
  font-variant: small-caps;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  color: var(--ink-recessed);
}

/* Sub-Pixel Structural Hairlines (From Variant 8a6a23bf) */
.hairline-b { border-bottom: 0.5px solid var(--hairline); }
.hairline-t { border-top: 0.5px solid var(--hairline); }
.hairline-r { border-right: 0.5px solid var(--hairline); }
.hairline-l { border-left: 0.5px solid var(--hairline); }

/* The Signature Dot Leader */
.dot-leader {
  flex-grow: 1;
  border-bottom: 1px dotted var(--hairline-dot);
  margin: 0 10px;
  position: relative;
  top: -4px;
  min-width: 16px;
}

/* Tactile Workspace Button Contract (.btn) */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 6px 14px;
  font-family: var(--font-sans);
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--hairline-btn);
  border-radius: 2px;
  cursor: pointer;
  transition: all 180ms cubic-bezier(0.25, 0.1, 0.25, 1);
  user-select: none;
}
.btn:hover {
  border-color: var(--hairline-btn-hover);
  color: #FFFFFF;
  background: rgba(245, 242, 237, 0.04);
}
.btn-primary {
  border-color: var(--accent-sage-border);
  background: var(--accent-sage-fill);
}
.btn-primary:hover {
  border-color: var(--accent-sage);
  background: var(--accent-sage-fill-hover);
}

/* Architectural Bottom-Line Input Contract (.input-line-group) */
.input-line-group {
  border-bottom: 0.5px solid var(--hairline);
  padding-bottom: 8px;
  transition: border-color 150ms ease;
}
.input-line-group:focus-within {
  border-bottom-color: var(--accent-sage);
}
.input-editorial {
  width: 100%;
  background: transparent;
  border: none;
  outline: none;
  font-family: var(--font-serif);
  font-size: 19px;
  font-weight: 300;
  line-height: 1.55;
  color: var(--ink);
  resize: none;
}
.input-editorial::placeholder {
  color: var(--ink-recessed);
  font-style: italic;
}
```

---

### Step 2: Assemble Views Using the 5 Canonical HTML AST Templates

Gemini Flash must copy these exact HTML patterns when constructing screens:

#### Template A: The 3-Pane Application / Archive Shell (`8a6a23bf` Upgraded with Responsive Collapse)
```html
<body class="w-full h-screen flex flex-col overflow-hidden bg-[#1A1918] text-[#F5F2ED]">
  <!-- 1. TOP MASTHEAD (64px) -->
  <header class="h-16 w-full flex items-center justify-between px-6 lg:px-10 hairline-b shrink-0">
    <div class="flex items-center gap-4">
      <span class="font-serif text-xl font-light tracking-tight">COMEDYOS</span>
      <span class="text-[10px] small-caps text-[#8C8782] mt-1">Archive v1.0</span>
    </div>
    <div class="flex items-center gap-6">
      <div class="flex items-center gap-2 border-b border-transparent focus-within:border-[#B4A28A] pb-0.5 transition-colors">
        <input type="text" placeholder="SEARCH ARCHIVE..." class="bg-transparent border-none outline-none text-[10px] small-caps text-[#F5F2ED] w-36 lg:w-48 placeholder:text-[#4A4845]" />
      </div>
      <button type="button" class="btn btn-primary">+ New Entry</button>
    </div>
  </header>

  <!-- 2. 3-PANE BODY -->
  <div class="flex flex-1 overflow-hidden">
    <!-- LEFT NAVIGATION RAIL (256px on lg, hidden on mobile) -->
    <aside class="hidden md:flex w-52 lg:w-64 hairline-r p-8 lg:p-10 flex-col justify-between shrink-0">
      <div class="space-y-8">
        <div>
          <h4 class="text-[10px] small-caps text-[#8C8782] mb-4">Library</h4>
          <ul class="space-y-3 text-[11px] tracking-wide">
            <li class="flex items-baseline group cursor-pointer text-[#8C8782]">
              <span class="mr-2">01.</span>
              <span class="group-hover:text-[#B4A28A] transition-colors">Introduction</span>
            </li>
            <li class="flex items-baseline group cursor-pointer text-[#F5F2ED]">
              <span class="text-[#B4A28A] mr-2">02.</span>
              <span class="font-medium underline underline-offset-4 decoration-[#B4A28A]">Getting Started</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="text-[9px] small-caps text-[#4A4845] leading-relaxed">
        ComedyOS Archive<br />Verbatim Knowledge Base
      </div>
    </aside>

    <!-- CENTER READING / WORKBENCH WELL -->
    <main class="flex-1 overflow-hidden flex">
      <div class="flex-1 px-6 md:px-12 lg:px-20 pt-12 lg:pt-16 pb-12 overflow-y-auto">
        <article class="max-w-2xl mx-auto">
          <!-- Content goes here -->
        </article>
      </div>

      <!-- RIGHT CONTEXT / TOC RAIL (192px, visible on xl+) -->
      <aside class="hidden xl:block w-48 hairline-l p-10 shrink-0">
        <h4 class="text-[9px] small-caps text-[#8C8782] mb-6 tracking-[0.2em]">On This Page</h4>
        <ul class="space-y-4 text-[10px] tracking-wide text-[#8C8782]">
          <li><a href="#section-1" class="hover:text-[#F5F2ED] transition-colors">2.1 The Dataset</a></li>
        </ul>
      </aside>
    </main>
  </div>
</body>
```

#### Template B: Editorial Chapter Header & Section Lockup (`8a6a23bf` Lines 916–935)
```html
<header class="mb-12">
  <div class="text-[10px] small-caps text-[#B4A28A] mb-2">Manual / 02</div>
  <h1 class="font-serif text-5xl font-light mb-6 text-[#F5F2ED]">Getting Started</h1>
  <p class="text-[#8C8782] text-sm leading-relaxed italic">
    An orientation guide for navigating the verbatim records of modern comedy masterclasses.
  </p>
</header>

<section id="the-dataset" class="mb-12">
  <div class="flex items-baseline mb-4">
    <span class="font-serif italic text-xl mr-4 text-[#B4A28A]">2.1</span>
    <h2 class="font-serif text-2xl font-light text-[#F5F2ED]">The Dataset</h2>
  </div>
  <p class="text-sm text-[#8C8782] leading-relaxed mb-4">
    Each entry is cataloged with a precise timestamp and source attribution. Use this resource not as a narrative, but as a <span class="text-[#F5F2ED]">typographic ledger</span> for studying the mechanics of humor.
  </p>
</section>
```

#### Template C: Circular Badge + Dot-Leader Index List (`8a6a23bf` Lines 945–976)
```html
<div class="space-y-3 text-[11px] small-caps">
  <div class="flex items-center group cursor-pointer py-1">
    <span class="w-4 h-4 rounded-full border border-[rgba(245,242,237,0.1)] flex items-center justify-center mr-3 text-[8px] text-[#8C8782] group-hover:border-[#B4A28A] group-hover:text-[#B4A28A]">A</span>
    <span class="text-[#F5F2ED] group-hover:text-[#B4A28A] transition-colors">Writing &amp; Joke Construction</span>
    <div class="dot-leader"></div>
    <span class="font-mono text-[#8C8782]">25 Entries</span>
  </div>
</div>
```

---

### Step 3: Run Pre-Commit Negative Token Verification

Before Gemini Flash marks any UI task complete, it must verify that **zero** banned CSS patterns exist in the output:
1. **No Card Backgrounds:** Search for `bg-[#22`, `bg-zinc`, `bg-neutral`, `bg-gray`, `bg-slate` -> Must return `0` matches.
2. **No Rounded Corners > 2px:** Search for `rounded-md`, `rounded-lg`, `rounded-xl`, `rounded-2xl`, `border-radius: 4px`, `border-radius: 8px` -> Must return `0` matches.
3. **No Shadows or Blur:** Search for `shadow-`, `box-shadow`, `backdrop-blur`, `backdrop-filter` -> Must return `0` matches.
4. **No Thick Left Callout Stripes:** Search for `border-l-2`, `border-l-4` -> Must return `0` matches.
5. **Every `<button>` Has `.btn`:** Search for `<button` without `class="...btn..."` -> Must return `0` matches.

---

### Step 4: Concrete Next Tasks Ready for Gemini Flash to Execute

When you switch to **Gemini 3.8 Flash** to build out the next screens of ComedyOS, you can assign any of these self-contained tasks by pointing Flash to this file (`design-system/FLASH_DESIGN_SYSTEM_EXECUTION_PLAN.md`):

- **Flash Task A — Build the Interactive `COMEDYOS Archive v1.0` Reader (`ComedyOS-app/archive-reader.html`):**
  Take the static Variant `8a6a23bf` layout and wire it directly to our live 70 stand-up craft quotes (`output/standup_craft_quotes.json`) and the 224 Google Keep notes so clicking `01. Introduction`, `03. Categories`, `04. Masterclasses`, or `A. Writing & Joke Construction` dynamically renders the verbatim quotes in the center reading well with live search and right-rail TOC anchors.
- **Flash Task B — Harmonize `joke-writer.html` with `8a6a23bf`'s 3-Pane Chrome & `0.5px` Sub-Pixel Hairlines:**
  Refine the top masthead of `joke-writer.html` to use `8a6a23bf`'s exact brand lockup (`COMEDYOS` in `Crimson Pro` `20px` + `Workbench v1.0` in `10px` `small-caps` `#8C8782`), `0.5px solid rgba(245,242,237,0.10)` dividers, and italic brass section numerals (`1.1`, `1.2`).
- **Flash Task C — Automated Design Linter Script (`ComedyOS-app/scripts/lint-design.mjs`):**
  Create an automated `npm run lint:design` script that parses all `.html` and `.tsx` files against the YAML tokens in `design-system/DESIGN.md` and fails the build if any banned SaaS classes or unstyled buttons are introduced.
