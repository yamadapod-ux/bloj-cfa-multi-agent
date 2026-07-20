#!/usr/bin/env python3
"""
Dashboard CRM v2 Update Script — Morgan QA Fix 2026-05-29
อัปเดต CRM entry ใน data.js ด้วยค่า v2 ที่ถูกต้อง

การเปลี่ยนแปลง:
- blendedFV: 258.00 -> 279.00  (weights corrected 40/30/30 per CLAUDE.md)
- targetBase: 258.00 -> 279.00
- targetBull: 365.00 -> 400.00
- mosPct: 42.5 -> 54.1  (FV $279 vs $181)
- pwEV: 243.50 -> 260.00  (Quinn P-W EV v2 with FCF $14.4B base)
- keyThesis: updated with v2 data
- topRisk: updated
- thesisBullets: Agentforce +169% -> +205% updated
- fullContent: updated with v2 summary (single-line in JS)
- competitorData CRM row: revenueGrowth 8.5->10.5, marketCap 175->169.6
"""

import re

data_js_path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

with open(data_js_path, "rb") as f:
    content = f.read()

text = content.decode("utf-8")

print(f"Read data.js: {len(text)} chars")

if 'ticker: "CRM"' not in text:
    print("ERROR: CRM entry not found in data.js")
    exit(1)

print("CRM entry found. Applying v2 updates...")

changes_made = []

# ============================================================
# 1. blendedFV: 258.00 -> 279.00
# ============================================================
if "    blendedFV: 258.00," in text:
    text = text.replace("    blendedFV: 258.00,", "    blendedFV: 279.00,", 1)
    changes_made.append("blendedFV: 258 -> 279")
else:
    print("WARNING: blendedFV 258.00 not found")

# ============================================================
# 2. targetBase: 258.00 -> 279.00
# ============================================================
if "    targetBase: 258.00," in text:
    text = text.replace("    targetBase: 258.00,", "    targetBase: 279.00,", 1)
    changes_made.append("targetBase: 258 -> 279")
else:
    print("WARNING: targetBase 258.00 not found")

# ============================================================
# 3. targetBull: 365.00 -> 400.00
# ============================================================
if "    targetBull: 365.00," in text:
    text = text.replace("    targetBull: 365.00,", "    targetBull: 400.00,", 1)
    changes_made.append("targetBull: 365 -> 400")
else:
    print("WARNING: targetBull 365.00 not found")

# ============================================================
# 4. mosPct: 42.5 -> 54.1
# ============================================================
if "    mosPct: 42.5," in text:
    text = text.replace("    mosPct: 42.5,", "    mosPct: 54.1,", 1)
    changes_made.append("mosPct: 42.5 -> 54.1")
else:
    print("WARNING: mosPct 42.5 not found")

# ============================================================
# 5. pwEV: 243.50 -> 260.00
# ============================================================
if "    pwEV: 243.50," in text:
    text = text.replace("    pwEV: 243.50,", "    pwEV: 260.00,", 1)
    changes_made.append("pwEV: 243.50 -> 260.00")
else:
    print("WARNING: pwEV 243.50 not found")

# ============================================================
# 6. keyThesis — update with v2 data (regex approach for Thai text)
# ============================================================
old_thesis_pattern = r'keyThesis: "Wide Moat enterprise CRM trade[^"]*",'
new_thesis = 'keyThesis: "v2 QA Fix: Salesforce Wide Moat CRM. FCF $14.4B FY2026 official. Revenue $41.5B. Q1 FY27 +13% re-acceleration. Agentforce ARR $1.2B +205% YoY. FY27 guide $45.8-46.2B. Blended FV $279 (40/30/30). MOS +54.1%. Conviction 7.0/10. BUY Staged Entry.",'
match = re.search(old_thesis_pattern, text)
if match:
    text = re.sub(old_thesis_pattern, new_thesis, text, count=1)
    changes_made.append("keyThesis: updated")
else:
    print("WARNING: keyThesis pattern not matched")

# ============================================================
# 7. topRisk — update
# ============================================================
old_risk = '    topRisk: "ROIC 6.29% < WACC 9.5% (EVA negative) + Microsoft Dynamics structural threat",'
new_risk = '    topRisk: "ROIC 6.3% < WACC 9.5% (EVA negative); Microsoft Dynamics bundle M365 = structural threat; Agentforce $1.2B = only 2.9% revenue (early stage); Q2 FY27 must sustain +12-13% growth",'
if old_risk in text:
    text = text.replace(old_risk, new_risk, 1)
    changes_made.append("topRisk: updated")
else:
    print("WARNING: topRisk not matched — trying without leading spaces")
    old_risk_alt = 'topRisk: "ROIC 6.29% < WACC 9.5% (EVA negative) + Microsoft Dynamics structural threat",'
    if old_risk_alt in text:
        text = text.replace(old_risk_alt, 'topRisk: "ROIC 6.3% < WACC 9.5% (EVA negative); Microsoft Dynamics bundle M365 = structural threat; Agentforce $1.2B = only 2.9% revenue; Q2 FY27 must sustain +12-13% growth",', 1)
        changes_made.append("topRisk: updated (alt match)")

