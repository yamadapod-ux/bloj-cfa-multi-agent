#!/usr/bin/env python3
"""
Update performance/tracker.md for ACN analysis.
Append ACN entry in Recommendations section and update W23 weekly report.
"""
import os

BASE = r"C:\Users\user\Desktop\บลจ\บลจ CFA"
TRACKER_PATH = os.path.join(BASE, "performance", "tracker.md")

with open(TRACKER_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add ACN to Recommendations Without Position tracking section
# Find the CRM line in that table and insert ACN after it
acn_rec_row = """| **ACN** | **2026-06-05** | **7,553.68** (June 3 close — positions.md) | **BUY (Value) $178.16** | **Deployed T1 5% — OPEN** | OPEN — tracking | — | **ALPHA PENDING** | Wide Moat IT Services, FCF yield 11.42%, Bookings ATH $22.1B, P/E 14.54x (31% discount) |
"""

# Insert after RDDT/last CRM row in recommendations table
insert_marker = "| **CRM** | **2026-05-29**"
if insert_marker in content:
    idx = content.find(insert_marker)
    end_of_line = content.find("\n", idx)
    content = content[:end_of_line+1] + acn_rec_row + content[end_of_line+1:]
    print("ACN recommendation row inserted in tracking table")

# 2. Update Week 2026-W23 section to include ACN
acn_w23_update = """- New Analysis: **ACN (2026-06-05)** — BUY Value Bucket | Conviction 7.17/10 | MOS +41.6% | Blended FV $252.35 | Stop $148
- Deploy trigger: **ACN T1 5% deploy at ~$178 — Force Deploy ACTIVE (Cash 69.28% > 30% + RISK-ON 4/4)**
- ACN Key patterns:
  - IT Services + AI Consulting = first non-software IT services sector in portfolio
  - Same AI fear pattern as ADBE/CRM: Wide Moat -43% drawdown = buy opportunity
  - FCF Yield 11.42% = strongest value signal across all VALUE bucket analyses
  - Bookings ATH $22.1B = leading indicator confirming demand; monitor Q3 FY26 (June 19)
  - Bear weight 30% (structural ongoing AI disruption = between 25% pure quality and 40% existential binary)
"""

# Find the W23 section and append ACN info
w23_marker = "- Action items: Run `dashboard/_patch_regn.py` to update dashboard/data.js"
if w23_marker in content:
    idx = content.find(w23_marker)
    end_of_line = content.find("\n", idx)
    content = content[:end_of_line+1] + acn_w23_update + content[end_of_line+1:]
    print("ACN update added to W23 weekly report")

# 3. Add ACN to Active Positions table
acn_position_row = """| **ACN** | **2026-06-05** | **$178.16** | **T1 planned (~2.8 shares)** | **~$500** | **$178.16** | **+0.00%** | **+0.00%** | **7,553.68** | **7,553.68** | **OPEN T1 — NEW 2026-06-05** |
"""

regn_position_marker = "| **REGN** | **2026-06-03**"
if regn_position_marker in content:
    idx = content.find(regn_position_marker)
    end_of_line = content.find("\n", idx)
    content = content[:end_of_line+1] + acn_position_row + content[end_of_line+1:]
    print("ACN position row added to Active Positions table")

with open(TRACKER_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("tracker.md updated successfully for ACN")
print(f"File size: {len(content)} chars")
