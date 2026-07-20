# _patch_mrvl_v2.ps1 — Leo patch script สำหรับ MRVL Re-Analysis v2
# รัน: .\dashboard\_patch_mrvl_v2.ps1
# ผล: เพิ่ม MRVL v2 entry ใน REPORTS array + อัปเดต LAST_UPDATED

$dataFile = "$PSScriptRoot\data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# 1. อัปเดต LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "[^"]*";', 'const LAST_UPDATED = "2026-05-12";'

# 2. เพิ่ม MRVL v2 object ก่อน closing ]; ของ REPORTS array
$mrvlV2Entry = @'

  {
    ticker: "MRVL",
    company: "Marvell Technology, Inc.",
    version: "v2",
    date: "2026-05-12",
    sector: "Technology / Semiconductors (Custom Silicon)",
    price: 171.17,
    recommendation: "TRIM/HOLD",
    blendedFV: 120.00,
    esgAdjFV: 113.00,
    targetBull: 215.00,
    targetBase: 145.00,
    stopLoss: 110.00,
    convictionEmma: 6.0,
    convictionQuinn: 5.5,
    convictionBear: 7.5,
    convictionAvg: 6.3,
    pwEV: 120.12,
    beta: 1.75,
    bearBeta: 2.00,
    maxDrawdown: -0.72,
    moat: "Narrow+ (Conditional)",
    esgScore: 6.2,
    esgRating: "B+",
    keyThesis: "Custom silicon thesis VALIDATED (DC Rev $4.88B FY26, NRE confirmed Amazon+Google). BUT price $171 > Blended FV $120 by 30%. Trim 3→1.5%. Re-entry $130-145.",
    topRisk: "NVDA inference ASIC competition (thesis invalidation); Amazon/Google NRE non-renewal; Trade war TSMC disruption (Aug 2026)",
    entryZone: "$130-145 (re-ADD after trim)",
    positionSize: "1.5% (TRIM from 3%)",
    mosPercent: -29.9,
    sp500Ref: 5810,
    reAnalysisOf: "MRVL_2026-05-06",
    ratingChange: "BUY -> TRIM/HOLD",
    priceChange: "+137.7% (v1 $72 -> v2 $171.17)",
    sensitivityVars: "Revenue CAGR x Terminal EBIT Margin",
    cellsJustifyPrice: "6/25 (24%)",
    reportFile: "../reports/MRVL_2026-05-12.md",
    fullContent: `# MRVL — Marvell Technology, Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth
### Re-Analysis v2 | 2026-05-12 | Previously: BUY $72 → Now: TRIM / HOLD

---

## TL;DR (30 วินาที)

- **Verdict:** TRIM จาก 3% → 1.5% | ราคา $171 สูงกว่า Blended FV $120 ถึง 30% — แต่ thesis ยังสมบูรณ์
- **ทำไม:** Custom silicon story validated แล้ว (DC Rev $4.88B FY26, NRE confirmed) แต่ตลาดราคา forward thesis ล่วงหน้า 3 ปีแล้ว — margin of safety หายไป
- **Downside Risk:** ถ้า 1 ใน 3 hyperscaler ลด ASIC program หรือ NVDA inference ชนะ custom silicon = -30–50% จากราคาปัจจุบัน

---

## Re-Analysis v1→v2 Change Log

| Item | v1 (2026-05-06) | v2 (2026-05-12) |
|------|-----------------|-----------------|
| ราคา | $72.00 | $171.17 (+137.7%) |
| Rating | BUY (Staged) | TRIM/HOLD |
| Blended FV | $112 | $120 |
| MOS | +56% | -29.9% |
| Stop Loss | $52 | $110 |
| Max Position | 3% | 1.5% |
| Conviction | 6.3/10 | 6.3/10 |

---

## Conviction Bar

Emma   ██████░░░░  6.0/10  — Thesis validated; P-W EV $118 < $171; no MOS
Quinn  █████▌░░░░  5.5/10  — P-W EV $149 vs $171 (-13%); Kelly=0%; trim
Bear   ███████▌░░  7.5/10  — Bear case strong; 3yr thesis priced-in
──────────────────────────────────────────────────────
Avg    ██████░░░░  6.3/10  — Gap: Quinn 5.5 vs Bear 7.5 = 2pt (< 3pt flag)

---

## Recommendation: TRIM → HOLD

> ### TRIM จาก 3% → 1.5%: Thesis validated แต่ MOS -29.9%
> ทุก agent คำนวณ P-W EV ต่ำกว่าราคา $171 | Kelly=0% | เหลือ 1.5% เป็น upside optionality

---

*See full report: reports/MRVL_2026-05-12.md*`
  },
'@

# แทนที่ ];\n\nconst ด้วย entry ใหม่ + ];
$content = $content -replace '(\];\s*\n\s*// End of REPORTS)', "$mrvlV2Entry`n];"

# ถ้า pattern ไม่ match ลอง pattern อื่น
if ($content -notmatch 'MRVL.*v2.*2026-05-12') {
    # ลองหาปิด array ท้ายไฟล์
    $lastBracket = $content.LastIndexOf('];')
    if ($lastBracket -gt 0) {
        $content = $content.Substring(0, $lastBracket) + $mrvlV2Entry + "`n];"
        Write-Host "Patched using LastIndexOf method"
    }
}

Set-Content $dataFile $content -Encoding UTF8
Write-Host "data.js patched: MRVL v2 (2026-05-12) added, LAST_UPDATED = 2026-05-12"
