"""
GitNexus x Neural-Memory Bridge Script
=======================================
Extracts structural insights from a GitNexus knowledge graph and outputs:
  1. memory-bank/codebase_graph_summary.json  -- machine-readable Bridge Schema
  2. memory-bank/codebaseGraph.md -- human-readable Memory-Bank page

Uses a hybrid strategy:
  - HTTP API  for metadata endpoints (repos, clusters, processes)
  - CLI subprocess (`npx gitnexus cypher`) for graph queries
    (avoids LadybugDB lock conflicts when MCP server is active)

Server lifecycle:
  - Automatically checks if `gitnexus serve` is running on the target port
  - If not running, starts it as a background subprocess and waits for readiness
  - Stops the server after bridge completes (only if this script started it)

Requirements:
  - `npx gitnexus` available on PATH (for both `serve` and `cypher`)
  - Python 3.8+  (stdlib only, no pip install needed)

Library usage:
  from gitnexus_bridge import BridgeConfig, run_bridge

  config = BridgeConfig(project_root="/path/to/project", repo="MyRepo")
  summary = run_bridge(config)

CLI usage (run from project root, or pass --project-root):
  python gitnexus_bridge.py
  python gitnexus_bridge.py --repo EIRtools
  python gitnexus_bridge.py --project-root /path/to/project
  python gitnexus_bridge.py --port 5000
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
DEFAULT_PORT = 4747
HUB_THRESHOLD = 15
TOP_N_HUBS = 15
SERVER_STARTUP_TIMEOUT = 30
SERVER_POLL_INTERVAL = 0.5

RISK_LEVELS = {
    range(0, 10): "LOW",
    range(10, 20): "MEDIUM",
    range(20, 30): "HIGH",
    range(30, 9999): "CRITICAL",
}

SCRIPT_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
@dataclass
class BridgeConfig:
    """All settings for a bridge run. Eliminates module-level globals."""

    project_root: str | Path = ""
    repo: str = ""
    port: int = DEFAULT_PORT
    base_url: str = ""
    top_n_hubs: int = TOP_N_HUBS
    json_out: str = ""
    md_out: str = ""
    no_auto_serve: bool = False

    def __post_init__(self) -> None:
        if not self.project_root:
            self.project_root = Path.cwd()
        self.project_root = Path(self.project_root).resolve()

        if not self.base_url:
            self.base_url = f"http://127.0.0.1:{self.port}"
        self.base_url = self.base_url.rstrip("/")

        if not self.json_out:
            self.json_out = str(
                self.project_root / "memory-bank" / "codebase_graph_summary.json"
            )
        if not self.md_out:
            self.md_out = str(
                self.project_root / "memory-bank" / "codebaseGraph.md"
            )


# ---------------------------------------------------------------------------
# Server lifecycle (context manager)
# ---------------------------------------------------------------------------
def _is_server_running(base_url: str) -> bool:
    """Check if GitNexus HTTP server is reachable."""
    try:
        req = urllib.request.Request(
            f"{base_url}/api/repos", headers={"Accept": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except (urllib.error.URLError, OSError):
        return False


def _start_server(port: int, cwd: Path) -> subprocess.Popen:
    """Start `npx gitnexus serve` as a background process."""
    cmd = f"npx gitnexus serve --port {port}"
    print(f"[INFO] Starting GitNexus server: {cmd}")

    proc = subprocess.Popen(
        cmd,
        shell=True,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc


def _wait_for_server(base_url: str, timeout: float = SERVER_STARTUP_TIMEOUT) -> bool:
    """Poll until the server responds or timeout expires."""
    deadline = time.time() + timeout
    attempt = 0
    while time.time() < deadline:
        attempt += 1
        if _is_server_running(base_url):
            print(f"[OK]   Server ready after {attempt} poll(s)")
            return True
        time.sleep(SERVER_POLL_INTERVAL)
    return False


def _stop_server(proc: subprocess.Popen) -> None:
    """Gracefully terminate the server process."""
    if proc.poll() is not None:
        return
    print("[INFO] Stopping GitNexus server...")
    try:
        proc.terminate()
        proc.wait(timeout=5)
        print("[OK]   Server stopped gracefully")
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        print("[OK]   Server stopped (killed)")
    except OSError:
        pass


@contextmanager
def managed_server(config: BridgeConfig) -> Iterator[None]:
    """Context manager that ensures the GitNexus server is running.

    Starts the server if needed and stops it on exit (only if we started it).
    """
    if config.no_auto_serve:
        if not _is_server_running(config.base_url):
            print(
                f"[ERROR] GitNexus server not running at {config.base_url} "
                f"and --no-auto-serve was specified"
            )
            sys.exit(1)
        print("[OK]   GitNexus server already running (--no-auto-serve)")
        yield
        return

    if _is_server_running(config.base_url):
        print("[OK]   GitNexus server already running")
        yield
        return

    proc = _start_server(config.port, config.project_root)
    try:
        if not _wait_for_server(config.base_url):
            print(f"[ERROR] Server did not start within {SERVER_STARTUP_TIMEOUT}s")
            _stop_server(proc)
            sys.exit(1)
        yield
    finally:
        _stop_server(proc)


# ---------------------------------------------------------------------------
# HTTP helpers  (for metadata endpoints that don't need DB lock)
# ---------------------------------------------------------------------------
def _get(url: str) -> Any:
    """GET JSON from *url*, raise on HTTP error."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.URLError as exc:
        print(f"[ERROR] Cannot reach {url}: {exc}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# CLI helpers  (for Cypher queries – avoids DB lock with MCP)
# ---------------------------------------------------------------------------
def _run_cypher(query: str, repo: str, cwd: Path) -> Any:
    """Execute Cypher via `npx gitnexus cypher --repo <name>` subprocess.

    Note: the CLI writes its JSON result to stderr (not stdout).
    We attempt to parse JSON from stderr first, then stdout as fallback.
    """
    cmd = f'npx gitnexus cypher "{query}" --repo {repo}'
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
            shell=True,
            cwd=str(cwd),
        )
        for stream in (result.stderr, result.stdout):
            raw = stream.strip()
            if not raw:
                continue
            json_start = raw.find("{")
            if json_start == -1:
                continue
            try:
                return json.loads(raw[json_start:])
            except json.JSONDecodeError:
                continue

        if result.returncode != 0:
            print(f"[WARN] Cypher CLI exited {result.returncode}")
        return {}
    except subprocess.TimeoutExpired:
        print("[WARN] Cypher CLI timed out")
        return {}
    except FileNotFoundError:
        print("[WARN] npx not found on PATH")
        return {}


