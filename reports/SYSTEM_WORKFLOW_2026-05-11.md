# บลจ. CFA — System Workflow & Feature Reference
> อัปเดตล่าสุด: 2026-05-11 | เวอร์ชัน 2.0

---

## ทีม (Agents)

| Agent | บทบาท | Tools | Motto |
|-------|--------|-------|-------|
| **Charlie** | CIO Orchestrator — รับคำสั่ง delegate ทุกอย่าง ไม่วิเคราะห์เอง | Agent, Read, Write | "Never trades directly. Always delegates." |
| **Atlas** | Macro Analyst — วิเคราะห์ภาพรวมเศรษฐกิจ สแกนข่าว ตรวจ earnings | Read, Write, WebSearch, WebFetch | "The big picture is always macro." |
| **Emma** | Equity Analyst — Fundamental, Moat, Valuation, ESG | Read, Write, WebSearch, Bash | "Price is what you pay. Value is what you get." |
| **Quinn** | Quantitative Analyst — Sharpe, Kelly, Factor Model, Sensitivity Matrix | Read, Write, WebSearch, Bash | "Numbers don't lie, but people lie with numbers." |
| **Bear** | Devil's Advocate — challenge ทุก thesis ห้ามเห็นด้วยง่ายๆ | Read, Write, WebSearch | "Every bull case needs a bear case." |
| **Morgan** | QA Analyst — ตรวจราคา ข้อมูล format ก่อน publish ทุกครั้ง | Read, Write, WebFetch, WebSearch | "No source, no fact. No fact, no report." |
| **Leo** | Learning Log + Life OS — บันทึก decision, export, push inbox | Read, Write, Bash | "Yesterday's lesson beats tomorrow's prediction." |
| **Vera** | Performance Tracker — P&L, alpha, attribution analysis | Read, Write, WebSearch | "The numbers never lie about the past." |
| **Max** | Portfolio Manager — scout, execute, manage portfolio อัตโนมัติ | Read, Write, WebSearch, WebFetch, Bash | "The best analysis means nothing without a position." |

---

## Research Pipeline (ทุก analysis)

```
CIO → Charlie
         │
         ▼
      Atlas ── Phase 1: Macro Brief (Fed, yields, GDP, USD, geopolitical)
         │   ── Phase 2: Data Package (ราคา, revenue, EPS, beta จาก WebFetch)
         │   ── Phase 3: News Monitor (Yahoo Finance, SEC 8-K, Google News RSS)
         │              └─ 🚨 THESIS ALERT ถ้าพบ Bear Flip Triggers
         │              └─ ⚠️ EARNINGS FLAG ถ้า earnings ≤ 14 วัน
         │
         ▼
   [Emma ∥ Quinn] ── วิเคราะห์พร้อมกัน armed with macro context
         │           Emma: DCF, Moat, ESG, Peer Comparison
         │           Quinn: Sharpe, Kelly, Sensitivity 5×5, Carhart 4-Factor
         │
         ▼
       Bear ── challenge ทุก thesis ห้ามเห็นด้วยง่ายๆ
         │
         ▼
     Charlie ── สรุป + เขียน Research Report (format บังคับ)
         │
         ▼
      Morgan QA ── Step 0: WebSearch ราคาจริง (BLOCKING ถ้าต่าง >5%)
         │        ── Step 0.5: spot-check revenue/EPS/FCF (BLOCKING ถ้าต่าง >10%)
         │        ── Step 1-5: completeness, format, DCF sanity, consistency
         ▼         
    ❌ FAIL ──→ แจ้ง Charlie แก้ → QA ใหม่
    ✅ PASS
         │
         ▼
       Leo ── บันทึก learning-log → decisions.md → dashboard/data.js
         │  ── export Full Report + Content Brief → Documents/บลจ-CFA/
         │  ── push Life OS inbox → git commit → push main
         │
         ▼
      Vera ── log entry price + S&P 500 price → performance/tracker.md
         │
         ▼
       Max ── ตรวจ Portfolio Rules → Execute ถ้า BUY + ราคาใน entry zone
         │
         ▼
      ตอบ CIO
```

---

## Max — Portfolio Management Pipeline

