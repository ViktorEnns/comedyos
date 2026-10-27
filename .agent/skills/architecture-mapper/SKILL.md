---
name: architecture-mapper
description: Trigger after creating new modules, altering database schemas, changing state flows, or refactoring cross-file imports to update Obsidian/Docusaurus visual Mermaid maps.
---
# Architecture & Dependency Mapper Skill

Whenever you add a new file, modify module imports, or alter data flow across components in Comedy OS, you MUST synchronize the visual documentation before completing the task.

## Step 1: Run the Automated Dependency & Boundary Audit
1. Execute `npm run map` inside `ComedyOS-app/` (or run `node scripts/update-map.mjs`).
2. Read the top of the synchronized maps:
   - Docusaurus: `docs-site/docs/architecture/DEPENDENCY_GRAPH.md`
   - Obsidian: `Comedy_OS_Note_Taker_Vault/Architecture/DEPENDENCY_GRAPH.md`
3. **CRITICAL GATE:** If `DEPENDENCY_GRAPH.md` reports an `ARCHITECTURAL VIOLATION` (such as a circular dependency or a UI component directly importing a low-level engine), you MUST refactor your code immediately to resolve the violation before returning control to the user.

## Step 2: Update the Semantic State & Data Flow Map
Inspect `SYSTEM_MAP.md` in `docs-site/docs/architecture/SYSTEM_MAP.md` and `Comedy_OS_Note_Taker_Vault/Architecture/SYSTEM_MAP.md` (create it if missing). Ensure it contains clean, human-readable Mermaid diagrams covering:
1. **High-Level Data Flow (`graph TD`):** Grouping nodes via `subgraph` into `UI Components`, `State & Hooks`, `Core Engines (Audio / OCR)`, and `Storage (SQLite / FileSystem)`.
2. **Active Feature State Machine (`stateDiagram-v2`):** If you built or modified an interactive UI component or async pipeline, document its exact state transitions (including error and offline fallback states).

## Formatting Rules for Obsidian & Docusaurus Compatibility
- Wrap all node labels containing parentheses, slashes, or spaces in double quotes: `A["Audio Engine (60fps ref)"]` instead of `A[Audio Engine (60fps ref)]`.
- Keep individual Mermaid diagrams under 25 nodes so they remain legible on a standard canvas. Split subsystem flows into separate `### Subsystem` headings if needed.
- Never delete existing valid subsystem diagrams when updating a single feature.