# ---------------------------------------------------------------------------
# Data fetchers
# ---------------------------------------------------------------------------
def fetch_repos(base: str) -> list[dict]:
    return _get(f"{base}/api/repos")


def fetch_clusters(base: str, repo: str) -> list[dict]:
    data = _get(f"{base}/api/clusters?repo={repo}")
    return data.get("clusters", data) if isinstance(data, dict) else data


def fetch_processes(base: str, repo: str) -> list[dict]:
    data = _get(f"{base}/api/processes?repo={repo}")
    return data.get("processes", data) if isinstance(data, dict) else data


def fetch_hub_nodes(
    repo: str, cwd: Path, limit: int = TOP_N_HUBS
) -> list[dict]:
    """Use Cypher CLI to find the most-connected symbols."""
    cypher = (
        "MATCH (n)-[r:CodeRelation]->(m) "
        "RETURN n.name AS symbol, n.filePath AS filePath, "
        f"count(r) AS connections "
        f"ORDER BY connections DESC LIMIT {limit}"
    )
    result = _run_cypher(cypher, repo, cwd)
    return _parse_cypher_result(result)


def fetch_outgoing(repo: str, symbol: str, cwd: Path) -> list[str]:
    """Fetch names of symbols that *symbol* calls/references."""
    safe_sym = symbol.replace("'", "\\'")
    cypher = (
        f"MATCH (a)-[:CodeRelation]->(b) "
        f"WHERE a.name = '{safe_sym}' RETURN DISTINCT b.name AS callee LIMIT 20"
    )
    rows = _parse_cypher_result(_run_cypher(cypher, repo, cwd))
    return [r["callee"] for r in rows if r.get("callee")]


