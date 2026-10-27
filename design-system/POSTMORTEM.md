# Design Drift Postmortem (`POSTMORTEM.md`)

**Subject:** Why the initial ComedyOS Waitlist Website (v1–v3) looked cheaper, boxier, and less intentional than the original Variant reference designs (`8a6a23bf`, `568d8c7f`, `782176fa`).

---

## 1. Executive Summary

When translating the three Variant.com references into the ComedyOS waitlist page, our implementation drifted away from Variant's quiet, archival elegance and regressed toward generic dark-mode SaaS patterns. Specifically:
1. We wrapped interactive specimens and the footer in **heavy opaque secondary boxes (`#22211F`)**.
2. We built form inputs as **filled grey rectangles** and the submit CTA as a **sharp-cornered opaque pastel-green brick** (`media_1792669507552_83978612.png`).
3. We let a generic third-party design linter (`Leonxlnx/taste-skill`) strip out Variant's signature `all-small-caps` labels, `#5C5A55` recessed metadata tier, and `#33312E` structural hairlines.

---

## 2. Root Causes of the Drift

### Root Cause #1: Wrapper Iframe Blindness (Incomplete Source Extraction)
- **What happened:** The three `https://variant.com/shared/<uuid>` URLs are Next.js wrapper pages that load the actual designs inside an `<iframe src="/design/<uuid>.html">`. Initially, we relied on screenshots of the top of those pages rather than fetching the raw `/design/<uuid>.html` source files.
- **What we missed:** The second Variant link (`568d8c7f` -> `/design/568d8c7f-893d-488a-96df-b7567643a865.html`) is a 1,362-line complete component specification (`ComedyOS — System Specimen v1.0`) containing the exact HTML and CSS for:
  - `02. Form Controls — Input & Action` (transparent bottom-line inputs, stacked `9px` small-caps labels, and underlined small-caps buttons)
  - `03. Note List — The Index` (open-canvas rows with `.dot-leader` and `group-hover:italic`)
  - `04. Content — Verbatim & Notes` (`pl-8 border-l hairline` stage directions and `bg-[#232220]/30` 30%-opacity callouts)
- **Lesson:** Always inspect the DOM for `<iframe src="...">` and fetch the raw design HTML before writing any code.

### Root Cause #2: Blind Obedience to a Generic Linter (`taste-skill` Collision)
- **What happened:** When asked to explore `Leonxlnx/taste-skill`, we optimized the page to score `0 FAIL` on `taste-skill`'s automated scripts (`lint.mjs` and `inspect.mjs`).
- **Why that backfired:** `taste-skill` is hardcoded with rules for generic editorial landing pages that directly contradicted Variant's design system:
  - `taste-skill` failed the page for `small-uppercase-overuse` (`>20%` uppercase/small-caps elements), so we deleted Variant's signature `.small-caps` (`font-variant: all-small-caps; letter-spacing: 0.15em`) system!
  - `taste-skill` failed the page for `low-contrast-text` on `#5C5A55`, so we brightened all metadata to `#A19F9A`. Without `#5C5A55` receding into `#1A1918`, every caption and label shouted at the same volume as the prose, forcing us to use boxes to separate content.
  - `taste-skill` encouraged putting product UI inside `data-ui="true"` containers with a distinct surface fill (`#22211F`), which created 4 huge grey boxes across the page.
- **Lesson:** External skills/linters must be treated as advisory diagnostics, never allowed to override the explicit tokens and component grammar of the user's reference design.

### Root Cause #3: Defaulting to "Box Soup" Instead of Spatial & Luminance Grouping
- **What happened:** Whenever we needed to show a product preview (OCR Scan, Unified Capture, Audio Diff, Color Tokens), we wrapped it in `.ui-specimen { background: #22211F; padding: 32px 36px; }`.
- **Why it looked cheap:** On a `#1A1918` canvas, large unbordered `#22211F` rectangles with `0px` sharp corners look like unstyled HTML `<div>` blocks. In Variant's actual spec (`variant-design-2.html`), **none** of the 6 specimen sections use a box container—they sit directly on `#1A1918`, separated by `64px` (`4rem`) of vertical whitespace, a `1px solid #33312E` bottom rule, and left-border indentation (`pl-8 border-l border-[#33312E]`).

### Root Cause #4: Generic SaaS Form Controls (`media_1792669507552_83978612.png`)
- **What happened:** We styled `<input>` fields with `background: #22211F; padding: 14px 16px; border: 0;` and the submit button with `background: #9FAF9A; color: #141413; padding: 14px 24px; border-radius: 0;`.
- **Why it failed the user's eye:**
  1. The inputs looked like generic dark-mode form boxes rather than part of a typographic ledger.
  2. The button looked like a flat, sharp-edged green brick (`0px` radius, no border refinement, sentence-case font) rather than an intentional interactive control.
  3. Inside the specimens, secondary buttons (`background: #282624; border: 1px solid rgba(245,242,237,0.12)`) looked indistinguishable from static metadata badges.

### Root Cause #5: Arbitrary `clamp()` Spacing Instead of Modular Rhythm
- **What happened:** We used fluid `clamp()` margins and arbitrary pixel gaps (`36px`, `140px`, `72px`, `56px`, `22px`, `18px`, `14px`).
- **Why it felt unintentional:** The human eye detects architectural polish when vertical and horizontal intervals repeat predictably (`48px` header-to-body, `64px` section padding + `64px` section margin, `96px` column gap). Arbitrary numbers break that rhythm.

---

## 3. Corrective Actions Taken

1. **Extracted Ground-Truth Specs:** Downloaded all three `/design/<uuid>.html` files from Variant and documented every token, class, and component in [`DESIGN.md`](file:///e:/-%20CODE/ComedyOS-2026/design-system/DESIGN.md), [`INVARIANT_DESIGN.md`](file:///e:/-%20CODE/ComedyOS-2026/design-system/INVARIANT_DESIGN.md), and [`ANTI_PATTERNS.md`](file:///e:/-%20CODE/ComedyOS-2026/design-system/ANTI_PATTERNS.md).
2. **Installed Permanent Workspace Skill:** Created [`.agent/skills/variant-faithful-design/SKILL.md`](file:///e:/-%20CODE/ComedyOS-2026/.agent/skills/variant-faithful-design/SKILL.md) so Antigravity enforces these rules automatically on future UI tasks.
3. **Re-architected the Waitlist Website (`index.html`):**
   - Removed all `#22211F` box containers and the `#22211F` footer background (>96% pure `#1A1918` open canvas).
   - Replaced the boxed inputs with Variant's exact transparent bottom-hairline inputs (`border-b border-[#33312E] pb-2`, stacked `9px` `.small-caps` `#5C5A55` label, `Crimson Pro` `18px` input text).
   - Replaced the green brick button and ambiguous specimen buttons with crisp `2px`-radius architectural CTA buttons (`border: 1px solid rgba(159, 175, 154, 0.55)`, subtle translucent sage surface, `all-small-caps` `11px` tracked text + `→`) and Variant's `border-b border-[#F5F2ED] pb-1` editorial action buttons.
   - Restored the 4-tier luminance hierarchy (`#F5F2ED` / `#A19F9A` / `#5C5A55` / `#33312E`) and Base-8/16 modular spacing rhythm (`mb-12`, `py-16`, `gap-16`, `gap-24`).
