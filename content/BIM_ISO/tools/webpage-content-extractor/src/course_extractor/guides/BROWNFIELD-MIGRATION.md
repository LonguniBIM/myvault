# Brownfield Migration Guide

Bring an existing project under harness_template **without** clobbering
its current files. Designed to be safe, dry-run-able, and reversible.

Estimated time: **15-30 minutes** depending on what's already present.

---

## When to use brownfield mode

Use this guide when your project already has any of:

- A `docs/` folder, or `AGENTS.md`, or `CLAUDE.md`.
- A `memory-bank/` or Serena `.serena/` directory.
- Existing `.cursor/rules/*.mdc` files (especially a shared
  `.global/` symlink).
- An older Harness installation (pre-template-v2).

If your project has NONE of these, use the
[Greenfield Quickstart](GREENFIELD-QUICKSTART.md) instead.

---

## Phase A — Audit (read-only)

Always start with a detection scan. This writes nothing.

```bash
cd /path/to/existing-project
bash /path/to/harness_template/scripts/detect-existing.sh
```

Expected output: a table of items with one of four statuses:

| Status | Meaning | Action in install |
|---|---|---|
| **present** | File exists, looks current | Preserved (--merge default) or backed up (--force) |
| **missing** | Not found | Will be installed |
| **outdated** | Found but pre-v2 (e.g., `AGENTS.md` lacks Workflow Phases) | Preserved by default; `--force` to upgrade |
| **pollution** | Carries sibling-project specifics | Add `project-namespace.mdc` to override; consider `migrate-globals.sh` |

Save this output — you'll reference it when planning the install.

### What pollution looks like

```bash
# Example: .cursor/rules/.global/mcp-mandatory-startup.mdc contains
# verify commands for a DIFFERENT project (DCMvn, etc.):
grep -E 'dotnet build "[^"]+\.sln"' .cursor/rules/.global/mcp-mandatory-startup.mdc
```

If that grep returns a match, your global rules carry sibling-project
pollution.

---

## Phase B — Dry-run install

```bash
bash /path/to/harness_template/scripts/install-harness.sh \
  --brownfield --dry-run \
  --project-name "MyExistingProject"
```

Read every `[info] [dry-run] would ...` line. The script will:

- Show which files it would render (with substitution).
- Show which files it would copy.
- Show which files exist and would be **preserved** (default brownfield is
  `--merge`).
- NOT actually write anything.

If anything looks wrong, fix or override (see options below).

---

## Phase C — Real install

Default brownfield behavior is `--merge`: missing files added, existing
files preserved.

```bash
bash /path/to/harness_template/scripts/install-harness.sh \
  --brownfield --project-name "MyExistingProject"
```

The script will:

1. Run an inline detection pass.
2. Prompt for confirmation (skip with `--yes`).
3. Add missing files only.
4. Print a summary + next steps.

### Variants

| Goal | Flag |
|---|---|
| Upgrade outdated files (backup + replace) | `--force` |
| Skip tooling stack (Harness only) | `--skip-tooling` |
| Skip Cursor rules (non-Cursor agent) | `--skip-cursor` |
| Run unattended | `--yes` |

---

## Phase D — Handle pollution (if detected)

If `detect-existing.sh` showed `pollution` status on
`cursor-global-mcp`, your `.global/` rules carry assumptions from
sibling projects. Two options:

### Option D.1 — Override locally (safe, low-risk)

The brownfield install already created `.cursor/rules/project-namespace.mdc`.
Open it and fill in:

- **Override 1** — Neural memory tag (your project's tag).
- **Override 2** — Verify commands (only those that apply to this project).
- **Override 4** — Serena language (default `markdown`; change to real
  stack when applicable).

This file wins over the polluted global for your project. Sibling projects
are unaffected.

### Option D.2 — Refactor the global (opt-in, cross-project)

If you want long-term consistency and have **coordinated with all sibling
projects**, run:

```bash
bash /path/to/harness_template/scripts/migrate-globals.sh \
  --target ./.cursor/rules/.global
# Script will:
#  1. Detect if .global is a symlink (warns about cross-project impact).
#  2. Back up the current global rules.
#  3. Replace with project-agnostic version from stack-templates.
#  4. Print a checklist for sibling projects.
```

After this, **every** project that previously relied on those globals
MUST install its own `project-namespace.mdc`:

```bash
# In each sibling project:
cd /path/to/sibling-project
bash /path/to/harness_template/scripts/install-harness.sh --brownfield --merge --skip-tooling
# Then edit .cursor/rules/project-namespace.mdc for that project's specifics.
```

Track each sibling-project rollout in their respective `HARNESS_BACKLOG.md`.

---

## Phase E — Bootstrap tooling (if not already done)

If `detect-existing.sh` showed `memory-bank/` or `.serena/` as missing:

```bash
bash /path/to/harness_template/scripts/bootstrap-tooling.sh \
  --project-name "MyExistingProject"
```

This is idempotent. Re-run safely.

The script also prints suggested MCP server config — add it to
`~/.cursor/mcp.json` if you haven't already.

---

## Phase F — Verify

Re-run detection:

```bash
bash /path/to/harness_template/scripts/detect-existing.sh
```

Goals:
- 0 missing items (except `cursor-global-dir`, `gitnexus-dir` — both optional).
- 0 pollution (if you ran migrate-globals).
- `outdated` may remain if you didn't `--force`; that's OK if the
  outdated file works for your project.

Run a smoke prompt in your agent:

> Recall what you know about this project. What workflow phases apply,
> and which lane would you use for adding a small feature?

The agent should reference the 4-phase workflow and Feature Intake.

---

## Rollback

All destructive operations create `*.bak.<timestamp>` backups:

```bash
# Find backups
find . -name "*.bak.*" -type f

# Restore a single file
mv path/to/file.bak.20260517123045 path/to/file
```

For `migrate-globals.sh`, the entire previous global directory is at
`.global.bak.<timestamp>/`.

---

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| Agent ignores Workflow Phases | Old `AGENTS.md` doesn't have the section | Re-run with `--force` or manually merge |
| `nmem_remember` uses wrong project tag | `project-namespace.mdc` not installed / empty | Install + fill Override 1 |
| `gitnexus query` fails | Repo not indexed | `cd <project> && npx gitnexus analyze` |
| Two `alwaysApply: true` rules conflict | Old `harness-agent.mdc` still active | Replace with the stub from `stack-templates/cursor-rules/harness-agent.mdc.stub` |
| Sibling project breaks after migrate-globals | That project doesn't have `project-namespace.mdc` yet | Run brownfield install in that project too |

## See also

- [GREENFIELD-QUICKSTART.md](GREENFIELD-QUICKSTART.md) — fresh-project flow.
- [ADR-0004](../decisions/0004-tooling-layer-separation.md) — Layering rule
  (why pollution happens and how to fix structurally).
- [ADR-0005](../decisions/0005-workspace-tooling-stack.md) — Recommended
  tooling stack roles.
- [../HARNESS_BACKLOG.md](../HARNESS_BACKLOG.md) — Where to log friction
  encountered during migration.
