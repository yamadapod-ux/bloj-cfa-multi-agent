# Learning Log — บลจ. CFA

> Leo ดูแลไฟล์นี้ | Agent ทุกตัวต้องอ่านก่อนทำงาน

---

## CIO Preferences

- **Benchmark comparison**: ทุกรายงานต้องเทียบกับ S&P 500 เสมอ (return, risk-adjusted performance)
- **CFA concept summary**: ท้ายรายงานทุกฉบับต้องมีส่วน "CFA Concepts ที่ใช้" สรุป framework ที่ทีมใช้วิเคราะห์
- **Output format**: ทุก analysis ต้องสร้างไฟล์ `.md` ใน `reports/` ชื่อ `TICKER_YYYY-MM-DD.md` — format เหมือน equity research report จริง (Cover Page, Executive Summary, Investment Thesis, Emma Section, Quinn Section, Bear Section, Valuation, Recommendation, CFA Concepts, Behind the Scenes)
- **Behind the Scenes**: ท้ายรายงานทุกฉบับต้องมีส่วนสรุปการทำงานของทีม (ใครทำอะไร, Bear challenges, Emma counter-arguments)
- **Session logs**: Leo ต้องสร้างไฟล์ใน `session_logs/` ชื่อ `YYYY-MM-DD_HHMM_TICKER.md` ทุก analysis — บันทึก full agent outputs, tool uses, tokens, Bear challenges, final decision
- **Obsidian-ready**: ใช้ Markdown formatting ที่เปิดใน Obsidian ได้ทันที (headers, tables, bullet points)
- **Agent notes**: แต่ละ agent ต้องสร้างไฟล์ของตัวเองใน `agent_notes/[agent]/YYYY-MM-DD_TICKER.md` ทุก analysis — มี methodology, full calculations, CFA concepts, conclusion
- **CFA Footnotes** *(House Rule — 2026-04-24)*: ทุก section heading ในรายงานต้องมี footnote `[CFA Lx: หมวด — Concept]` — ถ้า concept นั้น CIO ยังไม่เรียน ให้ mark `*(ยังไม่เรียน — อธิบาย 1 ประโยค)*`
- **ESG Risk Scorecard** *(House Rule — 2026-04-24)*: Emma ต้องสร้าง ESG section ทุกรายงาน — E/S/G score 1–10, overall rating, material risks พร้อม valuation impact % | Bear ต้อง challenge ESG assessment ด้วย | Framework: CFA L2–3 ESG Investing
- **Sensitivity Matrix** *(House Rule — 2026-04-24)*: Quinn ต้องสร้าง 5×5 matrix เลือก 2 ตัวแปรสำคัญที่สุดของหุ้นนั้น แสดง fair value ทุก scenario | ตัวอย่าง: NVDA = Revenue Growth × WACC | CCJ = Uranium Price × WACC | AVGO = Revenue Growth × Operating Margin | RKLB = Neutron Cadence × Space Systems GM | **AMD = Revenue CAGR × WACC** | **MRVL = Revenue CAGR × Terminal EBIT Margin** | **VEEV = Revenue CAGR × WACC** | **LDOS = Revenue CAGR × EBITDA Margin** | **FICO = Revenue CAGR × DOJ Penalty Probability** | **QCOM = Revenue CAGR × China Revenue % Lost** | **ACGL = Combined Ratio × Premium Growth** | **WPM = Gold Price × Silver Price** | **PGR = Combined Ratio × Premium Growth Rate**
- **Sector/Peer Comparison** *(House Rule — 2026-04-25)*: Emma ต้องสร้างตาราง 3–5 peers ทุกรายงาน เทียบ P/E, EV/EBITDA, ROE, ROIC, Revenue Growth, Gross Margin, Moat | Highlight ว่าหุ้นอยู่ตรงไหนในกลุ่ม (premium/discount/avg) | Framework: CFA L2 Relative Valuation
- **Conviction Level Score** *(House Rule — 2026-04-25)*: Emma/Quinn/Bear ให้คะแนน 1–10 ความมั่นใจในข้อสรุปของตัวเอง | Charlie หา average + note disagreement (≥3 จุด) | ถ้า average < 5 → flag "ข้อมูลไม่พอ ต้องรอ catalyst เพิ่ม" | วางท้าย Executive Summary
- **"What Would Change Our Mind"** *(House Rule — 2026-04-25)*: Bear รับผิดชอบ section ก่อน Recommendation | Bull Flip Triggers (3–5 ข้อวัดได้), Bear Flip Triggers (3–5 ข้อวัดได้), Thesis Invalidation Points | Framework: CFA L3 Investment Thesis & Portfolio Construction
- **Historical Decision Tracking** *(House Rule — 2026-04-25)*: Leo สร้าง/ดูแล `portfolio/decisions.md` — บันทึกทุก analysis (วันที่, ticker, rec, price, conviction, key thesis) | ถ้าวิเคราะห์ ticker เดิมซ้ำ → log การเปลี่ยนแปลง + เหตุผล | สร้าง Track Record ดูย้อนหลังได้
- **Dashboard Auto-Sync** *(House Rule — 2026-04-25)*: Leo อัปเดต `dashboard/data.js` ทุก session — embed `fullContent` (full markdown) เพื่อให้ dashboard render report เต็มไฟล์ได้ | dashboard ต้องเปิดด้วย file:// ได้, responsive, dark minimal, ไม่ใช้ server/API key
- **Visual Report Format** *(House Rule — 2026-05-05 — CIO อนุมัติ)*: ทุกรายงานใหม่ต้องใช้ format 7 elements ต่อไปนี้ (reference: `RKLB_2026-04-29.md`):
  1. **Emoji Section Headers** — ทุก heading มี emoji นำหน้า (เช่น `## 📌 ข้อมูลพื้นฐาน`, `## 🎯 คำแนะนำ`)
  2. **2-Table Header** — แยกเป็น Table 1 (📌) ข้อมูลหลัก + Table 2 (🎯) คำแนะนำ
  3. **Score Dashboard (📊)** — ตารางเดียวใน Executive Summary แสดง: Blended FV | MOS % | ESG Score | Conviction Avg | Investment Horizon
  4. **TL;DR Box (⚡)** — วางก่อน Executive Summary, 3 bullets บังคับ: Verdict / ทำไม / Downside Risk
  5. **Conviction Bar (█░)** — visual ASCII bar chart แทน bullet list (เช่น `Emma  : ████████░░ 8/10`)
  6. **Key Verdict Blockquote** — ใน Recommendation ต้องมี `> **[VERDICT]** — เหตุผล` + entry/stop/target
  7. **Catalyst Timeline ASCII** — `[Q1] ──●── [Q2] ──●── [Q3]` พร้อม magnitude label [HIGH]/[MED]/[LOW]
- **Full Autonomy Mode** *(House Rule — 2026-05-11 — CIO อนุมัติ)*: ทีมตัดสินใจลงทุนได้เองโดยไม่ต้องรอ CIO confirm ทุกครั้ง — หลัง QA PASS execute recommendation ได้ทันที เป้าหมายหลักของระบบ = Professional Investment Education ผ่านการปฏิบัติจริง

---

## Decision History

| วันที่ | หุ้น/หัวข้อ | ผลการตัดสินใจ | ผล | บทเรียน |
|--------|------------|---------------|-----|---------|
| 2026-04-24 | NVDA (NVIDIA Corp.) | BUY (Emma) / HOLD-to-BUY (Quinn) / Bear: เห็นด้วยบางส่วน | รอติดตาม | Emma: Fair Value $125-135, Margin of Safety ปานกลาง, Wide Moat (CUDA ecosystem). Quinn: β=1.85, Sharpe 3Y=1.70 (historical distorted), Forward Sharpe=0.40, Max Drawdown -43%. Bear: Capex cycle risk, ASIC disruption, Base Case downside -15-20% |
| 2026-04-24 | NVDA Full Report | **BUY Staged Entry** — 7% position, Entry1 $110, Entry2 $95-100, Stop $85, Target $130/$160 | รอติดตาม | Blended Fair Value $128. PEG 0.5x undervalued. Forward Sharpe 0.40 ต่ำกว่า benchmark. Probability-Weighted EV $118.75 (+8%). Bear challenges: ASIC disruption + EV gap. Resolution: Staged Entry |
| 2026-04-24 | CCJ (Cameco Corp.) | **HOLD / WAIT FOR PULLBACK** — Entry zone $40–45, Stop $35, Target $55 (base) / $95 (bull) | รอติดตาม | Blended Target $44. P-W EV $51.75 vs price $52.50 = MOS -1.4% (แทบไม่มี). Beta 1.65, Sharpe 0.905 (1Y). Max Drawdown historical -81%. Bear: uranium price dependency, KAP supply risk, Alpha = commodity beta. Position max 2–3% ณ ราคานี้ |
| 2026-04-24 | HIMS (Hims & Hers Health) | **AVOID** — Blended FV $11.40 < ราคา $16.50, Entry zone $10–13 ถ้า FDA clarity | รอติดตาม | P-W EV $12.75 vs ราคา $16.50 = -22.7% downside. Beta 2.4, Sharpe 1Y = -0.85 (Negative), Max Drawdown -77%. Bear: FDA regulatory risk existential, ESG Social High Risk (compounded drugs + class action). Carhart Alpha -32% = FDA idiosyncratic shock. Kelly = 0%. Base DCF $6.30, Bull $18-22 (ตลาด pricing in bull). Blended FV $11.40. |
| 2026-04-24 | TMDX (TransMedics Group) | **AVOID / WAIT** — Blended FV $22–23 < ราคา $40, Entry zone $15–22 ถ้า investigation cleared + 2Q consecutive growth ≥20% | รอติดตาม | P-W EV $22.96 vs ราคา $40 = -42.6% downside. Beta 1.85, Sharpe 1Y = -0.25 (Negative), Max Drawdown -82%. Bear: Investigation risk (DOJ/SEC), NOP decertification risk, XVIVO FDA expansion threat. Carhart Alpha -29% = idiosyncratic investigation shock. Kelly = 0%. Base DCF $15.40, Peer FV $25–35 (discounted). Blended FV $22–23. ESG HIGH RISK (Governance 2–4/10 pending investigation). Moat: NARROW — MedTech regulatory fortress ยังไม่ durable เพราะ XVIVO threat. Sensitivity Matrix: Volume CAGR × Gross Margin — ต้องการ 35% CAGR + 45% margin เพื่อ justify $40. |
| 2026-04-25 | AVGO (Broadcom Inc.) v1 | **BUY — Staged Entry, Defensive Sizing** — 5% position, Tranche1 $170 (40%), Tranche2 $155 (35%), Tranche3 $138 (25%), Stop $130, Target $215 (Base) / $290 (Bull) | รอติดตาม | Blended FV $220 (ESG-adj $223). P-W EV $212. MOS +21.6%. Beta 1.18 (moderate), Sharpe 3Y 1.05, Sortino 1.55, Max DD -31%, Carhart Alpha +5%/yr. Conviction Avg 7.2/10 (Emma 8 / Quinn 7.5 / Bear 6) — disagreement 2pt < 3pt threshold (no flag). Sensitivity: Rev Growth × Op Margin → Base $245, Bull $311, Bear $168. Bear challenges: (1) Google ASIC concentration >40% + Alchip threat (2) VMware churn cycle FY27 (3) Hock Tan key-person 73yrs no succession (4) Carhart α mis-specified (no AI factor). Resolution: size 5% (not 7%), Bear weight 40% in blend, stop $130 below Bear FV floor $140. ESG: Emma 6/10, Bear 4.7/10, reconciled 5.4/10 (-5% impact). Peer Comp: AVGO P/E 21x = 22% discount vs peer median 27x; ROIC 27% top quartile = "premium quality / discount valuation" rare quadrant. **First analysis post-4-rule upgrade — all rules applied successfully.** |
| 2026-04-29 | RKLB (Rocket Lab USA) | **HOLD/WAIT FOR PULLBACK** — Entry zone $16–19 OR Neutron static fire success, Max 2.5% (3 tranches), Stop $11, Target Base $25 / Bull $40–45 | รอติดตาม | Pre-profit binary-event play. Blended FV $20.30 (ESG-adj $18.70) vs ราคา $24.60 = MOS -19.5%. Beta 2.10 (3Y, non-stationary forward 2.5–3.0), Sharpe 0.42 < SPX 0.55, Max DD -71%, CVaR -18%. Carhart Alpha +8.2% (t=1.9, marginal — likely captures defense factor not in 4F). Hypothesis test t=0.76 → fail to reject H₀. Conviction Avg 6.0/10 (Emma 6 / Quinn 5 / Bear 7) — disagreement 2pt < 3pt threshold. Bear challenges: (1) Neutron success P 55% optimistic vs historical 35–45% (2) Timeline slip pattern reliable 12–18mo avg (3) Dilution risk under-modeled — 50% prob 15–20% in 24mo (4) SOTP circular logic — bear-adj $20.40 (5) Beta non-stationary, forward worse (6) Carhart alpha mis-attribution (defense factor missing). Sensitivity Matrix: Neutron Cadence × Space Systems GM. Quinn weights P-W EV $22.30 vs Bear weights $19.24. ESG 4.3/10 reconciled (Emma 5.0 / Bear 3.8) — defense ambiguity (HASTE = ESG-fund exclusion vs catalyst optionality). Triangulation 30/30/40 (Emma/Quinn/Bear) → $20.30 blend. Position 2.5% MAX (Quarter-Kelly + tail correction). **First binary-event play in track record — established framework: HOLD/WAIT default + smaller position vs mature names.** |
| 2026-05-06 | AMD (Advanced Micro Devices) | **BUY — Staged Entry** — 4% position, Tranche1 $100-110 (2%), Tranche2 $88-95 (1.5%), Tranche3 $78-85 (0.5%), Stop $78, Target $148 (Base) / $200 (Bull) | รอติดตาม | Blended FV $148 (ESG-adj $143). P-W EV $145. MOS +41%. Beta 1.75, Sharpe 0.62, Sortino 0.85, Max DD -57%, CVaR -26%, Carhart Alpha +4.2%/yr (t=1.7 marginal). Conviction Avg 6.7/10 (Emma 7 / Quinn 6 / Bear 7) — disagreement 1pt < 3pt threshold (no flag). Sensitivity: Revenue CAGR × WACC → Base $144 ✓. Bear challenges: CUDA moat "invisible wall" (ROCm adoption slower than bulls assume), P/E discount partially justified (ROIC 4.1% vs WACC 10%), Intel 18A recovery risk, Xilinx goodwill impairment. ESG: Emma 6.8, Bear 6.1 → reconciled 6.5/10 (-3% impact). Peer Comp: AMD P/E 22x = 21% discount vs peer median 28x, top-quartile growth = "premium growth, discount valuation" opportunity. Semiconductor exposure post-AMD: 16%. Quarter-Kelly → 4%. |
| 2026-05-06 | MRVL (Marvell Technology) | **BUY — Staged Entry** — 3% position, Tranche1 $65-75 (2%), Tranche2 $55-65 (1%), Stop $52, Target $112 (Base) / $165 (Bull) | รอติดตาม | Blended FV $112 (ESG-adj $106). P-W EV $119. MOS +56% (highest in portfolio). Beta 1.65, Sharpe 0.58, Alpha +3.8%/yr (t=1.48 weakest in BUY universe). Conviction Avg 6.3/10 (Emma 7 / Quinn 6 / Bear 6). Sensitivity: Revenue CAGR × Terminal EBIT Margin (margin expansion = key MRVL driver — variable choice different from AMD). Bear challenges: "Switzerland" narrative masks client concentration (Amazon/Google ~50%), P/E 38x compression risk, goodwill impairment $8B+. Bear P-W EV $100 (binary -12% haircut for client concentration event risk). ESG: Emma 6.7, Bear 5.5 → reconciled 6.2/10 (-5% impact — higher than AMD). Portfolio WARNING: Semiconductor exposure now 19% (NVDA+AVGO+AMD+MRVL). Hard ceiling 20%. Quarter-Kelly → 3%. |
| **2026-05-09** | **NVDA Re-Analysis v2** | **BUY (Staged — Maintain)** — ราคา $116, Blended FV $138 (+7.8% vs v1 $128), MOS +19.0% | รอติดตาม | Blackwell GB200 ramp confirmed (Q1 FY27 DC Rev ~$39B). WACC ลด 11%→10% (rate env.). ROIC 82-85% (จาก 75-80%). Beta 1.72 (จาก 1.85). Forward Sharpe 0.55 (จาก 0.40). Conviction 7.0/10 (จาก 6.7). Bear: ASIC-for-training escalation (Google/Amazon/Meta) + Trade truce expiry Jul 2026 = top risks. Bear P-W EV $106.90 (ต่ำกว่าราคา -8%). Entry T1 $105-120, T2 $90-100. Stop $88. Target $148/$185. S&P 500 ref ~5,650. |
| 2026-05-07 | **V (Visa Inc.)** | **HOLD / WAIT FOR PULLBACK** — ราคา $355, Blended FV $290, Entry zone $285-310, Stop $240, Target $355 (Base) / $420-450 (Bull), Max 4% | รอติดตาม | Asset-light toll road model, Wide moat (network effects), ROIC ~50%, Sharpe 0.95. Blended FV $290.30 (ESG-adj $261). P-W EV: Quinn $320 / Bear $252.50. MOS -18.2%. Beta 0.90 (ไม่ capture DOJ idiosyncratic risk). DOJ antitrust lawsuit 2024 = critical tail risk (35% structural remedy prob). Sensitivity: Revenue CAGR × WACC — $355 justified only in 6/25 cells (24%). ESG 6.4/10 (reconciled). Conviction 6.7/10 (Emma 7/Quinn 6/Bear 7). Life OS push: ล่าช้า — execute แล้ว 2026-05-09. |
| **2026-05-11** | **VEEV (Veeva Systems Inc.)** | **HOLD / WAIT FOR PULLBACK** — ราคา $166, Blended FV $192, Entry T1 $148-158, Stop $118, Max 3% | รอติดตาม | Healthcare SaaS — Wide Moat FDA 21 CFR lock-in (strongest switching cost in portfolio). S&P 500 inclusion May 19. FCF Yield 5.1%, Rev +16.3%, Alpha +4.8%/yr (t=2.1 = highest in portfolio). MOS +15.7% (below 20% BUY threshold). Bear DCF $152 near current price. Vault CRM migration off Salesforce = key unresolved risk. ROIC 115.9% inflated (adj. ~15-20%). Quarter-Kelly = 1%. Conviction 6.7/10 (Emma 7/Quinn 7/Bear 6). ESG 7.3/10 (PBC structure = healthcare SaaS positive). S&P 500 ref ~7,399. |
| **2026-05-14** | **LDOS (Leidos Holdings)** | **HOLD / WAIT FOR PULLBACK** — ราคา $122.88, Blended FV $105, Entry T1 $105-115 (2%), T2 $95-105 (1%), Stop $80, Max 3% | รอติดตาม | Defense/GovIT — Narrow Moat (clearance + switching cost). FCF Yield 7.0%, ROIC 17.5%, P/E 11.2x (41% discount vs sector median 19x). Q1 2026 raised guidance. DOGE = unquantifiable Black Swan (no historical precedent). Bear P-W EV $93 < ราคา $122.88. Blended FV $105 (ESG-adj $99) via 30/30/40. Beta 0.80 = defensive (ต่ำสุดใน universe). Alpha t=1.55 marginal. Conviction 6.3/10 (Emma 6/Quinn 5/Bear 8). Sensitivity: Revenue CAGR × EBITDA Margin — 8/25 cells justify $122.88. ESG 5.3/10 (dual-use AI/cyber weapons). S&P 500 ref ~5,650-5,800. First Defense/GovIT sector in portfolio. |
| **2026-05-15** | **FICO (Fair Isaac Corporation)** | **HOLD / WAIT FOR PULLBACK** — ราคา $1,088, Blended FV $1,078, Entry T1 $950-1,020 (2%), T2 $820-950 (1%), Stop $720, Max 3% | รอติดตาม | Financial Analytics / Credit Scoring — Near-Monopoly FICO Score (~90% US lending decisions). ROIC 68% Best-in-Class (adj. for neg equity ~35-45%). DOJ antitrust probe (ACTIVE) + FHFA VantageScore mandate (IN PROGRESS) = DUAL regulatory binary. Blended FV $1,078 ≈ ราคา $1,088 = MOS -0.9%. Bear 40% weight (DOJ binary pattern). Sensitivity: Revenue CAGR × DOJ Probability — 36% cells justify $1,088. ESG 5.3/10 (Social 4/10 — 45M credit invisibles + scoring bias vs minorities). Moat: NARROW+ (Emma Wide vs Bear Narrow+; reconciled Narrow+). Alpha (5Y) +6.8%/yr t=1.75 (90% conf. marginal). Beta 0.95 (historical) / 1.35 (regulatory 1Y). FCF yield 3.1% < risk-free 4.35%. Conviction 7.0/10 (Emma 7/Quinn 6/Bear 8). S&P 500 ref ~5,620. First Financial Analytics sector in portfolio. KEY INSIGHT: Moat = antitrust target — highest ROIC = most DOJ scrutiny (Moat Paradox). |
| **2026-05-15** | **QCOM (Qualcomm Inc.)** | **HOLD/WAIT** — ราคา $218, Blended FV $192, Entry zone $190-205, Stop $150, Max 5-7% (staged; no deploy — conv 6.5 < 7.0) | รอติดตาม | Semiconductor (QCT) + IP Licensing (QTL) — NARROW+ Moat. Mobile AI Tollbooth thesis: QTL $4.8B/yr @ 70% margin + Automotive $45B pipeline. Twin Binary Risks: Apple in-house modem (-$20-25/share, high prob 2025-2027) + China 53% revenue (US-China truce expiry July 2026, -$35-53/share, 30-40% prob). Blended FV $192 (IPS 40/35/25 Emma/Quinn/Bear). MOS -11.9%. Kelly NEGATIVE at $218. Forward Sharpe 0.18 (very low vs SPX 0.55). Sensitivity: Revenue CAGR × China Revenue % Lost — only 28% cells justify $218. Bear P-W EV $167 vs Quinn $204 vs Emma $196 = wide spread. ESG 6.35/10 (reconciled). Conviction 6.5/10 (Emma 7/Quinn 6/Bear 7). No trade — watchlist only. S&P 500 ref ~5,640. KEY INSIGHT: China Revenue % Lost as Sensitivity V2 (overrides WACC for concentration-risk names). FRAND Licensing = regulatory moat cap. |
| **2026-05-16** | **AVGO Re-Analysis v2** | **HOLD (Existing 5%) / ADD on Pullback $200-215** — ราคา $228, Blended FV $219, MOS -4.1% | รอติดตาม | Thesis intact (AI ASIC confirmed structural, VMware margin >60% achieved, Wide Moat maintained). BUT ราคา $228 > Blended FV $219 = MOS หาย. Forward Sharpe 0.12 (ต่ำกว่า S&P 500 0.55). Kelly ~0% = ไม่มีเหตุผล deploy ใหม่. IPS Conviction 6.7/10 < 7.0 threshold = no T1 auto-deploy. Bear 25% weight (quality name + binary overlay; ไม่ใช่ existential binary = Bear 40%). ESG-adj FV $209 (Governance Bear 3/10 — no succession). Stop Loss updated $130 → $190 (protect +32.6% gains from v1). Emma FV $213 / Quinn P-W EV $229 / Bear P-W EV $209. Key NEW risks: Apple WiFi in-house timeline ชัดขึ้น (-$15-25/share ถ้า confirm) + VMware first renewal cohort FY2027 = THE definitive test. KEY LEARNING: ตลาด "consumed" MOS ทั้งหมดใน 21 วัน (+32%) — FV stable แต่ entry point หายไป. S&P 500 ref ~5,650-5,700. |
| 2026-05-07 | **V (Visa Inc.)** | **HOLD / WAIT FOR PULLBACK** | รอติดตาม | *(duplicate placeholder — see full entry above)* |
| **2026-05-20** | **Dashboard Comprehensive Sync** | เพิ่ม 6 entries (ADBE/NOW/INTU/META/VEEV/FICO) เข้า `dashboard/data.js` + แก้ blendedFV: APP $460→$455, LDOS $105→$107, V $290.30→$288 (Morgan Audit Fix 2026-05-19) + LAST_UPDATED → 2026-05-20 | เสร็จสิ้น | Dashboard พร้อม 21 tickers: ADBE BUY FV $321 (+27% MOS), NOW BUY FV $226 (+148% MOS), INTU BUY FV $559 (+25.6% MOS), META HOLD FV $601 (-0.7% MOS — TC regime ห้าม deploy), VEEV HOLD FV $192 (+15.7% MOS), FICO HOLD FV $1,078 (-0.9% MOS — DOJ binary) |
| **2026-05-21** | **GOOGL v4 (Alphabet Inc.)** | **BUY** — ราคา $388.00 (verified), Blended FV $414, MOS +6.7%, Conviction 7.2/10, Stop $310, T1 4%, Max 8% | รอติดตาม (RISK-ON — ทีมสามารถ deploy T1 ได้) | Full re-analysis จากราคาจริง $388 (v3 ราคา $165.44 ผิด +134%). Google Cloud $20B Q1 2026 (+63% YoY) = 3rd revenue engine materializing. Op margin 36.1% structural. Revenue +22% Q1 2026. Regime RISK-ON 4/4. Growth MOS: Reverse DCF 0.87x < 1.2x + Multiple 58th pct < 70th. Bear P-W EV = $388 = ไม่มี MOS จาก Bear view = fair value entry ไม่ใช่ cheap entry. DOJ structural ruling = existential tail risk (FV $185-233). Morgan CONDITIONAL PASS. KEY LESSON: ราคา Atlas v3 ผิด $165.44 vs $388 = FV, Regime, Recommendation ผิดทั้งหมด — Price verification บังคับก่อน analysis ทุกครั้ง (CLAUDE.md Rule 13). |

