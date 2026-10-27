---
name: continue
description: Hydrates a fresh session from .agents/handover.md and immediately resumes execution.
---
# Session Hydration Protocol

1. Read `.agents/handover.md` immediately.
2. Inspect the files listed under `## Completed Changes` (via `git status` or `git diff` if needed) to verify the workspace state.
3. State in 2 bullet points that you have loaded the handover context and are ready, then **immediately begin executing** the task defined under `## Immediate Next Step`.
