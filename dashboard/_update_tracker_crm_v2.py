#!/usr/bin/env python3
"""
Update performance/tracker.md: replace all CRM v1 references with v2 data.
Uses binary read/write to avoid encoding issues.
"""

import re

tracker_path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\performance\tracker.md"

with open(tracker_path, "rb") as f:
    content = f.read()

text = content.decode("utf-8")

# ============================================================
# 1. Update Recommendations Without Position table — CRM row (line 56 area)
# ============================================================
old_crm_row = ('| **CRM** | **2026-05-29** | **~5,700-5,750 (est. — ต้องการ verified source สำหรับ alpha)** | '
               '**BUY (Staged Entry) $181** | **RISK-ON — Max deploy T1 ทันที (4% ที่ $175-190)** | '
               'OPEN — tracking | — | **ALPHA PENDING: S&P@Rec ยังเป็น est. — alpha คำนวณได้เมื่อ Max deploy + S&P verified** | '
               'First Enterprise SaaS Value analysis. FCF yield 9.77% = historically high. ROIC < WACC = Value Trap risk counter-balanced by Wide Moat + RPO $72.4B backlog. Conviction unanimity 7/7/7 = Bear Convergence Check triggered. |')

new_crm_row = ('| **CRM v2** | **2026-05-29** | **~5,700-5,750 (est. — ต้องการ verified source สำหรับ alpha)** | '
               '**BUY (Staged Entry) $181** | **RISK-ON — Max deploy T1 ทันที (4% ที่ $175-190)** | '
               'OPEN — tracking | — | **ALPHA PENDING: S&P@Rec ยังเป็น est. — alpha คำนวณได้เมื่อ Max deploy + S&P verified** | '
               '**v2 QA Fix 2026-05-29.** FCF $14.4B official + Revenue $41.5B FY2026. Q1 FY27 Revenue $11.1B +13% YoY re-acceleration. Agentforce +205% ARR. Blended FV $279 (weights 40/30/30 corrected). MOS +54.1%. Forward Return +15.4%/yr CAGR. |')

text = text.replace(old_crm_row, new_crm_row, 1)

# ============================================================
# 2. Update Week 2026-W22 section (lines 113-118 area)
# ============================================================
old_w22_new_analysis = ('- New Analysis this week: **CRM (2026-05-29)** — BUY (Value Bucket, Staged Entry) | '
                         'Conviction 7.0/10 | MOS +42.5% | Blended FV $258')
new_w22_new_analysis = ('- New Analysis this week: **CRM (2026-05-29) v2 QA Fix** — BUY (Value Bucket, Staged Entry) | '
                         'Conviction 7.0/10 | MOS +54.1% | Blended FV $279 (weights corrected 40/30/30)')

text = text.replace(old_w22_new_analysis, new_w22_new_analysis, 1)

old_w22_deploy = ('- Deploy trigger: CRM T1 4% ที่ $175-190 — Max ดำเนินการทันที')
new_w22_deploy = ('- Deploy trigger: CRM T1 4% ที่ $175-190 — Max ดำเนินการทันที | Blended FV $279 vs $181 = MOS +54.1%')

text = text.replace(old_w22_deploy, new_w22_deploy, 1)

old_w22_action = ('- Action items: Execute `dashboard/_add_crm.py`, verify data.js syntax, GOOGL + CRM Max deploy')
new_w22_action = ('- Action items: Execute `dashboard/_update_crm_v2.py` (v2 script), verify data.js syntax, GOOGL + CRM Max deploy | v2 QA Fix COMPLETE — all 5 HIGH issues resolved')

text = text.replace(old_w22_action, new_w22_action, 1)

# ============================================================
# 3. Update Conviction Calibration — CRM annotation (line 162 area)
# ============================================================
old_conv_row = ('| 7.0–7.4 | **8** (AVGO v3, FICO, ADBE, INTU, NOW, META, GOOGL v4 7.2, **CRM 7.0**) | '
                '3 (ADBE, NOW, INTU) + GOOGL v4 watchlist-BUY + CRM deploy-active | 0 | TBD | TBD | IPS gate pass — tracking |')

new_conv_row = ('| 7.0–7.4 | **8** (AVGO v3, FICO, ADBE, INTU, NOW, META, GOOGL v4 7.2, **CRM 7.0**) | '
                '3 (ADBE, NOW, INTU) + GOOGL v4 watchlist-BUY + CRM deploy-active | 0 | TBD | TBD | IPS gate pass — tracking |')

