# _patch_decisions_intu.ps1 — Add INTU row to decisions.md
# Run: powershell -ExecutionPolicy Bypass -File "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\_patch_decisions_intu.ps1"

$decisionsFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\portfolio\decisions.md"
$content = Get-Content $decisionsFile -Raw -Encoding UTF8

# Add INTU row after QCOM row
$qcomRow = '| **2026-05-15** | **QCOM** | **Qualcomm Inc.** | **HOLD/WAIT** | **~$218** | **6.5/10** | **$192** | Mobile AI Tollbooth + Automotive Ramp. Fabless semiconductor (Snapdragon SoC) + QTL patent licensing ($4.8B/yr @70% margin). ROIC 33% = top quartile. FCF $11B/yr. $45B automotive pipeline. Twin binary risks: Apple in-house modem (-$20-25/share) + China 53% revenue (90-day truce Jul 2026 expiry, -$35-53/share if restricted). Blended FV $192 = Emma 40%/Quinn 35%/Bear 25%. MOS -11.9%. ESG-adj FV $184. Kelly negative at $218. Sensitivity Matrix: 28% cells justify $218. First Mobile AI/Automotive semi in portfolio. S&P 500 ref ~5,640. | **$150** |'

$intuRow = '| **2026-05-16** | **INTU** | **Intuit Inc.** | **BUY (Staged)** | **$445** | **7.2/10** | **$559** | Financial Software OS for American SMBs and consumers. QuickBooks Wide Moat (10.1M subscribers, 750+ integrations, switching cost 200-400hrs). TurboTax Narrow+ (87% retention, Live tier growing 25%+). 100M+ financial profiles = AI data moat. -35% from high = entry window. IPS Conviction ≥7.0 → Deploy T1. ESG-adj FV $534. MOS +25.6%. Earnings May 20 = binary event (T1 3% pre, T2/T3 4% post). Sensitivity: 76% cells show upside. First Financial Software in portfolio. S&P 500 ref ~5,620–5,650. | **$348** |'

$content = $content -replace [regex]::Escape($qcomRow), "$qcomRow`n$intuRow"

# Update Rating Distribution section
$content = $content -replace '## Rating Distribution \(2026-05-15 — Post QCOM Analysis\)', '## Rating Distribution (2026-05-16 — Post INTU Analysis)'
$content = $content -replace '\| BUY \| 4 \| NVDA \(v2 Maintain\), AVGO, AMD, ADBE \|', '| BUY | 5 | NVDA (v2 Maintain), AVGO, AMD, ADBE, **INTU (NEW)** |'
$content = $content -replace '\| HOLD/WAIT \| 10 \|', '| HOLD/WAIT | 10 |'
$content = $content -replace '\*\*Average Conviction Score:\*\* 6.38/10 \(อัปเดตหลัง QCOM — QCOM 6.5/10 เพิ่มค่าเฉลี่ยเล็กน้อย\)', '**Average Conviction Score:** 6.45/10 (อัปเดตหลัง INTU — INTU 7.2/10 = highest new addition; pulls avg up)'

# Update Sector Concentration
$content = $content -replace '\*\*Technology / Financial Software\*\* \| \*\*QCOM \(HOLD/WAIT — 5-7% max\) NEW\*\* \| \*\*0% deployed\*\* \| Entry T1 \$190-205 \(3%\) / T2 \$170-190 \(2%\)', '| **Technology / Financial Software** | **INTU (BUY — 7% target) NEW** | **3% deployed (T1 pre-earnings)** | Entry T1 $430-460 (3%) / T2 $395-430 (2.5%) on miss / T3 $450-480 (1.5%) on beat |' + "`n" + '| **Technology / Mobile AI / Automotive Semi** | **QCOM (HOLD/WAIT — 5-7% max)** | **0% deployed** | Entry T1 $190-205 (3%) / T2 $170-190 (2%)'

