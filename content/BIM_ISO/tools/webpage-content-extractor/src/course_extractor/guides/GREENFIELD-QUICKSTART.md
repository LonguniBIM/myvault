# Greenfield Quickstart

Start a brand-new project with Harness v0 and the full tooling stack
(Serena + Memory-Bank + GitNexus + Neural Memory).

Estimated time: **5 minutes**.

---

## Prerequisites

- Git installed.
- Bash (Git Bash works on Windows; native on macOS/Linux/WSL).
- (Optional but recommended) An agent with MCP support: Cursor IDE,
  Claude Code, or similar.

## Step 1 — Clone the template

```bash
# Pick a name for your project
PROJECT="my-new-project"

# Clone harness_template
git clone https://github.com/LonguniBIM/harness_template "$PROJECT"
cd "$PROJECT"

# Reset to a fresh git history
rm -rf .git
git init -b main
```

## Step 2 — Run the installer

```bash
bash scripts/install-harness.sh --greenfield --project-name "$PROJECT"
```

This will:

1. Render `CLAUDE.md` from the `.template` with your project name.
2. Copy all Harness docs (`AGENTS.md`, `docs/HARNESS.md`, ADRs, templates).
3. Scaffold `memory-bank/` with 8 context dashboard files.
4. Scaffold `.serena/project.yml` and 4 Serena memory pointers.
5. Install `.cursor/rules/harness-mcp-bridge.mdc` and `project-namespace.mdc`.
6. Install `.gitignore` (if absent).

Add `--dry-run` to preview without writing.

## Step 3 — Install MCP servers (optional but recommended)

The harness works without MCP tools, but they unlock the full 4-phase
workflow. The installer prints a suggested config block. To re-print:

```bash
bash scripts/bootstrap-tooling.sh --dry-run
```

Add the printed JSON block to your agent's MCP config (e.g.,
`~/.cursor/mcp.json`). Verify with:

```bash
# In a Cursor chat:
CallMcpTool server="user-serena" toolName="activate_project"
            args={ "project": "<absolute path to your project>" }
```

## Step 4 — Verify

```bash
bash scripts/detect-existing.sh
```

You should see all items as **present** (except `cursor-global-dir` and
`gitnexus-dir`, which are optional).

## Step 5 — Commit

```bash
git add .
git commit -m "feat: initialize $PROJECT with harness_template"
```

(Optional) push to GitHub:

```bash
gh repo create "$PROJECT" --public --source . --push
```

See [GITHUB-PUBLISH-GUIDE.md](GITHUB-PUBLISH-GUIDE.md) for full publish
options.

## Step 6 — First task

Open the project in your agent. Ask:

> Read `AGENTS.md` and `docs/HARNESS.md`. Then propose what to do for our
> first spec ingestion.

The agent should:
- Read AGENTS.md → understand the 4-phase workflow.
- Recall (Phase 0) cross-session memory (likely empty on first run).
- Ask for the spec (Phase 1).
- Use `docs/FEATURE_INTAKE.md` to classify it.

## Common adjustments

### Change project name later

Edit:
- `CLAUDE.md` (project name line)
- `memory-bank/*.md` (project name in each file)
- `.serena/project.yml` (`project_name:` field)
- `.cursor/rules/project-namespace.mdc`

Or re-run with `--force`:
```bash
bash scripts/install-harness.sh --greenfield --project-name "NewName" --force
```

### Skip tooling (Harness only, no MCP)

```bash
bash scripts/install-harness.sh --greenfield --project-name "$PROJECT" \
  --skip-tooling --skip-cursor
```

This installs only `docs/`, `CLAUDE.md`, and `AGENTS.md`. Useful for
doc-only or non-Cursor environments.

### Multi-language stack

After picking a stack (in a story or ADR), edit `.serena/project.yml`:
```yaml
languages:
- python
- typescript
```

Then re-run Serena `activate_project` for the change to take effect.

## Where to go next

- [AGENTS.md](../../AGENTS.md) — Agent operating guide.
- [docs/HARNESS.md](../HARNESS.md) — Operating model.
- [docs/FEATURE_INTAKE.md](../FEATURE_INTAKE.md) — Request classification.
- [ADR-0004](../decisions/0004-tooling-layer-separation.md) — Why each
  tooling layer has one job.
- [ADR-0005](../decisions/0005-workspace-tooling-stack.md) — Recommended
  tooling stack.