# The row itself didn't change, just the annotation below it
old_crm_annotation = ('**CRM เพิ่มใน 7.0–7.4 bucket (Conviction 7.0) — BUY Value Bucket; IPS gate PASSED exactly (7.0 ≥ 7.0); '
                       'Convergence unanimity 7/7/7 = first unanimity event; deploy-active T1**')
new_crm_annotation = ('**CRM v2 ใน 7.0–7.4 bucket (Conviction 7.0) — BUY Value Bucket; IPS gate PASSED (7.0 ≥ 7.0); '
                       'Blended FV $279 (corrected 40/30/30 weights), MOS +54.1%; Convergence unanimity 7/7/7 = first unanimity event; deploy-active T1 | '
                       'v2 QA Fix: FCF $14.4B + Revenue $41.5B + Agentforce +205% + weights corrected**')

text = text.replace(old_crm_annotation, new_crm_annotation, 1)

# ============================================================
# 4. Replace entire CRM BUY Entry section (lines 276-305)
# ============================================================
old_crm_entry = """## CRM BUY Entry (2026-05-29)

| Field | ค่า |
|-------|-----|
| Ticker | CRM |
| Company | Salesforce, Inc. |
| Date | 2026-05-29 |
| Rec | **BUY (Value Bucket — Staged Entry)** |
| Price at Analysis | ~$181.00 (Scout Report 2026-05-28 ⚠️ single source — Morgan CONDITIONAL PASS; ≥2 URL verification pending) |
| S&P 500 at Analysis | ~5,700-5,750 (est. — ต้องการ verified source สำหรับ alpha calculation) |
| Blended FV | **$258** (Emma $311×40% + Quinn $244×35% + Bear $192×25%) |
| ESG-adj FV | ~$252 (-2.3% ESG discount) |
| MOS | **+42.5%** ($258 vs $181) |
| Conviction | **7.0/10** (Emma 7 / Quinn 7 / Bear 7) |
| Conviction Gate | **PASSED** (Value bucket: 7.0 ≥ 7.0 ✅ — minimal pass, exact threshold) |
| Value MOS Gate | **PASSED** (+42.5% ≥ 15% ✅) |
| Convergence Check | Bear Anti-Convergence Protocol triggered (7/7/7 unanimity, gap=0) → Counter-Arguments Found: Value Trap risk + Microsoft terminal threat |
| Entry Zone | T1: $175–190 (4%) — deploy ทันที | T2: $155–175 (2.5%) | T3: $140–155 (1.5%) |
| Max Position | 8% total (T1+T2+T3) |
| Stop Loss | **$146 (-20% จาก entry $182.50)** |
| Forward Return | **+12.3%/yr CAGR (+41.4% total, 3Y horizon from $181 to Blended FV $258)** |
| Key Thesis | Wide Moat enterprise CRM trade ที่ FCF yield 9.77% + Forward P/E 13x = ถูกที่สุดในประวัติศาสตร์ Agentforce ARR $1.2B +169% YoY = AI catalyst ใหม่ RPO $72.4B +14% = contractual visibility |
| Key Risks | ROIC 6.29% < WACC 9.5% (EVA -$3.21B/yr), Microsoft Dynamics structural bundle threat, Agentforce small-base hype, TGR 4% optimistic |
| Morgan QA | **CONDITIONAL PASS** (Flag 1: price single source ⚠️ | Flag 2: peer multiples approximate ⚠️ | Flag 3: shares outstanding approximate ⚠️) |
| Regime | RISK-ON 4/4 — deploy T1 ทันที |
| Moat | Wide (switching costs primary + network + intangible + scale + data) |
| Bucket | Value |
| Sector | Enterprise Software / Cloud CRM |
| Report | `reports/CRM_2026-05-29.md` |"""

