---
type: clip
title: "GitHub - kepano/obsidian-skills: Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI. · GitHub"
url: "https://github.com/kepano/obsidian-skills"
clipped: 2026-04-29
origin: web-clip
sources: []
tags: [web-clip]
---

# GitHub - kepano/obsidian-skills: Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI. · GitHub

Source: https://github.com/kepano/obsidian-skills

Skip to content

You signed in with another tab or window. Reload to refresh your session.

You signed out in another tab or window. Reload to refresh your session.

You switched accounts on another tab or window. Reload to refresh your session.

Dismiss alert

kepano

/

obsidian-skills

Public

Notifications

You must be signed in to change notification settings

Fork

1.8k

Star

27k

main1 Branch0 TagsGo to fileCodeOpen more actions menuFolders and filesNameNameLast commit messageLast commit dateLatest commitkepanoMerge pull request #64 from petersolopov/improve/defuddle-skip-md-urlsOpen commit detailsApr 3, 2026fa1e131 · Apr 3, 2026History37 CommitsOpen commit details37 Commits.claude-plugin.claude-pluginchore: update plugin version so it can be updated from the marketplaceFeb 25, 2026skillsskillsSkip defuddle for .md URLsMar 29, 2026LICENSELICENSElicenseJan 6, 2026README.mdREADME.mdMerge pull request #37 from chenminhua/patch-1Feb 27, 2026View all filesRepository files navigationAgent Skills for use with Obsidian.

These skills follow the Agent Skills specification so they can be used by any skills-compatible agent, including Claude Code and Codex CLI.

Installation

Marketplace

/plugin marketplace add kepano/obsidian-skills

/plugin install obsidian@obsidian-skills

npx skills

npx skills add git@github.com:kepano/obsidian-skills.git

Manually

Claude Code

Add the contents of this repo to a /.claude folder in the root of your Obsidian vault (or whichever folder you're using with Claude Code). See more in the official Claude Skills documentation.

Codex CLI

Copy the skills/ directory into your Codex skills path (typically ~/.codex/skills). See the Agent Skills specification for the standard skill format.

OpenCode

Clone the entire repo into the OpenCode skills directory (~/.opencode/skills/):

git clone https://github.com/kepano/obsidian-skills.git ~/.opencode/skills/obsidian-skills

Do not copy only the inner skills/ folder — clone the full repo so the directory structure is ~/.opencode/skills/obsidian-skills/skills/<skill-name>/SKILL.md.

OpenCode auto-discovers all SKILL.md files under ~/.opencode/skills/. No changes to opencode.json or any config file are needed. Skills become available after restarting OpenCode.

Skills

Skill

Description

obsidian-markdown

Create and edit Obsidian Flavored Markdown (.md) with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax

obsidian-bases

Create and edit Obsidian Bases (.base) with views, filters, formulas, and summaries

json-canvas

Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections

obsidian-cli

Interact with Obsidian vaults via the Obsidian CLI including plugin and theme development

defuddle

Extract clean markdown from web pages using Defuddle, removing clutter to save tokens

About

Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI.

Topics

cli

skills

opencode

obsidian

codex

claude

defuddle

clawdbot

openclaw

Resources

Readme

License

MIT license

Uh oh!

There was an error while loading. Please reload this page.

Activity

Stars

27k

stars

Watchers

169

watching

Forks

1.8k

forks

Report repository

Releases

No releases published

Packages

0

No packages published

Contributors

13

You can’t perform that action at this time.