def _parse_cypher_result(result: Any) -> list[dict]:
    """Parse Cypher response (may be markdown table or JSON rows)."""
    if isinstance(result, list):
        return result
    if isinstance(result, dict):
        if "rows" in result:
            return result["rows"]
        md = result.get("markdown", "")
        if md:
            return _parse_md_table(md)
    return []


def _parse_md_table(md: str) -> list[dict]:
    """Parse a pipe-delimited markdown table into list[dict]."""
    lines = [ln.strip() for ln in md.strip().splitlines() if ln.strip()]
    if len(lines) < 3:
        return []
    headers = [h.strip() for h in lines[0].split("|") if h.strip()]
    rows: list[dict] = []
    for line in lines[2:]:
        vals = [v.strip() for v in line.split("|") if v.strip()]
        if len(vals) == len(headers):
            row = dict(zip(headers, vals))
            for k, v in row.items():
                if v.isdigit():
                    row[k] = int(v)
                else:
                    try:
                        row[k] = float(v)
                    except ValueError:
                        pass
            rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def classify_risk(connections: int) -> str:
    for rng, label in RISK_LEVELS.items():
        if connections in rng:
            return label
    return "LOW"


def infer_role(symbol: str, sym_type: str, connections: int) -> str:
    name_lower = symbol.lower()
    if "app.xaml" in name_lower or "program" in name_lower:
        return "Composition Root / DI Hub"
    if "serviceextension" in name_lower or "servicecollection" in name_lower:
        return "DI Wiring"
    if "viewmodel" in name_lower or "masterviewmodel" in name_lower:
        return "ViewModel Orchestrator"
    if "base" in name_lower and sym_type in ("Class", "File"):
        return "Abstract Base / Template Method"
    if "validator" in name_lower or "validation" in name_lower:
        return "Validation Module"
    if "service" in name_lower:
        return "Infrastructure Service"
    if "merger" in name_lower or "merge" in name_lower:
        return "Data Aggregator"
    if connections >= 20:
        return "High-connectivity Hub"
    return "Standard Node"


def build_summary(
    repo_name: str,
    repo_info: dict,
    hubs: list[dict],
    clusters: list[dict],
    processes: list[dict],
    cwd: Path,
) -> dict:
    """Assemble the Bridge Schema JSON."""
    stats = repo_info.get("stats", {})

    hub_nodes = []
    for h in hubs:
        sym = h.get("symbol", "")
        conn = int(h.get("connections", 0))
        sym_type = h.get("type", "Unknown")
        connected_to = fetch_outgoing(repo_name, sym, cwd)
        hub_nodes.append(
            {
                "symbol": sym,
                "type": sym_type,
                "filePath": h.get("filePath", ""),
                "connections": conn,
                "role": infer_role(sym, sym_type, conn),
                "risk": classify_risk(conn),
                "connected_to": connected_to[:10],
            }
        )

    cluster_list = [
        {
            "name": c.get("heuristicLabel", c.get("label", "")),
            "symbols": c.get("symbolCount", 0),
            "cohesion": round(c.get("cohesion", 0), 3),
        }
        for c in clusters
    ]

    process_list = [
        {
            "name": p.get("heuristicLabel", p.get("label", "")),
            "steps": p.get("stepCount", 0),
            "type": p.get("processType", "unknown"),
        }
        for p in processes
    ]

    patterns = _detect_patterns(hub_nodes, cluster_list)

    return {
        "source": "GitNexus_Bridge",
        "repo": repo_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "nodes": stats.get("nodes", 0),
            "edges": stats.get("edges", 0),
            "clusters": stats.get("communities", len(clusters)),
            "processes": stats.get("processes", len(processes)),
            "files": stats.get("files", 0),
        },
        "hub_nodes": hub_nodes,
        "clusters": cluster_list,
        "processes": process_list,
        "architectural_patterns": patterns,
    }


