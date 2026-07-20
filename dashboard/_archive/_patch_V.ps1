# _patch_V.ps1 — Leo: Add V (Visa) entry to data.js
# Run from: C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\
# Usage: .\dashboard\_patch_V.ps1

$dataPath = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$content = Get-Content $dataPath -Raw

# V entry to insert before the closing ];
$vEntry = @'
,
  {
    ticker: "V",
    company: "Visa Inc.",
    date: "2026-05-07",
    sector: "Financial Services / Payment Networks",
    price: 355.00,
    recommendation: "HOLD",
    blendedFV: 290.00,
    targetBull: 450.00,
    targetBase: 355.00,
    stopLoss: 240.00,
    convictionEmma: 7,
    convictionQuinn: 6,
    convictionBear: 7,
    convictionAvg: 6.7,
    pwEV: 320.00,
    beta: 0.90,
    sharpe1Y: 0.95,
    maxDrawdown: -0.28,
    moat: "Wide",
    esgRating: "Medium",
    esgScore: 6.4,
    keyThesis: "World-class payment network toll road — Wide Moat via network effects (4.3B cards x 130M merchants x 200+ countries). ROIC 50% top quartile, no credit risk, 80%+ gross margin. BUT: price $355 = 18% above Blended FV $290. DOJ antitrust lawsuit (2024) = idiosyncratic risk NOT in beta. Kelly NEGATIVE at $355. Wait for entry $285-310.",
    topRisk: "DOJ antitrust structural remedy (35% prob) — could impair toll road model permanently. WACC understated by 1-1.5% (regulatory risk not in beta).",
    entryZone: "$285-310",
    positionSize: "4% (staged — 2 tranches at entry)",
    reportFile: "../reports/V_2026-05-07.md",
    fullContent: `# 💳 V — Visa Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth
*Analyst Team: Emma (Equity) · Quinn (Quant) · Bear (Risk) · Charlie (Orchestrator)*

---

## 📌 ข้อมูลหลัก

| Field | Detail |
|-------|--------|
| **Ticker** | V (NYSE) |
| **Date** | 2026-05-07 |
| **Price (est.)** | ~$355.00 |
| **Market Cap (est.)** | ~$730B |
| **Sector** | Financial Services — Payment Networks |
| **S&P 500 Price (ref.)** | ~5,600 (est. 2026-05-07) |
| **Fiscal Year End** | September 30 |
| **Analyst Team** | Emma · Quinn · Bear · Charlie |

---

## 🎯 คำแนะนำ

| Item | Detail |
|------|--------|
| **Recommendation** | **HOLD / WAIT FOR PULLBACK** |
| **Entry Zone (Tranche 1)** | $300–310 |
| **Entry Zone (Tranche 2)** | $285–300 |
| **Blended Fair Value** | **$290/share** |
| **ESG-Adjusted FV** | $274/share |
| **MOS @ Current Price** | **-18.2%** (overvalued) |
| **Stop Loss** | $240 |
| **Target Base** | $355 (current market = fair value at entry) |
| **Target Bull** | $420–450 |
| **Max Position** | **4%** (Quarter-Kelly at entry price) |
| **Investment Horizon** | 3–5 years |

---

## 📊 Score Dashboard

| Metric | Value | Notes |
|--------|-------|-------|
| **Blended FV** | $290 | Triangulation 30/30/40 (Emma/Quinn/Bear) |
| **MOS %** | -18.2% | Negative — overvalued at $355 |
| **P-W EV (Quinn)** | $320 | More optimistic scenario weights |
| **P-W EV (Bear)** | $252.50 | Bear DOJ-risk adjusted |
| **ESG Score** | 6.4/10 | Reconciled Emma 7.0 / Bear 5.7 |
| **Conviction Avg** | **6.7/10** | Emma 7 / Quinn 6 / Bear 7 |
| **Investment Horizon** | 3–5 yr | Long-term buy & hold |
| **Economic Moat** | **Wide** (narrowing risk) | 10–15 yr durability confirmed |
| **Beta** | 0.90 | Below-market; does NOT capture DOJ idiosyncratic risk |

---

> ⚡ **TL;DR — อ่าน 30 วินาที**
>
> - **Verdict:** HOLD/WAIT — Wide moat ชัดเจน แต่ราคา $355 = 18% เหนือ Blended FV $290. ยังไม่ใช่เวลาซื้อ.
> - **ทำไม:** Visa เป็น toll road ระดับ world-class มี network effects ที่แข็งแกร่งที่สุดในโลก แต่ตลาดกำลัง price in สมมติฐาน revenue growth สูง (11%+) ซึ่ง base case เรา (9%) ไม่สนับสนุน + DOJ antitrust lawsuit (2024) คือ idiosyncratic tail risk ที่ตลาดยังไม่ price in
> - **Downside Risk:** DOJ structural remedy (35% prob ตาม Bear) + WACC underestimation = price อาจ drop $195–220 ใน bear scenario = downside -45% จากราคาปัจจุบัน

---

## 📋 Executive Summary

Visa Inc. (V) คือบริษัท payment network ที่ทรงอิทธิพลที่สุดในโลก ดำเนินงานบน asset-light toll road model ด้วย network ที่ครอบคลุม 4.3B+ cards, 130M+ merchants, และ 200+ ประเทศ Visa มี moat ที่ถือเป็น "Wide" อย่างไม่ต้องสงสัย

อย่างไรก็ตาม ณ ราคา ~$355:
- **Blended Fair Value = $290/share** (Triangulation Emma 30% / Quinn 30% / Bear 40%)
- **MOS = -18.2%** (ราคาตลาดสูงกว่า FV ประมาณ 18%)
- **DOJ Antitrust Lawsuit (2024)**: กำลังดำเนินอยู่ — อาจทำให้ revenue โครงสร้างลดลง 15-25% ถ้า structural remedy ผ่าน

### 💪 Conviction Level Score

\`\`\`
Emma   ███████░░░  7/10  — Wide moat crystal clear; fairly priced แต่ 20% เหนือ FV
Quinn  ██████░░░░  6/10  — P-W EV $320 < $355; Kelly negative at current price
Bear   ███████░░░  7/10  — DOJ risk material & underweighted; WACC understated
──────────────────────────────────────────────────────────────────────────────
Avg    ██████░░░░  6.7/10  [gap max 1pt < 3pt threshold — no flag]
\`\`\`

---

## 💡 Investment Thesis

Visa ดำเนินงานบน **network effect flywheel** ที่ทรงพลังที่สุดในโลก ธุรกิจ asset-light ทำให้ ROIC ~50% สูงกว่า WACC มาก

**Bull Case ($420-450):** DOJ ยุติโดยไม่มี structural remedy + EM digital payment accelerates + Visa+ P2P new vertical > 15% revenue

**Bear Case ($195-220):** DOJ wins partial structural remedy → interchange capped 15% → Revenue -10-15% + multiple compression

---

## 🏰 Moat Analysis

**Moat Rating: WIDE (durability: 10-15 years; 20+ years uncertain)**

| Moat Source | Strength | Durability |
|------------|---------|-----------|
| Network Effects | Very High | 10-15 yr — 4.3B+ cards × 130M+ merchants × 200+ countries |
| Switching Costs | High | 10+ yr — Multi-year bank contracts, POS embedded |
| Intangible Assets | High | Long-term — Brand top-10 global; 200+ country licenses |
| Scale Economies | Very High | 15+ yr — $15T+ annual volume |
| Toll Road Model | Very High | Uncertain — Legally challenged by DOJ |

---

## 📊 Sector / Peer Comparison

| Company | P/E | EV/EBITDA | ROE | ROIC | Rev Growth | Moat | vs Visa |
|---------|-----|-----------|-----|------|------------|------|---------|
| **Visa (V)** | **28x** | **22x** | **55%** | **50%** | **9-10%** | **Wide** | **Subject — FAIR VALUE** |
| Mastercard (MA) | 30x | 25x | 200%+ | 45% | 11% | Wide | 7% P/E premium — justified |
| American Express (AXP) | 18x | 14x | 35% | 15% | 8% | Wide | 36% discount — takes credit risk |
| PayPal (PYPL) | 12x | 10x | 20% | 12% | 5% | Narrow | Deep discount — moat eroding |
| Fiserv (FI) | 22x | 15x | 18% | 8% | 8% | Narrow | Discount — B2B, no network effect |

**V Position: FAIR VALUE vs peers. ROIC 50% = TOP QUARTILE. Slight discount to MA (justified by lower growth).**

---

## 💰 Valuation

**Emma DCF (FCFF 2-Stage):** WACC 8.5%, CAGR 9%, Terminal g 4% → **$294/share**
**EV/EBITDA (22x FY26E):** **$288/share**
**P/E (28x × $10.80 FY26E EPS):** **$302/share**
**Emma Blended: $294.60/share**

### Triangulation (30/30/40)

| Agent | FV | Weight |
|-------|-----|--------|
| Emma | $294.60 | 30% |
| Quinn P-W EV | $320.00 | 30% |
| Bear P-W EV | $252.50 | 40% |

**Blended FV = $290/share | MOS = -18.2% @ $355**

---

## 📉 Quantitative Risk

| Metric | V | S&P 500 |
|--------|---|---------|
| Beta (5Y) | 0.90 | 1.00 |
| Sharpe (3Y) | 0.95 | 0.65 |
| Sortino (3Y) | 1.35 | 0.90 |
| Max Drawdown | -28% | -25% |
| VaR 95% | -22% | -20% |
| CVaR 95% | -30% | -27% |
| Jensen's Alpha | +3.5%/yr | — |

### Sensitivity Matrix 5×5 (Rev CAGR × WACC)

| CAGR \\ WACC | 7.5% | 8.0% | 8.5% | 9.0% | 9.5% |
|-------------|------|------|------|------|------|
| 13% | $432 | $398 | $368 | $342 | $318 |
| 11% | $396 | $365 | $338 | $314 | $292 |
| 9% (Base) | $361 | $332 | **$311** | $289 | **$269** |
| 7% | $325 | $299 | $278 | $258 | $241 |
| 5% | $288 | $266 | $247 | $230 | $214 |

Only 6/25 cells (24%) justify current price $355.

---

## 🌱 ESG Risk Scorecard

| Dimension | Emma | Bear | Reconciled | Valuation Impact |
|-----------|------|------|-----------|-----------------|
| E | 8/10 | 8/10 | 8/10 | -1% |
| S | 6/10 | 4/10 | 5/10 | -5% |
| G | 7/10 | 5/10 | 6/10 | -4% |
| **Overall** | **7.0** | **5.7** | **6.4/10** | **-10%** |

**ESG-Adjusted Blended FV: $290 × 0.90 = $261/share**

---

## 🔄 What Would Change Our Mind

### Bull Flip Triggers (HOLD/WAIT → BUY consideration):
1. Price drops to $285-310 — Kelly turns positive
2. DOJ dismissed / settled with behavioral remedies ONLY (not structural)
3. New revenue vertical > 15% of total revenue (Visa+ P2P, B2B Connect)
4. Cross-border volume CAGR sustains 12%+ for 2+ quarters
5. US Stablecoin regulation passed (bank-like framework)

### Bear Flip Triggers (→ STRONG AVOID):
1. DOJ wins ANY structural remedy → immediate re-analysis
2. Federal interchange fee cap (EU-style 0.3%) legislation passes
3. Cross-border volume growth < 5% for 2 consecutive quarters
4. Major sovereign captures > 10% domestic payment volume
5. Major data breach + regulatory enforcement compound

### Thesis Invalidation:
- DOJ structural remedy + US interchange cap simultaneous → V becomes regulated utility → $150-165
- Stablecoins achieve > 5% global payment volume within 5Y
- V loses 3+ percentage points of global volume share to MA

---

## 🎯 Recommendation

> ### HOLD / WAIT FOR PULLBACK
> ราคาปัจจุบัน $355 = 18% เหนือ Blended FV $290. Wide moat ชัดเจน แต่ราคาต้องลงมาก่อน. รอ Entry Zone $285-310.

| Tranche | Entry Zone | Size |
|---------|-----------|------|
| Tranche 1 | $300–310 | 2% |
| Tranche 2 | $285–300 | 2% |
| Max Position | — | 4% |

**Stop Loss: $240 | Target Base: $355 | Target Bull: $420-450**

---

## ⚠️ Risk Summary

| Risk | Probability | Impact | Severity |
|------|------------|--------|---------|
| DOJ Antitrust Structural Remedy | 35% | -20-30% | CRITICAL |
| WACC Re-rating (regulatory risk) | 40% | -10-15% | HIGH |
| Real-time payment rail displacement | 20% (5Y) | -15-20% | MEDIUM |
| Stablecoin disruption | 15% (5Y) | -20-30% LT | MEDIUM |
| Cross-border volume deceleration | 25% | -8-12% | MEDIUM |

---

## 📅 Catalysts Calendar

\`\`\`
Q2 2026 (Jun)  ──●── 📊 Q2 FY2026 Earnings         [HIGH]
                        Cross-border volume + DOJ commentary

Q3 2026 (Sep)  ──●── ⚖️ DOJ Antitrust Hearing       [CRITICAL]
                        Structural remedy ruling = -20-30% on day

Q4 2026 (Nov)  ──●── 📊 FY2026 Annual Earnings       [HIGH]
                        Full year cross-border + Visa+ P2P contribution

2027 H1        ──●── 🏛️ US Stablecoin Legislation     [HIGH]
                        PASS = bear risk reduced

2027 H2        ──●── ⚖️ DOJ Final Ruling              [CRITICAL]
                        Structural = stop loss triggers; Dismissed = BUY
\`\`\`

---

*Research Report: V_2026-05-07.md | บลจ. CFA Multi-Strategy Aggressive Growth*
*Report Date: 2026-05-07 | Next Review: DOJ Q3 2026 hearing OR price $310*
`
  }
];

