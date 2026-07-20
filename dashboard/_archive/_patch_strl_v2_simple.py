#!/usr/bin/env python3
"""
Simple line-based patch for STRL v2 update in data.js
"""

data_file = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

with open(data_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find STRL section (look for ticker: "STRL")
strl_ticker_line = -1
for i, line in enumerate(lines):
    if 'ticker: "STRL"' in line:
        strl_ticker_line = i
        break

if strl_ticker_line == -1:
    print("ERROR: STRL ticker line not found")
    exit(1)

print(f"Found STRL ticker at line {strl_ticker_line + 1}")

# Define replacements as (search_text, replacement_text) for lines near STRL
replacements = {
    '    price: 130.00,\n': '    price: 880.00,\n',
    '    recommendation: "HOLD",\n': '    recommendation: "AVOID",\n',
    '    blendedFV: 96.00,\n': '    blendedFV: 156.00,\n',
    '    targetBull: 128.00,\n': '    targetBull: 320.00,\n',
    '    targetBase: 96.00,\n': '    targetBase: 156.00,\n',
    '    stopLoss: 75.00,\n': '    stopLoss: 0,\n',
    '    convictionQuinn: 6,\n': '    convictionQuinn: 8,\n',
    '    convictionBear: 5,\n': '    convictionBear: 7,\n',
    '    convictionAvg: 6.0,\n': '    convictionAvg: 7.3,\n',
    '    pwEV: 85.20,\n': '    pwEV: 164.60,\n',
    '    esgScore: 5.4,\n': '    esgScore: 5.0,\n',
    '    esgRating: "Medium",\n': '    esgRating: "Medium-Low",\n',
    '    entryZone: "$95-110",\n': '    entryZone: "$200-270 (genuine) / $665-735 (reverse split)",\n',
    '    positionSize: "3-4% (3 tranches)",\n': '    positionSize: "0% (AVOID / Kelly Negative)",\n',
}

# Apply replacements only in STRL section (lines strl_ticker_line-1 to strl_ticker_line+30)
search_range = range(max(0, strl_ticker_line - 2), min(len(lines), strl_ticker_line + 35))
changes_made = 0

for i in search_range:
    original = lines[i]
    if original in replacements:
        lines[i] = replacements[original]
        print(f"  Line {i+1}: {original.strip()} -> {replacements[original].strip()}")
        changes_made += 1

# Also update LAST_UPDATED
for i, line in enumerate(lines):
    if 'const LAST_UPDATED = "2026-05-07";' in line:
        lines[i] = 'const LAST_UPDATED = "2026-05-07 (STRL v2)";\n'
        print(f"  Line {i+1}: LAST_UPDATED updated")
        break

# Also update keyThesis for STRL
for i in search_range:
    if 'keyThesis: "AI/Data center civil contractor' in lines[i]:
        lines[i] = '    keyThesis: "RE-ANALYSIS v2: AVOID at $880. Blended FV $156 = MOS -82.3%. P/S 10.7x vs peer median 0.7x = extreme overvaluation. Kelly NEGATIVE. CRITICAL: Possible Reverse Split (7:1) - verify shares before investing.",\n'
        print(f"  Line {i+1}: keyThesis updated")
        changes_made += 1
        break

# Update topRisk for STRL
for i in search_range:
    if 'topRisk: "DOGE/Federal spending cut' in lines[i]:
        lines[i] = '    topRisk: "Valuation mean-reversion (P/S 10.7x to 1.5x = -86%) + Momentum reversal (AI narrative break = -50-80%) + Reverse split uncertainty",\n'
        print(f"  Line {i+1}: topRisk updated")
        changes_made += 1
        break

with open(data_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"\ndata.js updated: {changes_made} changes made")
print("STRL v2 patch complete.")
