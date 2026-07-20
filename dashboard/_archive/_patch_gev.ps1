# _patch_gev.ps1 — Patch script สำหรับเพิ่ม GEV entry ใน data.js
# Leo สร้างสำหรับ GEV analysis 2026-05-09
# รัน: .\dashboard\_patch_gev.ps1

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

# อ่านไฟล์
$content = Get-Content $dataFile -Raw -Encoding UTF8

# อัปเดต LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-07";', 'const LAST_UPDATED = "2026-05-09";'

# GEV entry ที่จะเพิ่ม (ใส่ก่อน closing ]; ของ REPORTS array)
$gevEntry = @'
  ,
  {
    ticker: "GEV",
    company: "GE Vernova Inc.",
    date: "2026-05-09",
    sector: "Energy / Power Generation & Grid Infrastructure",
    price: 445.00,
    recommendation: "WAIT",
    blendedFV: 263.00,
    targetBull: 450.00,
    targetBase: 320.00,
    stopLoss: 195.00,
    convictionEmma: 7,
    convictionQuinn: 5,
    convictionBear: 7,
    convictionAvg: 6.0,
    pwEV: 263.00,
    beta: 1.15,
    sharpe1Y: 0.17,
    maxDrawdown: -0.35,
    moat: "Narrow",
    esgRating: "Medium",
    esgScore: 6.2,
    keyThesis: "AI data center power demand + Grid modernization supercycle = GEV Gas Power + Grid direct beneficiary; service backlog $95B+ = durable moat; แต่ราคา ~$440 = MOS -42% จาก Blended FV $263; รอ pullback ลง $320-380",
    topRisk: "Offshore wind drag ยาวกว่าคาด (FY2028) + Momentum reversal ถ้า AI power theme rotation",
    entryZone: "$320-380",
    positionSize: "3% max (Quarter-Kelly — เมื่อถึง entry zone)",
    bullFlipTriggers: [
      "Offshore Wind Restructuring Announced — GEV exit/JV offshore",
      "Gas Power Orders > $8B/Q สอง Quarter ติดต่อกัน",
      "EBITDA Margin > 13% ใน FY2026",
      "Price Pullback ลงมา $320-360",
      "Scott Strazik Insider Buying > $5M"
    ],
    bearFlipTriggers: [
      "Offshore Wind Losses > $1B ใน FY2025",
      "Gas Power Orders < $4B/Q สอง Quarter ติดต่อกัน",
      "EBITDA Margin < 9% ใน FY2025",
      "Hyperscaler AI Capex Cut > 15% by 2+ Companies",
      "US Offshore Wind Federal Policy Reversal"
    ],
    thesisInvalidation: "Nuclear SMR commercial scale 2028-2030 หรือ GEV offshore wind impairment > $3B additional หรือ CEO Scott Strazik departure",
    reportFile: "../reports/GEV_2026-05-09.md",
    fullContent: `# GEV — GE Vernova Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

---

## Recommendation: HOLD / WAIT FOR PULLBACK

**Blended FV: $263 | ESG-adj FV: $247 | MOS: -42% (ณ ราคา ~$440)**

GEV เป็นธุรกิจ world-class ใน megatrend ที่ถูก (AI data center power + Grid modernization) แต่ราคา ~$440 overvalued -42% จาก Blended FV $263

**Entry Zone: $320-380 | Stop Loss: $195 | Max Position: 3%**

## Key Metrics

| Metric | Value |
|--------|-------|
| Blended FV | $263 |
| ESG-adj FV | $247 |
| MOS | -42% |
| Beta | 1.15 |
| Forward Sharpe | 0.17 (vs S&P 500 0.55) |
| Conviction Avg | 6.0/10 |
| ESG Score | 6.2/10 (Medium Risk) |

## Investment Thesis

**Thesis 1: AI Data Center = New Demand Vector for Gas Power**
Hyperscaler AI capex $79.8B/Q (Q1 2026); gas turbines คือ fastest deployable baseload; GEV Gas Power Q4 2024 orders accelerating

**Thesis 2: Grid Modernization Supercycle**
US grid อายุ 40+ ปี; IRA + IIJA = $65B+ grid funding; GEV Electrification growing >20% YoY

**Thesis 3: Service Backlog = Recurring Revenue Moat**
Gas Power service backlog $95B+ = 30+ ปีของ recurring revenue; switching cost > $500M per site

**Thesis 4: Wind Drag Optionality**
Offshore wind drag clearing FY2027+ → EBITDA margin expansion 2-3pp

## Bear Challenges

1. Valuation premium ไม่ justify at $440 (P-W EV $263)
2. Offshore wind timeline may extend to FY2028
3. Gas turbine demand timeline 3-5Y (not immediate)
4. Quinn 13-month history = statistical limitation
5. MOM factor loading +0.50 = theme rotation risk

## Sensitivity Matrix (Rev CAGR x EBITDA Margin)

| Rev CAGR | 8% Margin | 12% Margin | 16% Margin |
|----------|-----------|-----------|-----------|
| 6% | $118 | $185 | $252 |
| 8% | $152 | $235 | $318 |
| 10% | $188 | $287 | $386 |
| 14% | $265 | $398 | $530 |

Cells >= $440: เพียง 2/25 (8%) justify current price

## What Would Change Our Mind

**Bull Flip:** Offshore wind restructuring + Price pullback $320-360 + Gas Power orders > $8B/Q
**Bear Flip:** Wind losses > $1B FY2025 + Gas orders < $4B/Q + Margin < 9%
**Invalidation:** Nuclear SMR commercial by 2028 OR CEO departure

*Full analysis: reports/GEV_2026-05-09.md*
*สร้างโดย Charlie (Orchestrator) | 2026-05-09 | บลจ. CFA*`
  }
'@

# แทนที่ closing ];\n ด้วย GEV entry + closing ];
$content = $content -replace '(\s*\}\s*\]\s*;)', "$gevEntry`n];"

# เขียนไฟล์
[System.IO.File]::WriteAllText($dataFile, $content, [System.Text.Encoding]::UTF8)
Write-Host "GEV entry added to dashboard/data.js successfully"
Write-Host "LAST_UPDATED updated to 2026-05-09"
