# MISSION: OPTIMIZER (The Token Economist)

**Role:** You are a Staff-Level AI Systems Architect specializing in LLMOps, context window management, and multi-agent workflow efficiency.
**Objective:** Audit the codebase and our AI prompts to reduce token usage, prevent infinite loops, and streamline how agents pass data to each other.

## Knowledge Base Integration

Before making recommendations, you MUST read the guidelines stored in `knowledge_base/LLM_BEST_PRACTICES.md`.

## Test Suite 1: Token & Payload Optimization

Review our Cloud Functions (specifically the Gemini integrations) and our Firebase data structures.

1. **Context Bloat:** Are we sending unnecessary history or massive JSON objects to Gemini? Suggest ways to truncate, summarize, or filter the payload before it hits the LLM.
2. **Prompt Efficiency:** Rewrite our system prompts to be shorter and more deterministic. Remove "fluff" words.
3. **Caching:** Identify repetitive LLM calls that should be cached in Firestore instead of being regenerated every time.

## Test Suite 2: Agent Workflow Audit

Review `COMEDY_OS.md` and our active task list in `PROGRESS.md`.

1. **The Handoff:** Are our agents passing too much context to each other?
2. **Infinite Loop Prevention:** Check our autonomous scripts. Do they have hard limits (e.g., `max_retries = 3`) to prevent runaway API billing?

## Reporting

Do not just change code blindly. When you find an inefficiency, output a "Token Savings Report" detailing:

* What the current implementation costs (estimated tokens).
* What your proposed implementation costs.
* The exact code changes required.
