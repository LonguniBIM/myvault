---
type: source
title: "Cowork"
tags: [extract, text]
related: []
created: 2026-05-10
updated: 2026-05-10
authors: []
year: 2026
url: ""
venue: ""
---

# Cowork

**Summary**: Content extracted from text file `Cowork.md`.

**Sources**: `Cowork.md`

**Last updated**: 2026-05-10

---

## Six-Question Analysis

### Q1 — What problem does this solve?

It solves the "outdated AI workflow" and the "typing bottleneck." It provides a system to set up Claude Cowork (desktop) with a structured local folder hierarchy and voice dictation to maximize speed, save token costs, and ensure outputs reflect the user's specific "taste" without repetitive prompting.

### Q2 — What numbered steps does the author prescribe?

**1. Structured Folder Setup**:
- Create a root folder `Claude Cowork`.
- Add three subfolders: `ABOUT ME` (for context), `OUTPUTS` (for deliverables), and `TEMPLATES` (for reusable skeletons).

**2. Core Context Files (in ABOUT ME)**:
- **about-me.md**: Interview yourself via Claude (20 questions) to capture identity/style. Keep it under 2,000 tokens.
- **anti-ai-writing-style.md**: List banned words (delve, harness, tapestry) and formatting constraints.
- **my-company.md**: Define goals, metrics, and strategy (6-8 questions).

**3. Configure Global Instructions**:
- Go to **Settings → Cowork → Edit Global Instructions**.
- Command Claude to always read `ABOUT ME` files first and save work to `OUTPUTS`.

**4. The Speed Layer (Wispr Flow)**:
- Install a dictation tool (Wispr Flow) to talk at 150 wpm instead of typing at 60 wpm.
- Use voice for initial prompts, answering `AskUserQuestion` forms, and giving nuanced feedback.

**5. Token Optimization Workflow**:
- **Restart Conversation**: Click "Restart from here" instead of sending long follow-up messages to save credits.
- **Fresh Sessions**: Start a new session every 20 messages by asking for a summary and pasting it into a new window.
- **Model Matching**: Use Sonnet/Haiku for simple tasks (grammar, formatting) and reserve Opus for deep work.

**6. Automated Templating**:
- At the end of a successful task, prompt: "Save this as a template in TEMPLATES/."
- Reference these skeletons in future tasks to maintain structural consistency.

### Q3 — What principles recur?

- **Files over Prompts**: Context is best managed through persistent local markdown files, not "clever" manual prompts.
- **The Human Bottleneck**: The user is the slow part; optimizing the "input bridge" (voice) is as important as the AI's speed.
- **Context Hygiene**: Small, high-signal context files (under 2k tokens) ensure Claude reads everything carefully rather than summarizing.
- **Flow State Engineering**: Spoken context is richer and more natural ("yapping") than typed context.

### Q4 — What mistakes does the author warn against?

- **Token Stacking**: Sending message 30 costs 31x message 1. Stop sending follow-ups; restart higher up.
- **Context Bloat**: Large profile files (20k+ tokens) waste money and degrade AI attention.
- **Lazy Prompting**: Typing usually leads to shorter, lower-context prompts than speaking.
- **Over-prompting**: Trying to explain things manually that should be in a persistent `.md` file.

### Q5 — What diagnostic questions does the author pose?

- Is my about-me file lean enough (under 2,000 tokens)?
- Am I the slow part of this session (should I be talking)?
- Did I restart the conversation to save tokens?
- Does Claude have my "north star" (my-company.md) and "taste" (anti-ai-writing-style.md)?

### Q6 — Can the method be expressed as numbered steps?

**YES** — Skill candidate: `setup-optimized-cowork-environment`.

## Content Preview

---
title: "Cowork."
source: "https://ruben.substack.com/p/claude-cowork-20"
author:
  - "[[Ruben Hassid]]"
published: 2026-04-09
created: 2026-05-09
description: "How to set up Claude Cowork (April 2026 update):"
tags:
  - "clippings"
---
I’ve been begging you to switch from ChatGPT to Claude for months.

![](https://substackcdn.com/image/fetch/$s_!S4Mm!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F223530a4-f8e2-4ca1-af2a-0921a9090164_756x244.png)


*(... full content in raw/extracts/)*

## Related pages

*(Cross-references to be added as concepts are identified)*
