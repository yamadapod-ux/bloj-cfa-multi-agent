# _patch_learning_log.ps1 — Leo patch script สำหรับเพิ่ม NOW ใน learning-log.md
# รัน: powershell -ExecutionPolicy Bypass -File "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\_patch_learning_log.ps1"

$logFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\learning-log.md"
$content = Get-Content $logFile -Raw -Encoding UTF8

# 1. Add NOW row to Decision History table (after the V row)
$visaRow = '| 2026-05-07 | **V (Visa Inc.)** | **HOLD / WAIT FOR PULLBACK**'
$nowRow = '| **2026-05-11** | **NOW (ServiceNow Inc.)** | **BUY — Staged Entry** — ราคา $91, Blended FV $226, MOS +148%, Max 5% (Quarter-Kelly), Stop $58, Target $226/$330 | รอติดตาม | Wide Moat Agentic AI Orchestration Platform — ลง 51% จาก ATH $186; Sensitivity Matrix 25/25 scenarios upside; SBC-adjusted FCF concern (headline 4.9% → real ~3.7%); Bear P-W EV $184.5 ยังสูงกว่า $91; Triangulation 30/30/40 → $226; Conviction 6.7/10 (Emma 7/Quinn 7/Bear 6); S&P 500 ref ~7,400. |'

# Find the visa row and add NOW after the next line (after the closing |)
$content = $content -replace '(\| 2026-05-07 \| \*\*V \(Visa Inc\.\)\*\*.*?\|)', "`$1`n$nowRow"

# 2. Update CFA Pending concepts count
$content = $content -replace 'Treynor Ratio \[L1\]:.*?7 uses\)', 'Treynor Ratio [L1]: วัด excess return ต่อ 1 unit Beta (systematic risk) — *(รอ CIO confirm — used in HIMS, TMDX, AVGO, RKLB, AMD, MRVL, NVDA v2, NOW — 8 uses)*'
$content = $content -replace 'Sortino Ratio \[L1\]:.*?7 uses\)', 'Sortino Ratio [L1]: Sharpe ที่ใช้เฉพาะ downside deviation แทน total std dev — *(รอ CIO confirm — used in HIMS, TMDX, AVGO, RKLB, AMD, MRVL, NVDA v2, NOW — 8 uses)*'
$content = $content -replace "Jensen's Alpha \[L2\]:.*?7 uses\)", "Jensen's Alpha [L2]: Alpha ที่เหลือหลังหักผล market beta ออก วัด skill ที่แท้จริง — *(รอ CIO confirm — used in HIMS, TMDX, AVGO, RKLB, AMD, MRVL, NVDA v2, NOW — 8 uses)*"
$content = $content -replace 'Cross-sectional Relative Valuation.*?5 uses\)', 'Cross-sectional Relative Valuation / Peer Comp [L2]: เทียบ multiple ของหุ้นกับ peer set ในมิติเดียวกัน highlight position quartile — *(รอ CIO confirm — used in AVGO, RKLB, AMD, MRVL, NVDA v2, NOW — 6 uses)*'
$content = $content -replace 'Investment Thesis Construction.*?5 uses\)', 'Investment Thesis Construction with Bull/Bear Flip Triggers [L3]: framework กำหนดเงื่อนไขวัดได้ที่จะเปลี่ยน rec — *(รอ CIO confirm — used in AVGO, RKLB, AMD, MRVL, NVDA v2, NOW — 6 uses)*'
$content = $content -replace 'ESG Materiality Analysis \[L2-3\]:.*?7 uses\)', 'ESG Materiality Analysis [L2-3]: ระบุ ESG factor ที่กระทบ valuation จริง พร้อม % impact — *(รอ CIO confirm — used in HIMS, TMDX, AVGO, RKLB, AMD, MRVL, NVDA v2, NOW — 8 uses)*'

# 3. Update last updated line
$content = $content -replace '\*อัปเดตล่าสุด: 2026-05-09.*\| Leo\*', '*อัปเดตล่าสุด: 2026-05-11 — NOW Analysis v1 (BUY Staged 5%, Blended FV $226, ESG-adj $215, Stop $58, Conviction 6.7/10, MOS +148%) + S&P 500 ref ~7,400 | Leo*'

# 4. Add NOW CFA Notes section before the last line
$nowCfaSection = @'

### NOW Session 2026-05-11 (Full Report — First Analysis)
- Emma ใช้: DCF (FCFF 2-Stage, Base $267), EV/Revenue (9x NTM, $249), EV/FCF SBC-adj blend ($236), Cross-sectional Peer Comparison (4 peers: ADBE/CRM/MSFT/WDAY), ESG Scorecard (E8/S7/G5→6.7→6.0 reconciled), Economic Moat Wide (5 sources: Switching Cost + Data Moat dominant), Porter's Five Forces, DuPont Modified
- Quinn ใช้: CAPM (Beta 1.10, CAPM ER 10.45%), Carhart 4-Factor (Alpha +3.5%/yr t=1.6 marginal, MOM factor -0.80 = anti-momentum), Sharpe/Sortino/Treynor, VaR -3.2%/CVaR -22%, Sensitivity Matrix 5x5 (Revenue CAGR x WACC — 25/25 cells upside from $91), Kelly Criterion (44-51% → Quarter-Kelly → cap 5%), P-W EV $229-248
- Bear ใช้: 5 systematic challenges: (1) SBC-adjusted FCF -40% from headline (2) CAGR deceleration law of large numbers at $11B+ (3) Agentic AI narrative vs revenue (4) Stale analyst TP $184 (5) IT budget freeze macro; ESG re-score Governance 5→3.5; Bear P-W EV $184.5 (20/40/30/10 distribution); 5 behavioral biases detected; What Would Change Our Mind (5 bull + 5 bear + 3 invalidation)
- Charlie ใช้: Triangulation 30/30/40 → Blended FV $226, Conviction Avg 6.7/10, Sector Concentration Check (Tech SaaS new sector opened)
- Key Outputs: Blended FV $226 (ESG-adj $215), MOS +148%, BUY Staged 5%, Stop $58, Target Base $226/Bull $330
- New Patterns: (1) Sensitivity Matrix 25/25 upside = rare signal for Wide Moat SaaS at deep drawdown (2) SBC-adjusted FCF critical distinction for SaaS names — must disclose both (3) Bear P-W EV > current price = Bear concedes MOS exists even in bear scenario (4) NOW + ADBE = first paired Wide Moat SaaS positions (complementary: Creative vs Workflow)
- Key Risk: SBC dilution systematic, CAGR decel, Agentic AI narrative not yet revenue, IT budget macro
- Top Catalyst: Q1 FY2026 earnings (Q2 2026), Agentic AI revenue disclosure (Q3 2026), SBC/Revenue annual proxy
'@

$content = $content -replace '(\*อัปเดตล่าสุด: 2026-05-11.*\| Leo\*)', "$nowCfaSection`n`n`$1"

Set-Content $logFile $content -Encoding UTF8
Write-Host "Patch complete: NOW added to learning-log.md Decision History + CFA Notes + updated concept counts"
