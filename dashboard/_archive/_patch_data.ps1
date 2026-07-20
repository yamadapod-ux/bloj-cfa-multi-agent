# Patch script for data.js — Leo (2026-05-06)
# Adds AMD and MRVL entries to REPORTS array and updates LAST_UPDATED
# Run from PowerShell: cd "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard" && .\\_patch_data.ps1

$file = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$content = Get-Content $file -Raw -Encoding UTF8

# Step 1: Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-04-25";', 'const LAST_UPDATED = "2026-05-06";'

# Step 2: Define AMD and MRVL entries to insert before ];
$newEntries = @'

  ,
  {
    ticker: "AMD",
    company: "Advanced Micro Devices, Inc.",
    date: "2026-05-06",
    sector: "Technology / Semiconductors",
    price: 105.00,
    recommendation: "BUY",
    blendedFV: 148.00,
    targetBull: 200.00,
    targetBase: 148.00,
    stopLoss: 78.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 7,
    convictionAvg: 6.7,
    pwEV: 145.00,
    beta: 1.75,
    sharpe1Y: 0.62,
    maxDrawdown: -0.57,
    moat: "Narrow+",
    esgRating: "Medium",
    esgScore: 6.5,
    keyThesis: "Best-in-class AI/HPC challenger — MI300X/MI350 gaining GPU market share + EPYC server CPU dominance + ROCm ecosystem maturing; MOS +41% from blended FV $148; challenger play complementing NVDA",
    topRisk: "CUDA moat (invisible wall) makes ROCm adoption slower than bulls expect + AI hyperscaler capex cycle peak risk + Intel 18A recovery",
    entryZone: "$95-110",
    positionSize: "4% (3 tranches: $100-110/2%, $88-95/1.5%, $78-85/0.5%)",
    bullFlipTriggers: [
      "MI350/MI400 GPU revenue >= $5B in single quarter",
      "ROCm developer adoption doubles in 6 months",
      "EPYC server market share > 40%",
      "Hyperscaler capex guidance remains high >= 2027",
      "Stock pullback <= $85"
    ],
    bearFlipTriggers: [
      "MI GPU revenue growth < 30% YoY for 2 consecutive quarters",
      "Intel 18A ships on time with competitive benchmarks",
      "TSMC N2 allocation AMD reduced from priority",
      "Gross margin drops below 48% for 2 quarters",
      "Custom ASIC replaces AMD GPU >= 20% of AI workload"
    ],
    thesisInvalidation: "ROCm strategy officially abandoned, Lisa Su departure, TSMC capacity cut for AMD due to geopolitics, SEC/DOJ investigation on accounting",
    reportFile: "../reports/AMD_2026-05-06.md",
    fullContent: `# AMD -- Advanced Micro Devices, Inc.
### Equity Research Report -- bljCFA Multi-Strategy Aggressive Growth

## Key Data

| Field | Detail |
|-------|--------|
| Ticker | AMD (NASDAQ) |
| Date | 2026-05-06 |
| Price | ~$105.00 |
| Market Cap | ~$170B |
| Sector | Technology / Semiconductors |

## Recommendation

| Field | Detail |
|-------|--------|
| Rating | BUY -- Staged Entry |
| Entry Zone | $95-110 |
| Blended FV | $148 |
| MOS | +41% |
| Stop Loss | $78 |
| Max Position | 4% (3 tranches) |

## TL;DR

- Verdict: BUY staged -- AMD is best-in-class AI/HPC challenger trading at 41% discount to fair value
- Why: MI300X/MI350 gaining GPU market share + EPYC server CPU dominance + ROCm ecosystem maturing
- Downside Risk: CUDA ecosystem loyalty slows ROCm adoption + hyperscaler capex slowdown

## Conviction

Emma: 7/10 | Quinn: 6/10 | Bear: 7/10 | Average: 6.7/10

## Valuation

DCF Base: $155 | Peer P/E: $143 | P-W EV: $145 | Bear P-W EV: $135
Blended FV (30/30/40): $148 | MOS: +41%

## Sensitivity Matrix (Revenue CAGR x WACC)

| CAGR / WACC | 8% | 9% | 10% | 11% | 12% |
|-------------|-----|-----|-----|-----|-----|
| 10% | $95 | $85 | $77 | $70 | $64 |
| 20% | $122 | $110 | $100 | $91 | $83 |
| 28% Base | $175 | $158 | $144 | $131 | $120 |
| 36% | $220 | $198 | $180 | $164 | $150 |
| 45% | $272 | $245 | $222 | $202 | $184 |

## Peer Comparison

| Metric | AMD | NVDA | Intel | MRVL | Qualcomm | Median |
|--------|-----|------|-------|------|----------|--------|
| P/E Fwd | 22x | 35x | N/M | 38x | 14x | 28x |
| ROE | 2.7% | 69% | -25% | 8% | 42% | 25% |
| Rev Growth | +36% | +94% | -7% | +46% | +18% | +30% |
| Gross Margin | 53% | 76% | 41% | 57% | 57% | 57% |
| Moat | Narrow+ | Wide | Narrow | Narrow+ | Moderate | -- |

AMD P/E 22x = 21% discount to peer median 28x despite top-quartile growth = rare premium quality / discount valuation

## ESG: 6.5/10 (E:7/S:7/G:6) | Valuation Impact: -3% | ESG-Adj FV: $143

## Recommendation: BUY Staged Entry 4% Max | Entry $95-110 | Stop $78 | Target $148 base / $200 bull

Full report: reports/AMD_2026-05-06.md | bljCFA | 2026-05-06`
  },
  {
    ticker: "MRVL",
    company: "Marvell Technology, Inc.",
    date: "2026-05-06",
    sector: "Technology / Semiconductors (Custom Silicon + Networking)",
    price: 72.00,
    recommendation: "BUY",
    blendedFV: 112.00,
    targetBull: 165.00,
    targetBase: 112.00,
    stopLoss: 52.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 6,
    convictionAvg: 6.3,
    pwEV: 119.00,
    beta: 1.65,
    sharpe1Y: 0.58,
    maxDrawdown: -0.63,
    moat: "Narrow+",
    esgRating: "Medium",
    esgScore: 6.2,
    keyThesis: "Custom silicon kingmaker for hyperscalers (Amazon Trainium, Google TPU) + Ethernet networking for AI clusters -- Switzerland of semiconductor; MOS +56% from blended FV $112; structural demand independent of GPU winner",
    topRisk: "Client concentration Amazon/Google ~50% revenue = cliff edge risk + hyperscaler in-house silicon maturation + M&A goodwill impairment ($8B+ Inphi/Cavium)",
    entryZone: "$65-75",
    positionSize: "3% (2 tranches: $65-75/2%, $55-65/1%)",
    bullFlipTriggers: [
      "Amazon Trainium 3/Google TPU Next NRE contract renewal >= $2B",
      "Data Center revenue >= $8B in FY26",
      "Gross margin breaks above 60%",
      "Adj. EPS FY26 >= $3.00",
      "Stock pullback <= $60"
    ],
    bearFlipTriggers: [
      "Hyperscaler announces in-house SerDes/networking replacing MRVL",
      "Amazon or Google reduces MRVL spending >= 20%",
      "Revenue growth below 20% YoY for 2 consecutive quarters",
      "Goodwill impairment >= $2B",
      "Broadcom launches competing custom ASIC design service"
    ],
    thesisInvalidation: "AWS/Google announces full in-house silicon replacing MRVL entirely, TSMC allocation cut, SEC investigation on M&A accounting, Revenue miss >= 20% two consecutive quarters",
    reportFile: "../reports/MRVL_2026-05-06.md",
    fullContent: `# MRVL -- Marvell Technology, Inc.
### Equity Research Report -- bljCFA Multi-Strategy Aggressive Growth

## Key Data

| Field | Detail |
|-------|--------|
| Ticker | MRVL (NASDAQ) |
| Date | 2026-05-06 |
| Price | ~$72.00 |
| Market Cap | ~$62B |
| Sector | Technology / Semiconductors (Custom Silicon + Networking) |

## Recommendation

| Field | Detail |
|-------|--------|
| Rating | BUY -- Staged Entry |
| Entry Zone | $65-75 |
| Blended FV | $112 |
| MOS | +56% |
| Stop Loss | $52 |
| Max Position | 3% (2 tranches) |

## TL;DR

- Verdict: BUY staged -- MRVL is custom silicon kingmaker; hyperscalers depend on MRVL for AI ASIC and interconnect; MOS +56%
- Why: Amazon Trainium, Google TPU use MRVL silicon design services + Ethernet switching for AI clusters -- structural demand regardless of GPU winner
- Downside Risk: Client concentration Amazon/Google ~50% revenue -- if hyperscaler in-house design matures, MRVL may be dis-intermediated

## Conviction

Emma: 7/10 | Quinn: 6/10 | Bear: 6/10 | Average: 6.3/10

## Valuation

DCF Base: $128 | Peer P/E: $123 | P-W EV: $119 | Bear P-W EV: $100
Blended FV (30/30/40): $112 | MOS: +56% (highest in semiconductor portfolio)

## Sensitivity Matrix (Revenue CAGR x Terminal EBIT Margin)

| CAGR / Margin | 20% | 26% | 32% Base | 38% | 44% |
|---------------|-----|-----|---------|-----|-----|
| 12% | $52 | $65 | $80 | $96 | $112 |
| 22% | $70 | $88 | $108 | $130 | $152 |
| 32% Base | $90 | $112 | $138 | $165 | $193 |
| 42% | $115 | $143 | $175 | $210 | $246 |
| 52% | $142 | $178 | $218 | $261 | $306 |

## Peer Comparison

| Metric | MRVL | AVGO | AMD | NVDA | Credo | Median |
|--------|------|------|-----|------|-------|--------|
| P/E Fwd | 38x | 21x | 22x | 35x | 45x | 30x |
| ROE | 8% | 45% | 2.7% | 69% | -15% | 25% |
| Rev Growth | +46% | +22% | +36% | +94% | +45% | +40% |
| Gross Margin | 57% | 68% | 53% | 76% | 62% | 63% |
| Moat | Narrow+ | Wide | Narrow+ | Wide | Narrow | -- |

MRVL FY27E P/E 17x = genuinely cheap vs current 38x trailing; growth premium + re-rating story

## ESG: 6.2/10 (E:6.5/S:5.5/G:6.3) | Valuation Impact: -5% | ESG-Adj FV: $106

## Bear Warning: Client concentration Amazon/Google ~50% = cliff edge; semiconductor exposure now 19% -- hard ceiling at 3%

## Recommendation: BUY Staged Entry 3% Max | Entry $65-75 | Stop $52 | Target $112 base / $165 bull

Full report: reports/MRVL_2026-05-06.md | bljCFA | 2026-05-06`
  }
'@

# Step 3: Insert new entries before the closing ];
# The closing is exactly "];"
$content = $content -replace "`n\];", ($newEntries + "`n];")

# Step 4: Write back
Set-Content $file $content -Encoding UTF8

Write-Host "SUCCESS: data.js patched -- AMD and MRVL added, LAST_UPDATED = 2026-05-06"
Write-Host "Total reports now: 8 (NVDA, CCJ, HIMS, TMDX, AVGO, RKLB, AMD, MRVL)"