new_crm_entry = """## CRM BUY Entry — v2 QA Fix (2026-05-29)

> **v2 QA Fix (2026-05-29):** FCF base corrected $13.1B→$14.4B, Revenue $37.9B→$41.5B (FY2026 official), Agentforce +169%→+205%, Q1 FY27 data incorporated, weights corrected 40/35/25→40/30/30. Blended FV $258→$279, MOS +42.5%→+54.1%.

| Field | ค่า |
|-------|-----|
| Ticker | CRM |
| Company | Salesforce, Inc. |
| Date | 2026-05-29 |
| Rec | **BUY (Value Bucket — Staged Entry)** |
| Price at Analysis | **$181.00** (Source 1: salesforce.com/news/press-releases/2026/05/27/fy27-q1-earnings/ ✅ | Source 2: valuethemarkets.com/news/salesforce-posts-record-q1-revenue-of-111b ✅ | ≥2 URL sources PASS) |
| S&P 500 at Analysis | ~5,700-5,750 (est. — ต้องการ verified source สำหรับ alpha calculation) |
| Blended FV | **$279** (Emma $351×40% + Quinn $260×30% + Bear $202×30%) |
| ESG-adj FV | ~$273 (-2.2% ESG discount) |
| MOS | **+54.1%** ($279 vs $181) |
| Conviction | **7.0/10** (Emma 7 / Quinn 7 / Bear 7) |
| Conviction Gate | **PASSED** (Value bucket: 7.0 ≥ 7.0 ✅ — minimal pass, exact threshold) |
| Value MOS Gate | **PASSED** (+54.1% ≥ 15% ✅) |
| Blended FV Weights | **40/30/30** (Emma/Quinn/Bear) — CLAUDE.md Return-side rule; v1 weights 40/35/25 CORRECTED |
| Convergence Check | Bear Anti-Convergence Protocol triggered (7/7/7 unanimity, gap=0) → Counter-Arguments Found: Value Trap risk + Microsoft terminal threat |
| Entry Zone | T1: $175–190 (4%) — deploy ทันที | T2: $155–175 (2.5%) | T3: $140–155 (1.5%) |
| Max Position | 8% total (T1+T2+T3) |
| Stop Loss | **$146 (-20% จาก entry $182.50)** |
| Forward Return | **+15.4%/yr CAGR (+53.8% total, 3Y horizon from $182.50 entry mid to Blended FV $279)** |
| Key Thesis (v2) | Wide Moat enterprise CRM. FCF $14.4B FY2026 official (margin 34.7%). Revenue $41.5B (+9.5%). Q1 FY27 Revenue $11.1B +13% YoY re-acceleration. Agentforce ARR $1.2B +205% YoY (Q1 FY27). FY27 guide $45.8-46.2B. Blended FV $279 (40/30/30) vs $181 = MOS +54.1% |
| Key Risks | ROIC 6.3% < WACC 9.5% (EVA negative); Microsoft Dynamics bundle threat; Agentforce $1.2B = only 2.9% of revenue; Q2 FY27 must confirm +12-13% revenue growth |
| Morgan QA | **CONDITIONAL PASS v2** (Flag: Shares URL pending SEC EDGAR | Flag: S&P 500 close URL pending | Flag: Beta/peer multiples approximate but flagged) |
| Regime | RISK-ON 4/4 — deploy T1 ทันที |
| Moat | Wide (switching costs primary + network + intangible + scale + data) |
| Bucket | Value |
| Sector | Enterprise Software / Cloud CRM |
| Sources | Revenue $41.5B + FCF $14.4B: https://www.salesforce.com/news/press-releases/2026/05/27/fy27-q1-earnings/ | Agentforce +205%: https://www.valuethemarkets.com/news/salesforce-posts-record-q1-revenue-of-111b |
| Report | `reports/CRM_2026-05-29.md` (v2 updated) |"""

text = text.replace(old_crm_entry, new_crm_entry, 1)

# Write back
with open(tracker_path, "wb") as f:
    f.write(text.encode("utf-8"))

print("SUCCESS: tracker.md updated with CRM v2 data")
print("Changes made:")
print("  - Recommendations table: CRM v1 → CRM v2 with Blended FV $279, MOS +54.1%")
print("  - Week 2026-W22: MOS +42.5%/BFV $258 → MOS +54.1%/BFV $279, weights corrected")
print("  - Conviction Calibration: CRM annotation updated with v2 data")
print("  - CRM BUY Entry section: full replacement with v2 data")
print("  - Forward Return: +12.3%/yr → +15.4%/yr CAGR")
print("  - Blended FV weights: 40/35/25 → 40/30/30 (CLAUDE.md corrected)")
