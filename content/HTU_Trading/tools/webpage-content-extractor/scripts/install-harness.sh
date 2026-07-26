#!/usr/bin/env bash
# install-harness.sh — Greenfield + Brownfield installer for harness_template
#
# Supports two modes:
#   --greenfield    Fresh install of Harness v0 + tooling stack into an empty
#                   (or near-empty) project.
#   --brownfield    Detect-and-adapt install into a project with existing
#                   harness/tooling files. Interactive, with dry-run support.
#
# Usage:
#   bash install-harness.sh --greenfield --project-name "MyProject"
#   bash install-harness.sh --brownfield [--dry-run] [--yes]
#
# See docs/guides/GREENFIELD-QUICKSTART.md and BROWNFIELD-MIGRATION.md.

set -euo pipefail

# -------- Defaults --------
MODE=""
PROJECT_NAME=""
PROJECT_TAG=""
TARGET_DIR=""
SOURCE_DIR=""
SOURCE_URL="${HARNESS_SOURCE_BASE_URL:-https://raw.githubusercontent.com/LonguniBIM/harness_template/main}"
DRY_RUN="no"
ASSUME_YES="no"
FORCE="no"
MERGE_ONLY="no"
SKIP_TOOLING="no"
SKIP_CURSOR="no"
INSTALL_DATE="$(date -u +%Y-%m-%d)"

# -------- Logging helpers --------
RED=$'\033[31m'; YELLOW=$'\033[33m'; GREEN=$'\033[32m'; BLUE=$'\033[34m'; BOLD=$'\033[1m'; RESET=$'\033[0m'
[ -t 1 ] || { RED=""; YELLOW=""; GREEN=""; BLUE=""; BOLD=""; RESET=""; }

log()   { printf "%s\n" "$*"; }
info()  { printf "%s[info]%s %s\n" "$BLUE" "$RESET" "$*"; }
warn()  { printf "%s[warn]%s %s\n" "$YELLOW" "$RESET" "$*" >&2; }
err()   { printf "%s[err]%s  %s\n" "$RED" "$RESET" "$*" >&2; }
ok()    { printf "%s[ok]%s   %s\n" "$GREEN" "$RESET" "$*"; }
step()  { printf "\n%s== %s ==%s\n" "$BOLD" "$*" "$RESET"; }

usage() {
  cat <<'EOF'
install-harness.sh — Install Harness v0 + tooling stack into a project.

USAGE:
  install-harness.sh --greenfield --project-name <name> [options]
  install-harness.sh --brownfield [options]

MODES:
  --greenfield        Fresh install. Fails on conflict unless --force given.
  --brownfield        Detect existing, prompt interactively. Use --dry-run first.

OPTIONS:
  --project-name <name>   Project name (used for {{PROJECT_NAME}} substitution).
                          Default: basename of target directory.
  --project-tag <tag>     Cross-session memory namespace tag.
                          Default: lowercased project name.
  --directory <path>      Target directory. Default: current directory.
  --source-dir <path>     Path to harness_template repo. Default: auto-detect
                          from script location.
  --source-url <url>      Remote raw URL base (for piped curl installs).
                          Default: https://raw.githubusercontent.com/LonguniBIM/harness_template/main
  --dry-run               Print actions without writing.
  --yes                   Assume yes for all interactive prompts.
  --force | --override    Overwrite conflicts (backs up *.bak.<timestamp>).
  --merge                 Add missing files only; leave existing untouched.
  --skip-tooling          Don't scaffold memory-bank/, .serena/.
  --skip-cursor           Don't install .cursor/rules/.
  --help, -h              Print this help.

EXAMPLES:
  # Greenfield, current directory
  install-harness.sh --greenfield --project-name "MyApp"

  # Brownfield dry-run
  install-harness.sh --brownfield --dry-run

  # Greenfield from remote (piped)
  curl -fsSL https://raw.githubusercontent.com/LonguniBIM/harness_template/main/scripts/install-harness.sh \
    | bash -s -- --greenfield --project-name "MyApp" --yes
EOF
}

