---
name: setup-optimized-cowork-environment
description: Set up a high-speed, token-efficient Claude Cowork environment with structured folders and voice dictation.
type: skill
trigger: "When starting with Claude Cowork or wanting to optimize an existing setup for speed and cost."
time_estimate: "20 minutes"
difficulty: "easy"
prerequisites:
  - Claude Desktop App (Paid Pro/Max plan)
  - Dictation tool (e.g., Wispr Flow)
tags:
  - setup
  - optimization
  - cowork
  - tokens
related:
  - "[[Cowork]]"
  - "[[Claude Cowork + Project]]"
created: 2026-05-10
updated: 2026-05-10
---

# Setup Optimized Cowork Environment

## Why This Matters

Most users are the "slow part" of the AI workflow. This setup solves the human bottleneck by using voice dictation (150 wpm vs 60 wpm typing) and persistent context files to eliminate repetitive prompting and context waste.

## The Skill

Configure a 3-folder local workspace and global instructions to maximize Claude's "agentic" capabilities.

## Steps

### Phase 1: Local Folder Structure (5 minutes)

1. Create a root folder named `Claude Cowork`.
2. Create three subfolders inside:
   - `ABOUT ME`: For identity, taste, and company context.
   - `OUTPUTS`: For Claude to save deliverables (one subfolder per project).
   - `TEMPLATES`: For reusable skeletons/best work.

### Phase 2: Core Context Files (10 minutes)

1. **`about-me.md`**: Ask Claude to interview you (20 questions) about role, tools, and "what good looks like." Condense to <2,000 tokens.
2. **`anti-ai-writing-style.md`**: List banned patterns (e.g., negative parallelism) and 100+ "AI-words" (delve, leverage, etc.).
3. **`my-company.md`**: Define 2-3 top goals for the year and what you are "saying no to."

### Phase 3: Global Instructions (2 minutes)

1. Go to **Settings → Cowork → Edit Global Instructions**.
2. Paste the standard instruction:
   `Before every task, read all files in ABOUT ME/. Save deliverables in OUTPUTS/[ProjectName]. Use AskUserQuestion if the brief is unclear.`

### Phase 4: Voice Bridge (3 minutes)

1. Install a dictation tool (e.g., Wispr Flow).
2. Set a hotkey.
3. Practice "yapping" your initial prompts to provide 3x richer context than typing.

## Usage Habits

- **Restarting Conversations**: Instead of follow-ups, click "Restart the conversation from here" to clear token history.
- **Auto-Templating**: At the end of a task, prompt: `"Save this as a template in TEMPLATES/"`.
- **Model Selection**: Use Sonnet for grammar/formatting; reserve Opus for deep reasoning.

## Watch Out For

- **Context Bloat**: Keep profile files small (<2k tokens) or Claude will summarize them loosely.
- **Token Stacking**: Long sessions are "token furnaces." Start fresh every 20 messages.

## Source

**Article**: [[Cowork]]  
**Author**: [[Ruben Hassid]]  
**Published**: 2026-04-09
