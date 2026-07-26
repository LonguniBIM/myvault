# Ingest a Webpage-Complete lesson folder into the BIM ISO wiki.
#
# Thin wrapper over scripts\ingest_lesson.py (the workspace bridge), which reuses
# the existing wiki-integration layer (update_wiki_index / update_wiki_log).
#
# Usage:  .\scripts\ingest_to_wiki.ps1 -Source "..\..\raw\sources\Lesson 1 - ..." [-NoTranscribe]
param(
    [Parameter(Mandatory = $true)][string]$Source,
    [switch]$NoTranscribe
)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot                         # tools\webpage-content-extractor
$wikiRoot = (Resolve-Path (Join-Path $root "..\..")).Path        # BIM_ISO
$bridge = Join-Path $wikiRoot "scripts\ingest_lesson.py"
$py = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) { throw "venv not set up; run scripts\setup.ps1 first" }

$bridgeArgs = @($bridge, "--input", (Resolve-Path $Source).Path)
if ($NoTranscribe) { $bridgeArgs += "--no-transcribe" }

$env:PYTHONUTF8 = "1"
$ErrorActionPreference = "Continue"   # tool logs progress to stderr
& $py @bridgeArgs
$ErrorActionPreference = "Stop"
if ($LASTEXITCODE -ne 0) { throw "ingest failed ($LASTEXITCODE)" }
