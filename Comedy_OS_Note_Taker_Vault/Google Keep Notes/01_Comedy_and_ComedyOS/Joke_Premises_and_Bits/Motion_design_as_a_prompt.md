---
title: "Motion design as a prompt"
created: "2026-09-26 11:36:50"
updated: "2026-09-26 11:36:50"
category: "01_Comedy_and_ComedyOS"
subcategory: "Joke_Premises_and_Bits"
source: "Google Keep Takeout"
original_files: ["Motion design as a prompt.json"]
tags: ["#comedy_and_comedyos", "#google-keep-takeout"]
related_vault_notes: ["[[31_Visual_Diff_Report]]"]
---

# Motion design as a prompt

> [!INFO] Cross-Vault Architecture Connections
> **Related System Modules:** [[31_Visual_Diff_Report]]

Opus 5.5 is absolutely cracked at motion design

this entire video is code

0 After Effects
0 manual animation

I showed it one viral motion post and said:

“explain MakerMap, but make it insane”

it came back with 20 seconds of one shape morphing through the entire product:

sign up → your pin → 3,393 real makers lighting up the globe → matches → a meetup → search

the crazy part?

the entire animation is deterministic math

the springs, cursor, morphs and motion blur are all generated inside one HTML file

here’s the prompt structure

steal it ↓

<inputs> 
Ask me for: 
• my product + URL 
• 8–12 UI states that tell its story 
• the real data shown in each state 
• brand colors + fonts + accent color 
• required formats (1:1, 16:9, 9:16) 
</inputs>

<rules> 
One HTML file. One canvas
One draw(t) function

No CSS transitions
No timers
No state carried between frames

One shape, never cut

Every state is the same element changing size, radius and color while the content swaps

A cursor drives the sequence with real clicks, typing and one drag

Real UI. Real data. No placeholders.

</rules>
<structure> 
120 BPM grid

Something happens on every bea

logo → button → handle field → “is this you?” → loader → pin → globe filling with users → matches → tabs → RSVP → search → logo

</structure>

<motion> 
Closed-form springs everywhere with only a tiny overshoot.

If a value changes target multiple times, sum one spring per change

Content enters after its container starts morphing and leaves before the next morph so text never overlaps

Use a short blur on transitions

Never fade black directly into the accent color. Move an accent element between states instead

Make tab indicators stretch by putting each edge on a different spring

Zoom the camera so every state fills the frame

Make the last frame equal the first so the whole thing loops
</motion>

<export> 
First render one frame per beat as a contact sheet

Fix anything cramped or broken

Then render every frame in headless Chrome at 60fps, averaging 6 subframes for motion blur

Pipe into ffmpeg:
H.264 + yuv420p

Export all aspect ratios in parallel
</export>


---
*Imported from Google Keep Takeout · Created: 2026-09-26 11:36:50 · Last Modified: 2026-09-26 11:36:50*