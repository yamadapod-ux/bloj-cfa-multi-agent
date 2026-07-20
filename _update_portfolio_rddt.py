#!/usr/bin/env python3
"""
Update portfolio.js: add RDDT position + update summary fields.
Uses binary read/write, node --check verification.
"""
import subprocess, sys

path = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\portfolio.js"

with open(path, 'rb') as f:
    raw = f.read()
content = raw.decode('utf-8')

# ------------------------------------------------------------------
# 1. Update summary fields
# ------------------------------------------------------------------
replacements = [
    ('PORTFOLIO_LAST_UPDATED = "2026-05-29 (Price Refresh | CRM +6.44% post-earnings | NOW +37.97%)"',
     'PORTFOLIO_LAST_UPDATED = "2026-05-30 (RDDT T1 Deployed — 3 shares @ $175.94)"'),
    ('currentCash:      7817.07,',  'currentCash:      7289.25,'),
    ('investedValue:    2230.91,',  'investedValue:    2758.73,'),
    ('positionCount:    4,',        'positionCount:    5,'),
    ('cashPct:          77.8,',     'cashPct:          72.55,'),
    ('lastUpdated:      "2026-05-29"',  'lastUpdated:      "2026-05-30"'),
    ('lastTradeAction:  "Price Refresh 2026-05-29 | CRM +6.44% | NOW +37.97% | ADBE +3.49% | GOOGL -1.39%"',
     'lastTradeAction:  "RDDT T1 DEPLOYED 2026-05-30 | 3 shares @ $175.94 | Growth bucket | Conv 6.67 | Morgan QA PASS"'),
    ('macroRegime:      "RISK-ON 4/4 (Atlas 2026-05-21)"',
     'macroRegime:      "RISK-ON 3/4 (Atlas 2026-05-30)"'),
]
for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        print(f"Updated: {old[:60]}")
    else:
        print(f"WARNING not found: {old[:60]}")

# ------------------------------------------------------------------
# 2. Insert RDDT position before positions array closing ],
# ------------------------------------------------------------------
rddt_entry = """    {
      ticker: "RDDT", company: "Reddit, Inc.", sector: "Communication Services / Social Media",
      recommendation: "BUY", conviction: 6.67,
      tranches: [
        { tranche: "T1", entryDate: "2026-05-30", entryPrice: 175.94, shares: 3, costBasis: 527.82, note: "Growth | AI data licensing moat | Revenue +69% | Conv 6.67 | Growth MOS both pass | Morgan QA PASS" },
      ],
      totalShares: 3, avgEntryPrice: 175.94, totalCostBasis: 527.82,
      entryPrice: 175.94, shares: 3, costBasis: 527.82,
      currentPrice: 175.94, marketValue: 527.82, returnPct: 0.0, weightPct: 5.25,
      blendedFV: 169.25, mosPct: -3.8,
      stopLoss: 140.75, stopDistancePct: 20.0,
      entryZone: "T1: $155-178 | T2: $145-160 (pullback or AI licensing $200M+ confirmed)",
      tranche: "T1",
      t2Zone: "$145-160 — after pullback or AI licensing quarterly run-rate $200M+ confirmed",
      thesis: "Social media + AI data licensing dual moat. Revenue +69% Q1 2026. ARPU $5.23 growing 45% YoY vs META $40+. AI licensing Google $60M/yr to $400M/yr potential by 2027. Debt-free $2.77B net cash. ROIC 56.7%. Growth MOS: Reverse DCF 1.03x + 55-60th pct. Bear risk: Meta Forum May 2026 + Google dependency.",
      status: "OPEN", bucket: "Growth", reportFile: "reports/RDDT_2026-05-30.md",
      priceUpdated: "2026-05-30", priceSource: "StockAnalysis.com $175.94 (2026-05-29) + SEC Q1 2026 market cap $33.87B ÷ 192.51M shares = $175.94",
      regime: "RISK-ON 3/4 | Multiplier: 1.0x",
    },
"""

# Find closing of positions array: "  ],\n\n  tradeLog:"
# Find the CRM entry's closing - use CRM-specific priceSource as anchor
anchor = 'priceSource: "StockAnalysis $192.65 + Investing.com $192.88 (2026-05-29)"'
idx = content.find(anchor)
if idx == -1:
    print("ERROR: CRM anchor not found")
    sys.exit(1)
# Find the closing "}," after this anchor (end of CRM block)
close_idx = content.find('\r\n    },\r\n  ],', idx)
if close_idx == -1:
    print("ERROR: CRM closing brace not found")
    sys.exit(1)
# Insert after the "}," (i.e., before the positions array's "]")
insert_after = close_idx + len('\r\n    },')
content = content[:insert_after] + '\n' + rddt_entry + content[insert_after:]
print(f"RDDT inserted at position {idx}")

# ------------------------------------------------------------------
# 3. Write back
# ------------------------------------------------------------------
with open(path, 'wb') as f:
    f.write(content.encode('utf-8'))
print(f"Written: {len(content)} chars")

# ------------------------------------------------------------------
# 4. node --check
# ------------------------------------------------------------------
r = subprocess.run(['node', '--check', path], capture_output=True, text=True)
if r.returncode == 0:
    print("node --check: PASS ✅")
else:
    print(f"node --check: FAIL ❌\n{r.stderr[:500]}")
    sys.exit(1)

print("portfolio.js updated successfully")
