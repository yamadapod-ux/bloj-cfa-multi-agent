# _apply_strl.ps1 — Apply STRL patch to data.js
# Usage: cd "C:\Users\user\Desktop\บลจ\บลจ CFA" then .\dashboard\_apply_strl.ps1

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$insertFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\_strl_insert.js"

Write-Host "Reading data.js..." -ForegroundColor Yellow
$lines = [System.IO.File]::ReadAllLines($dataFile, [System.Text.Encoding]::UTF8)
Write-Host "Total lines: $($lines.Count)" -ForegroundColor Gray

# Step 1: Update LAST_UPDATED
$updated = $false
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match 'const LAST_UPDATED') {
        $lines[$i] = 'const LAST_UPDATED = "2026-05-07";'
        Write-Host "LAST_UPDATED updated at line $($i+1)" -ForegroundColor Cyan
        $updated = $true
        break
    }
}
if (-not $updated) { Write-Host "WARNING: LAST_UPDATED not found" -ForegroundColor Red }

# Step 2: Find last ]; line (closing REPORTS array)
$closeIndex = -1
for ($i = $lines.Count - 1; $i -ge 0; $i--) {
    if ($lines[$i] -eq '];') {
        $closeIndex = $i
        Write-Host "Found closing ]; at line $($i+1)" -ForegroundColor Cyan
        break
    }
}

if ($closeIndex -lt 0) {
    Write-Host "ERROR: Cannot find ]; — aborting" -ForegroundColor Red
    exit 1
}

# Step 3: Read insert content
Write-Host "Reading STRL insert..." -ForegroundColor Yellow
$insertLines = [System.IO.File]::ReadAllLines($insertFile, [System.Text.Encoding]::UTF8)
Write-Host "Insert lines: $($insertLines.Count)" -ForegroundColor Gray

# Step 4: Assemble new file
$before = $lines[0..($closeIndex - 1)]
$after  = $lines[$closeIndex..($lines.Count - 1)]
$newLines = $before + $insertLines + $after

Write-Host "Writing updated data.js ($($newLines.Count) lines)..." -ForegroundColor Yellow
[System.IO.File]::WriteAllLines($dataFile, $newLines, [System.Text.Encoding]::UTF8)

Write-Host "Done! data.js updated with STRL entry." -ForegroundColor Green
Write-Host "  Lines before: $($lines.Count) | Lines after: $($newLines.Count)" -ForegroundColor Gray
