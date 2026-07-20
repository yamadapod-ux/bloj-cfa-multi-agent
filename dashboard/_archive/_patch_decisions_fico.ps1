# _patch_decisions_fico.ps1 — Leo patch script for FICO entry in decisions.md
# Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\
# Usage: cd "C:\Users\user\Desktop\บลจ\บลจ CFA"; .\dashboard\_patch_decisions_fico.ps1

$file = "C:\Users\user\Desktop\บลจ\บลจ CFA\portfolio\decisions.md"
$content = Get-Content $file -Raw -Encoding UTF8

# 1. Add FICO row after LDOS row in Decision History table
$ldosRow = '| **2026-05-14** | **LDOS** | **Leidos Holdings, Inc.** | **HOLD/WAIT** | **$122.88** | **6.3/10** | **$105** | Defense/GovIT'
$ficoRow = '| **2026-05-15** | **FICO** | **Fair Isaac Corporation** | **HOLD/WAIT** | **$1,088** | **7.0/10** | **$1,078** | Financial Analytics / Credit Scoring — Near-Monopoly credit scoring (~90% US lending decisions). ROIC 68% Best-in-Class. Repriced -49% from ATH on DOJ antitrust probe + FHFA VantageScore mandate. Blended FV $1,078 ≈ ราคา $1,088 = thin MOS. Triangulation 30/30/40 (Bear 40% = DOJ binary). ESG-adj FV $1,007. Kelly 3%. First Financial Analytics sector in portfolio. S&P 500 ref ~5,620. | **$720** |'

$content = $content -replace [regex]::Escape($ldosRow), "$ldosRow`n$ficoRow"

# 2. Update Rating Distribution
$oldRating = 'HOLD/WAIT | 8 | CCJ, RKLB, V (v2 Maintain), GEV, VEEV, NOK, **LDOS (NEW)**'
$newRating = 'HOLD/WAIT | 9 | CCJ, RKLB, V (v2 Maintain), GEV, VEEV, NOK, LDOS, **FICO (NEW)**'
$content = $content -replace [regex]::Escape($oldRating), $newRating

# 3. Update Average Conviction Score
$content = $content -replace '(?<=Average Conviction Score: )\d+\.\d+/10 \(อัปเดตหลัง LDOS\)', '6.35/10 (อัปเดตหลัง FICO)'

# 4. Update Sector Concentration table — add FICO row
$oldSector = '| **Telecom Equipment / Infrastructure** | NOK (HOLD/WAIT — 1.5% max) | 0% deployed | Entry $4.00-$4.60 |'
$newSector = "| **Telecom Equipment / Infrastructure** | NOK (HOLD/WAIT — 1.5% max) | 0% deployed | Entry \$4.00-\$4.60 |`n| **Financial Analytics / Credit Scoring** | **FICO (HOLD/WAIT — 3% max) NEW** | **0% deployed** | Entry T1 \$950-1020 (2%) / T2 \$820-950 (1%) |"
$content = $content -replace [regex]::Escape($oldSector), $newSector

# 5. Update Track Record — add FICO to a new theme section
$oldFooter = '*อัปเดตล่าสุด: 2026-05-14'
$newFooter = '*อัปเดตล่าสุด: 2026-05-15'
$content = $content -replace $oldFooter, $newFooter

# 6. Update footer content
$oldFooterFull = '*อัปเดตล่าสุด: 2026-05-14 — LDOS First Analysis (HOLD/WAIT) — Defense/GovIT sector ใหม่ในพอร์ต. ราคา $122.88. Blended FV $105 (ESG-adj $99). Entry T1 $105-115 (2%) / T2 $95-105 (1%). Stop $80. Conviction 6.3/10. DOGE = unquantifiable Black Swan. Q2 2026 Book-to-Bill = key catalyst. S&P 500 ref ~5,650-5,800 | Leo*'
$newFooterFull = "*อัปเดตล่าสุด: 2026-05-15 — FICO First Analysis (HOLD/WAIT) — Financial Analytics sector ใหม่ในพอร์ต. ราคา `$1,088. Blended FV `$1,078 (ESG-adj `$1,007). Entry T1 `$950-1,020 (2%) / T2 `$820-950 (1%). Stop `$720. Conviction 7.0/10. DOJ + FHFA = dual active regulatory binary. Bear 40% weight. S&P 500 ref ~5,620 | Leo*"
$content = $content -replace [regex]::Escape($oldFooterFull), $newFooterFull

$content | Set-Content $file -Encoding UTF8
Write-Host "decisions.md patched with FICO entry"
