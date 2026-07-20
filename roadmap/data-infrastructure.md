# แผน Data Infrastructure — บลจ. CFA
*บันทึก 2026-05-09 | ยังไม่ implement — รอแผนใหม่*

---

## สถานะปัจจุบัน

Atlas ใช้ **WebFetch + WebSearch** จาก free sources (Stockanalysis.com, Yahoo Finance, Macrotrends)

**ข้อจำกัดที่ยังมี:**
- HTML layout เปลี่ยนบ่อย → Atlas อาจ misread ตาราง
- ไม่มี analyst consensus (EPS forecast, target price, Forward P/E ที่แม่น)
- Historical price series สำหรับ Quinn ยังต้อง parse เอง
- Macro data (CPI, Fed rate) ยังมาจาก WebSearch ไม่ใช่ official source

---

## Phase 1 — ฟรี (ทำได้ทันที)

### FRED API (Federal Reserve Economic Data)
- **ใช้สำหรับ:** Atlas Phase 1 — Macro Brief
- **ข้อมูลที่ได้:** Fed Funds Rate, 10Y Treasury Yield, CPI, PCE, GDP, Unemployment, ISM PMI
- **ราคา:** ฟรี ไม่จำกัด calls
- **API:** `https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&api_key=YOUR_KEY`
- **สมัคร:** https://fred.stlouisfed.org/docs/api/api_key.html
- **Impact:** Atlas macro data เชื่อถือได้ 100% — official จาก Federal Reserve โดยตรง

### SEC EDGAR API
- **ใช้สำหรับ:** Source verification + official filing numbers
- **ข้อมูลที่ได้:** ตัวเลขจาก 10-K, 10-Q โดยตรง — authoritative ที่สุด
- **ราคา:** ฟรี ไม่จำกัด
- **API:** `https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json`
- **สมัคร:** ไม่ต้องสมัคร — public API
- **Impact:** Morgan ใช้ verify ตัวเลขจาก SEC filing จริง ไม่ใช่ third-party

---

## Phase 2 — ราคาเหมาะสม

### Financial Modeling Prep (FMP)
- **ใช้สำหรับ:** Atlas Phase 2 — Data Package ทั้งหมด
- **ข้อมูลที่ได้:**
  - Income statement, Balance sheet, Cash flow → JSON สะอาด
  - Key ratios (P/E, EV/EBITDA, ROE, ROIC, FCF Yield ฯลฯ)
  - **Analyst consensus: EPS forecast, Revenue forecast, Target price** ← สิ่งที่ขาดอยู่ตอนนี้
  - Peer comparison
  - DCF inputs
- **ราคา:** ~$15/เดือน (Starter) | ~$30/เดือน (Professional — รวม real-time)
- **API ตัวอย่าง:**
  ```bash
  curl "https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=8&apikey=YOUR_KEY"
  curl "https://financialmodelingprep.com/api/v3/analyst-estimates/AAPL?apikey=YOUR_KEY"
  ```
- **สมัคร:** https://financialmodelingprep.com/developer/docs
- **Impact:** Atlas เปลี่ยนจาก WebFetch HTML → API call JSON ทันที ไม่มี parsing ผิดพลาด + ได้ analyst consensus

---

## Phase 3 — ถ้าต้องการ Quant จริงจัง

### Polygon.io
- **ใช้สำหรับ:** Quinn — historical price series, real-time data
- **ข้อมูลที่ได้:** Real-time + historical OHLCV, options data, aggregates
- **ราคา:** Free tier (limited) | $29/เดือน (Starter)
- **API ตัวอย่าง:**
  ```bash
  curl "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-01/2024-01-01?apikey=YOUR_KEY"
  ```
- **สมัคร:** https://polygon.io/
- **Impact:** Quinn คำนวณ Sharpe, Beta, Max Drawdown จาก price series จริงแทนการ estimate

---

## การ Integrate เข้าระบบ

เมื่อพร้อม implement ต้องทำ:
1. เก็บ API keys ใน `.env` ที่ project root
2. Atlas อ่าน key จาก `.env` แล้วใช้ Bash tool รัน `curl` หรือ Python `requests`
3. เพิ่ม `Bash` เข้า Atlas tools (ตอนนี้มีแค่ Read, Write, WebSearch, WebFetch)
4. อัปเดต Phase 2 ใน atlas.md ให้ใช้ API calls แทน WebFetch URLs

**ลำดับ recommended:**
```
FRED + SEC EDGAR (ฟรี, ทำก่อน)
    ↓
FMP $15/เดือน (แก้ปัญหา data quality 80%)
    ↓
Polygon.io $29/เดือน (ถ้าต้องการ quant จริงจัง)
```
