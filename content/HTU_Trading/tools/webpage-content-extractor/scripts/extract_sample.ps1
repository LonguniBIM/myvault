# Extract one lesson folder/zip and open the output.
# Usage:  .\scripts\extract_sample.ps1 -Source "..\..\raw\sources\Lesson 1 - ..." [-Output .\output] [-NoTranscribe]
param(
    [Parameter(Mandatory = $true)][string]$Source,
    [string]$Output = ".\output",
    [switch]$NoTranscribe,
    [switch]$Open
)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$exe = ".venv\Scripts\course-extract.exe"
if (-not (Test-Path $exe)) { throw "venv not set up; run scripts\setup.ps1 first" }

$extraArgs = @("extract", "--input", $Source, "--output", $Output, "--formats", "md,docx,json")
if ($NoTranscribe) { $extraArgs += "--no-transcribe" }

# The tool logs progress to stderr; don't let that trip ErrorActionPreference=Stop.
$ErrorActionPreference = "Continue"
& $exe @extraArgs
$ErrorActionPreference = "Stop"
if ($LASTEXITCODE -ne 0) { throw "extract failed ($LASTEXITCODE)" }

if ($Open) {
    $slug = (Get-ChildItem $Output -Directory | Sort-Object LastWriteTime | Select-Object -Last 1).FullName
    Start-Process explorer.exe $slug
}
