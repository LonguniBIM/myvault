---
type: source
title: "Claude Skills"
tags: [extract, text]
related: []
created: 2026-05-10
updated: 2026-05-10
authors: []
year: 2026
url: ""
venue: ""
---

# Claude Skills

**Summary**: Content extracted from text file `Claude Skills.md`.

**Sources**: `Claude Skills.md`

**Last updated**: 2026-05-10

---

## Six-Question Analysis

### Q1 — What problem does this solve?

It solves the "re-explanation fatigue" and token waste. It allows users to capture repeatable processes as "Skills" (slash commands) that fire automatically when a task is recognized, rather than requiring the user to re-upload files or write long context-heavy prompts every time.

### Q2 — What numbered steps does the author prescribe?

**Building a Skill via Skill Creator:**
1. Open Claude Cowork (Opus 4.6 + Extended Thinking).
2. Prompt: "Use the skill-creator to help me build a skill for [task]."
3. Answer the "interview" questions specifically to capture the process.
4. Review the generated `SKILL.md` and the evaluation results.
5. Save the Skill folder and upload it via **Settings → Capabilities → Skills → Upload**.

**Optimization Hacks:**
1. **Debug**: Ask "When would you use the [skill-name] skill?" to verify Claude's understanding.
2. **Negative Triggers**: Add "Do NOT use for..." instructions to prevent hijacking.
3. **Voice Stacking**: Use an `about-me.md` file for tone and a Skill for the technical process.
4. **Reverse-Engineering**: Turn a successful Cowork chat session directly into a Skill via the session menu arrow.
5. **Prompt-Level Quality**: Add "Take your time. Quality over speed. Don't skip steps." to the user prompt to overcome AI "laziness".

### Q3 — What principles recur?

- **Skills as Processes**: Skills should capture *how* to do a job, while voice files capture *who* you are.
- **Automatic Invocation**: A well-described Skill invokes itself based on the request; you don't always need to type the slash command.
- **Token Efficiency**: Skills save money because Claude only reads the header until a match is found, reducing context window bloat.
- **Portability**: Skills are an open standard (`SKILL.md`) that will eventually work across multiple AI platforms.

### Q4 — What mistakes does the author warn against?

- Writing vague descriptions (causes the Skill to never fire).
- Writing too broad descriptions (causes the Skill to hijack unrelated conversations).
- Putting tone/voice rules inside the Skill (keep them separate in an `about-me.md` file).
- Skipping the "Evaluation" step during creation.

### Q5 — What diagnostic questions does the author pose?

- When would you use this skill? (The debugging question).
- Is this a process I repeat at least weekly? (The threshold for building a Skill).
- Does the Skill fire when it shouldn't? (Indicating a lack of negative triggers).

### Q6 — Can the method be expressed as numbered steps?

**YES** — Skill candidate: `build-and-deploy-claude-skills`.

## Content Preview

---
title: "Claude Skills."
source: "https://ruben.substack.com/p/claude-skills"
author:
  - "[[Ruben Hassid]]"
published: 2026-04-01
created: 2026-05-09
description: "How to set up Claude the right way (so you actually stop prompting)."
tags:
  - "clippings"
---
AI has different levels.

- **Level 1**: You’re using the free ChatGPT.
- **Level 2**: You’re using the paid ChatGPT + Thinking.

*(... full content in raw/extracts/)*

## Related pages

*(Cross-references to be added as concepts are identified)*
