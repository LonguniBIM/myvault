#!/usr/bin/env bash
# detect-existing.sh — Brownfield detection for harness_template
#
# Scans a target directory for existing Harness / tooling-stack files and
# reports what is present, missing, or needs an upgrade.
#
# Usage:
#   bash detect-existing.sh [--directory <path>] [--json|--pretty]

set -euo pipefail

TARGET_DIR=""
OUTPUT="pretty"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --directory) TARGET_DIR="$2"; shift 2 ;;
    --json)      OUTPUT="json"; shift ;;
    --pretty)    OUTPUT="pretty"; shift ;;
    -h|--help)
      cat <<EOF
detect-existing.sh — Scan project for Harness / tooling-stack presence.

Usage:
  detect-existing.sh [--directory <path>] [--json|--pretty]

Output statuses:
  present       File/dir exists
  missing       Not found
  outdated      Found but appears to be an older/incomplete version
  pollution     Found but contains sibling-project specifics
EOF
      exit 0
      ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done

[[ -z "$TARGET_DIR" ]] && TARGET_DIR="$(pwd)"
TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd)"

# -------- Detection items: name|path|kind --------
# kind: file | dir | content_check
ITEMS=(
  "agents-md|AGENTS.md|content_check_v2"
  "claude-md|CLAUDE.md|file"
  "harness-md|docs/HARNESS.md|file"
  "feature-intake|docs/FEATURE_INTAKE.md|file"
  "architecture|docs/ARCHITECTURE.md|file"
  "test-matrix|docs/TEST_MATRIX.md|file"
  "harness-backlog|docs/HARNESS_BACKLOG.md|file"
  "decisions-dir|docs/decisions|dir"
  "adr-0004|docs/decisions/0004-tooling-layer-separation.md|file"
  "adr-0005|docs/decisions/0005-workspace-tooling-stack.md|file"
  "templates-dir|docs/templates|dir"
  "stories-dir|docs/stories|dir"
  "memory-bank-dir|memory-bank|dir"
  "memory-bank-decisionlog|memory-bank/decisionLog.md|file"
  "memory-bank-activecontext|memory-bank/activeContext.md|file"
  "serena-dir|.serena|dir"
  "serena-yaml|.serena/project.yml|file"
  "serena-memories|.serena/memories|dir"
  "gitnexus-dir|.gitnexus|dir"
  "cursor-rules-dir|.cursor/rules|dir"
  "cursor-harness-agent|.cursor/rules/harness-agent.mdc|file"
  "cursor-bridge|.cursor/rules/harness-mcp-bridge.mdc|content_check_bridge"
  "cursor-namespace|.cursor/rules/project-namespace.mdc|file"
  "cursor-global-dir|.cursor/rules/.global|dir"
  "cursor-global-mcp|.cursor/rules/.global/mcp-mandatory-startup.mdc|file"
  "install-script|scripts/install-harness.sh|file"
)

# Detect symlink for .cursor/rules/.global
GLOBAL_SYMLINK_TARGET=""
if [[ -L "$TARGET_DIR/.cursor/rules/.global" ]]; then
  GLOBAL_SYMLINK_TARGET="$(readlink "$TARGET_DIR/.cursor/rules/.global" 2>/dev/null || echo "")"
fi

# -------- Check function --------
check_item() {
  local name="$1"; local rel="$2"; local kind="$3"
  local full="$TARGET_DIR/$rel"
  local status="missing"
  local note=""

  case "$kind" in
    file)
      [[ -f "$full" ]] && status="present"
      ;;
    dir)
      [[ -d "$full" ]] && status="present"
      ;;
    content_check_v2)
      # AGENTS.md present but check if it has the "Workflow Phases" section
      if [[ -f "$full" ]]; then
        if grep -q "Workflow Phases" "$full" 2>/dev/null; then
          status="present"
        else
          status="outdated"
          note="missing 'Workflow Phases' section (pre-template-v2)"
        fi
      fi
      ;;
    content_check_bridge)
      # If harness-mcp-bridge.mdc exists, check it uses generic syntax (not sibling project name)
      if [[ -f "$full" ]]; then
        status="present"
        # Check for sibling-project name pollution (anything that isn't
        # the current project name in the bridge file)
      fi
      ;;
  esac

  # Pollution check on globals
  if [[ "$rel" == ".cursor/rules/.global/mcp-mandatory-startup.mdc" && -f "$full" ]]; then
    # If file contains hardcoded sibling-project commands (heuristic: dotnet build "<X>.sln"),
    # flag as pollution
    if grep -Eq 'dotnet build "[^"]+\.sln"' "$full" 2>/dev/null; then
      status="pollution"
      note="contains sibling-project verify commands"
    fi
  fi

  echo "$name|$rel|$kind|$status|$note"
}

