# Patch script: Insert NVDA v2 entry into data.js
# Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\
# Usage: .\dashboard\_patch_nvda_v2.ps1

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

# Read current content
$content = Get-Content $dataFile -Raw -Encoding UTF8

# Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-07"', 'const LAST_UPDATED = "2026-05-09"'

# NVDA v2 entry to insert
$nvdaV2Entry = @'
,
  {
    ticker: "NVDA",
    company: "NVIDIA Corporation",
    date: "2026-05-09",
    sector: "Technology / Semiconductors",
    price: 116.00,
    recommendation: "BUY",
    blendedFV: 138.00,
    targetBull: 185.00,
    targetBase: 148.00,
    stopLoss: 88.00,
    convictionEmma: 7.5,
    convictionQuinn: 6.5,
    convictionBear: 7.0,
    convictionAvg: 7.0,
    pwEV: 129.73,
    beta: 1.72,
    sharpe1Y: 1.45,
    sharpeForward: 0.55,
    maxDrawdown: -0.44,
    moat: "Wide+",
    esgRating: "Medium",
    esgScore: 6.7,
    reanalysis: true,
    reanalysisVersion: "v2",
    previousAnalysis: "2026-04-24",
    keyThesis: "Re-Analysis v2: Blackwell GB200 ramp confirmed (Q1 FY27 DC Rev $39B). Sovereign AI new vector (Saudi/UAE/India). WACC ลด 10%. ROIC 82-85%. Blended FV ขึ้นจาก $128 → $138. MOS +19%.",
    topRisk: "ASIC disruption escalation (Google/Amazon/Meta training ASIC) + US-China trade truce expiry Jul 2026",
    entryZone: "$105-120 (T1) / $90-100 (T2)",
    positionSize: "7% (staged — maintain)",
    sp500Ref: 5650,
    reportFile: "../reports/NVDA_2026-05-09.md",
    fullContent: `# NVDA — NVIDIA Corporation
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth
### Re-Analysis v2 | 2026-05-09 | Previous: 2026-04-24

## 📌 ข้อมูลหลัก

| Field | Detail |
|-------|--------|
| Ticker | NVDA (NASDAQ) |
| วันที่วิเคราะห์ | 2026-05-09 |
| ราคา ณ วันวิเคราะห์ | ~$116.00 |
| Market Cap | ~$2.83T |
| Sector | Technology / Semiconductors |
| S&P 500 ณ วันวิเคราะห์ | ~5,650 |
| Re-Analysis Version | v2 (จาก v1: 2026-04-24) |

## 🎯 คำแนะนำ

| Item | v1 (2026-04-24) | v2 (2026-05-09) |
|------|-----------------|-----------------|
| Recommendation | BUY (Staged) | BUY (Staged — Maintain) |
| Blended FV | $128 | $138 (+7.8%) |
| MOS | +18.2% | +19.0% |
| Stop Loss | $85 | $88 |
| Target Base | $130 | $148 |
| Target Bull | $160 | $185 |

## ⚡ TL;DR — อ่าน 30 วินาที

- Verdict: BUY (Staged Entry) — MAINTAIN | Blended FV $138 | MOS ~+19%
- ทำไม: Q1 FY2027 DC Rev $39B ยืนยัน Blackwell ramp แข็งแกร่ง + Sovereign AI deals ใหม่ + WACC ลด
- Downside Risk: Bear P-W EV $106.90 (ต่ำกว่าราคา -8%) — ASIC disruption + Trade war คือ top 2 threats

## ⚠️ RE-ANALYSIS CHANGE LOG (v1 → v2)

Key changes: Blended FV $128→$138, WACC 11%→10%, ROIC 75-80%→82-85%, Beta 1.85→1.72, Forward Sharpe 0.40→0.55, Conviction 6.7→7.0, Bear top risk: ASIC escalation + Trade war (new)

## 📊 Score Dashboard

| Blended FV | MOS % | ESG Score | Conviction Avg | Horizon |
|-----------|-------|-----------|---------------|---------|
| $138 | +19.0% | 6.7/10 | 7.0/10 | 3-5 ปี |

## Conviction Bar

Emma   ███████░░░  7.5/10  — Blackwell confirm + WACC ลด thesis แข็งขึ้นมาก
Quinn  ██████░░░░  6.5/10  — Quant metrics ดีขึ้นทั้งหมด alpha t=1.85 best in semi portfolio
Bear   ███████░░░  7.0/10  — มั่นใจ risk ถูก under-price Bear P-W EV < ราคาปัจจุบัน
Avg    ███████░░░  7.0/10

## Recommendation

> BUY — Staged Entry (MAINTAIN from v1)
> Blackwell revenue confirmed. Blended FV $138, MOS +19% at $116
> Entry: $105-120 (T1) / $90-100 (T2) | Stop: $88 | Target: $148/$185

See full report: reports/NVDA_2026-05-09.md`
  }
'@

# Insert before the closing ]; of REPORTS array
$content = $content -replace '(\*Benchmark: S&P 500\*\n`\n  \}\n\];)', "`$1`n$nvdaV2Entry"

# Actually find the exact closing pattern
# Look for the last }]; pattern and insert before it
$insertPoint = '`
  }
];'

$newContent = $content -replace [regex]::Escape($insertPoint), ($nvdaV2Entry + "`n" + $insertPoint)

Set-Content $dataFile $newContent -Encoding UTF8
Write-Host "Patch applied: NVDA v2 entry added to data.js, LAST_UPDATED = 2026-05-09"
