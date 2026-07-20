# _patch_V_simple.ps1 — Leo: Append V (Visa) to REPORTS array in data.js
# This script inserts the V entry before the closing ]; of REPORTS array

$dataPath = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

# Read all lines
$lines = Get-Content $dataPath

# Find the line with just "];"  (closing of REPORTS array)
# That's the line that says "];" after the last fullContent backtick
$insertIdx = -1
for ($i = $lines.Count - 1; $i -ge 0; $i--) {
    if ($lines[$i].Trim() -eq "];") {
        $insertIdx = $i
        break
    }
}

if ($insertIdx -eq -1) {
    Write-Error "Could not find ]; in data.js"
    exit 1
}

Write-Host "Found ]; at line $($insertIdx + 1)"

# Build V entry block (without leading comma since we insert before ];)
# The previous entry ends with }, so we add comma + V entry
$vEntry = @'
,
  {
    ticker: "V",
    company: "Visa Inc.",
    date: "2026-05-07",
    sector: "Financial Services / Payment Networks",
    price: 355.00,
    recommendation: "HOLD",
    blendedFV: 290.00,
    targetBull: 450.00,
    targetBase: 355.00,
    stopLoss: 240.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 7,
    convictionAvg: 6.7,
    pwEV: 320.00,
    beta: 0.90,
    sharpe1Y: 0.95,
    maxDrawdown: -0.28,
    moat: "Wide",
    esgRating: "Medium",
    esgScore: 6.4,
    keyThesis: "World-class payment network toll road — Wide Moat via network effects (4.3B cards x 130M merchants x 200+ countries). ROIC 50% top quartile, no credit risk, 80%+ gross margin. BUT: price $355 = 18% above Blended FV $290. DOJ antitrust lawsuit (2024) = idiosyncratic risk NOT in beta. Kelly NEGATIVE at $355. Wait for entry $285-310.",
    topRisk: "DOJ antitrust structural remedy (35% prob) — could impair toll road model permanently. WACC understated by 1-1.5%.",
    entryZone: "$285-310",
    positionSize: "4% (staged — 2 tranches at entry)",
    reportFile: "../reports/V_2026-05-07.md",
    fullContent: `# 💳 V — Visa Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

## 📌 ข้อมูลหลัก
| Field | Detail |
|-------|--------|
| Ticker | V (NYSE) |
| Date | 2026-05-07 |
| Price (est.) | ~$355.00 |
| Market Cap (est.) | ~$730B |
| Sector | Financial Services — Payment Networks |
| S&P 500 Price (ref.) | ~5,600 (est. 2026-05-07) |

## 🎯 คำแนะนำ
| Item | Detail |
|------|--------|
| Recommendation | HOLD / WAIT FOR PULLBACK |
| Entry Zone (Tranche 1) | $300-310 |
| Entry Zone (Tranche 2) | $285-300 |
| Blended Fair Value | $290/share |
| MOS @ Current Price | -18.2% (overvalued) |
| Stop Loss | $240 |
| Target Base | $355 |
| Target Bull | $420-450 |
| Max Position | 4% (Quarter-Kelly at entry) |

## 📊 Score Dashboard
| Metric | Value |
|--------|-------|
| Blended FV | $290 |
| MOS % | -18.2% |
| P-W EV (Quinn) | $320 |
| P-W EV (Bear) | $252.50 |
| ESG Score | 6.4/10 |
| Conviction Avg | 6.7/10 |
| Moat | Wide (narrowing risk) |
| Beta | 0.90 |

> TL;DR: HOLD/WAIT. Wide moat toll road แต่ราคา $355 = 18% เหนือ Blended FV $290. DOJ antitrust lawsuit (2024) = idiosyncratic tail risk. รอ entry $285-310.

## 📋 Executive Summary
Visa Inc. (V) คือบริษัท payment network ที่ทรงอิทธิพลที่สุดในโลก Wide Moat via network effects.
Blended FV = $290/share. MOS = -18.2%. DOJ antitrust lawsuit pending. Kelly NEGATIVE at $355.

Conviction Bar:
Emma   7/10 — Wide moat clear; 20% above FV reduces appeal
Quinn  6/10 — P-W EV $320 < $355; Kelly negative at current
Bear   7/10 — DOJ risk material; WACC 8.5% understated vs correct 9.5%
Avg    6.7/10

## 🏰 Moat Analysis
Wide Moat: Network Effects (4.3B cards x 130M merchants x 200+ countries) + Switching Costs + Intangible Assets + Scale Economies + Toll Road Model
Durability: 10-15 years confirmed; 20+ years uncertain (DOJ + RTP/stablecoin threats)

## 📊 Peer Comparison
V: P/E 28x, ROIC 50% (TOP QUARTILE), Rev Growth 9-10%, Moat Wide — FAIR VALUE vs peers
MA: P/E 30x (7% premium — justified by 11% growth)
AXP: P/E 18x (36% discount — takes credit risk)
PYPL: P/E 12x (deep discount — moat eroding)
FI: P/E 22x (discount — B2B, no consumer network effect)

## 💰 Valuation
Emma DCF FCFF: $294/share | EV/EBITDA 22x: $288 | P/E 28x: $302 | Emma Blended: $294.60
Quinn P-W EV: $320 (Bull25% $450 + Base45% $330 + Bear20% $220 + Extreme10% $150)
Bear P-W EV: $252.50 (Bull15% $420 + Base35% $295 + Bear35% $195 + Extreme15% $120)
Blended FV (30/30/40): $290/share — MOS -18.2%

## 📉 Sensitivity Matrix 5x5 (Rev CAGR x WACC)
| CAGR/WACC | 7.5% | 8.0% | 8.5%(Base) | 9.0% | 9.5%(DOJ) |
|-----------|------|------|-----------|------|----------|
| 13% | $432 | $398 | $368 | $342 | $318 |
| 11% | $396 | $365 | $338 | $314 | $292 |
| 9%(Base) | $361 | $332 | $311 | $289 | $269 |
| 7% | $325 | $299 | $278 | $258 | $241 |
| 5% | $288 | $266 | $247 | $230 | $214 |
Only 6/25 cells (24%) justify $355. Base case $311 = -12.4% below current.

## 🌱 ESG Scorecard
E: 8/10 (asset-light, low direct impact) | S: 5/10 (merchant fee discrimination + DOJ incentive payments) | G: 6/10 (DOJ lawsuit = material governance risk)
Overall: 6.4/10 | Adjustment: -10% | ESG-adj FV: $261

## 🔄 What Would Change Our Mind
Bull Flip Triggers: (1) Price $285-310 (2) DOJ dismissed/behavioral-only (3) New vertical >15% revenue (4) Cross-border 12%+ (5) US Stablecoin regulation
Bear Flip Triggers: (1) DOJ structural remedy (2) US interchange cap (3) Cross-border <5% 2Q (4) Sovereign alternative 10%+ (5) Data breach + enforcement
Thesis Invalidation: DOJ structural + interchange cap simultaneously | Stablecoin >5% global volume

## 🎯 Recommendation
HOLD / WAIT FOR PULLBACK
Entry Tranche 1: $300-310 (2%) | Tranche 2: $285-300 (2%) | Max 4%
Stop Loss: $240 | Target Base: $355 | Target Bull: $420-450

## 📅 Catalysts
Q2 2026 (Jun): Q2 FY2026 Earnings — cross-border volume [HIGH]
Q3 2026 (Sep): DOJ Antitrust Hearing [CRITICAL]
Q4 2026 (Nov): FY2026 Annual Earnings [HIGH]
2027 H1: US Stablecoin Legislation [HIGH]
2027 H2: DOJ Final Ruling [CRITICAL]

*Report: V_2026-05-07.md | บลจ. CFA | 2026-05-07*
`
  }
'@

# Insert vEntry before the ]; line
$before = $lines[0..($insertIdx - 1)]
$after = $lines[$insertIdx..($lines.Count - 1)]

$newLines = $before + $vEntry.Split("`n") + $after

Set-Content $dataPath $newLines -Encoding UTF8
Write-Host "SUCCESS: V entry added to data.js at line $insertIdx"
Write-Host "Total lines now: $($newLines.Count)"
