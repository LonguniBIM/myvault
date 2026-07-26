---
type: entity
title: "DESIGN.md (brand system file)"
tags: [design, brand, cowork, setup]
related: "[[claude-design]], [[claude-cowork]], [[brand-deck-rules]]"
created: 2026-05-10
updated: 2026-05-10
---

# DESIGN.md (brand system file)

**DESIGN.md** is the central brand system file that defines the visual and component rules for Claude-generated outputs. It acts as the "source of truth" for design consistency in autonomous workflows.

## Role in Pipeline

It is the middle link in the **Claude Design Pipeline**:
[[claude-cowork]] → **DESIGN.md** → [[claude-design]]

## Core Content

A typical `DESIGN.md` includes:
- **Brand Colors**: HEX codes for primary, secondary, and accent colors.
- **Typography**: Font family choices and scaling rules.
- **Components**: Rules for buttons, cards, and navigation elements.
- **Spacing**: Grid and margin standards.

## Deployment

- Usually stored in the `.obsidian/` or `ABOUT ME/` folder of a Cowork project.
- Referenced by Claude to ensure all UI elements generated match the project's brand identity.

> [!tip] Integration
> Can be linked to [[brand-deck-rules]] for consistent PowerPoint and slide generation using the [[research-brief-generate]] method.