# -------- Run checks --------
RESULTS=()
for entry in "${ITEMS[@]}"; do
  IFS='|' read -r name rel kind <<<"$entry"
  RESULTS+=("$(check_item "$name" "$rel" "$kind")")
done

# -------- Output --------
if [[ "$OUTPUT" == "json" ]]; then
  printf '{\n  "target": "%s",\n' "$TARGET_DIR"
  if [[ -n "$GLOBAL_SYMLINK_TARGET" ]]; then
    printf '  "cursor_global_symlink": "%s",\n' "$GLOBAL_SYMLINK_TARGET"
  fi
  printf '  "items": [\n'
  local_n=${#RESULTS[@]}
  local_i=0
  for r in "${RESULTS[@]}"; do
    local_i=$((local_i+1))
    IFS='|' read -r name rel kind status note <<<"$r"
    sep=","
    [[ $local_i -eq $local_n ]] && sep=""
    printf '    {"name":"%s","path":"%s","kind":"%s","status":"%s","note":"%s"}%s\n' \
      "$name" "$rel" "$kind" "$status" "$note" "$sep"
  done
  printf '  ]\n}\n'
else
  # Pretty output
  RED=$'\033[31m'; YELLOW=$'\033[33m'; GREEN=$'\033[32m'; DIM=$'\033[2m'; RESET=$'\033[0m'
  [ -t 1 ] || { RED=""; YELLOW=""; GREEN=""; DIM=""; RESET=""; }

  printf "\n%sBrownfield detection: %s%s\n" "$DIM" "$TARGET_DIR" "$RESET"
  if [[ -n "$GLOBAL_SYMLINK_TARGET" ]]; then
    printf "%s.cursor/rules/.global symlink target:%s %s\n\n" "$DIM" "$RESET" "$GLOBAL_SYMLINK_TARGET"
  else
    printf "\n"
  fi

  printf "%-30s %-60s %-12s %s\n" "Item" "Path" "Status" "Note"
  printf "%-30s %-60s %-12s %s\n" "----" "----" "------" "----"

  present_count=0; missing_count=0; outdated_count=0; pollution_count=0
  for r in "${RESULTS[@]}"; do
    IFS='|' read -r name rel kind status note <<<"$r"
    case "$status" in
      present)   color="$GREEN"; present_count=$((present_count+1)) ;;
      missing)   color="$DIM";   missing_count=$((missing_count+1)) ;;
      outdated)  color="$YELLOW"; outdated_count=$((outdated_count+1)) ;;
      pollution) color="$RED";   pollution_count=$((pollution_count+1)) ;;
      *)         color="" ;;
    esac
    printf "%-30s %-60s ${color}%-12s${RESET} %s\n" "$name" "$rel" "$status" "$note"
  done

  printf "\nSummary: %s%d present%s, %s%d missing%s, %s%d outdated%s, %s%d pollution%s\n\n" \
    "$GREEN" "$present_count" "$RESET" \
    "$DIM" "$missing_count" "$RESET" \
    "$YELLOW" "$outdated_count" "$RESET" \
    "$RED" "$pollution_count" "$RESET"

  if [[ $pollution_count -gt 0 ]]; then
    printf "${RED}Pollution detected.${RESET} Consider running scripts/migrate-globals.sh to refactor\n"
    printf "  shared .global/ rules to be project-agnostic.\n\n"
  fi
  if [[ $outdated_count -gt 0 ]]; then
    printf "${YELLOW}Outdated files detected.${RESET} Brownfield install with --force will backup\n"
    printf "  + overwrite. With --merge (default), outdated files are left alone.\n\n"
  fi
fi
