---
type: clip
title: "GitHub - forrestchang/andrej-karpathy-skills: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. · GitHub"
url: "https://github.com/forrestchang/andrej-karpathy-skills?fbclid=IwZXh0bgNhZW0CMTAAYnJpZBExamhxamlKRmgzbkt3MVcxU3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7wPby614aRMpmmU_HuCVTHIeX8xDBrSI21PhmmwIr_wpmsiON2PtJsUHE_dw_aem_1Q6Pp6cQohFjZ0HJbJyGow"
clipped: 2026-04-28
origin: web-clip
sources: []
tags: [web-clip]
---

# GitHub - forrestchang/andrej-karpathy-skills: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. · GitHub

Source: https://github.com/forrestchang/andrej-karpathy-skills?fbclid=IwZXh0bgNhZW0CMTAAYnJpZBExamhxamlKRmgzbkt3MVcxU3NydGMGYXBwX2lkEDIyMjAzOTE3ODgyMDA4OTIAAR7wPby614aRMpmmU_HuCVTHIeX8xDBrSI21PhmmwIr_wpmsiON2PtJsUHE_dw_aem_1Q6Pp6cQohFjZ0HJbJyGow

Skip to content

You signed in with another tab or window. Reload to refresh your session.

You signed out in another tab or window. Reload to refresh your session.

You switched accounts on another tab or window. Reload to refresh your session.

Dismiss alert

forrestchang

/

andrej-karpathy-skills

Public

Notifications

You must be signed in to change notification settings

Fork

9.2k

Star

94.8k

main5 Branches0 TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitherobrine19Sync Chinese README with English version (add Cursor section) (#95)Apr 20, 20262c60614 · Apr 20, 2026History28 CommitsOpen commit details28 Commits.claude-plugin.claude-pluginFix plugin.json schema validation errorsFeb 1, 2026.cursor/rules.cursor/rulesadd cursor support (#92)Apr 19, 2026skills/karpathy-guidelinesskills/karpathy-guidelinesrefactor: restructure repo for skills.sh compatibilityJan 28, 2026CLAUDE.mdCLAUDE.mdAdd Karpathy-inspired Claude Code guidelinesJan 27, 2026CURSOR.mdCURSOR.mdadd cursor support (#92)Apr 19, 2026EXAMPLES.mdEXAMPLES.mdAdd examples of coding principles and common mistakesJan 30, 2026README.mdREADME.mdadd cursor support (#92)Apr 19, 2026README.zh.mdREADME.zh.mdSync Chinese README with English version (add Cursor section) (#95)Apr 20, 2026View all filesRepository files navigationKarpathy-Inspired Claude Code Guidelines

Check out my new project Multica — an open-source platform for running and managing coding agents with reusable skills.

Follow me on X: https://x.com/jiayuan_jy

A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

English | 简体中文

The Problems

From Andrej's post:

"The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."

"They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."

"They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."

The Solution

Four principles in one file that directly address these issues:

Principle

Addresses

Think Before Coding

Wrong assumptions, hidden confusion, missing tradeoffs

Simplicity First

Overcomplication, bloated abstractions

Surgical Changes

Orthogonal edits, touching code you shouldn't

Goal-Driven Execution

Leverage through tests-first, verifiable success criteria

The Four Principles in Detail

1. Think Before Coding

Don't assume. Don't hide confusion. Surface tradeoffs.

LLMs often pick an interpretation silently and run with it. This principle forces explicit reasoning:

State assumptions explicitly — If uncertain, ask rather than guess

Present multiple interpretations — Don't pick silently when ambiguity exists

Push back when warranted — If a simpler approach exists, say so

Stop when confused — Name what's unclear and ask for clarification

2. Simplicity First

Minimum code that solves the problem. Nothing speculative.

Combat the tendency toward overengineering:

No features beyond what was asked

No abstractions for single-use code

No "flexibility" or "configurability" that wasn't requested

No error handling for impossible scenarios

If 200 lines could be 50, rewrite it

The test: Would a senior engineer say this is overcomplicated? If yes, simplify.

3. Surgical Changes

Touch only what you must. Clean up only your own mess.

When editing existing code:

Don't "improve" adjacent code, comments, or formatting

Don't refactor things that aren't broken

Match existing style, even if you'd do it differently

If you notice unrelated dead code, mention it — don't delete it

When your changes create orphans:

Remove imports/variables/functions that YOUR changes made unused

Don't remove pre-existing dead code unless asked

The test: Every changed line should trace directly to the user's request.

4. Goal-Driven Execution

Define success criteria. Loop until verified.

Transform imperative tasks into verifiable goals:

Instead of...

Transform to...

"Add validation"

"Write tests for invalid inputs, then make them pass"

"Fix the bug"

"Write a test that reproduces it, then make it pass"

"Refactor X"

"Ensure tests pass before and after"

For multi-step tasks, state a brief plan:

1. [Step] → verify: [check]

2. [Step] → verify: [check]

3. [Step] → verify: [check]

Strong success criteria let the LLM loop independently. Weak criteria ("make it work") require constant clarification.

Install

Option A: Claude Code Plugin (recommended)

From within Claude Code, first add the marketplace:

/plugin marketplace add forrestchang/andrej-karpathy-skills

Then install the plugin:

/plugin install andrej-karpathy-skills@karpathy-skills

This installs the guidelines as a Claude Code plugin, making the skill available across all your projects.

Option B: CLAUDE.md (per-project)

New project:

curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md

Existing project (append):

echo "" >> CLAUDE.md

curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md

Using with Cursor

This repository includes a committed Cursor project rule (.cursor/rules/karpathy-guidelines.mdc) so the same guidelines apply when you open the project in Cursor. See CURSOR.md for setup, using the rule in other projects, and how this relates to Claude Code.

Key Insight

From Andrej:

"LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."

The "Goal-Driven Execution" principle captures this: transform imperative instructions into declarative goals with verification loops.

How to Know It's Working

These guidelines are working if you see:

Fewer unnecessary changes in diffs — Only requested changes appear

Fewer rewrites due to overcomplication — Code is simple the first time

Clarifying questions come before implementation — Not after mistakes

Clean, minimal PRs — No drive-by refactoring or "improvements"

Customization

These guidelines are designed to be merged with project-specific instructions. Add them to your existing CLAUDE.md or create a new one.

For project-specific rules, add sections like:

## Project-Specific Guidelines

- Use TypeScript strict mode

- All API endpoints must have tests

- Follow the existing error handling patterns in `src/utils/errors.ts`

Tradeoff Note

These guidelines bias toward caution over speed. For trivial tasks (simple typo fixes, obvious one-liners), use judgment — not every change needs the full rigor.

The goal is reducing costly mistakes on non-trivial work, not slowing down simple tasks.

License

MIT

About

A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

Resources

Readme

Uh oh!

There was an error while loading. Please reload this page.

Activity

Stars

94.8k

stars

Watchers

495

watching

Forks

9.2k

forks

Report repository

Releases

No releases published

Packages

0

No packages published

Contributors

8

You can’t perform that action at this time.
