# _patch_veev.ps1 — Leo patch script for VEEV dashboard entry
# Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\
# Usage: .\dashboard\_patch_veev.ps1

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-09";', 'const LAST_UPDATED = "2026-05-11";'

# VEEV entry to insert before closing ];
$veevEntry = @'

  {
    ticker: "VEEV",
    company: "Veeva Systems Inc.",
    date: "2026-05-11",
    sector: "Healthcare Technology / Life Sciences SaaS",
    price: 166.00,
    recommendation: "HOLD",
    blendedFV: 192.00,
    targetBull: 265.00,
    targetBase: 192.00,
    stopLoss: 118.00,
    convictionEmma: 7,
    convictionQuinn: 7,
    convictionBear: 6,
    convictionAvg: 6.7,
    pwEV: 200.50,
    beta: 0.82,
    sharpe1Y: 0.78,
    maxDrawdown: -0.64,
    moat: "Wide",
    esgRating: "Low Risk",
    esgScore: 7.3,
    keyThesis: "Healthcare SaaS — Wide Moat FDA 21 CFR lock-in (strongest switching cost in portfolio). S&P 500 inclusion May 19 = institutional flow. FCF Yield 5.1%, Rev +16.3% YoY, Alpha +4.8%/yr (t=2.1 highest in portfolio). BUT MOS +15.7% < 20% BUY threshold; Bear DCF $152 near current price; Vault CRM migration off Salesforce = unresolved execution risk.",
    topRisk: "Vault CRM migration retention miss + Revenue CAGR deceleration to 12% (Bear) + Rate re-rating WACC 11%",
    entryZone: "$148-158 (T1) / $130-145 (T2)",
    positionSize: "3% max (staged — HOLD/WAIT)",
    bullFlipTriggers: [
      "Vault CRM migration Q2 FY2027 retention >= 95%",
      "Data Cloud revenue > $200M annualized",
      "FY2027 Revenue guidance >= 18%",
      "Fed rate cut >= 50bp cumulative 2026",
      "Price pullback to $140-150"
    ],
    bearFlipTriggers: [
      "Vault CRM migration retention < 90%",
      "Revenue CAGR < 12% for 2 consecutive quarters",
      "Salesforce wins top-20 pharma from VEEV Commercial Cloud",
      "VEEV M&A > $5B",
      "FDA CSA modernization removes 21 CFR Part 11 lock-in"
    ],
    thesisInvalidation: "Vault CRM migration failure > 15% customer churn OR Peter Gassner CEO departure OR Revenue growth < 8% any full fiscal year",
    reportFile: "../reports/VEEV_2026-05-11.md",
    fullContent: `# VEEV -- Veeva Systems Inc.
### Equity Research Report - บลจ. CFA Multi-Strategy Aggressive Growth

## ข้อมูลหลัก
| Ticker | Date | Price | Market Cap | Sector |
|--------|------|-------|-----------|--------|
| VEEV (NYSE) | 2026-05-11 | ~$166 | ~$25.7B | Healthcare Technology / Life Sciences SaaS |

## คำแนะนำ: HOLD / WAIT FOR PULLBACK
| Recommendation | Entry T1 | Blended FV | MOS | Stop Loss | Max Position |
|:---:|:---:|:---:|:---:|:---:|:---:|
| HOLD / WAIT | $148-158 | $192 | +15.7% | $118 | 3% (staged) |

## Score Dashboard
| Blended FV | MOS | ESG | Conviction Avg | Horizon |
|-----------|-----|-----|---------------|---------|
| $192 | +15.7% | 7.3/10 | 6.7/10 | 3-5 ปี |

## TL;DR
- Verdict: HOLD/WAIT -- FDA lock-in moat แข็งแกร่ง แต่ MOS +15.7% < 20% BUY threshold; Bear DCF $152 ใกล้ราคา $166
- ทำไม: ROIC 115.9% inflated (adj ~15-20%); Vault CRM migration off Salesforce = unresolved; Quarter-Kelly = 1% (thin signal)
- Downside Risk: Vault CRM miss + Revenue decel + Rate re-rating = $88-110 extreme scenario

## Conviction Score
Emma   7/10 -- Wide moat clear, DCF base $170 near current price, analyst targets $280+ = upside compelling
Quinn  7/10 -- Alpha t=2.1 highest in portfolio; 72% sensitivity scenarios above $166; Kelly thin
Bear   6/10 -- ROIC inflated, Vault CRM migration unresolved, S&P 500 catalyst priced in
Avg    6.7/10 -- No flag (gap 1pt < 3pt threshold; avg > 5)

## Valuation (Triangulation 30/30/40)
| Agent | Method | FV | Weight |
|-------|--------|-----|--------|
| Emma | DCF + Peer Blend | $225 | 30% |
| Quinn | P-W EV | $205 | 30% |
| Bear | P-W EV (conservative) | $178 | 40% |
| Charlie Blended FV | ESG-adj (-2%) | $192 | -- |
MOS @ $166 = +15.7%

## Sensitivity Matrix 5x5 (Rev CAGR x WACC)
| Rev CAGR \\ WACC | 8.5% | 9.0% | 10.0% | 11.0% | 12.0% |
|---|---|---|---|---|---|
| 8% | $148 | $135 | $118 | $105 | $93 |
| 12% | $192 | $176 | $155 | $138 | $123 |
| 16% (Base) | $248 | $228 | $170 | $152 | $135 |
| 20% | $322 | $296 | $230 | $205 | $183 |
| 24% | $412 | $379 | $295 | $263 | $235 |
72% of 25 scenarios = FV above $166 current price.

## ESG: 7.3/10 (Low Risk / Positive)
E: 7.5/10 (cloud-native SaaS, near-zero emissions) | S: 6.5/10 (pharma adjacency) | G: 8.0/10 (PBC structure, founder-CEO)
ESG-adj impact: -2% on Blended FV

## Top Risks
1. Vault CRM migration retention miss (25% prob, HIGH impact -30-50% to FV)
2. Revenue CAGR decel to 12% (35% prob, HIGH impact -20-30%)
3. S&P 500 inclusion catalyst priced in (60% -- trading not valuation)
4. Salesforce Life Sciences Cloud threat (20%, MEDIUM -- Commercial Cloud only 30%)
5. Rate re-rating WACC 11% (30% prob, HIGH -- DCF drops to $152 bear)

## Recommendation: HOLD / WAIT FOR PULLBACK
Entry T1 $148-158 (2%) | T2 $130-145 (0.5%) | T3 on Vault CRM success (0.5%)
Stop $118 | Target Base $192 | Target Bull $265 | Consensus $280
Key Catalyst: Vault CRM migration result Q2 FY2027 (Aug 2026) -- THE most important event
`
  },
'@

# Insert before closing ];
$content = $content -replace '];(\s*\n\s*// Computed)', "$veevEntry`];`$1"

Set-Content $dataFile $content -Encoding UTF8
Write-Host "VEEV entry added to dashboard/data.js successfully"
Write-Host "LAST_UPDATED updated to 2026-05-11"
