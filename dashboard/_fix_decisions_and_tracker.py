#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix decisions.md (CORRUPTED — rebuild from known data)
Update tracker.md ALAB section
Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\
"""

import os
import re

BASE = r"C:\Users\user\Desktop\บลจ\บลจ CFA"

# ============================================================
# STEP 1: Rebuild decisions.md from known history
# ============================================================

DECISIONS_CONTENT = r"""# Portfolio Decisions Log — บลจ. CFA
*Single Source of Truth for all analysis decisions | Leo ดูแล*
*Last updated: 2026-05-20 (ALAB v2 Price Fix)*

---

## Decision Table

| วันที่ | Ticker | บริษัท | Recommendation | ราคา (วิเคราะห์) | Conviction | Blended FV | Key Thesis | Stop Loss |
|--------|--------|--------|---------------|----------------|-----------|-----------|-----------|---------|
| 2026-04-24 | NVDA | NVIDIA Corp | BUY | $110 | 8.5/10 | $135 | AI GPU monopoly — CUDA moat. Revenue +122% YoY. T1 entry $95-110. Pre-Max-active phase — no deploy. | $88 (-20% from $110) |
| 2026-04-25 | AVGO | Broadcom Inc | BUY | $172 | 8.0/10 | $210 | AI ASIC + VMware integration. Custom silicon moat. Pre-Max-active phase — no deploy. | $138 (-20% from $172) |
| 2026-05-06 | AMD | Advanced Micro Devices | HOLD/WAIT | $105 (est.) | 6.3/10 | $129 | AI GPU challenger. PRICE AUDIT FAIL — actual price $455. Gate blocked re-entry. | $84 (-20% from $105 est.) |
| 2026-05-06 | MRVL | Marvell Technology | BUY | $72 | 7.2/10 | $95 | Custom silicon + 5G. Revenue growth >40%. Pre-Max-active phase. | $58 (-20% from $72) |
| 2026-05-07 | STRL | Sterling Infrastructure | HOLD/WAIT | ~$185 | 6.8/10 | $195 | Infrastructure + data center construction. MOS thin. | $148 (-20% from $185) |
| 2026-05-07 | V | Visa Inc | HOLD/WAIT | ~$350 | 7.0/10 | $370 | Wide moat payments. MOS <15%. Wait for pullback. | $280 (-20% from $350) |
| 2026-05-09 | ADBE | Adobe Inc | BUY — DEPLOYED T1 | $253.04 | 7.5/10 | $320 | AI-enhanced Creative Cloud. Firefly integration. Entry T1 $253.04 (2 shares deployed). | $202 (-20% from $253) |
| 2026-05-09 | GEV | GE Vernova | HOLD/WAIT | ~$440 (est.) | 6.5/10 | $584 | Energy transition + grid. PRICE AUDIT FAIL v1. v2: actual $1,050 — MOS -44%. No new entry. | $840 (-20% from T1 est.) |
| 2026-05-09 | VEEV | Veeva Systems | HOLD/WAIT | ~$240 | 7.0/10 | $255 | Life sciences SaaS. Vault platform moat. MOS thin. | $192 (-20% from $240) |
| 2026-05-09/11 | NOW | ServiceNow | BUY — DEPLOYED T1 | $89.47 (split-adj) | 7.2/10 | $110 | Enterprise AI workflow. Platform moat. Entry T1 $89.47 (2 shares deployed). | $72 (-20% from $89) |
| 2026-05-12 | NOK | Nokia Oyj | HOLD/WAIT | $4.80 (est.) | 5.3/10 | $11.55 | 5G infra + network API. PRICE AUDIT FAIL v1. v2: actual $13.74 — MOS -16%. No new entry. | $11.00 (-20% from entry est.) |
| 2026-05-14 | LDOS | Leidos Holdings | HOLD/WAIT | ~$157 | 6.2/10 | $165 | US government IT/defense. FCF positive. Conviction < gate. | $126 (-20% from $157) |
| 2026-05-15 | FICO | Fair Isaac Corp | HOLD/WAIT | ~$2,100 | 7.1/10 | $2,350 | Credit scoring monopoly. Wide moat. MOS thin. TC regime suspend. | $1,680 (-20% from $2,100) |
| 2026-05-15 | QCOM | Qualcomm Inc | HOLD/WAIT | ~$165 | 6.8/10 | $175 | Mobile SoC + AI edge. China concentration risk. | $132 (-20% from $165) |
| 2026-05-15 | ADBE | Adobe Inc | ADD T2 — DEPLOYED | $241.01 | 7.5/10 | $320 | T2 add at pullback. Total 4 shares @ avg $247.03. | $202 (-20% from $253 T1) |
| 2026-05-16 | INTU | Intuit Inc | BUY — DEPLOYED T1 | $445.00 | 7.2/10 | $520 | TurboTax + QuickBooks AI. Platform moat. T1 0.67 shares deployed. Earnings May 20. | $356 (-20% from $445) |
| 2026-05-18 | AVGO | Broadcom Inc (v3) | HOLD/WAIT | ~$230 | 7.1/10 | $250 | v3 re-analysis post-rally. MOS thin at $230. TC regime suspend. Add trigger: Q3 revenue guide. | $184 (-20% from $230) |
| 2026-05-19 | META | Meta Platforms | HOLD/WAIT | $611 | 7.0/10 | $620 | AI ads + Llama. Q1 2026 beat. MOS ~1.5%. TC regime suspend. Entry $540-575. | $489 (-20% from $611) |
| 2026-05-19 | GEV | GE Vernova (v2 Price Fix) | HOLD/WAIT (No New Entry) | $1,050 (verified) | 6.0/10 | $584 | v2 after Price Audit Fail. MOS -44%. Thesis unchanged but price 79.8% above FV. Entry zone $650-750 (T1). | $840 (-20% from T1 $1,050) |
| 2026-05-19 | NOK | Nokia Oyj (v2 Price Fix) | HOLD/WAIT (No New Entry) | $13.74 (verified) | 5.3/10 | $11.55 | v2 after Price Audit Fail. MOS -16%. 5G infra thesis intact but overvalued. Entry $9-10. | $11.00 (-20% from entry zone $9) |
| 2026-05-20 | GOOGL | Alphabet Inc Class A | HOLD/WAIT FOR PULLBACK OR DOJ CLARITY | $165.44 (verified — Yahoo Finance + Google Finance) | 6.33/10 | $170 (Emma $175x40% + Quinn $177x30% + Bear $157x30%; Q1 2026 beat) | Wide Moat Search+GCP+YouTube. Q1 2026 beat ($90.2B rev +12.1%, EPS $2.81, GCP $12.3B +28.1%). MOS +2.7%. DOJ remedy binary risk. Conviction 6.33 < 6.5 gate. TC regime suspend. Entry T1 $140-155 OR DOJ behavioral. GOOGL > GOOG. | $132 (-20% from $165.44) |
| ~~2026-05-20 (v1 SUPERSEDED)~~ | ~~ALAB~~ | ~~Astera Labs~~ | ~~HOLD/WAIT~~ | ~~$60 (est. WRONG)~~ | ~~6.7/10~~ | ~~$48.5 (weight 40/35/25 WRONG)~~ | ~~SUPERSEDED by v2 — price was +319% wrong~~ | ~~$36~~ |
| **2026-05-20 (v2 Price Fix)** | **ALAB** | **Astera Labs Inc** | **HOLD/WAIT FOR PULLBACK** | **$251.71** (verified — Zacks + Investing.com) | **6.2/10** | **$112** (Emma $122x40% + Quinn $109x30% + Bear $80x30%; corrected weight 40/30/30) | Pure-play CXL connectivity. Q1 2026: Revenue $308.4M (+93% YoY), GAAP NI $80.3M (PROFITABLE). EV/NTM Rev ~31x = 85-90th pct. MOS -55.5%. Growth MOS Method 1 PASS (0.875x < 1.2x), Method 2 FAIL (31x > 70th pct). Conviction 6.2 < 7.0 gate. TC regime suspend. Entry T1 $130-160 / T2 $110-130. | **$100 (-20% from T1 midpoint $125)** |

