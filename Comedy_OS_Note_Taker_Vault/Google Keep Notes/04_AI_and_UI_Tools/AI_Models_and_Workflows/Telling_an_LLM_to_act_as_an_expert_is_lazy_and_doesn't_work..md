---
title: "Telling an LLM to \"act as an expert\" is lazy and doesn't work."
created: "2026-01-29 15:37:58"
updated: "2026-01-29 15:37:58"
category: "04_AI_and_UI_Tools"
subcategory: "AI_Models_and_Workflows"
source: "Google Keep Takeout"
original_files: ["Telling an LLM to _act as an expert_ is lazy and d.json"]
tags: ["#ai_and_ui_tools", "#google-keep-takeout"]
related_vault_notes: ["[[31_Visual_Diff_Report]]"]
---

# Telling an LLM to "act as an expert" is lazy and doesn't work.

> [!INFO] Cross-Vault Architecture Connections
> **Related System Modules:** [[31_Visual_Diff_Report]]

Here's the complete persona template I use:

"You are a [specific role + seniority] with [X years] experience in [industry/domain].

You specialize in [specific expertise].

Your approach: [methodologies/frameworks you use]

Your constraints: [budget/time/resources]

Deliver: [specific output format]"

Copy this. Customize it. Watch quality jump.

Add this line: "If you lack enough information to give a complete answer, ask clarifying questions before proceeding."

- Senior DevOps Engineer (AWS/Kubernetes focus)
- B2B SaaS Growth PM (PLG motion)
- Technical SEO Specialist (SaaS niche)
- Data Engineer (Python/dbt stack)

......


The framework that took me from 60% to 94% output quality:

Every persona needs 5 elements:

1. Specific role + seniority
2. Industry/domain context
3. Methodologies they use
4. Constraints they operate under
5. Output format they'd deliver

Let me break down each one:

1. SPECIFIC ROLE + SENIORITY

Bad: "Act as a developer"

Good: "Act as a Senior Backend Engineer with 8 years specializing in distributed systems"

Bad: "Act as a writer"

Good: "Act as a Technical Content Writer who translates complex SaaS features for non-technical buyers"

Seniority level changes decision-making patterns.

2. INDUSTRY/DOMAIN CONTEXT

Bad: "Act as a product manager"

Good: "Act as a B2B SaaS Product Manager in the fintech space, working with enterprise customers ($100K+ ACV)"

Context shapes priorities.

Consumer PM thinks viral growth.
Enterprise PM thinks compliance and security.

Different worlds. Different outputs.

3. METHODOLOGIES THEY USE

Bad: "Help me analyze this data"

Good: "You use JTBD framework for user research, run multivariate tests for validation, and present findings with statistical significance at 95% confidence"

Methodologies = thinking frameworks.

No framework = random analysis.
Clear framework = structured insights.


4. CONSTRAINTS THEY OPERATE UNDER

This is the game-changer nobody talks about.

Add: "You have a $50K budget, 6-week timeline, and a team of 3 junior developers. You prioritize shipping over perfection."

Constraints force realistic solutions.

Without constraints, LLMs give you fantasy answers that don't work in real life.


5. OUTPUT FORMAT EXPERTS USE

Bad: "Give me your analysis"

Good: "Deliver a 2-page executive brief with: situation assessment, 3 strategic options with pros/cons, and your recommended path with success metrics"

Experts don't just think differently.

They communicate in specific formats.

Format = professionalism signal.


---
*Imported from Google Keep Takeout · Created: 2026-01-29 15:37:58 · Last Modified: 2026-01-29 15:37:58*