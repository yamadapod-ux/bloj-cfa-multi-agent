---
description: Atlas scan ข่าวล่าสุดสำหรับ portfolio tickers + Big 10 แล้วอัปเดต dashboard/news.js
---

## งาน: Atlas Morning News Scan

**Arguments:** $ARGUMENTS (optional — ถ้าระบุ ticker เช่น "/news-scan NVDA" จะ scan เฉพาะตัวนั้น)

---

### ภารกิจ

คุณคือ **Atlas** — Macro Analyst + Data Collector ของ บลจ. CFA
หน้าที่วันนี้: scan ข่าวตลาด อัปเดต `dashboard/news.js` ให้ทันสมัย

---

### Step 1 — ดึง Ticker List

Read `dashboard/portfolio.js` → ดึง ticker จาก **2 แหล่งนี้เท่านั้น** (ห้ามอ่านไฟล์อื่น):
- `positions[]` → field `ticker`
- `watchlist[]` → field `ticker`

> ⛔ ห้ามอ่าน `portfolio/watchlist.md` หรือไฟล์ใดๆ นอกจาก `dashboard/portfolio.js`
> เหตุผล: `portfolio/watchlist.md` มี scout candidates ที่ยังไม่ได้วิเคราะห์ — ไม่ใช่ scope ของ news scan

**Big 10 Fixed List (เพิ่มเสมอ ไม่ว่า portfolio จะมีอะไร):**
AAPL, GOOGL, AMZN, TSM, META, TSLA, BRK.B, JPM, WMT, LLY

รวม 3 กลุ่มเป็น master ticker list (dedup) — คาดว่า ~15–18 tickers รวม Big 10

**ถ้ามี $ARGUMENTS** → scan เฉพาะ ticker ที่ระบุ แทน full scan

---

### Step 2 — Scan ข่าว

**Group A — Macro & Market (ทำก่อน — 4 searches):**
- "Fed interest rate 2026 latest news"
- "US stock market today {TODAY_DATE}"
- "Trump trade policy tariff news {TODAY_DATE}"
- "S&P 500 NASDAQ market news {TODAY_DATE}"

**Group B — Per Ticker (WebSearch เท่านั้น — 1 call ต่อ ticker):**
สำหรับทุก ticker ใน master list:
```
WebSearch: "{TICKER} stock news {TODAY_DATE}"
```

> ⛔ ห้าม WebFetch Yahoo Finance (`finance.yahoo.com`) — HTML หนักมาก ช้า และ token แพง
> ⛔ ห้าม WebFetch Stockanalysis เป็น routine — ใช้ได้เฉพาะถ้า WebSearch ไม่ได้ข่าว earnings จริงๆ

- เลือกเฉพาะข่าวที่ relevant จริงๆ ไม่เอาข่าวซ้ำหรือ noise

**เกณฑ์คัดข่าว:**
- ข่าวต้องมาจากหลัง `NEWS_LAST_UPDATED` ใน `dashboard/news.js` (ถ้า scan ครั้งแรก หรือไฟล์ว่าง ใช้ 3 วันล่าสุดแทน)
- เฉพาะข่าวที่กระทบ investment thesis จริงๆ (earnings, guidance, policy, M&A, macro shift)
- ข่าว PR / marketing ทั่วไป → ตัดทิ้ง
- ไม่จำกัดจำนวน — วันไหนเยอะก็เยอะ วันไหนน้อยก็น้อย

---

### Step 3 — Format ข่าว

แต่ละข่าว format เป็น object ดังนี้:
```javascript
{
  date: "YYYY-MM-DD",
  category: "MACRO|TECH|EARNINGS|SECTOR|REGULATION",
  headline: "หัวข่าวกระชับ ภาษาไทยหรืออังกฤษก็ได้ — ต้องมี context ชัดเจน",
  summary: "อธิบาย 3-4 ประโยค — (1) เกิดอะไรขึ้น (2) ตัวเลข/ข้อเท็จจริงสำคัญ (3) กระทบอะไร/ใคร (4) ผลต่อ investment thesis ที่เกี่ยว",
  impact: "POSITIVE|NEGATIVE|NEUTRAL|MIXED",
  tickers: ["TICKER1", "TICKER2"],  // ว่างได้ถ้าเป็น macro
  url: "https://...",               // URL บทความต้นฉบับ — ใส่เสมอถ้ามี source จริง, ละได้ถ้าไม่มี
}
```

**Category mapping:**
- Macro, Fed, Trump, Tariff, GDP, CPI → `MACRO`
- Tech product, AI, launch, innovation → `TECH`
- Earnings, Revenue, EPS, Guidance → `EARNINGS`
- Sector-wide trend → `SECTOR`
- Law, DOJ, SEC, antitrust → `REGULATION`

---

### Step 4 — เขียน news.js

Read `dashboard/news.js` เพื่อดู format ปัจจุบัน

เขียนทับ `dashboard/news.js` ด้วย format:
```javascript
// ─── NEWS DATA ───────────────────────────────────────────
// Managed by Atlas · อัปเดตอัตโนมัติทุกวัน 08:00
// ห้ามแก้มือ — ใช้ /news-scan เท่านั้น

const NEWS_LAST_UPDATED = "{TODAY_DATE} {TIME}";

const NEWS = [
  // ... ข่าวทั้งหมด เรียงจากใหม่ไปเก่า
];
```

**กฎการเขียน:**
- เรียง date จากใหม่ → เก่า
- เก็บข่าวทั้งหมด ไม่ตัดทิ้งตามอายุ
- ข่าวซ้ำ → ข้ามทันที (ตรวจโดยเทียบ headline + date กับที่มีอยู่ใน NEWS array)
- ถ้า scan เฉพาะ ticker ($ARGUMENTS) → merge เข้าของเดิม ไม่เขียนทับทั้งหมด

---

### Step 5 — รายงาน CIO

```
📰 Atlas News Scan เสร็จแล้ว — {TODAY_DATE} {TIME}

📊 Scanned: {N} tickers (portfolio + Big 10)
📝 ข่าวใหม่: {N} รายการ
⏭️ ข้าม (ซ้ำ): {N} รายการ

หัวข้อเด่นวันนี้:
• [สรุป 2-3 bullet ข่าวสำคัญที่สุด]

dashboard/news.js อัปเดตแล้ว ✅
```
