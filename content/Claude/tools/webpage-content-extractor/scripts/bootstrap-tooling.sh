#!/usr/bin/env bash
# bootstrap-tooling.sh — Scaffold tooling-stack files into a project that
# already has Harness docs installed.
#
# Idempotent: safe to re-run; existing files preserved unless --force given.
#
# Usage:
#   bash bootstrap-tooling.sh [--project-name "<name>"] [--force] [--dry-run]
#
# Scaffolds: memory-bank/, .serena/project.yml, .serena/memories/*.md
# Prints:    Suggested ~/.cursor/mcp.json server config block

set -euo pipefail

PROJECT_NAME=""
PROJECT_TAG=""
TARGET_DIR=""
SOURCE_DIR=""
DRY_RUN="no"
FORCE="no"
ASSUME_YES="no"

INSTALL_DATE="$(date -u +%Y-%m-%d)"

# -------- Logging --------
RED=$'\033[31m'; YELLOW=$'\033[33m'; GREEN=$'\033[32m'; BLUE=$'\033[34m'; BOLD=$'\033[1m'; RESET=$'\033[0m'
[ -t 1 ] || { RED=""; YELLOW=""; GREEN=""; BLUE=""; BOLD=""; RESET=""; }
info()  { printf "%s[info]%s %s\n" "$BLUE" "$RESET" "$*"; }
warn()  { printf "%s[warn]%s %s\n" "$YELLOW" "$RESET" "$*" >&2; }
err()   { printf "%s[err]%s  %s\n" "$RED" "$RESET" "$*" >&2; }
ok()    { printf "%s[ok]%s   %s\n" "$GREEN" "$RESET" "$*"; }
step()  { printf "\n%s== %s ==%s\n" "$BOLD" "$*" "$RESET"; }

usage() {
  cat <<'EOF'
bootstrap-tooling.sh — Scaffold tooling stack files for harness_template.

Usage:
  bootstrap-tooling.sh [options]

Options:
  --project-name <name>   Project name (default: basename of --directory)
  --project-tag <tag>     Cross-session memory tag (default: lowercased name)
  --directory <path>      Target directory (default: $PWD)
  --source-dir <path>     Path to harness_template (default: auto-detect)
  --force                 Overwrite existing tooling files (backup first)
  --dry-run               Print actions, don't write
  --yes                   Assume yes for prompts
  --help, -h              This help

Files scaffolded:
  memory-bank/{activeContext,codebaseGraph,decisionLog,productContext,
               progress,projectbrief,systemPatterns,techContext}.md
  .serena/project.yml
  .serena/memories/{project_overview,style_and_conventions,
                    suggested_commands,task_completion_checklist}.md
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project-name) PROJECT_NAME="$2"; shift 2 ;;
    --project-tag)  PROJECT_TAG="$2"; shift 2 ;;
    --directory)    TARGET_DIR="$2"; shift 2 ;;
    --source-dir)   SOURCE_DIR="$2"; shift 2 ;;
    --force)        FORCE="yes"; shift ;;
    --dry-run)      DRY_RUN="yes"; shift ;;
    --yes|-y)       ASSUME_YES="yes"; shift ;;
    -h|--help)      usage; exit 0 ;;
    *) err "Unknown option: $1"; usage; exit 2 ;;
  esac
done

[[ -z "$TARGET_DIR" ]] && TARGET_DIR="$(pwd)"
TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd)"

[[ -z "$PROJECT_NAME" ]] && PROJECT_NAME="$(basename "$TARGET_DIR")"
[[ -z "$PROJECT_TAG" ]] && PROJECT_TAG="$(printf "%s" "$PROJECT_NAME" | tr '[:upper:]' '[:lower:]' | tr -c 'a-z0-9' '-' | sed 's/-\+/-/g; s/^-\|-$//g')"

# Auto-detect SOURCE_DIR
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || echo "")"
if [[ -z "$SOURCE_DIR" && -n "$SCRIPT_DIR" && -d "$SCRIPT_DIR/../stack-templates" ]]; then
  SOURCE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
fi
if [[ -z "$SOURCE_DIR" ]]; then
  err "Could not auto-detect harness_template source dir. Use --source-dir."
  exit 1
fi

do_dry() { [[ "$DRY_RUN" == "yes" ]]; }

