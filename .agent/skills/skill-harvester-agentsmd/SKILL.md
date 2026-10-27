---
name: skill-harvester
description: Analyzes successful implementation patterns and extracts them into reusable Antigravity skills and AGENTS.md links.
---
# Skill Harvester & AGENTS.md Updater

Analyze the exact patterns, libraries, state structures, and edge-case fixes that made an implementation work without breaking, and extract it into a reusable Antigravity skill.

## 1. Create the Skill File
Create `.agents/skills/[kebab-case-skill-name]/SKILL.md` using this exact structure:

```markdown
---
name: [kebab-case-skill-name]
description: [Max 200 chars: Exact trigger condition—when should an agent load this skill?]
---
# [Skill Title]

## Core Architecture & Pattern
- [3-5 concise bullets explaining the exact data flow / state mechanism that succeeded]

## Implementation Checklist
1. [Step-by-step procedural rules to execute this pattern]
2. [Required libraries, hooks, or token conventions]

## Guardrails (Do Not Break)
- NEVER [Specific trap we avoided or fixed during this task]
- ALWAYS [Mandatory verification check before finishing]
```

## 2. Link in AGENTS.md
Append a 1-line reference under the `## Available Workflows & Skills` section of `AGENTS.md` pointing to the new `SKILL.md` path and stating when to trigger it.
