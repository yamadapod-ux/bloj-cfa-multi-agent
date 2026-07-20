#!/usr/bin/env python3
"""Leo: Append RDDT row to portfolio/decisions.md"""
import os

decisions_path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\portfolio\decisions.md"

new_row = "| **2026-05-30** | **RDDT** | **Reddit, Inc.** | **BUY (Growth Bucket — Staged Entry)** | **$175.94** (StockAnalysis.com 2026-05-29 https://stockanalysis.com/stocks/rddt/ + SEC Q1 2026 8-K implied $33.87B/192.51M = $175.94 ✅ ≥2 sources) | **6.67/10** | **$169.25** (Emma $140×40% + Quinn $248.50×30% + Bear $129×30%) | Growth social platform w/ AI data licensing moat. Revenue +69% YoY Q1 2026, Q2 guided +72%. AI licensing $60M/yr → $400M/yr potential. ARPU $5.23 growing +45% YoY. Debt-free $2.77B net cash. ROIC 56.7%. Growth MOS: Reverse DCF 1.03× (≤1.2×) + 55-60th pct (≤70th) — BOTH PASS. Risk: Meta Forum app (May 2026), Google double-dependency (traffic + data deal). T1 5% entry $155-178, T2 3% conditional. **S&P 500 ref 7,591.42** (May 29 close) | **$140.75 (-20.0% from entry $175.94)** |\n"

with open(decisions_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before the Re-Analysis Log section
insert_marker = "\n---\n\n## Re-Analysis Log"
if insert_marker in content:
    content = content.replace(insert_marker, "\n" + new_row + insert_marker, 1)
    print("Inserted RDDT row before Re-Analysis Log section")
else:
    # fallback: before the last ---
    last_dash = content.rfind("\n---\n")
    if last_dash != -1:
        content = content[:last_dash] + "\n" + new_row + content[last_dash:]
        print("Inserted RDDT row before last --- (fallback)")
    else:
        content = content.rstrip() + "\n" + new_row
        print("Appended RDDT row at end (final fallback)")

with open(decisions_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"decisions.md updated: {os.path.getsize(decisions_path)} bytes")