render_or_skip() {
  local src="$1"; local dst="$2"
  if [[ -e "$dst" ]]; then
    if [[ "$FORCE" == "yes" ]]; then
      local bak="${dst}.bak.$(date +%Y%m%d%H%M%S)"
      do_dry && info "[dry-run] backup: $dst -> $bak" || { mv "$dst" "$bak"; info "Backed up: $dst -> $bak"; }
    else
      info "Exists (preserved): $dst"
      return 0
    fi
  fi
  if do_dry; then
    info "[dry-run] render: $src -> $dst"
    return 0
  fi
  mkdir -p "$(dirname "$dst")"
  sed \
    -e "s|{{PROJECT_NAME}}|${PROJECT_NAME}|g" \
    -e "s|{{PROJECT_TAG}}|${PROJECT_TAG}|g" \
    -e "s|{{INSTALL_DATE}}|${INSTALL_DATE}|g" \
    "$src" > "$dst"
  ok "Wrote: $dst"
}

copy_or_skip() {
  local src="$1"; local dst="$2"
  if [[ -e "$dst" ]]; then
    if [[ "$FORCE" == "yes" ]]; then
      local bak="${dst}.bak.$(date +%Y%m%d%H%M%S)"
      do_dry && info "[dry-run] backup: $dst -> $bak" || { mv "$dst" "$bak"; info "Backed up: $dst -> $bak"; }
    else
      info "Exists (preserved): $dst"
      return 0
    fi
  fi
  do_dry && { info "[dry-run] copy: $src -> $dst"; return 0; }
  mkdir -p "$(dirname "$dst")"
  cp -p "$src" "$dst"
  ok "Wrote: $dst"
}

step "harness_template bootstrap-tooling"
info "Project: $PROJECT_NAME (tag: $PROJECT_TAG)"
info "Target:  $TARGET_DIR"
info "Source:  $SOURCE_DIR"
[[ "$DRY_RUN" == "yes" ]] && warn "DRY-RUN: no writes"

step "Scaffold memory-bank/"
for f in activeContext codebaseGraph decisionLog productContext progress projectbrief systemPatterns techContext; do
  render_or_skip "$SOURCE_DIR/stack-templates/memory-bank/${f}.md.template" "$TARGET_DIR/memory-bank/${f}.md"
done

step "Scaffold .serena/"
render_or_skip "$SOURCE_DIR/stack-templates/serena/project.yml.template" "$TARGET_DIR/.serena/project.yml"
render_or_skip "$SOURCE_DIR/stack-templates/serena/memories/project_overview.md.template" "$TARGET_DIR/.serena/memories/project_overview.md"
render_or_skip "$SOURCE_DIR/stack-templates/serena/memories/suggested_commands.md.template" "$TARGET_DIR/.serena/memories/suggested_commands.md"
copy_or_skip   "$SOURCE_DIR/stack-templates/serena/memories/style_and_conventions.md" "$TARGET_DIR/.serena/memories/style_and_conventions.md"
copy_or_skip   "$SOURCE_DIR/stack-templates/serena/memories/task_completion_checklist.md" "$TARGET_DIR/.serena/memories/task_completion_checklist.md"

step "Suggested MCP server config"
cat <<EOF
Add this block to your Cursor MCP config (typically ~/.cursor/mcp.json or
the equivalent for your agent runtime). Adjust commands and paths to match
your local MCP server installations.

{
  "mcpServers": {
    "user-serena": {
      "command": "uvx",
      "args": ["serena-mcp-server"]
    },
    "user-neural-memory": {
      "command": "npx",
      "args": ["-y", "neural-memory-mcp"]
    },
    "user-gitnexus": {
      "command": "npx",
      "args": ["-y", "gitnexus-mcp"]
    },
    "user-mcp-feedback-enhanced": {
      "command": "npx",
      "args": ["-y", "mcp-feedback-enhanced"]
    }
  }
}

Then activate Serena for this project (in Cursor):
  CallMcpTool server="user-serena" toolName="activate_project"
              args={ "project": "$TARGET_DIR" }

For GitNexus indexing (if the project has code):
  cd "$TARGET_DIR" && npx gitnexus analyze

EOF

step "Next steps"
cat <<EOF
1. Verify MCP servers are running in your agent (Cursor / Claude CLI / etc.).
2. Open the project; the agent should auto-recall via Phase 0.
3. Edit memory-bank/projectbrief.md and productContext.md with your
   project's purpose once you have a spec.
EOF
