# Scripts

Installation and bootstrap automation for harness_template.

## Scripts at a glance

| Script | When to run | What it does |
|---|---|---|
| `install-harness.sh` | Once per project, on adoption | Installs Harness docs + tooling stack + Cursor rules. Greenfield/brownfield modes. |
| `bootstrap-tooling.sh` | When tooling-stack files are missing in a project that already has Harness docs | Idempotent scaffold of `memory-bank/`, `.serena/`. Prints MCP config block. |
| `detect-existing.sh` | Before a brownfield install (or to audit a project's state) | Reports presence / absence / outdated-ness / pollution. JSON or pretty output. |
| `migrate-globals.sh` | Opt-in, only when shared `.cursor/rules/.global/` carries sibling-project pollution | Backs up + replaces with project-agnostic version. Requires per-project `project-namespace.mdc` afterwards. |

## Quick examples

### Greenfield (new project)

```bash
git clone https://github.com/LonguniBIM/harness_template my-new-project
cd my-new-project
rm -rf .git && git init -b main
bash scripts/install-harness.sh --greenfield --project-name "MyProject"
```

### Brownfield (existing project)

```bash
cd existing-project
bash <harness_template>/scripts/detect-existing.sh             # audit first
bash <harness_template>/scripts/install-harness.sh --brownfield --dry-run
# Review, then re-run without --dry-run:
bash <harness_template>/scripts/install-harness.sh --brownfield
```

### Add tooling stack to a project that already has Harness docs

```bash
cd my-project
bash <harness_template>/scripts/bootstrap-tooling.sh
```

### Refactor shared globals (cross-project consistency)

```bash
bash <harness_template>/scripts/migrate-globals.sh --target ./.cursor/rules/.global
# Then in EACH sibling project:
bash <harness_template>/scripts/install-harness.sh --brownfield --merge
```

## Conventions

- All scripts are Bash (no Python required).
- All scripts support `--dry-run` to print actions without writing.
- All destructive operations create a `*.bak.<timestamp>` backup.
- All scripts can be piped via `curl | bash` for one-line installs.

See [../docs/guides/GREENFIELD-QUICKSTART.md](../docs/guides/GREENFIELD-QUICKSTART.md)
and [../docs/guides/BROWNFIELD-MIGRATION.md](../docs/guides/BROWNFIELD-MIGRATION.md)
for end-to-end walkthroughs.
