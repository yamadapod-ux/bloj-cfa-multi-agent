# Script เพิ่ม GEV entry ใน learning-log.md
# Leo | 2026-05-09

$logFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\learning-log.md"

# อ่านไฟล์
$content = Get-Content $logFile -Raw -Encoding UTF8

# 1. เพิ่ม GEV row ใน Decision History table (ก่อน separator ---)
$gevDecisionRow = "| **2026-05-09** | **GEV (GE Vernova Inc.)** | **HOLD / WAIT FOR PULLBACK** — Entry zone `$320-380, Stop `$195, Max 3%, Catalyst = Offshore Wind Restructuring | รอติดตาม | Blended FV `$263 (ESG-adj `$247). P-W EV: Quinn `$280 / Bear `$245. MOS -42% ณ ราคา ~`$440. Beta 1.15 (comparable). Forward Sharpe 0.17 < S&P 500 0.55. Conviction 6.0/10 (Emma 7 / Quinn 5 / Bear 7) — Quinn low เพราะ 13-month history. SOTP method ครั้งแรก: Gas Power 22x + Grid 20x + Wind 5x EV/Rev → SOTP FV `$298. Sensitivity: Rev CAGR × EBITDA Margin — ราคา `$440 justify เพียง 8% scenarios. Bear challenges: offshore wind drag FY2028, AI timeline 3-5Y, MOM factor +0.50 = theme rotation risk. |"

# หาตำแหน่ง Visa row แล้วเพิ่ม GEV ต่อจาก
$content = $content -replace "(\| 2026-05-07 \| \*\*V \(Visa Inc\.\)\*\*.*?รอติดตาม.*?\|)", "`$1`n$gevDecisionRow"

# 2. อัปเดต Sensitivity Matrix example list
$content = $content -replace "(\*\*MRVL = Revenue CAGR × Terminal EBIT Margin\*\*)", "`$1 | **GEV = Revenue CAGR × EBITDA Margin Expansion**"

# 3. อัปเดต Pending CIO Confirm count สำหรับ SOTP
$gevSotpEntry = "`n- Sum-of-the-Parts (SOTP) [L2]: ประเมิน conglomerate โดยแยก segment ใช้ multiple ต่างกัน แล้วรวม equity value — *(รอ CIO confirm — used in GEV — 1 use)*"
$gevPorter5Entry = "`n- Porter's 5 Forces [L2]: วิเคราะห์ความเข้มข้นการแข่งขันใน industry ด้วย 5 แรง — *(รอ CIO confirm — used in GEV — 1 use)*"

# เพิ่มหลัง Pre-Profit DCF entry
$content = $content -replace "(- Pre-Profit DCF.*?\*\))", "`$1$gevSotpEntry$gevPorter5Entry"

# 4. อัปเดต Pending count สำหรับ existing items (เพิ่ม GEV)
$content = $content -replace "(Treynor Ratio \[L1\]:.*?— 7 uses\*\))", "`$1".Replace("7 uses", "7 uses")
# (ไม่เพิ่ม count เพราะ GEV ใช้เหมือนกัน แต่ไม่ใช่ 8 uses เพิ่ม)

# 5. เพิ่ม GEV CFA Notes Section
$gevNotes = @"


### GEV Session 2026-05-09 (Full Report — First Analysis)
- Emma ใช้: DCF (FCFF 2-Stage, Base `$245), EV/EBITDA Relative (`$249), SOTP 3-Segment (`$298, ครั้งแรก), Cross-sectional Peer Comparison (ETN/EMR/PWR/NEE — Power/Grid sector), ESG Scorecard (E5/S7/G6.5 → 6.2 reconciled), Economic Moat (Narrow+ — Gas Power Wide, Wind None, Grid Narrow)
- Quinn ใช้: Beta 1.15 (comparable method — GEV 13-month history only), CAPM E(R) 9.5%, Carhart 4-Factor (MOM +0.50 = theme risk), Forward Sharpe 0.17 (vs 2.18 historical distorted), Sortino 0.26, VaR 95% 1M -13.5%, CVaR -18-22%, Max Drawdown -30-35% (forward est.), Sensitivity Matrix 5x5 (Revenue CAGR × EBITDA Margin — margin expansion = key variable), Kelly Criterion (Negative ณ ราคา > FV), P-W EV `$280
- Bear ใช้: 7 Challenges (Valuation/Spin-off/Wind Timeline/AI Narrative/Statistical/ESG/Behavioral), Probability-Weighted Scenario (Bull 10%/Base+ 20%/Base 30%/Bear 30%/Extreme 10%), ESG re-score (E 6→4, G 7→6, reconciled 6.2), Behavioral Biases (Narrative Fallacy/Recency/Anchoring to Backlog/Confirmation/Overconfidence), Bear P-W EV `$245, What Would Change Our Mind (5 Bull + 5 Bear + 3 Invalidation)
- Charlie ใช้: Triangulation 30/30/40 → Blended FV `$263, ESG-adj `$247, MOS -42%, Conviction Average 6.0/10, First Power/Grid sector analysis
- Atlas Macro Brief: Fed 4.25-4.50%, 10Y 4.30%, S&P 500 ~5,650, Hyperscaler AI Capex `$79.8B/Q, Trade Truce active, Grid DOE `$2-3T decade capex needed, Offshore wind headwind (Trump admin)
- Key Outputs: Blended FV `$263 (ESG-adj `$247), HOLD/WAIT, Entry `$320-380, Max 3%, Stop `$195, Catalyst = Offshore Wind Restructuring
- New Frameworks (GEV Session):
  1. **SOTP (Sum-of-the-Parts)** — ครั้งแรกใน track record; เหมาะสำหรับ 3-segment conglomerate; Gas Power (22x) / Grid (20x) / Wind (5x EV/Rev) = SOTP FV `$298 vs DCF `$245 (gap `$53 = value unlock ถ้า wind restructured)
  2. **Comparable Beta Method for Short History** — GEV 13-month history → comparable ETN/EMR/PWR median 1.05 + adjustment 0.10 = 1.15; standard สำหรับ spin-off < 3Y ต่อไป
  3. **"Narrative ถูก, Timeline ผิด" Framework** — ตรวจสอบ implementation timeline (turbine order → delivery 18-36 months) ไม่ใช่แค่ direction ของ thesis
  4. **Offshore Wind Loss Segment Modeling** — loss-making segment ต้อง model separately + stress-test timeline (FY2027 base vs FY2028 bear)
- Key Risk: Offshore wind drag timeline + Momentum reversal (Carhart MOM +0.50) + Spin-off management track record
- Top Catalyst to Watch: Offshore Wind Restructuring/Exit announcement (immediate BUY trigger), Gas Power Q Orders > `$8B/Q × 2Q, EBITDA Margin > 13% FY2026, Price pullback `$320-360
"@

# เพิ่มก่อน *อัปเดตล่าสุด* ท้ายไฟล์
$content = $content -replace "(\*อัปเดตล่าสุด: 2026-05-09 — V.*?\| Leo\*)", "$gevNotes`n`n---`n`n*อัปเดตล่าสุด: 2026-05-09 — GEV Analysis v1 (HOLD/WAIT, Blended FV `$263, Entry `$320-380, First Power/Grid analysis) | Leo*"

# เขียนไฟล์
[System.IO.File]::WriteAllText($logFile, $content, [System.Text.Encoding]::UTF8)
Write-Host "learning-log.md updated with GEV session"
