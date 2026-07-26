# GitNexus x Neural-Memory Bridge -- Setup Guide

## Overview

This guide bootstraps the **Hybrid Brain** workflow for any new project:
- **GitNexus** indexes the codebase into a knowledge graph (hub nodes, clusters, processes)
- **Neural-Memory** stores experiential context (past bugs, decisions, patterns)
- **Bridge Script** connects both systems via a Cursor rule that cross-references them on every code change

## Prerequisites

| Requirement | Check command |
|-------------|---------------|
| Node.js >= 18 | `node -v` |
| Python >= 3.8 | `python --version` |
| Git repo initialized | `git status` |
| Neural-Memory MCP configured | Cursor Settings > MCP > neural-memory |
| GitNexus MCP configured | Cursor Settings > MCP > gitnexus |

## Directory Structure (Target)

After setup, the project should have:

```
<project-root>/
  .cursor/
    rules/
      .global/
        neural-memory-workflow.mdc    # Always-apply: recall/remember lifecycle
        gitnexus-neural-bridge.mdc    # Always-apply: cross-reference workflow
    skills/
      .global/
        gitnexus/
          gitnexus_bridge.py          # Bridge script (shared library)
  memory-bank/
    projectbrief.md                   # Foundation: project goals and scope
    productContext.md                 # Why the project exists, UX goals
    techContext.md                    # Tech stack, dependencies, constraints
    systemPatterns.md                 # Architecture patterns and decisions
    activeContext.md                  # Current work focus and next steps
    progress.md                      # What works, what's left
    decisionLog.md                   # Chronological decision record
    codebaseGraph.md                 # [Auto-generated] GitNexus graph summary
    codebase_graph_summary.json      # [Auto-generated] Machine-readable graph
```

## Shared Library Usage

The bridge script is designed as a **shared library** — one copy can serve multiple
projects. You can either copy it into each project or reference a central copy.

### Option A: Central Copy (Recommended for Multi-Project Workspaces)

Keep one copy at a known location (e.g., a shared `.global/` directory) and
invoke it with `--project-root` to target different projects:

```bash
# From anywhere — target ReviztoTools
python path/to/gitnexus_bridge.py --project-root /path/to/ReviztoTools --repo ReviztoTools

# Target DCMvn_CS
python path/to/gitnexus_bridge.py --project-root /path/to/DCMvn_CS --repo DCMvn_CS

# Target EIRtools
python path/to/gitnexus_bridge.py --project-root /path/to/EIRtools --repo EIRtools
```

### Option B: Programmatic API (from Python scripts)

```python
from gitnexus_bridge import BridgeConfig, run_bridge

# Single project
config = BridgeConfig(
    project_root="/path/to/ReviztoTools",
    repo="ReviztoTools",
)
summary = run_bridge(config)

# Multiple projects in a loop
projects = [
    ("ReviztoTools", "/path/to/ReviztoTools"),
    ("DCMvn_CS", "/path/to/DCMvn_CS"),
    ("EIRtools", "/path/to/EIRtools"),
]
for repo_name, root in projects:
    config = BridgeConfig(project_root=root, repo=repo_name)
    run_bridge(config)
```

### Option C: Custom Output Paths

```python
config = BridgeConfig(
    project_root="/path/to/project",
    repo="MyRepo",
    json_out="/custom/path/summary.json",
    md_out="/custom/path/graph.md",
    port=5000,  # non-default port
)
summary = run_bridge(config)
```

### BridgeConfig Reference

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `project_root` | str/Path | `cwd()` | Project root directory |
| `repo` | str | auto-detect | GitNexus repository name |
| `port` | int | `4747` | GitNexus server port |
| `base_url` | str | `http://127.0.0.1:{port}` | Server URL (overrides port) |
| `top_n_hubs` | int | `15` | Number of hub nodes to extract |
| `json_out` | str | `{project_root}/memory-bank/codebase_graph_summary.json` | JSON output path |
| `md_out` | str | `{project_root}/memory-bank/codebaseGraph.md` | Markdown output path |
| `no_auto_serve` | bool | `False` | Skip auto-starting the server |