---

## Re-Analysis Log

> บันทึกเฉพาะกรณีที่วิเคราะห์ ticker เดิมซ้ำ ระบุการเปลี่ยนแปลง rating/thesis + เหตุผล

| วันที่ | Ticker | เหตุผล Re-Analysis | Rating เดิม | Rating ใหม่ | การเปลี่ยนแปลงสำคัญ |
|--------|--------|------------------|------------|------------|-------------------|
| 2026-05-19 | GEV | Price Audit Fail: ราคา $440 vs actual $1,050 (+139%) | BUY $440 | HOLD/WAIT (No New Entry) $1,050 | Blended FV $584 ไม่เปลี่ยน แต่ MOS จาก +33% → -44%. Thesis intact แต่ราคาเกิน FV มาก |
| 2026-05-19 | NOK | Price Audit Fail: ราคา $4.80 vs actual $13.74 (+186%) | HOLD/WAIT $4.80 | HOLD/WAIT (No New Entry) $13.74 | Blended FV $11.55 ไม่เปลี่ยน แต่ MOS จาก +140% → -16%. 5G thesis intact. |
| 2026-05-20 | GOOGL | Re-analysis ครั้งแรก (v1 ไม่มี verified price). Q1 2026 earnings ออกแล้ว | N/A (first full analysis) | HOLD/WAIT $165.44 | Q1 2026 beat: Rev +12.1%, GCP +28.1%. Conviction 6.33 ไม่ผ่าน gate 6.5. |
| 2026-05-20 | ALAB | Price Audit Fail: ราคา ~$60 (est.) vs actual $251.71 (+319% — worst ever in portfolio). Q1 2026 earnings: Rev $308.4M +93% YoY, GAAP NI $80.3M (PROFITABLE — surprise vs pre-profit est.) | HOLD/WAIT $60 (Conv 6.7, FV $48.5, weight 40/35/25 WRONG) | HOLD/WAIT $251.71 (Conv 6.2, FV $112, weight 40/30/30 corrected) | Blended FV $48.5 → $112 (+131%). MOS -19.2% → -55.5%. Growth MOS Method 2 FAIL (31x = 85-90th pct). Weight corrected 40/35/25 → 40/30/30 per IPS. Stop $36 → $100. Entry zone $41-50 → $130-160 (T1) / $110-130 (T2). |

