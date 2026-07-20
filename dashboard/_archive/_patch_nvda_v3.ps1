# Patch script — NVDA v3 Re-Analysis entry
# Run: pwsh -File dashboard/_patch_nvda_v3.ps1
# Adds NVDA v3 entry to REPORTS array in data.js

$dataFile = Join-Path $PSScriptRoot "data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "[^"]*";', 'const LAST_UPDATED = "2026-05-16";'

# Mark NVDA v2 entry as superseded (change recommendation label)
$content = $content -replace '(ticker: "NVDA"[^}]*date: "2026-05-09"[^}]*recommendation: )"BUY"', '$1"BUY (SUPERSEDED BY v3)"'

# Build new NVDA v3 entry
$newEntry = @'

  // NVDA v3 — Re-Analysis 2026-05-16
  {
    ticker: "NVDA",
    company: "NVIDIA Corporation",
    date: "2026-05-16",
    version: "v3",
    sector: "Technology / Semiconductors — AI Infrastructure",
    price: 227.00,
    recommendation: "HOLD (Existing) / WAIT (New Entry)",
    blendedFV: 149.00,
    esgAdjFV: 144.00,
    targetBull: 220.00,
    targetBase: 200.00,
    stopLoss: 128.00,
    convictionEmma: 6.0,
    convictionQuinn: 5.5,
    convictionBear: 8.5,
    convictionAvg: 6.7,
    pwEV: 149.18,
    beta: 1.72,
    forwardSharpe: -0.57,
    maxDrawdown: -0.62,
    moat: "Wide",
    esgRating: "Medium",
    esgScore: 6.0,
    mos: -0.344,
    ipsGate: "FAIL (6.7 < 7.0)",
    kellySignal: "NEGATIVE (-7.8)",
    sensitivityCells: "0/25 justify $227",
    preEarnings: "2026-05-28 Q1 FY2027",
    keyThesis: "Thesis ถูก (Blackwell Wide+, Sovereign AI, CUDA 5.5M+ devs) แต่ราคา $227 เกิน FV $149 = MOS -34.4%. Forward Sharpe -0.57 = NEGATIVE. Kelly -7.8. เพิ่ม position ไม่ได้ที่ $227",
    topRisk: "ASIC training 20-25% now → 35-40% FY2028. H200 approved NOT shipped. Multiple compression P/E 54x. US-China truce July 2026 expiry.",
    entryZone: "NEW: $165–185 (4% max) | EXISTING: HOLD 7%",
    positionSize: "HOLD 7% (existing) / 4% max (new entry at $165-185)",
    spxRef: 5825,
    reportFile: "../reports/NVDA_2026-05-16.md",
    fullContent: `# NVDA v3 Re-Analysis — 2026-05-16
Rating: HOLD (Existing) / WAIT (New Entry)
Blended FV: $149 (ESG-adj $144)
MOS at $227: -34.4%
Forward Sharpe: -0.57 (NEGATIVE)
Kelly: -7.8 (NEGATIVE)
Conviction: 6.7/10 (Bear-Quinn gap 3pt FLAG)
IPS Gate: FAIL (6.7 < 7.0)
Pre-Earnings: 28 พ.ค. 2026

Key: Thesis ถูก แต่ราคา $227 เกิน FV $149 ถึง 52%.
New Entry Zone: $165-185 | Stop: $128 (-30% from entry $183)
Existing holders (v1 $110 / v2 $116): HOLD — thesis intact, +96-106% return.
`
  },
'@

# Insert before closing bracket of REPORTS array
$content = $content -replace '(\];[\s\n]*// End REPORTS)', "$newEntry`$1"

# Fallback: insert before last ]; if pattern not found
if ($content -notmatch '\];[\s\n]*// End REPORTS') {
    # Find last ]; and insert before it
    $lastIdx = $content.LastIndexOf('];')
    if ($lastIdx -ge 0) {
        $content = $content.Substring(0, $lastIdx) + $newEntry + $content.Substring($lastIdx)
    }
}

Set-Content $dataFile $content -Encoding UTF8
Write-Host "NVDA v3 entry added to data.js. LAST_UPDATED set to 2026-05-16."
