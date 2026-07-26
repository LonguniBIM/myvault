#!/usr/bin/env bash
# migrate-globals.sh — Opt-in refactor of shared .cursor/rules/.global/ rules
# to be project-agnostic.
#
# WARNING: This script touches the shared global rules directory, which may
# be symlinked across MULTIPLE projects. Run only when you're prepared to
# coordinate the change across all sharing projects.
#
# What it does:
#   - Detects .cursor/rules/.global/ (resolving symlink if any)
#   - Backs up the current rules to .global.bak.<timestamp>/
#   - Installs the project-agnostic version from
#     stack-templates/cursor-global/
#   - Reminds you to install project-namespace.mdc in EACH sibling project
#     that previously relied on the polluted global
#
# Usage:
#   bash migrate-globals.sh [--target <path>] [--dry-run] [--yes]

set -euo pipefail

TARGET_GLOBAL=""
DRY_RUN="no"
ASSUME_YES="no"
SOURCE_DIR=""

RED=$'\033[31m'; YELLOW=$'\033[33m'; GREEN=$'\033[32m'; BLUE=$'\033[34m'; BOLD=$'\033[1m'; RESET=$'\033[0m'
[ -t 1 ] || { RED=""; YELLOW=""; GREEN=""; BLUE=""; BOLD=""; RESET=""; }
info()  { printf "%s[info]%s %s\n" "$BLUE" "$RESET" "$*"; }
warn()  { printf "%s[warn]%s %s\n" "$YELLOW" "$RESET" "$*" >&2; }
err()   { printf "%s[err]%s  %s\n" "$RED" "$RESET" "$*" >&2; }
ok()    { printf "%s[ok]%s   %s\n" "$GREEN" "$RESET" "$*"; }
step()  { printf "\n%s== %s ==%s\n" "$BOLD" "$*" "$RESET"; }

usage() {
  cat <<'EOF'
migrate-globals.sh — Refactor shared .global/ Cursor rules to project-agnostic.

Usage:
  migrate-globals.sh [--target <path>] [--dry-run] [--yes]

Options:
  --target <path>   Path to the .global directory (or its symlink). If a
                    symlink is detected, the script resolves to the real
                    location and warns about cross-project impact.
                    Default: ./.cursor/rules/.global
  --dry-run         Print actions, don't write.
  --yes             Skip the cross-project impact confirmation. Use with care.
  --help, -h        This help.

After migration, each project that previously relied on the polluted global
rules MUST install a project-namespace.mdc to declare its own:
  - project name
  - cross-session memory tag
  - validation commands
  - serena language

See docs/decisions/0004-tooling-layer-separation.md for the rationale.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)    TARGET_GLOBAL="$2"; shift 2 ;;
    --source-dir) SOURCE_DIR="$2"; shift 2 ;;
    --dry-run)   DRY_RUN="yes"; shift ;;
    --yes|-y)    ASSUME_YES="yes"; shift ;;
    -h|--help)   usage; exit 0 ;;
    *)           err "Unknown: $1"; usage; exit 2 ;;
  esac
done

[[ -z "$TARGET_GLOBAL" ]] && TARGET_GLOBAL="./.cursor/rules/.global"

# Auto-detect SOURCE_DIR
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || echo "")"
if [[ -z "$SOURCE_DIR" && -n "$SCRIPT_DIR" && -d "$SCRIPT_DIR/../stack-templates/cursor-global" ]]; then
  SOURCE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
fi
if [[ -z "$SOURCE_DIR" ]]; then
  err "Could not auto-detect harness_template source dir. Use --source-dir."
  exit 1
fi

step "Detecting current .global/ location"
RESOLVED_GLOBAL=""
IS_SYMLINK="no"
if [[ -L "$TARGET_GLOBAL" ]]; then
  IS_SYMLINK="yes"
  RESOLVED_GLOBAL="$(readlink -f "$TARGET_GLOBAL" 2>/dev/null || readlink "$TARGET_GLOBAL")"
  warn "Symlink detected: $TARGET_GLOBAL -> $RESOLVED_GLOBAL"
  warn "Changes will affect EVERY project sharing this symlink."
elif [[ -d "$TARGET_GLOBAL" ]]; then
  RESOLVED_GLOBAL="$(cd "$TARGET_GLOBAL" && pwd)"
  info "Real directory: $RESOLVED_GLOBAL"
else
  err "No .global directory or symlink at: $TARGET_GLOBAL"
  err "Nothing to migrate. Exiting."
  exit 0
fi

step "Cross-project impact"
cat <<EOF
The following file will be replaced with the project-agnostic version
from harness_template:

  $RESOLVED_GLOBAL/mcp-mandatory-startup.mdc

The current file may contain commands or tags specific to a single
sibling project. After this migration, EACH sibling project must install
its own .cursor/rules/project-namespace.mdc (provided by harness_template's
install-harness.sh) to restate those specifics.

If any sibling project is mid-flight, coordinate the change with its
maintainer first.
EOF

if [[ "$ASSUME_YES" != "yes" && "$DRY_RUN" != "yes" ]]; then
  read -r -p "Continue with migration? Type 'yes' to confirm: " ans </dev/tty || ans=""
  if [[ "$ans" != "yes" ]]; then
    err "Aborted by user"
    exit 1
  fi
fi

step "Backup current rules"
BACKUP_DIR="${RESOLVED_GLOBAL}.bak.$(date +%Y%m%d%H%M%S)"
if [[ "$DRY_RUN" == "yes" ]]; then
  info "[dry-run] would backup: $RESOLVED_GLOBAL -> $BACKUP_DIR"
else
  cp -a "$RESOLVED_GLOBAL" "$BACKUP_DIR"
  ok "Backed up to: $BACKUP_DIR"
fi

step "Install project-agnostic mcp-mandatory-startup.mdc"
SRC="$SOURCE_DIR/stack-templates/cursor-global/mcp-mandatory-startup.mdc"
DST="$RESOLVED_GLOBAL/mcp-mandatory-startup.mdc"
if [[ "$DRY_RUN" == "yes" ]]; then
  info "[dry-run] would copy: $SRC -> $DST"
else
  cp -p "$SRC" "$DST"
  ok "Replaced: $DST"
fi

step "Next steps (post-migration checklist)"
cat <<EOF
${BOLD}For EACH project that previously used these globals:${RESET}

  1. cd to that project's root.
  2. Run: bash <harness_template>/scripts/install-harness.sh --brownfield --merge
     (this adds project-namespace.mdc without touching existing files)
  3. Open the new .cursor/rules/project-namespace.mdc and fill in:
     - Override 1: Neural memory tag (per-project)
     - Override 2: Verify commands (if the project has a build/test stack)
     - Override 4: Serena language (if not markdown)
  4. Test by running an agent prompt and verifying the agent uses the
     project's own tag (not a sibling's).

${BOLD}Rollback:${RESET}
  If issues arise, restore from $BACKUP_DIR:
    rm -rf "$RESOLVED_GLOBAL" && cp -a "$BACKUP_DIR" "$RESOLVED_GLOBAL"

EOF

if [[ "$IS_SYMLINK" == "yes" ]]; then
  warn "Remember: the symlinked global is now project-agnostic. Every"
  warn "project relying on it MUST install project-namespace.mdc to be"
  warn "fully functional. Track this in each project's HARNESS_BACKLOG.md."
fi