## Step-by-Step Setup

### Step 1: Initialize memory-bank

Create the `memory-bank/` directory with 7 core files. Each file has a specific role:

```
mkdir memory-bank
```

**projectbrief.md** -- Foundation document (create first, shapes all others):
```markdown
# Project Brief: <Project Name>

## Purpose
<1-2 sentences: what this project does>

## Core Requirements
- <requirement 1>
- <requirement 2>

## Target Platform
<OS, framework, runtime>

## Source References
<links to specs, designs, or prior art>
```

**productContext.md** -- Why and how:
```markdown
# Product Context: <Project Name>

## Why This Project Exists
<Problem it solves>

## How It Should Work
<User flow summary>

## UX Goals
- <goal 1>
- <goal 2>
```

**techContext.md** -- Stack and constraints:
```markdown
# Tech Context: <Project Name>

## Technology Stack
| Component | Technology | Version |
|-----------|------------|---------|
| Language  | ...        | ...     |
| Framework | ...        | ...     |

## Development Setup
<How to build and run>

## Constraints
- <constraint 1>
```

**systemPatterns.md** -- Architecture:
```markdown
# System Patterns: <Project Name>

## Architecture Overview
<diagram or description>

## Pattern 1: <Name>
<description>
```

**activeContext.md** -- Current state:
```markdown
# Active Context: <Project Name>

## Current State
<what's working now>

## Active Work Focus
- <current task>

## Next Steps
1. <next step>
```

**progress.md** -- Tracking:
```markdown
# Progress: <Project Name>

## Completed
- <done item>

## Remaining
- <todo item>

## Known Issues
- <issue>
```

**decisionLog.md** -- Decisions:
```markdown
# Decision Log: <Project Name>

## DEC-001: <Title>
**Date:** <date>
**Decision:** <what was decided>
**Reason:** <why>
**Alternative:** <what was rejected>
```

### Step 2: Copy Cursor rules

Create `.cursor/rules/.global/` with two always-apply rules:

**neural-memory-workflow.mdc** -- Core recall/remember lifecycle:

```markdown
---
description: Auto-integrate NeuralMemory into every AI interaction
alwaysApply: true
---

# NeuralMemory Workflow

## On Every User Prompt
1. **Recall first** -- `nmem_recall` with keywords from user query
2. **Research** -- search docs/web if needed
3. **Confirm** -- present findings + plan before acting
4. **Act** -- execute after confirmation

## On Bug Fix / Code Change
1. `nmem_remember(type="error")` -- store issue + solution
2. `nmem_remember(type="decision")` -- store architectural choices

## Session Lifecycle
- Start: `nmem_recap(level=2)` then `nmem_session`
- End: `nmem_health`, consolidate if grade < C

## What to Remember
| Type | When |
|------|------|
| error | Bug fixed, exception resolved |
| decision | Tech choice, pattern selection |
| insight | Non-obvious pattern discovered |
| instruction | User preference, coding convention |
| workflow | Multi-step process, deploy procedure |
| todo | Deferred task (auto-expires 30 days) |

## Rules
- Never store secrets or credentials
- Keep content under 200 words
- Always include relevant tags
- Use explicit `type` for critical memories
```

**gitnexus-neural-bridge.mdc** -- Cross-referencing workflow:

```markdown
---
description: Cross-reference GitNexus (code graph) with Neural-Memory before/after code changes
alwaysApply: true
---

# GitNexus x Neural-Memory Bridge

## Hub Node Threshold
A hub node is any symbol with 15+ outgoing connections.
Consult `memory-bank/codebaseGraph.md` for the current hub list.

## Before Modifying Code
1. `nmem_recall("<symbol>")` -- check past experience
2. `gitnexus impact(target="<symbol>", direction="upstream")` -- blast radius
3. Cross-reference both signals into a risk summary
4. If hub node or past issue flagged -- present risk, ask confirmation

## After Code Change
5. `nmem_remember(content="...", tags=["<project>", "hub-node", "blast-radius:<N>"])`
6. `gitnexus detect_changes()` -- verify scope

## Bridge Refresh
After major refactors:
python .cursor/skills/.global/gitnexus/gitnexus_bridge.py --repo <name>
```

