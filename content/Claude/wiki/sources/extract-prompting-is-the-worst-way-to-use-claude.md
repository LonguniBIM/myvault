---
type: source
title: "Prompting Is The Worst Way To Use Claude"
tags: [extract, text]
related: []
created: 2026-05-10
updated: 2026-05-10
authors: []
year: 2026
url: ""
venue: ""
---

# Prompting Is The Worst Way To Use Claude

**Summary**: Content extracted from text file `Prompting is the worst way to use Claude.md`.

**Sources**: `Prompting is the worst way to use Claude.md`

**Last updated**: 2026-05-10

---

## Six-Question Analysis

### Q1 — What problem does this solve?

It solves the "generic AI output" and "prompting fatigue" problem. Most people get average results because they don't provide enough context (tone, audience, rules) because typing long prompts is too much work. This guide introduces a system where persistent text files act as the prompt automatically via Claude Cowork, managed by a user-friendly "Second Brain" interface (Obsidian).

### Q2 — What numbered steps does the author prescribe?

**1. Claude Cowork Setup (The "Employee" Layer)**:
- Install the Claude desktop app and get a Pro/Team plan.
- Create a local folder `Claude Cowork`.
- Add subfolders: `about-me` (for context), `claude-output` (for results), and `templates` (for reusable structures).
- Populate `about-me` with 3 files: `about-me.md`, `anti-ai-writing-style.md`, and `my-company.md`.
- Set **Global Instructions** to always read the `about-me` folder.

**2. Obsidian Integration (The "Second Brain" Layer)**:
- Download and install **Obsidian** (free).
- Choose "Open folder as a vault" and select your `Claude Cowork` folder.
- Use Obsidian to browse, search, and edit your context files with a clean UI (Google Docs style) rather than a raw text editor.

**3. The Skill Extraction Workflow**:
- Prompt Claude Cowork: "Create a skill called [name]. Interview me about [task]. Save it as a skill I can call with /[name]."
- Answer the interview questions.
- Review and benchmarks the skill.
- Move the resulting skill file to a dedicated `SKILLS` folder in Obsidian for easy editing.

### Q3 — What principles recur?

- **Files are the Prompt**: Context should be persistent and automatic, not repetitive and manual.
- **Agentic Workflow**: Cowork acts like a "real employee," reading rules and saving deliverables directly to your machine.
- **Portability and Control**: Using `.md` files in a local folder ensures your AI "brain" is yours, searchable, and works across different tools (Obsidian + Claude).
- **The "Second Brain" Concept**: Organizing your AI's context files is as important as the AI itself.

### Q4 — What mistakes does the author warn against?

- **Average Prompting**: Typing short, vague prompts and blaming Claude for average results.
- **Re-explaining Rules**: Creating new Projects for every topic and repeating the same context/rules.
- **The "Geeky" Editor Trap**: Trying to edit raw `.md` files in basic text editors (leads to frustration and lack of maintenance).
- **Not Editing Context**: Letting your `about-me` files get stale. (Fix: Edit in Obsidian to sync live to Cowork).

### Q5 — What diagnostic questions does the author pose?

- Who wants to type 500 words of instructions just to get a first draft?
- Is it too much work to set up Cowork? (Solution: 20-minute block).
- Does the output sound like everyone else? (Signal for lack of context).

### Q6 — Can the method be expressed as numbered steps?

**YES** — Skill candidate: `setup-obsidian-cowork-second-brain`.

## Content Preview

---
title: "Prompting is the worst way to use Claude."
source: "https://ruben.substack.com/p/stop-prompting-claude"
author:
  - "[[Ruben Hassid]]"
published: 2026-04-15
created: 2026-05-09
description: "Prompting is the worst way to use Claude. Do this instead:"
tags:
  - "clippings"
---
Stop prompting Claude.

For example, this is the worst way to use Claude:


*(... full content in raw/extracts/)*

## Related pages

*(Cross-references to be added as concepts are identified)*
