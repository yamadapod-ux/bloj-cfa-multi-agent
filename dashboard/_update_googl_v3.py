"""
Leo Python Script — Update GOOGL entry in dashboard/data.js (v3 Re-Analysis 2026-05-21)
Dashboard Write Safety Rule: Use Python, not Write tool (avoids newline collapse)
"""
import re, os

DATA_JS = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"

with open(DATA_JS, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update LAST_UPDATED
content = re.sub(
    r'const LAST_UPDATED = "[^"]+";',
    'const LAST_UPDATED = "2026-05-21";',
    content
)

# 2. Build new GOOGL object string
new_googl_block = r"""  {
    ticker: "GOOGL",
    company: "Alphabet Inc. Class A",
    date: "2026-05-21",
    version: "v3 (Re-Analysis)",
    sector: "Communication Services / Technology",
    price: 165.44,
    recommendation: "HOLD/WAIT",
    blendedFV: 173.00,
    esgAdjFV: 164.00,
    targetBull: 215.00,
    targetBase: 173.00,
    stopLoss: 132.00,
    convictionEmma: 7.0,
    convictionQuinn: 6.5,
    convictionBear: 6.5,
    convictionAvg: 6.67,
    mosPct: 4.6,
    pwEV: 180.00,
    beta: 1.07,
    sharpe1Y: -0.02,
    maxDrawdown: -0.45,
    moat: "Wide",
    esgRating: "Medium-High",
    esgScore: 5.0,
    convictionGatePassed: true,
    regimeBlock: "TRANSITIONAL-CAUTIOUS",
    macroRegime: "TRANSITIONAL-CAUTIOUS",
    sp500Reference: 5850,
    keyThesis: "Cheapest quality mega-cap — conviction gate PASSED (6.67 >= 6.5). Q1 2026 op margin 34.4% (+470bps) structural. AI Overviews not hurting Search. GCP run rate $49B. Deploy T1 6% when RISK-ON.",
    topRisk: "DOJ structural separation (-30-50% FV) + CapEx $75-85B FY2026 FCF compression (Bear NEW v3) + AI Search substitution",
    entryZone: "$140-155 or DOJ behavioral ruling + price <= $175",
    positionSize: "6% (Conv 6.67% x 1.0 RISK-ON) -- TC regime suspends currently",
    ratingChangeNote: "v2 (2026-05-20) Conviction 6.33 NOT MET gate -> v3 (2026-05-21) Conviction 6.67 GATE PASSED",
    bullFlipTriggers: [
      "DOJ final remedy = behavioral only -> FV re-rates $200+; BUY immediately",
      "GCP market share >= 14% global in Q2 2026 -> Cloud acceleration confirmed",
      "Search revenue +12%+ YoY in Q2 2026 -> AI Overviews definitively OK",
      "CapEx guidance revised $60-65B -> FCF upgrade; Bear challenge resolved",
      "Price <= $140 + no new negative catalyst -> Kelly positive; all signals align"
    ],
    bearFlipTriggers: [
      "DOJ structural separation (Chrome/Android) -> SELL immediately; FV $75-90",
      "Search share < 88% in 2 consecutive reports -> AI substitution confirmed",
      "GCP growth < 15% YoY in Q2/Q3 2026 -> Cloud disappointing",
      "CapEx > $85B FY2026 + no FCF recovery guidance -> capital spiral",
      "Apple deal terminated -> Search revenue -10-15% structural headwind"
    ],
    thesisInvalidation: "Chrome/Android forced divestiture OR Search share < 80% rolling 12M OR 3 consecutive quarters Search revenue YoY decline",
    businessSummary: {
      oneLiner: "Alphabet คือเจ้าของ Google Search, YouTube, และ Google Cloud -- บริษัทโฆษณาดิจิทัลและ cloud ที่ใหญ่ที่สุดในโลก",
      analogy: "เหมือนเป็นเจ้าของทางด่วนทุกเส้นบนอินเทอร์เน็ต -- ใครก็ตามที่ต้องการพาคนไปที่ไหนต้องจ่ายเงินผ่าน Google",
      moneyFlow: [
        "ผู้ใช้ค้นหาสิ่งต้องการบน Google (2 ล้านล้านครั้ง/ปี)",
        "ผู้ลงโฆษณาจ่ายเงินเพื่อให้โฆษณาปรากฏข้างผลการค้นหา (Cost-per-Click)",
        "GCP ให้บริษัทต่างๆ เช่า cloud + AI infrastructure แบบ subscription ($49B annualized run rate)",
        "YouTube Ads บน 2.7B+ MAU + Subscriptions (Google One, YouTube Premium)"
      ],
      whyDifferent: "25 ปีของข้อมูลการค้นหา + Android 3B devices + network effect = ecosystem ที่คู่แข่งไม่สามารถ replicate; AI Overviews Q1 2026 ไม่กระทบ Search revenue",
      simpleRisk: "DOJ บังคับแยกบริษัท หรือ CapEx $75-85B FY2026 ทำให้ FCF ต่ำกว่า risk-free rate"
    },
    thesisBullets: [
      { title: "Search Monopoly ยังแข็ง", why: "90%+ global share; AI Overviews Q1 2026 ไม่กระทบ Search +9.8% YoY -- worry หลักไม่เป็นจริงใน Q1" },
      { title: "GCP = Next Revenue Engine", why: "Q1 2026 $12.3B +28.1% YoY; run rate $49B annualized; margin expanding 9%->17%+; path to #2 cloud" },
      { title: "Operating Margin Expansion (NEW)", why: "Q1 2026: 34.4% (+470bps YoY) = structural improvement; GCP scale leverage + cost efficiency" },
      { title: "Valuation Discount ผิดปกติ", why: "P/E ~18x = 22-25% discount vs peers (META ~19x, MSFT ~28x); ROIC 26% > sector median" },
      { title: "Capital Return Machine", why: "$62.5B buyback FY2024; net cash $98-103B; no leverage = fortress balance sheet" }
    ],
    esgBreakdown: { e: 7, s: 4.5, g: 3.25, overall: 5.0 },
    customerConcentration: {
      noSingleCustomerAbove1pct: "<1% each -- millions of advertisers worldwide",
      appleDistributionDeal: "~$20B/yr cost item (TAC); DOJ target -- not a customer"
    },
    geographyRevenue: {
      unitedStates: "~47%",
      emea: "~29% (DXY weak = FX tailwind)",
      apac: "~17%",
      otherAmericas: "~7%",
      chinaDirectExposure: "~<3% -- low vs QCOM/AMD"
    },
    revenueSegments: [
      { label: "Search & Other", value: 57 },
      { label: "YouTube Ads", value: 10 },
      { label: "Google Cloud (GCP)", value: 14 },
      { label: "Google Network", value: 9 },
      { label: "Subscriptions/Devices/Other", value: 10 }
    ],
    competitorData: [
      { ticker: "GOOGL", company: "Alphabet", revenueGrowth: 12.1, operatingMargin: 34.4, marketCap: 2010 },
      { ticker: "META", company: "Meta Platforms", revenueGrowth: 33, operatingMargin: 41, marketCap: 1550 },
      { ticker: "MSFT", company: "Microsoft", revenueGrowth: 17, operatingMargin: 45, marketCap: 3200 },
      { ticker: "AMZN", company: "Amazon", revenueGrowth: 11, operatingMargin: 11, marketCap: 2100 }
    ],
    reportFile: "../reports/GOOGL_2026-05-20.md",
    fullContent: `# GOOGL v3 -- Alphabet Inc. Class A
### Re-Analysis 2026-05-21 | บลจ. CFA Multi-Strategy Aggressive Growth

## Key Changes v3 (from v2 2026-05-20)
- Conviction: 6.33 -> **6.67** (Growth gate 6.5 PASSED)
- Blended FV: $170 -> **$173** (+$3)
- MOS: +2.7% -> **+4.6%** (+1.9pp)
- Emma FV: $175 -> $178 | Quinn FV: $177 -> $180 | Bear FV: $157 -> $155
- NEW Bear Risk: CapEx guidance $75-85B FY2026 (vs $52.5B FY2024) = FCF compression

## Recommendation: HOLD/WAIT (TC Regime) -- Conviction Gate PASSED

| Metric | Value |
|--------|-------|
| Blended FV | **$173** (Emma $178x40% + Quinn $180x35% + Bear $155x25%) |
| MOS | +4.6% |
| Stop Loss | $132 (-20% from entry $165.44) |
| Conviction | 6.67/10 -- gate PASSED (>= 6.5 Growth) |
| Regime | TRANSITIONAL-CAUTIOUS -- suspend new positions |
| Deploy when | Regime RISK-ON -> 6% T1 | DOJ behavioral -> 6-7% | Price <= $140 -> BUY |

## Why HOLD not BUY
1. TC regime prohibits new positions (despite conviction gate passing)
2. Forward Sharpe still marginally negative at $165.44
3. CapEx $75-85B FY2026 = FCF compression risk (Bear) -- needs Q2 2026 confirmation

## Key Catalysts
- DOJ Remedy Order Q3-Q4 2026: CRITICAL -- behavioral = BUY; structural = SELL
- Q2 2026 Earnings (Aug): Search revenue trend + CapEx actual vs guidance
- Macro Regime: If RISK-ON -> auto-deploy 6%

*Full report: reports/GOOGL_2026-05-20.md (updated in-place, v3 section at top)*
`
  },"""

# 3. Find the GOOGL block using a multi-line pattern
# Look for ticker: "GOOGL" and find the block start/end
lines = content.split('\n')
start_line = None
brace_count = 0
end_line = None

for i, line in enumerate(lines):
    if start_line is None and 'ticker: "GOOGL"' in line:
        # Find the opening brace -- go backwards from this line
        for j in range(i, max(i-5, 0), -1):
            if '{' in lines[j]:
                start_line = j
                break
        if start_line is None:
            start_line = i - 1
        brace_count = 0
        # Count braces from start
        for k in range(start_line, len(lines)):
            brace_count += lines[k].count('{') - lines[k].count('}')
            if brace_count == 0 and k > start_line:
                end_line = k
                break
        break

if start_line is not None and end_line is not None:
    # Check if there's a trailing comma
    if end_line + 1 < len(lines) and lines[end_line].rstrip().endswith(','):
        pass  # comma already in the block end line
    # Rebuild content
    new_lines = lines[:start_line] + [new_googl_block] + lines[end_line+1:]
    new_content = '\n'.join(new_lines)
    with open(DATA_JS, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"SUCCESS: GOOGL block replaced (lines {start_line}-{end_line})")
    print(f"File size after: {os.path.getsize(DATA_JS):,} bytes")
else:
    print(f"ERROR: GOOGL block not found (start={start_line}, end={end_line})")
    print("Attempting simple string replacement...")
    # Fallback: just update LAST_UPDATED (already done) and print warning
    with open(DATA_JS, 'w', encoding='utf-8') as f:
        f.write(content)
    print("LAST_UPDATED updated; GOOGL block needs manual update")