# -------- Argument parsing --------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --greenfield)      MODE="greenfield"; shift ;;
    --brownfield)      MODE="brownfield"; shift ;;
    --project-name)    PROJECT_NAME="$2"; shift 2 ;;
    --project-tag)     PROJECT_TAG="$2"; shift 2 ;;
    --directory)       TARGET_DIR="$2"; shift 2 ;;
    --source-dir)      SOURCE_DIR="$2"; shift 2 ;;
    --source-url)      SOURCE_URL="$2"; shift 2 ;;
    --dry-run)         DRY_RUN="yes"; shift ;;
    --yes|-y)          ASSUME_YES="yes"; shift ;;
    --force|--override) FORCE="yes"; shift ;;
    --merge)           MERGE_ONLY="yes"; shift ;;
    --skip-tooling)    SKIP_TOOLING="yes"; shift ;;
    --skip-cursor)     SKIP_CURSOR="yes"; shift ;;
    -h|--help)         usage; exit 0 ;;
    *)                 err "Unknown option: $1"; usage; exit 2 ;;
  esac
done

# -------- Resolve mode --------
if [[ -z "$MODE" ]]; then
  err "Mode required: --greenfield or --brownfield"
  usage
  exit 2
fi

# -------- Resolve TARGET_DIR --------
if [[ -z "$TARGET_DIR" ]]; then
  TARGET_DIR="$(pwd)"
fi
TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd || echo "$TARGET_DIR")"

# -------- Resolve PROJECT_NAME / PROJECT_TAG --------
if [[ -z "$PROJECT_NAME" ]]; then
  PROJECT_NAME="$(basename "$TARGET_DIR")"
  info "Auto-detected project name: $PROJECT_NAME"
fi
if [[ -z "$PROJECT_TAG" ]]; then
  PROJECT_TAG="$(printf "%s" "$PROJECT_NAME" | tr '[:upper:]' '[:lower:]' | tr -c 'a-z0-9' '-' | sed 's/-\+/-/g; s/^-\|-$//g')"
  info "Auto-derived project tag: $PROJECT_TAG"
fi

# -------- Resolve SOURCE_DIR --------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || echo "")"
if [[ -z "$SOURCE_DIR" ]]; then
  if [[ -n "$SCRIPT_DIR" && -f "$SCRIPT_DIR/../AGENTS.md" ]]; then
    SOURCE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
    info "Auto-detected source dir: $SOURCE_DIR"
  fi
fi
USE_REMOTE="no"
if [[ -z "$SOURCE_DIR" ]]; then
  USE_REMOTE="yes"
  info "No local source dir; will fetch files from: $SOURCE_URL"
fi

# -------- Helpers --------
abs_path()  { (cd "$1" 2>/dev/null && pwd) || echo "$1"; }

do_dry()    { [[ "$DRY_RUN" == "yes" ]]; }

confirm() {
  local prompt="$1"
  if [[ "$ASSUME_YES" == "yes" ]]; then return 0; fi
  read -r -p "$prompt [y/N] " ans </dev/tty || ans=""
  [[ "$ans" =~ ^[Yy]$ ]]
}

backup_if_exists() {
  local p="$1"
  if [[ -e "$p" ]]; then
    local bak="${p}.bak.$(date +%Y%m%d%H%M%S)"
    if do_dry; then
      info "[dry-run] would backup: $p -> $bak"
    else
      mv "$p" "$bak"
      info "Backed up: $p -> $bak"
    fi
  fi
}

# Substitute {{PROJECT_NAME}}, {{PROJECT_TAG}}, {{INSTALL_DATE}}
render_template() {
  local input="$1"
  local output="$2"
  if do_dry; then
    info "[dry-run] would render: $output"
    return 0
  fi
  mkdir -p "$(dirname "$output")"
  sed \
    -e "s|{{PROJECT_NAME}}|${PROJECT_NAME}|g" \
    -e "s|{{PROJECT_TAG}}|${PROJECT_TAG}|g" \
    -e "s|{{INSTALL_DATE}}|${INSTALL_DATE}|g" \
    "$input" > "$output"
}

