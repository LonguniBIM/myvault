---
type: source
title: Claude Code
tags: [claude-code, workflow, setup, prompts, context, high, high]
related: [claude-code, claude-cowork, github, vscode, vibecoding, screenshot-first-prompting, project-memory-file, permission-friction, claude-code-for-non-coders-workflow]
created: 2026-05-10
updated: 2026-05-10
authors: [Ruben Hassid]
year: 2026
url: "https://ruben.substack.com/p/claude-code"
venue: substack
skill_potential: true
---

# Claude Code

> [!info] Source
> Ruben Hassid's guide frames [[claude-code]] as a way for non-coders to create websites, dashboards, training materials, and technical briefs through English prompts, screenshots, file context, and iterative visual review.

## Summary

This source extends the project's existing Claude product-line research by positioning [[claude-code]] as the coding equivalent of [[claude-cowork]]: an agentic workspace that turns folders, screenshots, prompts, and GitHub publishing into deliverables without requiring the user to read code.

The article's core claim is that "English is the new code" for non-technical users, but the workflow only works well when the user supplies strong context, tests the resulting website visually, and knows how to interrupt loops.

## Six-Question Analysis

### 1. What problem does this document solve?

It solves the onboarding gap for non-coders who hear that [[claude-code]] is transformative but do not know why they would use a developer tool or how to start safely.

The source translates developer concepts into familiar metaphors:
- [[github]] is "Google Drive for code"
- [[vscode]] is the faster workspace for Claude Code
- The user acts as project manager while Claude acts as junior developer
- Visual testing replaces code review for non-coders

### 2. What numbered steps does the author prescribe?

The article contains several step-based workflows:

1. **Basic Claude Code setup**: create [[github]] account, connect GitHub in Claude settings, prompt Claude Code with goal/success criteria/example/steps, accept edits, inspect the live website.
2. **Faster VS Code setup**: download [[vscode]], install the Claude extension, enable skip/bypass permissions, start a new Claude Code session.
3. **Prompting pattern**: start with screenshots, describe the end result instead of implementation steps, point Claude to files, do one deliverable per prompt, screenshot visual bugs.
4. **Project memory setup**: ask Claude Code to create [[project-memory-file]] using a root CLAUDE.md that records project structure, design choices, preferences, and pages.
5. **First 30 minutes**: install, build a context folder, start a first task, accept/edit, then produce a real deliverable.

These steps are extracted into [[claude-code-for-non-coders-workflow]].

### 3. What principles recur throughout?

- **Natural-language briefs beat implementation instructions**: describe the desired outcome, not HTML/CSS mechanics.
- **Files replace prompts**: durable context in markdown files and CLAUDE.md reduces re-explanation.
- **Screenshots compress visual intent**: visual references and bug screenshots are faster than long descriptions.
- **One deliverable per sprint**: smaller iterations prevent overloaded prompts and make quality easier to judge.
- **Visual QA matters for non-coders**: if the user cannot review code, they must test the actual site across buttons, pages, and mobile.

### 4. What mistakes does the author warn against?

- Treating Claude Code as only for developers.
- Dumping too many features into one prompt.
- Giving low-level implementation instructions instead of product requirements.
- Saying "make it look good" without references, fonts, spacing, or color direction.
- Ignoring repeated error loops instead of stopping and asking for alternative approaches.
- Relying on the desktop Code tab after becoming comfortable, when VS Code offers a faster workflow.
- Trusting generated code blindly without testing the live result.

### 5. What diagnostic questions does the author pose?

The source implies a practical checklist:

- What do I want Claude Code to build, and what does success look like?
- What example, screenshot, or reference can I attach?
- What files should Claude read before building?
- Is this one deliverable or an overloaded bundle of features?
- What looks wrong in the live website after clicking through it?
- Has Claude repeated the same error twice, indicating a loop?
- What should be recorded in CLAUDE.md so future sessions retain project context?

### 6. Can the method be expressed as numbered steps?

Yes. The method is a strong skill candidate because it has a clear trigger, ordered setup steps, reusable prompt template, quality-control loop, and loop-breaking rule. See [[claude-code-for-non-coders-workflow]].

## Extracted Entities

- [[claude-code]] — primary tool being explained
- [[claude-cowork]] — comparison point for file-based workflows
- [[github]] — publishing and repository host
- [[vscode]] — recommended Claude Code workspace after first trial
- [[wispr-flow]] — voice dictation helper for building context files

## Extracted Concepts

- [[vibecoding]] — building by directing an AI agent through natural language and feedback
- [[screenshot-first-prompting]] — using images to specify desired UI and diagnose bugs
- [[permission-friction]] — repeated permission prompts as a workflow bottleneck
- [[project-memory-file]] — using CLAUDE.md as durable project context

## Skill Candidate Assessment

- **Skill name**: [[claude-code-for-non-coders-workflow]]
- **Potential**: high
- **Steps**: 7
- **Why it qualifies**: It combines setup, context preparation, prompt structure, visual QA, iterative feedback, and loop recovery into a repeatable operating procedure.

## Connections

This source reinforces [[files-replace-prompts]] by treating markdown context files and CLAUDE.md as the core memory layer. It also extends [[dual-tool-workflow]] by distinguishing the desktop app as a first trial from [[vscode]] as the faster long-term Claude Code environment.
