---
description: วิเคราะห์หุ้น — fetch ข้อมูลจริงใน main conversation ก่อน แล้วค่อย dispatch pipeline (แก้ปัญหา training knowledge ban)
---

## งาน: Analyze Stock — Verified Data First

**Arguments:** $ARGUMENTS (TICKER — เช่น "/analyze GOOGL" หรือ "/analyze NVDA")

**วันที่วันนี้:** ใช้ `currentDate` จาก system context

---

> ## ⛔ กฎเหล็กของ skill นี้
> **ทุก data fetch ต้องเกิดใน main conversation — ห้าม delegate ให้ sub-agent หาข้อมูลเอง**
> ถ้า WebSearch ไม่ได้ผล → เขียน "DATA FETCH FAILED — BLOCK PIPELINE" แล้วหยุดทันที
> ห้าม proceed ด้วย estimate หรือ training knowledge ไม่ว่ากรณีใด

---

### Phase 0 — Parse Arguments

```
TICKER = $ARGUMENTS (uppercase)
TODAY  = วันที่ปัจจุบันจาก system
```

ถ้าไม่มี TICKER → หยุดทันที แจ้ง: "ระบุ ticker เช่น `/analyze GOOGL`"

---

### Phase 1 — Fetch Current Price (≥ 2 sources บังคับ)

ทำตามลำดับนี้ — WebFetch ก่อนเสมอ WebSearch เป็น fallback เท่านั้น:

**Source 1 — Yahoo Finance (WebFetch primary):**
```
WebFetch: https://finance.yahoo.com/quote/{TICKER}/
```
ดึง: ราคาปัจจุบัน, Market Cap, 52W Range, Beta, P/E, Forward P/E, EPS, Volume

**Source 2 — Stockanalysis (WebFetch primary):**
```
WebFetch: https://stockanalysis.com/stocks/{ticker}/
```
ดึง: ราคา, Market Cap, Shares Outstanding, P/E, Forward P/E, EV/Revenue, ROE, ROIC

**Fallback — ถ้า WebFetch ทั้งสองล้มเหลว:**
```
WebSearch: "{TICKER} stock price today {TODAY_YEAR}"
WebSearch: "{TICKER} stock quote market cap {MONTH} {YEAR}"
```
*(บันทึกว่าใช้ WebSearch fallback — ข้อมูลอาจ cached)*

บันทึกผล:
```
Price Source 1: $_____ (Yahoo Finance WebFetch) URL: https://finance.yahoo.com/quote/{TICKER}/
Price Source 2: $_____ (Stockanalysis WebFetch)  URL: https://stockanalysis.com/stocks/{ticker}/
Price ที่ใช้: ค่าล่าสุดที่ verified
```

**Gate:** ถ้าได้ < 2 sources หรือ 2 sources ต่างกัน > 5% → หยุด flag ⚠️ และแจ้ง CIO

---

### Phase 2 — Fetch Financial Statements (WebFetch primary)

ทำ WebFetch ทุก URL ด้านล่างตามลำดับ — ดึง structured data โดยตรงจากหน้าเว็บ:

**2A — Income Statement:**
```
WebFetch: https://stockanalysis.com/stocks/{ticker}/financials/
```
ดึง: Revenue TTM + 4Q ล่าสุด + FY, Gross Margin, EBITDA, Net Income, EPS Diluted, Revenue Growth YoY

**2B — Balance Sheet:**
```
WebFetch: https://stockanalysis.com/stocks/{ticker}/financials/balance-sheet/
```
ดึง: Cash, Total Debt, Net Debt, Total Assets, Shareholders Equity, Shares Outstanding

> ⚠️ **Arithmetic Sanity Check (บังคับ — เพิ่มหลัง MU session 2026-08-27):** WebFetch ใช้ AI model สรุปหน้าเว็บให้ — ตัวเลข "Net Cash/Net Debt" ที่หน้าเว็บสรุปมาเองบางครั้ง**ไม่ตรงกับ Cash − Total Debt** ที่ควรจะเป็น (เคยพบ: หน้าเว็บสรุป Net Cash $23.8B แต่ Cash $24.99B − Debt $6.38B = $18.61B จริง ต่างกัน 22% — ไม่ถูกจับได้จนกว่าจะถึงชั้น Atlas downstream) ให้ **คำนวณ Net Cash/Net Debt เองเสมอ** จาก Cash และ Total Debt ที่ fetch มา แล้วเทียบกับตัวเลขที่หน้าเว็บสรุปไว้ — ถ้าต่างกัน > 5% ให้ใช้ **ค่าที่คำนวณเอง** (Cash − Debt) เป็นค่าหลักในการส่งต่อ พร้อม flag ความขัดแย้งไว้ในบันทึกผลด้านล่าง อย่ารอให้ downstream agent จับ

