# _patch_intu.ps1 — Leo's patch script for INTU entry in data.js
# Run: powershell -ExecutionPolicy Bypass -File "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\_patch_intu.ps1"

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-15"', 'const LAST_UPDATED = "2026-05-16"'

# New INTU entry to insert before the closing of REPORTS array
$newEntry = @'
  ,{
    ticker: "INTU",
    company: "Intuit Inc.",
    date: "2026-05-16",
    sector: "Technology / Financial Software",
    price: 445.00,
    recommendation: "BUY",
    blendedFV: 559.00,
    targetBull: 750.00,
    targetBase: 559.00,
    stopLoss: 348.00,
    convictionEmma: 7.5,
    convictionQuinn: 7.0,
    convictionBear: 7.0,
    convictionAvg: 7.2,
    pwEV: 559.00,
    beta: 1.15,
    sharpe1Y: 0.03,
    maxDrawdown: -0.56,
    moat: "Narrow+ to Wide",
    esgRating: "BB+",
    esgScore: 6.5,
    keyThesis: "Financial Software OS for American SMBs and consumers. QuickBooks Wide Moat (10.1M subscribers, 750+ integrations, switching cost 200-400hrs). TurboTax Narrow+ (87% retention, Live tier growing 25%+). 100M+ data profiles = AI moat. -35% from high = WIDE entry window. Earnings May 20.",
    topRisk: "IRS Direct File expanding to 40+ states (structural threat to TurboTax free tier). Earnings May 20 = binary ±8%. Credit Karma flat 3 years (high-rate headwind).",
    entryZone: "T1 $430-460 (3% pre-earnings), T2 $395-430 (2.5% on miss), T3 $450-480 (1.5% on beat)",
    positionSize: "7% total (staged; IPS Conviction 7.2 ≥ 7.0 → Deploy T1)",
    reportFile: "../reports/INTU_2026-05-16.md",
    competitorData: [
      { name: "H&R Block", ticker: "HRB", pe: 12, evEbitda: 10, roe: 85, roic: 15, revGrowth: 5, grossMargin: 62, moat: "Narrow" },
      { name: "ADP", ticker: "ADP", pe: 28, evEbitda: 22, roe: 81, roic: 20, revGrowth: 7, grossMargin: 72, moat: "Narrow-Wide" },
      { name: "Workday", ticker: "WDAY", pe: 45, evEbitda: 30, roe: 12, roic: 8, revGrowth: 15, grossMargin: 75, moat: "Narrow+" },
      { name: "Xero", ticker: "XRO", pe: 100, evEbitda: 55, roe: 8, roic: 5, revGrowth: 25, grossMargin: 87, moat: "Narrow (APAC)" },
      { name: "Sage", ticker: "SGE.L", pe: 25, evEbitda: 18, roe: 20, roic: 18, revGrowth: 9, grossMargin: 60, moat: "Narrow" }
    ],
    revenueSegments: [
      { segment: "Small Business & Self-Employed (QuickBooks)", revenue: 9.0, pct: 55, growth: 19, margin: 35 },
      { segment: "Consumer (TurboTax)", revenue: 4.7, pct: 29, growth: 8, margin: 55 },
      { segment: "Credit Karma", revenue: 1.8, pct: 11, growth: 5, margin: 15 },
      { segment: "ProTax (Professional Tax)", revenue: 0.8, pct: 5, growth: 7, margin: 45 }
    ],
    fullContent: `# INTU — Intuit Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

## 📌 ข้อมูลหลัก

| Field | Value |
|-------|-------|
| Ticker | INTU (NASDAQ) |
| Date | 2026-05-16 |
| Current Price | $445 |
| Market Cap | ~$126B |
| Sector | Technology — Financial Software |
| S&P 500 Ref (entry) | ~5,620–5,650 |

## 🎯 คำแนะนำ

| Field | Value |
|-------|-------|
| Recommendation | **BUY — Staged Entry (Pre-Earnings Limited)** |
| Entry Zone T1 (Pre-Earnings) | $430–$460 (3%) |
| Entry Zone T2 (Post-Earnings Miss) | $395–$430 (2.5%) |
| Entry Zone T3 (Earnings Beat) | $450–$480 (1.5%) |
| Blended Fair Value | $559 (Emma 40% / Quinn 35% / Bear 25%) |
| ESG-Adjusted FV | ~$534 |
| Margin of Safety | +25.6% |
| Stop Loss | $348 (-21.8% จาก entry $445) |
| Max Position | 7% |

## ⚡ TL;DR
- **Verdict:** BUY ด้วย Staged Entry — Financial Software Wide Moat ลง -35% จาก high โดย fundamentals ไม่เสียหาย
- **ทำไม:** Blended FV $559 vs $445 = MOS +25.6%; FCF yield 4.3%; QuickBooks 10.1M subscribers; AI + Anthropic = structural tailwind; Conviction 7.2/10 → IPS Deploy T1
- **Downside Risk:** IRS Direct File 40+ states (structural threat); Earnings May 20 ±8%; Credit Karma flat 3 ปี

## 📊 Score Dashboard
| Metric | Value |
|--------|-------|
| Blended FV | $559 |
| ESG-Adj FV | $534 |
| MOS | +25.6% |
| ESG Score | 6.5/10 |
| Conviction | 7.2/10 |
| Forward 3Y Return | +25–68% (base–bull) |
| Stop Loss | $348 (-21.8% from $445) |`
  }
'@

# Insert before last closing "];" of REPORTS array
$content = $content -replace '(\];\s*$)', "$newEntry`n];"

Set-Content $dataFile $content -Encoding UTF8
Write-Host "INTU patch applied successfully to data.js"
Write-Host "LAST_UPDATED set to 2026-05-16"
Write-Host "INTU entry added to REPORTS array"
Write-Host "competitorData and revenueSegments embedded"