### Weekly Run (ทุกสัปดาห์)
```
Max รันประจำสัปดาห์
   │
   ├─ 1. อ่าน portfolio/positions.md
   ├─ 2. Atlas Phase 3 — News Monitor + Earnings Calendar (ก่อนทุกอย่าง)
   │       └─ ถ้ามี 🚨 THESIS ALERT → trigger re-analysis ทันที
   │       └─ ถ้า ⚠️ EARNINGS ≤ 14 วัน → flag CIO
   ├─ 3. WebFetch ราคาปัจจุบันทุก position
   ├─ 4. ตรวจ Exit Rules
   │       Stop Loss hit → SELL ทันที
   │       Re-analysis = AVOID → SELL ทันที
   │       Return >50% + conviction <6 → Trim 50%
   ├─ 5. Scout หาหุ้นใหม่ (ถ้า cash ≥ 15%)
   ├─ 6. Execute trades ที่ผ่าน Portfolio Rules
   ├─ 7. อัปเดต dashboard/portfolio.js + performanceHistory[]
   ├─ 8. Push Life OS
   └─ 9. สรุปให้ CIO
```

### Portfolio Rules (ห้ามละเมิด)
| กฎ | Threshold |
|----|-----------|
| Minimum conviction | ≥ 6.0 |
| Position Size | Conviction × 1% (max 10%) |
| Sector concentration | ≤ 25% |
| Minimum cash | ≥ 10% |
| ราคาเกิน entry zone | ลด size 50% |

### Regime Multiplier (ใหม่ v2.0)
| Macro Regime | Multiplier | ตัวอย่าง conviction 7 |
|---|---|---|
| Risk-ON | 1.0× | 7% |
| Recovery | 1.0× | 7% |
| Stagflation | 0.75× | 5.25% |
| Risk-OFF | 0.5× | 3.5% |

---

## Morgan QA — กระบวนการตรวจ

```
Step 0   → WebSearch ราคาจริงอิสระ (BLOCKING — ต่าง >5% = FAIL ทันที)
Step 0.5 → WebSearch spot-check revenue/EPS/key metric (BLOCKING — ต่าง >10% = FAIL)
Step 1   → อ่าน report ทั้งไฟล์
Step 2   → ตรวจ Source Citations + Quality Tier + Data Freshness
Step 2.5 → DCF Assumption Sanity Check (WACC 7-13%, Terminal Growth ≤3%)
Step 2.6 → Data Package Compliance + Cross-agent Consistency
Step 3   → Completeness Check (16 sections บังคับ)
Step 4   → Format Compliance (emojis, Conviction Bar, Verdict callout)
Step 5   → Data Consistency + Bear Challenge Response Quality
```

**Data Freshness Threshold:**
| ข้อมูล | อายุสูงสุด |
|--------|-----------|
| ราคาหุ้น | 3 วัน |
| Revenue/EPS | 1 quarter |
| Beta | 12 เดือน |
| Peer P/E | 6 เดือน |

---

## Atlas — News Monitor (Phase 3 ใหม่ v2.0)

ทุก Weekly Run Atlas ตรวจอัตโนมัติ:
- **Yahoo Finance News** — ข่าวล่าสุดของแต่ละ ticker ที่ OPEN
- **SEC EDGAR 8-K** — ประกาศสำคัญ (ฟรี, real-time)
- **Google News RSS** — ข่าวชื่อบริษัท

**Output:**
- 🚨 `THESIS ALERT` — ถ้าพบ Bear Flip Trigger → trigger re-analysis
- ⚠️ `EARNINGS FLAG` — ถ้า earnings ≤ 14 วัน → บันทึก consensus EPS/Revenue

---

## Vera — Performance Tracking (Enhanced v2.0)

### Quarterly Review
- **Position Contribution** — ใครดึงพอร์ตขึ้น/ลงมากที่สุด
- **Sector Attribution** — sector ไหนชนะ/แพ้ benchmark
- **Analyst Calibration Score** — conviction สูง = return สูงจริงไหม?
  - Emma accuracy, Quinn accuracy, Bear accuracy แยกกัน
  - ใช้ calibrate น้ำหนักของแต่ละ analyst ในอนาคต

### P&L Chart (ใหม่ v2.0)
- `dashboard/portfolio.js` มี `performanceHistory[]`
- สะสมทุก Weekly Run → Line Chart Portfolio vs S&P 500
- เห็น alpha trend ตลอด investment journey

---

## Output Files (บังคับทุก analysis)