# Add INTU triggers section before QCOM triggers
$qcomTriggers = '### QCOM (2026-05-15 — First Analysis)'
$intuTriggers = @'
### INTU (2026-05-16 — First Analysis)
- **Q3 FY2026 Earnings Beat (May 20):** Revenue > $8.8B AND EPS > $13.00 → confirm thesis → complete sizing to 7% (T3 add)
- **QuickBooks Online subscriber growth > 15%:** Enterprise Suite ramp confirmed → raise conviction to 8/10
- **IRS Direct File budget/political limitations:** Expansion stalls → structural threat reduced → BUY conviction 8+
- **Credit Karma mortgage recovery:** Fed cuts → refi wave → CK revenue accelerates → ADD signal
- **Price drops to $400 or below:** MOS > 33% from ESG-adj FV $534 → BUY immediately
- **TurboTax unit decline > 5% for 2 consecutive years:** IRS Direct File confirmed disruptive → reduce to 2%
- **QuickBooks subscriber growth below 8%:** Market share reversal → moat cracking → reduce
- **Credit Karma goodwill impairment ($4B+):** Acquisition destroyed → thesis review
- **AI tax prep competitor crosses 10M users:** Disruption real → reduce
- **IRS Direct File reaches 10M returns:** 25%+ of TT addressable market disrupted → explicit model → likely reduce
- **IRS Direct File handles Schedule C + investments comprehensively:** THESIS INVALIDATION — 80%+ of TT market at risk → re-analysis
- **QuickBooks subscriber base negative YoY:** Emergency re-analysis → AVOID consideration
- **Major data breach (10M+ financial profiles):** Immediate sell + re-analysis
- **Price ≤ $430:** T1 entry zone review (3%)
- **Price ≤ $395:** T2 entry zone (2.5% on earnings miss)
- **Price ≤ $348:** Stop loss → AVOID

'@

$content = $content -replace $qcomTriggers, "$intuTriggers`n$qcomTriggers"

# Add Financial Software to Track Record
$matureSection = '### Mature / Cash-Flow-Positive / Wide Moat'
$intuTrack = '- **INTU (BUY 7% target, Conv 7.2)** — Financial Software OS. QB Wide Moat + TT Narrow+. 100M+ data profiles. MOS +25.6%. Earnings May 20 key catalyst.'
$content = $content -replace $matureSection, "$matureSection`n$intuTrack"

# Update last updated timestamp
$content = $content -replace '\*อัปเดตล่าสุด: 2026-05-15.*Leo\*', '*อัปเดตล่าสุด: 2026-05-16 — INTU First Analysis (BUY Staged) — Financial Software ใหม่ในพอร์ต. ราคา $445. Blended FV $559 (ESG-adj $534). Entry T1 $430-460 (3% pre-earnings) / T2 $395-430 (2.5% on miss) / T3 $450-480 (1.5% on beat). Stop $348. Conviction 7.2/10 → IPS Gate PASS → Deploy T1. Earnings May 20 = VERY HIGH catalyst. Sensitivity: 76% cells show upside (Revenue CAGR × WACC). Bear: IRS Direct File $40 haircut + CK goodwill $4.25B risk. First Financial Software sector in portfolio. S&P 500 ref ~5,620–5,650. | Leo*'

# Add Financial Software to Sector Concentration
$sectorTable = '| **Financial Analytics / Credit Scoring** | FICO (HOLD/WAIT — 3% max) | **0% deployed** | Entry T1 $950-1,020 (2%) / T2 $820-950 (1%) |'
$intuSector = '| **Technology / Financial Software** | **INTU (BUY — 7% target) NEW** | **3% target (T1 pre-earnings)** | Entry T1 $430-460 (3%) / T2 $395-430 (2.5%) / T3 $450-480 (1.5%) |'
$content = $content -replace [regex]::Escape($sectorTable), "$sectorTable`n$intuSector"

# Add INTU to Key Monitoring Dashboard
$monitoringHeader = '| **QCOM** | **Apple Modem Contract**'
$intuMonitoring = '| **INTU** | **Earnings Q3 FY2026 (May 20)** | **4 days away** | **Revenue > $8.8B = Beat; < $8.2B = Miss** | **T2 entry if miss; T3 entry if beat** |
| **INTU** | **QuickBooks Subscribers** | **10.1M (+11% YoY)** | **> 15% = Bull Flip T3 add** | **< 8% = moat cracking concern** |
| **INTU** | **IRS Direct File User Count** | **1.2M (FY2025)** | **Plateau = structural risk reduced** | **> 10M = Bear Flip Trigger** |
| **INTU** | **Credit Karma Revenue** | **$1.8-1.9B (flat 3yr)** | **Fed cut → refi recovery = Bull** | **Goodwill impairment > $2B = Bear Flip** |
| **INTU** | **Price** | **$445** | **$430-460 (T1 entry)** | **< $348 = stop loss** |'
$content = $content -replace [regex]::Escape($monitoringHeader), "$intuMonitoring`n$monitoringHeader"

Set-Content $decisionsFile $content -Encoding UTF8
Write-Host "decisions.md updated with INTU entry"
Write-Host "Rating Distribution: BUY count → 5 (NVDA/AVGO/AMD/ADBE/INTU)"
Write-Host "Sector Concentration: Financial Software added"
Write-Host "INTU triggers section added"
Write-Host "Monitoring dashboard updated with INTU"
