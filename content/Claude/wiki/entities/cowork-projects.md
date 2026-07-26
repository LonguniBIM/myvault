---
type: entity
title: Cowork Projects (scoped memory)
tags: [cowork, memory, projects, context]
related: "[[claude-cowork]], [[cowork-folder-structure]], [[about-me-md]], [[prompt-templates]]"
created: 2026-05-09
updated: 2026-05-09
---

# Cowork Projects (scoped memory)

Cowork Projects is a memory scoping system that allows Claude Cowork to maintain separate context per project, avoiding cross-contamination between unrelated work.

## Structure

Each project has its own folder containing:
- **ABOUT-ME/** — Project-specific context files
  - `about-me.md` — Project goals, stakeholders, constraints
  - `my-company.md` — Company/client-specific information
  - `anti-ai-writing-style.md` — Writing style preferences
- **OUTPUTS/** — Generated artifacts and deliverables
- **TEMPLATES/** — Reusable prompt templates for this project

## Benefits

- **Context isolation** — No token waste on irrelevant project history
- **Faster startup** — Only load context for current project
- **Better accuracy** — Claude doesn't confuse details between projects

## Integration

- **[[claude-cowork]]** — Automatically loads project context on startup
- **[[cowork-global-instructions]]** — Global rules apply across all projects
- **[[5-day-team-rollout-playbook]]** — How to set up projects for team adoption

## Related Patterns

- [[cowork-folder-structure]] — Standard directory layout
- [[prompt-templates-per-project]] — Project-specific prompt library

> [!info] God Node
> Cowork Projects is highly connected (5 edges), bridging Personal Context Files and Cowork Tooling communities.
