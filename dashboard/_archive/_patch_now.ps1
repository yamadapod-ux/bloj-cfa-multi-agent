# _patch_now.ps1 — Leo patch script สำหรับ NOW entry ใน data.js
# รัน: powershell -ExecutionPolicy Bypass -File "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\_patch_now.ps1"

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-09";', 'const LAST_UPDATED = "2026-05-11";'

# NOW entry to insert before the closing ]; of REPORTS array
$nowEntry = @'
,
  {
    ticker: "NOW",
    company: "ServiceNow Inc.",
    date: "2026-05-11",
    sector: "Technology / Enterprise SaaS / Agentic AI Platform",
    price: 91.00,
    recommendation: "BUY",
    blendedFV: 226.00,
    targetBull: 330.00,
    targetBase: 226.00,
    stopLoss: 58.00,
    convictionEmma: 7,
    convictionQuinn: 7,
    convictionBear: 6,
    convictionAvg: 6.7,
    pwEV: 229.00,
    beta: 1.10,
    sharpe1Y: 0.70,
    maxDrawdown: -0.51,
    moat: "Wide",
    esgRating: "Medium",
    esgScore: 6.0,
    keyThesis: "Wide Moat Agentic AI Orchestration Platform — ลงมา 51% จาก ATH $186 สู่ระดับที่ Sensitivity Matrix 25/25 scenarios ให้ upside; Revenue Growth +21.7%; MOS +148% (rare สำหรับ Wide Moat SaaS); Agentic AI platform คือ layer ที่ AI agents วิ่งบน ไม่ใช่สิ่งที่ถูก AI disrupt; Partnership 2026: MSFT+NVDA+Accenture",
    topRisk: "SBC-adjusted FCF ต่ำกว่า headline 40% (real FCF yield ~3.7% ไม่ใช่ 4.9%); CAGR deceleration law of large numbers ที่ $11B+ scale; Agentic AI narrative ยังไม่มี revenue proof; IT budget freeze recession risk",
    entryZone: "T1: $85-95 / T2: $72-84 / T3: $60-71",
    positionSize: "5% (Quarter-Kelly, staged 3 tranches)",
    reportFile: "../reports/NOW_2026-05-11.md",
    fullContent: `# NOW — ServiceNow Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

## Summary

| Field | Detail |
|-------|--------|
| Ticker | NOW (NYSE) |
| Date | 2026-05-11 |
| Price | ~$91.00 |
| Market Cap | ~$46.9B |
| Sector | Enterprise SaaS / Agentic AI Platform |
| Recommendation | BUY — Staged Entry 5% |
| Entry Zone | T1: $85-95 / T2: $72-84 / T3: $60-71 |
| Blended FV | $226 (ESG-adj $215) |
| MOS | +148% |
| Stop Loss | $58 |
| Conviction | 6.7/10 (Emma 7 / Quinn 7 / Bear 6) |
| S&P 500 ref | ~7,400 |

## TL;DR

- Verdict: BUY Staged — NOW ลงมา 51% จาก ATH ถึงระดับที่ทุก scenario ใน Sensitivity Matrix 5x5 (25/25 cells) ให้ upside จากราคา $91
- ทำไม: Wide Moat Agentic AI orchestration platform + WACC 10% DCF FV $267 + EV/Rev 9x FV $241 = Blended $226 = MOS +148%
- Downside Risk: SBC-adjusted FCF ต่ำกว่า headline ~40% + CAGR deceleration risk ที่ revenue >$11B + IT budget freeze recession sensitivity; Stop $58

## Valuation Triangulation (30/30/40)

| Agent | FV | Weight |
|-------|-----|--------|
| Emma DCF/Rev/FCF Blend | $267 | 30% |
| Quinn P-W EV | $229-248 | 30% |
| Bear P-W EV | $184.5 | 40% |
| Blended FV | $226 | 100% |
| ESG-adj FV | $215 | — |

## Sensitivity Matrix 5x5 (Revenue CAGR x WACC)

| CAGR vs WACC | 8% | 9% | 10% | 11% | 12% |
|---|---|---|---|---|---|
| 12% | $182 | $161 | $143 | $128 | $115 |
| 15% | $222 | $196 | $175 | $157 | $141 |
| 18% | $264 | $234 | $209 | $187 | $169 |
| 20% | $295 | $261 | $233 | $209 | $189 |
| 25% | $378 | $335 | $299 | $268 | $242 |

ราคา $91 ต่ำกว่าทุก 25/25 cells = ALL scenarios ให้ upside. Bear extreme (CAGR 12%, WACC 12%) = $115 = +26% upside จาก $91.

## ESG: 6.0/10 (Reconciled) | ESG-adj FV: $215

E: 8/10 (cloud-native, low footprint) | S: 7/10 (strong employee programs, SBC wealth concentration concern) | G: 4.5/10 (SBC 13-16% revenue = systematic dilution, exec comp misalignment vs -51% stock)

## Top Risks

1. SBC-adjusted FCF: headline $3.4B -> real economic $1.6-1.9B (-44%); FCF Yield จริง ~3.7% ไม่ใช่ 4.9%
2. CAGR deceleration: law of large numbers ที่ $11B+; CRM decelerated 25%->8-9% ที่ $15B; WDAY 22%->15-16% ที่ $8B
3. Agentic AI narrative: MSFT Copilot Studio + CRM Agentforce + Oracle compete ใน same space; ยังไม่มี revenue proof
4. IT budget freeze: enterprise macro sensitivity; deal elongation risk Q2-Q3 2026
5. Analyst TP $184 อาจ stale: set ตอน ATH; real consensus post-drop อาจ $120-140

## Recommendation: BUY Staged Entry 5%

T1: $85-95 (50% = 2.5%) — execute ณ ราคาปัจจุบัน ~$91
T2: $72-84 (35% = 1.75%) — add on further decline
T3: $60-71 (15% = 0.75%) — near Bear extreme floor
Stop Loss: $58 | Target Base: $226 | Target Bull: $330 | Horizon: 3-5 ปี`
  }
'@

# Replace the closing ]; with entry + ];
$content = $content -replace '\};\s*\n\];\s*\n\n// Computed', "}$nowEntry`n]`n`n// Computed"

# Write back
Set-Content $dataFile $content -Encoding UTF8
Write-Host "Patch complete: NOW entry added to dashboard/data.js | LAST_UPDATED set to 2026-05-11"
