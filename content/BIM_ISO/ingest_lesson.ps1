# Wrapper script to ingest lessons into wiki
# Run this from D:\wiki\BIM_ISO directory

param(
    [ValidateSet('all', 'watch', 'folder')]
    [string]$Mode = 'all',

    [string]$Folder
)

$projectDir = $PSScriptRoot
if (-not $projectDir) {
    $projectDir = Get-Location
}

$pythonExe = Join-Path $projectDir "tools\webpage-content-extractor\.venv\Scripts\python.exe"
$scriptDir = Join-Path $projectDir "scripts"

Write-Host "Lesson Ingestion Wrapper" -ForegroundColor Cyan
Write-Host "Project dir: $projectDir" -ForegroundColor Gray
Write-Host "Python: $pythonExe" -ForegroundColor Gray
Write-Host "Scripts dir: $scriptDir" -ForegroundColor Gray
Write-Host "Mode: $Mode" -ForegroundColor Yellow
Write-Host ""

if (-not (Test-Path $pythonExe)) {
    Write-Error "Python not found at: $pythonExe"
    exit 1
}

if (-not (Test-Path $scriptDir)) {
    Write-Error "Scripts directory not found at: $scriptDir"
    exit 1
}

try {
    switch ($Mode) {
        'all' {
            Write-Host "Ingesting all new/changed lessons..." -ForegroundColor Green
            & $pythonExe (Join-Path $scriptDir "ingest_lesson.py") --all
        }
        'watch' {
            Write-Host "Watching for new lessons..." -ForegroundColor Green
            Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
            & $pythonExe (Join-Path $scriptDir "watch_ingest.py")
        }
        'folder' {
            if (-not $Folder) {
                Write-Error "Folder parameter required: .\ingest_lesson.ps1 -Mode folder -Folder raw\sources\lesson-name"
                exit 1
            }
            $folderPath = Join-Path $projectDir "raw\sources\$Folder"
            if (-not (Test-Path $folderPath)) {
                Write-Error "Folder not found: $folderPath"
                exit 1
            }
            Write-Host "Ingesting: $Folder" -ForegroundColor Green
            & $pythonExe (Join-Path $scriptDir "ingest_lesson.py") $folderPath
        }
    }
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nSuccess!" -ForegroundColor Green
    }
} catch {
    Write-Error "Error: $_"
    exit 1
}
