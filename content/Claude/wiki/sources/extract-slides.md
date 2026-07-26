---
type: source
title: "Slides"
tags: [extract, text]
related: []
created: 2026-05-10
updated: 2026-05-10
authors: []
year: 2026
url: ""
venue: ""
---

# Slides

**Summary**: Content extracted from text file `Slides.md`.

**Sources**: `Slides.md`

**Last updated**: 2026-05-10

---

## Six-Question Analysis

### Q1 — What problem does this solve?

It solves the "presentation bottleneck"—the slow, manual process of researching, outlining, and designing slide decks. By using a combination of Claude (for thinking/research) and Gamma (for automated high-fidelity design), users can create polished, on-brand presentations in minutes rather than hours.

### Q2 — What numbered steps does the author prescribe?

**The "Research → Brief → Generate" Workflow (Favorite Method)**:
1. **Research (Claude Cowork)**:
   - Use a prompt to research a topic using local files + at least 5 varied web searches (trends, data, expert opinions).
   - Save findings to `research-brief.md`.
2. **Briefing (Claude Cowork)**:
   - Convert the research brief into a slide-by-slide outline.
   - Specify slide titles, 2-3 key points, and specific data/stats.
   - Save to `gamma-outline.md`.
3. **Generation (Claude + Gamma Connector)**:
   - Use the Gamma connector inside Claude to generate the deck using the outline with `textMode: "generate"`.
4. **Editing (Gamma)**:
   - Open the Gamma link and perform a "10-15 minute greatness pass": rewrite awkward phrases, cut weak cards, and verify data.

**Advanced Brand Workflow (For Teams)**:
1. **Gamma Theme**: Import an existing company PPTX/Google Slides into Gamma to auto-extract colors, fonts, and logos. Set as workspace default.
2. **Brand Rules File**: Use Claude Cowork to analyze all brand assets and generate a `brand-deck-rules.md` file (Visual identity, Structure, Tone, Recurring elements).
3. **Execution**: Start every prompt with "Read brand-deck-rules.md first."

### Q3 — What principles recur?

- **Claude Thinks, Gamma Designs**: Separate the "intelligence" (content) from the "interface" (design) for maximum quality.
- **Taste as the Filter**: AI provides the speed and the "average" draft; the user's value is in the final 10-15 minute edit to reach "greatness."
- **Context Isolation**: Research is more effective when it combines local sources with real-time web data (2025-2026 sources).
- **Automation of Consistency**: Use persistent markdown files to ensure every team member produces on-brand decks without manual oversight.

### Q4 — What mistakes does the author warn against?

- **Manual Slide Creation**: Don't waste time on layout in 2026.
- **Basic Claude PPTX**: Claude's native PPTX generation is often too visually "flat" for client-facing work (Method #1).
- **Vague Prompts in Gamma**: One-line prompts in Gamma result in pretty but empty slides (Method #2).
- **Ignoring the "Greatness Pass"**: Failing to spend 15 minutes editing the AI output results in "good" instead of "great."

### Q5 — What diagnostic questions does the author pose?

- Would I say this slide out loud? (The resonance test).
- Does this card earn its place? (The density test).
- Is the data right? (The verification test).
- Have I researched the right information before outlining? (The foundation test).

### Q6 — Can the method be expressed as numbered steps?

**YES** — Skill candidate: `rapid-on-brand-presentation-workflow`.

## Content Preview

---
title: "Slides."
source: "https://ruben.substack.com/p/powerpoint"
author:
  - "[[Ruben Hassid]]"
published: 2026-03-08
created: 2026-05-09
description: "How to use AI to make a (fantastic) PowerPoint in 2026:"
tags:
  - "clippings"
---
It’s 2026, so you better not make your slides manually. AI does it for you.

But how? I tested every method, and landed on 3 (the third one is my favorite).


*(... full content in raw/extracts/)*

## Related pages

*(Cross-references to be added as concepts are identified)*