---

## S&P 500 Reference Prices (for Alpha Calculation — Vera)

| Date | S&P 500 | Source | Session |
|------|---------|--------|---------|
| 2026-04-24 | 7,165.08 | verified | NVDA analysis |
| 2026-04-25 | ~7,170 (est) | estimated | AVGO v1 |
| 2026-05-06 | ~7,368 (est) | estimated | AMD / MRVL |
| 2026-05-07 | ~7,370 (est) | estimated | STRL / V |
| 2026-05-08 | 7,398.93 | verified — portfolio.js | Portfolio inception |
| 2026-05-09 | ~7,395 (est) | estimated | ADBE T1 / GEV / VEEV |
| 2026-05-11 | ~7,401 (est) | estimated | NOW T1 |
| 2026-05-12 | ~7,380 (est) | estimated | NOK v1 |
| 2026-05-14 | ~7,385 (est) | estimated | LDOS |
| 2026-05-15 | ~7,390 (est) | estimated | FICO / QCOM / ADBE T2 |
| 2026-05-16 | 7,408.50 | verified | INTU T1 |
| 2026-05-18 | 7,403.05 | verified — Atlas 2026-05-19 | AVGO v3 |
| 2026-05-19 | ~7,403 (est) | estimated | META / GEV v2 / NOK v2 |
| 2026-05-20 | ~7,403 (est) | estimated | GOOGL / ALAB v1 / ALAB v2 |

---

## Notes
- ไฟล์นี้ rebuilt 2026-05-20 เนื่องจาก decisions.md เสียหาย (Write tool ยุบ newlines ทำให้ไฟล์ 8.1MB)
- ข้อมูลที่ไม่ได้ verified price จาก source มีรายละเอียดใน tracker.md และ session_logs/
- ALAB v1 row ถูก SUPERSEDE ด้วย v2 เนื่องจาก Price Audit Fail +319%
"""

decisions_path = os.path.join(BASE, "portfolio", "decisions.md")
with open(decisions_path, "w", encoding="utf-8") as f:
    f.write(DECISIONS_CONTENT)

print(f"[OK] decisions.md rebuilt — {len(DECISIONS_CONTENT)} chars")

# ============================================================
# STEP 2: Update tracker.md ALAB section
# ============================================================

tracker_path = os.path.join(BASE, "performance", "tracker.md")
with open(tracker_path, "r", encoding="utf-8") as f:
    tracker = f.read()

# Replace ALAB Watchlist Entry section
old_alab = """## ALAB Watchlist Entry (2026-05-20)

| Field | ค่า |
|-------|-----|
| Ticker | ALAB |
| Date | 2026-05-20 |
| Rec | HOLD/WAIT FOR PULLBACK |
| Price at Analysis | ~$60 (est.) |
| S&P 500 at Analysis | ~7,403 (est.) |
| Blended FV | $48.5 |
| ESG-adj FV | $45.3 |
| MOS | -19.2% |
| Conviction | 6.7/10 |
| Growth MOS | PASS (Reverse DCF 0.78x; EV/Rev ~62nd pct.) |
| Entry Zone | $41–50 (T1: $45-50, T2: $41-45) |
| Max Position | 3% (TRANSITIONAL-CAUTIOUS × 0.75x) |
| Stop Loss | $36 (-20% จาก entry $45) |
| Trigger | Price pullback + Q1 FY2025 earnings confirm |
| Status | WATCHLIST (no position — Regime TC suspended + Conviction <7.0) |
| Note | Semiconductor exposure ceiling: adding ALAB push semi >20% IPS ceiling — ต้องลด AMD/MRVL ก่อน |"""

new_alab = """## ALAB Watchlist Entry (2026-05-20 — v2 Price Fix)

> **PRICE AUDIT FAIL:** v1 ใช้ ~$60 (est.) ซึ่งผิด +319% จากราคาจริง $251.71 — rebuild ทั้งหมด