def _detect_patterns(hubs: list[dict], clusters: list[dict]) -> list[str]:
    """Heuristically detect architectural patterns from graph data."""
    patterns: list[str] = []

    has_di_hub = any("DI" in h["role"] for h in hubs)
    has_base = any("Base" in h["role"] or "Template" in h["role"] for h in hubs)
    has_vm = any("ViewModel" in h["role"] for h in hubs)
    has_validator = any("Validation" in h["role"] for h in hubs)
    has_service = any("Service" in h["role"] for h in hubs)

    cluster_names = {c["name"].lower() for c in clusters}

    if has_di_hub:
        patterns.append("Dependency Injection via composition root")
    if has_base:
        patterns.append("Template Method pattern via abstract base class")
    if has_vm:
        patterns.append("MVVM pattern with ViewModel orchestrators")
    if has_validator and has_service:
        patterns.append(
            "Clean Architecture: separate validation and infrastructure layers"
        )
    if "viewmodels" in cluster_names:
        patterns.append("Presentation layer clustered as ViewModels community")
    if any("service" in n for n in cluster_names):
        patterns.append("Service layer detected as distinct cluster")

    if not patterns:
        patterns.append(
            "No strong architectural pattern detected from graph topology"
        )

    return patterns


# ---------------------------------------------------------------------------
# Output generators
# ---------------------------------------------------------------------------
def write_json(summary: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"[OK] JSON written to {path}")


def write_markdown(summary: dict, path: Path) -> None:
    """Generate memory-bank/codebaseGraph.md from Bridge Schema."""
    path.parent.mkdir(parents=True, exist_ok=True)
    s = summary
    lines: list[str] = []

    lines.append(f"# Codebase Graph: {s['repo']}")
    lines.append(
        f"*Auto-generated by GitNexus Bridge on " f"{s['timestamp'][:10]}*\n"
    )

    # Stats
    st = s["stats"]
    lines.append("## Graph Statistics")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Files | {st['files']} |")
    lines.append(f"| Nodes | {st['nodes']} |")
    lines.append(f"| Edges | {st['edges']} |")
    lines.append(f"| Clusters | {st['clusters']} |")
    lines.append(f"| Processes | {st['processes']} |")
    lines.append("")

    # Hub Nodes
    lines.append(f"## Hub Nodes (Top {len(s['hub_nodes'])})")
    lines.append(
        "Symbols with the highest connectivity. "
        "Changes to these require impact analysis.\n"
    )
    lines.append("| Symbol | Type | Connections | Risk | Role |")
    lines.append("|--------|------|-------------|------|------|")
    for h in s["hub_nodes"]:
        lines.append(
            f"| `{h['symbol']}` | {h['type']} | {h['connections']} "
            f"| **{h['risk']}** | {h['role']} |"
        )
    lines.append("")

    # Hub details
    lines.append("### Hub Connection Details")
    for h in s["hub_nodes"]:
        if h["connected_to"]:
            targets = ", ".join(f"`{t}`" for t in h["connected_to"][:8])
            lines.append(f"- **`{h['symbol']}`** -> {targets}")
    lines.append("")

    # Clusters
    lines.append("## Architectural Clusters")
    lines.append("Functional communities detected by Leiden algorithm.\n")
    lines.append("| Cluster | Symbols | Cohesion |")
    lines.append("|---------|---------|----------|")
    for c in s["clusters"]:
        lines.append(f"| {c['name']} | {c['symbols']} | {c['cohesion']:.3f} |")
    lines.append("")

    # Processes
    lines.append("## Execution Flows")
    lines.append("Traced call-chain processes in the codebase.\n")
    lines.append("| Process | Steps | Type |")
    lines.append("|---------|-------|------|")
    for p in s["processes"]:
        lines.append(f"| {p['name']} | {p['steps']} | {p['type']} |")
    lines.append("")

    # Patterns
    lines.append("## Detected Architectural Patterns")
    for pat in s["architectural_patterns"]:
        lines.append(f"- {pat}")
    lines.append("")

    # Cross-reference section (agent-maintained)
    lines.append("## Cross-Reference Notes")
    lines.append(
        "*This section is maintained by the agent. "
        "Add experiential context linking graph insights to past work.*\n"
    )
    lines.append("<!-- Agent: append notes here after bug fixes or refactors -->")
    lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[OK] Markdown written to {path}")


