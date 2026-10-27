# ComedyOS Visual Design Anti-Patterns (`DESIGN_ANTI_PATTERNS.md`)

> **LLM Invariant Directive:** This file defines strict negative constraints and positive contracts for UI generation. 
> To prevent negative priming in fast models (e.g., Gemini 3.8 Flash), forbidden patterns are defined strictly as semantic invariants (`NEVER ...`), and code blocks are reserved exclusively for the verified implementation contracts (`✅ REQUIRED`).

---

## 1. Container Architecture: Open Canvas vs. "Box Soup"

### Invariants
- **NEVER** wrap interactive elements, feature lists, or specimens in secondary background boxes (`#22211F`), cards, or nested containers ("Card-within-card sandwiches").
- **NEVER** apply 4-sided borders around content groups.
- **ALWAYS** place content directly onto the open canvas (`#1A1918`).
- **ALWAYS** establish grouping and structure through **top/bottom hairline dividers**, **left-border indentation**, or **dotted horizontal leaders**.

### ✅ REQUIRED Pattern (Open Canvas & Hairline Dividers)
```html
<div class="space-y-6">
  <div class="border-b border-[#33312E] pb-4">
    <span class="font-mono text-[9px] uppercase tracking-[0.2em] text-[#5C5A55]">01. Foundations</span>
    <h2 class="serif text-3xl font-light text-[#F5F2ED] mt-2">The Mathematics of a Joke</h2>
  </div>
  
  <!-- Left Hairline Indentation for Sub-Items -->
  <div class="pl-6 border-l border-[#33312E] space-y-4">
    <p class="text-sm font-light text-[#A19F9A] leading-relaxed">
      Stand-up structure relies on economy of syllables and unexpected pivots.
    </p>
  </div>
</div>
```

---

## 2. Input Fields: Architectural Baseline vs. Floating Grey Bricks

### Invariants
- **NEVER** put solid background fills (`#22211F`, `#2A2926`) or 4-sided borders around text `<input>` or `<textarea>` elements.
- **NEVER** use generic rounded corners (`rounded-lg`, `rounded-md`) on input containers.
- **ALWAYS** use a **100% transparent background** with a single **1px bottom border** (`border-b border-[#33312E]`).
- **ALWAYS** position an `all-small-caps` tracking label in `#5C5A55` directly above the input.

### ✅ REQUIRED Pattern (Variant Baseline Input)
```html
<div class="input-field-line">
  <label class="block text-[9px] tracking-[0.16em] uppercase text-[#5C5A55] mb-1 font-mono">
    Email Address
  </label>
  <input
    type="email"
    class="w-full bg-transparent border-none border-b border-[#33312E] pb-2 outline-none serif text-lg font-light text-[#F5F2ED] placeholder:text-[#4A4845] focus:border-[#9FAF9A] transition-colors"
    placeholder="comedian@domain.com"
  />
</div>
```

---

## 3. Interactive Buttons: Tactile Geometry vs. Clichés

### Invariants
- **NEVER** render interactive buttons as plain italic underlined text indistinguishable from body copy.
- **NEVER** render buttons as solid opaque pastel slabs (`#9FAF9A` background) with raw `0px` or bubbly `999px` pill radii.
- **ALWAYS** provide crisp tactile affordance with a `1px` structural hairline stroke and a micro-chamfer radius (`2px`).
- **ALWAYS** use `all-small-caps` uppercase tracking (`0.15em`) with tabular figures for telemetry.

### ✅ REQUIRED Pattern (Architectural & Editorial Buttons)
```css
/* Primary Conversion CTA */
.btn-architectural {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
  border-radius: 2px;
  background: rgba(159, 175, 154, 0.10);
  border: 1px solid rgba(159, 175, 154, 0.55);
  color: #F5F2ED;
  font-variant: all-small-caps;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.15em;
  transition: all 150ms cubic-bezier(0.4, 0, 0.2, 1);
}
.btn-architectural:hover {
  background: rgba(159, 175, 154, 0.20);
  border-color: #9FAF9A;
}

/* Editorial Inline Action Button */
.btn-editorial {
  background: transparent;
  border: 0;
  border-bottom: 1px solid #F5F2ED;
  padding-bottom: 4px;
  color: #F5F2ED;
  font-variant: all-small-caps;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.15em;
  transition: color 150ms ease, border-color 150ms ease;
}
.btn-editorial:hover {
  color: #9FAF9A;
  border-bottom-color: #9FAF9A;
}
```

---

## 4. Editorial Callouts & Quotes: Display Monograph vs. Bootstrap Stripes

### Invariants
- **NEVER** use thick asymmetric colored left border stripes (`border-l-4 border-emerald-500` or `border-l-4 border-amber-500`) with dark box fills.
- **NEVER** attach animated pulsing status dots (`animate-pulse`) to static labels or headings.
- **ALWAYS** set blockquotes in large unboxed display serif (`Newsreader` / `Crimson Pro`), centered or indented with small-caps attribution.
- **ALWAYS** use dotted horizontal leaders for ledger rows and timecodes.

### ✅ REQUIRED Pattern (Verbatim Quote & Ledger Row)
```html
<!-- Monograph Quote -->
<figure class="text-center py-8">
  <blockquote class="serif text-3xl sm:text-4xl italic font-light text-[#F5F2ED] leading-snug max-w-2xl mx-auto">
    “If you can say it in five words instead of ten, it’s twice as funny.”
  </blockquote>
  <figcaption class="font-mono text-[10px] uppercase tracking-[0.2em] text-[#5C5A55] mt-4">
    Jimmy Carr · Blocks Podcast · 00:14:45
  </figcaption>
</figure>

<!-- Ledger Row with Dot Leader -->
<div class="flex items-baseline w-full">
  <span class="text-sm font-light text-[#F5F2ED]">Writing Every Single Day</span>
  <div class="flex-grow border-b border-dotted border-[#33312E] mx-3 mb-1" />
  <span class="font-mono text-[10px] text-[#9FAF9A]">08:12</span>
</div>
```

---

## 5. Optical Luminance & Spacing Hierarchy

### Invariants
- **NEVER** flatten text contrast by setting rubrics and labels to `#A19F9A` to satisfy generic automated linters; this destroys the typographic ledger hierarchy.
- **NEVER** use arbitrary spacing values (`22px`, `37px`, `70px`).
- **ALWAYS** preserve the 4 strict luminance tiers against `#1A1918`:
  1. `#F5F2ED` (Primary headlines, verbatim quotes, active button text)
  2. `#A19F9A` (Body prose and reading copy)
  3. `#5C5A55` (Rubrics, uppercase labels, timestamps, metadata)
  4. `#33312E` (Hairline rules, dotted leaders, inactive structural borders)
- **ALWAYS** stick to the base-8/base-16 spacing rhythm: `{8px, 16px, 24px, 32px, 48px, 64px, 96px}`.
