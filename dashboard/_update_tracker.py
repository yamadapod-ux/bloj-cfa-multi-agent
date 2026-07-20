#!/usr/bin/env python3
# Script: update performance/tracker.md for CLFD session
# 1. Add CLFD row to Recommendations Without Position table
# 2. Update W21 weekly report
# 3. Update Conviction Calibration table (6.0-6.4 bucket)
# 4. Append CLFD watchlist entry at end

TRACKER_MD = r"C:\Users\user\Desktop\บลจ\บลจ CFA\performance\tracker.md"

with open(TRACKER_MD, "rb") as f:
    content = f.read().decode("utf-8")

# === UPDATE 1: Add CLFD row to Recommendations Without Position table ===
# Find the FPS row and add CLFD after it
fps_row_marker = "| **FPS** | **2026-05-22** |"
clfd_row = "\n| **CLFD** | **2026-05-22** | **7,432.97** (last verified Atlas 2026-05-21) | **HOLD/WAIT $42.71** | **MOS -43.4%, Conviction 6.0 (Value gate exact), MOS gate FAIL** | WATCHLIST — รอ entry $20-26 | — | — | Fiber optic recovery + BEAD thesis แต่ราคาแพงกว่า FV 43.4%; 84% Sensitivity scenarios negative; H2 FY2026 ต้องทำ +83% step-up; Bear 7/10 confidence ว่า $42.71 แพง |"

pos = content.find(fps_row_marker)
if pos != -1:
    # Find end of FPS row (next newline after the row)
    end_of_fps = content.find("\n", pos)
    if end_of_fps != -1:
        content = content[:end_of_fps] + clfd_row + content[end_of_fps:]
        print("UPDATE 1: CLFD row added to Recommendations Without Position table ✓")
    else:
        print("WARNING: Could not find end of FPS row")
else:
    print("WARNING: FPS row not found — appending CLFD separately")

# === UPDATE 2: Update W21 weekly report — add CLFD ===
w21_marker = "- New Analysis this week: META (2026-05-19), GOOGL (2026-05-20/21), ALAB (2026-05-20), **FPS (2026-05-22)**"
w21_replacement = "- New Analysis this week: META (2026-05-19), GOOGL (2026-05-20/21), ALAB (2026-05-20), **FPS (2026-05-22)**, **CLFD (2026-05-22)**"

if w21_marker in content:
    content = content.replace(w21_marker, w21_replacement, 1)
    print("UPDATE 2: W21 weekly report updated ✓")
else:
    print("WARNING: W21 marker not found")

# === UPDATE 3: Update Conviction Calibration — 6.0-6.4 bucket ===
old_6064 = "| 6.0–6.4 | **5** (AMD v1, RKLB, LDOS, AMD v2, **FPS 6.0**) |"
new_6064 = "| 6.0–6.4 | **6** (AMD v1, RKLB, LDOS, AMD v2, FPS 6.0, **CLFD 6.0**) |"

if old_6064 in content:
    content = content.replace(old_6064, new_6064, 1)
    print("UPDATE 3: Conviction Calibration 6.0-6.4 updated ✓")
else:
    print("WARNING: Conviction Calibration row not found")

# Also update the note line
old_note = "**FPS เพิ่มใน 6.0–6.4 bucket (Conviction 6.0) — HOLD/WAIT watchlist**"
new_note = "**FPS เพิ่มใน 6.0–6.4 bucket (Conviction 6.0) — HOLD/WAIT watchlist**\n**CLFD เพิ่มใน 6.0–6.4 bucket (Conviction 6.0) — HOLD/WAIT watchlist; Value gate barely met แต่ MOS -43.4% ไม่ผ่าน MOS gate**"

if old_note in content:
    content = content.replace(old_note, new_note, 1)
    print("UPDATE 3b: Conviction note updated ✓")

# === UPDATE 4: Append CLFD Watchlist Entry at end ===
clfd_watchlist = """
---

## CLFD Watchlist Entry (2026-05-22)

| Field | ค่า |
|-------|-----|
| Ticker | CLFD |
| Date | 2026-05-22 |
| Rec | HOLD/WAIT — รอ Pullback สู่ Entry Zone |
| Price at Analysis | $42.71 (Yahoo Finance real-time ✅ / Stockanalysis $44.50 ✅ gap 4.2%) |
| S&P 500 at Analysis | 7,432.97 (last verified Atlas 2026-05-21) |
| Blended FV | $24.15 (Emma $28.07×40% + Quinn $22.29×30% + Bear $21.20×30%) |
| ESG-adj FV | $23.67 (-2%) |
| MOS | **-43.4%** (ราคา $42.71 เกิน FV $24.15) |
| Conviction | **6.0/10** |
| Conviction Gate | BARELY MET (Value gate 6.0 — exact) |
| Value MOS Gate | NOT MET (MOS -43.4% vs threshold +15%) |
| Sensitivity Matrix | 84% scenarios negative ณ $42.71 |
| Entry Zone | $22-26 (T1: near Blended FV) / $18-22 (T2: near Bear FV floor) |
| Max Position | 5% (Value Bucket, RISK-ON 1.0x — เมื่อ entry zone ถึง) |
| Stop Loss | $19.32 (-20% จาก entry mid $24.15) |
| Trigger | Price pullback สู่ $20-26 + H2 FY2026 revenue confirmation ≥ $50M Q3 |
| Key Risks | BEAD timing delay, H2 +83% step-up, Corning competition, GM 37% low |
| Morgan QA | CONDITIONAL PASS (Net Cash $80.13M reconciliation flag) |
| Bucket | Value Primary + Growth Overlay (BEAD catalyst) |
| Moat | Narrow (customer relationships + speed-to-market + rural ISP focus) |
"""

content = content + clfd_watchlist
print("UPDATE 4: CLFD Watchlist Entry appended ✓")

# Write back
with open(TRACKER_MD, "wb") as f:
    f.write(content.encode("utf-8"))

print("SUCCESS: tracker.md updated")

# Verify
with open(TRACKER_MD, "rb") as f:
    verify = f.read().decode("utf-8")
if "CLFD" in verify and "Clearfield" in verify:
    print("VERIFICATION: CLFD found in tracker.md ✓")
else:
    print("VERIFICATION FAILED")
