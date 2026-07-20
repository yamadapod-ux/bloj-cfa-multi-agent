# Simple patch: append STRL entry before ]; and update LAST_UPDATED
# Run from PowerShell: cd "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard" then .\dashboard\_run_strl_patch.ps1

$file = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

# Read as string array to find line numbers
$lines = [System.IO.File]::ReadAllLines($file, [System.Text.Encoding]::UTF8)

# Find line with LAST_UPDATED and replace
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match 'const LAST_UPDATED = "2026-05-06"') {
        $lines[$i] = 'const LAST_UPDATED = "2026-05-07";'
        Write-Host "Updated LAST_UPDATED at line $($i+1)"
        break
    }
}

# Find closing ]; line and insert STRL before it
$insertIndex = -1
for ($i = $lines.Count - 1; $i -ge 0; $i--) {
    if ($lines[$i].Trim() -eq '];') {
        $insertIndex = $i
        Write-Host "Found ]; at line $($i+1)"
        break
    }
}

if ($insertIndex -ge 0) {
    $strlLines = @(
        '  ,',
        '  {',
        '    ticker: "STRL",',
        '    company: "Sterling Infrastructure, Inc.",',
        '    date: "2026-05-07",',
        '    sector: "Industrials / Infrastructure & Construction Services",',
        '    price: 130.00,',
        '    recommendation: "HOLD",',
        '    blendedFV: 96.00,',
        '    targetBull: 128.00,',
        '    targetBase: 96.00,',
        '    stopLoss: 75.00,',
        '    convictionEmma: 7,',
        '    convictionQuinn: 6,',
        '    convictionBear: 7,',
        '    convictionAvg: 6.0,',
        '    pwEV: 85.20,',
        '    beta: 1.10,',
        '    sharpe1Y: 0.85,',
        '    maxDrawdown: -0.38,',
        '    moat: "Narrow",',
        '    esgRating: "Medium-Low",',
        '    esgScore: 5.4,',
        '    keyThesis: "AI data center site work (E-Infrastructure 45%) + IIJA Transportation (38%) = dual tailwind. Blended FV $96 = MOS -26% at current $130. New sector diversification (Infrastructure/Construction) — beta 1.10 reduces portfolio beta. Reclassification: HOLD/WAIT — entry $95-110.",',
        '    topRisk: "Hyperscaler capex cycle peak + DOGE Transportation cuts + fixed-price contract inflation",',
        '    entryZone: "$95-110 (3 tranches — NOT at current $130)",',
        '    positionSize: "3-4% max at entry zone",',
        '    reportFile: "../reports/STRL_2026-05-07.md",',
        '    fullContent: `# STRL — Sterling Infrastructure, Inc. | HOLD/WAIT',
        '',
        '## Key Facts',
        '- Price: ~$130 | Blended FV: $96 | MOS: -26%',
        '- Conviction: Emma 7 / Quinn 6 / Bear 7 = Avg 6.0/10',
        '- Entry Zone: $95-110 (3 Tranches) | Stop Loss: $75',
        '- Sector: Industrials / Infrastructure (NEW sector in portfolio)',
        '',
        '## Business (3 Segments)',
        '- E-Infrastructure ~45%: Data center + fab site work (AI proxy)',
        '- Transportation ~38%: Highway/bridge/aviation (IIJA-backed)',
        '- Building Solutions ~17%: Residential/commercial Sun Belt',
        '',
        '## Valuation Summary',
        '- DCF Base (12% CAGR, 11% margin): $93',
        '- EV/EBITDA 15x: $135',
        '- Peer Relative 12.5x: $111',
        '- Bear P-W EV: $74.60',
        '- Blended FV (method): $105 pre-ESG → $96 ESG-adj (-5.5%)',
        '- Triangulation 30/30/40: $84',
        '- Final Blended FV: $96 | P-W EV: $85.20',
        '',
        '## Recommendation: HOLD/WAIT FOR PULLBACK',
        '- Entry Zone $95-110 (3 tranches)',
        '- Stop Loss $75 | Target Base $96 | Target Bull $128',
        '- Max Position 3-4%',
        '',
        '## Bear Top Risks',
        '1. Hyperscaler capex deceleration (E-Infra lagging indicator)',
        '2. Fixed-price inflation → margin ceiling ~9.5% (not 11.5%)',
        '3. DOGE/Federal IIJA spending cuts (Transportation 38% at risk)',
        '4. Multiple compression (P/E 20x → 12-15x)',
        '5. Current price $130 = Bear FV $86 = -34% to Bear case',
        '',
        '## Conviction Bar',
        'Emma   XXXXXXX...  7/10  — Fundamental thesis clear, margin expansion',
        'Quinn  XXXXXX....  6/10  — P-W EV $88.50 < $130; Kelly negative at $130',
        'Bear   XXXXXXX...  7/10  — Overvalued; hyperscaler cycle underpriced',
        'Avg    XXXXXX....  6.0/10',
        '',
        '*Report: STRL_2026-05-07.md | บลจ. CFA | 2026-05-07*',
        '`',
        '  }'
    )

    # Build new lines array
    $newLines = $lines[0..($insertIndex-1)] + $strlLines + $lines[$insertIndex..($lines.Count-1)]

    [System.IO.File]::WriteAllLines($file, $newLines, [System.Text.Encoding]::UTF8)
    Write-Host "STRL object inserted. File updated successfully." -ForegroundColor Green
} else {
    Write-Host "ERROR: Could not find ]; in file" -ForegroundColor Red
}