### Step 3: Copy the bridge script

Copy `.cursor/skills/.global/gitnexus/gitnexus_bridge.py` from the template project.
The script uses only Python stdlib (no pip install needed).

### Step 4: Index with GitNexus

```bash
# From project root (must be a git repo)
npx gitnexus analyze

# Optional: enable embeddings for semantic search
npx gitnexus analyze --embeddings
```

### Step 5: Run the bridge

```bash
# Auto-manages server lifecycle (recommended):
python .cursor/skills/.global/gitnexus/gitnexus_bridge.py --repo <RepoName>

# Or target a different project from anywhere:
python path/to/gitnexus_bridge.py --project-root /path/to/project --repo <RepoName>
```

This generates:
- `memory-bank/codebase_graph_summary.json`
- `memory-bank/codebaseGraph.md`

### Step 6: Seed Neural-Memory

Open Cursor in the project and ask the agent:

> "Read memory-bank/codebaseGraph.md and seed Neural-Memory with the key insights:
> hub nodes as facts, safety rules as instructions, bridge workflow as workflow."

Or manually call `nmem_remember` for each critical insight.

## Verification Checklist

| # | Check | How to verify |
|---|-------|---------------|
| 1 | Git repo exists | `git status` returns no error |
| 2 | memory-bank/ has 7+ files | `ls memory-bank/*.md` |
| 3 | .cursor/rules/.global/ has 2 bridge rules | Check for `neural-memory-workflow.mdc` and `gitnexus-neural-bridge.mdc` |
| 4 | Bridge script exists | `ls .cursor/skills/.global/gitnexus/gitnexus_bridge.py` |
| 5 | GitNexus index exists | `npx gitnexus status` or `.gitnexus/meta.json` |
| 6 | codebaseGraph.md generated | `ls memory-bank/codebaseGraph.md` |
| 7 | Neural-Memory seeded | `nmem_recall("hub nodes codebase")` returns results |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `npx gitnexus analyze` fails | Ensure you're in a git repo with committed files |
| Bridge script returns 0 hub nodes | Ensure `gitnexus serve` is running on :4747 |
| Cypher queries fail with lock error | MCP and HTTP server share DB lock; bridge uses CLI fallback |
| `nmem_recall` returns nothing | Run `nmem_remember` to seed initial context first |
| `ModuleNotFoundError` when importing | Add script directory to `sys.path` or use `--project-root` CLI |

## Applying to Multiple Repos

For a workspace with multiple repos under one parent (e.g., `DCMvnTools/`):

1. Keep **one copy** of the bridge script in a shared location
2. Use `--project-root` and `--repo` to target each project independently
3. GitNexus indexes all repos independently (`npx gitnexus analyze` in each)
4. Neural-Memory stores per-project tags to separate context
5. Each project gets its own `memory-bank/` for outputs

### Batch Script Example (PowerShell)

```powershell
$bridge = "F:\Digital Team\LongDang\C_RnD\DCMvnTools\ReviztoTools\.cursor\skills\.global\gitnexus\gitnexus_bridge.py"
$projects = @(
    @{ Root = "F:\Digital Team\LongDang\C_RnD\DCMvnTools\ReviztoTools"; Repo = "ReviztoTools" },
    @{ Root = "F:\Digital Team\LongDang\C_RnD\DCMvnTools\DCMvn_CS"; Repo = "DCMvn_CS" }
)

foreach ($p in $projects) {
    Write-Host "`n=== Running bridge for $($p.Repo) ===" -ForegroundColor Cyan
    python $bridge --project-root $p.Root --repo $p.Repo
}
```
