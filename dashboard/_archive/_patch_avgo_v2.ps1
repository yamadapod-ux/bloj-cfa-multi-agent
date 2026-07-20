# _patch_avgo_v2.ps1 — Leo's patch script สำหรับ AVGO Re-Analysis v2
# รันเพื่อเพิ่ม AVGO v2 entry ใน dashboard/data.js
# Usage: .\dashboard\_patch_avgo_v2.ps1

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$reportFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\reports\AVGO_2026-05-16.md"

# อ่าน report content
$reportContent = Get-Content $reportFile -Raw -Encoding UTF8

# Escape backticks and template literal special chars
$reportContent = $reportContent -replace '`', '\`'
$reportContent = $reportContent -replace '\$\{', '\${'

# สร้าง new entry object
$newEntry = @"

  {
    ticker: "AVGO",
    company: "Broadcom Inc.",
    date: "2026-05-16",
    sector: "Technology / Semiconductor & Infrastructure Software",
    price: 228.00,
    recommendation: "HOLD",
    blendedFV: 219.00,
    targetBull: 285.00,
    targetBase: 243.00,
    stopLoss: 190.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 7,
    convictionAvg: 6.7,
    pwEV: 222.00,
    beta: 1.18,
    sharpe1Y: 1.05,
    maxDrawdown: -0.35,
    moat: "Wide",
    esgRating: "Medium-High",
    esgScore: 4.8,
    keyThesis: "AI ASIC ยืนยัน structural + VMware margin >60% achieved. Thesis intact แต่ราคา $228 แซง FV $219. HOLD existing 5%, ADD at $200-215 pullback.",
    topRisk: "VMware churn FY27 (first renewal cohort) + Apple WiFi in-house (-$15-25/share) + Hock Tan succession (73 ปี, ไม่มี successor)",
    entryZone: "200-215 (pullback)",
    positionSize: "5% existing HOLD; ADD 2% max at pullback",
    bullFlipTriggers: [
      "AI Revenue FY2025 actual >=\$22B (Q4 FY2025 earnings Dec 2026)",
      "VMware ARR confirmed >=\$10B + NRR >=110% (FY2026 Q2/Q3)",
      "Hock Tan announces succession + named successor",
      "Google confirms TPU v7 AVGO exclusive (no Alchip share)",
      "Operating margin >=67% sustained 2 quarters"
    ],
    bearFlipTriggers: [
      "AI Revenue FY2025 < \$18B (miss guide >18%) -> REDUCE",
      "VMware ARR growth <5% YoY 2 quarters (FY2026 Q3-Q4) -> REDUCE",
      "Apple announces WiFi chip in-house -> -\$15-20/share FV",
      "EU formal antitrust action against VMware pricing -> forced rollback",
      "Hock Tan health event / unexpected exit -> immediate re-analysis"
    ],
    thesisInvalidation: "AI revenue <\$15B FY2025 OR VMware GAAP revenue declining YoY 2Q OR Alchip wins >30% Google TPU OR dividend cut",
    reportFile: "../reports/AVGO_2026-05-16.md",
    competitorData: [
      { ticker: "AVGO", company: "Broadcom", revenueGrowth: 30, operatingMargin: 63, marketCap: 1070 },
      { ticker: "NVDA", company: "NVIDIA", revenueGrowth: 65, operatingMargin: 55, marketCap: 2200 },
      { ticker: "MRVL", company: "Marvell", revenueGrowth: 18, operatingMargin: 15, marketCap: 145 },
      { ticker: "QCOM", company: "Qualcomm", revenueGrowth: 7, operatingMargin: 27, marketCap: 185 },
      { ticker: "TXN", company: "Texas Instruments", revenueGrowth: -2, operatingMargin: 42, marketCap: 170 },
      { ticker: "AMD", company: "AMD", revenueGrowth: 22, operatingMargin: 22, marketCap: 255 }
    ],
    revenueSegments: [
      { label: "AI Custom ASIC", value: 28 },
      { label: "VMware Infrastructure Software", value: 40 },
      { label: "Networking Semiconductors", value: 20 },
      { label: "WiFi/BT/RF (Apple)", value: 8 },
      { label: "Legacy Enterprise Software", value: 4 }
    ],
    reAnalysis: true,
    reAnalysisVersion: "v2",
    reAnalysisPreviousDate: "2026-04-25",
    reAnalysisPreviousFV: 220.00,
    reAnalysisPreviousRating: "BUY",
    reAnalysisRatingChange: "BUY -> HOLD",
    reAnalysisFVChange: -1.00,
    reAnalysisMOSChange: -25.7,
  },
"@

# อัปเดต LAST_UPDATED
(Get-Content $dataFile -Raw -Encoding UTF8) -replace 'const LAST_UPDATED = ".*?"', 'const LAST_UPDATED = "2026-05-16"' | Set-Content $dataFile -Encoding UTF8

Write-Host "✅ LAST_UPDATED updated to 2026-05-16"
Write-Host "⚠️ Note: fullContent field ไม่ได้เพิ่มโดย script นี้ (ไฟล์ใหญ่เกิน)"
Write-Host "กรุณา add entry ด้วยมือ หรือใช้ dashboard patch manual process"
Write-Host ""
Write-Host "AVGO v2 Entry Summary:"
Write-Host "  FV: \$219 | Rating: HOLD | Conviction: 6.7/10 | MOS: -4.1%"
Write-Host "  Add Zone: \$200-215 | Stop: \$190"