**2C — Cash Flow:**
```
WebFetch: https://stockanalysis.com/stocks/{ticker}/financials/cash-flow-statement/
```
ดึง: Operating CF, CapEx, Free Cash Flow TTM + annual

**2D — SEC EDGAR Cross-check (revenue + shares outstanding):**
> ⚡ Token-saving note: `sec.gov/cgi-bin/browse-edgar` reliably 403s WebFetch (confirmed 2026-08-20 VEEV session) — **ข้าม WebFetch ไปที่ WebSearch โดยตรง** อย่าเสีย call ลอง WebFetch ก่อน
```
WebSearch: "{TICKER} 10-K annual report revenue shares outstanding site:sec.gov"
```
ดึง: link 10-K ล่าสุด → เปิดดู Shares Outstanding (cover page) และ Revenue (ปีล่าสุด) — ถ้าเจอ URL ตรงของ filing document (ไม่ใช่ browse-edgar listing page) สามารถ WebFetch URL นั้นตรงๆ ได้ (มักไม่ 403 เพราะเป็น static document ไม่ใช่ CGI endpoint)

**2E — Historical Revenue (growth rate):**
> ⚡ Token-saving note: `macrotrends.net` reliably 403s WebFetch (confirmed 2026-08-20 VEEV session) — **ข้าม WebFetch ไปที่ WebSearch โดยตรง**
```
WebSearch: "{TICKER} revenue history 5 year fiscal {YEAR-4} {YEAR-3} {YEAR-2} {YEAR-1} {YEAR}"
```
ดึง: Revenue 5 ปีย้อนหลัง (ใช้คำนวณ CAGR สำหรับ DCF) — cross-check ตัวเลขจาก 2 แหล่งใน search results ถ้ามี (เช่น WallStreetZen + stockanalysis.com มักให้ตัวเลขตรงกัน)

**Fallback สำหรับ 2A-2C — ถ้า Stockanalysis WebFetch ล้มเหลว:**
```
WebSearch: "{TICKER} quarterly earnings revenue EPS {YEAR} site:stockanalysis.com"
WebSearch: "{TICKER} latest quarterly earnings revenue EPS {YEAR}"
```

บันทึกผล:
```
Quarter:           Q___ ____
Revenue TTM:       $_____B  (YoY: +__%)  [Source: Stockanalysis / EDGAR]
EPS (Diluted):     $_____                [Source: Stockanalysis]
Free Cash Flow:    $_____B               [Source: Stockanalysis]
Gross Margin:      _____%
Cash / Total Debt: $_____B / $_____B
Net Cash (Debt):   $_____B  [self-calc: Cash − Debt]  (page สรุปว่า: $_____B — ⚠️ conflict [ระบุถ้าต่างกัน > 5%, ใช้ self-calc])
Shares Outstanding:_____M               [Source: Stockanalysis / EDGAR cross-check]
⚠️ EDGAR vs Stockanalysis conflict: [ระบุถ้าต่างกัน > 5%]
```

---

### Phase 2F — Fetch Competitor Data (Live — บังคับ ห้ามใช้ training knowledge)

> ⛔ ห้ามประมาณตัวเลข competitor จาก training knowledge เด็ดขาด — ต้อง WebFetch ทุกตัว

**Step 1 — Subject Stock Entry (ใช้ข้อมูลจาก Phase 1–2A ที่มีแล้ว):**
```
{TICKER} entry สำหรับ competitorData:
- revenueGrowth: Revenue Growth YoY TTM จาก Phase 2A (%)
- operatingMargin: Operating Income TTM / Revenue TTM × 100 (%)
  → ถ้าไม่มี Operating Income ให้คำนวณจาก: (EBITDA - D&A est.) / Revenue
  → หรือใช้ Net Income / Revenue เป็น lower-bound proxy ระบุว่าเป็น proxy
- marketCap: จาก Phase 1 (หน่วย $M เช่น $2.5B = 2500)
```