copy_file() {
  local src="$1"; local dst="$2"
  if do_dry; then
    info "[dry-run] would copy: $src -> $dst"
    return 0
  fi
  mkdir -p "$(dirname "$dst")"
  cp -p "$src" "$dst"
}

# Fetch file from remote (when SOURCE_DIR is unavailable)
fetch_remote() {
  local rel="$1"; local out="$2"
  if do_dry; then
    info "[dry-run] would fetch: $SOURCE_URL/$rel -> $out"
    return 0
  fi
  mkdir -p "$(dirname "$out")"
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$SOURCE_URL/$rel" -o "$out"
  elif command -v wget >/dev/null 2>&1; then
    wget -qO "$out" "$SOURCE_URL/$rel"
  else
    err "Neither curl nor wget available; cannot fetch remote source"
    exit 1
  fi
}

# Provision a single file: copy/render template; handle conflicts per mode.
# Args: src_rel (relative under SOURCE_DIR), dst_path, [is_template=yes|no]
provision_file() {
  local src_rel="$1"; local dst="$2"; local is_template="${3:-no}"
  local tmp=""
  local src=""

  if [[ -e "$dst" ]]; then
    if [[ "$MERGE_ONLY" == "yes" ]]; then
      info "Exists (merge mode, skip): $dst"
      return 0
    fi
    if [[ "$MODE" == "greenfield" && "$FORCE" != "yes" ]]; then
      err "Conflict (greenfield, no --force): $dst already exists"
      err "Hint: run with --force to backup-and-overwrite, or --merge to skip existing"
      exit 1
    fi
    backup_if_exists "$dst"
  fi

  if [[ "$USE_REMOTE" == "yes" ]]; then
    tmp="$(mktemp)"
    fetch_remote "$src_rel" "$tmp"
    src="$tmp"
  else
    src="$SOURCE_DIR/$src_rel"
    if [[ ! -f "$src" ]]; then
      warn "Source missing: $src_rel — skipped"
      return 0
    fi
  fi

  if [[ "$is_template" == "yes" ]]; then
    render_template "$src" "$dst"
  else
    copy_file "$src" "$dst"
  fi
  if [[ -n "$tmp" ]]; then rm -f "$tmp"; fi
  return 0
}

