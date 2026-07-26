---
name: rapid-on-brand-presentation-workflow
description: Create polished, on-brand slide decks in minutes by combining Claude's research with Gamma's automated design.
type: skill
trigger: "When you need a high-fidelity presentation for a client, board, or strategy session."
time_estimate: "20 minutes"
difficulty: "medium"
prerequisites:
  - Claude Pro/Max account
  - Gamma account (Free/Pro)
  - Gamma Connector enabled in Claude
tags:
  - presentation
  - slides
  - gamma
  - design
related:
  - "[[Slides]]"
created: 2026-05-10
updated: 2026-05-10
---

# Rapid On-Brand Presentation Workflow

## Why This Matters

Manual slide design is slow and often results in "flat" visuals. This workflow separates **intelligence** (Claude) from **interface** (Gamma) to produce greatness in 20 minutes.

## The Skill

Execute a 4-step research-to-generation pipeline for high-fidelity decks.

## Steps

### 1. Research (5-10 mins)

1. Open Claude Cowork.
2. Prompt: `"Research [topic] for [success criteria]. Use local files + 5 varied web searches (trends, data, 2025-2026 sources). Save results to research-brief.md."`
3. Identify gaps and fill them before proceeding.

### 2. Briefing (2 mins)

1. Follow up: `"Read research-brief.md and turn it into a Gamma-ready outline. Title, 2-3 key points, and specific stats per slide. Save to gamma-outline.md."`

### 3. Generation (1 min)

1. Follow up: `"Use the Gamma connector to generate this presentation using textMode 'generate'."`
2. Ensure you specify the correct **Brand Theme** if working in a team.

### 4. The Greatness Pass (10 mins)

1. Open the Gamma link.
2. **Resonance Test**: Would I say this out loud?
3. **Density Test**: Does every card earn its place?
4. **Verification**: Is the data accurate?

## Advanced Team Setup

1. **Extract Theme**: Import your company PPTX into Gamma (Library → Themes) to auto-extract colors/fonts.
2. **Brand Rules**: Create a `brand-deck-rules.md` in your Cowork folder containing visual identity, structure rules, and tone instructions.
3. **Daily Use**: Always start prompts with `"Read brand-deck-rules.md first."`

## Success Criteria

- [ ] Deck contains 2025-2026 data.
- [ ] Visuals are on-brand (colors/logo).
- [ ] Output is editable in Gamma.

## Source

**Article**: [[Slides]]  
**Author**: [[Ruben Hassid]]  
**Published**: 2026-03-08
