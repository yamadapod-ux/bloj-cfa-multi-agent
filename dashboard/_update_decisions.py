#!/usr/bin/env python3
# Script: append CLFD row to portfolio/decisions.md Decision History table
# Safe method: find "---\n\n## Re-Analysis Log" and insert new row before it

DECISIONS_MD = r"C:\Users\user\Desktop\บลจ\บลจ CFA\portfolio\decisions.md"

with open(DECISIONS_MD, "rb") as f:
    content = f.read().decode("utf-8")

# New CLFD row to insert
clfd_row = "| **2026-05-22** | **CLFD** | **Clearfield, Inc.** | **HOLD/WAIT — รอ Pullback** | **$42.71** (Yahoo Finance real-time ✅ / Stockanalysis $44.50 ✅ gap 4.2%) | **6.0/10** | **$24.15** (Emma $28.07×40% + Quinn $22.29×30% + Bear $21.20×30%) | Fiber optic equipment for rural ISPs. BEAD $42.45B tailwind real แต่ timing uncertain. FCF positive TTM $14.44M. MOS -43.4% vs Blended FV $24.15. 84% sensitivity scenarios negative return. H2 FY2026 ต้องทำ +83% จาก Q2 run rate. RISK-ON 3/4 แต่ MOS ไม่ผ่าน Value gate → ไม่ deploy. Entry zone $20-26. **S&P 500 ref 7,432.97** (last verified Atlas 2026-05-21) | **$19.32 (-20% จาก entry mid $24.15)** |\n"

# Find insertion point: before "---\n\n## Re-Analysis Log"
marker = "---\n\n## Re-Analysis Log"
pos = content.find(marker)

if pos == -1:
    print("ERROR: Could not find Re-Analysis Log marker")
    exit(1)

print(f"Found marker at position {pos}")

# Insert CLFD row before the "---\n\n## Re-Analysis Log"
new_content = content[:pos] + clfd_row + content[pos:]

with open(DECISIONS_MD, "wb") as f:
    f.write(new_content.encode("utf-8"))

print("SUCCESS: CLFD row appended to decisions.md")

# Verify
with open(DECISIONS_MD, "rb") as f:
    verify = f.read().decode("utf-8")
if "CLFD" in verify and "Clearfield" in verify:
    print("VERIFICATION: CLFD found in decisions.md ✓")
else:
    print("VERIFICATION FAILED")
