# Setup the extractor venv on Windows.
# Usage:  .\scripts\setup.ps1
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if (-not (Test-Path ".venv")) {
    Write-Host "Creating venv (.venv)..."
    $py = (Get-Command py -ErrorAction SilentlyContinue)
    if ($py) { py -3.12 -m venv .venv } else { python -m venv .venv }
}

& ".venv\Scripts\python.exe" -m pip install --upgrade pip
& ".venv\Scripts\python.exe" -m pip install -e ".[transcribe]"

Write-Host ""
Write-Host "Checking external tools:"
$ffprobe = (Get-Command ffprobe -ErrorAction SilentlyContinue)
if ($ffprobe) { Write-Host "  ffprobe: $($ffprobe.Source)" } else { Write-Host "  ffprobe: NOT FOUND (install FFmpeg for audio matching)" }
$soffice = (Get-Command soffice -ErrorAction SilentlyContinue)
if ($soffice) { Write-Host "  soffice: $($soffice.Source)" } else { Write-Host "  soffice: NOT FOUND (optional, only for --render-docx)" }

Write-Host ""
Write-Host "Ready. Example:"
Write-Host '  .\.venv\Scripts\course-extract.exe extract --input "..\..\raw\sources\Lesson 1 - ..." --output .\output'