# ---------------------------------------------------------------------------
# Public API — programmatic entry point
# ---------------------------------------------------------------------------
def run_bridge(config: BridgeConfig) -> dict:
    """Run the full bridge pipeline and return the summary dict.

    This is the primary programmatic API. Use this when calling the bridge
    from another script or from multiple projects in a loop.

    Args:
        config: BridgeConfig with project_root, repo, port, output paths, etc.

    Returns:
        The bridge summary dict (also written to JSON and MD files).
    """
    t0 = time.time()
    project_root = Path(config.project_root)

    with managed_server(config):
        repos = fetch_repos(config.base_url)
        if not repos:
            print("[ERROR] No indexed repos found. Run `npx gitnexus analyze` first.")
            sys.exit(1)

        if config.repo:
            repo_info = next(
                (r for r in repos if r["name"] == config.repo), None
            )
            if not repo_info:
                available = ", ".join(r["name"] for r in repos)
                print(
                    f"[ERROR] Repo '{config.repo}' not found. Available: {available}"
                )
                sys.exit(1)
        else:
            cwd_str = str(project_root)
            repo_info = next(
                (
                    r
                    for r in repos
                    if os.path.normpath(r["path"]) == os.path.normpath(cwd_str)
                ),
                repos[0],
            )

        repo_name = repo_info["name"]
        print(f"[INFO] Analyzing repo: {repo_name}")
        print(f"[INFO] Stats: {repo_info.get('stats', {})}")

        print("[INFO] Fetching clusters...")
        clusters = fetch_clusters(config.base_url, repo_name)
        print(f"       -> {len(clusters)} clusters")

        print("[INFO] Fetching processes...")
        processes = fetch_processes(config.base_url, repo_name)
        print(f"       -> {len(processes)} processes")

        print(f"[INFO] Fetching top {config.top_n_hubs} hub nodes via CLI Cypher...")
        hubs = fetch_hub_nodes(repo_name, project_root, config.top_n_hubs)
        print(f"       -> {len(hubs)} hub nodes")

        print("[INFO] Building Bridge Schema...")
        summary = build_summary(
            repo_name, repo_info, hubs, clusters, processes, project_root
        )

        json_path = Path(config.json_out)
        md_path = Path(config.md_out)
        write_json(summary, json_path)
        write_markdown(summary, md_path)

        elapsed = time.time() - t0
        mins, secs = divmod(int(elapsed), 60)
        print(f"\n[DONE] Bridge complete in {mins}m{secs:02d}s")
        print(f"       Hub nodes with >= {HUB_THRESHOLD} connections (risk threshold):")
        for h in summary["hub_nodes"]:
            if h["connections"] >= HUB_THRESHOLD:
                print(
                    f"         {h['risk']:8s}  {h['symbol']} ({h['connections']} conn)"
                )

        return summary


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="GitNexus x Neural-Memory Bridge",
        epilog=(
            "Library usage:\n"
            "  from gitnexus_bridge import BridgeConfig, run_bridge\n"
            "  config = BridgeConfig(project_root='/path/to/project', repo='MyRepo')\n"
            "  summary = run_bridge(config)\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--repo", help="Repository name (auto-detected if omitted)")
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"GitNexus server port (default: {DEFAULT_PORT})",
    )
    parser.add_argument(
        "--base-url", default=None, help="GitNexus server URL (overrides --port)"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=TOP_N_HUBS,
        help="Number of hub nodes to extract",
    )
    parser.add_argument(
        "--project-root",
        type=str,
        default=None,
        help="Project root directory (defaults to cwd)",
    )
    parser.add_argument("--json-out", type=str, default=None, help="JSON output path")
    parser.add_argument("--md-out", type=str, default=None, help="Markdown output path")
    parser.add_argument(
        "--no-auto-serve",
        action="store_true",
        help="Do not auto-start the GitNexus server",
    )
    args = parser.parse_args()

    config = BridgeConfig(
        project_root=args.project_root or "",
        repo=args.repo or "",
        port=args.port,
        base_url=args.base_url or "",
        top_n_hubs=args.top,
        json_out=args.json_out or "",
        md_out=args.md_out or "",
        no_auto_serve=args.no_auto_serve,
    )

    run_bridge(config)


if __name__ == "__main__":
    main()
