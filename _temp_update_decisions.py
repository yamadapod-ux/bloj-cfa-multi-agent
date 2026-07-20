#!/usr/bin/env python3
"""Leo: Append RDDT row to portfolio/decisions.md"""

import os

decisions_path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\portfolio\decisions.md"

new_row = "| **2026-05-30** | **RDDT** | **Reddit, Inc.** | **BUY (Growth Bucket — Staged Entry)** | **$175.94** (StockAnalysis.com 2026-05-29 https://stockanalysis.com/stocks/rddt/ + SEC Q1 2026 implied $33.87B/192.51M ✅ ≥2 URL) | **6.67/10** | **$169.25** (Emma $140×40% + Quinn $248.50×30% + Bear $129×30%) | Growth social platform w/ AI data licensing moat. Revenue +69% YoY, Q2 guided +72%. AI licensing $60M/yr → $400M/yr potential. ARPU $5.23 growing. Debt-free $2.77B net cash. ROIC 56.7%. Growth MOS: Reverse DCF 1.03× (≤1.2×) + 55-60th pct (≤70th) — BOTH PASS. Risk: Meta Forum (May 2026), Google double-dependency. T1 5% entry $155-178, T2 3% at $145-160 or AI licensing $200M+ confirm. **S&P 500 ref 7,591.42** (May 29 close — Investing.com + Trading Economics) | **$140.75 (-20.0% from entry $175.94)** |\n"

with open(decisions_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before the Re-Analysis Log section (or at the end of Decision History table)
insert_marker = "\n---\n\n## Re-Analysis Log"
if insert_marker in content:
    content = content.replace(insert_marker, "\n" + new_row + insert_marker)
    print("Inserted before Re-Analysis Log section")
else:
    # fallback: append at end
    content = content + "\n" + new_row
    print("Appended at end (fallback)")

with open(decisions_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("decisions.md updated successfully")
print(f"File size: {os.path.getsize(decisions_path)} bytes")
