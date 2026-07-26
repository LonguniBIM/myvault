---
type: source
title: "Claude Cowork + Project"
tags: [extract, text]
related: []
created: 2026-05-10
updated: 2026-05-10
authors: []
year: 2026
url: ""
venue: ""
---

# Claude Cowork + Project

**Summary**: Content extracted from text file `Claude Cowork + Project.md`.

**Sources**: `Claude Cowork + Project.md`

**Last updated**: 2026-05-10

---

## Six-Question Analysis

### Q1 — What problem does this solve?

It solves the "memory gap" in agentic workflows. While Claude Cowork can execute tasks, it originally started every session from zero. "Cowork Projects" combine the execution power of Cowork with the persistent memory and custom instructions of Projects, creating a durable AI employee workspace.

### Q2 — What numbered steps does the author prescribe?

**Creation Workflow:**
1. Open Claude Desktop sidebar > **Projects** > **+**.
2. Choose a method:
   - **Start from scratch**: Create a new local folder and add instructions/files.
   - **Import from a Claude Project**: Transfer instructions/files from an existing browser-based project.
   - **Use existing folder**: Wrap an existing Cowork folder in a Project.
3. Add custom instructions (tone, rules, guardrails).

**Initialization Workflow:**
1. Run the setup prompt: "I just created this Project. Read every file in the folder. Then summarize what you know about this workspace... If something is unclear, use AskUserQuestion."

**Daily Usage Workflow:**
1. Drop new briefs/research into the Project folder.
2. Prompt: "I want to [task]. Start with AskUserQuestion to refine the angle with me before you write anything."
3. Click answers in the generated form.
4. Review the markdown or docx file created directly in the folder.

### Q3 — What principles recur?

- **Scoped Memory**: Knowledge persists within a Project but is isolated from others, preventing "overfitting" or context leakage.
- **Execution + Memory**: Cowork is for doing; Projects are for remembering. Combining them creates an "AI employee".
- **Local Source of Truth**: Files and history are stored on the user's machine, giving Claude direct read/write access to deliverables.

### Q4 — What mistakes does the author warn against?

- Using the old browser-based Projects for execution (they are for chat/team playbooks only).
- Not using **AskUserQuestion** (leads to misaligned execution).
- Expecting team sharing or cloud sync (not available for local Cowork Projects yet).
- Closing the desktop app (stops scheduled tasks).

### Q5 — What diagnostic questions does the author pose?

- Is this a team playbook (use browser Project) or personal execution (use Cowork Project)?
- Has Claude learned the workspace context correctly (use the setup prompt)?
- Do I need this task to recur automatically (use Scheduled tasks)?

### Q6 — Can the method be expressed as numbered steps?

**YES** — Skill candidate: `setup-cowork-project-workflow`.

## Content Preview

---
title: "Claude Cowork + Project."
source: "https://ruben.substack.com/p/claude-cowork-project"
author:
  - "[[Ruben Hassid]]"
published: 2026-03-29
created: 2026-05-09
description: "How to make Claude Cowork (instantly) better:"
tags:
  - "clippings"
---
You switched from ChatGPT to Claude.

You read my guides on [Claude](https://ruben.substack.com/p/claude), [Cowork](https://ruben.substack.com/p/claude-cowork), [Teams](https://ruben.substack.com/p/claude-for-teams), [Charts](https://ruben.substack.com/p/claude-charts), [Code](https://ruben.substack.com/p/claude-code), and [Computer](https://ruben.substack.com/p/claude-computer).


*(... full content in raw/extracts/)*

## Related pages

*(Cross-references to be added as concepts are identified)*