# ============================================================
# 8. thesisBullets — Agentforce +169% -> +205%
# ============================================================
old_bullet2 = '{ title: "Agentforce ARR $1.2B +169% YoY"'
new_bullet2_start = '{ title: "Agentforce ARR $1.2B +205% YoY (Q1 FY27) - Accelerating"'
if old_bullet2 in text:
    text = text.replace(old_bullet2, new_bullet2_start, 1)
    changes_made.append("thesisBullet: +169% -> +205%")
else:
    print("WARNING: Agentforce bullet +169% not found")

# ============================================================
# 9. fullContent — update (single-line replacement)
# ============================================================
old_full = 'fullContent: `# CRM — Salesforce, Inc. Full Research Report 2026-05-29\\n\\nSee reports/CRM_2026-05-29.md for full content\\n\\nBUY | Blended FV $258 | MOS +42.5% | Conviction 7.0/10\\nEntry Zone $170-195 | Stop Loss $146 (-20% from entry $182.50)\\nFCF yield 9.77% + Forward P/E 13x + Agentforce ARR $1.2B +169% + RPO $72.4B\\nValue Bucket: IPS Gate PASS (Conv 7.0 >= 7.0, MOS +42.5% >= 15%)\\nRisk: ROIC 6.29% < WACC 9.5% (EVA negative), Microsoft Dynamics structural threat`'

new_full = 'fullContent: `## CRM v2 QA Fix 2026-05-29 - Salesforce, Inc.\\n### BUY | Blended FV $279 (40/30/30) | MOS +54.1% | Conviction 7.0/10\\n\\n## v2 Changes: Revenue $37.9B->$41.5B | FCF $13.1B->$14.4B | Agentforce +169%->+205%\\nWeights: 40/35/25->40/30/30 | Blended FV: $258->$279 | MOS: +42.5%->+54.1%\\nQ1 FY27: Revenue +13% YoY re-acceleration | FY27 guide $45.8-46.2B\\n\\n## Entry Zone $170-195 | T1 $175-190 (4%) | Stop $146 (-20% from $182.50)\\nForward Return 3Y: +15.4%/yr CAGR (+53.8% total)\\n\\n## Blended FV: Emma $351 x40% + Quinn $260 x30% + Bear $202 x30% = $279\\nSources: salesforce.com/news/press-releases/2026/05/27/fy27-q1-earnings/\\nMorgan QA: CONDITIONAL PASS (Shares/S&P500/Beta URL CONDITIONAL)`'

# Use unicode escape for em dash in old string
if 'fullContent: `# CRM —' in text:
    text = text.replace(old_full, new_full, 1)
    changes_made.append("fullContent: updated to v2")
else:
    # Try with literal em dash character
    old_full_literal = old_full.replace('\\u2014', '—')
    if old_full_literal in text:
        text = text.replace(old_full_literal, new_full, 1)
        changes_made.append("fullContent: updated to v2 (literal match)")
    else:
        # Try regex
        full_pattern = r'fullContent: `# CRM [^\n]*Full Research Report 2026-05-29[^`]*`'
        if re.search(full_pattern, text):
            text = re.sub(full_pattern, new_full, text, count=1)
            changes_made.append("fullContent: updated (regex match)")
        else:
            print("WARNING: fullContent pattern not matched by any method")

# ============================================================
# 10. competitorData CRM row
# ============================================================
old_comp = '{ ticker: "CRM", company: "Salesforce", revenueGrowth: 8.5, operatingMargin: 15, marketCap: 175 },'
new_comp = '{ ticker: "CRM", company: "Salesforce", revenueGrowth: 10.5, operatingMargin: 15, marketCap: 169.6 },'
if old_comp in text:
    text = text.replace(old_comp, new_comp, 1)
    changes_made.append("competitorData: revenueGrowth 8.5->10.5, marketCap 175->169.6")
else:
    # Try without trailing comma
    old_comp_nc = '{ ticker: "CRM", company: "Salesforce", revenueGrowth: 8.5, operatingMargin: 15, marketCap: 175 }'
    if old_comp_nc in text:
        text = text.replace(old_comp_nc, '{ ticker: "CRM", company: "Salesforce", revenueGrowth: 10.5, operatingMargin: 15, marketCap: 169.6 }', 1)
        changes_made.append("competitorData: revenueGrowth 8.5->10.5, marketCap 175->169.6 (no comma)")
    else:
        print("WARNING: competitorData CRM row not matched")

# ============================================================
# Write back
# ============================================================
with open(data_js_path, "wb") as f:
    f.write(text.encode("utf-8"))

print(f"\nSUCCESS: data.js updated with {len(changes_made)} changes:")
for c in changes_made:
    print(f"  + {c}")

# Verification
with open(data_js_path, "r", encoding="utf-8") as f:
    verify = f.read()

print("\nVerification:")
checks = [
    ("blendedFV: 279.00", "blendedFV updated"),
    ("mosPct: 54.1", "mosPct updated"),
    ("pwEV: 260.00", "pwEV updated"),
    ("+205%", "+205% Agentforce in CRM section"),
]
for pattern, label in checks:
    if pattern in verify:
        print(f"  [PASS] {label}")
    else:
        print(f"  [FAIL] {label} - not found")

# Syntax check hint
print("\nRun node --check to verify JS syntax:")
print(r'  node --check "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"')