| **2026-05-29** | **CRM** | **Salesforce, Inc.** | **BUY (Value Bucket — Staged Entry)** | **$181.00** (Source 1: Salesforce Q1 FY27 press release 2026-05-27; Source 2: valuethemarkets.com 2026-05-27 ✅) | **7.0/10** | **$279** (Emma $351x40% + Quinn $260x30% + Bear $202x30%) | Wide Moat enterprise CRM. FCF $14.4B FY2026 (+9.5% Rev $41.5B). Agentforce ARR $1.2B +205% YoY (Q1 FY27). Revenue re-accel Q4->Q1: +12%->+13%. RPO $72.4B. MOS +54.1%. ROIC 6.29% < WACC 9.5% (EVA negative) key Bear risk. Morgan CONDITIONAL PASS. **S&P 500 ref 7,520.36** (May 27 close). | **$146 (-20% from entry $182.50)** |
| **2026-06-14** | **ACGL (Arch Capital Group)** | **HOLD / WAIT FOR PULLBACK** — ราคา $91.66, Blended FV $106 (ESG-adj $103), Entry zone $80-88, Stop $73, Max 5% | รอติดตาม | **First insurance sector ในพอร์ต.** Specialty insurer 3-engine (Insurance/Reinsurance/Mortgage). Combined ratio 81.7%, ROE 21.3%, BVPS $66.45, P/E 7.05x at sector median, beta 0.31 (defensive ที่สุดในพอร์ต). Bucket VALUE (Residual Income / Justified P/B-ROE — first non-DCF insurance framework). Blended FV $106 (Emma $126×40% + Quinn $97.85×30% + Bear $88×30%). **MOS +15.6% ผ่าน Value gate (≥15%) แต่ Conviction 6.3 < Value gate 7.0 → no deploy = HOLD pattern แรกที่ MOS ผ่าน/Conviction fail.** Bear key risk: peak-ROE anchoring (ถ้า ROE fade→13%, FV~$96; trough 11%→~$86≈ราคา) + soft P&C pricing cycle (cat renewals -10/-20%, ex-cat combined +130bps) + shared blind spot (3 agents ดู metrics ปี cat เบา = collective recency bias). Sensitivity: Combined Ratio × Revenue Growth (CR ครอบงำ growth ขาดลอย). Moat NARROW+. ESG 5.8/10 (E5/S7/G6). FOMC June 16-17 binary → HOLD deploy จนผ่าน. Morgan QA PASS (Data Quality 9/10). S&P 500 ref 7,431.46. |
| **2026-07-06** | **CRDO (Credo Technology Group Holding Ltd)** | **HOLD / WAIT FOR PULLBACK** — ราคา $241.91 (July 2 close), Blended FV $185.86 (ESG-adj $180.3), Entry T1 $175-190 (1.5%) / T2 $150-165 (1.0%), Stop $130, Max 2.5% | รอติดตาม | **1st Semiconductor-Connectivity/Optical-Networking niche sub-sector ในพอร์ต** (AI datacenter AEC cables + optical DSP, distinct จาก MRVL custom-silicon และ ALAB CXL/PCIe). Revenue +205.68% YoY (base-effect small FY2025 base), Gross Margin 68.04%, Op Margin 33.33%, net cash $1,422.4M. **Beta 3.20 = สถิติใหม่สูงสุดในพอร์ตทั้งหมด** (เดิม RKLB 2.10, +52%). Blended FV $185.86 (Emma $226.6×40% + Quinn $189.45×30% + Bear $127.94×30%). MOS -23.2%. **Growth MOS Gate FAIL ทั้ง 2 วิธี**: Reverse DCF 1.65x > 1.2x threshold (implied flat 97% 5yr CAGR vs consensus-anchor 58.8%); Multiple Percentile inconclusive-leans-fail (78% of 52W-high proxy, ไม่มี 5Y history จริง). **Conviction 6.3 < Growth gate 6.5 → NO DEPLOY แม้ Revenue Growth ผ่านสบายมาก (205.68% vs threshold 20%)** — ตัวอย่างชัดเจนว่า revenue growth ผ่านไม่พอสำหรับ Growth bucket ต้องผ่าน conviction+MOS ด้วย (3 independent frameworks: Emma EV/Revenue, Quinn P-W EV, Bear P-W EV คำนวณแยกกันแต่ conviction gate fail ร่วมกัน). Extreme customer concentration: top10≈90% FY2026 revenue, 2 customers ≥10% each, FY2025 single-customer ~67% (SEC 10-K cross-checked, per-customer FY2026 % unverifiable). Kelly NEGATIVE (-51% to -164%). Sensitivity 6/25 cells (24%) justify price. Moat NARROW (cost advantage + switching cost), durability 10-15yr (Emma) vs 5-8yr (Bear — Broadcom 38x market-cap bundling risk). Max Drawdown est. -45% to -65% base, tail -80-83% (cross-validated 3 frameworks). RISK-ON 3/4 majority — Force Deploy active แต่ไม่ override conviction gate. Morgan QA PASS (Data Quality 8/10, 0 HIGH/2 MEDIUM/2 LOW issues). S&P 500 ref 7,483.24. |
| **2026-07-12** | **WPM (Wheaton Precious Metals Corp.)** | **HOLD / WAIT FOR PULLBACK** — ราคา $110.05 (July 10 close), Blended FV $99.20 (ESG-adj ~$97), Entry zone $85-92, Stop $71, Max 5% (tail-hedge diversifier) | รอติดตาม | **First Precious Metals Streaming sector ในพอร์ต (100% ใหม่ — diversification จาก 8 tech/software positions).** Streaming model: จ่ายทอง $479/oz, เงิน $6.58/oz ขายตลาด $4,120/$60.43 = gross margin 85.8%, debt-free (net cash +$2,157M), Wide Moat (cost advantage ถาวร), ESG AAA (MSCI) — Bear challenge ว่าเป็น "structural halo" ของ asset-light model ไม่ใช่ genuine low-risk. Blended FV $99.20 (Emma $100×40% + Quinn $107.32×30% + Bear $90×30%). **MOS -9.9% และ Conviction 6.3 < 7.0 fail ทั้งคู่ → NO DEPLOY** (ACGL peak-cycle pattern ซ้ำ — ต้อง normalize peak metal prices ก่อนคำนวณ MOS). Salobo (Vale) ~38-40% NAV concentration (2x threshold 20%) = key risk, ไม่มี operating control. Beta 1.19, Forward Sharpe **-0.17** (<<S&P 0.55), Kelly NEGATIVE. Return 1Y +23.87% = leveraged commodity beta (gold+silver) ไม่ใช่ genuine alpha (Quinn factor decomposition — first clean commodity-beta-vs-alpha framework). **Sensitivity Matrix Variable ใหม่: Gold × Silver** (แทน WACC/margin) — unfavorable convexity (1.27x downside leverage vs 1.09-1.12x upside ที่ gold record). Regime RISK-ON 3/4 (fresh re-call, Fed hawkish dissenter เดียว). Morgan QA PASS (Data Quality 8.4/10, 0 HIGH, 2 MEDIUM — gold "record high" framing imprecise vs actual 2026 ATH $5,589 Jan 28, ไม่กระทบตัวเลข valuation). S&P 500 ref 7,575.39. |
| **2026-07-22** | **PGR (The Progressive Corporation)** | **HOLD / WAIT FOR PULLBACK** — ราคา $205.90 (July 21 close), Blended FV $208 (ESG-adj $202), Entry zone $175-185, Stop $144, Max 5% | รอติดตาม | **First Auto/Personal-Lines P&C sector ในพอร์ต** (distinct จาก ACGL — Specialty/Reinsurance/Mortgage, Bermuda-domiciled, institutional). Digital/telematics-driven auto & property insurer, Revenue TTM +10.49% (highest ในกลุ่ม peer ALL/TRV/CB/ACGL) แต่ operating margin 16.56% **ต่ำสุดในกลุ่มทั้งหมด** (ACGL 28.94%) — underwriting discipline gap verify ได้ตรงๆ จากข้อมูล. ROE 34.94%, ROIC 28.70%, combined ratio Q2 2026 87.1-87.3 (แย่ลง YoY จาก 86.2, ยังทำกำไร). **หุ้นร่วง 2 รอบใน 1 สัปดาห์**: 15 ก.ค. -9% (June NPW growth ชะลอ +3% + JPMorgan downgrade valuation concern) และ 21 ก.ค. -2.98% (Q2 EPS beat 3.2% แต่ margin concern) — Bear framework ใหม่: "leading indicator ยืนยันด้วย lagging indicator ในสัปดาห์เดียวกัน = confirmed signal ไม่ใช่ noise". Blended FV $208 (Emma $228×40% + Quinn $206×30% + Bear $183×30%; ESG-adj $202) ≈ ราคาปัจจุบัน = **MOS +1.0% แทบไม่มี**. Conviction 6.67 < Value gate 7.0. **ทั้งสอง Value gate ล้มเหลวพร้อมกัน (pattern เดียวกับ WPM 2026-07-12).** Beta 0.25 = new portfolio-low (ต่ำกว่า ACGL 0.31). Insurance-specific valuation (Two-Stage Residual Income + Justified P/B-ROE) ใช้ซ้ำสำเร็จเป็นครั้งที่ 2 หลัง ACGL. Sensitivity: Combined Ratio × Premium Growth Rate — 14/25 cells (56%) support price โดยรวม แต่ cell ตรงจริง (CR 87%/growth 3%) ต่ำกว่าราคา = ตรงกับความกังวลตลาดพอดี. ESG 6.0/10 (E5/S6/G7). Morgan CONDITIONAL PASS (peer P/E data gap + S&P ref date mismatch — ทั้งคู่ transparent flag ไม่กระทบ core decision). RISK-ON 3/4. **Session พิเศษ: ทำงานโดยไม่มี WebSearch/Bash tool access — ใช้ CIO Verified Data Package ตามคำสั่ง CIO explicit แทน**, และไม่สามารถแก้ dashboard/data.js ตรงๆ ได้ (ไฟล์ใหญ่เกิน ~220K tokens) — เตรียม `dashboard/_patch_pgr.py` ไว้แทน ต้อง run ในเซสชันที่มี Python execution. |
| **2026-07-29** | **DXCM (DexCom, Inc.)** | **HOLD / WAIT FOR PULLBACK + EARNINGS CLARITY** — ราคา $74.85 (July 28 close), Blended FV $75.14 (ESG-adj $66.12), Entry zone $58-65, Stop Loss $45, Max Position 0% (NO DEPLOY) | รอติดตาม (Q2 2026 earnings 2026-07-30) | **First Medical Devices/Continuous Glucose Monitoring (CGM) sector ในพอร์ต** (Max Scout Round 15). CGM duopoly กับ Abbott (US share ~74% DXCM). Quality สูงสุดในกลุ่มที่ทีมเคยวิเคราะห์ (ROE 35.62%, ROIC 39.25%, FCF-positive 2 ปีติด, net cash). **Session พิเศษ: Morgan QA Round 1 FAIL — Terminal Growth Rate 3.5% เกินเพดาน sanity-check มาตรฐาน (1-3%)** -> Charlie แก้เป็น 3.0% แล้ว recompute cascade เต็มรูปแบบผ่าน anchor ที่ผูกกัน (Emma FV $75->$72, Bear P-W EV $67.70->$65.96 เพราะ Bear's scenario anchors อ้างอิงตรงกับ Emma's DCF Base/Bull Case, Team Blended FV $76.86->$75.14, MOS +2.7%->+0.4%) -> **Morgan Round 2 PASS (Data Quality 9.5/10)** — recommendation ไม่เปลี่ยน (ยัง HOLD/WAIT) แต่ MOS ยิ่งอ่อนแอชัดเจนขึ้น หลังแก้ไข ยืนยันว่า data correction ไม่จำเป็นต้องเปลี่ยน thesis (pattern เดียวกับ CRM v1->v2). MOS +0.4% AND Conviction 6.17 < 7.0 — ทั้งสอง Value gate ล้มเหลวพร้อมกัน (pattern เดียวกับ WPM/PGR). **DXCM รายงาน Q2 2026 earnings พรุ่งนี้ (2026-07-30)** — historical -40.66% single-day crash precedent เดียวกัน quarter เมื่อ 2 ปีก่อน (2024-07-26 guidance cut) ขณะที่ตลาด priced เพียง ~9% weekly implied move. Conviction Avg 6.17/10 (Emma 6.0/Quinn 5.5/Bear 7.0). Beta 1.45 (5Y monthly) vs 0.84 (3Y daily, correlation only 0.265) — CAPM ไม่เหมาะอธิบายหุ้นนี้. Moat Narrow+ (borderline Wide US/T1D core, Narrow international/Type 2). RISK-ON 3/4 (Atlas 2026-07-29, regime re-call หลัง 17-day stale). S&P 500 ref 7,428.78. |
| **2026-08-01/02** | **RDDT Stop-Loss Breach → HOLD** | **HOLD เต็มจำนวน (ไม่ trim/ไม่ sell)** — ราคาปิด $140.67 < stop $140.75 (breach แรกของพอร์ต, -0.06%) หลัง Q2 2026 earnings **beat ทุกตัวชี้วัด** (Rev $804.9M +61% YoY beat est., EPS $1.25 vs $0.95 est., ARPU +36% YoY) แต่หุ้นร่วง -20.99% วันเดียว (largest single-day drop on record) เพราะไม่มีดีล AI licensing ใหม่กับ Google + คำเตือน "search-referral traffic ผันผวน" | รอติดตาม | Max ตรวจ Bear Flip Triggers (5 ข้อ) + Thesis Invalidation (3 ข้อ) จาก `RDDT_2026-05-30.md` — **zero triggers fired** (ARPU +36% >> floor <20%, revenue beat ไม่ใช่ miss, Google ยังไม่ terminate ดีล — แค่ยังไม่มีดีลใหม่) → สรุปว่าเป็น sentiment/no-new-catalyst sell-off ไม่ใช่ fundamental deterioration. **ยืนยัน 3-tier stop-breach framework (established ACN 2026-06-22)**: 0 triggers fired = HOLD full (RDDT, this event) / 1 Bear Flip fired = TRIM partial (ACN — Q3 FY26 revenue miss + guide cut) / all Invalidation criteria fired = full exit (ยังไม่เคยเกิด). ต่างจาก ACN ตรงที่ ACN มี Bear Flip #1 ยิงจริง ส่วน RDDT ไม่มีข้อไหนยิงเลย — **จำนวน trigger ที่ยิงจริง (ไม่ใช่แค่ "ราคาต่ำกว่า stop") คือตัวกำหนด severity ของ response**. CIO delegated authority ("แล้วแต่พวกนาย เรามาศึกษาเฉยๆ") — Max ตัดสินใจ HOLD เองอย่างเป็นทางการ (commit e253632), อัปเดต `dashboard/portfolio.js` dataIntegrityLog + `portfolio/trade-log.md` แล้ว |
| **2026-08-02** | **ABBV (AbbVie Inc.)** | **HOLD / WAIT FOR PULLBACK** — ราคา $250.94 (July 31 close), Blended FV $251.08 (ESG-adj $226), Entry zone $205-220, Stop Loss $160, Max Position 0% (NO DEPLOY) | รอติดตาม | **Max Scout Round 17 top pick** — claimed ROIC 22.49% + Wide Moat (Rinvoq/Skyrizi), **ทั้งสองตัวเลขถูกปรับหลัง full analysis**: ROIC ที่ถูกต้องคือ 14-16% (team reference, self-calc จาก GAAP NOPAT/Invested Capital), Moat = **Narrow** (ไม่ใช่ Wide — Rinvoq 2037 patent extension มาจาก legal settlement/evergreening ที่ FTC/Congress กำลังเล็งเป้า reform ไม่ใช่ structural moat ถาวร). Healthcare/Pharma sector ที่ 2 ในพอร์ต (หลัง REGN) — diversified large-cap dividend-pharma, คนละ sub-sector profile จาก REGN (specialty biotech-growth). Rinvoq+Skyrizi เติบโต +24%+ YoY ($8.03B/ไตรมาส) ทดแทน Humira erosion -35.9% YoY ($756M) ได้เกินพอ. FCF $19.98B แข็งแรง, dividend sustainable บน cash-basis (coverage 1.63x, GAAP payout ratio 325-336% เป็น misleading เพราะ negative equity). Beta 0.35 (reconciled) = ต่ำสุดในพอร์ตถ้าเพิ่มเข้ามา, dividend yield 2.76% = income stream แรกของพอร์ต — Bear challenge ว่า 10Y yield spike (4.75%) กด valuation ทั้ง tech-growth และ bond-proxy dividend stock พร้อมกันได้ (ไม่ใช่ free-lunch hedge). Blended FV $251.08 (Emma DCF $256×40% + Quinn P-W EV $310.61×30% + Bear P-W EV $185×30%) ≈ ราคา $250.94 = **MOS +0.06% แทบเป็นศูนย์**. Emma/Quinn DCF ต่างกัน 21% ($256 vs $310.61) — **Bear หา root cause ได้ว่าเป็น discount rate methodology gap** (Emma ปรับ credit-risk premium ขึ้นเป็น 8.0% สำหรับ negative equity/Debt-EBITDA 4.93x, Quinn ใช้ CAPM ดิบ 6.17% ไม่ได้ปรับ) ไม่ใช่ growth optimism — ตัวอย่างที่ดีของ triangulation process ทำงานถูกต้อง (หา root cause ก่อนเลือกข้าง). Conviction Avg 6.77/10 (Emma 6.5/Quinn 6.8/Bear 7.0) < Value bucket gate (≥7.0). **ทั้งสอง Value bucket gate ล้มเหลวพร้อมกัน (MOS +0.06% << 15%, Conviction 6.77 < 7.0) — pattern เดียวกับ WPM (2026-07-12), PGR (2026-07-22), DXCM (2026-07-29), ACGL (2026-06-14) — นี่คือ 5th instance ของ "dual gate failure" ในไตรมาสนี้.** Key risks: Rinvoq IRA Medicare negotiation รอบ 2027 (precedent Imbruvica -38%), Skyrizi patent cliff 2033 ไม่มี evergreening settlement รองรับ (revenue at risk >$20B/ปี ใหญ่กว่า Humira peak), 10Y yield spike กด bond-proxy valuation. Morgan QA PASS (Data Quality 8.5/10, 0 HIGH, 1 MEDIUM ไม่กระทบ recommendation). RISK-ON 3/4 (Atlas fresh re-call 2026-08-02, urgent per Max flag หลัง 21-day stale record — confirm เดิม ไม่เปลี่ยน). Max ไม่ deploy (0% position). S&P 500 ref 7,489.72 (July 31 close, verified 2 sources: CNBC/24-7 Wall St + Google Finance). |

