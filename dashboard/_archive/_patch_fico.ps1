# _patch_fico.ps1 — Leo patch script for FICO entry
# Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\
# Usage: cd "C:\Users\user\Desktop\บลจ\บลจ CFA"; .\dashboard\_patch_fico.ps1

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$reportFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\reports\FICO_2026-05-15.md"

# Read report content
$reportContent = Get-Content $reportFile -Raw -Encoding UTF8
$reportContentEscaped = $reportContent -replace '\\', '\\\\' -replace '`', '\`' -replace '\$\{', '\${'

# Read current data.js
$data = Get-Content $dataFile -Raw -Encoding UTF8

# Update LAST_UPDATED
$data = $data -replace 'const LAST_UPDATED = "[\d-]+";', 'const LAST_UPDATED = "2026-05-15";'

# New FICO entry
$ficoEntry = @"

  {
    ticker: "FICO",
    company: "Fair Isaac Corporation",
    date: "2026-05-15",
    sector: "Financial Analytics / Credit Scoring",
    price: 1088.00,
    recommendation: "HOLD/WAIT",
    blendedFV: 1078.00,
    targetBull: 1900.00,
    targetBase: 1350.00,
    stopLoss: 720.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 8,
    convictionAvg: 7.0,
    pwEV: 1059.00,
    beta: 0.95,
    sharpe1Y: 0.45,
    maxDrawdown: -0.49,
    moat: "Narrow+",
    esgRating: "Moderate Risk",
    esgScore: 5.3,
    keyThesis: "ROIC 68% Best-in-Class + ~90% US lending decisions use FICO Score. Repriced -49% from ATH on DOJ antitrust probe + FHFA VantageScore mandate. At Blended FV \$1,078 — thin MOS, HOLD/WAIT for entry zone \$950-1020.",
    topRisk: "DOJ structural remedy (15% prob) → FV \$350-400; FHFA dual-score erodes mortgage moat; FCF yield 3.1% below risk-free 4.35%",
    entryZone: "\$950–1,020 (T1, 2%) / \$820–950 (T2, 1%)",
    positionSize: "3% max (Quarter-Kelly, regulatory tail adjusted)",
    esgDetail: "E:7 S:4 G:5 | Social: 45M credit invisibles + documented scoring bias vs minorities (CFPB). Gov: CEO 14yr tenure, board allowed 7x price increase now under DOJ",
    sp500Ref: 5620,
    reportFile: "../reports/FICO_2026-05-15.md",
    fullContent: ``PLACEHOLDER_FICO_CONTENT``
  },
"@

# Insert before closing of REPORTS array
$data = $data -replace '(\];[\s]*const SECTORS)', "$ficoEntry`$1"

# Write back
$data | Set-Content $dataFile -Encoding UTF8

Write-Host "FICO entry added to dashboard/data.js"
Write-Host "LAST_UPDATED set to 2026-05-15"
Write-Host "NOTE: Replace PLACEHOLDER_FICO_CONTENT with actual report markdown if needed"
