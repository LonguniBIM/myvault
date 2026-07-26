---
type: source
title: Cowork (April 2026 update)
source_url: "https://ruben.substack.com/p/claude-cowork-20"
author: "[[Ruben Hassid]]"
published: 2026-04-09
tags:
  - cowork
  - update
  - automation
  - workflow
related:
  - "[[Claude]]"
  - "[[Claude Cowork]]"
  - "[[Wispr Flow]]"
  - "[[Token Optimization]]"
created: 2026-05-09
updated: 2026-05-10
---

# Cowork (April 2026 update)

## Source Context

**Author:** [[Ruben Hassid]]  
**Published:** 2026-04-09  
**URL:** https://ruben.substack.com/p/claude-cowork-20  
**Type:** Newsletter / Technical Tutorial

## Six-Question Analysis

### 1. What problem does this document solve?

**Problem:** Users are using Claude Cowork with outdated setups (from early 2026) that are slow, token-expensive, and fail to leverage new features like Opus 4.6 and dictation tools.

**Key pain points:**
- Token bloat (re-reading massive history/profile files)
- Input bottlenecks (typing vs speaking)
- Lack of structure in Cowork folders

### 2. What numbered steps does the author prescribe?

**Method 1: The Triple-Folder Cowork Setup**
1. Create a root folder named **Claude Cowork**.
2. Create 3 subfolders: `ABOUT ME/`, `OUTPUTS/`, `TEMPLATES/`.
3. Populate `ABOUT ME/` with 3 core files: `about-me.md`, `anti-ai-writing-style.md`, `my-company.md`.
4. Keep these files under 2,000 tokens each to prevent loose summarizing by Claude.

**Method 2: Initializing the Profile (The Interview)**
1. Open a new Cowork session using Opus 4.6 + Extended Thinking.
2. Prompt Cowork to interview you (using `AskUserQuestion`) to build the files.
3. Dictate answers using Wispr Flow for richer context and speed.
4. Command Cowork to condense answers into prose/bullets (no raw transcripts).

**Method 3: Global Instructions Configuration**
1. Go to **Settings → Cowork → Edit Global Instructions**.
2. Paste instructions that force Claude to read `ABOUT ME/` before every task.
3. Explicitly forbid reading `OUTPUTS/` or `TEMPLATES/` unless specified (to save tokens).

**Method 4: Token-Saving Habits**
1. **Restart conversations** instead of sending follow-ups (saves re-reading history).
2. **Fresh sessions every 20 messages** to clear context bloat.
3. **Batch tasks** into single messages.
4. **Use Sonnet/Haiku** for low-stakes tasks; save Opus for deep work.

### 3. What principles recur throughout?

1. **Context efficiency** - High-signal, low-noise files (under 2,000 tokens).
2. **"Yapping" as Quality** - Spoken input provides 4x speed and richer context than lazy typing.
3. **The Human Bottleneck** - AI is faster than our typing; optimize input via dictation.
4. **Tool Specialization** - Use the right model for the right task (Opus vs Sonnet).
5. **Flow State** - Dictation feels natural and mirrors creative dialogue.

### 4. What mistakes does the author warn against?

1. **Token Furnaces** - Sending 30+ follow-up messages in one thread (98.5% of tokens are history bloat).
2. **Generic AI Tone** - Letting Claude write without an `anti-ai-writing-style` audit.
3. **Profile Bloat** - Keeping 20,000+ word "about me" transcripts (causes Claude to lose focus).
4. **Self-Editing while Inputting** - Just "dump" thinking via voice and let Claude filter.

### 5. What diagnostic questions does the author pose?

1. "Is my about-me file eating too much context?" (Check if > 2,000 tokens).
2. "Am I the slow part of this conversation?" (Check typing speed vs speaking speed).
3. "Does this sound like my voice or generic AI?"

### 6. Can the method be expressed as numbered steps?

**YES** - Three main workflows identified:
- **Cowork Folder Architecture** (`wiki/methodology/cowork-folder-setup`)
- **Voice-Driven Context Extraction** (`wiki/methodology/voice-context-ingest`)
- **Token Budget Management** (`wiki/methodology/cowork-token-optimization`)

---

## Key Features (April 2026)

- **Opus 4.6 + Extended Thinking:** The current "smartest" model combination.
- **Connectors:** Native integration with Slack, Google Drive, and Notion.
- **Wispr Flow:** Recommended dictation layer to solve the human input bottleneck.

## Extraction Metadata

**Extracted:** 2026-05-10  
**Source file:** `d:\wiki\Claude\raw\sources\Cowork.md`  
**Skill status:** Candidate - high potential for `cowork-setup` and `voice-ingest` skills.
