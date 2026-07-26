---
type: entity
title: Claude Skills
tags: [skills, ecosystem, claude-code, workflow]
related: "[[skill-creator]], [[makemyskill]], [[skill-md-file]], [[claude-code]]"
created: 2026-05-09
updated: 2026-05-09
---

# Claude Skills

Claude Skills is the extensible skill system for Claude Code, enabling custom workflows and automations beyond built-in capabilities.

## Core Components

- **[[skill-creator]]** — Anthropic's official tool for creating new skills
- **[[makemyskill]]** — Community platform (makemyskill.com) for skill discovery and sharing
- **[[skill-md-file]]** — SKILL.md open standard for skill documentation and metadata

## Ecosystem

Skills creation follows a structured pipeline:
1. Identify a repeatable workflow or pattern
2. Document as numbered steps in SKILL.md format
3. Register with Skill Creator for Claude Code integration
4. Share via makemyskill community platform

## Connection to Other Systems

- **[[claude-code]]** — Skills are invoked via `/skill-name` in Claude Code
- **[[cowork-projects]]** — Skills can be triggered from Cowork autonomous workflows
- **[[voice-profile]]** — Skills can be customized per user via about-me.md context

## Related Concepts

- [[skill-design-pattern]] — How to structure effective skills
- [[negative-triggers-principle]] — Avoid skill names that conflict with common commands
- [[plugins-skill-bundles]] — Grouping related skills into bundles

> [!info] God Node
> Claude Skills is one of the 10 most-connected nodes in the knowledge graph (8 edges), indicating it's a core abstraction in the Claude ecosystem.
