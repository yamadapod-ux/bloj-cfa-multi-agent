# _patch_nok.ps1 — เพิ่ม NOK entry เข้า dashboard/data.js
# Leo สร้าง | 2026-05-12 | หลัง Morgan QA PASS

$dataJsPath = "$PSScriptRoot\data.js"
$content = Get-Content $dataJsPath -Raw -Encoding UTF8

$nokEntry = @'
  {
    ticker: "NOK",
    company: "Nokia Corporation",
    date: "2026-05-12",
    sector: "Telecom Equipment / Technology Infrastructure",
    price: 4.80,
    recommendation: "HOLD",
    blendedFV: 8.34,
    targetBull: 15.00,
    targetBase: 8.34,
    stopLoss: 3.50,
    convictionEmma: 6,
    convictionQuinn: 5,
    convictionBear: 6,
    convictionAvg: 5.7,
    pwEV: 9.96,
    beta: 0.90,
    sharpe1Y: -0.28,
    maxDrawdown: -0.505,
    moat: "Narrow",
    esgRating: "Medium",
    esgScore: 6.0,
    keyThesis: "Contrarian value play: Net cash $4.36B (16% market cap) + Nokia Technologies patent licensing (80% margin) undervalued vs hardware business. Post-Huawei ban Western market share gain durable. 5G Wave 2 (private/edge) = next catalyst 2026-2028.",
    topRisk: "Value trap ถ้า revenue ไม่ฟื้น (ROIC 7.3% < WACC 8.5%) + Goodwill €12B impairment risk + FRAND patent reform tail risk + EUR/USD currency risk (ADR)",
    entryZone: "$4.00 – $4.60 (T1) | $3.50-$4.00 (T2) | Catalyst add on Revenue +5% 2Q",
    positionSize: "1.5% max (unusual sector + Narrow moat)",
    reportFile: "../reports/NOK_2026-05-12.md",
    sp500Ref: 5650,
    adrNote: "1 ADR = 1 Ordinary Share HEL:NOKIA | Finnish WHT 15% treaty on dividend | EUR/USD 1.09",
    fullContent: `# 📡 NOK — Nokia Corporation
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

📌 Ticker: NOK (NYSE ADR) | Date: 2026-05-12 | Price: $4.80 | Market Cap: ~$27B | Sector: Telecom Equipment

🎯 Recommendation: HOLD/WAIT FOR PULLBACK | Entry: $4.00-$4.60 | Blended FV: $8.34 | MOS: +42.4% | Stop: $3.50 | Max Position: 1.5%

📊 Score: Blended FV $8.34 | MOS +42.4% | ESG 6.0/10 | Conviction 5.7/10 | Horizon 2-3Y

> ⚡ TL;DR: HOLD/WAIT — MOS 39% สูงน่าสนใจ แต่ยังขาด catalyst ชัดเจน | NOK มี net cash $4.36B = 16% market cap และ Patent licensing 80% margin แต่ ROIC < WACC และ revenue ยังไม่ฟื้น | Downside Risk: Value trap ถ้า telco capex freeze + goodwill impairment €12B

💪 Conviction:
Emma   ██████░░░░  6/10  — MOS 40.6% + net cash protect; ROIC<WACC กด
Quinn  █████░░░░░  5/10  — P-W EV $9.96; แต่ Sharpe ลบ historical
Bear   ██████░░░░  6/10  — Bear P-W EV $6.62; goodwill + patent risks
Avg    █████░░░░░  5.7/10

## 💡 Investment Thesis
"NOK = Cheap Hardware + Hidden Patent Gem + Net Cash Floor"
1. Nokia Technologies (Patent Licensing) ~80% EBIT margin = Hidden Value
2. Huawei ban = Durable Western market share gain (structural not cyclical)
3. Net Cash $4.36B = 16% Market Cap = Downside Floor
4. 5G Wave 2 (Enterprise/Private) = 2026-2028 growth catalyst
5. India 5G (Jio/Airtel) major contracts

## 💰 Valuation (Triangulation 30/30/40)
Emma DCF P-W: $10.18 (30%) | Quinn P-W EV: $9.96 (30%) | Bear P-W EV: $6.62 (40%)
Pre-ESG Blend: $8.69 | ESG-adj (-4%): $8.34 | MOS @ $4.80: +42.4%

## 📉 Sensitivity Matrix — Rev CAGR × WACC
| CAGR \\ WACC | 7.5% | 8.0% | 8.5% | 9.0% | 10.0% |
|---|---|---|---|---|---|
| +1.0% | $6.20 | $5.55 | $4.95 | $4.40 | $3.50 |
| +2.5% | $8.10 | $7.30 | $6.55 | $5.85 | $4.75 |
| **+4.0%** | $11.80 | $10.70 | **$9.65** | $8.70 | $7.10 |
| +6.0% | $15.50 | $14.10 | $12.80 | $11.60 | $9.50 |
| +8.0% | $19.80 | $18.10 | $16.50 | $15.00 | $12.30 |
80% ของ scenarios ให้ FV > $4.80

## 🌱 ESG: 6.0/10 (Medium Risk) | ESG-Adj FV $8.34
E: 7/10 (net-zero 2040, 5G energy efficient) | S: 5/10 (14,000 layoff, surveillance history) | G: 6/10 (Alcatel-Lucent goodwill, Infinera timing)

## ⚠️ Top Risks
1. Value Trap (Revenue no-recovery): 30% prob
2. Goodwill Impairment €12B: 15% prob — Alcatel-Lucent legacy
3. FRAND Patent Reform: 10-15% prob — THESIS INVALIDATION risk
4. EUR/USD Currency Risk (ADR): 40% prob
5. O-RAN Disruption: 25% prob (long-term moat narrowing)

## 🎯 Recommendation: HOLD/WAIT FOR PULLBACK
Entry T1: $4.00-$4.60 (1.0%) | T2: $3.50-$4.00 (0.5%) | Catalyst Add: +0.5% on Revenue +5% 2Q
Stop: $3.50 | Target Base: $8.34 (+74%) | Bull: $15.00 (+213%)
ADR: Finnish WHT 15% treaty | EUR/USD risk — monitor`,
  },
'@

# แทรก NOK entry ก่อน closing ];
$insertBefore = "];"
$newContent = $content -replace [regex]::Escape($insertBefore), ($nokEntry + "`n" + $insertBefore)

# อัปเดต LAST_UPDATED
$newContent = $newContent -replace 'const LAST_UPDATED = ".*?"', 'const LAST_UPDATED = "2026-05-12"'

Set-Content -Path $dataJsPath -Value $newContent -Encoding UTF8
Write-Host "NOK entry added to data.js successfully | LAST_UPDATED = 2026-05-12"
