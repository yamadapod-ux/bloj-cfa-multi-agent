# Leo Patch Script — Add V Re-Analysis v2 to dashboard/data.js
# Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\
# Command: .\dashboard\_patch_v_v2.ps1

$dataFile = "dashboard\data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# 1. Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-09"', 'const LAST_UPDATED = "2026-05-11"'

# 2. New V v2 entry to insert before closing ]; of REPORTS array
$newEntry = @'
  {
    ticker: "V",
    company: "Visa Inc.",
    date: "2026-05-11",
    version: "v2",
    sector: "Financial Services — Payment Networks",
    price: 337.00,
    recommendation: "HOLD",
    blendedFV: 286.00,
    esgAdjFV: 269.00,
    targetBull: 420.00,
    targetBase: 355.00,
    stopLoss: 240.00,
    convictionEmma: 7.5,
    convictionQuinn: 6.5,
    convictionBear: 7.0,
    convictionAvg: 7.0,
    pwEVEmma: 295.00,
    pwEVQuinn: 296.50,
    pwEVBear: 271.80,
    beta: 0.88,
    sharpeEst: 0.55,
    maxDrawdown: -0.27,
    moat: "Wide",
    esgRating: "Medium",
    esgScore: 5.85,
    mos: -0.150,
    wacc: 0.085,
    keyThesis: "Asset-light toll road model, Wide moat network effects, ROIC 50% vs WACC 8.5%. DOJ antitrust risk 25-35% structural remedy. Stablecoin legislation risk unmodeled in v1.",
    topRisk: "DOJ structural remedy (25-35% prob) → debit revenue -15-20% + stablecoin legislation creating alternative payment rails",
    entryZone: "$285-300 (T1) | $270-285 (T2)",
    positionSize: "4% max (Quarter-Kelly at entry)",
    dojProbBull: 0.25,
    dojProbBase: 0.40,
    dojProbBear: 0.35,
    sp500Ref: 5650,
    priorVersion: "V_2026-05-07",
    priorFV: 290.00,
    priorPrice: 355.00,
    priorMOS: -0.182,
    reportFile: "../reports/V_2026-05-11.md",
    fullContent: `# 💳 V — Visa Inc. (Re-Analysis v2)
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

📌 **ข้อมูลหลัก** | Ticker: V (NYSE) | Date: 2026-05-11 (v2) | Price: ~$337 | Market Cap: ~$690B | Sector: Financial Services — Payment Networks | S&P 500 ref: ~5,650

🎯 **คำแนะนำ: HOLD / WAIT FOR PULLBACK (Maintain)** | Entry T1: $285-300 | Entry T2: $270-285 | Blended FV: $286 | ESG-Adj FV: $269 | MOS: -15.0% | Stop Loss: $240 | Max Position: 4%

📊 **Score Dashboard**
| Blended FV | MOS | ESG | Conviction | Horizon |
|-----------|-----|-----|-----------|---------|
| $286 | -15.0% | 5.85/10 | 7.0/10 | 3-5yr |

💪 **Conviction Level Score**
\`\`\`
Emma   ███████▌░░  7.5/10  — Wide moat ชัดเจน, DOJ risk ลด (25%), ราคาใกล้ entry มากขึ้น
Quinn  ██████▌░░░  6.5/10  — Kelly negative, alpha ไม่ significant, 1/25 cells support ราคา
Bear   ███████░░░  7.0/10  — DOJ risk ยัง elevated (35%), stablecoin unmodeled, asymmetric downside
──────────────────────────────────────────────────────────────────────────────────────────
Avg    ███████░░░  7.0/10  [no flag — max gap 1pt < 3pt threshold]
\`\`\`

⚡ **TL;DR:** HOLD/WAIT Maintain — $337 ยัง 15% เหนือ FV $286 | DOJ antitrust case ยังดำเนินอยู่ (structural remedy risk 25-35%) | Stablecoin risk quantified (-$15/share) | Sensitivity matrix: 1/25 cells support ราคา | รอ pullback สู่ $285-300

## 💰 Valuation (Triangulation 30/30/40)
| Agent | P-W EV | Weight |
|-------|--------|--------|
| Emma | $295 | 30% |
| Quinn | $296.5 | 30% |
| Bear | $271.8 | 40% |
**Blended FV = $286 | ESG-Adj FV = $269 | MOS @ $337 = -15.0%**

## Re-Analysis v1→v2 Changes
| Item | v1 ($355) | v2 ($337) |
|------|-----------|-----------|
| Blended FV | $290 | $286 |
| MOS | -18.2% | -15.0% |
| Conviction | 6.7/10 | 7.0/10 |
| DOJ structural (Emma) | 35% | 25% |
| DOJ structural (Bear) | 35% | 35% ✓ |
| Stablecoin | Not modeled | -$15/share |
| Sensitivity var | Rev × WACC | Rev × DOJ Prob |

## 📉 Sensitivity Matrix (Quinn v2) — Rev CAGR × DOJ Structural Remedy Probability
| Rev CAGR \\ DOJ Prob | 0% | 10% | 20% | 25% (Base) | 40% |
|---|---|---|---|---|---|
| 6% | $256 | $245 | $235 | **$230** | $213 |
| 7.5% | $276 | $265 | $255 | **$249** | $233 |
| 9% (Base) | $296 | $285 | $275 | **$269** | $253 |
| 10.5% | $316 | $305 | $295 | **$289** | $274 |
| 12% | **$336** | $325 | $315 | $309 | $293 |
Only 1/25 cells ≥ $337 (12% CAGR + 0% DOJ) = extremely optimistic

## 🌱 ESG: 5.85/10 (Medium Risk — ลดจาก v1 6.4/10)
E: 8/10 | S: 4.5/10 (SME interchange fees; EU cap risk) | G: 5/10 (DOJ = governance flag)
ESG-Adj FV = $269 (discount 6%)

## 🔄 What Would Change Our Mind
**Bull Flip:** (1) DOJ dismissed → BUY ทันที (2) Price ≤ $290 → T1 entry (3) Revenue ≥ 11% สองไตรมาส → upgrade FV
**Bear Flip:** (1) DOJ structural remedy ผ่าน → SELL (2) Revenue ≤ 7% สองไตรมาส → AVOID (3) Stablecoin Act ผ่าน → moat ลด
**Invalidation:** DOJ wins full structural remedy OR FedNow ≥ 20% US debit market share

## 🎯 Recommendation: HOLD / WAIT FOR PULLBACK (Maintain)
> ### HOLD / WAIT — Entry Zone $285-300 (ยังห่าง ~11-17%)
> ราคา $337 ยัง 15% เหนือ Blended FV $286 | Kelly NEGATIVE | รอ DOJ resolution หรือราคาลงก่อน

Entry T1: $285-300 (2%) | Entry T2: $270-285 (1.5%) | Entry T3: DOJ resolved (0.5%) | Stop: $240`,
  },
'@

# Insert new V v2 entry before closing ]; of REPORTS array
# Find the closing of the array and insert before it
$insertPoint = $content.LastIndexOf('];')
$content = $content.Substring(0, $insertPoint) + $newEntry + "`n" + $content.Substring($insertPoint)

# Save
Set-Content $dataFile $content -Encoding UTF8

Write-Host "Patch applied successfully — V Re-Analysis v2 added to dashboard/data.js"
Write-Host "LAST_UPDATED changed to 2026-05-11"