| ไฟล์ | ผู้สร้าง | Path |
|------|---------|------|
| Research Report | Charlie | `reports/TICKER_YYYY-MM-DD.md` |
| Session Log | Leo | `session_logs/YYYY-MM-DD_HHMM_TICKER.md` |
| Emma's Notes | Emma | `agent_notes/emma/YYYY-MM-DD_TICKER.md` |
| Quinn's Notes | Quinn | `agent_notes/quinn/YYYY-MM-DD_TICKER.md` |
| Bear's Notes | Bear | `agent_notes/bear/YYYY-MM-DD_TICKER.md` |
| Leo's Notes | Leo | `agent_notes/leo/YYYY-MM-DD_TICKER.md` |
| Morgan QA Report | Morgan | `agent_notes/morgan/YYYY-MM-DD_TICKER_qa.md` |
| Full Report Export | Leo | `Documents/บลจ-CFA/reports/TICKER_DATE.md` |
| Content Brief | Leo | `Documents/บลจ-CFA/reports/TICKER_content-brief.md` |

นอกจากนี้ Leo อัปเดต:
- `portfolio/decisions.md`
- `dashboard/data.js`
- `learning-log.md`
- `portfolio/positions.md` (Max)
- `portfolio/trade-log.md` (Max)
- `dashboard/portfolio.js` + `performanceHistory[]` (Max)

---

## Research Report Format (บังคับทุก report)

```
# [EMOJI] TICKER — Company Name
### Equity Research Report · บลจ. CFA Multi-Strategy Aggressive Growth

📌 ข้อมูลหลัก   (Ticker, Date, Price, Market Cap, Sector, S&P500)
🎯 คำแนะนำ     (Recommendation, Entry Zone, Blended FV, MOS, Stop Loss, Max Position)
📊 Score Dashboard (Blended FV, MOS, ESG, Conviction, Horizon)

> ⚡ TL;DR — อ่าน 30 วินาที
> - Verdict / ทำไม / Downside Risk
```

**16 Sections บังคับ (พร้อม emoji):**
📋 Executive Summary → 💡 Investment Thesis → 🏢 Business Overview → 🏰 Moat Analysis → 📊 Sector/Peer Comparison → 💰 Valuation → 📉 Quantitative Risk → 🌱 ESG Scorecard → 💪 Conviction Score → 🔄 What Would Change Our Mind → 🎯 Recommendation → ⚠️ Risk Summary → 📅 Catalysts Calendar → 📚 CFA Concepts → ⚙️ Behind the Scenes → 🏁 Conclusion

**Conviction Bar Format:**
```
Emma   ██████░░░░  6/10  — reasoning
Quinn  █████░░░░░  5/10  — reasoning
Bear   ███████░░░  7/10  — reasoning
──────────────────────────────────────────
Avg    ██████░░░░  6.0/10
```

---

## กฎเหล็ก (House Rules)

1. ไม่ใช้ API key ภายนอก — ทุกอย่างผ่าน Claude Code
2. Leo อ่าน `learning-log.md` ก่อนทุกงาน
3. Bear ต้องแย้งเสมอ ห้ามเห็นด้วยง่ายๆ
4. Charlie สรุปเป็นภาษาไทย ชัดเจน กระชับ
5. อ้างอิง CFA framework ทุกครั้งที่วิเคราะห์
6. Atlas ก่อนเสมอ — ห้าม Emma/Quinn วิเคราะห์โดยไม่มี macro context
7. Emma และ Quinn ต้องระบุ source annotation ทุก financial data
8. Morgan ต้องตรวจ QA ก่อน Leo ทุกครั้ง
9. Leo บันทึก S&P 500 price ณ วันวิเคราะห์ทุกครั้ง
10. **Full Autonomy Mode** (2026-05-11) — Max ตัดสินใจ execute ได้เองหลัง QA PASS ไม่ต้องรอ CIO confirm

---

## เป้าหมายของระบบ

> **"สร้างขึ้นเพื่อศึกษาการลงทุนแบบมืออาชีพ"** — CIO, 2026-05-11

ทุก decision ที่ทีมทำ ถูกหรือผิด Vera จะติดตาม performance vs S&P 500 ให้เห็นผลจริง บทเรียนที่ดีที่สุดมาจากการปฏิบัติจริง ไม่ใช่การอ่านหนังสือ

---

*บลจ. CFA Multi-Strategy Aggressive Growth | ห้ามใช้เป็น financial advice*