**Step 2 — หา 4–5 Peers:**
```
WebSearch: "{TICKER} {company name} direct competitors peers {sector} 2026"
```
เลือก tickers ที่ compete โดยตรง — ไม่ใช่แค่ sector เดียวกัน

**Step 3 — Fetch ทุก peer พร้อมกัน (parallel WebFetch):**

สำหรับแต่ละ peer: fetch ทั้ง 2 URLs พร้อมกัน
```
WebFetch: https://stockanalysis.com/stocks/{peer}/
→ ดึง: market cap (หน่วย $M หรือ $B), company name

WebFetch: https://stockanalysis.com/stocks/{peer}/financials/
→ ดึง: revenue growth YoY TTM (%), operating margin TTM (%)
```

ถ้า WebFetch peer ใดล้มเหลว → WebSearch fallback:
```
WebSearch: "{PEER_TICKER} revenue growth operating margin market cap 2026"
```
ถ้ายังไม่ได้ → ระบุ "N/A" ห้ามเดา

บันทึกผล (ต้องมีก่อน Phase 5):
```
## Competitor Data (Live-Verified)
| Ticker | Company | Rev Growth TTM | Op Margin TTM | Market Cap | Source |
|--------|---------|---------------|--------------|------------|--------|
| {TICKER} | {subject} | __% | __% | $__M | Phase 2A |
| PEER1  | ...     | __%  | __%  | $__M | Stockanalysis |
| PEER2  | ...     | __%  | __%  | $__M | Stockanalysis |
| PEER3  | ...     | __%  | __%  | $__M | Stockanalysis |
| PEER4  | ...     | __%  | __%  | $__M | Stockanalysis |
```

**กฎเหล็ก:**
- Entry แรกต้องเป็น **subject stock เอง** เสมอ (ทำให้ competitive map highlight ตัวหลักได้)
- ตัวเลขทุกตัวต้องมี source — ห้ามมี "est." สำหรับ competitor metrics
- หน่วย marketCap ต้องเป็น **$M** ตลอด (เช่น $166B Corning = 166000, $580M CLFD = 580)

---

### Phase 3 — Fetch Macro Indicators

**Search:**
```
WebSearch: "VIX index today {TODAY_DATE}"
WebSearch: "US 10 year 2 year yield spread today {TODAY_DATE}"
WebSearch: "high yield credit spreads today {TODAY_DATE}"
WebSearch: "Fed interest rate policy 2026 latest"
```

บันทึกผล:
```
VIX:              _____ → RISK-ON (<20) / TC (20-30) / RISK-OFF (>30)
Yield Curve 10-2: _____bps → Normal (>0) / Flat / Inverted
HY Spreads:       _____bps → RISK-ON (<400) / TC (400-600) / RISK-OFF (>600)
Fed Stance:       _____ → Cuts/Neutral/Hikes priced in
Macro Regime:     _____ (majority vote 3/4)
```

---

### Phase 4 — Fetch Company Context (1 search)

**Search:**
```
WebSearch: "{TICKER} {company name} news analyst outlook {CURRENT_MONTH} {YEAR}"
```

บันทึก: ข่าวสำคัญ 3-5 ข้อที่กระทบ thesis

---

### Phase 5 — Compile & Display Verified Data Package

แสดงสรุปให้ CIO เห็นก่อน proceed:

```
## ✅ Verified Data Package — {TICKER} ({TODAY})

### Price (≥ 2 sources verified)
| Source | Price | URL |
|--------|-------|-----|
| [Source 1] | $____ | [link] |
| [Source 2] | $____ | [link] |
| **ใช้:** | **$____** | |

### Latest Earnings — Q__ ____
| Metric | Value | YoY | Source |
|--------|-------|-----|--------|
| Revenue | $__B | +__% | [URL] |
| EPS | $__ | +__% | [URL] |
| Net Income | $__B | +__% | [URL] |
| [Key segment] | $__B | +__% | [URL] |

### Macro Regime
| Indicator | Value | Signal |
|-----------|-------|--------|
| VIX | ___ | ___ |
| Yield Curve | ___bps | ___ |
| HY Spreads | ___bps | ___ |
| Fed Stance | ___ | ___ |
| **Regime** | **___** | **X/4 indicators** |

### Key News
- ___
- ___
- ___

---
⚠️ Pipeline จะ proceed ด้วยข้อมูลชุดนี้เท่านั้น — agents ห้ามหาข้อมูลใหม่เอง
```