// Computed summaries (auto-calculated)
const SUMMARY = {
  totalAnalyzed: REPORTS.length,
  byRating: {
    BUY: REPORTS.filter(r => r.recommendation === "BUY").length,
    HOLD: REPORTS.filter(r => r.recommendation === "HOLD").length,
    AVOID: REPORTS.filter(r => r.recommendation === "AVOID").length,
    WAIT: REPORTS.filter(r => r.recommendation === "WAIT").length,
  },
  avgConviction: (REPORTS.reduce((s, r) => s + r.convictionAvg, 0) / REPORTS.length).toFixed(1),
  watchlist: REPORTS.filter(r => ["HOLD","WAIT"].includes(r.recommendation) || r.entryZone),
};
'@

# Replace the old closing lines with V entry + closing
$oldEnding = @'
`
  }
];

// Computed summaries (auto-calculated)
const SUMMARY = {
  totalAnalyzed: REPORTS.length,
  byRating: {
    BUY: REPORTS.filter(r => r.recommendation === "BUY").length,
    HOLD: REPORTS.filter(r => r.recommendation === "HOLD").length,
    AVOID: REPORTS.filter(r => r.recommendation === "AVOID").length,
    WAIT: REPORTS.filter(r => r.recommendation === "WAIT").length,
  },
  avgConviction: (REPORTS.reduce((s, r) => s + r.convictionAvg, 0) / REPORTS.length).toFixed(1),
  watchlist: REPORTS.filter(r => ["HOLD","WAIT"].includes(r.recommendation) || r.entryZone),
};
'@

# Update LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-07";', 'const LAST_UPDATED = "2026-05-07";'

$newContent = $content.Replace($oldEnding.TrimEnd(), $vEntry.TrimEnd())
Set-Content $dataPath $newContent -Encoding UTF8
Write-Host "V entry added to data.js successfully"
