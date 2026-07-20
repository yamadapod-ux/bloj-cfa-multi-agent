import re

filepath = "C:/Users/user/Desktop/บลจ/บลจ CFA/learning-log.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

print(f"File loaded: {len(content)} chars")

# ---- 1. เพิ่ม CRM row ใน Decision History table ----
crm_row = "| **2026-05-29** | **CRM** | **Salesforce, Inc.** | **BUY (Value Bucket — Staged Entry)** | **$181.00** (Source 1: Salesforce Q1 FY27 press release 2026-05-27; Source 2: valuethemarkets.com 2026-05-27 ✅) | **7.0/10** | **$279** (Emma $351x40% + Quinn $260x30% + Bear $202x30%) | Wide Moat enterprise CRM. FCF $14.4B FY2026 (+9.5% Rev $41.5B). Agentforce ARR $1.2B +205% YoY (Q1 FY27). Revenue re-accel Q4->Q1: +12%->+13%. RPO $72.4B. MOS +54.1%. ROIC 6.29% < WACC 9.5% (EVA negative) key Bear risk. Morgan CONDITIONAL PASS. **S&P 500 ref 7,520.36** (May 27 close). | **$146 (-20% from entry $182.50)** |\n"

decision_section_end = "---\n\n## What Works"
if decision_section_end in content:
    content = content.replace(decision_section_end, crm_row + decision_section_end, 1)
    print("Step 1: CRM row added to Decision History")
else:
    print("ERROR: Decision History end marker not found")

# ---- 2. เพิ่ม CRM session ใน CFA Notes (before VEEV) ----
crm_cfa_note = """
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

"""

veev_note_marker = "### VEEV Session 2026-05-11"
if veev_note_marker in content:
    content = content.replace(veev_note_marker, crm_cfa_note + veev_note_marker, 1)
    print("Step 2: CRM CFA note added")
else:
    print("ERROR: VEEV note marker not found")

# ---- 3. เพิ่ม CRM session ใน What Works section ----
crm_what_works = """
### 2026-05-29 — CRM Session (10th post-upgrade, 1st Enterprise SaaS / CRM analysis)
- **Wide Moat + Deep Value Convergence at 7.0**: Emma/Quinn/Bear ให้ Conviction 7.0/10 ทุกคน = strong convergence ที่ Value Bucket Gate (>=7.0) พอดี; first time all three agents agree exact score; Anti-Convergence Protocol NOT triggered (avg=7.0 < 8.0 threshold)
- **Revenue Re-Acceleration as Key Catalyst**: Q4 FY26 +12% -> Q1 FY27 +13% = inflection point; ต่างจาก pure AI hype เพราะ revenue direction เปลี่ยนจริง
- **Morgan CONDITIONAL PASS แต่ Rating ไม่เปลี่ยน**: v1 Morgan QA FAIL (5 HIGH issues) -> v2 แก้ครบ -> Rating BUY ยังคงเดิม; lesson: data correction ไม่ใช่ thesis correction เสมอไป; เมื่อข้อมูลถูกแก้เพื่อ accuracy ผลอาจยิ่งยืนยัน thesis (FV $258->$279, MOS +42.5%->+54.1%)
- **Q1 FY2027 Data Freshness Rule**: Morgan QA FAIL ส่วนหนึ่งเพราะ report ใช้ FY2026 data โดยไม่รวม Q1 FY2027 ที่ออกวันที่ 2026-05-27 (2 วันก่อน analysis) -- ยืนยัน: ต้องตรวจ earnings release <=30 วันก่อน analysis date เสมอ
- **EVA Negative != AVOID**: ROIC 6.29% < WACC 9.5% = EVA negative แต่ FCF yield 9.77% + Wide Moat + RPO $72.4B = override EVA signal; lesson: EVA negative is a bear challenge not automatic disqualifier for FCF-generative Wide Moat names

"""

avgo_reanalysis_marker = "### 2026-05-16 — AVGO Re-Analysis v2"
if avgo_reanalysis_marker in content:
    content = content.replace(avgo_reanalysis_marker, crm_what_works + "\n" + avgo_reanalysis_marker, 1)
    print("Step 3: CRM What Works added")
else:
    print("ERROR: AVGO v2 marker not found in What Works")

# ---- 4. เพิ่ม CRM lesson Error #6 ----
crm_lesson = """
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
"""

prevention_checklist_marker = "## สรุป Prevention Checklist"
if prevention_checklist_marker in content:
    content = content.replace(prevention_checklist_marker, crm_lesson + "\n" + prevention_checklist_marker, 1)
    print("Step 4: Error #6 lesson added")
else:
    print("ERROR: Prevention Checklist marker not found")

# ---- 5. อัปเดต Prevention Checklist row 8 ----
old_row7 = "| 7 | Leo + Morgan + Vera | Dashboard sync บังคับหลังทุกการแก้ไข financial data | ทุกครั้งที่แก้ไข |"
new_rows = old_row7 + "\n| 8 | Atlas + Emma + Morgan | ตรวจ Earnings Release <=30 วัน ก่อน analysis -- ต้องใช้ post-earnings data เสมอ (STEP 0B) | ทุก analysis |"
if old_row7 in content:
    content = content.replace(old_row7, new_rows, 1)
    print("Step 5: Prevention Checklist row 8 added")
else:
    print("ERROR: Row 7 not found")

# ---- 6. อัปเดต footer timestamp ----
old_footer = "*อัปเดตล่าสุด: 2026-05-20"
new_footer = "*อัปเดตล่าสุด: 2026-05-29 — เพิ่ม CRM session (BUY Value Bucket, FV $279, MOS +54.1%, Conviction 7.0/10). Morgan CONDITIONAL PASS. S&P 500 ref 7,520.36. Error #6: Revenue Data Freshness prevention rule added (Atlas STEP 0B). | อัปเดตก่อนหน้า: 2026-05-20"
if old_footer in content:
    content = content.replace(old_footer, new_footer, 1)
    print("Step 6: Footer updated")
else:
    print("ERROR: Footer not found")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Done. File saved: {len(content)} chars")
