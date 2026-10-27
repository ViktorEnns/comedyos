---
id: POST-MVP-IDEAS-001
title: Post-MVP Feature Concepts & Future Roadmap
tags: [roadmap, post-mvp, feature-backlog, ideation, contests, elo, rehearsals]
status: backlog
---

# 🚀 Post-MVP Feature Concepts & Future Roadmap

> **Status:** Filed for Post-MVP. The immediate milestone is validating the core MVP (Audio Ingestion, Visual Diff Report, Atomic Bit Database, and State Machine) with active touring and open-mic comics. These concepts are preserved and architected here for future product cycles.

---

## 1. 🃏 Flash-Card Style Set Learning & Rehearsal Engine
* **Target Need:** Stand-up comics preparing for a Netflix/special taping, late-night set, or tour showcase who need to memorize their act down to the exact syllable and transition without relying on notes.
* **The Concept:** A spaced-repetition rehearsal mode (inspired by Duolingo / Anki) adapted for spoken comedic performance.
* **Key Mechanics:**
  - **Prompt & Reveal Mode:** The screen prompts the setup premise (*"Airport TSA..."*). The comic speaks the punchline and tags aloud.
  - **Rehearsal Performance Timer:** Measures delivery speed and beat pauses, comparing run times against target time allotments (e.g. 5:00 red-light cap).
  - **Multi-Run Delta Graph:** Compares audio from Run 1, Run 2, and Run 3 against the source script. Highlights deviations, dropped setups, and spontaneous phrasing improvements.
  - **Promotion Prompt:** If an unwritten line flows better during rehearsal, the system prompts: *"Promote this new phrasing to script canon? [Yes / Revert]"*.

---

## 2. 🔀 Smart Word Substitution & Vernacular Tuning Engine
* **Target Need:** Eliminating syllable bloat and replacing weak, flat words with sharper, punchier alternatives.
* **Key Mechanics:**
  - **Vernacular Harmonization:** Flags words that sound overly academic, archaic, or unnatural for the comic's authentic stage persona.
  - **Crowd Reaction Weighting:** Suggests punchlines and nouns that empirically generated higher laugh decibels in similar setups across past sets.
  - **Syllable Economy Filter:** Automatically flags multisyllabic words and suggests punchy, monosyllabic alternatives (e.g., replacing *"automobile accident"* with *"wreck"*).
  - **Anti-Overuse Shield:** Detects habitual filler words (`"like"`, `"you know"`, `"basically"`, `"so anyway"`) and highlights them for trimming.

---

## 3. 🧼 Clean-Set / Corporate Profanity Filter Lens
* **Target Need:** Working comics adapting raw club material for corporate gigs, television appearances, cruise ships, or clean club showcases.
* **Key Mechanics:**
  - **Single-Tap "Clean Lens":** Highlights all profanity, crude anatomical references, or sensitive keywords in soft rose.
  - **Context-Aware Clean Replacements:** Offers non-cheesy, punchline-preserving clean substitutions.
  - **Clean Set Export:** Generates an alternate clean version of the setlist without altering the raw club original in the Bit Database.

---

## 4. ✍️ Athletic Writing Streak & Creative Wellness Engine
* **Target Distortion:** Destructive Belief #1 (*"If I heal my trauma or get happy, I won't be funny anymore"* / *The Tortured Artist Fallacy*).
* **The Concept:** Stand-up writing framed not as spontaneous tortured chaos, but as an athletic discipline of deliberate daily micro-reps (inspired by Jerry Seinfeld's calendar chain).
* **Key Mechanics:**
  - **Micro-Rep Logging:** A comic registers a streak if they log at least **1 new premise**, **3 alternate punchlines/tags**, or **edit 1 existing bit**.
  - **Guilt-Free Grace Cycles:** Implements "Show Day / Recovery Day" shields—taking a night off after a 4-show weekend preserves your streak.
  - **Composure Analytics:** Correlates sets where the comic felt calm/prepared vs. manic/exhausted, empirically demonstrating that emotional stability yields tighter timing.

---

## 5. 🤝 Peer Punch-Up Exchange & Cryptographic Anti-Theft Ledger
* **Target Beliefs:** Productive Belief #7 (*"Asking peers for punch-ups improves craft"*) & Destructive Belief #10 (*"Asking for feedback makes you weak / Stealing jokes is fine"*).
* **Key Mechanics:**
  - **Cryptographic Provenance Hash:** Generates an immutable timestamped SHA-256 hash when a premise is logged in the Bit Vault, providing objective mathematical proof of prior creation.
  - **Green Room Punch-Up Link:** Ephemeral link for 2–3 trusted peers (*"Help me punch up this wedding bit"*).
  - **Co-Writer Split & Attribution:** Automatically attributes accepted tags in the metadata: *Tag 2 written by @Dave (Green Room Session, 12.11.2026)*.

---

## 6. 🥊 Roast with Friends (Separated Game Engine)
* **Status:** Fully specified in its own standalone section:
* **Master Architecture:** [[Roast_With_Friends/00_Roast_With_Friends_Master|Roast with Friends Master Architecture]]
* **Game Modes:** [[Roast_With_Friends/01_Game_Modes_and_Battles|01: Game Modes & Battle Formats]]
* **Acoustic Referee:** [[Roast_With_Friends/02_Acoustic_Referee_and_Scoring|02: Acoustic Referee & Scoring]]
* **ELO Ladder:** [[Roast_With_Friends/03_ELO_and_Social_Ladder|03: ELO Rating & Matchmaking]]
* **Safety Boundaries:** [[Roast_With_Friends/04_Safety_and_Consent_Borders|04: Safety & Consent Matrix]]