| **2026-08-05** | **ETN (Eaton Corporation plc)** | **HOLD / WAIT FOR PULLBACK — NO DEPLOY** — ราคา $444.80 (Aug 4, 2026 close, verified 2 sources), Blended FV $308.25 (ESG-adj $293), Entry T1 $255-270 (1.5%)/T2 $225-245 (1.0%), Stop Loss $210, Max Position 0% | รอติดตาม | **Electrical Equipment/Diversified Industrials — Data Center Infrastructure theme.** AI data-center capex boom แท้จริง (backlog ~307GW, ROE 18.87%), Q2 2026 beat + raised FY26 guide (EPS $13.40-13.60, organic growth 11-13%) แต่ราคาวิ่งขึ้น +14.9% จาก scout price ~$387 ใน ~1 สัปดาห์จนไม่เหลือ margin of safety ในทุก methodology. **Emma-Quinn divergence 3.05x ($145.34 DCF Base vs $443.23 multiple-based P-W EV) — ใหญ่ที่สุดที่ทีมเคยเจอในประวัติศาสตร์ทีม** (เดิม ABBV 21% gap เป็นสถิติสูงสุด) — Bear หา root cause สำเร็จว่าเป็น **circular reasoning** ใน Quinn's base case (exit forward P/E = current forward P/E สมมติว่าตลาด price ถูกอยู่แล้ว) ไม่ใช่ error หรือ growth-assumption gap — reconciled ด้วยการ reweight scenario probabilities เป็น Bear's P-W EV $390.47 (MOS -12.2%, ยังคงบวกกว่า Emma แต่ยัง FAIL gate) — **pattern ใหม่สำหรับ reconcile FV divergence สูง: หา root-cause ของ methodology gap ก่อนเลือกข้าง แทนที่จะ average โดยไม่รู้สาเหตุ** (reusable template สำหรับ divergence ครั้งต่อไป). Blended FV (40/30/30) = $308.25, MOS -30.7% FAIL Value gate (≥15%). Conviction 6.23/10 (Emma 7.2/Quinn 4.5/Bear 7.0, gap Emma-Quinn 2.7 <3.0 threshold ไม่ flag) FAIL deploy gate (≥7.0). **ทั้งสอง Value bucket gate ล้มเหลวพร้อมกัน — 6th instance ของ pattern นี้ในไตรมาสนี้** (ต่อจาก ACGL 2026-06-14, WPM 2026-07-12, PGR 2026-07-22, DXCM 2026-07-29, ABBV 2026-08-02) — data point สำหรับ Vera rolling 4Q/8Q review ว่า Value gate อาจ demanding เกินไปสำหรับ quality names ที่เพิ่งมี catalyst บวก. Moat: **Narrow** (ไม่ใช่ Wide) — Op Margin 17.71% ต่ำสุดในกลุ่ม peer (EMR 24.52%/HON 33.91%/PH 20.87%/VRT 18.94%) ทั้งที่เทรด P/E premium สูงสุด (40.9-44.6x) — VRT (คู่แข่งตรงที่สุด) ชนะทั้ง growth (+26.23%) และ margin ในธุรกิจ overlap โดยตรง. Reverse-DCF confirms ราคา implied perpetual growth 7.71% forever ไม่ sustainable. Beta 1.18, Sharpe (CAPM basis) 0.367 / Sharpe (scenario-implied basis) -0.292 — พลิกลบเมื่อใช้ expected return จริงจาก scenario model. ESG: Emma pre-Bear {e:6,s:6,g:7,overall:6.3} → **Bear-reconciled {e:6,s:5,g:6.5,overall:6.0}** (product-liability tail risk underweight เพราะ customer concentration ไม่มีข้อมูล verify). Morgan CONDITIONAL PASS (Data Quality 9/10, 0 HIGH, 2 MEDIUM transparent-flagged — ESG structured-data-block inconsistency แก้แล้วก่อน embed dashboard + 3 Business Deep Dive subsections NOT AVAILABLE, 1 LOW format). RISK-ON 3/4 (Atlas 2026-08-02 regime record, cross-checked ไม่ stale). **S&P 500 ref 7,741.41** (Google Finance intraday 2026-08-04 ~14:42 EDT, cross-check Yahoo/Bloomberg 7,741.78 — `agent_notes/atlas/2026-08-05_regime.md`, ใหม่กว่า 2026-08-02 record ที่ใช้เดิม 7,489.72 July 31 close). |
| **2026-08-05** | **VRT (Vertiv Holdings Co)** | **HOLD / WAIT FOR PULLBACK — NO DEPLOY** — ราคา $269.93 (Aug 4, 2026 close, verified 2 sources: stockanalysis.com/Yahoo Finance exact match), Blended FV $276.82 (ESG-adj $263.08), Entry T1 $225-240 (1.5%)/T2 $195-210 (1.0%), Stop Loss $185, Max Position 0% | รอติดตาม | **First single-gate-failure สำหรับ Growth bucket** — ต่างจาก dual-gate-fail pattern (MOS+Conviction ล้มเหลวพร้อมกัน) ที่พบซ้ำใน Value bucket 6 ครั้งไตรมาสนี้ (ACGL/WPM/PGR/DXCM/ABBV/ETN) VRT ผ่านทั้ง Revenue Growth gate (+26.23% >> 20%) และ Growth MOS gate (marginal, Method 1 Reverse DCF 0.41× PASS ชัดเจน, Method 2 data gap ทำไม่ได้) แต่ FAIL เฉพาะ Conviction gate เดียว (6.00 < 6.5 required) — data point ใหม่สำหรับ Vera rolling review ว่า valuation near-fair ไม่การันตี conviction ผ่านถ้ามี real unknowns หลายจุดพร้อมกัน (customer concentration ~45-50% unverified/SEC 10-K blocked 403, moat erosion จาก Eaton Boyd-Thermal + Schneider Electric, Method 2 data gap). **Direct competitor cross-validation กับ ETN (วิเคราะห์วันเดียวกัน)** — VRT ชนะ ETN ทั้ง growth (+26.23% vs +15.53%) และ margin (19.96% vs 17.71%) ในธุรกิจ overlap โดยตรง (Data Center Physical Infrastructure/Thermal Management) ยืนยัน insight ที่ ETN's report ระบุไว้แล้วจากมุมมอง VRT เอง — cross-validation ระหว่าง 2 independent analyses. **Emma-Quinn divergence 24.7% ($255 DCF/EV-Revenue Base vs $318.07 multiple-based P-W EV)** — Bear หา root cause สำเร็จว่าเป็น **circular reasoning เดียวกับที่พบใน ETN วันเดียวกัน**: Quinn's base case ใช้ TTM trailing multiple (9.0x) เป็น forward multiple โดยไม่มี independent justification ว่าตลาดจะไม่ de-rate เลยแม้ revenue โต 22% — reconciled ด้วย Bear's reweighted P-W EV $264.68 (ใกล้ Emma มากกว่า, MOS -1.94% เกือบ fair) — ยืนยันว่า framework "หา root-cause ก่อนเลือกข้าง" (established จาก ETN) reusable ข้ามหุ้นได้จริง. Blended FV (40/30/30) = $276.82, **MOS +2.55% knife-edge** (sensitivity แกว่ง -0.1% ถึง +2.6% ขึ้นกับ multiple anchor). Conviction 6.00/10 (Emma 6.0/Quinn 6.5/Bear 5.5, gap สูงสุด Quinn-Bear 1.0 < 3.0 threshold ไม่ flag) FAIL deploy gate (≥6.5). ROIC 37.58%, net cash, FY26 guidance raised 2 รอบติด — ธุรกิจคุณภาพสูงจริง. Moat: **Narrow** (ไม่ Wide) ถูกท้าทายตรงจาก Eaton (Boyd Thermal M&A Mar 2026) + Schneider Electric — เหตุผลเดียวกับที่ ETN ถูกให้ Narrow. Beta 2.05 (สูงสุดในกลุ่ม peer เท่าที่มีข้อมูล). ESG: Emma pre-Bear {e:6,s:6,g:6,overall:6.0} → **Bear-reconciled {e:6,s:6,g:5,overall:5.7}** (customer concentration disclosure opacity = material governance risk ไม่ใช่แค่ data gap ธรรมดา). **Morgan QA Round 1 FAIL (Data Quality 7.4/10, 6 issues: CFA footnotes หาย 6 headings, Competitor Profiles subsection หาย, businessSummary fields หาย, customerConcentration ไม่ structured, Conviction gap label ผิด, CAPM caveat ไม่ชัด) → Charlie แก้ครบ 6 จุด → Morgan Round 2 PASS (Data Quality 8.7/10, 1 MEDIUM ใหม่ non-blocking: competitorData self-entry threatLevel นอก enum — Leo แก้ก่อน embed dashboard โดยใช้ simplified schema ตรงกับ ALAB/ETN precedent)**. RISK-ON 3/4 (Atlas 2026-08-02 regime record, cross-checked ไม่ stale). **S&P 500 ref 7,741.41** (Google Finance intraday 2026-08-04 ~14:42 EDT, cross-check Yahoo/Bloomberg 7,741.78 — `agent_notes/atlas/2026-08-05_regime.md`, ใช้ record เดียวกับ ETN วันนี้). |
---

## What Works
*(Leo จะบันทึกเมื่อ CIO confirm)*

### 2026-05-11 — CIO Full Autonomy Declaration
- **CIO Statement (2026-05-11)**: "พวกนายตัดสินใจได้เต็มที่เลย เหตุที่เราสร้างพวกนายขึ้นมาเพราะต้องการศึกษาการลงทุนแบบมืออาชีพ"
- **Full Autonomy Granted**: ทีมตัดสินใจลงทุนได้เองโดยไม่ต้องขออนุมัติ CIO ทุกครั้ง — หลัง QA PASS execute recommendation ได้ทันที
- **System Purpose Clarified**: เป้าหมายหลักของระบบ = **ศึกษาการลงทุนแบบมืออาชีพ (Professional Investment Education)** — ทุก decision, analysis, mistake คือบทเรียน
- **Teaching Through Practice**: ทีมทำงานเพื่อสอน CIO ผ่านการปฏิบัติจริง ไม่ใช่แค่ report เพื่ออนุมัติ
- **Implication สำหรับ Charlie**: หลัง QA PASS → execute recommendation ได้เลย ไม่ต้องรอ CIO confirm — รายงานผลให้ทราบภายหลัง

