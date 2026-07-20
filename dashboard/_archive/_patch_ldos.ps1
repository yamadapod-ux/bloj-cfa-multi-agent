# _patch_ldos.ps1 — Leo patch script สำหรับเพิ่ม LDOS ใน dashboard/data.js
# รัน: powershell -ExecutionPolicy Bypass -File dashboard/_patch_ldos.ps1
# วันที่: 2026-05-14

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# อัปเดต LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-09"', 'const LAST_UPDATED = "2026-05-14"'

# LDOS object ใหม่
$ldosEntry = @'
  {
    ticker: "LDOS",
    company: "Leidos Holdings, Inc.",
    date: "2026-05-14",
    sector: "Defense / Government IT Services",
    price: 122.88,
    recommendation: "HOLD",
    blendedFV: 105.00,
    targetBull: 168.00,
    targetBase: 141.00,
    stopLoss: 80.00,
    convictionEmma: 6,
    convictionQuinn: 5,
    convictionBear: 8,
    convictionAvg: 6.3,
    pwEV: 107.15,
    beta: 0.80,
    sharpe1Y: 0.58,
    maxDrawdown: -0.44,
    moat: "Narrow",
    esgRating: "Medium-High Risk",
    esgScore: 5.3,
    entryZone: "$95–115",
    positionSize: "3% (T1: $105-115, T2: $95-105)",
    keyThesis: "Defense/GovIT Narrow Moat — 38,000+ cleared employees + mission-critical switching costs. FCF Yield 7.0%, ROIC 17.5%, P/E 11.2x (41% discount vs sector median 19x). Q1 2026 raised guidance. DOGE fear oversold. Backlog ~$38-40B = ~2.4x annual revenue. First Defense/GovIT in portfolio.",
    topRisk: "DOGE (Dept. of Government Efficiency) budget cuts — unquantifiable Black Swan. Civil segment ($4.5B, 27% revenue) = highest exposure. If DOGE cuts Civil 20% = -$900M revenue = -5.4% total. Bear P-W EV $93 < current price. Beta 0.80 understates DOGE idiosyncratic risk.",
    bullFlipTriggers: [
      "Q2 2026 Book-to-Bill >= 1.05x — pipeline growing despite DOGE",
      "FY2026 Guidance Raise >=3% consecutive second time (post Q2 2026)",
      "DOGE Impact quantified <= $500M/yr revenue (official statement or 10-Q)",
      "Price drops to <= $95 — MOS adequate even vs Bear P-W EV $93",
      "Civil Segment Revenue +-2% YoY in Q2 2026 — DOGE not biting",
    ],
    bearFlipTriggers: [
      "Book-to-Bill < 0.90x for two consecutive quarters",
      "FY2026 Guidance Cut (any amount)",
      "Civil Segment Revenue -10%+ YoY",
      "Net Debt/EBITDA increases above 3.5x",
      "Goodwill Impairment >= $1B",
    ],
    thesisInvalidation: "DOGE specifically targets LDOS via Executive Order OR Major contract cancellation >$1B single contract OR Leverage Crisis/Credit Rating Downgrade",
    reportFile: "../reports/LDOS_2026-05-14.md",
    fullContent: `# 🛡️ LDOS — Leidos Holdings, Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

📌 **ข้อมูลหลัก** | Ticker: LDOS (NYSE) | Date: 2026-05-14 | Price: $122.88 | Market Cap: ~$16.5B | Sector: Defense / Government IT Services | S&P 500 ref: ~$5,650-5,800

🎯 **คำแนะนำ: HOLD / WAIT FOR PULLBACK** | Entry Zone: $95–115 | Blended FV: $105 | ESG-Adj FV: $99 | MOS: -8.6% (slightly overvalued) | Stop Loss: $80 | Max Position: 3%

📊 **Score Dashboard:** Blended FV $105 | MOS -8.6% | ESG 5.3/10 (Medium-High) | Conviction 6.3/10 | Horizon 18-36 mo | Alpha +3.8%/yr t=1.55 (marginal)

> ⚡ **TL;DR:**
> - Verdict: HOLD/WAIT — ย่อ -40.3% จาก 52w High จาก DOGE fears แต่ Blended FV $105 ≈ ราคา $122.88 = ยังไม่ถูกพอ รอ entry $95-115
> - ทำไม: FCF Yield 7%, ROIC 17.5%, Q1 2026 raised guidance = fundamentals ดี แต่ Bear P-W EV $93 = downside risk สูงถ้า DOGE กระทบ Civil segment (27% revenue) มากกว่าคาด
> - Downside: DOGE ตัด Civil 20% + Book-to-Bill <1.0x = FV $65-80 = stop loss $80 triggered

## 💡 Investment Thesis
LDOS เป็น high-quality government contractor ที่ถูก sentiment-driven selloff มากกว่า fundamental impairment Q1 2026 raised guidance + Backlog $38-40B (2.4x annual revenue) = fundamental ยังดี อย่างไรก็ตาม DOGE = unquantifiable Black Swan ที่ต้องการ MOS เพิ่มเติมก่อน entry

## 📊 Peer Comparison
| | LDOS | BAH | SAIC | CACI | LMT | Peer Median |
|--|------|-----|------|------|-----|-------------|
| P/E | 11.2x | ~23x | ~16x | ~19x | ~18x | ~19x |
| FCF Yield | 7.0% (HIGHEST) | 3-4% | 5-6% | 4-5% | 5-6% | ~5% |
| ROIC | 17.5% (BEST) | ~16% | ~13% | ~11% | ~14% | ~14% |
LDOS = Deep Discount P/E (-41% vs median) + Premium FCF Yield (+2pp vs median) = value opportunity IF DOGE <= moderate

## 💰 Valuation (Triangulation 30/30/40)
| Agent | P-W EV | Weight |
|-------|--------|--------|
| Emma (DCF + Relative blend) | $116.61 | 30% |
| Quinn (P-W EV) | $107.15 | 30% |
| Bear (P-W EV conservative) | $93.20 | 40% |
**Blended FV = $105 | ESG-adj $99 | MOS @ $122.88 = -8.6%**

## 📉 Sensitivity Matrix 5x5 (Revenue CAGR x EBITDA Margin)
| CAGR \\ Margin | 6.5% | 7.5% | 8.5% | 9.5% | 10.5% |
|---|---|---|---|---|---|
| 1.5% | $38 | $55 | $71 | $88 | $105 |
| 3.0% | $52 | $72 | $93 | $114 | $135 |
| 4.5% (Base) | $66 | $91 | $115 | $141 | $167 |
| 6.0% | $81 | $110 | $138 | $168 | $199 |
| 7.5% | $96 | $130 | $163 | $196 | $231 |
8/25 cells (32%) justify current price — limited upside scenarios

## 💪 Conviction Score
Emma: 6/10 — Thesis intact แต่ DCF Base limited upside
Quinn: 5/10 — P-W EV $107 < $122.88; entry $95-110
Bear: 8/10 — DOGE Black Swan; Bear P-W EV $93 = AVOID
Avg: 6.3/10 — Gap Emma-Bear = 2pt (near flag threshold)

## 🌱 ESG: 5.3/10 (Medium-High Risk) | ESG-Adj FV $99
E: 6/10 | S: 4/10 (dual-use AI/cyber weapons = ESG fund exclusion) | G: 6/10 (Net Debt 3x concern)
Valuation Impact: -5.6%

## 🔄 What Would Change Our Mind
Bull: Q2 2026 Book-to-Bill >=1.05x / DOGE Impact <=500M / Price <=95 / Civil Revenue +-2% YoY
Bear: Book-to-Bill <0.90x 2Q / Guidance Cut / Civil Revenue -10%+ / Net Debt/EBITDA >3.5x
Invalidation: DOGE targets LDOS specifically / Contract cancellation >$1B / Credit downgrade

## 🎯 Recommendation: HOLD / WAIT FOR PULLBACK
> Rounding FV $105 (ESG-adj $99) < Price $122.88. Entry T1 $105-115 (2%), T2 $95-105 (1%). Stop $80. Target Base $141 / Bull $168. Q2 2026 Book-to-Bill = KEY catalyst. First Defense/GovIT in portfolio.

## ⚠️ Top Risks
1. DOGE cuts Civil segment — HIGH — No historical precedent
2. Continuing Resolution — HIGH — New contract award slowdown
3. Goodwill Impairment $8B+ — MEDIUM — M&A history
4. Leverage Net Debt ~3x EBITDA at 4.5% rate — MEDIUM

## 📅 Catalysts
Q2 2026 Earnings (Jul/Aug): Book-to-Bill + Civil Revenue — HIGH
FY2026 Appropriations Vote (Q3 2026) — HIGH
Q4 2026 Contract Award Season — MEDIUM
Q1 2027 Earnings: First full DOGE-regime quarter — HIGH`
  },
'@

# แทนที่ closing ]; ด้วย entry ใหม่ + ];
$content = $content -replace '\];(\s*\n// Computed)', "$ldosEntry`n];`$1"

Set-Content $dataFile $content -Encoding UTF8
Write-Host "LDOS entry added to dashboard/data.js successfully"
Write-Host "LAST_UPDATED updated to 2026-05-14"
