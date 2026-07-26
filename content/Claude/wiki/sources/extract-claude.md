---
type: source
title: "Claude"
tags: [extract, text]
related: []
created: 2026-05-10
updated: 2026-05-10
authors: []
year: 2026
url: ""
venue: ""
---

# Claude

**Summary**: Content extracted from text file `Claude.md`.

**Sources**: `Claude.md`

**Last updated**: 2026-05-10

---

## Six-Question Analysis

### Q1 — What problem does this solve?

It solves the "wrong AI" problem for knowledge workers. It frames Claude as a superior alternative to ChatGPT for writing, analyzing, and working with files, particularly through its agentic "Cowork" and "Excel" integrations.

### Q2 — What numbered steps does the author prescribe?

**Onboarding Workflow (30 minutes):**
1. **Minutes 0-5**: Install Claude Desktop, sign up for Pro ($20/mo), and open **Cowork**.
2. **Minutes 5-10**: Create an `about-me.md` text file containing your job role, communication style, and writing samples.
3. **Minutes 10-15**: Start a Cowork conversation by pointing it to your `about-me.md` folder and prompting: "Read the about-me file. Based on it, write [task]."
4. **Minutes 15-20**: Install a Plugin (Productivity, Marketing, or Sales) and use a slash command (e.g., `/marketing:draft-post`).
5. **Minutes 20-25**: Try an Artifact by asking for interactive HTML/SVG output (e.g., "Create a weekly planner template").
6. **Minutes 25-30**: Install the Claude Excel Add-in and use it to explain formulas or generate a P&L model from scratch.

**Prompting Principle:**
1. Start prompts with: "Read the uploaded files completely before responding. DO NOT start executing yet. Instead, ask me clarifying questions (use AskUserQuestion)."

### Q3 — What principles recur?

- **Files replace prompts**: Durable context in markdown files is better than long, clever prompts.
- **Agentic feedback loop**: Forcing Claude to ask questions (AskUserQuestion) ensures alignment before execution.
- **Right tool for the right task**: Use Opus 4.6 + Extended Thinking for reasoning; use Gemini for images; use Grok for real-time search.

### Q4 — What mistakes does the author warn against?

- Using the wrong model (Sonnet/Haiku when Opus 4.6 is needed for complex reasoning).
- Forgetting to turn on **Extended Thinking**.
- Overbloating "Projects" with too many files (prefers Cowork + local folders).
- Relying on images/search in Claude (where it falls short).

### Q5 — What diagnostic questions does the author pose?

- Am I writing a prompt, or should I be pointing Claude to a file?
- Did I force Claude to ask me clarifying questions before it started?
- Is this a task for Claude (writing/thinking) or Gemini (images)?

### Q6 — Can the method be expressed as numbered steps?

**YES** — Skill candidate: `master-claude-in-30-minutes`.

## Content Preview

---
title: "Claude."
source: "https://ruben.substack.com/p/claude"
author:
  - "[[Ruben Hassid]]"
published: 2026-02-18
created: 2026-05-09
description: "How to set up Claude the right way (so you actually stop going back to ChatGPT)."
tags:
  - "clippings"
---
The people I talk to every day quietly switched.

The creators I follow. The teams I consult for. The founders in my DMs. One by one, they stopped opening ChatGPT. And they all moved to the same place.


*(... full content in raw/extracts/)*

## Related pages

*(Cross-references to be added as concepts are identified)*
