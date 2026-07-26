---
type: source
title: "Be a 10x Vibe Coder (Claude Code + Cursor + MCP)"
tags: [workflow, mcp, optimization, skills, agents, topic:workflow, topic:optimization, topic:mcp, priority:high]
related: [claude-ai-assistant, cursor-ide, context7-mcp, supabase-mcp, bugbot, whisperflow, ultrathink-keyword, dual-tool-workflow, background-tasks-feature, ai-code-review, vibe-coder-workflow]
created: 2026-05-08
updated: 2026-05-08
authors: [Chris (indie developer)]
year: 2026
url: "https://www.youtube.com/watch?v=li788UL1qyI"
venue: "YouTube / Podcast"
---

# Be a 10x Vibe Coder (Claude Code + Cursor + MCP)

**Source**: YouTube — hosted by Craig, guest Chris (indie developer building productivity apps solo)
**Extracted**: 2026-05-08 via Whisper transcription

---

## Six-Question Analysis

### Q1 — What problem does this solve?

Solo developers and vibe coders struggle to choose the right AI coding tool at the right moment. With Claude Code, Cursor, and dozens of models available, there's no clear framework for when to use which — leading to suboptimal output and wasted tokens. Chris presents a battle-tested dual-tool workflow that consistently multiplies solo developer output.

### Q2 — What numbered steps does the author prescribe?

**Tool Selection Decision Tree:**
1. **Complex architecture / whole-app scaffolding** → Claude Code + Opus (use sparingly, exhausts in 3–4 hrs/week)
2. **Complex bugs / plan-first tasks** → Cursor Plan Mode with GPT-5.1 high (planning) + Sonnet (execution)
3. **UI / animations / design details** → Claude Code (has edge over Cursor even on same Sonnet model)
4. **Simple small changes** → Either tool, no plan mode needed

**7 Rapid-Fire Tips:**
1. **Always use plan mode** — toggle in Cursor or Shift+Tab in Claude Code; increases output quality ~20%+
2. **Use `ultrathink` keyword** — special Claude Code keyword, triggers deeper thinking, adds color change; use in 90% of messages
3. **Run server in background** — tell Claude Code "run the server in the background"; gives Claude access to live server logs for debugging
4. **Use MCP servers** — Context7 for docs, Supabase for database; replaces manual URL-feeding
5. **Add AI code review** — Bugbot or Claude Code's GitHub integration; catches security issues on every PR ($40/mo for Cursor's version)
6. **Dictate prompts** — use Whisper Flow; produces more detailed prompts in less time than typing
7. **Use Claude deep research** — Claude.ai chat (included with Claude Code plan) for 12-min architectural research before coding

### Q3 — What principles recur?

- **Plan before execute**: Both tools have plan modes; reviewing the plan prevents costly retroactive fixes
- **Right tool for right task**: Don't commit to one tool — maintain two and switch by task type
- **Give AI full context**: MCP servers, background logs, dictated details = AI makes fewer mistakes
- **Start simple, graduate**: Beginners → Create.xyz / v0 / Bolt → Claude Code + Cursor after gaining AI fluency
- **Parallel A/B testing**: Run same prompt on both tools, pick the better result

### Q4 — What mistakes does the author warn against?

- Feeding documentation via URL instead of using Context7 MCP (scraping is unreliable, poorly formatted)
- Skipping plan mode — you'll fix mistakes retroactively instead of preventing them
- Not using AI code review as a solo developer — security vulnerabilities will slip through at vibe coding speed
- Not running a background server — you have to manually copy/paste logs for every debug session
- Typing prompts instead of dictating — loses detail and steers AI less precisely

### Q5 — What diagnostic questions does the author pose?

- Is the problem *very complex or architectural*? → Claude Code + Opus
- Is Opus quota exhausted? → Cursor Plan Mode (GPT-5.1 high)
- Is the problem a *complex bug*? → Cursor Plan Mode (better at follow-up questions)
- Is it *UI / design / animation*? → Claude Code (edge even with same Sonnet model)
- Am I a solo dev with no code reviewer? → Add Bugbot or equivalent immediately
- Do I need a technical architecture decision? → Claude deep research first, then code

### Q6 — Can the method be expressed as numbered steps?

**YES** → see [[vibe-coder-workflow]] methodology page. Skill candidate.

---

## Key Entities Mentioned

- [[claude-ai-assistant]] — Claude Code with Opus 4.1 and Sonnet models
- [[cursor-ide]] — Plan Mode with GPT-5.1 high + Sonnet execution
- [[context7-mcp]] — Free MCP server for compressed, LLM-formatted documentation
- [[supabase-mcp]] — Database MCP that configures Supabase security rules
- [[bugbot]] — AI code reviewer for GitHub PRs
- [[whisperflow]] — Voice dictation tool with developer terminology support

## Key Concepts

- [[ultrathink-keyword]] — Special Claude Code keyword for deeper reasoning
- [[dual-tool-workflow]] — Using Claude Code + Cursor simultaneously for different tasks
- [[background-tasks-feature]] — Claude Code's ability to run dev server and access logs
- [[ai-code-review]] — Automated PR review for solo developers

## Key Findings

- Plan mode produces ~20% better output at minimum on same model
- Cursor Plan Mode + GPT-5.1 high gave better first-shot result than Claude Code on same Sonnet model in live test
- Claude Code has edge over Cursor for UI/animations even using identical model
- `ultrathink` keyword appears to not significantly increase token consumption despite deeper reasoning
