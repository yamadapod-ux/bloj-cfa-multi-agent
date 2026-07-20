"""Append ALAB row to portfolio/decisions.md — Leo script 2026-05-20"""
import os

BASE = r'C:\Users\user\Desktop\บลจ\บลจ CFA'
filepath = os.path.join(BASE, 'portfolio', 'decisions.md')

with open(filepath, 'rb') as f:
    raw = f.read()

# The new ALAB row to append
alab_row = (
    '| **2026-05-20** | **ALAB** | **Astera Labs, Inc.** | **HOLD/WAIT FOR PULLBACK** | **~$60 (est.)** | **6.7/10** | **$48.5** | '
    'AI Connectivity (CXL/PCIe) pure-play — FY2024 Rev $396M +244% YoY. Blended FV $48.5 (Emma $53×40% + Quinn $52.4×35% + Bear $36.6×25%). '
    'MOS -19.2% at $60. Growth MOS: PASS (Reverse DCF 0.78x < 1.2x; EV/Rev ~62nd percentile < 70th). '
    'Customer concentration ⚠️ Top 2 (Microsoft+Google) ~50%+ = primary binary risk. Marvell/Broadcom entering CXL in 12-18mo. '
    'Conviction 6.7 < 7.0 BUY gate at $60. Regime TRANSITIONAL-CAUTIOUS = Force Deploy suspended. '
    'Entry T1 $45-50 (2%), T2 $41-45 (1%), Max 3%. '
    'Sector: Semiconductors/AI Connectivity. Bucket: Growth. IPO Mar 2024. S&P 500 ref ~7,403 (est. 2026-05-20). | **$36 (-20% จาก entry $45)** |\n'
)

# Insert before the '---' separator before Re-Analysis Log
# Find the separator that precedes Re-Analysis Log
marker = b'\n---\n\n## Re-Analysis Log'
idx = raw.find(marker)

if idx == -1:
    # Fallback: just append at end
    raw = raw + b'\n' + alab_row.encode('utf-8')
else:
    insert = ('\n' + alab_row).encode('utf-8')
    raw = raw[:idx] + insert + raw[idx:]

with open(filepath, 'wb') as f:
    f.write(raw)

print('ALAB row appended to decisions.md successfully')