### 2026-04-25 — System Upgrade Session
- **CIO confirm: "ทำได้ดีมาก"** — approve approach ทั้ง house rules + dashboard upgrade
- **Reuse infrastructure** ก่อน rebuild — ตรวจของเก่า (vault dashboard, agent prompts) แล้ว upgrade ตรงจุด แทน port ของเก่ามาทั้งดุ้น (`my-bljor/` mock data ไม่ migrate)
- **Status table format** — สรุปงานเป็น table (Feature | Status) ชัด อ่านง่าย CIO ติดตามได้ทันที
- **Backfill via one-shot Python script** + เก็บไฟล์ไว้ (`dashboard/_backfill.py`) เผื่อ re-run — ดีกว่า edit data.js manually 4 ครั้ง
- **file:// + CDN architecture** (marked.js, Chart.js, Tailwind) — ไม่ต้อง server / API key, fallback `<pre>` ถ้า CDN block
- **Embed `fullContent` ใน data.js** — ทำให้ dashboard render report เต็มได้โดยไม่ต้อง fetch (file:// CORS-free)

### 2026-04-25 — AVGO Session (1st post-upgrade)
- **All 4 new house rules applied successfully** — Sector Peer Comp, Conviction Score (avg 7.2), What Would Change Our Mind (5 bull / 5 bear / 4 invalidation triggers), Historical Decision Tracking
- **Triangulation 30/30/40 (Emma/Quinn/Bear)** — first time give Bear 40% weight to counter confirmation bias when 3 methods use shared assumptions → reduces spurious convergence
- **Bear ESG re-score reconciliation** — Emma 6 + Bear 4.7 → mid 5.4 reconciled — productive debate format
- **Disagreement check 2pt < 3pt threshold** working as designed — no false alarm flag

### 2026-04-29 — RKLB Session (2nd post-upgrade, 1st binary-event play)
- **Triangulation 30/30/40 confirmed working for binary-event names** — Bear weight 40% essential when binary tail un-modeled in fundamental DCF
- **Pre-profit DCF Revenue-Based 2-Stage** reused successfully (TMDX → RKLB) — framework solidifying
- **Sensitivity Matrix with independent probability distributions** — Quinn weights vs Bear weights applied to same 5×5 grid → produces different P-W EVs → blend reveals true probability sensitivity (innovation vs single-distribution approach)
- **Position sizing escalation rule emerged**: Mature names (NVDA/AVGO) = 5–7% / Pre-profit binary (RKLB) = 2.5% / Pre-profit regulatory binary (TMDX/HIMS) = AVOID
- **Defense ESG ambiguity handled** — first time ESG factor (HASTE) is BOTH negative (exclusion) AND positive (catalyst optionality); reconciled by treating each angle separately
- **Stop loss methodology refined**: $11 = below Bear extreme case $5 + ~120% buffer (vs AVGO $130 = below Bear floor $140 with 7% buffer) — more buffer for higher-vol pre-profit names

### 2026-05-05 — Visual Report Format Standard (CIO อนุมัติ)
- **CIO อนุมัติ Visual Report Format 7 elements** — implement แล้วใน `RKLB_2026-04-29.md` และ update เป็น standard ใน CLAUDE.md
- **Emoji Section Headers** — ช่วยให้สแกน report ได้เร็ว ลด cognitive load
- **2-Table Header** — แยก fact (📌) กับ action (🎯) ชัดเจน ไม่ปะปนกัน
- **TL;DR Box (⚡) ก่อน Executive Summary** — CIO เห็น verdict ทันทีโดยไม่ต้องอ่านทั้งหมดก่อน
- **Conviction Bar แบบ visual (█░)** — อ่านความเห็นของแต่ละ agent ได้เร็วกว่า bullet list
- **Key Verdict เป็น blockquote** — เด่นชัด ไม่หายไปในข้อความ
- **Catalyst Timeline ASCII** — visualize ลำดับ event ที่ต้องติดตามได้ทันที

### 2026-05-06 — AMD + MRVL Session (3rd post-upgrade, 1st paired semiconductor analysis)
- **Sensitivity Matrix Variable Selection is company-specific**: AMD = Revenue CAGR × WACC (growth uncertainty); MRVL = Revenue CAGR × Terminal EBIT Margin (margin expansion is key MRVL uncertainty — not WACC)
- **Binary Risk Haircut on P-W EV**: Bear applied -12% additional haircut to MRVL P-W EV for client concentration event risk not captured by continuous distribution — extends RKLB's binary haircut approach to non-binary-event names with high client concentration
- **Portfolio-Level Sector Concentration Warning**: Bear issued first cross-name portfolio warning — "19% semiconductor exposure approaching ceiling" — demonstrates Bear's role beyond single-name risk
- **Challenger Play Framework**: AMD = "challenger insurance" to NVDA portfolio position — AMD benefits if NVDA supply constrained or CUDA moat cracks; this "paired position logic" is new to portfolio
- **Position Sizing Ladder Confirmed**: Wide moat (NVDA) 7% > Broad platform (AVGO) 5% > Challenger expanding moat (AMD) 4% > Custom silicon niche moat (MRVL) 3% > Pre-profit binary (RKLB) 2.5% > AVOID
- **Alpha Weakness as Position Size Signal**: MRVL alpha t=1.48 < AMD t=1.71 — weaker alpha = smaller position (3% vs 4%); this correlation confirmed across portfolio

### 2026-05-09 — NVDA Re-Analysis v2 (1st re-analysis session)
- **First Re-Analysis session in track record** — establishes framework for future v2/v3/vN re-analyses
- **Re-Analysis Change Log (v1→v2)** — table format showing every change + reason = CIO can track thesis evolution at-a-glance
- **Atlas Macro Brief first** — rate context (WACC -1pp) and trade context (China revenue risk) proved crucial for updating model accurately
- **ASIC-for-training data in v2** — Bear's v1 theoretical warning (ASIC affects inference) upgraded to data-backed concern (Google TPU training Gemini, Amazon Trainium2 6x) — shows value of re-analysis cadence
- **Revenue CAGR debate identified as single most important variable** — Emma 32% vs Bear 22% = $33 FV swing — defined Q2 FY2027 (Aug 2026) as definitive catalyst to watch
- **Triangulation 30/30/40 held and absorbed agent disagreement** — Bear P-W EV $106.90 vs Emma $145 = $38 gap, blend $129.73 reflects both views appropriately

### 2026-05-11 — VEEV Session (5th post-upgrade, 1st Healthcare SaaS analysis)
- **S&P 500 Inclusion Flow Analysis — first time in portfolio**: Quinn computed ~$3.5B passive buying (8.4 days avg volume); Bear correctly challenged as front-run (announcement already priced); consensus = trading catalyst, not valuation catalyst
- **ROIC Adjusted for Excess Cash — important analytical extension**: VEEV ROIC 115.9% (reported) vs ~15-20% (adjusted for $4.5B excess cash in denominator); Bear's correction analytically correct; lesson: always compute both for cash-rich SaaS companies (ADBE, VEEV pattern emerging)
- **Vault CRM Migration as Unmodeled Risk**: VEEV migrating off Salesforce platform (2022 announced, 2025-2026 executing) = creates customer evaluation window; NOT modeled in consensus; Q2 FY2027 (Aug 2026) = THE most important catalyst
- **Healthcare SaaS Moat Type = Regulatory Switching Cost**: FDA 21 CFR Part 11 CSV validation = 18-24 month re-validation to switch = strongest switching cost in portfolio (stronger than CUDA lock-in, stronger than Creative Cloud)
- **Alpha t=2.1 = HIGHEST in portfolio** (NVDA 1.85 / AVBO 1.8 / AMD 1.70 / MRVL 1.48 / VEEV 2.1) — strongest statistical evidence of genuine excess return; BUT Quarter-Kelly = 1% (thin MOS signal) → contradiction resolved: HOLD not BUY
- **PBC Governance Analysis — first PBC company**: Veeva PBC conversion 2021 = legally balances profit + health mission; ESG-fund eligible (positive vs RKLB defense exclusion); foundation for future PBC analysis in other sectors
- **Position Sizing Ladder Extended**: Healthcare Wide Moat SaaS (VEEV) = 3% max — same as MRVL (thin MOS profile + execution risk parity)

### 2026-05-14 — LDOS Session (6th post-upgrade, 1st Defense/GovIT analysis)
- **Defense/GovIT Sensitivity Variable: Revenue CAGR × EBITDA Margin** — สำหรับ GovIT: CAGR = DOGE sensitivity (ถ้า DOGE ตัด = CAGR ลด); Margin = contract mix (fixed-price vs cost-plus); ต่างจาก VEEV/AMD/V ที่ใช้ Revenue CAGR × WACC
- **DOGE as Unquantifiable Black Swan → Bear 40% weight** — ไม่มี historical precedent สำหรับ government efficiency drive ขนาดนี้ → Charlie ให้ Bear 40% weight (pattern เดียวกับ RKLB binary + V DOJ)
- **Clearance Moat = Shared Moat (NARROW only)** — Bear correctly flags: BAH/SAIC/CACI ล้วนมี clearances → ไม่ exclusive → NARROW ไม่ใช่ NARROW+ หรือ WIDE
- **First Counter-cyclical/Defensive Name ใน Portfolio** — LDOS Beta 0.80 = ต่ำสุดใน universe → ลด portfolio beta + excellent diversification กับทุก position
- **Alpha-to-Size Correlation ยืนยันอีกครั้ง** — LDOS Alpha t=1.55 (marginal) → Size 3% (ระหว่าง AMD t=1.70/4% และ MRVL t=1.48/3%) = consistent กับ established ladder
- **Government Contractor Valuation Framework (FIRST USE)**: FCF Yield (7%) primary signal + P/E vs sector median (11.2x vs 19x = 41% discount) + Backlog conversion analysis + DOGE Bear scenario (-20% Civil) = 4 pillars ของ GovIT valuation

### 2026-05-15 — FICO Session (7th post-upgrade, 1st Financial Analytics / Credit Scoring analysis)
- **Sensitivity Variable: Revenue CAGR × DOJ Penalty Probability** — Quinn override ของ Atlas recommendation (WACC); DOJ structural remedy moves FV ~$700 vs WACC ±1% moves only ~$80 → regulatory binary = dominant variable; most company-specific variable selection to date
- **Dual Active Regulatory Binary (DOJ + FHFA simultaneously)** — First name with 2 concurrent active regulatory threats; V had DOJ only; LDOS had DOGE only; FICO = DOJ antitrust probe + FHFA VantageScore mandate both active; Bear 40% weight confirmed consistent with established pattern
- **Moat Paradox Identified** — FICO's ROIC 68% = best-in-class = evidence of monopoly rents = DOJ target; moat quality is inversely related to regulatory safety in some cases; new analytical lens for future high-ROIC names
- **ROIC Negative Equity Adjustment (FICO)** — FICO has negative book equity from buybacks (same issue as VEEV excess cash); Bear correctly adjusted: reported 68% → ~35-45% adjusted; lesson: check for negative equity distortion (different from excess cash distortion but same principle)
- **Antitrust Probability Tree — Pricing Monopoly Type** — 5-scenario DOJ tree different from V (network access antitrust); FICO = pricing power abuse type → outcomes: no action / consent decree / price cap / structural remedy / full case; new framework for future pricing monopoly names (e.g., credit rating agencies, stock exchanges)
- **Social ESG = Credit Access Inequality** — Bear's most important ESG challenge: 45M "credit invisibles" + documented CFPB research on scoring bias vs minorities → FICO monopoly is CFPB/DOJ target partly for social equity reasons; S score 3-4/10; most impactful ESG downgrade since TMDX (Organ Equity)
- **Financial Analytics Sector Framework (FIRST)** — Asset-light B2B data/analytics model; key valuation drivers: pricing power + volume (origination cycles) + software platform growth; key risks: regulatory pricing cap + alternative scoring penetration + macro credit cycle

### 2026-05-15 — QCOM Session (8th post-upgrade, 1st Mobile Semiconductor / IP Licensing analysis)
- **Sensitivity Variable: Revenue CAGR × China Revenue % Lost** — Quinn's override of WACC for V2; China 53% concentration = direct revenue binary event (US-China truce July 2026 expiry); dominates discount rate sensitivity; framework established for any name with >30% revenue in single risky geography/counterparty
- **FRAND Licensing Risk = Regulatory Moat Cap** — QTL 70% margin licensing = regulatory target globally (EU €997M, Korea $865M, China $975M, US FTC); pattern: highest margin IP = most antitrust scrutiny = FRAND cap pressure; applies to IDCC, QRVO, patent licensing companies
- **Moat Paradox (2nd occurrence)** — QTL Wide moat in IP licensing = antitrust target = structural headwind (FRAND rate reduction risk); first seen in FICO (ROIC 68% = DOJ); QCOM = ROIC 33% + QTL 70% margin = same pattern; rule: check antitrust exposure for any company with moat-driven margins >50%
- **"11th Cell" Combined Binary Scenario** — Bear raised off-matrix scenario: Apple 100% in-house AND China restriction simultaneously = -$18B revenue = FV ~$85-100 = Thesis Invalidation; sensitivity matrices should always note combined event scenario even if matrix can't show it
- **Automotive Pipeline Haircut Rule** — $45B pipeline ÷ 8 years × 65% win rate = $3.6B/yr (not full $5.6B); applies to all pipeline-heavy companies; Bear revised automotive contribution to $3.5B by FY2027 (vs Emma bull $5B+)
- **IPS Conviction Gate 6.5 < 7.0 = Watchlist Only** — Blended conviction 6.5 below IPS threshold 7.0 → no auto-deploy T1; QCOM goes to Watchlist; first clean test of IPS conviction gate in semiconductor sector
- **IPS Weight Changed from 30/30/40 to 40/35/25** — Bear weight reduced to 25% vs. historical 40% for pure binary names; rationale: QCOM is NOT pure binary (it's a quality business with binary risks on top); Bear 40% weight reserved for names where binary risk dominates (RKLB, V, LDOS, FICO); new rule: Bear 25% for quality names with binary overlay, Bear 40% for names where binary = existential


### 2026-05-29 — CRM Session (10th post-upgrade, 1st Enterprise SaaS / CRM analysis)
- **Wide Moat + Deep Value Convergence at 7.0**: Emma/Quinn/Bear ให้ Conviction 7.0/10 ทุกคน = strong convergence ที่ Value Bucket Gate (>=7.0) พอดี; first time all three agents agree exact score; Anti-Convergence Protocol NOT triggered (avg=7.0 < 8.0 threshold)
- **Revenue Re-Acceleration as Key Catalyst**: Q4 FY26 +12% -> Q1 FY27 +13% = inflection point; ต่างจาก pure AI hype เพราะ revenue direction เปลี่ยนจริง
- **Morgan CONDITIONAL PASS แต่ Rating ไม่เปลี่ยน**: v1 Morgan QA FAIL (5 HIGH issues) -> v2 แก้ครบ -> Rating BUY ยังคงเดิม; lesson: data correction ไม่ใช่ thesis correction เสมอไป; เมื่อข้อมูลถูกแก้เพื่อ accuracy ผลอาจยิ่งยืนยัน thesis (FV $258->$279, MOS +42.5%->+54.1%)
- **Q1 FY2027 Data Freshness Rule**: Morgan QA FAIL ส่วนหนึ่งเพราะ report ใช้ FY2026 data โดยไม่รวม Q1 FY2027 ที่ออกวันที่ 2026-05-27 (2 วันก่อน analysis date) -- ยืนยัน: ต้องตรวจ earnings release <=30 วันก่อน analysis date เสมอ
- **EVA Negative != AVOID**: ROIC 6.29% < WACC 9.5% = EVA negative แต่ FCF yield 9.77% + Wide Moat + RPO $72.4B = override EVA signal; lesson: EVA negative is a bear challenge not automatic disqualifier for FCF-generative Wide Moat names


### 2026-05-16 — AVGO Re-Analysis v2 (2nd Re-Analysis Session, 9th post-upgrade)
- **Price Audit Fail → Re-Analysis → HOLD: Pattern Confirmed** — ราคา $228 ≈ Blended FV $219 = thesis ดี แต่ entry หาย; FV แทบไม่เปลี่ยน ($220 → $219) แต่ราคา +32% = MOS ถูก "consumed" โดยตลาด; KEY LEARNING: ติดตาม thesis ≠ timing of entry
- **Forward Sharpe 0.12 = Primary Signal สำหรับ HOLD** — ต่ำกว่า S&P 500 (0.55) มาก + Kelly ~0% = สองสัญญาณ quant บ่งชี้ว่าไม่ควร deploy ใหม่ที่ $228; ถ้า pullback $200–210 → Forward Sharpe กลับ ~0.30 = acceptable
- **Bear 25% (ไม่ใช่ 40%) Confirmed for AVGO** — AVGO = quality name with binary overlay (VMware churn, Apple, Hock Tan) แต่ไม่ใช่ existential binary (RKLB/V/LDOS/FICO = Bear 40%); IPS 2026-05-15 rule applied correctly
- **ESG Governance ลดมากขึ้น (G 6→3)** — Bear's ESG G score 3/10 เหตุผล: no succession plan ยังไม่มีประกาศ, Hock Tan mega-comp $160M, EU antitrust pending; ทำให้ ESG-adj FV ลดจาก $223 → $209 (vs v1 ที่ ESG-adj เพิ่ม); NOTE: ESG หัวข้อนี้จะต้อง watch closely
- **Apple WiFi/BT In-house Risk ชัดขึ้น** — Bear identify ว่า Apple AW3 chip ใน Apple Watch = internal already; iPhone WiFi = next logical step (2–4 ปี); FV impact -$15–25/share; Emma underweight ใน v1 และ v2; NOTE สำคัญสำหรับ future monitoring
- **Re-Analysis Change Log v1→v2 (AVGO)** — FV แทบไม่เปลี่ยน ($220→$219), แต่ Rating change BUY→HOLD, MOS +21.6%→-4.1%, Stop Loss $130→$190; pattern เดียวกับ NVDA v2→v3 และ MRVL v1→v2; "Price ran ahead of FV" = recurring theme
- **VMware First Renewal Cohort FY27 = Key Catalyst** — enterprise contracts 3-year signed Nov 2023–2024 = renewal H1 2027; TRUE TEST ของ VMware switching cost moat; Bear's most important near-term risk; monitor VMware ARR quarterly mentions

### 2026-06-14 — ACGL Session (11th post-upgrade, 1st Insurance sector analysis)
- **Insurance Valuation Framework (FIRST) — Residual Income / Justified P/B-ROE แทน FCFF DCF**: Insurance ไม่ใช้ FCFF DCF (float + reserves ทำให้ cash flow ไม่ meaningful); Emma ใช้ Two-Stage Residual Income (PRIMARY $127) + Justified P/B-ROE ($152) + BVPS compounding ($118) → Emma blend $126; Justified P/B = (ROE−g)/(r−g); foundation สำหรับ insurance/bank/financial names ในอนาคต
- **Conviction Gate Fail แม้ MOS Pass = HOLD pattern (FIRST clean occurrence)**: ACGL MOS +15.6% ผ่าน Value gate (≥15%) แต่ Conviction 6.3 < 7.0 → HOLD/WAIT; ต่างจาก HOLD ก่อนหน้า (FICO/V/QCOM) ที่ MOS ก็ไม่ผ่าน; ยืนยันว่า Value bucket ต้องผ่านทั้ง 2 gates (MOS AND Conviction) — MOS เพียงอย่างเดียวไม่พอ deploy
- **Peak-ROE Anchoring Lesson**: MOS +15.6% เป็น illusion จาก peak-ROE extrapolation — Emma FV $126 พึ่ง ROE 21.3% (cyclical peak); Bear ชี้: ที่ ROE 11% trough + g 4%, Justified P/B 1.4x = $93 ≈ ราคาวันนี้; lesson: สำหรับ cyclical names (insurance/commodity/financials) ต้อง normalize ROE/margin ก่อนคำนวณ MOS ไม่งั้น MOS เป็น mid-cycle illusion
- **Beta 0.31 = Lowest in Portfolio = Diversifier Value แต่ False Comfort สำหรับ Tail**: ต่ำสุดในพอร์ต (vs LDOS 0.80, V 0.90, FICO 0.95); ลด portfolio beta ~0.07 ที่ 8% weight; แต่ Bear เตือน: beta ไม่ capture underwriting/cat tail (pattern เดียวกับ V beta 0.90 ไม่ capture DOJ) — CAPM Low-Vol Anomaly ทำให้ Sharpe literal ต่ำเกินจริง → Emma floor CoE ที่ 9.0%
- **Insurance-Specific Sensitivity: Combined Ratio × Revenue Growth**: CR ครอบงำ growth ขาดลอย (CR เลื่อน 12pt = FV ±$45; growth 16pt = FV ±$13); ตลาดที่กลัว soft pricing (growth ลด) โฟกัสผิดตัวแปร — CR คือตัวกำหนด FV จริง; new variable selection สำหรับ insurance sector (vs WACC/margin สำหรับ tech)
- **Shared Blind Spot / Collective Recency Bias (Bear self-critique)**: Bear flag ว่า 3 agents ดู metrics ในปีที่ cat เบา = valuation อิง favorable cat year; ไม่ใช่ Convergence Risk Note (ไม่มี unanimity ≥8) แต่เป็น Bear identifying shared assumption risk — แสดง value ของ Bear แม้ conviction ไม่ converge สูง
- **Portfolio Diversification Gap Identified**: พอร์ตขาด insurance/financials-defensive 100% + semiconductor-heavy → ACGL เป็น diversification candidate ที่ดี แต่ entry discipline (Conviction gate) สำคัญกว่า rushing เข้าเพื่อ diversify

---

### 2026-07-06 — CRDO Session (12th post-upgrade, 1st Semiconductor-Connectivity/Optical-Networking niche sub-sector)
- **First Semiconductor-Connectivity/Optical-Networking Niche Sub-Sector** — CRDO (AEC cables + optical DSP transceivers) เป็น distinct sub-sector จาก MRVL (custom silicon) และ ALAB (CXL/PCIe); ทั้งสามเป็น "AI-connectivity" theme แต่ product/customer-lock-in mechanism ต่างกัน — framework สำหรับแยกแยะ connectivity sub-niches ในอนาคต
- **Beta 3.20 = New Portfolio-High Record** (เดิม RKLB 2.10, +52%) — confirmed จาก Yahoo Finance เพียง 1 reliable source (Macroaxis 4.47 ถูก exclude เพราะ source ไม่ผ่านมาตรฐาน 2-source cross-check) — ยืนยันวินัยการไม่ใช้ unverified source แม้จะทำให้ conservative estimate ดูอนุรักษ์นิยมเกินไป
- **Growth Gate Fail Despite Extreme Revenue Growth Pass — Clean 3rd Occurrence**: Revenue Growth +205.68% ผ่านสบายมาก (>>20% threshold) แต่ Conviction เฉลี่ย 6.3 < Growth gate 6.5 → HOLD ไม่ deploy — ยืนยันชัดเจนว่า Growth bucket ต้องผ่านทั้ง Revenue Growth AND Conviction AND MOS (Reverse DCF/Multiple) พร้อมกัน ไม่ใช่แค่ revenue growth เพียงอย่างเดียว (pattern เดียวกับ ACGL ที่ MOS ผ่านแต่ Conviction fail — คนละ gate แต่หลักการเดียวกัน: ต้องผ่านทุก gate ไม่ใช่ gate เดียว)
- **3 Independent Frameworks Converge on Same Conclusion Despite Different Methods**: Emma (EV/Revenue Target-Multiple), Quinn (Probability-Weighted EV + Kelly + Sensitivity), Bear (independent P-W EV with growth-cliff scenario) — ทั้งสามคำนวณแยกกันโดยไม่มี shared assumption ที่ตั้งใจ แต่สรุปทิศทางเดียวกัน (overvalued, no MOS) = cross-validation ที่แข็งแรง แม้ magnitude ต่างกัน (Emma MOS -6.3% vs Bear -47.1%)
- **Anchoring Bias Self-Detection (Bear)**: Bear flag ว่า Emma และ Quinn ทั้งคู่เลือก 18x EV/Revenue base-multiple อิสระต่อกัน แต่ทั้งคู่ไม่มี peer absolute-revenue data ให้ benchmark จริง — อาจเป็น anchoring บน "current-minus-modest-haircut heuristic" (32.7x ÷ ~2 = 18x) มากกว่า independently-derived fundamental multiple — บทเรียนสำหรับ future sessions ที่ peer data ขาด: ต้อง cross-check ว่า multiple assumption มาจาก anchoring หรือไม่
- **Data Gap Transparency Under Training Knowledge Ban**: Customer/geography FY2026 breakdown, peer P/E-EV/EBITDA-ROE-ROIC ทั้งหมดถูกบันทึกเป็น "DATA NOT AVAILABLE (verified)" แทนการเดา — Morgan ชม "ตัวอย่างที่ดีของการปฏิบัติตามกฎ" — ยืนยันว่าทีมเลือก data-gap transparency มากกว่า fabricate เพื่อความสมบูรณ์ของรายงาน

---

### 2026-07-12 — WPM Session (13th post-upgrade, 1st Precious Metals Streaming sector)
- **First Precious Metals Streaming / Royalty Sector in Portfolio** — WPM (streaming model: จ่าย fixed-cost ต่อ oz แลกสิทธิ์ซื้อทอง/เงินจากเหมือง แล้วขายตลาด) เป็น 100% sector ใหม่ ต่างจาก tech/software 8 positions เดิม — NAV/DCF (annuity-style PV of stream cash flow over life-of-mine) เป็น valuation framework ใหม่ third-type (หลัง FCFF DCF ปกติ + Insurance Residual Income ของ ACGL)
- **Sensitivity Matrix Variable ใหม่: Gold Price × Silver Price** — แทนที่ WACC/margin variables ที่ใช้กับ tech names ทั้งหมด; เกิดจาก WPM มี 2 metal exposures พร้อมกัน (gold 51% / silver 47% Q1'26) ที่ทั้งคู่เป็น swing factor เท่าเทียมกัน — framework สำหรับ multi-commodity-exposure names ในอนาคต
- **Commodity Beta vs Genuine Alpha — First Clean Decomposition**: Quinn แยกชัดเจนว่า WPM return 1Y +23.87% = leveraged gold/silver beta (WPM จริงๆ underperform blended-metal-return ~+41% เพราะ multiple compression + Constancia depletion) ไม่ใช่ manager skill; conviction ในหุ้นนี้ = conviction ในทิศทางโลหะ 3-5 ปี ไม่ใช่ conviction ในบริษัท — บทเรียนสำคัญสำหรับทุก commodity-linked name ในอนาคต (CCJ precedent เคยแตะประเด็นนี้บางส่วน, WPM ทำให้ framework ชัดเจนสมบูรณ์)
- **ACGL Peak-Cycle Discipline Applied Successfully (2nd use)** — Emma normalize gold spot $4,120 → base $3,400 ก่อนคำนวณ MOS (เหมือน ACGL normalize ROE peak); ผลคือ MOS -9.9% (ติดลบ) แทนที่จะเป็น MOS บวกลวงจาก peak-metric — ยืนยันว่า cyclical normalization discipline ใช้ซ้ำได้ข้าม sector (insurance → commodities)
- **Salobo/Counterparty Concentration Framework (NEW for Streaming/Royalty)** — Bear ระบุ Salobo (Vale) ~38-40% ของ NAV = single-asset/single-counterparty risk 2x เกิน threshold 20%; streaming model ไม่มี operating control เหนือ underlying mine — framework ใหม่สำหรับวิเคราะห์ streaming/royalty companies (FNV, RGLD) ในอนาคต ที่ต้อง check per-asset NAV concentration เสมอ
- **Unfavorable Convexity ที่ Peak Commodity Price** — Quinn's elasticity table (1.09-1.12x upside leverage ที่ gold record vs 1.27x downside leverage ที่ gold ต่ำ) เป็น insight สำคัญที่ Bear amplify เป็น Challenge หลัก — ซื้อ streaming company ที่ peak commodity = รับ downside convexity โดยไม่ได้ upside convexity ตอบแทน — บทเรียนสำหรับ derivative/leveraged-exposure businesses ทั้งหมด
- **Morgan Catches Narrative-Level Error Not Just Numerical Error** — Morgan พบว่าทีมเรียก gold $4,120 ว่า "record high" ทั้งที่ actual 2026 ATH คือ $5,589 (Jan 28) — ตัวเลขที่ใช้ใน model ถูกต้อง 100% แต่ narrative framing ("record") ผิด และกระทบ anchoring-bias thesis ของ Bear บางส่วน; MEDIUM severity ไม่ block QA PASS แต่เป็นตัวอย่างว่า Morgan QA ตรวจได้ลึกกว่าแค่ตัวเลข — ตรวจ narrative consistency ด้วย
- **Bear Weight 30% (ไม่ใช่ 40%) Confirmed for Quality-Cyclical Names** — WPM = quality business (debt-free, Wide Moat) with commodity-price overlay ไม่ใช่ existential/regulatory binary (ต่าง RKLB/V/LDOS/FICO ที่ Bear 40%) — เข้า pattern เดียวกับ AVGO/QCOM (Bear 25-30% สำหรับ quality names)

---

### 2026-07-22 — PGR Session (14th post-upgrade, 1st Auto/Personal-Lines P&C sector, 2nd Insurance sector session overall)
- **First Auto/Personal-Lines P&C Sector (distinct from ACGL's Specialty/Reinsurance/Mortgage)** — PGR (Progressive) = direct-to-consumer + independent agent auto/property insurer, 20+ yr telematics (Snapshot) data moat — different sub-sector economics from ACGL's institutional/Bermuda-domiciled specialty book; sector taxonomy within Insurance now has 2 distinct sub-types tracked
- **"Two Confirmed Signals in One Week" Bear Framework (NEW)** — Bear established a reusable pattern: when a leading indicator (June premium growth deceleration) is corroborated by a lagging indicator (Q2 combined ratio deterioration) within the same week, AND price falls on both events (including falling despite an EPS beat), treat as a confirmed signal rather than noise — extends beyond PGR to any future "beat but still falls" situation
- **Objective Margin-Gap Evidence vs Bear Opinion** — PGR operating margin (16.56%) verified as lowest among 4 named peers (ALL/TRV/CB/ACGL) despite highest revenue growth (+10.49%) — this is a hard, source-cited data point (not a soft Bear assertion) that downgraded Emma's moat rating from potential Wide to NARROW+; lesson: when peer comparison data is directly available, treat quantifiable gaps as primary evidence, not merely a bear talking point
- **Insurance Residual Income / Justified P/B-ROE Framework — 2nd Successful Reuse (after ACGL)** — confirms the framework is generalizable across the Insurance sector bucket, not a one-off; CoE floor 9.0% reused directly from ACGL precedent (beta too low to capture underwriting/regulatory tail)
- **Both Value Gates Fail Simultaneously — 3rd Occurrence (WPM pattern)** — MOS +1.0% (essentially none) AND Conviction 6.67 < 7.0 both fail together, same double-gate-fail pattern as WPM (2026-07-12); growing evidence that "both gates fail" is a distinct, common HOLD sub-pattern worth tracking separately from single-gate-fail cases (ACGL/MA/TOST)
- **Beta 0.25 = New Portfolio-Low** (prior low ACGL 0.31) — extends the "low-beta insurer, high tail risk" theme; CAPM literal continues to understate insurer risk across the sector, reinforcing the CoE-floor discipline as a standing rule for the Insurance bucket
- **Session Constraint Precedent: Full Pipeline Executed Without Live WebSearch/Bash Tools** — this session ran entirely on a CIO-provided Verified Data Package (per explicit CIO instruction: "ห้ามหาข้อมูลราคาหรือ financials ใหม่เอง") with no WebSearch/WebFetch/Bash tool access; the full Atlas→Emma→Quinn→Bear→Charlie→Morgan→Leo pipeline still completed successfully — establishes that CIO-prepared verified data packages are a valid substitute for live tool access when tools are unavailable, provided sourcing/URLs are pre-verified
- **Large-File Write Limitation Encountered (dashboard/data.js)** — `dashboard/data.js` (~220,000 tokens) could not be safely read/rewritten in full within this session's Read/Write-only toolset; per the existing "Dashboard Write Safety" house rule, a targeted Python patch script (`dashboard/_patch_pgr.py`) was prepared instead of risking a full-file Write — confirms the house rule's value and extends it as a hard requirement whenever a session lacks code-execution tooling

---

### 2026-07-29 — DXCM Session (15th post-upgrade, 1st Medical Devices/CGM sector, 1st clean QA correction-cycle capture)
- **Terminal Growth Rate Sanity Check ทำงานได้จริง (บทเรียนสำคัญที่สุดของ session นี้)** — Morgan Round 1 จับ Emma's DCF terminal growth rate 3.5% ที่เกินเพดาน sanity-check มาตรฐาน (1-3%) ได้แม่นยำ แม้ตัวเลขนี้จะดูสมเหตุสมผลเพราะต่ำกว่า industry CAGR (15.09%) มาก — ยืนยันว่า sanity-check ต้องเทียบกับ absolute ceiling (long-run GDP/inflation ~1-3%) ไม่ใช่แค่ relative-to-industry-CAGR — เป็นครั้งแรกที่ Morgan QA จับ terminal-growth-rate violation แบบนี้ได้ชัดเจน
- **Cascade Correction ผ่าน Anchor ที่ผูกกัน (Emma → Bear) — ตัวอย่างการแก้ไขที่สมบูรณ์** — Bear's P-W EV Base/Upside scenarios (32%/18% probability) อ้างอิงตรงกับ Emma's DCF Base/Bull Case ตัวเลข ดังนั้นเมื่อ Emma แก้ ($73→$69.80, $83→$79) Bear's P-W EV ต้อง cascade ตาม ($67.70→$65.96) ด้วย — Charlie ระบุ dependency นี้ได้ครบและแก้ไขทุกจุดถูกต้อง (verified โดย Morgan Round 2 independent recompute ตรงเป๊ะทุกตัวเลข) ขณะที่ Quinn's P-W EV ($88.51) ไม่เปลี่ยนเพราะใช้ independent Growth-framework (EV/Revenue) ไม่ผูกกับ Emma's DCF — เป็นตัวอย่างที่ดีว่าทีมต้อง track ว่า scenario anchors ไหน "borrow" ตัวเลขจาก agent อื่น เพื่อไม่ให้เกิด partial/incomplete correction
- **Morgan Round 2 Targeted Scope + Full-File Consistency Scan (NEW pattern)** — Morgan ไม่ re-run full Round 1 checklist ในรอบ 2 แต่ scope เฉพาะจุดที่เปลี่ยนจาก correction (targeted re-verify คำนวณอิสระทุกจุด) พร้อมกับ "cascade consistency check" ที่ scan ทั้งไฟล์หาตัวเลขเก่า ($76.86, +2.7%, $67.70, $73.31) ที่อาจตกหล่น — ไม่พบเลย (ปรากฏเฉพาะใน correction-log context ที่ถูกต้องตามจุดประสงค์ audit trail) — ควรเป็น pattern มาตรฐานสำหรับ Round 2+ QA cycles ในอนาคต (ประหยัดเวลาแต่ยังคง rigor)
- **Data Correction ไม่ใช่ Thesis Correction เสมอไป (ยืนยันซ้ำจาก CRM v1→v2)** — MOS เปลี่ยนจาก +2.7% เป็น +0.4% แต่ recommendation ไม่เปลี่ยน (ยังคง HOLD/WAIT) เพราะทิศทางเดิมชัดอยู่แล้วว่า MOS อ่อนแอ — การแก้ไขทำให้ conclusion แข็งแกร่งขึ้น ไม่ใช่พลิกกลับ ยืนยันว่าต้องแยกมิติ "data error ที่กระทบตัวเลข" ออกจาก "data error ที่กระทบ decision" เสมอ
- **Duopoly Catalyst-Sharing Insight (Bear, ใหม่)** — Bear ชี้ว่า Medicare Type 2 catalyst (bull case หลักของ DXCM) อาจ benefit Abbott (cost-leader ในตลาด non-insulin) เท่าๆ กันหรือมากกว่า DXCM — มุมมองใหม่ที่ต่างจาก monopoly/near-monopoly patterns ก่อนหน้า (FICO, V/MA) ที่ catalyst มักถูกมองเป็นข้อดีของบริษัทที่วิเคราะห์ฝ่ายเดียว — สำหรับ duopoly names ในอนาคต ต้องพิจารณาว่า catalyst แชร์กับคู่แข่งหรือไม่
- **Earnings-Adjacent Analysis Discipline (First Clean Case)** — นี่เป็นครั้งแรกที่ทีมวิเคราะห์หุ้นที่มี earnings อีก 1 วันพอดี ทีมเลือก WAIT อย่างชัดเจนแม้ MOS เกือบผ่าน (+0.4%) เพราะมี precedent จริง (-40.66% single-day crash ไตรมาสเดียวกันเมื่อ 2 ปีก่อน) ที่ตลาด priced ไว้เพียง ~9% weekly implied move — ตัวอย่างวินัยที่ดีของการไม่ deploy ก่อน binary event ที่มี tail-risk precedent ชัดเจน

### 2026-08-01/02 — RDDT Stop-Loss Breach: 3-Tier Exit Framework Confirmed with First "Zero-Trigger" Case
- **Event**: RDDT breached stop loss for the first time in portfolio history — ราคาปิด $140.67 < stop $140.75 (-0.06%) หลัง Q2 2026 earnings ที่ beat ทุกตัวชี้วัด (Rev $804.9M +61% YoY, EPS $1.25 vs $0.95 est., ARPU +36% YoY) แต่หุ้นร่วง -20.99% วันเดียว (largest single-day drop on record) เพราะไม่มีดีล AI licensing ใหม่กับ Google + คำเตือน "search-referral traffic ผันผวน"
- **Decision**: HOLD เต็มจำนวน (ไม่ trim/ไม่ sell) — Max ตรวจ Bear Flip Triggers (5 ข้อ) + Thesis Invalidation (3 ข้อ) จาก `RDDT_2026-05-30.md` แล้วพบว่า **zero triggers fired**
- **3-Tier Stop-Breach Severity Framework Confirmed (established ACN 2026-06-22, ทดสอบครั้งที่ 2 กับ RDDT)**:
  - **0 triggers fired → HOLD full** (RDDT, this event)
  - **1 Bear Flip fired → TRIM partial** (ACN 2026-06-22 — Bear Flip #1 revenue guide-cut fired → TRIM 50%)
  - **All Thesis Invalidation criteria fired → full exit** (ยังไม่เคยเกิดในพอร์ต — precedent: INTU auto-sold ก่อนมี framework นี้ด้วยเหตุผลคล้ายกัน)
  - **Key lesson**: จำนวน trigger ที่ยิงจริง (verifiable, checklist-based จาก report เดิม) — ไม่ใช่แค่ "ราคาต่ำกว่า stop" อย่างเดียว — คือตัวกำหนด severity ของ response ป้องกันการ react ต่อ price action ล้วนๆ โดยไม่เช็ค fundamentals ก่อน
- **"Earnings Beat + Sell-the-News ≠ Automatic Thesis Break"** — ต้องแยก sentiment-driven price action (ตลาดกลัวสิ่งที่ "ยังไม่เกิดขึ้น" เช่น Google AI licensing deal ที่ "ยังไม่มี" ไม่ใช่ "ถูกยกเลิก") ออกจาก fundamentals-driven thesis break จริง (revenue miss, guidance cut, customer loss ฯลฯ) — RDDT เป็นตัวอย่างแรกที่ ARPU/Revenue แข็งแรงกว่าคาดมาก แต่ราคาตกหนักที่สุดในประวัติศาสตร์หุ้นเดียวกัน
- **CIO Full Autonomy Reaffirmed (3rd confirmation, หลัง 2026-05-11 และ 2026-06-22)**: CIO ตอบ "แล้วแต่พวกนาย เรามาศึกษาเฉยๆ" เมื่อแจ้งเรื่อง stop-breach — มอบอำนาจให้ Max ตัดสินใจ HOLD เองอย่างเป็นทางการโดยไม่ต้องรอ confirm ทีละครั้ง (commit e253632)
- **Cross-reference**: `reports/RDDT_2026-05-30.md` (Bear Flip Triggers + Thesis Invalidation sections), `portfolio/trade-log.md` (2026-08-01 entry), `session_logs/lessons_2026-06.md` (ACN 3-tier framework origin)

---

## What Doesn't Work
*(Leo จะบันทึกเมื่อ CIO ปฏิเสธ)*

### 2026-05-20 — Dashboard data.js พัง: Write Tool ทำให้ข้อมูลหาย (Critical Infrastructure Lesson)
- **Root Cause**: Leo ใช้ Write tool เขียน `dashboard/data.js` ใหม่ทั้งไฟล์เพื่อเพิ่ม 6 entries → Write tool ยุบ newlines ทั้งหมดในไฟล์ต้นฉบับเป็น literal `\n` (backslash+n) และรวบ 15 entries เดิมเป็น 1 บรรทัดยาว 64KB ที่เริ่มด้วย `//` → JS parser อ่านเป็น comment ยักษ์ 1 บรรทัด → 15 entries เดิม (NVDA ถึง NOK) หายจาก JavaScript context โดยสมบูรณ์
- **อาการ**: Dashboard แสดงข้อมูลว่าง — แต่ `node --check` ผ่าน (comment ไม่ใช่ syntax error!) ทำให้หา bug ยากมาก จนพบ `\U`, `\D` (Windows path `C:\Users\Desktop`) ใน template literal = "Invalid Unicode escape sequence"
- **เวลาที่เสียไป**: ~1 ชั่วโมง debug + fix — CIO เห็นทันทีว่า "ข้อมูลหาย"
- **กฎใหม่ — MANDATORY ทุก agent**: **ห้ามใช้ Write tool เขียน `dashboard/data.js` ทั้งไฟล์** ไม่ว่ากรณีใดทั้งสิ้น
  - **วิธีที่ถูก (เพิ่ม entry ใหม่)**: ใช้ Python script อ่าน binary → find ตำแหน่ง `  },\n];` → insert object ใหม่ก่อน `];` → write กลับ
  - **วิธีที่ถูก (แก้ entry เดิม)**: ใช้ Python เพื่อ find/replace เฉพาะ field ที่เปลี่ยน
  - **วิธีที่ถูก (แก้ LAST_UPDATED)**: ใช้ Python `content.replace(old_date, new_date)`
  - **ห้ามทำ**: อย่าเอา content ทั้งไฟล์มา pass เข้า Write tool แม้จะ format ถูกต้องในตอนเขียน
- **Lesson เพิ่มเติม**: ตรวจ Windows path ทุกครั้งก่อน insert เข้า JS template literal — backslash `\U`, `\D`, `\b` ใน path เป็น invalid JS escape → ต้องแทนด้วย forward slash หรือ `\\`

### 2026-07-22 — PGR Session: Confirmed Again — Even Read-Only Tool Sessions Must Respect data.js Write Safety
- **Confirmation of prior rule**: This session had no code-execution tool at all (not even the Python-script workaround), so the safest choice was to NOT touch `dashboard/data.js` directly and instead leave a ready-to-run patch script (`dashboard/_patch_pgr.py`) for a future session with proper tooling — avoided any risk of repeating the 2026-05-20 incident
- **Same principle extended to `portfolio/watchlist.md`** (~94,000 tokens) — file too large to safely reconstruct via single Read+Write in this session; flagged for follow-up rather than risking truncation/corruption of a 1,670-line file with extensive Scout Report history

---

## Bear's Best Calls
*(จุดที่ Bear เตือนได้ถูกต้อง)*
*(จะอัปเดตเมื่อมีผลย้อนหลังจริง)*

---

## CFA Studied
*(Leo อัปเดตเมื่อ CIO เรียน concept ใหม่)*
- Level I: Basic Financial Reporting, DuPont, Sharpe Ratio, Beta, VaR, Hypothesis Testing, CAPM, Time Value of Money
- Level II: DCF (FCFF/FCFE), EV/EBITDA, PEG, Economic Moat, Porter's 5 Forces, Carhart 4-Factor, Scenario Analysis
- Level III: Kelly Criterion, CVaR/Expected Shortfall, Behavioral Finance, Portfolio Construction

**Pending CIO Confirm (จาก HIMS/TMDX/AVGO/RKLB/AMD/MRVL/NVDA v2/V/VEEV/LDOS/FICO/QCOM/AVGO v2 Sessions):**
- Treynor Ratio [L1]: วัด excess return ต่อ 1 unit Beta (systematic risk) — *(รอ CIO confirm — used 12 times)*
- Sortino Ratio [L1]: Sharpe ที่ใช้เฉพาะ downside deviation แทน total std dev — *(รอ CIO confirm — used 12 times)*
- Jensen's Alpha [L2]: Alpha ที่เหลือหลังหักผล market beta ออก วัด skill ที่แท้จริง — *(รอ CIO confirm — used 12 times)*
- Cross-sectional Relative Valuation / Peer Comp [L2]: เทียบ multiple ของหุ้นกับ peer set ในมิติเดียวกัน — *(รอ CIO confirm — used 11 times)*
- Investment Thesis Construction with Bull/Bear Flip Triggers [L3]: framework กำหนดเงื่อนไขวัดได้ที่จะเปลี่ยน rec — *(รอ CIO confirm — used 11 times)*
- ESG Materiality Analysis [L2-3]: ระบุ ESG factor ที่กระทบ valuation จริง พร้อม % impact — *(รอ CIO confirm — used 13 times)*
- Pre-Profit DCF (Revenue-Based 2-Stage Modified) [L2]: DCF framework สำหรับหุ้นยังไม่ทำกำไร — *(รอ CIO confirm — used in TMDX, RKLB — 2 uses)*
- **Institutional Flow Analysis / S&P 500 Index Inclusion Effect [L3*]**: วิเคราะห์ผลกระทบ passive index inclusion ต่อราคาและ vol — *(รอ CIO confirm — used in VEEV — 1st use)*
- **ROIC Adjusted for Excess Cash [L1/L2]**: ROIC ที่ปรับ denominator สำหรับ cash-rich companies (add excess cash back) เพื่อให้ได้ true operating ROIC — *(รอ CIO confirm — used in VEEV, FICO — 2 uses)*
- **Public Benefit Corporation (PBC) Governance Analysis [L2-L3]**: วิเคราะห์ governance ของ PBC structure ที่ balance profit + social mission + legal stakeholder obligation — *(รอ CIO confirm — used in VEEV — 1st use)*
- **Government Contractor / Defense Sector Valuation Framework [L2]**: FCF Yield primary + Backlog analysis + Contract type mix (cost-plus vs fixed-price) + DOGE/budget risk scenario — *(รอ CIO confirm — used in LDOS — 1st use)*
- **Antitrust Pricing Monopoly Probability Tree [L2*]**: DOJ 5-scenario analysis for pricing power abuse antitrust (different from V network access antitrust) — no action / consent decree / price cap / structural remedy / full case — *(รอ CIO confirm — used in FICO — 1st use)*
- **Financial Analytics / Credit Scoring Sector Framework [L2]**: Asset-light B2B data model; pricing power × volume cycle × platform growth; regulatory moat = antitrust target paradox — *(รอ CIO confirm — used in FICO — 1st use)*
- **ROIC Negative Equity Distortion [L1/L2]**: ROIC overstated when book equity is negative from buybacks; adjust by adding cumulative buybacks to denominator — *(รอ CIO confirm — used in FICO — ROIC adj. concept; related to VEEV excess cash adj.)*
- **FRAND Licensing Risk [L2*]**: Fair, Reasonable, Non-Discriminatory licensing terms forced by regulators on IP holders to prevent monopoly abuse; applies to patent licensing semis (QCOM, IDCC, QRVO) — *(รอ CIO confirm — used in QCOM — 1st use)*
- **Combined Binary Scenario (Off-Matrix 11th Cell) [L2]**: Simultaneous occurrence of 2 independent tail events (Apple in-house + China ban = QCOM Thesis Invalidation); not captured in standard 5×5 matrix → must be documented separately — *(รอ CIO confirm — used in QCOM — 1st use)*
- **Automotive Pipeline Haircut [L2]**: Revenue pipeline ÷ years × win rate ≠ near-term DCF Stage 1 input; full pipeline must be discounted by timeline + historical win rate — *(รอ CIO confirm — used in QCOM — 1st use)*
- **Forward Sharpe as Primary "No Deploy" Signal [L1/L3]**: Forward Sharpe = expected excess return ÷ forward vol; ถ้า < S&P 500 benchmark (~0.55) = ไม่ควร deploy capital ใหม่ (ดีกว่าถือ SPY); AVGO v2 Forward Sharpe 0.12 = primary signal สำหรับ HOLD — *(รอ CIO confirm — used in AVGO v2, QCOM, WPM, PGR — 4 uses as explicit signal)*
- **Momentum "Borrowing" Alpha [L2/L3]**: ราคาขึ้น +32% ใน 21 วัน = Momentum factor ดึงราคาเกิน fundamental; อาจ "borrow" forward alpha 6–12 เดือน → forward alpha ลด; ต้องรอ mean-reversion ก่อน re-entry — *(รอ CIO confirm — used in AVGO v2 — 1st explicit framework)*
- **Insurance Residual Income / Justified P/B-ROE [L2]**: (ROE−g)/(r−g) valuation framework for insurers where FCFF DCF is not meaningful (float + reserves distort cash flow) — *(รอ CIO confirm — used in ACGL, PGR — 2 uses)*
- **Two-Confirmed-Signals-In-One-Week Framework [L2/L3]**: When a leading indicator is corroborated by a lagging indicator within the same short window (esp. "beat but still falls" price action), treat as confirmed signal not noise — *(รอ CIO confirm — used in PGR — 1st use)*

---

## CFA Notes ที่เกี่ยวข้อง

### NVDA Session 2026-04-24 (Initial Analysis)
- Emma ใช้: DCF (FCFF), EV/EBITDA, PEG Ratio, DuPont ROE, Moat Analysis
- Quinn ใช้: CAPM, Carhart 4-Factor, Sharpe/Sortino/Treynor, VaR Parametric, Hypothesis Testing (Momentum)
- Bear ใช้: Downside Scenario Analysis (Base/Bear/Extreme), Behavioral Bias Detection (Recency Bias, Narrative Fallacy, Overconfidence)
- Key Risk: Hyperscaler AI capex cycle peak, Custom ASIC (Google TPU, Amazon Trainium, Meta MTIA), Export restriction expansion, DeepSeek-style efficiency breakthrough

### NVDA Session 2026-04-24 (Full Report — 09:00)
- Emma ใช้: DCF (FCFF), EV/EBITDA, PEG Ratio, DuPont 3-Factor, Moat Analysis, Porter's 5 Forces, ROIC vs WACC (EVA), GARP Framework
- Quinn ใช้: CAPM, Carhart 4-Factor (Market/SMB/HML/MOM), Sharpe/Sortino/Treynor, VaR Parametric, CVaR/Expected Shortfall, Hypothesis Testing, Jensen's Alpha
- Bear ใช้: Probability-Weighted Scenario Analysis (Bull/Base/Bear/Extreme), Kelly Criterion, Behavioral Finance, Max Drawdown, Tail Risk
- Charlie ใช้: Valuation Triangulation (DCF + EV/EBITDA + PEG + Scenario), Staged Entry Strategy, Position Sizing
- Key Outputs: Blended Fair Value $128, Staged Entry 7%, Stop Loss $85, Bear top risk = ASIC Disruption

### NVDA Session 2026-05-09 (Re-Analysis v2)
- Emma ใช้: DCF (FCFF 2-Stage updated), DuPont 3-Factor (updated), Economic Moat (re-assessed Wide+), Peer Comparison (4 peers: AMD/Intel/AVGO/TSMC), ESG Scorecard (E6/S7/G7 → 6.7, reconciled 6.0), ROIC vs WACC (82-85% vs 10% WACC)
- Quinn ใช้: CAPM/Beta updated (1.72), Carhart 4-Factor (alpha t=1.85), Sharpe/Sortino/Treynor, VaR/CVaR, Max Drawdown (new -44%), Sensitivity Matrix 5×5 (Revenue CAGR × WACC — same variables v1), Kelly Criterion (Quarter-Kelly → 7% maintain), P-W EV ($141.90)
- Bear ใช้: Probability-Weighted Scenario (15/40/30/15 distribution more cautious), Behavioral Bias Detection (5 biases: Recency, Momentum Anchoring, Confirmation, Anchoring to v1, Overconfidence), ASIC escalation research (Google/Amazon/Meta training ASIC data-backed), Trade war binary event modeling, ESG challenge (Governance 5/10 vs Emma 7/10)
- Charlie ใช้: Triangulation 30/30/40 → Blended FV $129.73 → ESG-adj $138, Conviction Average (7.0/10), Re-Analysis Change Log format (new)
- Atlas Macro Brief: Fed 4.25-4.50%, 10Y 4.30%, S&P ~5,650, US-China 90d truce active, Hyperscaler capex $79.8B/Q
- Key Outputs: Blended FV $138, MOS +19%, BUY Maintain 7%, Stop $88, Target $148/$185
- New Framework: Re-Analysis Change Log (v1→v2) — first time format used

### HIMS Session 2026-04-24 (Full Report — 10:00)
- Emma ใช้: DCF (FCFE), DuPont 3-Factor, Economic Moat (5 sources), Market-Based Valuation (EV/Revenue, P/S), ESG Materiality Analysis
- Quinn ใช้: Beta, Sharpe Ratio, Sortino Ratio, CVaR/Expected Shortfall, Carhart 4-Factor, Sensitivity Matrix 5x5 (Subscriber Growth × ARPU), Kelly Criterion, Jensen's Alpha, Treynor Ratio
- Bear ใช้: Probability-Weighted Scenario Analysis (4 scenarios), ESG Critical Challenge, Regulatory Risk Analysis, Behavioral Finance
- Charlie ใช้: Valuation Triangulation (DCF + Peer + P-W EV + Sensitivity), Position Sizing
- Key Outputs: Blended Fair Value $11.40, AVOID recommendation, Entry zone $10–13, Max 1-2% speculative
- New Concepts Identified: Treynor Ratio, Sortino Ratio, Jensen's Alpha (รอ CIO confirm เพิ่ม Studied List)
- Key Risk: FDA enforcement on compounded drugs, GLP-1 subscriber churn, Carhart Alpha -32% (idiosyncratic shock)

### TMDX Session 2026-04-24 (Full Report — 11:00)
- Emma ใช้: DCF (Revenue-Based 2-Stage, Pre-Profit Modified), DuPont Modified (Pre-Profit), Economic Moat (5 sources — MedTech vs Software), Relative Valuation (EV/Revenue), ESG Materiality Analysis (Organ Equity + Governance + Environmental)
- Quinn ใช้: Beta, Sharpe Ratio, Sortino Ratio, Treynor Ratio, VaR Parametric, CVaR/Expected Shortfall, Carhart 4-Factor, Jensen's Alpha, Sensitivity Matrix 5×5 (OCS Case Volume CAGR × Gross Margin), Kelly Criterion
- Bear ใช้: Probability-Weighted Scenario Analysis (4 scenarios), ESG Critical Challenge (Organ Equity + Governance), Regulatory Risk Analysis (NOP decertification), Tail Risk
- Charlie ใช้: Valuation Triangulation (DCF Base + DCF Bull + Peer + P-W EV), Position Sizing
- Key Outputs: Blended Fair Value $22–23, AVOID recommendation, Entry zone $15–22 (conditions required), Kelly = 0%
- Key Learning: Pre-profit DCF framework, MedTech Moat = Regulatory Fortress, Investigation risk = unquantifiable tail, ESG in organ transplant has unique angles (equity access, data integrity)
- Key Risk: DOJ/SEC investigation (top risk), NOP decertification, XVIVO FDA expansion, CMS reimbursement uncertainty

### AVGO Session 2026-04-25 (Full Report — 14:30) — 1st post-upgrade
- Emma ใช้: DCF (FCFF 2-Stage), EV/EBITDA, PEG Ratio, DuPont 3-Factor, Economic Moat (5 sources — Switching Cost + Intangible + Scale dominant), Cross-sectional Peer Comparison (6 peers), ESG Materiality
- Quinn ใช้: CAPM, Beta Regression, Sharpe/Sortino/Treynor, VaR Parametric, CVaR/Expected Shortfall, Max Drawdown, Hypothesis Testing (outperformance + alpha), Carhart 4-Factor (Market/SMB/HML/MOM), Jensen's Alpha (+5%/yr), Sensitivity Matrix 5×5 (Revenue Growth × Operating Margin), Kelly Criterion, Probability-Weighted EV
- Bear ใช้: Probability-Weighted Scenario Analysis (4 scenarios — independent Bear distribution), ESG Critical Re-score (4.7 vs Emma 6), Behavioral Finance (5 biases: Recency, Narrative Fallacy, Confirmation, Anchoring, Overconfidence), Investment Thesis Construction (Bull/Bear Flip Triggers + Invalidation Points) [new framework]
- Charlie ใช้: Valuation Triangulation (Emma DCF + Quinn P-W EV + Bear P-W EV blend 30/30/40), Position Sizing (Half-Kelly + tail correction → 5%), Staged Entry (3 tranches), Conviction Average (7.2/10), Disagreement Check (2pt < 3pt threshold)
- Key Outputs: Blended FV $220 (ESG-adj $223), P-W EV $212, MOS +21.6%, BUY Staged 5%, Stop $130, Target Base $215/Bull $290

### AVGO Re-Analysis v2 Session 2026-05-16
- Emma ใช้: DCF (FCFF 2-Stage updated — Rev CAGR 22% FY26, Op Margin 63-66%), EV/EBITDA (peer multiple updated), PEG (1.61x — premium), Business Deep Dive (Porter's 5 Forces, Customer Concentration, Geography), Cross-sectional Peer Comparison (6 peers — updated multiples), ESG Scorecard (E5.5/S4.5/G4.5 → 4.8/10 reconciled)
- Quinn ใช้: Beta 1.18 (stable), Carhart Alpha +3-4%/yr (reduced from +5%/yr, momentum may have borrowed forward), Sharpe/Sortino stable historical, Forward Sharpe 0.12 (KEY SIGNAL — ต่ำมาก), Sensitivity Matrix 5×5 (same variables: Revenue Growth × Op Margin — updated numbers), Kelly ~0%, P-W EV $229 (unchanged)
- Bear ใช้: 5 challenges (Growth 22% optimistic, VMware churn FY27 timing, Apple concentration underweighted, ESG Governance 6→3, Forward Sharpe 0.12 confirms no deploy), Bear P-W EV $209 (เพิ่มจาก $195 เพราะ bull thesis ดีขึ้น), ESG Overall 4.0 vs Emma 5.7 → reconciled 4.8
- Charlie ใช้: IPS 40/35/25 (Emma/Quinn/Bear — CONFIRMED for quality name), Blended FV $219, ESG-adj $209, MOS -4.1%, Conviction Average 6.7/10, IPS Gate FAIL (6.7 < 7.0), HOLD recommendation
- Atlas Macro Brief: Regime TRANSITIONAL Risk-ON, Fed 4.25-4.50%, 10Y 4.30%, VIX ~17-20 (improved from April), Hyperscaler capex $85-90B/Q (beat v1 estimate), US-China truce ACTIVE (Jul 2026 expiry), WACC 9.0%
- Key Outputs: Blended FV $219 (ESG-adj $209), MOS -4.1%, HOLD Existing 5%, ADD $200-215 (pullback), Stop $190, Conviction 6.7/10, No auto-deploy (IPS gate)
- New Framework: Momentum "Borrowing" Alpha — ราคา +32% ใน 21 วัน = momentum ดึงราคาเกิน fundamental; alpha อาจ borrow forward 6-12 เดือน → mean-reversion risk; forward alpha ลด

### RKLB Session 2026-04-29 (Full Report — 14:30) — 2nd post-upgrade, 1st binary-event play
- Emma ใช้: DCF (Revenue-Based 2-Stage Pre-Profit Modified), SOTP, Cross-sectional Peer Comp (7 peers), Economic Moat (5 sources — Narrow today, path to Wide via Neutron), Porter's 5 Forces, DuPont Modified (Pre-Profit), ESG Materiality (Defense ambiguity — first time)
- Quinn ใช้: CAPM, Beta Regression (rolling, non-stationary noted), Sharpe/Sortino/Treynor, VaR/CVaR, Max Drawdown, Hypothesis Testing, Carhart 4-Factor, Jensen's Alpha (+8.2%, t=1.9 marginal), Sensitivity Matrix 5×5 (Neutron Cadence × Space Systems GM), Kelly Criterion, Probability-Weighted EV
- Bear ใช้: Probability-Weighted Scenario Analysis (4 scenarios independent), ESG Critical Re-score (3.8 vs Emma 5.0 → reconciled 4.3), Behavioral Finance (6 biases — added Survivorship Bias), Bull/Bear Flip Triggers, Beta Non-stationarity Critique, Carhart Mis-attribution Test
- Key Outputs: Blended FV $20.30 (ESG-adj $18.70), P-W EV $19.80, MOS -19.5%, HOLD/WAIT, Stop $11

### AMD Session 2026-05-06 (Full Report — 09:00) — 3rd post-upgrade, 1st semiconductor challenger analysis
- Emma ใช้: DCF (FCFF 2-Stage, Base $155), Cross-sectional Peer Comparison (5 peers), ESG Scorecard (E 7/S 7/G 6 → 6.8→6.5 reconciled), Economic Moat (Narrow+expanding), DuPont Modified
- Quinn ใช้: Beta 1.75, Sharpe 0.62/Sortino 0.85/Treynor 0.079, Carhart 4-Factor (Alpha +4.2%/yr t=1.7), VaR -18%/CVaR -26%, Sensitivity Matrix 5×5 (Revenue CAGR × WACC), Quarter-Kelly → 4%, P-W EV $145
- Bear ใช้: Challenge ROCm, Intel 18A, Xilinx goodwill, ESG re-score 6.8→6.1, Bear P-W EV $135, What Would Change Our Mind (5+5+4)
- Key Outputs: Blended FV $148 (ESG-adj $143), MOS +41%, BUY Staged 4%, Stop $78

### MRVL Session 2026-05-06 (Full Report — 11:00) — 4th post-upgrade, 1st custom silicon analysis
- Emma ใช้: DCF (FCFF 2-Stage, Base $128), Cross-sectional Peer Comparison (5 peers), ESG Scorecard (E 7/S 6/G 7 → 6.7→6.2 reconciled), Economic Moat (Narrow+ switching cost + IP), DuPont
- Quinn ใช้: Beta 1.65 (R²=0.52), Sharpe 0.58/Sortino 0.80/Treynor 0.072, Carhart (Alpha +3.8%/yr t=1.48 weakest in BUY universe), Sensitivity Matrix 5×5 (Revenue CAGR × Terminal EBIT Margin), Quarter-Kelly → 3%, P-W EV $119
- Bear ใช้: Client concentration challenge, P/E 38x compression, M&A goodwill $8B+, ESG re-score 6.7→5.5, Bear P-W EV $100 (+binary -12% haircut), Portfolio-level 19% semiconductor warning
- Key Outputs: Blended FV $112 (ESG-adj $106), MOS +56%, BUY Staged 3%, Stop $52

### V (Visa Inc.) Session 2026-05-07 (Full Report)
- Emma ใช้: DCF (FCFF 2-Stage, Base $294), EV/EBITDA, P/E, Peer Comparison (4 peers: MA/AXP/PYPL/FI), ESG Scorecard (E8/S6/G7 → 7.0→6.4 reconciled), Economic Moat Wide, Porter's 5 Forces
- Quinn ใช้: Beta 0.90, Sharpe 0.95/Sortino 1.35/Treynor 0.12, Carhart (Alpha +3.5%/yr t=1.65), Sensitivity Matrix (Revenue CAGR × WACC — $355 justified only 24%), Kelly (negative at $355), P-W EV $320
- Bear ใช้: 5 challenges (DOJ, WACC, network effects, stablecoin), Bear P-W EV $252.50, ESG re-score S 4/G 5
- Key Outputs: Blended FV $290.30 (ESG-adj $261), HOLD/WAIT, Entry $285-310, Stop $240, Max 4%


### CRM Session 2026-05-29 (Full Report — v3 CONDITIONAL PASS) — Enterprise Software / CRM
- Emma: DCF (FCFF 2-Stage, TGR 4% CFA Option B justification), DuPont (ROIC 6.29% < WACC 9.5% = EVA negative), Economic Moat WIDE (5 sources: switching cost + network + intangible + scale + data), Cross-sectional Peer Comparison (5 peers: MSFT/SAP/NOW/ORCL/INTU), ESG Scorecard (E7/S6.5/G5 -> 6.3->6.0 reconciled)
- Quinn: P-W EV $260, Sensitivity Matrix 5x5 (FCF CAGR x WACC), Quarter-Kelly -> 4%, FCF Yield Analysis (9.77% TTM)
- Bear: 4 challenges (ROIC<WACC = EVA negative; TGR 4% optimistic; Agentforce $1.2B vs Microsoft Co-Pilot $10B; Microsoft structural underweighted); Bear P-W EV $202; ESG re-score 6.0 (Governance CEO/Chairman dual role)
- Charlie: Triangulation 40/30/30 (IPS standard), Blended FV $279 (Emma $351x40% + Quinn $260x30% + Bear $202x30%), ESG-adj FV $272, Conviction 7.0/10
- Atlas Macro Brief: RISK-ON 4/4, WACC 9-10%, CRM China exposure <1%
- Morgan QA: CONDITIONAL PASS — 5 HIGH issues fixed in v2 (Revenue/FCF base, Q1 FY27 data, TGR justification, weights 40/35/25->40/30/30, Shares 967M->937M). 3 pending minor annotations -- no impact on recommendation
- Key Outputs: Blended FV $279 (ESG-adj $272), MOS +54.1%, BUY (Value Bucket), T1 $175-190 (4%), T2 $155-175 (2.5%), T3 $140-155 (1.5%), Stop $146, Max 8%
- Conviction: Emma 7 / Quinn 7 / Bear 7 -> avg 7.0/10; Anti-Convergence NOT triggered (avg<8.0)
- S&P 500 ref: 7,520.36 (May 27 close)
- Key New Frameworks:
  1. **ROIC<WACC as Bear Primary Challenge for Mature SaaS** -- EVA negative != uninvestable if FCF yield high + Wide Moat
  2. **Revenue Re-Acceleration as Investment Signal** -- Q4 FY26 +12% -> Q1 FY27 +13% = inflection from deceleration
  3. **Value Bucket + AI Growth Catalyst Hybrid** -- Wide Moat + FCF (Value) + Agentforce (Growth catalyst) = hybrid play
  4. **Q1 FY2027 Data Freshness -- Earnings Calendar Check (STEP 0B)** -- v1 Morgan FAIL เพราะไม่รวม Q1 FY27 ที่ออก 2 วันก่อน

### VEEV Session 2026-05-11 (Full Report) — 5th post-upgrade, 1st Healthcare SaaS analysis
- Emma ใช้: DCF (FCFF 2-Stage, Base $170), DuPont (ROIC adjusted for excess cash — new), Cross-sectional Peer Comparison (4 peers: CRM/ADBE/IQVIA/Medidata), ESG Scorecard (E8/S7/G9 → 8.0/reconciled 7.3/10), Economic Moat Wide (FDA 21 CFR switching cost primary), Porter's 5 Forces
- Quinn ใช้: Beta 0.82 (R²=0.58), Carhart 4-Factor (Alpha +4.8%/yr t=2.1 = HIGHEST in portfolio), Sharpe 0.78/Sortino 1.10/Treynor 0.095, VaR -24%/CVaR -31%, Max Drawdown -64%, Sensitivity Matrix 5×5 (Revenue CAGR × WACC — same variables as NVDA/AMD/V), Quarter-Kelly = 1% (thin MOS), P-W EV $205, S&P 500 Inclusion Flow Analysis (new framework), Hypothesis Test (outperformance), Portfolio Correlation Analysis
- Bear ใช้: ROIC inflation challenge (excess cash distorts denominator — key correction), Vault CRM migration risk (off Salesforce, unmodeled), Salesforce Life Sciences Cloud threat, Revenue decel thesis (12% vs Emma 16%), Analyst target multiple justification challenge ($280 implies 17x EV/Rev at 4.25% rates), ESG re-score (8.0→6.7), 5 behavioral biases, Bear P-W EV $178, What Would Change Our Mind (5+5+4)
- Charlie ใช้: Triangulation 30/30/40 → Blended FV $200 → ESG-adj $192, Conviction Average 6.7/10, Morgan QA PASS
- Atlas Macro Brief: Fed 4.25-4.50%, 10Y 4.30%, S&P ~7,399, VIX ~22, Healthcare SaaS multiple NOT recovered from 2021-22 SaaS crash
- Key Outputs: Blended FV $192 (ESG-adj), MOS +15.7%, HOLD/WAIT, Entry T1 $148-158 (2%), T2 $130-145 (0.5%), T3 Vault CRM success (0.5%), Stop $118, Max 3%
- Conviction Score: Emma 7 / Quinn 7 / Bear 6 → avg 6.7/10 (gap 1pt < 3pt flag)
- Key New Frameworks:
  1. **S&P 500 Inclusion Flow Analysis** — passive buying mandate (~$3.5B) quantified; Bear correctly challenged as priced-in; lesson: trading catalyst, not valuation catalyst
  2. **ROIC Adjusted for Excess Cash** — first explicit correction; VEEV 115.9% → ~15-20% adjusted; lesson: apply to all cash-rich SaaS names (ADBE, VEEV pattern)
  3. **PBC Governance Analysis** — first PBC company; ESG positive (healthcare mission legally mandated); future PBC screening framework established
  4. **Healthcare SaaS Moat Type** — FDA regulatory switching cost = 18-24mo re-validation = strongest in portfolio; different from technology lock-in (CUDA) or creative workflow lock-in (Adobe)
- Key Debate: Revenue CAGR (Emma 16% vs Bear 12%) = $48 FV swing → Vault CRM migration result (Q2 FY2027 Aug 2026) = definitive catalyst; same pattern as NVDA's Revenue CAGR debate (VEEV version)
- Key Risk: Vault CRM migration retention miss (Bear's #1), Revenue decel, WACC re-rating, Salesforce Commercial Cloud threat
- data.js: Patch script at `dashboard/_patch_veev.ps1` — run to add VEEV entry to dashboard

### LDOS Session 2026-05-14 (Full Report) — 6th post-upgrade, 1st Defense/GovIT analysis
- Emma ใช้: DCF (FCFF 2-Stage, Base $115 adj.margin), DuPont (ROE 31% = leverage-driven), Cross-sectional Peer Comparison (4 peers: BAH/SAIC/CACI/LMT), ESG Scorecard (E6/S4/G6 → 5.3/10 reconciled, dual-use AI/cyber concern), Economic Moat NARROW (clearance+switching cost, shared moat), ROIC vs WACC (17.5% vs 10.5% = +7% EVA spread)
- Quinn ใช้: Beta 0.80 (Adj. 0.87), Carhart 4-Factor (Alpha +3.8%/yr t=1.55 NOT significant — fail to reject H₀), Sharpe 0.58/Sortino 0.72/Treynor 0.076, VaR -12.5%/CVaR -17.0%, Max Drawdown -44%, Sensitivity Matrix 5×5 (Revenue CAGR × EBITDA Margin — DOGE-specific variable selection), Quarter-Kelly → 3-4% (capped at 3%), P-W EV $107.15
- Bear ใช้: DOGE Civil segment challenge (-20% = -$900M revenue), DCF margin 9.5% optimistic (actual 8.4%), Moat shared challenge, Beta understates DOGE idiosyncratic risk, ESG Social re-score 5→3 (dual-use weapons), Bear P-W EV $93.20 (ESG-adj $86.68), What Would Change Our Mind (5+5+4)
- Charlie ใช้: Triangulation 30/30/40 → Bear 40% (DOGE Black Swan), Blended FV $105 (ESG-adj $99), Conviction Average 6.3/10, Gap Emma(6) vs Bear(8) = 2pt (near threshold)
- Atlas Macro Brief: Fed 4.25-4.50%, 10Y ~4.40-4.50%, DOGE = top risk (HIGH), Continuing Resolution risk (HIGH), Market Regime: TRANSITIONAL
- Key Outputs: Blended FV $105 (ESG-adj $99), MOS -8.6%, HOLD/WAIT, Entry T1 $105-115 (2%) / T2 $95-105 (1%), Stop $80, Max 3%
- Conviction Score: Emma 6 / Quinn 5 / Bear 8 → avg 6.3/10 (gap 2pt — near 3pt threshold)
- Key New Frameworks:
  1. **Defense/GovIT Sensitivity Variable** — Revenue CAGR × EBITDA Margin (not WACC) — DOGE = revenue risk, contract mix = margin risk
  2. **DOGE as Black Swan** — no historical precedent → Bear 40% weight; adds to pattern (RKLB binary + V DOJ + LDOS DOGE)
  3. **Clearance Moat = Shared Moat** — BAH/SAIC/CACI all have clearances → NARROW only, never claim exclusive advantage
  4. **Government Contractor 4-Pillar Valuation** — FCF Yield + Backlog + Contract Mix + Budget Scenario
- Key Debate: DOGE impact severity (Emma: ≤5% total revenue; Bear: 7-10%+ Civil-specific) = unresolved until Q2 2026 Book-to-Bill data
- Key Risk: DOGE Civil cuts (Bear #1), Continuing Resolution (Bear #2), Goodwill $8B+ impairment risk (Bear #3)
- data.js: Patch script at `dashboard/_patch_ldos.ps1` — run to add LDOS entry to dashboard

### FICO Session 2026-05-15 (Full Report) — 7th post-upgrade, 1st Financial Analytics / Credit Scoring analysis
- Emma ใช้: DCF (FCFF 2-Stage, P-W EV $1,225), Cross-sectional Peer Comparison (5 peers: SPGI/MCO/VRSK/EFX/TRU), ESG Scorecard (E7/S5/G6 → 6.0→5.3 reconciled; S downgraded to 4 by Bear for credit inequality), Economic Moat NARROW+ (Emma Wide vs Bear Narrow+ → Charlie reconciled Narrow+), DuPont (ROIC adjusted for negative equity), EV/EBITDA ($1,000), P/E ($1,040)
- Quinn ใช้: Beta 0.95 (3Y) / 1.35 (1Y regulatory) / 1.1-1.2 forward, Carhart 4-Factor (Alpha +6.8%/yr t=1.75 at 90% conf.), Sharpe 0.45/Sortino 0.62/Treynor ~0.074, VaR -25%/CVaR -35%, Max Drawdown -49%, Sensitivity Matrix 5×5 (Revenue CAGR × DOJ Penalty Probability — Quinn's override of Atlas WACC recommendation; 36% cells justify $1,088), Quarter-Kelly → 3% (regulatory tail adjusted), P-W EV $1,219
- Bear ใช้: Emma moat Wide → NARROW+ (FHFA structural reform ALREADY happening); DCF margin expansion inconsistent with software mix shift; DOJ probability higher than Emma/Quinn (50% adverse vs 30%); ROIC 68% overstated (neg equity distortion → adj ~35-45%); Behavioral Finance (5 biases incl. Anchoring to ATH $2,200); ESG Social 5→3/10 (45M credit invisibles + CFPB documented scoring bias); Bear P-W EV $934
- Charlie ใช้: Triangulation 30/30/40 → Blended FV $1,078, ESG-adj $1,007, Conviction Average 7.0/10, Bear 40% weight (DOJ binary pattern)
- Atlas Macro Brief: Fed 4.25-4.50%, 10Y 4.35-4.45%, Mortgage origination $1.8T (vs $4.5T peak), Consumer credit delinquency rising (8.5%), WACC 10%, S&P ~5,620, Market Regime: TRANSITIONAL-CAUTIOUS
- Key Outputs: Blended FV $1,078 (ESG-adj $1,007), MOS -0.9%, HOLD/WAIT, Entry T1 $950-1,020 (2%) / T2 $820-950 (1%), Stop $720, Max 3%
- Conviction Score: Emma 7 / Quinn 6 / Bear 8 → avg 7.0/10 (Quinn–Bear gap 2pt — watch)
- Key New Frameworks:
  1. **Sensitivity Variable: Revenue CAGR × DOJ Penalty Probability** — first direct regulatory probability as sensitivity axis
  2. **Dual Active Regulatory Binary** — DOJ + FHFA simultaneously = extends Bear 40% pattern to 2-regulatory-front case
  3. **Moat Paradox** — ROIC 68% = monopoly rents = DOJ target; moat quality ≠ regulatory safety
  4. **ROIC Negative Equity Distortion** — buyback-driven neg equity inflates ROIC; adj 68% → ~35-45%
  5. **Antitrust Pricing Monopoly Probability Tree** — 5 scenarios for pricing power abuse antitrust (vs V network access type)
  6. **Credit Access Inequality as ESG Material Risk** — Social 3-4/10; CFPB documented bias; ESG fund exclusion structural headwind
- Key Debate: DOJ probability (Emma/Quinn 25-30% vs Bear 50% adverse) = unresolved; Bear's FHFA "already happening" vs Emma "gradual risk" = key moat debate
- Key Risk: DOJ structural remedy (Bear #1 at 15%); FHFA VantageScore mandate; FCF yield 3.1% < risk-free 4.35%; margin compression from software mix shift
- data.js: Patch script at `dashboard/_patch_fico.ps1` — run to add FICO entry to dashboard

### QCOM Session 2026-05-15 (Full Report) — 8th post-upgrade, 1st Mobile Semiconductor / IP Licensing analysis
- Emma ใช้: DCF (FCFF 2-Stage, Base $193, P-W EV $196), EV/EBITDA (17x → $257), P/E (22x → $237), Blended FV $217, ESG-adj $204, DuPont (ROE 42%, ROIC 33%), Economic Moat NARROW+ (QTL Wide + QCT Narrow → Blended NARROW+), Cross-sectional Peer Comparison (6 peers: AVGO/MRVL/SWKS/MTK/AMD), ESG Scorecard (E7/S6/G7 → 6.7 → 6.35 reconciled), Porter's 5 Forces
- Quinn ใช้: Beta 1.35 (Blume adj. 1.24), Carhart 4-Factor (Alpha +3.5-5%/yr t=1.5-1.65 marginal), Sharpe 0.34/Sortino 0.51/Forward Sharpe 0.18, VaR -17.8%/CVaR -23%, Max Drawdown -45%, China Binary Black Swan VaR -40%, Sensitivity Matrix 5×5 (Revenue CAGR × China Revenue % Lost — Quinn override of WACC as V2), Kelly Criterion (NEGATIVE at $218), P-W EV $204, Portfolio Correlation (QCOM vs ADBE 0.45 / NOW 0.40)
- Bear ใช้: 5 Emma challenges (Apple Modem Unmodeled → Bear DCF base $165-175; China 53% binary $35-53/share; Automotive $45B marketing not financial; Arm threat moderate → serious; QTL FRAND structural); 3 Quinn challenges (Beta 1.35 too low → 1.50-1.65 forward; Matrix missing combined binary; Carhart alpha t=1.5 mis-specified); Bear P-W EV $167 (4 scenarios: 15/40/30/15); ESG re-score 6.7→6.0 (Social 6→5, ESG-adj reconciled 6.35); Behavioral Finance (5 biases: Recency/Narrative/Confirmation/Anchoring/Optimism); FRAND pattern documented; Bear conviction 6.5/10
- Charlie ใช้: Triangulation 40/35/25 (Emma/Quinn/Bear — CHANGED from 30/30/40; Bear 25% not 40% for quality name with binary overlay, not existential binary), Blended FV $192, Conviction Average 6.5/10, IPS Gate: 6.5 < 7.0 → Watchlist only (no auto-deploy)
- Atlas Macro Brief: Fed 4.25-4.50%, 10Y 4.35-4.45%, VIX 17-20, DXY 100-102, US-China 90d truce ACTIVE (expires July 2026), Market Regime: TRANSITIONAL-CAUTIOUS with Risk-ON bias; WACC recommendation 10.5-11.0% → Emma used 10.75%
- Key Outputs: Blended FV $192 (ESG-adj ~$183), MOS -11.9%, HOLD/WAIT, Entry T1 $190-205, Stop $150, Conviction 6.5/10, Max 5-7% when entry zone hit
- Conviction Score: Emma 7 / Quinn 6 / Bear 7 → avg 6.5/10 (Quinn–Bear gap 1pt < 3pt flag threshold)
- Key New Frameworks:
  1. **Sensitivity Variable: Revenue CAGR × China Revenue % Lost** — China 53% concentration binary (July 2026 truce expiry) > WACC sensitivity; rule: when geographic/counterparty concentration >30% + active binary event → override WACC with concentration % lost as V2
  2. **FRAND Licensing Risk** — regulatory moat cap for IP licensing companies; global regulatory pattern; new CFA concept documented
  3. **Combined Binary "11th Cell" Scenario** — Apple 100% + China ban simultaneously = Thesis Invalidation; off-matrix event must be documented even when 5×5 matrix can't capture it
  4. **Automotive Pipeline Haircut Rule** — Pipeline ÷ years × win rate = actual near-term contribution; not face value
  5. **IPS Weight Rule Clarified** — Bear 25% for quality name with binary overlay; Bear 40% reserved for existential binary names (RKLB, V DOJ, LDOS DOGE, FICO DOJ+FHFA)
- Key Debate: Apple modem transition timeline (Emma: gradual 2025-2027; Bear: 100% in-house 2026); China probability (Emma 15-20%; Bear 30-40%); Automotive ramp pace (Emma $5B+ by 2027; Bear $3.5B)
- Key Risk: Apple in-house modem (Bear #1 — high probability, near-term); China 53% export restriction (Bear #2 — 30-40% within 12M); QTL FRAND structural (Bear #3 — 40% in 5 years); Arm competitive threat (Bear #4 — 3-5yr timeline)
- Catalyst Watch: July 2026 (US-China truce expiry = China binary trigger); iPhone 2025-2026 release (Apple modem share data); QCOM Q3 FY2026 Earnings (automotive revenue trajectory); QTL licensing negotiations

### PGR Session 2026-07-22 (Full Report) — 14th post-upgrade, 1st Auto/Personal-Lines P&C analysis
- Emma ใช้: Two-Stage Residual Income (PRIMARY $255), Justified P/B-ROE ($221, normalized ROE 20%), BVPS Compounding Cross-check ($187), Emma Blend 50/20/30 → $228; Economic Moat NARROW+ (telematics data moat but margin gap vs peer); Cross-sectional Peer Comparison (4 peers: ALL/TRV/CB/ACGL); ESG Scorecard (E5/S6/G7 → 6.0/10); Porter's 5 Forces; CoE floor 9.0% (reused from ACGL)
- Quinn ใช้: Beta 0.25 (new portfolio-low), CoE floor 9.0%, Forward Sharpe ≈ -0.26, Kelly ~0%, Sensitivity Matrix 5×5 (Combined Ratio × Premium Growth Rate — reused ACGL variable pair), P-W EV $206 (Bull $260/25% · Base $205/50% · Bear $155/25%)
- Bear ใช้: 4 challenges per CIO instruction (margin gap vs peer verified objectively; "2 drops in 1 week" = confirmed signal not noise, new Two-Confirmed-Signals framework; loss costs have structural component; Fed hawkish pivot double-edged for float income vs equity multiple); Bear P-W EV $183 (Bull $250/15% · Base $195/45% · Bear $145/40%, heavier bear-weighting due to 2 confirmed signals)
- Charlie ใช้: Triangulation 40/30/30 (IPS standard) → Blended FV $208 (Emma $228×40% + Quinn $206×30% + Bear $183×30%), ESG-adj $202, Conviction Average 6.67/10
- Atlas: RISK-ON 3/4 (VIX 18.77/YC +39bps/HY 269-271bps RISK-ON, Fed hawkish dissenter), Data Package built entirely from CIO Verified Data Package (no live WebSearch this session)
- Morgan QA: CONDITIONAL PASS — 2 caveats (peer P/E/EV-EBITDA data gap, transparently flagged not fabricated; S&P 500 reference date mismatch July 20 vs July 21)
- Key Outputs: Blended FV $208 (ESG-adj $202), MOS +1.0%, HOLD/WAIT FOR PULLBACK, Entry $175-185, Stop $144 (-20.0%), Max 5% (when gate passes)
- Conviction Score: Emma 7 / Quinn 6 / Bear 7 → avg 6.67/10 (gap 1pt < 3pt, no flag)
- Key New Frameworks:
  1. **Two-Confirmed-Signals-In-One-Week (Bear)** — leading + lagging indicator corroboration within the same short window = confirmed signal, not noise; extends to any future "beat but still falls" case
  2. **Objective Margin-Gap Evidence** — peer operating margin comparison used as primary (not secondary/soft) evidence for moat downgrade when direct data available
  3. **Insurance Residual Income Framework — 2nd Reuse** — confirms generalizability across Insurance sector bucket (ACGL → PGR)
- Key Risk: Underwriting margin gap vs entire peer group (Bear #1), confirmed 2-signal deceleration, structural loss-cost component (climate + auto repair inflation), Fed hawkish pivot risk to float income valuation
- Catalyst Watch: Monthly disclosure (Aug 2026), Q3 2026 earnings (~Oct 2026), 2026 H2 hurricane season, Fed FOMC Sep/Oct/Dec 2026

---

### 2026-04-25 — System Upgrade (4 New House Rules + Dashboard Migration)
- **Trigger**: CIO request — upgrade ระบบ 4 อย่าง + ย้าย dashboard เข้า vault
- **House Rules ใหม่ที่เพิ่ม**: Sector/Peer Comparison, Conviction Level Score, What Would Change Our Mind, Historical Decision Tracking
- **Dashboard Changes**: ย้ายจาก `Desktop/my-bljor/` → vault `dashboard/`; marked.js CDN; Leo embed `fullContent`

### 2026-05-05 — Visual Report Format Standard (CIO อนุมัติ)
- **Trigger**: CIO อนุมัติ format ใหม่ให้ใช้เป็น standard ทุกรายงาน
- **Reference implementation**: `reports/RKLB_2026-04-29.md`
- **7 Visual Elements**: Emoji Headers, 2-Table, Score Dashboard, TL;DR Box, Conviction Bar, Key Verdict blockquote, Catalyst Timeline ASCII

### 2026-05-06 — AMD + MRVL Paired Semiconductor Analysis
- **Trigger**: CIO request — Full Research Report สำหรับ AMD และ MRVL ทั้งสองตัว
- **New Frameworks**: Sensitivity variable selection company-specific, Binary Risk Haircut, Challenger Play paired position, Portfolio Sector Concentration Alert, Alpha-to-Position-Size Correlation
- **Semiconductor Exposure After Session**: 19% (NVDA 7% + AVBO 5% + AMD 4% + MRVL 3%) — CEILING 20%

### 2026-05-09 — NVDA Re-Analysis v2 (1st Re-Analysis Session)
- **Trigger**: CIO request — Re-Analysis หลัง 15 วัน ราคาฟื้น + Blackwell Q1 FY2027 data
- **New Frameworks**: Re-Analysis Change Log (v1→v2), Atlas Macro Brief as WACC input, ASIC-for-Training tracking, Source Annotation requirement
- **data.js**: Patch script at `dashboard/_patch_nvda_v2.ps1`
- **Rating Change**: BUY → BUY Maintain; FV $128→$138; Stop $85→$88

### 2026-05-07 — V (Visa Inc.) Analysis
- **Trigger**: CIO request — Full Research Report สำหรับ Visa Inc. (V)
- **Key**: DOJ idiosyncratic risk NOT in beta 0.90; Kelly negative at $355; first Financial Services sector

### 2026-05-11 — VEEV (Veeva Systems Inc.) Analysis — 5th post-upgrade, 1st Healthcare SaaS
- **Trigger**: CIO approval — Max Scout Brief passed; S&P 500 inclusion catalyst
- **New Frameworks**:
  1. **S&P 500 Inclusion Flow Analysis** (first time) — quantified passive buying ~$3.5B; Bear challenged as front-run
  2. **ROIC Adjusted for Excess Cash** (explicit first) — 115.9% → ~15-20% adjusted; apply to all cash-rich SaaS
  3. **PBC Governance Analysis** (first PBC company) — ESG positive; healthcare mission legally mandated
  4. **Healthcare SaaS Regulatory Moat** — FDA CSV lock-in = strongest switching cost in portfolio
- **Files Created**: 6 files + decisions.md updated + learning-log updated + patch script for data.js
- **data.js**: Patch script at `dashboard/_patch_veev.ps1`
- **Rating**: HOLD/WAIT — Blended FV $192, Entry $148-158, Stop $118, Max 3%
- **Key Learning**: Revenue CAGR debate (Emma 16% vs Bear 12%) = same pattern as NVDA; Vault CRM migration result (Aug 2026) = THE definitive catalyst

### 2026-05-11 — CIO Full Autonomy Declaration
- **Trigger**: CIO statement clarifying team's mandate and system purpose
- **Key Change**: ทีมได้รับ Full Autonomy — execute decisions ได้หลัง QA PASS โดยไม่ต้องรอ CIO confirm
- **Educational Mission Confirmed**: ระบบนี้สร้างมาเพื่อ Professional Investment Education ผ่านการปฏิบัติจริง
- **Implication**: ทุก decision, analysis, mistake = บทเรียน — ทีมต้องทำให้ดีที่สุดและบันทึกทุกอย่างเพื่อ CIO เรียนรู้

### 2026-05-14 — LDOS (Leidos Holdings) Analysis — 6th post-upgrade, 1st Defense/GovIT
- **Trigger**: Max Scout — LDOS เป็น top pick; sector ใหม่ Defense/GovIT ไม่มีในพอร์ต; ย่อ -40.3% จาก 52w High
- **New Frameworks**:
  1. **Defense/GovIT Sensitivity Variable** — Revenue CAGR × EBITDA Margin (DOGE = revenue; contract mix = margin)
  2. **DOGE as Unquantifiable Black Swan** — no precedent → Bear 40%; extends Black Swan pattern (RKLB, V, LDOS)
  3. **Clearance Moat = Shared Moat** — NARROW only; BAH/SAIC/CACI all have clearances = not exclusive
  4. **Government Contractor 4-Pillar Valuation** — FCF Yield + Backlog + Contract Mix + Budget Scenario
- **Files Created**: 6 files + decisions.md updated + learning-log updated + patch script for data.js
- **data.js**: Patch script at `dashboard/_patch_ldos.ps1`
- **Rating**: HOLD/WAIT — Blended FV $105 (ESG-adj $99), Entry T1 $105-115 (2%), T2 $95-105 (1%), Stop $80, Max 3%
- **Key Learning**: Beta 0.80 = ต่ำสุดใน universe → first counter-cyclical/defensive name; Alpha t=1.55 → 3% position (Alpha-to-Size ladder consistent)
- **Key Catalyst**: Q2 2026 Book-to-Bill (Jul/Aug 2026) = THE key metric for DOGE impact quantification

### 2026-05-15 — FICO (Fair Isaac Corporation) Analysis — 7th post-upgrade, 1st Financial Analytics / Credit Scoring
- **Trigger**: Max Scout — FICO ย่อ -49% จาก ATH $2,200; DOJ probe = entry opportunity? New sector Financial Analytics
- **New Frameworks**:
  1. **Sensitivity Variable: Revenue CAGR × DOJ Penalty Probability** — first direct regulatory probability as sensitivity axis; Quinn override of Atlas WACC recommendation
  2. **Dual Active Regulatory Binary** — DOJ + FHFA simultaneously; first 2-front regulatory case; extends Bear 40% pattern
  3. **Moat Paradox** — ROIC 68% = DOJ target; moat quality ≠ regulatory safety
  4. **ROIC Negative Equity Distortion** — buyback-driven neg equity inflates ROIC; adj 68% → ~35-45%
  5. **Antitrust Pricing Monopoly Probability Tree** — 5 scenarios; different from V network access antitrust
  6. **Credit Access Inequality as ESG Material Risk** — Social 3-4/10; CFPB documented scoring bias
- **Files Created**: 6 mandatory files + decisions.md updated + learning-log updated + data.js updated (QCOM entry #12)
- **Rating**: HOLD/WAIT — Blended FV $1,078 (ESG-adj $1,007), Entry T1 $950-1,020 (2%), T2 $820-950 (1%), Stop $720, Max 3%
- **Key Learning**: MOS -0.9% = essentially at fair value = no entry at $1,088; wait for pullback or DOJ catalyst
- **Key Catalyst**: DOJ investigation resolution (unknown timeline, est. 12-36 months) = single most important variable

### 2026-05-15 — QCOM (Qualcomm Inc.) Analysis — 8th post-upgrade, 1st Mobile Semiconductor / IP Licensing
- **Trigger**: CIO request — Full Research Report สำหรับ QCOM; Mobile AI Tollbooth + Automotive pipeline thesis; Bear challenge focus: Apple dependency, Arm threat, China risk
- **New Frameworks**:
  1. **Sensitivity Variable: Revenue CAGR × China Revenue % Lost** — override WACC for geographic concentration names (>30% revenue in single risky market); China 53% + July 2026 truce expiry = dominant binary
  2. **FRAND Licensing Risk** — global regulatory enforcement pattern on IP licensing; new CFA concept for IP-heavy names
  3. **Combined Binary "11th Cell" Scenario** — simultaneous Apple + China event = Thesis Invalidation; must document off-matrix combined event
  4. **Automotive Pipeline Haircut** — $45B pipeline ÷ 8yrs × 65% win rate = near-term DCF contribution; marketing number ≠ financial input
  5. **IPS Weight Rule Clarified (Bear 25% vs 40%)** — Bear 25% for quality name with binary overlay; Bear 40% for existential binary (RKLB/V DOJ/LDOS DOGE/FICO dual regulatory)
- **Files Created**: 6 mandatory files + decisions.md updated + learning-log updated + data.js updated (QCOM entry #12)
- **Rating**: HOLD/WAIT — Blended FV $192 (40/35/25), Entry $190-205, Stop $150, Max 5-7% (staged; no auto-deploy, conv 6.5 < 7.0)
- **IPS Gate Result**: Conviction 6.5/10 < threshold 7.0 → WATCHLIST ONLY; no trade executed; Max alerted to monitor $190-205
- **Key Learning**: Twin binary risks (Apple modem + China 53%) = 71% revenue in 2 risky pockets; FRAND = moat cap mechanism; "11th Cell" framework now established for future combined-event scenarios
- **Key Catalysts**: July 2026 US-China truce expiry; iPhone 2025 Apple modem share data; Q3 FY2026 automotive revenue trajectory; QTL FRAND litigation outcomes

### 2026-05-16 — AVGO Re-Analysis v2 (9th post-upgrade, 2nd Re-Analysis Session)
- **Trigger**: Price Audit FAIL — ราคา $228 > v1 FV $220; ราคาขึ้น +32% ใน 21 วัน; CIO ต้องการ deploy decision
- **New Frameworks**:
  1. **Momentum "Borrowing" Alpha** — ราคา +32% ใน 21 วัน อาจ "borrow" forward alpha 6–12 เดือน → mean-reversion risk; forward alpha ลด; ต้องรอ re-entry ที่ cheaper entry
  2. **Forward Sharpe as Primary HOLD Signal** — Forward Sharpe 0.12 (< S&P 500 0.55) = ไม่ควร deploy ทุกครั้ง; rule: Forward Sharpe < benchmark threshold = HOLD default (applies universally)
  3. **Price Audit Fail Protocol Confirmed** — AVGO ใช้ protocol เดียวกับ NVDA v3, MRVL v2: Price Audit Fail → Re-Analysis → Rating downgrade; FV stable แต่ Rating เปลี่ยนตาม MOS
  4. **Stop Loss Ratchet** — เมื่อ unrealized gain สูง ปรับ stop loss ขึ้นเพื่อ protect gains (AVGO: $130 → $190; MRVL: $52 → $110; NVDA: $85 → $128 for new entry); loss tolerance ลดลงเมื่อ position profitable
  5. **Apple WiFi In-house Risk Tracking** — Apple AW3 (Watch) = internal first mover; iPhone WiFi = next; -$15–25/share; จะต้อง monitor ทุก Apple product launch; rule: check Apple product roadmap for any position with >10% Apple revenue
- **Files Created**: 8 files (Atlas 2 + Emma + Quinn + Bear + Leo + Session Log + Report) + decisions.md + learning-log + dashboard patch script
- **data.js**: Patch script at `dashboard/_patch_avgo_v2.ps1`
- **Rating Change**: BUY (5% staged) → HOLD (existing) / ADD on Pullback ($200-215)
- **IPS Gate Result**: Conviction 6.7/10 < threshold 7.0 → no T1 auto-deploy; position held from v1
- **Key Debates**:
  1. Revenue CAGR FY2026: Emma 22% vs Bear 18% → Charlie blend
  2. VMware churn: Emma "stable switching cost" vs Bear "enterprises evaluating NOW" → unresolved (FY27 H1 definitive)
  3. ESG Governance: Emma 6/10 vs Bear 3/10 → reconciled 4.5/10 (Bear view more credible on succession)
  4. Apple concentration: Emma modeled in ESG discount vs Bear "needs DCF haircut" → Bear stronger case
- **Key Catalysts**: FY2025 Q4 AI revenue (Oct/Dec 2026) = THE most important; VMware ARR Q2/Q3 FY2026; Apple product launches (WiFi sourcing)
- **KEY INSIGHT: "Thesis wins, entry loses"** — Bull thesis ยืนยันทุกข้อ (AI ASIC, VMware margin, ROIC) = แต่ ราคาตลาดวิ่งไปก่อน = MOS หาย = HOLD ไม่ BUY; lesson: thesis เดินเร็ว ≠ entry เดินตาม thesis เสมอ

---

## Lessons Learned (Morgan Retrospective Audit)

> บันทึกจาก Morgan Retrospective Audit วันที่ 2026-05-19 และ NOW Re-verify วันที่ 2026-05-20
> Leo รับผิดชอบ — ห้ามเกิดซ้ำ — ทุก agent ต้องอ่านก่อนทำงาน

---

### 2026-05-20 — Error #1: Shares Outstanding ไม่ verify หลัง Corporate Action (NOW)

**สิ่งที่เกิด:** รายงาน `NOW_2026-05-11.md` ใช้ shares 515M (pre-split) แทน 1.03B (post 5-for-1 split วันที่ Dec 18, 2025) ทำให้คำนวณ FV ผิดทั้งหมด

**ผลกระทบ:**

| รายการ | ค่าที่รายงาน (ผิด) | ค่าจริง |
|--------|-------------------|---------|
| Shares Outstanding | 515M | 1,030M |
| Market Cap implied | $226B | ~$113B (ณ FV price) |
| Fair Value per share | $226.00 | ~$121.45 |
| MOS | +148% (สูงผิดปกติมาก) | +17.8% |

**สาเหตุ:** Morgan ไม่ได้ cross-check shares กับ SEC 10-Q ล่าสุดหลัง corporate action — ใช้ตัวเลขจาก pre-split source โดยไม่รู้

**Prevention Rule (บังคับ):**
1. ทุกครั้งที่วิเคราะห์หุ้นที่มี corporate action (stock split / reverse split / spinoff / rights issue) ใน **12 เดือนที่ผ่านมา** → ต้อง verify shares outstanding จาก **SEC 10-Q หรือ 10-K ล่าสุด** ก่อนใช้ในการคำนวณ
2. Sanity check บังคับ: `price × shares ≈ market cap` (ต้องตรงกับ source อิสระ ±10%)
3. ถ้า MOS ออกมา >50% → flag ทันที เป็น signal ว่าอาจมี data error (โดยเฉพาะ shares outstanding)
4. Morgan ต้องตรวจ "Corporate Actions in Last 12 Months" เป็น checklist item แรกในทุก QA

**Agent ที่รับผิดชอบ:**
- **Emma** — ต้องระบุ source shares outstanding (SEC form + date) ทุกรายงาน
- **Morgan** — ต้องตรวจ corporate action history ก่อน approve QA PASS
- **Quinn** — ต้อง sanity check market cap = price × shares ก่อน submit quant section

---

### 2026-05-20 — Error #2: Blended FV Weight ผิดใน 6 รายงาน

**สิ่งที่เกิด:** รายงาน 6 ฉบับใช้ weight ผิดจาก IPS House Rules (40/30/30 Emma/Quinn/Bear)

| Ticker | Weight ที่ใช้ (ผิด) | Weight ที่ถูก (IPS) | ผลกระทบต่อ FV |
|--------|-------------------|-------------------|--------------|
| ADBE | 30/30/40 (Bear สูงเกิน) | 40/30/30 | FV ต่ำกว่าจริง |
| LDOS | 30/30/40 (Bear สูงเกิน) | 40/30/30 | FV ต่ำกว่าจริง |
| V | 30/30/40 (Bear สูงเกิน) | 40/30/30 | FV ต่ำกว่าจริง |
| META | 40/35/25 (Quinn สูง Bear ต่ำ) | 40/30/30 | FV ต่างจากจริง |
| APP | 40/35/25 (Quinn สูง Bear ต่ำ) | 40/30/30 | FV ต่างจากจริง |
| QCOM | 40/35/25 (Quinn สูง Bear ต่ำ) | 40/30/30 | FV ต่างจากจริง |

**หมายเหตุ:** การ override Bear weight (เช่น Bear 40% สำหรับ existential binary) ต้องผ่าน Charlie อนุมัติและระบุชัดเจนในรายงาน ไม่ใช่เปลี่ยนโดยปริยาย

**สาเหตุ:** Charlie ไม่มี checklist บังคับ verify weight ก่อน finalize — ใช้ weight ตาม convention ของแต่ละ session โดยไม่ยึด IPS กลาง

**Prevention Rule (บังคับ):**
1. Charlie ต้อง hardcode ใน pre-finalize checklist ทุกรายงาน: **"Blended FV = Emma×40% + Quinn×30% + Bear×30% — verify ก่อน write"**
2. ถ้าต้องการ override weight → ต้องระบุ section แยกในรายงาน พร้อมเหตุผล + note ใน `decisions.md`
3. Morgan QA checklist ต้องเพิ่ม: `[ ] Blended FV weight = 40/30/30 (หรือระบุ override + เหตุผลชัดเจน)`
4. สูตรที่ถูกต้อง: `Blended FV = (Emma_FV × 0.40) + (Quinn_FV × 0.30) + (Bear_FV × 0.30)`

**Agent ที่รับผิดชอบ:**
- **Charlie** — ต้อง verify weight ทุกครั้งก่อน finalize
- **Morgan** — ต้องตรวจ weight ใน QA checklist

---

### 2026-05-20 — Error #3: Terminal Growth Rate เกิน Threshold (META 5%, ADBE 3.5%)

**สิ่งที่เกิด:** Emma ใช้ TGR เกิน Morgan Protocol ที่กำหนด max 3%

| Ticker | TGR ที่ใช้ (ผิด) | TGR Max (IPS) | ผลกระทบต่อ FV |
|--------|-----------------|--------------|--------------|
| META | 5.0% | 3.0% | FV สูงเกินจริง ~$60-100/share |
| ADBE | 3.5% | 3.0% | FV สูงเกินจริง (ขนาดน้อยกว่า) |

**สาเหตุ:** Emma ไม่มี hard cap ใน checklist — ใช้ TGR ตาม management guidance / analyst consensus โดยไม่ตรวจ upper bound

**Prevention Rule (บังคับ):**
1. **Emma ต้อง cap TGR ที่ 3.0% เสมอ** ไม่มีข้อยกเว้นโดยปริยาย
2. ถ้าต้องการ TGR > 3.0% → ต้องระบุเหตุผลเฉพาะเจาะจง + แสดง DCF ณ TGR = 3.0% ควบคู่ด้วยเสมอ + ต้องผ่าน Morgan approve พร้อม note ใน QA
3. Morgan QA ต้องเพิ่ม: `[ ] Terminal Growth Rate ≤ 3.0% (หรือมี explicit justification + Morgan approve)`
4. Rule of thumb: TGR > US nominal GDP growth (~2-3%) = ต้องพิสูจน์เหตุผลเฉพาะ

**Agent ที่รับผิดชอบ:**
- **Emma** — ต้องตรวจ TGR ทุกครั้งก่อน finalize DCF
- **Morgan** — ต้องตรวจ TGR ใน QA checklist

---

### 2026-05-20 — Error #4: ราคาล้าสมัย >100% โดยไม่มีป้าย PRICE AUDIT FAIL (GEV +130%, NOK +186%)

**สิ่งที่เกิด:** รายงาน GEV และ NOK มีราคาต่างจากตลาดจริงมากกว่า 100% แต่ไม่มีป้ายเตือน

| Ticker | สถานะ | Discrepancy | ผลกระทบ |
|--------|--------|------------|---------|
| GEV | ราคาในรายงาน ต่างจากตลาดจริง | +130% | CIO อาจใช้รายงานผิด |
| NOK | ราคาในรายงาน ต่างจากตลาดจริง | +186% | CIO อาจใช้รายงานผิด |

**สาเหตุ:** ไม่มีกระบวนการ price check สำหรับ HOLD/WAIT positions — รายงานเก่าค้างโดยไม่มีการ flag

**Prevention Rule (บังคับ):**
1. **Max ต้อง price check ทุก HOLD/WAIT position ทุกสัปดาห์** — ถ้าราคาต่างจาก report >20% → เพิ่ม banner `> ⚠️ PRICE AUDIT FAIL — ราคาในรายงานล้าสมัย X% จากวันที่ Y` ทันที โดยไม่รอ Morgan audit
2. ถ้าราคาต่าง >50% → escalate ให้ Charlie พิจารณา re-analysis ก่อน CIO ใช้รายงานตัดสินใจ
3. Vera ต้องตรวจ price discrepancy ใน weekly report — positions ที่ราคาห่างจาก report >20% ต้อง flag
4. รายงานที่ผ่าน 90 วันโดยไม่มี price update → auto-flag "STALE — requires price audit" ใน decisions.md

**Agent ที่รับผิดชอบ:**
- **Max** — ต้องทำ weekly price check ทุก HOLD/WAIT position
- **Vera** — ต้องตรวจ discrepancy ใน weekly report
- **Charlie** — ต้อง escalate re-analysis ถ้าราคาต่าง >50%

---

### 2026-05-20 — Error #5: Dashboard ไม่ sync หลังแก้ไขข้อมูล

**สิ่งที่เกิด:**
- ADBE, NOW, INTU (OPEN positions) ไม่อยู่ใน `dashboard/data.js` — CIO ไม่เห็นใน dashboard
- FV ผิดของ APP, LDOS, V ค้างอยู่ใน dashboard โดยไม่ได้อัปเดตหลัง Morgan Audit Fix

**สาเหตุ:** ไม่มีกระบวนการบังคับ "แก้ข้อมูล → sync dashboard พร้อมกัน"

**Prevention Rule (บังคับ):**
1. ทุกการแก้ไข financial data ต้อง sync `dashboard/data.js` พร้อมกันทันที — ห้าม delay
2. หลังแก้ไขรายงานหรือ FV ใดๆ → Leo ต้องทำ dashboard sync checklist:
   - `[ ]` แก้ไข reports/TICKER_DATE.md แล้ว
   - `[ ]` แก้ไข portfolio/decisions.md แล้ว
   - `[ ]` อัปเดต dashboard/data.js แล้ว (FV, price, recommendation ตรงกัน)
   - `[ ]` อัปเดต LAST_UPDATED ใน data.js แล้ว
3. Morgan QA ต้องตรวจ: `[ ]` ticker นี้อยู่ใน dashboard/data.js ไหม? — ถ้าไม่อยู่ → FAIL ทันที
4. Vera weekly report ต้องตรวจ: ทุก ticker ใน decisions.md ต้องอยู่ใน dashboard.js ด้วย

**Agent ที่รับผิดชอบ:**
- **Leo** — ต้องทำ dashboard sync ทุกครั้งหลังแก้ไขข้อมูล
- **Morgan** — ต้องตรวจ dashboard sync ใน QA
- **Vera** — ต้องตรวจ consistency ระหว่าง decisions.md กับ dashboard.js ใน weekly report

---


### 2026-05-29 — Error #6: Revenue Data Freshness — Q1 FY2027 Earnings Released ก่อน Report ออก

**สิ่งที่เกิดขึ้น:** รายงาน CRM v1 ใช้ข้อมูล FY2026 annual (Revenue $37.9B, FCF $13.1B) โดยไม่รวม Q1 FY2027 ที่ Salesforce รายงาน 2026-05-27 -- เพียง 2 วันก่อน analysis date 2026-05-29

| รายการ | ค่าที่รายงาน v1 (ผิด) | ค่าจริง Q1 FY2027 |
|--------|---------------------|--------------------|
| Revenue base | $37.9B FY2026 | $41.5B FY2026 official + Q1 FY27 $11.1B (+13%) |
| FCF base | $13.1B | $14.4B FY2026 (FCF margin 34.7%) |
| Agentforce ARR growth | +169% YoY | +205% YoY (Q1 FY27) |
| FY2027 guidance | ไม่มี | $45.8-46.2B (ประกาศ 2026-05-27) |
| Blended FV | $258 | $279 (หลังแก้ข้อมูล) |
| MOS | +42.5% | +54.1% |

**สาเหตุ:** Atlas Data Package ไม่ตรวจ earnings release calendar ก่อนสร้าง Data Package -- ใช้ข้อมูลก่อนหน้า โดยไม่ทราบว่า Q1 earnings ออกแล้ว 2 วันก่อน

**Prevention Rule (บังคับ):**
1. **Atlas ต้องตรวจ "Earnings Released in Last 30 Days" เป็น STEP 0B** ก่อนสร้าง Data Package -- ถ้ามี earnings release <=30 วัน -> ต้องใช้ข้อมูล post-earnings เท่านั้น
2. หากพบ earnings ออกแล้วแต่ยังไม่ incorporate -> flag [EARNINGS FRESHNESS ISSUE] ทันที ก่อน dispatch Emma/Quinn
3. Morgan QA ต้องตรวจ: [ ] ถ้ามี earnings release <=30 วัน -> report ใช้ข้อมูล post-earnings
4. Emma ต้องระบุ "Latest Earnings Date" ใน header ของทุก analysis

**Agent ที่รับผิดชอบ:** Atlas (STEP 0B), Emma (Latest Earnings Date), Morgan (earnings freshness checklist)

---

### 2026-07-22 — Error #7 (Process Note, Not a Data Error): Session Ran Without Live WebSearch/Bash Tools

**สิ่งที่เกิดขึ้น:** PGR analysis session มีเฉพาะ Read/Write tools — ไม่มี WebSearch/WebFetch/Bash access เลย ต่างจากทุก session ก่อนหน้า

**วิธีจัดการ:** CIO ให้ Verified Data Package มาพร้อม URL sources ครบถ้วนล่วงหน้า ("ห้ามหาข้อมูลราคาหรือ financials ใหม่เอง") — ทีมใช้ข้อมูลนี้เป็น single source of truth ตลอด pipeline ได้สำเร็จ ไม่มี data error เกิดขึ้น

**Limitation ที่เกิดตามมา:**
1. ไม่สามารถแก้ `dashboard/data.js` ได้ตรงๆ (ไฟล์ ~220K tokens เกิน context ของ session) — เตรียม `dashboard/_patch_pgr.py` ไว้แทน
2. ไม่สามารถแก้ `portfolio/watchlist.md` ได้ตรงๆ (ไฟล์ ~94K tokens) — ต้องรอ session ที่มี tool เต็มรูปแบบ
3. ไม่สามารถ verify S&P 500 close ของวันที่ตรงกับ analysis date (July 21) ได้เอง — ใช้ July 20 verified figure แทน พร้อม flag ชัดเจน

**Prevention/Process Rule (บันทึกไว้ ไม่ใช่ error สำหรับ agent ใดโดยเฉพาะ):**
1. เมื่อ session ไม่มี WebSearch/Bash tool access — CIO-provided Verified Data Package ที่มี URL ครบถ้วนเป็น**ทางเลือกที่ยอมรับได้**สำหรับดำเนิน pipeline ต่อ (ไม่ต้อง block ทั้งหมด)
2. Large files (data.js, watchlist.md เกิน ~50K tokens) — **ห้าม** พยายาม full-file Read+Write โดยไม่มี code-execution tool; ให้เตรียม patch script/pending-update note แทนเสมอ
3. Missing verified data ที่ตรง date พอดี (เช่น S&P 500 ณ วันวิเคราะห์) — ใช้ตัวเลข verified ล่าสุดที่มีอยู่ในระบบ พร้อม flag ชัดเจนว่ายังไม่ re-verify

**Agent ที่รับผิดชอบ:** Charlie (orchestration under tool constraint), Leo (large-file limitation documentation + patch script prep), Vera (flag S&P 500 date mismatch for follow-up)

---

## สรุป Prevention Checklist สำหรับทุก Agent (จาก Morgan Audit 2026-05-19/20)

| # | Agent | Prevention Rule | Trigger |
|---|-------|----------------|---------|
| 1 | Emma + Morgan | Verify shares outstanding จาก SEC 10-Q/10-K หลัง corporate action (12 เดือน) | ทุก analysis |
| 2 | Emma + Quinn + Morgan | Sanity check: price × shares ≈ market cap (±10%) | ทุก analysis |
| 3 | Emma + Morgan | MOS > 50% → flag ทันที เป็น signal ของ data error | ทุก analysis |
| 4 | Charlie + Morgan | Blended FV = Emma×40% + Quinn×30% + Bear×30% — hardcode ใน checklist | ทุก analysis |
| 5 | Emma + Morgan | Terminal Growth Rate ≤ 3.0% หรือ explicit justification + Morgan approve | ทุก analysis |
| 6 | Max + Vera | Weekly price check ทุก HOLD/WAIT — >20% discrepancy → PRICE AUDIT FAIL banner | รายสัปดาห์ |
| 7 | Leo + Morgan + Vera | Dashboard sync บังคับหลังทุกการแก้ไข financial data | ทุกครั้งที่แก้ไข |
| 8 | Atlas + Emma + Morgan | ตรวจ Earnings Release <=30 วัน ก่อน analysis -- ต้องใช้ post-earnings data เสมอ (STEP 0B) | ทุก analysis |
| 9 | Charlie + Leo | เมื่อไม่มี WebSearch/Bash tool — ใช้ CIO Verified Data Package แทนได้ | เมื่อ tool ไม่พร้อม |
| 10 | Leo | Large files (>~50K tokens) ห้าม full-file Read+Write โดยไม่มี code-execution tool — เตรียม patch script แทน | เมื่อไฟล์ใหญ่เกินไป |

---

*อัปเดตล่าสุด: 2026-07-22 — เพิ่ม PGR session (HOLD/WAIT FOR PULLBACK, Blended FV $208, MOS +1.0%, Conviction 6.67/10, both Value gates fail). First Auto/Personal-Lines P&C sector. New Bear framework: Two-Confirmed-Signals-In-One-Week. Session ran without live WebSearch/Bash tools — CIO Verified Data Package used instead. dashboard/data.js + watchlist.md too large to safely edit this session — patch script prepared (`dashboard/_patch_pgr.py`). Error #7 process note added. | อัปเดตก่อนหน้า: 2026-05-29 — เพิ่ม CRM session (BUY Value Bucket, FV $279, MOS +54.1%, Conviction 7.0/10). Morgan CONDITIONAL PASS. S&P 500 ref 7,520.36. Error #6: Revenue Data Freshness prevention rule added (Atlas STEP 0B). | อัปเดตก่อนหน้า: 2026-05-20 — เพิ่ม "Lessons Learned" section จาก Morgan Retrospective Audit 2026-05-19 + NOW Re-verify 2026-05-20 — 5 errors บันทึกแล้ว พร้อม prevention rules บังคับสำหรับทุก agent และ Prevention Checklist สรุป 7 ข้อ | ไฟล์นี้อัปเดตล่าสุดก่อนหน้า 2026-05-16 — AVGO Re-Analysis v2 (HOLD/ADD on Pullback). Rating: BUY → HOLD. FV $219 (ESG-adj $209). MOS -4.1%. Forward Sharpe 0.12. Kelly ~0%. Conviction 6.7/10 < IPS 7.0 = no deploy. Stop updated $130→$190. | Leo*
