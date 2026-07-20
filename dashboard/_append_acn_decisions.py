#!/usr/bin/env python3
"""Append ACN entry to portfolio/decisions.md"""
import os

BASE = r"C:\Users\user\Desktop\บลจ\บลจ CFA"
DECISIONS_PATH = os.path.join(BASE, "portfolio", "decisions.md")

ACN_ENTRY = """| **2026-06-05** | **ACN** | **Accenture PLC** | **BUY (Value Bucket — Staged Entry)** | **$178.16** (stockanalysis.com 2026-06-04 + stocktitan.net 2026-06-04 ✅ ≥2 URL) | **7.17/10** | **$252.35** (Emma $287×40% + Quinn $285×30% + Bear $173.50×30%) | Wide Moat IT Services / AI Consulting. Revenue Q2 FY26 $18.0B +8% USD/+13% LC. Bookings Q2 FY26 **$22.1B all-time record** (bull/bear debate: demand acceleration vs pull-forward). FCF Yield 11.42% = highest in IT Services universe. ROIC 27.19% >> WACC 9.5% = EVA spread +17.7%. P/E 14.54× = 31% discount vs peer median 21× = "Best quality at worst valuation" in sector. AI thesis: ACN BENEFITS from AI implementation wave (same pattern ADBE/CRM). Bear: Revenue CAGR 3.5–5% vs Emma 8% (structural disruption risk). Sensitivity Matrix: 96% of 25 scenarios above current price. Value bucket Conv 7.17 ≥ 7.0 ✅, MOS +41.6% ≥ 15% ✅. RISK-ON 4/4 + Force Deploy ACTIVE. Morgan CONDITIONAL PASS (Shares outstanding ~632M needs URL verify). T1 5% $175–192, T2 3% $155–175, T3 2% $140–155. **S&P 500 ref 7,553.68** (June 3 close — positions.md verified) | **$148 (-20.0% จาก entry mid $185)** |
"""

ACN_REANALYSIS = """
"""

with open(DECISIONS_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Find the last row in the table (before the Re-Analysis Log section)
# Insert after the REGN entry (last entry before "---")
insert_marker = "| **2026-06-03**"
if insert_marker in content:
    # Find the end of the REGN line
    idx = content.rfind(insert_marker)
    # Find the newline after this entry
    end_of_line = content.find("\n", idx)
    if end_of_line == -1:
        end_of_line = len(content)
    # Insert ACN entry after REGN
    content = content[:end_of_line+1] + ACN_ENTRY + content[end_of_line+1:]
    print("ACN entry inserted after REGN row")
else:
    # Append to end if not found
    content = content.rstrip() + "\n" + ACN_ENTRY
    print("ACN entry appended to end of file")

with open(DECISIONS_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("decisions.md updated successfully")
print(f"File size: {len(content)} chars")
