---
name: compact
description: Flushes current session state, file modifications, and next steps into .agents/handover.md for zero-token context reset.
---
# Context Compaction & Handover Protocol

Execute a hard state flush to prepare for a clean session reset:

1. **Overwrite `.agents/handover.md`** with a strict, token-lean summary (MAXIMUM 25 lines total).
2. **Enforce this exact structure inside `.agents/handover.md`:**
   - `## Active Objective`: 1–2 sentences on the feature or bug currently in flight.
   - `## Completed Changes`: Bullet list of exact files modified and architectural decisions locked in during this session.
   - `## Unresolved / Broken`: Any failing tests, uncommitted diffs, or active blockers (write `None` if clean).
   - `## Immediate Next Step`: The exact, deterministic instruction for the next agent to execute first.
3. **Strict Constraints:**
   - Omit all conversational history, polite filler, and code dumps.
   - Reference relevant rule files, design systems, or governance files if applicable.
4. **Final Output to User:**
   - Reply ONLY with: `✓ State flushed to .agents/handover.md. Run /clear (or Ctrl+Shift+L) and type /continue.`
