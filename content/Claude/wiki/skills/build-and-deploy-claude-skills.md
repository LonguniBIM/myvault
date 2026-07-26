---
name: build-and-deploy-claude-skills
description: Create, test, and deploy reusable Claude Skills (slash commands) to automate repeatable processes.
type: skill
trigger: "When you have a process you repeat at least weekly and want to automate it to save tokens and time."
time_estimate: "30 minutes"
difficulty: "medium"
prerequisites:
  - Claude Cowork (Opus 4.6 + Extended Thinking)
  - Desktop App installed
tags:
  - automation
  - skills
  - productivity
  - optimization
related:
  - "[[Claude Skills]]"
created: 2026-05-10
updated: 2026-05-10
---

# Build and Deploy Claude Skills

## Why This Matters

Skills (slash commands) solve "re-explanation fatigue" and token waste. They capture *how* to do a job as a reusable process that fires automatically or via a slash command, reducing the need to re-upload files or write long context-heavy prompts.

## The Skill

Build a portable `SKILL.md` and deploy it to Claude's Capabilities menu.

## Steps

### Phase 1: Creation via Skill Creator

1. Open **Claude Cowork** (use Opus 4.6 + Extended Thinking).
2. Prompt: `"Use the skill-creator to help me build a skill for [task]."`
3. Answer the "interview" questions to specifically capture the process steps and logic.
4. Review the generated `SKILL.md` file.

### Phase 2: Evaluation and Debugging

1. Run the "Evaluation" step during the creation process.
2. **The Debug Question**: Ask Claude: `"When would you use the [skill-name] skill?"` to verify it understands the trigger correctly.
3. Check for **Negative Triggers**: Ensure the `SKILL.md` includes "Do NOT use for..." instructions to prevent hijacking unrelated tasks.

### Phase 3: Deployment

1. Save the Skill folder locally.
2. Go to **Settings → Capabilities → Skills → Upload**.
3. Upload the Skill folder.

## Optimization Hacks

- **Reverse-Engineering**: Turn a successful chat session into a Skill via the session menu arrow.
- **Voice Stacking**: Keep voice/tone in `about-me.md` and technical processes in the Skill.
- **Overcoming Laziness**: Add `"Take your time. Quality over speed. Don't skip steps."` to the internal user prompt in `SKILL.md`.

## Watch Out For

- **Vague Descriptions**: Causes the Skill to never fire.
- **Broad Descriptions**: Causes the Skill to hijack unrelated conversations.
- **Internalizing Tone**: Keep tone/voice rules separate (in `about-me.md`) to keep Skills technical and reusable.

## Source

**Article**: [[Claude Skills]]  
**Author**: [[Ruben Hassid]]  
**Published**: 2026-04-01