---

### Phase 6 — Dispatch Charlie พร้อม Verified Data

ส่ง verified data package ให้ Charlie ด้วย prompt นี้:

```
CIO สั่งวิเคราะห์ {TICKER} — ใช้ข้อมูลที่ verify แล้วด้านล่าง ห้ามหาข้อมูลราคาหรือ financials ใหม่เอง

## VERIFIED DATA PACKAGE (do not replace — use as-is)
[วาง Verified Data Package จาก Phase 5 ที่นี่]

## งานของ Charlie:
1. ส่ง Verified Data Package นี้ให้ Emma และ Quinn ใช้เป็น single source of truth
2. Emma → Fundamental valuation (DCF, moat, ESG) ใช้ตัวเลขจาก package เท่านั้น
3. Quinn → Quant analysis (beta, sharpe, sensitivity) ใช้ตัวเลขจาก package เท่านั้น
4. Bear → Devil's advocate ใช้ตัวเลขจาก package เท่านั้น
5. Charlie → สรุป report + Blended FV + คำแนะนำ
6. Morgan → QA (ตรวจ source citation ว่า agents ใช้ verified data ไม่ได้แต่งเอง)
7. Leo → บันทึก decisions.md + dashboard/data.js โดย **data.js object ต้องมี 11 rich fields ครบทุกข้อ** (ดูรายการด้านล่าง)
8. Vera → อัปเดต tracker.md
9. Max → พิจารณา execute simulated trade

Macro Regime = {REGIME} → ใช้กำกับ position size multiplier และ force deploy rule

## Dashboard Required Fields (Leo บังคับ — ห้ามขาด)
CIO ตรวจงานจาก dashboard เป็นหลัก ทุก field ด้านล่างต้องอยู่ใน data.js object ถ้าข้อมูลไม่มีให้ใส่ estimate + "(est.)" ไม่ใช่ละไว้:

```
maxDrawdown       — number (% จาก 52W high to low หรือ ATH)
reportFile        — "../reports/{TICKER}_{DATE}.md"
businessSummary   — { oneLiner, analogy, moneyFlow: ["...", "...", "..."] }
thesisBullets     — [{ title, why }, ...] อย่างน้อย 3 bullets
esgBreakdown      — { e: N, s: N, g: N, overall: N }
revenueSegments   — [{ label, value }, ...] (% breakdown by product/end-market)
competitorData    — [{ ticker, company, revenueGrowth, operatingMargin, marketCap }, ...]
                    ⚠️ entry แรกต้องเป็น subject stock เอง (ใช้ข้อมูลจาก Phase 1–2A)
                    ⚠️ peers ทุกตัวต้องใช้ข้อมูลจาก Phase 2F เท่านั้น — ห้ามประมาณจาก training knowledge
                    ⚠️ หน่วย marketCap = $M ตลอด (เช่น $166B = 166000, $2.5B = 2500, $580M = 580)
                    ⚠️ ถ้า peer ใด fetch ไม่ได้ → ใส่ "N/A" ใน revenueGrowth/operatingMargin ห้ามเดา
geographyRevenue  — { unitedStates, international/asia/other, chinaExposure }
bullFlipTriggers  — ["...", ...] 4-5 ข้อวัดได้ (จาก What Would Change Our Mind section)
bearFlipTriggers  — ["...", ...] 4-5 ข้อวัดได้
thesisInvalidation — "..." 1-2 ประโยค
```

ใช้ ALAB object ใน data.js เป็น reference template สำหรับ format ที่ถูกต้อง

Working directory: C:\Users\user\Desktop\บลจ\บลจ CFA
ภาษาไทยเป็นหลัก | ปฏิบัติตาม CLAUDE.md ทุกข้อ
```

---

### Phase 7 — รายงาน CIO หลัง Pipeline เสร็จ

```
✅ /analyze {TICKER} เสร็จสมบูรณ์

📊 Data verified: ราคา {2 sources} · Earnings {Q__ ____} · Macro {REGIME}
🔬 Pipeline: Atlas → Emma ∥ Quinn → Bear → Charlie → Morgan → Leo → Vera → Max
📁 Report: reports/{TICKER}_{TODAY}.md
📈 Dashboard: อัปเดตแล้ว

{RECOMMENDATION} · Blended FV ${___} · MOS {__}% · Conviction {__}/10
```
