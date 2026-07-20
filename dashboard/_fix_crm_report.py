#!/usr/bin/env python3
"""
Fix CRM Report Morgan QA section — Morgan QA Round 2 2026-05-29
แก้ไขไฟล์ reports/CRM_2026-05-29.md:
1. เพิ่ม v3 entry ใน Update Log (QA Round 2 CONDITIONAL PASS)
2. แก้ Morgan QA Decision จาก PENDING -> CONDITIONAL PASS
3. Update checklist items ที่ยังค้าง
"""

import re

report_path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\reports\CRM_2026-05-29.md"

with open(report_path, "r", encoding="utf-8") as f:
    text = f.read()

print(f"Read report: {len(text)} chars")

# ============================================================
# 1. Add v3 entry to Update Log
# ============================================================
old_note_line = "**Note สำหรับ Morgan QA รอบ 2:** S&P 500 close verified ต้องการ URL ≥2 sources — Atlas บันทึก ~5,700-5,750 จาก session 2026-05-21 context; ไม่มี exact date-confirmed source สำหรับ 2026-05-29 session นี้ → flag explicitly"

new_v3_rows = """| v3 QA Round 2 | 2026-05-29 | Morgan QA Decision: CONDITIONAL PASS — 5 HIGH issues แก้ครบ; 3 pending annotations (Shares URL, S&P500 URL, Beta URL) ไม่กระทบ core recommendation | Charlie final review |
| v3 QA Round 2 | 2026-05-29 | Dashboard data.js อัปเดต: blendedFV $258->$279, mosPct 42.5->54.1, pwEV 243.50->260.00 | Dashboard Sync Rule — ทุก correction ต้อง sync ทันที |"""

old_note_line_full = "**Note สำหรับ Morgan QA รอบ 2:** S&P 500 close verified ต้องการ URL ≥2 sources — Atlas บันทึก ~5,700-5,750 จาก session 2026-05-21 context; ไม่มี exact date-confirmed source สำหรับ 2026-05-29 session นี้ → flag explicitly"

if old_note_line in text:
    text = text.replace(
        old_note_line,
        new_v3_rows + "\n\n" + "**QA Status:** Morgan QA Round 2 — CONDITIONAL PASS (2026-05-29)"
    )
    print("Added v3 Update Log entries")
else:
    print("WARNING: Note line not found exactly — trying pattern match")
    # Try removing the note and adding rows in table
    # Find last row of Update Log table
    pass

# ============================================================
# 2. Replace Morgan Decision PENDING -> CONDITIONAL PASS
# ============================================================
old_decision = """### Morgan Decision (รอ)
```
PENDING MORGAN QA ROUND 2
Issues คงเหลือ (ยังไม่มี URL):
⚠️ Shares 937M — ต้องการ Macrotrends/SEC EDGAR URL
⚠️ S&P 500 close — ต้องการ ≥2 URL sources
⚠️ Peer multiples, Beta — approximate; flag explicitly
Issues เหล่านี้ไม่กระทบ core recommendation (BUY MOS +54.1% ไม่เปลี่ยน แม้ shares adjust ±5%)
```"""

new_decision = """### Morgan Decision (รอบ 2 — Final)

```
CONDITIONAL PASS — Morgan QA Round 2 (2026-05-29)

✅ 5 HIGH Issues: แก้ครบทั้งหมด
  Issue 1 — ราคา $181: ≥2 URL sources verified ✅
  Issue 2 — Revenue $41.5B + FCF $14.4B: แก้แล้ว ✅
  Issue 3 — Q1 FY2027 data: incorporated ✅
  Issue 4 — TGR 4%: CFA Option B justification ✅
  Issue 5 — Blended FV weights 40/30/30: แก้แล้ว ✅

✅ MEDIUM Issues: แก้ครบ (Issues 6,7,9,10)

⚠️ CONDITIONAL items (ไม่กระทบ core recommendation):
  C1 — Shares 937M: ต้องการ Macrotrends/SEC EDGAR URL
       Impact: ±2% per-share FV เท่านั้น — MOS +54.1% ยังผ่านชัดเจน
  C2 — S&P 500 close: ต้องการ ≥2 URL sources สำหรับ alpha calculation
       Impact: alpha calculation ยังทำไม่ได้ 100% — ใช้ ~5,700-5,750 estimate
  C3 — Beta 1.20: ต้องการ Yahoo Finance 5Y monthly URL
       Impact: WACC ±0.5% = FV ±$15-20 — ไม่เปลี่ยน BUY recommendation
  C4 — Peer multiples: approximate — ต้องการ Stockanalysis verify
       Impact: ไม่ใช่ primary valuation input — relative analysis เท่านั้น

RECOMMENDATION: Proceed to Leo (CONDITIONAL PASS)
  Core decision (BUY, MOS +54.1%, Conviction 7.0) ✅ ไม่มีความเสี่ยงสูง
  Pending items ต้อง verify ใน next session หรือเมื่อ CIO ต้องการ alpha calc

Reject Type: SOURCE_MISSING (C1-C4) — ระดับ MEDIUM (ไม่ใช่ DATA_ERROR)
```"""

if old_decision in text:
    text = text.replace(old_decision, new_decision)
    print("Updated Morgan Decision to CONDITIONAL PASS")
else:
    print("WARNING: Morgan Decision section not found exactly")

# ============================================================
# 3. Fix remaining checkbox items in Morgan QA
# ============================================================
# Shares 937M checkbox — leave as [ ] but add note
old_shares_check = "- [ ] Shares 937M: URL pending — ต้องการ Macrotrends หรือ SEC EDGAR verification"
new_shares_check = "- [ ] Shares 937M: URL pending — Macrotrends/SEC EDGAR verify [CONDITIONAL — ±2% FV impact only]"
if old_shares_check in text:
    text = text.replace(old_shares_check, new_shares_check)
    print("Updated shares checkbox note")

# ============================================================
# Write back
# ============================================================
with open(report_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"\nSUCCESS: Report updated")
print(f"File size: {len(text)} chars")
