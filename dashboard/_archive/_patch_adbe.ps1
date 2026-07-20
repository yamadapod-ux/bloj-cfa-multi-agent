# Patch script: เพิ่ม ADBE entry ใน dashboard/data.js
# Run: cd "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard" ; .\..\_patch_adbe.ps1

$dataFile = "C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\data.js"
$content = Get-Content $dataFile -Raw -Encoding UTF8

# อัปเดต LAST_UPDATED
$content = $content -replace 'const LAST_UPDATED = "2026-05-07"', 'const LAST_UPDATED = "2026-05-09"'

# ADBE entry ที่จะเพิ่ม (ก่อน ];)
$adbeEntry = @'
  ,
  {
    ticker: "ADBE",
    company: "Adobe Inc.",
    date: "2026-05-09",
    sector: "Technology / Creative & Marketing Software (SaaS)",
    price: 253.00,
    recommendation: "BUY",
    blendedFV: 311.70,
    targetBull: 465.00,
    targetBase: 311.00,
    stopLoss: 185.00,
    convictionEmma: 8,
    convictionQuinn: 7,
    convictionBear: 7,
    convictionAvg: 7.3,
    pwEV: 316.00,
    beta: 1.25,
    sharpe1Y: 0.70,
    maxDrawdown: -0.56,
    moat: "Wide",
    esgRating: "Low-Medium",
    esgScore: 7.2,
    keyThesis: "Wide Moat Creative Software leader — P/E 12.3x vs peer median 30x = 59% discount; FCF Margin 42%; ROE 58.8%; Firefly AI = new revenue layer (not replacement); $25B buyback; MOS +23.2%; Kelly 28-31% positive",
    topRisk: "AI disruption (Canva 220M users; Bear FCF growth 8% not 12% → FV ~$255 near current price); SBC-adj FCF $7.5B not $9.0B; Firefly revenue = thesis invalidation watch",
    entryZone: "T1: $240-260 / T2: $215-235 / T3: $190-210",
    positionSize: "5% (staged, 3 tranches)",
    reportFile: "../reports/ADBE_2026-05-09.md",
    fullContent: `# ADBE — Adobe Inc.
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

---

## 📌 ข้อมูลหลัก

| Field | Detail |
|-------|--------|
| **Ticker** | ADBE (NASDAQ) |
| **Date** | 2026-05-09 |
| **Current Price** | ~$253.00 |
| **Market Cap** | ~$108.8B |
| **Sector** | Technology / Creative & Marketing Software (SaaS) |
| **Analyst Team** | Emma (Equity) · Quinn (Quant) · Bear (Risk) · Charlie (Orchestrator) |
| **Atlas Macro Context** | Fed 4.25–4.50% · 10Y 4.30% · S&P 500 ~7,399 · US-China 90d Truce Active |

---

## 🎯 คำแนะนำ

| Field | Detail |
|-------|--------|
| **Recommendation** | **BUY — Staged Entry** |
| **Entry Zone** | T1: $240–260 · T2: $215–235 · T3: $190–210 |
| **Blended Fair Value** | **$311.70** (ESG-adj: $302) |
| **Margin of Safety** | **+23.2%** (ESG-adj: +19.5%) |
| **Stop Loss** | $185 |
| **Target Base** | $311 (+23%) |
| **Target Bull** | $395–465 (+56–84%) |
| **Max Position** | 5% (Quarter-Kelly, Wide Moat) |

---

## 📊 Score Dashboard

| Metric | Value |
|--------|-------|
| Blended Fair Value | $311.70 |
| MOS % | +23.2% |
| ESG Score | 7.2/10 |
| Conviction Avg | 7.3/10 |
| Investment Horizon | 3–5+ ปี |
| S&P 500 Reference | ~7,399 |

---

> ## ⚡ TL;DR
>
> - **Verdict: BUY (Staged, 5%)** — Wide Moat SaaS leader ราคา $253 = P/E 12.3x vs peer median 30x = discount 59% บน FCF Margin 42% + ROE 58.8%
> - **ทำไม:** ตลาด over-price AI disruption risk; Firefly = monetization catalyst ไม่ใช่ existential threat; Blended FV $311 = MOS +23%; Kelly 28-31% positive (ต่างจาก V ที่ Kelly ลบ)
> - **Downside Risk:** Bear FCF 8% case → FV $202–255 = ใกล้ราคาปัจจุบัน; Firefly revenue miss Q2 FY2027 = thesis invalidation; Stop $185

---

## 💪 Conviction Level Score

Emma   ████████░░  8/10  — Wide Moat / massive discount vs peers; Firefly thesis compelling
Quinn  ███████░░░  7/10  — Kelly positive 28-31%, 56% cells support; momentum still negative
Bear   ███████░░░  7/10  — Cautious BUY; FCF growth 8% not 12%; SBC-adj FCF $7.5B not $9.0B
─────────────────────────────────────────────────────────────────────────────────────
Avg    ███████░░░  7.3/10  [No flag — gap 1pt < 3pt threshold]

---

## 💰 Valuation Triangulation

| Source | Weight | Value |
|--------|--------|-------|
| Emma Blended FV | 30% | $363 |
| Quinn P-W EV | 30% | $316 |
| Bear P-W EV | 40% | $270 |
| **Charlie Blended** | 100% | **$311.70** |
| ESG-adj (-3%) | | **$302** |

MOS: +23.2% | Kelly: 28-31% raw → 5% Quarter-Kelly

---

## 📉 Sensitivity Matrix 5×5 (FCF CAGR x Exit EV/EBITDA Multiple)

| FCF CAGR \\ EV/EBITDA | 8x | 12x | 16x | 20x | 24x |
|----------------------|------|------|------|------|------|
| 5% (Bear Disruption) | $118 | $177 | $236 | $295 | $354 |
| 8% (Bear Base) | $135 | $202 | $270 | $337 | $405 |
| 12% (Base) | $158 | $237 | $316 | $395 | $474 |
| 16% (Bull) | $186 | $279 | $372 | $465 | $558 |
| 20% (Extreme Bull) | $220 | $330 | $440 | $550 | $660 |

Cells >= $253: 14/25 = 56% | Base (12% x 16x) = $316

---

## 🔄 What Would Change Our Mind

**Bull Flip Triggers:**
1. Firefly API Revenue >= $500M ใน FY2026
2. Creative Cloud subscriber growth >= 8% YoY
3. International revenue (neutral) >= 15%
4. Operating Margin >= 35% GAAP
5. EV/EBITDA re-rate >= 18x

**Bear Flip Triggers:**
1. Revenue growth <= 8% สองไตรมาสติดกัน
2. Canva/Google enterprise wins >= 3 Fortune 500 ใน 12 เดือน
3. FCF Margin <= 35%
4. DOJ/EU antitrust new investigation
5. CEO Narayen departure without succession

**Thesis Invalidation:**
Firefly < $200M by Q2 FY2027 → Full Re-Analysis Required

---

## 🎯 Recommendation

> ### BUY — Staged Entry (5%, 3 Tranches)
> Wide Moat Creative Software leader ราคา $253 = P/E 12.3x vs peer median 30x = 59% discount บน FCF Margin 42%; Blended FV $311.70 = MOS +23.2%; Kelly positive 28-31%

T1: $240-260 (2%) — immediate | T2: $215-235 (2%) — pullback | T3: $190-210 (1%) — Bear base
Stop: $185 | Base: $311 | Bull: $395-465

---

*รายงานจัดทำโดย บลจ. CFA Team | 2026-05-09 | S&P 500 ref: ~7,399*
`
  }
'@

# แทรก ADBE entry ก่อน ];
$content = $content -replace '];', "$adbeEntry`n];"

# เขียนกลับ
Set-Content $dataFile -Value $content -Encoding UTF8
Write-Host "ADBE entry เพิ่มใน data.js สำเร็จ | LAST_UPDATED อัปเดตเป็น 2026-05-09"
