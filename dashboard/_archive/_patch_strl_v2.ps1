# _patch_strl_v2.ps1 — Update STRL entry in data.js to v2 (correct price $880)
# Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard
# powershell -ExecutionPolicy Bypass -File "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\_patch_strl_v2.ps1"

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$lines = Get-Content $dataFile -Encoding UTF8

# Find STRL object start line (look for ticker: "STRL")
$strlStart = -1
$strlEnd = -1
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match 'ticker: "STRL"') {
        # Back up 1 line to get the opening {
        $strlStart = $i - 1
    }
    # Find the fullContent closing backtick after STRL start
    if ($strlStart -gt 0 -and $i -gt ($strlStart + 20) -and $lines[$i] -match '^\s*`$' -and $strlEnd -eq -1) {
        # Check next line is }
        if ($i + 1 -lt $lines.Count -and $lines[$i + 1] -match '^\s*\}') {
            $strlEnd = $i + 1
            break
        }
    }
}

Write-Host "STRL object found: lines $strlStart to $strlEnd"

# Build new STRL fullContent (abbreviated — main metadata only for dashboard)
$newFullContent = @'
# 🏗️ STRL — Sterling Infrastructure, Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth
### RE-ANALYSIS v2 — 2026-05-07 | ราคาที่ถูกต้อง: ~$880

## 📌 ข้อมูลหลัก

| Field | Detail |
|-------|--------|
| Ticker | STRL (NASDAQ) |
| วันที่วิเคราะห์ | 2026-05-07 (Re-Analysis v2) |
| ราคา (as-of) | ~$880.00 (แก้ไขจาก $130 ที่ผิดพลาด) |
| Market Cap | ~$25.8B |
| Sector | Industrials / Infrastructure & Construction Services |
| S&P 500 ณ วันวิเคราะห์ | ~5,650 |

## 🎯 คำแนะนำ

| Field | Detail |
|-------|--------|
| Recommendation | AVOID (Upgraded จาก HOLD/WAIT ใน v1) |
| Entry Zone | $200–270 (genuine re-rating) / $665–735 (if reverse split 7:1) |
| Blended Fair Value | $156 (ESG-adjusted) |
| Margin of Safety | -82.3% |
| Stop Loss | N/A (AVOID) |
| Max Position | 0% (Kelly Negative) |

## ⚡ TL;DR

- Verdict: AVOID — ที่ราคา $880 ตลาดกำลัง price STRL เหมือน SaaS (P/S ~10x) ทั้งที่เป็น construction contractor (peer median P/S 0.7x)
- ทำไม: Blended FV $156 = MOS -82.3%; ไม่มี scenario ใน Sensitivity Matrix 5×5 justify $880 (extreme bull $750 < $880)
- Critical Flag: Reverse Split possible ($130×7=$910≈$880) — verify shares outstanding ก่อนลงทุน

## Re-Analysis Change Log (v1→v2)

| Item | v1 (ผิด) | v2 (ถูก) |
|------|----------|----------|
| ราคา | $130 | $880 |
| Market Cap | ~$3.8B | ~$25.8B |
| Rating | HOLD/WAIT | AVOID |
| Blended FV | $96 | $156 |
| MOS | -26% | -82.3% |
| Kelly | 3% (at entry) | NEGATIVE |
| P/E Fwd | ~20x | ~123-147x |
| P/S | ~0.8x | ~10.7x |

See full report: reports/STRL_2026-05-07.md
'@

# Build new STRL object (lines 3622 to 3648 replacement + new fullContent)
$newStrlObject = @"
  {
    ticker: "STRL",
    company: "Sterling Infrastructure, Inc.",
    date: "2026-05-07",
    reAnalysisVersion: "v2",
    sector: "Industrials / Infrastructure & Construction",
    price: 880.00,
    recommendation: "AVOID",
    blendedFV: 156.00,
    targetBull: 320.00,
    targetBase: 156.00,
    stopLoss: 0,
    convictionEmma: 7,
    convictionQuinn: 8,
    convictionBear: 7,
    convictionAvg: 7.3,
    pwEV: 164.60,
    beta: 1.10,
    sharpe1Y: 0.55,
    maxDrawdown: -0.38,
    moat: "Narrow",
    esgRating: "Medium-Low",
    esgScore: 5.0,
    keyThesis: "RE-ANALYSIS v2: AVOID at \$880. Blended FV \$156 = MOS -82.3%. P/S 10.7x vs peer median 0.7x = extreme overvaluation. Kelly NEGATIVE. CRITICAL: Possible Reverse Split (7:1: \$130x7=\$910≈\$880) — verify shares before investing.",
    topRisk: "Valuation mean-reversion (P/S 10.7x→1.5x = -86%) + Momentum reversal (AI narrative break = -50-80%) + Reverse split uncertainty",
    entryZone: "\$200-270 (genuine) / \$665-735 (reverse split)",
    positionSize: "0% (AVOID / Kelly Negative)",
    reportFile: "../reports/STRL_2026-05-07.md",
    fullContent: `$newFullContent`
  }
"@

# Replace lines from strlStart to strlEnd
$before = $lines[0..($strlStart - 1)]
$after = $lines[($strlEnd + 1)..($lines.Count - 1)]
$newLines = $before + $newStrlObject.Split("`n") + $after

# Update LAST_UPDATED
$newLines = $newLines | ForEach-Object { $_ -replace 'const LAST_UPDATED = "2026-05-07";', 'const LAST_UPDATED = "2026-05-07 (v2 STRL re-analysis)";' }

Set-Content $dataFile -Value $newLines -Encoding UTF8
Write-Host "STRL data.js patch v2 COMPLETE"
Write-Host "  price: 130 -> 880"
Write-Host "  recommendation: HOLD -> AVOID"
Write-Host "  blendedFV: 96 -> 156"
Write-Host "  convictionAvg: 6.0 -> 7.3"
Write-Host "  esgScore: 5.4 -> 5.0"