# -------- Greenfield-only conflict check --------
greenfield_conflict_check() {
  local conflicts=()
  for p in AGENTS.md CLAUDE.md docs/HARNESS.md memory-bank .serena .cursor/rules/harness-mcp-bridge.mdc; do
    [[ -e "$TARGET_DIR/$p" ]] && conflicts+=("$p")
  done
  if [[ ${#conflicts[@]} -gt 0 ]]; then
    if [[ "$FORCE" == "yes" ]]; then
      warn "Greenfield --force: existing files will be backed up:"
      printf "  - %s\n" "${conflicts[@]}" >&2
    elif [[ "$MERGE_ONLY" == "yes" ]]; then
      info "Greenfield --merge: existing files preserved:"
      printf "  - %s\n" "${conflicts[@]}"
    else
      err "Greenfield mode: target has existing harness/tooling files."
      printf "  - %s\n" "${conflicts[@]}" >&2
      err "Use --brownfield mode, or pass --force / --merge."
      exit 1
    fi
  fi
}

# -------- Section: Harness docs --------
install_harness_docs() {
  step "Installing Harness docs"
  local files=(
    "AGENTS.md|yes"
    "docs/HARNESS.md|no"
    "docs/FEATURE_INTAKE.md|no"
    "docs/ARCHITECTURE.md|no"
    "docs/TEST_MATRIX.md|no"
    "docs/GLOSSARY.md|no"
    "docs/HARNESS_BACKLOG.md|no"
    "docs/README.md|no"
    "docs/decisions/0001-harness-first-development.md|no"
    "docs/decisions/0002-post-spec-product-lifecycle.md|no"
    "docs/decisions/0003-generic-spec-intake-harness.md|no"
    "docs/decisions/0004-tooling-layer-separation.md|no"
    "docs/decisions/0005-workspace-tooling-stack.md|no"
    "docs/decisions/README.md|no"
    "docs/templates/story.md|no"
    "docs/templates/decision.md|no"
    "docs/templates/spec-intake.md|no"
    "docs/templates/validation-report.md|no"
    "docs/templates/high-risk-story/design.md|no"
    "docs/templates/high-risk-story/execplan.md|no"
    "docs/templates/high-risk-story/overview.md|no"
    "docs/templates/high-risk-story/validation.md|no"
    "docs/stories/README.md|no"
    "docs/stories/backlog.md|no"
    "docs/stories/epics/README.md|no"
    "docs/product/README.md|no"
    "docs/demo/README.md|no"
    "docs/guides/HARNESS-SETUP-GUIDE.md|no"
    "docs/guides/GITHUB-PUBLISH-GUIDE.md|no"
    "docs/guides/GREENFIELD-QUICKSTART.md|no"
    "docs/guides/BROWNFIELD-MIGRATION.md|no"
    "scripts/README.md|no"
    "scripts/install-harness.sh|no"
    "scripts/bootstrap-tooling.sh|no"
    "scripts/detect-existing.sh|no"
    "scripts/migrate-globals.sh|no"
  )
  # CLAUDE.md is rendered from a template
  provision_file "CLAUDE.md.template" "$TARGET_DIR/CLAUDE.md" "yes"
  local entry rel is_t
  for entry in "${files[@]}"; do
    rel="${entry%|*}"
    is_t="${entry##*|}"
    provision_file "$rel" "$TARGET_DIR/$rel" "$is_t"
  done
  ok "Harness docs installed"
}

# -------- Section: stack-templates → memory-bank + .serena --------
install_tooling_stack() {
  if [[ "$SKIP_TOOLING" == "yes" ]]; then
    info "Skipping tooling stack (--skip-tooling)"
    return 0
  fi
  step "Scaffolding tooling stack (memory-bank/, .serena/)"

  local mb_files=(activeContext codebaseGraph decisionLog productContext progress projectbrief systemPatterns techContext)
  local f
  for f in "${mb_files[@]}"; do
    provision_file "stack-templates/memory-bank/${f}.md.template" \
                   "$TARGET_DIR/memory-bank/${f}.md" "yes"
  done

  provision_file "stack-templates/serena/project.yml.template" \
                 "$TARGET_DIR/.serena/project.yml" "yes"

  local serena_mem=(project_overview suggested_commands)
  for f in "${serena_mem[@]}"; do
    provision_file "stack-templates/serena/memories/${f}.md.template" \
                   "$TARGET_DIR/.serena/memories/${f}.md" "yes"
  done
  # Non-templated Serena memories
  provision_file "stack-templates/serena/memories/style_and_conventions.md" \
                 "$TARGET_DIR/.serena/memories/style_and_conventions.md" "no"
  provision_file "stack-templates/serena/memories/task_completion_checklist.md" \
                 "$TARGET_DIR/.serena/memories/task_completion_checklist.md" "no"

  ok "Tooling stack scaffolded"
}

# -------- Section: .cursor/rules --------
install_cursor_rules() {
  if [[ "$SKIP_CURSOR" == "yes" ]]; then
    info "Skipping Cursor rules (--skip-cursor)"
    return 0
  fi
  step "Installing Cursor rules"
  provision_file "stack-templates/cursor-rules/harness-mcp-bridge.mdc.template" \
                 "$TARGET_DIR/.cursor/rules/harness-mcp-bridge.mdc" "yes"
  provision_file "stack-templates/cursor-rules/project-namespace.mdc.template" \
                 "$TARGET_DIR/.cursor/rules/project-namespace.mdc" "yes"
  provision_file "stack-templates/cursor-rules/harness-agent.mdc.stub" \
                 "$TARGET_DIR/.cursor/rules/harness-agent.mdc" "no"
  ok "Cursor rules installed"
}

# -------- Section: ignore files --------
install_ignore_files() {
  step "Installing .gitignore / .gitnexusignore / .cursorindexingignore"
  # Only install if not present (these often pre-exist with custom content)
  for entry in ".gitignore|no" ".gitnexusignore|no" ".cursorindexingignore|no"; do
    rel="${entry%|*}"; is_t="${entry##*|}"
    if [[ -e "$TARGET_DIR/$rel" ]]; then
      info "Exists (preserved): $rel — review manually to ensure tooling state dirs ignored"
    else
      provision_file "$rel" "$TARGET_DIR/$rel" "$is_t"
    fi
  done
}

# -------- Main flow --------
step "harness_template installer"
log "Mode:         $MODE"
log "Target:       $TARGET_DIR"
log "Project:      $PROJECT_NAME (tag: $PROJECT_TAG)"
log "Source:       ${SOURCE_DIR:-$SOURCE_URL (remote)}"
log "Dry-run:      $DRY_RUN"
log "Force:        $FORCE   Merge-only: $MERGE_ONLY"
log "Skip tooling: $SKIP_TOOLING   Skip cursor: $SKIP_CURSOR"
log ""

if [[ "$MODE" == "greenfield" ]]; then
  greenfield_conflict_check
  if [[ "$DRY_RUN" != "yes" ]]; then
    if ! confirm "Proceed with greenfield install?"; then
      err "Aborted by user"; exit 1
    fi
  fi
fi

if [[ "$MODE" == "brownfield" ]]; then
  step "Brownfield detection"
  if [[ -n "$SCRIPT_DIR" && -x "$SCRIPT_DIR/detect-existing.sh" ]]; then
    "$SCRIPT_DIR/detect-existing.sh" --directory "$TARGET_DIR" --pretty || true
  else
    warn "detect-existing.sh not found locally; using simple file-presence checks"
    for p in AGENTS.md docs/HARNESS.md memory-bank .serena .cursor/rules; do
      if [[ -e "$TARGET_DIR/$p" ]]; then
        info "Found existing: $p"
      else
        info "Missing: $p (will install)"
      fi
    done
  fi
  if [[ "$DRY_RUN" != "yes" ]]; then
    if ! confirm "Proceed with brownfield install? (existing files will be backed up if --force, or skipped if --merge)"; then
      err "Aborted by user"; exit 1
    fi
  fi
  # In brownfield, default to merge unless --force given
  if [[ "$FORCE" != "yes" && "$MERGE_ONLY" != "yes" ]]; then
    info "Brownfield default: --merge (existing files preserved). Use --force to overwrite."
    MERGE_ONLY="yes"
  fi
fi

install_harness_docs
install_tooling_stack
install_cursor_rules
install_ignore_files

# -------- Summary --------
step "Install summary"
log "Project name: ${BOLD}$PROJECT_NAME${RESET}"
log "Project tag:  ${BOLD}$PROJECT_TAG${RESET}"
log "Target:       $TARGET_DIR"
if [[ "$DRY_RUN" == "yes" ]]; then
  warn "DRY-RUN: no files were written. Re-run without --dry-run to apply."
else
  ok "Installation complete."
  log ""
  log "${BOLD}Next steps:${RESET}"
  log "  1) Review docs/decisions/0004-tooling-layer-separation.md and"
  log "     0005-workspace-tooling-stack.md for the integration model."
  log "  2) (Optional) Run scripts/bootstrap-tooling.sh to register Serena project."
  log "  3) (Optional, brownfield only) If sibling-project pollution exists in"
  log "     .cursor/rules/.global/, run scripts/migrate-globals.sh."
  log "  4) Commit changes: git add . && git commit -m 'chore: install harness_template'"
fi
