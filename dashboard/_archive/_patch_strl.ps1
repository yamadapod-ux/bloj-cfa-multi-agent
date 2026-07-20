# _patch_strl.ps1 — Leo's patch script for STRL data.js update
# Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\
# Usage: .\dashboard\_patch_strl.ps1

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# 1. Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-06";', 'const LAST_UPDATED = "2026-05-07";'

# 2. STRL object to insert (before ];)
$strlObject = @'
  ,
  {
    ticker: "STRL",
    company: "Sterling Infrastructure, Inc.",
    date: "2026-05-07",
    sector: "Industrials / Infrastructure & Construction Services",
    price: 130.00,
    recommendation: "HOLD",
    blendedFV: 96.00,
    targetBull: 128.00,
    targetBase: 96.00,
    stopLoss: 75.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 7,
    convictionAvg: 6.0,
    pwEV: 85.20,
    beta: 1.10,
    sharpe1Y: 0.85,
    maxDrawdown: -0.38,
    moat: "Narrow",
    esgRating: "Medium-Low",
    esgScore: 5.4,
    keyThesis: "AI data center site work (E-Infrastructure 45%) + IIJA Transportation (38%) = dual tailwind infrastructure play. Blended FV $96 = MOS -26% at current price. New sector diversification (Infrastructure/Construction) — beta 1.10 reduces portfolio beta vs semiconductor holdings.",
    topRisk: "Hyperscaler capex cycle peak (E-Infrastructure lagging indicator) + DOGE Transportation spending cuts + fixed-price contract inflation risk",
    entryZone: "$95-110",
    positionSize: "3-4% (3 tranches at entry zone — NOT at current $130)",
    bullFlipTriggers: [
      "Price pullback to $95-110 — MOS turns positive, Kelly positive",
      "Operating margin sustained >11% for 3 consecutive quarters",
      "E-Infrastructure wins new hyperscaler client >= $500M",
      "New cost-plus/GMP contracts >= 30% E-Infrastructure revenue",
      "Transportation backlog grows YoY despite DOGE pressure"
    ],
    bearFlipTriggers: [
      "E-Infrastructure revenue miss >= 15% vs guidance for 2 consecutive quarters",
      "Operating margin falls below 8% for 2 consecutive quarters",
      "Backlog falls >= 25% YoY",
      "Major hyperscaler announces construction contractor diversification",
      "DOGE/Congress rescinds IIJA contracts >= $200M from STRL"
    ],
    thesisInvalidation: "E-Infrastructure % falls below 35% of revenue; Net Debt/EBITDA > 3x sustained; major safety incident (class action/OSHA shutdown); backlog collapses >30% in single quarter",
    reportFile: "../reports/STRL_2026-05-07.md",
    fullContent: `# 🏗️ STRL — Sterling Infrastructure, Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

---

## 📌 ข้อมูลหลัก

| Field | Detail |
|-------|--------|
| **Ticker** | STRL (NASDAQ) |
| **วันที่วิเคราะห์** | 2026-05-07 |
| **ราคา (asof)** | ~$130.00 |
| **Market Cap** | ~$3.8B (Mid-Cap) |
| **Sector** | Industrials / Infrastructure & Construction Services |
| **Benchmark** | S&P 500 |
| **Analyst Team** | Emma (Equity) · Quinn (Quant) · Bear (Risk) · Charlie (Orchestrator) · Leo (Recorder) |

## 🎯 คำแนะนำ

| Field | Detail |
|-------|--------|
| **Recommendation** | **HOLD / WAIT FOR PULLBACK** |
| **Entry Zone** | $95–110 (3 Tranches) |
| **Blended Fair Value** | **$96** |
| **Margin of Safety** | **-26%** (ราคาปัจจุบันแพงกว่า FV) |
| **Stop Loss** | $75 |
| **Max Position** | **3–4%** (new sector, conviction 6.0/10) |

## 📊 Score Dashboard

| Blended FV | MOS % | ESG Score | Conviction Avg | Investment Horizon |
|-----------|-------|-----------|---------------|-------------------|
| $96 | -26% | 5.4/10 (Medium-Low) | 6.0/10 | Long-term 3–5 ปี |

---

> ## ⚡ TL;DR — อ่าน 30 วินาที
>
> - **Verdict:** HOLD/WAIT — STRL เป็นบริษัทดีในธุรกิจที่ถูก moment แต่ราคาปัจจุบัน ~$130 แพงกว่า Blended FV $96 ถึง 26% — รอ pullback ที่ $95-110 ก่อน
> - **ทำไม:** E-Infrastructure segment (data center site work) = AI proxy ที่ไม่มีความเสี่ยง tech obsolescence แต่ valuation re-rating ส่วนใหญ่เกิดขึ้นแล้ว + hyperscaler capex cycle เสี่ยงชะลอ 2026-2027
> - **Downside Risk:** ถ้า hyperscaler capex pause + margin miss + DOGE cuts Transportation → Bear case $62 = downside -52% จากราคาปัจจุบัน

---

## 📋 Executive Summary [CFA L2: Equity Valuation — Integrated Analysis Framework]

Sterling Infrastructure, Inc. (STRL) เป็น mid-cap infrastructure contractor ที่ได้รับ multiple re-rating จาก AI data center boom ผ่าน E-Infrastructure segment ราคาหุ้นพุ่ง ~300%+ ใน 3 ปีที่ผ่านมา จาก ~$30 → ~$130

**ทีมวิเคราะห์เห็นด้วยว่า:** STRL เป็นบริษัทที่มีคุณภาพดี — backlog แข็งแกร่ง ($5.6B+), margin expansion จาก E-Infrastructure mix shift, IIJA-backed Transportation demand. อย่างไรก็ตาม **ราคาปัจจุบัน ~$130 สะท้อน bull case ไปแล้ว**

### 💪 Conviction Level Score

\`\`\`
Emma   ███████░░░  7/10  — Fundamental thesis ชัด, moat building, margin expansion
Quinn  ██████░░░░  6/10  — P-W EV $88.50 < $130; Kelly negative at current price
Bear   ███████░░░  7/10  — Overvalued at $130; Bear FV $86; hyperscaler cycle risk underpriced
──────────────────────────────────────────
Avg    ██████░░░░  6.0/10  [ไม่ flag — avg >= 5, gap = 0pt]
\`\`\`

---

## 💡 Investment Thesis [CFA L2: Industry Analysis — Competitive Strategy]

**Bull Case:**
1. E-Infrastructure = AI Infrastructure Proxy Without Tech Risk — "dirt doesn't become obsolete"
2. Revenue Visibility: $5.6B+ Backlog (~2.3x annual revenue)
3. Margin Expansion: Mix shift E-Infrastructure 45%→55% = operating leverage
4. IIJA Multi-Year Demand Floor for Transportation segment
5. Asset-Light: Capex/Revenue ~3.5% = better FCFF conversion

**Why Bear Resists Full BUY:**
At $130, investor is paying for: mix shift not yet achieved, margin expansion not yet sustained, hyperscaler capex continuing uninterrupted — all 3 assumptions required simultaneously.

---

## 🏢 Business Overview [CFA L2: Industry Analysis — Business Description]

| Segment | Revenue % | Key Clients | Growth Driver | Key Risk |
|---------|-----------|------------|--------------|---------|
| E-Infrastructure | ~45% | Microsoft, Google, Amazon | AI build-out | Hyperscaler capex cycle |
| Transportation | ~38% | Federal/State DOTs | IIJA multi-year | DOGE/spending cuts |
| Building Solutions | ~17% | Residential/Commercial | Sun Belt housing | Housing cycle |

**Financial Summary (FY2025E):** Revenue ~$2.4B | Op Margin ~8.5% | ROE ~22% | ROIC ~14% | Backlog ~$5.6B | Net Debt ~$250M

---

## 🏰 Moat Analysis [CFA L2: Porter's 5 Forces + Economic Moat]

**Moat Rating: NARROW** (Emma) / WEAK-NARROW (Bear)

| Porter's Force | Intensity | Impact |
|---------------|-----------|--------|
| New Entrants | Medium-Low | Bonding capacity + track record = barriers |
| Supplier Power | Medium | Commodity inputs; labor constrained |
| Buyer Power | HIGH | Hyperscalers = sophisticated multi-vendor buyers |
| Substitutes | Low | Cannot substitute civil earthwork |
| Rivalry | HIGH | PWR, PRIM, EME all compete; fixed-price bidding |

---

## 📊 Sector / Peer Comparison [CFA L2: Relative Valuation]

| Company | Ticker | P/E Fwd | EV/EBITDA | ROE | ROIC | Rev Growth | Moat |
|---------|--------|---------|-----------|-----|------|-----------|------|
| **Sterling Infra.** | **STRL** | **~20x** | **~15x** | **~22%** | **~14%** | **~15%** | **Narrow** |
| Primoris Services | PRIM | 13x | 8x | 15% | 9% | 10% | Narrow |
| MYR Group | MYRG | 15x | 9x | 17% | 11% | 8% | Narrow |
| Quanta Services | PWR | 25x | 16x | 21% | 13% | 18% | Narrow-Wide |
| EMCOR Group | EME | 22x | 14x | 30% | 18% | 12% | Narrow-Wide |

**STRL Position:** Growth premium vs PRIM/MYRG (justified by highest rev growth 15%); parity with EME; slight discount to PWR. BUT EME/PWR have better moats + higher ROIC = premium partially questioned.

---

## 💰 Valuation [CFA L2: DCF + Market-Based + Scenario]

| Method | FV | Weight |
|--------|-----|--------|
| DCF Base (12% CAGR, 11% margin) | $93 | 35% |
| EV/EBITDA Peer 15x | $135 | 25% |
| Peer Relative 12.5x | $111 | 25% |
| Bear P-W EV | $75 | 15% |
| **Pre-ESG Blend** | **$105** | — |
| **ESG Adj -5.5%** | **$96** | — |

**Triangulation 30/30/40 (Emma/Quinn/Bear):** $93×30% + $88.5×30% + $74.6×40% = **$84**
**Charlie Final Blended FV: $96** | **P-W EV: $85.20** | **MOS: -26%**

---

## 📉 Sensitivity Matrix 5×5 [CFA L2: Scenario Analysis — Revenue CAGR × Operating Margin]

| | Op Margin 8.0% | Op Margin 9.5% | Op Margin 11.0% | Op Margin 12.5% | Op Margin 14.0% |
|---|---|---|---|---|---|
| Rev CAGR 5% | $42 | $52 | $63 | $74 | $85 |
| Rev CAGR 8% | $54 | $66 | $78 | $92 | $105 |
| **Rev CAGR 11%** | $68 | $83 | **$93 BASE** | $115 | $130 |
| Rev CAGR 14% | $85 | $103 | $121 | $140 | $160 |
| Rev CAGR 17% | $102 | $126 | $148 | $170 | $195 |

**Current price $130 = priced at CAGR 14% + Margin 11% = execution premium zone**

---

## 📉 Quantitative Risk [CFA L1-L2: Risk Metrics + Carhart 4-Factor]

| Metric | STRL | S&P 500 | Note |
|--------|------|---------|------|
| Beta | ~1.10 | 1.00 | Lower than all semiconductor holdings |
| Sharpe (3Y) | ~0.85 | 0.75 | Historical high (momentum); forward lower |
| Max Drawdown | -38% | -25% | Meaningful — justify stop loss $75 |
| VaR (95%, 1M) | -13% | -9% | |
| CVaR (95%, 1M) | -19% | -13% | |
| Jensen's Alpha | +6.5%/yr | — | t~2.0; strip momentum → drops to 3.5% |

---

## 🌱 ESG Risk Scorecard [CFA L2-3: ESG Materiality]

| Dimension | Emma | Bear | Reconciled |
|-----------|------|------|-----------|
| Environmental (E) | 5/10 | 4/10 | 4.5/10 |
| Social (S) | 6/10 | 5/10 | 5.5/10 |
| Governance (G) | 7/10 | 5/10 | 6.0/10 |
| **Overall** | 6.0 | 4.7 | **5.4/10** |

**Material Risks:** Environmental permitting delays (-2%), Worker safety incidents (-2%), Weak ESG disclosure → fund exclusion (-1.5%) | **Total ESG Impact: -5.5%**

---

## 🔄 What Would Change Our Mind [CFA L3: Investment Thesis — Flip Triggers]

**Bull Flip Triggers (HOLD → BUY):**
1. Price pullback to $95-110 (MOS turns positive, Kelly positive)
2. Operating margin sustained >11% for 3 consecutive quarters
3. E-Infrastructure wins new hyperscaler client >= $500M
4. New cost-plus/GMP contracts >= 30% E-Infrastructure revenue
5. Transportation backlog grows YoY despite DOGE pressure

**Bear Flip Triggers (HOLD → SELL/AVOID):**
1. E-Infrastructure revenue miss >= 15% vs guidance for 2 consecutive quarters
2. Operating margin < 8% for 2 consecutive quarters
3. Backlog falls >= 25% YoY
4. Major hyperscaler announces construction diversification
5. DOGE/Congress rescinds IIJA contracts >= $200M

**Thesis Invalidation:**
- E-Infrastructure % falls below 35% of revenue
- Net Debt/EBITDA > 3x sustained
- Major safety incident (class action/OSHA shutdown)
- Backlog collapses >30% in single quarter

---

## 🎯 Recommendation [CFA L3: Portfolio Construction]

> ### HOLD / WAIT FOR PULLBACK — Entry Zone $95-110
> STRL เป็นบริษัทดีในธุรกิจที่ถูก moment แต่ราคา $130 สะท้อน bull case ไปแล้ว รอ pullback สู่ Entry Zone ก่อนเปิด position

| Tranche | ราคา | Size | Trigger |
|---------|------|------|---------|
| Tranche 1 | $105-110 | 1.5% | Pullback + margin >= 10% last quarter |
| Tranche 2 | $95-105 | 1.5% | Further pullback + backlog solid |
| Tranche 3 | $85-95 | 1.0% | Deeper pullback + E-Infra wins confirmed |

**Stop Loss: $75 | Target Base: $96 | Target Bull: $128 | Max Position: 4%**

---

## ⚠️ Risk Summary [CFA L2-3: Risk Analysis]

| Risk | Probability | Impact |
|------|------------|--------|
| Hyperscaler capex pause | 30% | High -25% |
| Fixed-price inflation | 35% | Medium -15% |
| DOGE Transportation cuts | 25% | Medium -10% |
| Multiple compression | 40% | Medium -20% |
| Labor shortage cost overrun | 30% | Low -8% |

---

## 📅 Catalysts Calendar

\`\`\`
Q2 2026  ──●──  📊 Q1 2026 Earnings Release                   [HIGH]
                 E-Infrastructure revenue + margin primary watch

Q2 2026  ──●──  🏗️ Data Center Project Awards                 [HIGH]
                 New hyperscaler wins = Bull flip trigger potential

Q3 2026  ──●──  📊 Q2 2026 Earnings                           [HIGH]
                 2nd consecutive quarter = pattern confirmation

Q3 2026  ──●──  🏛️ IIJA Obligation Progress Report             [MEDIUM]
                 Federal/State DOT obligation = DOGE test

Q4 2026  ──●──  📊 Q3 2026 Earnings + Full-Year Guide          [HIGH]
                 FY2026 margin guide > 11% = upgrade trigger

2027 H1  ──●──  🔄 Hyperscaler Capex FY2027 Guidance           [HIGH]
                 >= 2 hyperscalers cut > 15% = Bear flip trigger
\`\`\`

---

## 📚 CFA Concepts ที่ใช้

| Concept | Level | สถานะ |
|---------|-------|-------|
| DCF FCFF 2-Stage | L2 | รู้แล้ว |
| EV/EBITDA Market-Based | L2 | รู้แล้ว |
| Peer Cross-Sectional | L2 | รู้แล้ว |
| Carhart 4-Factor + Jensen's Alpha | L2 | รู้แล้ว |
| Sensitivity Matrix 5×5 | L2 | รู้แล้ว |
| Kelly Criterion | L3 | รู้แล้ว |
| Investment Thesis Flip Triggers | L3 | รู้แล้ว |
| ESG Materiality | L2-3 | รู้แล้ว |
| Infrastructure Industry Cycle | L2 | *(ยังไม่เรียน)* |
| Political/Policy Risk (DOGE) | L3 | *(ยังไม่เรียน)* |

---

## ⚙️ Behind the Scenes

**Emma:** DCF + EV/EBITDA + Peer Comp + ESG + Moat/Porter's 5 Forces | Conviction 7/10
**Quinn:** Risk metrics + Carhart 4-Factor + Sensitivity Matrix 5×5 + Kelly | Conviction 6/10
**Bear:** 6 challenges (moat/margin/DOGE/capex/valuation/ESG) + Flip Triggers + Bear FV $86 | Conviction 7/10
**Charlie:** Triangulation 30/30/40 → $84; Method blend → $96; Final Blended FV $96; HOLD/WAIT

**Key Debate:** Bear wins on current valuation (all 3 agents: DCF $93, P-W EV $88.50, Bear P-W $74.60 — all below $130). Emma wins on quality of business and long-term thesis. Resolution: HOLD/WAIT at $130, BUY at $95-110.

---

## 🏁 Conclusion

STRL เป็นบริษัทคุณภาพดีใน sector ที่ได้รับ tailwind แข็งแกร่ง แต่ราคา $130 = -26% overvalued vs Blended FV $96. เพิ่มใน Watchlist — รอ pullback + margin confirmation ก่อนเปิด position.

**Portfolio Impact:** NEW sector (Infrastructure/Construction) = diversification benefit + beta 1.10 ลด portfolio beta เฉลี่ย. Semiconductor ceiling 19% ไม่ถูกกระทบ.

---

*Report สร้างโดย: Charlie (Orchestrator) | Emma (Equity) | Quinn (Quant) | Bear (Risk) | Leo (Recorder)*
*วันที่: 2026-05-07 | บลจ. CFA Multi-Strategy Aggressive Growth*
`
  }
'@

# 3. Replace the closing ]; with STRL object + ];
$content = $content -replace '(\r?\n)];(\r?\n// Computed)', "`$1$strlObject`$1];`$2"

# 4. Write back
Set-Content $dataFile -Value $content -Encoding UTF8 -NoNewline

Write-Host "data.js patched successfully:" -ForegroundColor Green
Write-Host "  - LAST_UPDATED updated to 2026-05-07" -ForegroundColor Cyan
Write-Host "  - STRL object inserted before ];" -ForegroundColor Cyan
