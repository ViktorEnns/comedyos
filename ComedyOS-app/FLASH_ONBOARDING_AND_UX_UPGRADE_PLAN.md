# ComedyOS v1.1 — Comedian Onboarding, Wayfinding, Lexicon Highlighter & QA Execution Plan (`FLASH_ONBOARDING_AND_UX_UPGRADE_PLAN.md`)

> **Target Executor:** Gemini 3.8 Flash (or Autonomous Implementation Agent)
> **Architect:** Gemini 4 Argon
> **Companion Specifications:**
> - [`design-system/DESIGN.md`](file:///e:/-%20CODE/ComedyOS-2026/design-system/DESIGN.md) (Constitutional Tokens & Rules)
> - [`design-system/DESIGNER_TASTE.md`](file:///e:/-%20CODE/ComedyOS-2026/design-system/DESIGNER_TASTE.md) (Granola, `beui.dev`, Variant `e4b3ad22`, Little Might & Linear Taste Rules)
> - [`design-system/LINEAR_UX_FOR_COMEDYOS.md`](file:///e:/-%20CODE/ComedyOS-2026/design-system/LINEAR_UX_FOR_COMEDYOS.md) (Keyboard Chords, `Cmd+K`, Breadcrumbs & Optimistic Sync)
> - [`design-system/COMEDIAN_PERSONA_UX_MATRIX.md`](file:///e:/-%20CODE/ComedyOS-2026/design-system/COMEDIAN_PERSONA_UX_MATRIX.md) (ADHD 10-Min Hyperfocus, Cringe-Blockade Visual Set Mirror, LPM Telemetry)

---

## 1. Architectural Diagnosis: What Breaks in `joke-writer.html` Today

### A. Visual & Wayfinding Bugs
1. **Lost in Space ("Where am I?"):** The current header only shows `B-104 · V1.0`, `Journal (0)`, and `Supabase Sync`. There is no global navigation bar or active location indicator telling the user whether they are in the **Workbench**, **Journal Vault**, **Set Builder**, or **Settings**, nor how to switch between them.
2. **Oversized Cloud Sync / Auth Drawer Inside the Editor:** Unauthenticated users are dropped directly into the writing screen with a large `Supabase Sync` config drawer exposing raw API URL/Key inputs. Auth and tester onboarding must happen **before** entering the workbench, and once inside the app, sync status must be a tiny, unobtrusive top-right pill (`● Synced · @stage_name`).
3. **Invisible / Ambiguous Interactive Triggers:** While `.btn` exists, several headers and mode toggles lack clear active states or tactile button affordances.

### B. User Flow & Functional Bugs
1. **Orphan `joke_blocks` on Block Deletion:** When a user deletes a block (`removeBlock(idx)`) and saves, `syncEntryToSupabase()` only runs `.upsert(blocksPayload)` for remaining blocks—it never deletes removed block IDs from `public.joke_blocks` in Supabase. Consequently, deleted blocks reappear on page reload!
   - **Fix:** Before upserting `blocksPayload`, run `await supabaseClient.from('joke_blocks').delete().eq('journal_entry_id', entry.id)` (or delete any IDs not in the active array).
2. **Non-Deterministic `blk_` IDs Replaced on Every Save:** `currentJoke.blocks` initializes with `id: 'blk_' + Math.random()...` (10 chars), and `syncEntryToSupabase` checks `(b.id && b.id.length === 36) ? b.id : generateUUID()`, generating a brand-new UUID on *every single keystroke sync* instead of persisting the UUID back to `b.id`! This floods `public.joke_blocks` with duplicate rows on every 300ms debounce!
   - **Fix:** Always use `generateUUID()` (36-char RFC 4122 UUID) when creating any block in memory, and write `b.id = validUuid` back to the in-memory block before upserting.
3. **Mobile vs. Desktop View Confusion:** On desktop, clicking `📱 Mobile Keep View` hides the desktop workbench and shows a narrow column without explaining that it is a mobile simulator, and there is no **Set Builder (Single-Joke Cards)** view.

### C. Security Audit Findings (Must Fix Before Comedian Onboarding)
1. **DOM XSS in `renderJournalLedger()`, `renderSequentialCircuit()`, `renderMobileKeepFeed()`, and `pinComparison()`:**
   - User-entered `title`, `raw_text`, and `block.content` are interpolated directly into `.innerHTML` templates (`<span class="serif">${titleSnippet}</span>` and `<textarea>${block.content}</textarea>`). If a user pastes text containing `</textarea><img src=x onerror=...>` or `<script>`, it executes arbitrary JS in their session.
   - **Fix:** Create a strict `escapeHtml(str)` helper and sanitize all interpolated strings, or assign `.textContent` / `.value` via DOM properties after creating elements.
2. **Exposed API Configuration Drawer:**
   - Remove the `<details>API CONFIGURATION (wjaaplveswgfveolixqn)</details>` block from the user-facing UI. The public `anon` key is meant to be embedded in client JS Constants (`COMEDYOS_DEFAULT_SUPABASE_URL` / `KEY`), never editable in a form by testers.
3. **Missing `INSERT` RLS Policy on `public.profiles`:**
   - In `supabase-schema.sql`, `public.profiles` has `SELECT` and `UPDATE` policies, relying on the `handle_new_comedyos_user()` trigger for initial creation. However, if a client runs `.upsert()` on `public.profiles` during the Tester Onboarding step, PostgreSQL checks both `INSERT` and `UPDATE` RLS policies!
   - **Fix:** Add `create policy "Users can insert their own profile" on public.profiles for insert with check (auth.uid() = id);` plus tester credential columns (`stage_name`, `home_scene`, `years_performing`, `social_handle`, `writing_style`, `onboarding_completed`).

---

## 2. Database Migration for Comedian Tester Onboarding (`supabase-onboarding-migration.sql`)

Run this non-destructive SQL migration in the Supabase SQL Editor (`wjaaplveswgfveolixqn`):

```sql
-- Add Comedian Tester Onboarding fields to public.profiles
alter table public.profiles
  add column if not exists stage_name text default '',
  add column if not exists home_scene text default '',
  add column if not exists years_performing text default '',
  add column if not exists social_handle text default '',
  add column if not exists primary_workflow text default 'hybrid',
  add column if not exists onboarding_completed boolean not null default false;

-- Allow authenticated users to upsert their own profile during onboarding
drop policy if exists "Users can insert their own profile" on public.profiles;
create policy "Users can insert their own profile"
  on public.profiles for insert
  with check (auth.uid() = id);
```

---

## 3. Step-by-Step UI & Architecture Upgrade Specification for Gemini Flash

### Phase 1: Pre-App Auth & Comedian Tester Onboarding Gate (`#onboardingGateView`)
Instead of showing the workbench to logged-out users or burying login inside a sync drawer, `joke-writer.html` must implement a **2-Step Pre-App Onboarding Gate** that covers the viewport until the comedian is signed in (or explicitly clicks `[Continue in Local Guest Mode]`):

1. **Hero & Tagline Architecture (Drawing from Keep Notes + Little Might / Variant Taste):**
   - **Eyebrow:** `COMEDYOS · EARLY TESTER COHORT V1.0`
   - **Headline (`Crimson Pro`, `48px`, `#F5F2ED`):**
     *"Stop guessing what works. Make bombing productive."*
   - **Sub-tagline (`Crimson Pro` italic, `20px`, `#A19F9A`):**
     *"The typographic workbench and stage telemetry system for stand-up comedians. See with your eyes which lines hit—without cringing at your own voice."*
2. **Step 1 — Instant Authentication:**
   - Primary CTA: `[Continue with Google]` (`.btn-primary`, large tactile button)
   - Secondary CTA: Email Magic Link input + `[Send Login Link]`
   - Tertiary Bypass for quick preview: `[Try Local Guest Sandbox →]`
3. **Step 2 — Comedian Credentials Card (Shown once authenticated if `!profile.onboarding_completed`):**
   - Collects 4 fast fields so we can follow up with testers and calibrate their workspace:
     1. **Stage Name / Handle** (`stage_name`, e.g., *"Viktor Enns"*)
     2. **Home Scene / City** (`home_scene`, e.g., *"Austin, TX / Berlin / NYC"*)
     3. **Years on Stage** (`years_performing`: `Open Mic (<2 yrs)` · `Club Regular (2–5 yrs)` · `Touring Pro (5+ yrs)`)
     4. **Instagram / X / Contact Handle** (`social_handle`, for tester follow-up)
     5. **Stage Workflow** (`primary_workflow`: `Write First, Perform Notes` vs. `Riff Onstage, Edit Recording`)
   - Saves directly to `public.profiles` and transitions smoothly into the Workbench.

---

### Phase 2: Persistent Top Wayfinding Header & Breadcrumb (`#globalWayfindingHeader`)
Replace the ambiguous `.context-strip` with a crystal-clear **Variant `8a6a23bf` + Linear Wayfinding Header**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ COMEDYOS   [01 Workbench]  [02 Journal (14)]  [03 Set Cards]  [04 Archive]   /  B-104 · Undisputed Champion  │
│                                                       [⚡ 10m Sprint]  [⌘K]  [● @viktor · Synced]  [+ New]   │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

- **4 Explicit Top-Level Destinations (Keyboard `1`, `2`, `3`, `4` when outside inputs):**
  1. **`01 Workbench`**: The Two-Stage Brain Dump + Sequential Joke Circuit + Granola Metadata Pills + `beui.dev` Lexicon Highlighter.
  2. **`02 Journal Vault`**: Full-width or split-view filterable ledger of all jokes with status badges (`SEED`, `STRUCTURED`, `STAGE READY`), LPM metrics, and 1-click Side-by-Side Diff Compare.
  3. **`03 Set Cards (Mobile & Stage Builder)`**: The Variant `e4b3ad22`-inspired Single-Joke Card grid & tonight's Set List builder with total runtime & LPM calculator, plus Mobile Capture dock.
  4. **`04 Craft Archive`**: Verbatim comedy masterclass axioms (Seinfeld, Louis CK, Jimmy Carr, Mark Normand principles from the vault) for instant writer's block relief.
- **Compact Account & Cloud Status Pill (`#accountSyncPill`):**
  - Replaces the old giant `Supabase Sync` button.
  - Displays a `6px` status dot (`#9FAF9A` when synced, `#FDBA74` when saving, `#5C5A55` when local guest) + `@stage_name`. Clicking it opens a clean, compact popover with `Sync Now`, `Edit Tester Profile`, and `Sign Out`.

---

### Phase 3: Granola Metadata Bar + `beui.dev` Lexicon Highlighter + LPM Telemetry
Inside the **Workbench (`01 Workbench`)**, upgrade the Right Sequential Circuit header to include:

1. **Granola-Style Document Title & Pill Strip:**
   - Editable Serif Joke Title (`Undisputed Champion`, `28px` `Crimson Pro`)
   - Directly below: Pill strip with:
     - Status Selector Pill: `[◐ Structured ▾]` (`Seed` / `Structured` / `Stage Ready` / `Retired`)
     - Live Stage Runtime & LPM Pill: `[⏱ 00:42 · 🎯 7.8 LPM]` (calculated from active punchlines + tags divided by estimated speaking duration + `[p: Xs]` pauses)
     - Cringe-Free Laugh Tagging: `[🔥 Mark Laugh Hit]` / `[❄️ Mark Dead Air]`
2. **`beui.dev` Inline Lexicon & Cadence Filter Bar:**
   - A row of tactile filter pills above the circuit:
     - `[Lexicon: Off]`
     - `[🔁 Repetition (2)]` (Sky blue `.word-hl-repeat` on words repeated `>=2` times across setup/punch)
     - `[🧱 Heavy >3 Syl (4)]` (Warm amber `.word-hl-heavy` on words with `>=3` syllables so the comic can substitute shorter words)
     - `[✂ Filler Fluff (1)]` (Coral `.word-hl-filler` on weak modifiers like *just, really, basically, actually, very, like*)
     - `[⚡ Punch Trigger]` (Sage mint `.word-hl-punch` on the final word of every active punchline to verify the laugh word is at the very end of the sentence).
   - When any filter pill is active, a synchronized **Lexicon Inspection Overlay / Lens** renders the blocks with `beui.dev`'s exact `2px`-radius tinted word boxes, allowing clicking any highlighted word to edit or trim it immediately.
3. **10-Minute ADHD Hyperfocus Sprint Timer (`[⚡ 10:00 Sprint]`):**
   - Clicking `[⚡ 10m Sprint]` in the top header starts a non-intrusive 10-minute countdown timer and suppresses non-essential chrome ("Ghost Writing Mode"), helping comedians beat procrastination in a single focused burst.
