# Agent Rules & Instructions

You MUST consult and follow these rules at all times across all tasks:

1. **Language & Translations Policy:**
   - **German (`de`) locale support is deactivated.** Work strictly on the English (`en`) version from now on.
   - **DO NOT translate to or from other languages unless specifically instructed.**
   - If there is existing content in the German language present in the repository, keep it as-is and do not translate or alter it unless explicitly instructed.
   - The primary language of documentation, product specs, and source text is **English**.

2. **Source Integrity:**
   - Preserve original formatting, sections, and technical terminology when importing external documents.

3. **Design & Layout Guidelines:**
   - **Avoid using scrollbars if possible.** Find other elegant ways to display overflowing content (e.g., natural flex/grid expansion, smooth hidden scroll with gradient fade masks, pagination, or progressive disclosure).
   - **Seek the most elegant solution to layout problems.** If the definition of an elegant solution is ever unclear for a specific interface problem, search online for established modern UI patterns (e.g. Linear, Stripe, Raycast), analyze real-world implementations, and present clear, structured ideas to the user.
   - **Solve layout issues with contrast, spacing, and grouping first before relying on borders.** Try to minimize borders across the entire interface (avoid "border-soup"). Use the space more effectively through intentional background surface shifts, generous whitespace, typographic weight hierarchy, and soft elevation instead of outlining every container with heavy borders.

---

## Visual Architecture & Boundary Enforcement
- **Before modifying multi-file flows:** Read `Comedy_OS_Note_Taker_Vault/Architecture/SYSTEM_MAP.md` or `docs-site/docs/architecture/SYSTEM_MAP.md` to understand existing data boundaries.
- **After structural changes:** Load `.agents/skills/architecture-mapper/SKILL.md` and run `npm run map` in `ComedyOS-app` to verify zero circular dependencies and keep Obsidian visual maps updated.

---

## Available Workflows & Skills
- **Architecture Mapper:** [`.agents/skills/architecture-mapper/SKILL.md`](file:///e:/-&#32;CODE/ComedyOS-2026/.agents/skills/architecture-mapper/SKILL.md) — Trigger after creating new modules, altering database schemas, changing state flows, or refactoring cross-file imports to update Obsidian/Docusaurus visual Mermaid maps.
- **Context Compaction:** [`.agents/skills/compact/SKILL.md`](file:///e:/-&#32;CODE/ComedyOS-2026/.agents/skills/compact/SKILL.md) — Trigger via `/compact` when completing a task or milestone to flush state to `.agents/handover.md`.
- **Session Continuation:** [`.agents/skills/continue/SKILL.md`](file:///e:/-&#32;CODE/ComedyOS-2026/.agents/skills/continue/SKILL.md) — Trigger via `/continue` to hydrate fresh context from `.agents/handover.md` and resume.
- **Skill Harvester:** [`.agents/skills/skill-harvester-agentsmd/SKILL.md`](file:///e:/-&#32;CODE/ComedyOS-2026/.agents/skills/skill-harvester-agentsmd/SKILL.md) — Trigger upon milestone completion to distill successful patterns into new skills.
- **Variant Faithful Design:** [`.agents/skills/variant-faithful-design/SKILL.md`](file:///e:/-&#32;CODE/ComedyOS-2026/.agents/skills/variant-faithful-design/SKILL.md) — Trigger when designing or styling UI to match the Variant typographic ledger aesthetic.