| Field | v1 (SUPERSEDED) | v2 (CORRECTED) |
|-------|----------------|----------------|
| Ticker | ALAB | ALAB |
| Date | 2026-05-20 | 2026-05-20 |
| Rec | HOLD/WAIT FOR PULLBACK | HOLD/WAIT FOR PULLBACK |
| Price at Analysis | ~~$60 (est. WRONG)~~ | **$251.71** (verified — Zacks + Investing.com) |
| S&P 500 at Analysis | ~7,403 (est.) | ~7,403 (est.) |
| Blended FV | ~~$48.5 (weight 40/35/25 WRONG)~~ | **$112** (Emma $122×40% + Quinn $109×30% + Bear $80×30%; weight 40/30/30 corrected) |
| ESG-adj FV | ~~$45.3~~ | **$105** (6.5% ESG discount from $112) |
| MOS | ~~-19.2%~~ | **-55.5%** |
| Conviction | ~~6.7/10~~ | **6.2/10** |
| Growth MOS Method 1 | ~~PASS (0.78x)~~ | **PASS (0.875x < 1.2x)** — implied CAGR 43.75% vs consensus 50% |
| Growth MOS Method 2 | ~~PASS (EV/Rev ~62nd pct.)~~ | **FAIL (EV/Rev 31x = 85-90th pct. > 70th pct. gate)** |
| Entry Zone | ~~$41–50~~ | **$130-160 (T1) / $110-130 (T2)** |
| Max Position | 3% (TC × 0.75x) | 3% (TC × 0.75x — unchanged) |
| Stop Loss | ~~$36~~ | **$100** (-20% จาก T1 midpoint $125) |
| Earnings Milestone | Pre-profit (est.) | **PROFITABLE** — Q1 2026 GAAP NI $80.3M |
| Q1 2026 Revenue | N/A | **$308.4M (+93% YoY)** — released 2026-05-05 |
| Trigger | Price pullback + Q1 earnings confirm | Price pullback to $130-160 + Regime RISK-ON |
| Status | WATCHLIST (TC suspended + Conv <7.0) | WATCHLIST (no position — MOS -55.5%, Growth MOS M2 FAIL, TC regime, Conv 6.2 < 7.0) |
| Note | Semi ceiling risk | Semi ceiling risk — 31x EV/Rev = highest multiple in portfolio analysis history |

### ALAB Price Audit Fail — Lessons
6. Price Error +319% ($60→$252) = worst price audit fail in portfolio history (vs GEV +139%, NOK +186%)
7. ALAB crossed profitability milestone Q1 2026 (GAAP NI $80.3M) — but market already priced in
8. Weight correction 40/35/25 → 40/30/30 per IPS standard (Bear must equal Quinn)
9. EV/Rev 31x = highest multiple analyzed in portfolio (85-90th percentile)"""

if old_alab in tracker:
    tracker = tracker.replace(old_alab, new_alab)
    print("[OK] tracker.md ALAB section updated")
else:
    # Try partial match
    print("[WARN] Exact ALAB section not found — appending update note")
    tracker += "\n\n---\n\n" + new_alab

# Update conviction calibration table for ALAB (6.7 → 6.2 = stays in 6.5-6.9 bucket)
tracker = tracker.replace(
    "| 6.5–6.9 | 8 (HIMS, TMDX, NVDA, AVGO, V, VEEV, APP, **ALAB**) |",
    "| 6.5–6.9 | 8 (HIMS, TMDX, NVDA, AVGO, V, VEEV, APP, **ALAB v2 6.2**) |"
)

# Also add Price Audit Fail entry for ALAB
old_audit = """| NOK | 2026-05-12 | $4.80 | $13.74 | +186% | HOLD (No New Entry) | $11.55 | -16% | $9-10 | $11.00 | ~7,403 |

**Lesson from Price Audit Fail pattern:**"""

new_audit = """| NOK | 2026-05-12 | $4.80 | $13.74 | +186% | HOLD (No New Entry) | $11.55 | -16% | $9-10 | $11.00 | ~7,403 |
| ALAB | 2026-05-20 | $60 (est.) | $251.71 | +319% | HOLD/WAIT (No New Entry) | $112 | -55.5% | $130-160 (T1) | $100 | ~7,403 |

**Lesson from Price Audit Fail pattern:**"""

if old_audit in tracker:
    tracker = tracker.replace(old_audit, new_audit)
    print("[OK] tracker.md Price Audit Fail table updated with ALAB")
else:
    print("[WARN] Price Audit Fail table pattern not found — check manually")

with open(tracker_path, "w", encoding="utf-8") as f:
    f.write(tracker)

print(f"[OK] tracker.md updated — {len(tracker)} chars")

print("\n=== DONE: decisions.md rebuilt + tracker.md updated ===")
print("Next: Run _run_alab_update.py for data.js update")
