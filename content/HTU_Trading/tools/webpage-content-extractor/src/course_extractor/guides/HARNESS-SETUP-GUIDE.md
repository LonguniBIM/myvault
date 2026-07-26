# Harness v0 Setup Guide

> **v2** — This guide reflects `harness_template` with the integrated
> 4-layer tooling stack (Harness + Memory-Bank + Serena + GitNexus +
> Neural Memory) and the platform-agnostic Workflow Phases. For the
> previous Cursor-only setup, see git history.

## Two paths

| Your project... | Use this guide |
|---|---|
| ...is empty or brand new | [GREENFIELD-QUICKSTART.md](GREENFIELD-QUICKSTART.md) |
| ...already has Harness, docs, memory-bank, or .cursor/rules | [BROWNFIELD-MIGRATION.md](BROWNFIELD-MIGRATION.md) |
| ...you only want the docs (no MCP tooling) | This guide, "Harness-only" section below |

## Source

[github.com/LonguniBIM/harness_template](https://github.com/LonguniBIM/harness_template)

## Prerequisites

- Git installed and accessible from terminal.
- Bash (Git Bash on Windows; native on macOS/Linux/WSL).
- Target project directory exists.
- (Optional) Agent with MCP support: Cursor, Claude Code, or similar.

---

## Path 1 — Greenfield install

Full walkthrough: [GREENFIELD-QUICKSTART.md](GREENFIELD-QUICKSTART.md).

TL;DR:
```bash
git clone https://github.com/LonguniBIM/harness_template my-project
cd my-project
rm -rf .git && git init -b main
bash scripts/install-harness.sh --greenfield --project-name "MyProject"
```

## Path 2 — Brownfield migration

Full walkthrough: [BROWNFIELD-MIGRATION.md](BROWNFIELD-MIGRATION.md).

TL;DR:
```bash
cd existing-project
bash /path/to/harness_template/scripts/detect-existing.sh
bash /path/to/harness_template/scripts/install-harness.sh --brownfield --dry-run
bash /path/to/harness_template/scripts/install-harness.sh --brownfield
```

## Path 3 — Harness-only (no MCP tooling)

If you want only the process framework (no Memory-Bank scaffolds, no
`.cursor/rules`, no Serena), use the `--skip-tooling --skip-cursor` flags:

```bash
cd /path/to/target-project
bash /path/to/harness_template/scripts/install-harness.sh \
  --greenfield --project-name "MyProject" \
  --skip-tooling --skip-cursor
```

Resulting structure:
```
project/
├── AGENTS.md
├── CLAUDE.md
├── docs/
│   ├── HARNESS.md, FEATURE_INTAKE.md, ARCHITECTURE.md
│   ├── decisions/0001..0005-*.md
│   ├── templates/, stories/, product/, demo/, guides/
└── scripts/install-harness.sh (and friends)
```

You can add tooling later by running:
```bash
bash scripts/bootstrap-tooling.sh         # memory-bank/ + .serena/
bash scripts/install-harness.sh --brownfield --skip-tooling   # .cursor/rules/ only
```

---

## After install — agent setup

### Cursor IDE

The installer puts `.cursor/rules/harness-mcp-bridge.mdc` and
`.cursor/rules/project-namespace.mdc` with `alwaysApply: true`, so every
agent prompt receives the integrated workflow.

Add MCP server config to `~/.cursor/mcp.json` (or your equivalent):

```bash
bash scripts/bootstrap-tooling.sh --dry-run
# Copy the printed JSON block into your MCP config
```

### Claude Code CLI

Claude Code auto-reads `CLAUDE.md` and `AGENTS.md` at the project root.
No additional setup needed for the process framework.

For MCP tooling, install the same servers as listed in the
`bootstrap-tooling.sh` output, configured via your Claude Code MCP
config.

### Other agents

Any agent that can read Markdown can follow `AGENTS.md`. The 4-phase
workflow is canonical in `AGENTS.md` §"Workflow Phases" — agents that
don't support MCP can still implement Phase 0/1/2/3 by reading
`memory-bank/` and `docs/` directly, and asking the user for confirmation
in chat.

---

## Verification

```bash
# Audit installed state
bash scripts/detect-existing.sh

# Expected: all items 'present' or 'missing' (optional ones).
# 'outdated' or 'pollution' rows indicate cleanup needed.
```

In your agent, run a smoke prompt:

> Read AGENTS.md and describe the 4-phase workflow.

The agent should respond with Phase 0/1/2/3 from
`AGENTS.md` §"Workflow Phases".

---

## How the harness works (refresher)

The harness is NOT an app template. It is a repository-level operating
framework that turns human intent into agent-ready work.

### Core workflow

```
Human intent / product spec
  → Feature Intake (classify risk: tiny / normal / high-risk)
  → Story packet (from templates)
  → Agent work loop (implement + validate)
  → Product delta (code, tests, API)
  → Harness delta (docs, decisions, test matrix)
  → Next intent
```

### Layered tooling (per ADR-0004)

```
L1 Process    →  Harness docs/
L2 Orchestr.  →  AGENTS.md §Workflow Phases + .cursor/rules/harness-mcp-bridge.mdc
L3 Context    →  memory-bank/*.md (dashboards) + .serena/memories/* (pointers)
L4 Knowledge  →  Code graph (e.g., GitNexus) + cross-session memory (e.g., Neural Memory)
L5 Semantic   →  LSP tool (e.g., Serena)
```

Each layer has one role; data has one canonical home. See
[ADR-0004](../decisions/0004-tooling-layer-separation.md) for the SSOT
rule and [ADR-0005](../decisions/0005-workspace-tooling-stack.md) for
the recommended stack.

### Key concepts

- **Feature Intake**: Every prompt goes through `FEATURE_INTAKE.md` for
  risk classification before implementation.
- **Risk Lanes**: tiny (direct patch), normal (story-sized), high-risk
  (needs design + exec plan + human confirmation).
- **Risk Checklist**: 10 flags (auth, authorization, data model, audit,
  external systems, public contracts, cross-platform, existing behavior,
  weak proof, multi-domain). 4+ flags = high-risk.
- **Test Matrix**: Maps product behavior to proof (unit, integration, E2E,
  platform).
- **Decision Records**: Durable records of why important choices were
  made. 3-step write per ADR-0004.
- **Harness Backlog**: Captures friction — when an agent is confused or
  repeats manual reasoning, it logs an improvement proposal.

### Templates

| Template | Path | Use For |
|----------|------|---------|
| Story | `docs/templates/story.md` | Normal story packets |
| Decision | `docs/templates/decision.md` | Architectural decisions |
| Spec Intake | `docs/templates/spec-intake.md` | Processing new specs |
| Validation Report | `docs/templates/validation-report.md` | Validation evidence |
| High-Risk Story | `docs/templates/high-risk-story/` | Complex stories (4 files) |

---

## Notes

- The harness starts with no product implementation — it grows from
  friction.
- Do not scaffold app source folders until a story explicitly moves to
  implementation.
- When a user provides a project spec, decompose it into product docs,
  stories, and decisions — do not maintain a monolithic spec.
- All scripts support `--dry-run` and create `*.bak.<timestamp>` backups
  on destructive operations.
