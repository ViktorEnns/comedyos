# COMEDY OS: System Architecture & Rules (The Main Context & Anti-Patterns)

## 1. Project Context

* **Mission:** A zero-friction performance intelligence platform for stand-up comedians.
* **Core Stack:** Flutter (Android Mobile MVP), Firebase (Auth, Firestore, Storage), Google Cloud Functions (Node.js), Vertex AI (Gemini 1.5 Flash).
* **Key Paradigms:**
  * **Offline-First:** Users must be able to capture ideas without cellular signal.
  * **Invisible Librarian:** We do NOT force users to use folders. We rely on Semantic Vector Search for retrieval.
  * **Progressive Disclosure:** Legacy #tags are supported, but semantic search is encouraged.

## 2. The "Do Not Do" List (Lessons Learned)

*Agents: Read this before writing code to avoid repeating historical mistakes.*

* **DO NOT** use standard HTML text fields for the mobile app. We are strictly using Flutter native text widgets.
* **DO NOT** try to build complex multi-agent orchestration for the Cloud Functions yet. Keep the Gemini API calls contained in simple, single-purpose functions.
* **DO NOT** overwrite the `manual_tag_count` when saving a note. It must be incremented (`+1`), not reset.
* *(Add future mistakes here as you find them)*

## 3. Code Quality & Evaluation Protocol

*Before submitting any code or marking a task as done, you must self-evaluate against these rules:*

1. **Linter Check:** Run `flutter analyze`. Zero warnings allowed.
2. **No Orphaned Code:** Ensure there are no unused variables, dead imports, or commented-out blocks of old logic.
3. **UI Consistency:** Ensure all text aligns with the "Digital Legal Pad" vertical rhythm (base unit: 32px).
4. **Error Handling:** Every network request must have a `try/catch` block with a user-friendly fallback UI.

## 4. User Experience Guidelines

* **Guideline 1 (Affordances & Hints):** Give the user clear visual affordances to understand and use features quickly and effectively. Keyboard shortcuts (on desktop) and other productivity helpers need unobtrusive inline hints until the user explicitly turns them off in the settings menu.
* **Guideline 2 (Zero Scrollbars & Elegant Overflow):** Avoid using scrollbars if possible. Find other elegant ways to display overflowing content (e.g., natural flex/grid container expansion, smooth hidden scroll with gradient fade masks, pagination, or progressive disclosure).
* **Guideline 3 (Pursuit of Elegant Solutions):** In general, always seek the most elegant solution to a layout problem. If the definition of an elegant solution is ever unclear for a specific interface challenge, search online for established modern UI patterns (e.g., Linear, Stripe, Raycast, Vercel), analyze how world-class interfaces handle it, and present clear ideas and options to the user.
* **Guideline 4 (Contrast, Spacing & Minimal Borders):** Try solving layout issues with contrast, spacing, and grouping first before relying on borders. Try to minimize borders throughout the application; avoid "border-soup" where every container is framed in a 1px stroke. Use space more effectively through intentional background shifts, generous white space, typographic hierarchy, and soft elevation.
