# Comedian Persona UX Synthesis & Feature Matrix (`COMEDIAN_PERSONA_UX_MATRIX.md`)

> **Source Research:** [`Comedian Persona - Wer sie sind.md`](file:///g:/OneDrive/-%20DEV/comedy%20os/comedy%20os%20obsidian%20vault/UX/User%20Research/Comedian%20Persona%20-%20Wer%20sie%20sind.md) (Granola Research Synthesis)
> **Purpose:** Translates the psychological traits, stage pain points, and working habits of stand-up comedians into concrete UX rules and features for ComedyOS.

---

## 1. Psychological & Workflow Profile -> UX Rules

| Comedian Reality (From Research) | Why Standard Note Apps Fail Them | ComedyOS UX & Architectural Solution |
| :--- | :--- | :--- |
| **1. Chaotic Work Mode: "10 Minutes of Hyperfocus, Then Burned Out for Days"** (High ADHD prevalence) | Notion/Obsidian require folder hygiene, properties, and setup before writing. By the time a comic organizes a page, the 10-minute dopamine window is gone. | **Zero-Setup Instant Capture + "10-Minute Hyperfocus Sprint" Mode:** Opening ComedyOS drops the comic straight into an active canvas or 1-item-at-a-time **Seed Triage**. Optional 10-minute countdown pill (`[⚡ 10:00 Sprint]`) gamifies punching up 3 bits before burnout hits. |
| **2. Authority Resistance & Outsider Mentality** ("Fit nowhere, hate being told what to do") | Rigid form wizards or preachy AI ("Here is a funnier joke for you!") trigger immediate rejection. | **Instrument, Not Ghostwriter:** ComedyOS never writes "AI slop jokes" for the comic. Instead, it acts like a **telemetry & linguistic mirror**—counting syllables, highlighting repeated words (`beui.dev` style), and letting the comic promote their own words (`Alt+S`, `Alt+P`). |
| **3. The "Cringe-Blockade"** (Many record their sets, but **never listen back** because hearing their own voice/bombing makes them cringe—leading to stagnation and quitting) | Standard voice memo apps force comics to scrub through 15 minutes of raw audio of their own voice to find 2 minutes of working material. | **Visual Set Mirror (Zero-Audio Review):** Transcribe and plot the set as a **Visual Laugh & Rhythm Waveform** with automatic **[🔥 92% Duchenne Laugh]** and **[❄️ Dead Air]** markers on the text blocks. Comics can **read** where the laughs hit and where they bombed *without ever having to hear their own voice*, jumping straight to the 2-minute highlight clip for social media. |
| **4. Word Economy Obsession** ("Advanced comics count syllables, substitute words, and trim to the absolute minimum") | Google Docs and Apple Notes treat a joke like an essay—giving zero feedback on syllable drag, filler words, or punch-word placement. | **`beui.dev` Inline Lexicon & Cadence Highlighter:** Toggleable inline word highlights right inside the joke blocks: **Amber** for heavy multi-syllable words (`>3 syl`), **Coral** for filler fluff (*"like", "basically", "just"*), **Sky Blue** for repeated/callback words, and **Sage Mint** for the final laugh-trigger word. |
| **5. Laughs Per Minute (LPM) & Pause Mechanics** (Goal: `6–10 LPM`; strategic pauses trigger double laughs) | Comics have no way to see if their written bit has enough punch density to hit `6–10 LPM` before walking onstage. | **Live LPM & Tempo Estimator:** ComedyOS calculates estimated stage runtime from word count + `[p: 1.5s]` pause tags (at the comic's baseline WPM, default `130 WPM`) and computes **Projected LPM** (`Active Punchlines + Tags ÷ Minutes`). Color-coded badge turns sage green when the bit enters the `6.0–10.0 LPM` zone. |
| **6. The "Steve Martin Principle" & Fear of Bombing** (Obsession over a single non-laugher; bombing is the #1 fear) | Bombing feels like a personal rejection rather than actionable data. | **Reframe Bombing as Data ("Variant Testing"):** When a punchline misses onstage, the comic doesn't delete the joke—they click `[+ Alt Punch]` to test Variant B at the next mic ( comedians doing 5–6 sets/night). |
| **7. Two Distinct Stage Workflows:**<br>*(A) Write first -> bring notes onstage -> observe*<br>*(B) Rough idea -> improvise onstage -> record -> edit after* | Most apps only support Workflow A (typing) or Workflow B (voice recorder), never bridging the two. | **Unified Bi-Directional Pipeline:** Workflow A uses the **Sequential Circuit** + **Stage Set Card View**; Workflow B uses **Mobile Voice/Set Ingestion** → **Brain Dump Transcript** → `Alt+S / Alt+P` promotion into structured blocks. |

---

## 2. Feature Gap Audit: What Already Exists vs. What Is Missing

### ✅ What Is Already Built in `joke-writer.html` (v1.0-test)
1. **Two-Stage Desktop Workbench:** Unconstrained Left Brain Dump (`01. BRAIN DUMP / RAW INPUT`) + Right Sequential Joke Circuit (`02. SEQUENTIAL JOKE CIRCUIT`: Setup → Variable Bridges → Punchlines → Tags).
2. **Keyboard & Selection Promotion:** `Alt+S` (Setup), `Alt+B` (Bridge), `Alt+P` (Punchline), `Alt+T` (Tag), `Cmd+Enter` (Split at cursor), plus floating selection popover.
3. **8 Bridge Subtypes:** Misdirect, Exaggeration, The Bend, Repetition, Reimagine, Reenact, List, Exploration.
4. **Punchline Variants & Pause Cues:** `+ Alt Punch` with `Stage Active` toggle and `[p: 1.5s]` pause tag insertion.
5. **Word & Syllable Telemetry:** Real-time word and syllable counter per block and for the full circuit.
6. **Mobile "Google Keep for Jokes" View:** Quick text capture, Web Speech API live voice memo, and camera/notebook scan preview.
7. **Obsidian/Antigravity Split Journal Drawer & Side-by-Side Comparison:** Compare two versions of a joke and pull lines across.
8. **Multi-Tenant Supabase Cloud Sync (`wjaaplveswgfveolixqn`):** Google OAuth, Magic Link, RLS-protected `profiles`, `journal_entries`, and `joke_blocks`.

### 🚀 What Is Missing (And Must Be Added for Comedian Testing)
1. **Pre-App Onboarding & Tester Credential Gate:**
   - Currently, unauthenticated users land directly inside the workbench with a confusing `Supabase Sync` drawer.
   - **Fix:** Show a dedicated, high-craft **ComedyOS Tester Onboarding Screen** *before* the workbench that handles login + captures **Comedian Credentials** (`Stage Name`, `Home Scene / City` [e.g., Austin, NYC, Berlin], `Years Performing`, `Instagram/TikTok Handle`, and `Primary Workflow: Write-First vs. Riff-Onstage`).
2. **Clear Wayfinding & Top Navigation Header (Fixing "Where Am I?"):**
   - Currently, there is no navigation bar showing where the user is or how to switch between **Workbench**, **Journal Vault**, **Set Builder (Mobile Cards)**, and **Settings/Profile**.
   - **Fix:** Implement the **Variant `8a6a23bf` + Linear Wayfinding Header** with explicit view tabs, active joke breadcrumb (`COMEDYOS / WORKBENCH / B-104`), and a tiny top-right account/sync pill (`● Synced · @stage_name`).
3. **`beui.dev` Inline Linguistic Word Highlighter (Lexicon Harness):**
   - Add the 1-click filter pills (`[All]`, `[Repetition]`, `[Heavy >3 Syl]`, `[Filler Fluff]`) that highlight target words inline using `beui.dev`'s sharp tinted spans so comedians can trim fat in seconds.
4. **Live LPM (Laughs Per Minute) & Stage Runtime Badge:**
   - Upgrade the circuit telemetry from `0 WORDS · 0 SYL` to `01:12 EST · 8.3 LPM (TARGET 6-10) · 142W · 198S`.
5. **Cringe-Free "Set Tape Mirror" & Duchenne Laugh Marker:**
   - Allow comics to tag blocks or transcript segments with `[🔥 Laugh Hit]` / `[❄️ Rewrite]` and filter for **2-Minute Social Clip Candidates** without listening to raw audio.
6. **Variant `e4b3ad22` Single-Joke Mobile Cards & Set Builder View:**
   - Add a dedicated **Set Builder / Stage Cards View** where single jokes are rendered as gorgeous, scannable cards with clear visual hierarchy, estimated runtime, LPM badge, and drag/reorder controls for tonight's 5-minute or 15-minute spot.
