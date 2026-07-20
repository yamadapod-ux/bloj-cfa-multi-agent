# House Rules — ตัวอย่าง 3 Sections ใหม่

> ไฟล์นี้แสดง format ของ 3 house rules ใหม่ โดยใช้ NVDA และ CCJ เป็นตัวอย่าง
> รายงานจริงรอบหน้าจะมี sections เหล่านี้รวมอยู่ในรายงานเต็มแล้ว

---

# ตัวอย่างที่ 1: CFA Footnotes

## วิธีใส่ใน section heading

```
## DuPont Analysis [CFA L1: Financial Reporting — DuPont Decomposition]
## DCF Valuation [CFA L2: Equity Valuation — FCFF Model]
## Carhart 4-Factor [CFA L2: Portfolio Management — Multi-Factor Models] *(ยังไม่เรียน — โมเดลที่แยกผลตอบแทนออกเป็น 4 ปัจจัย: ตลาด, ขนาด, มูลค่า, momentum)*
## CVaR / Expected Shortfall [CFA L3: Risk Management — Tail Risk Measures] *(ยังไม่เรียน — ค่าเฉลี่ยของการขาดทุนที่เกิน VaR ใช้วัด tail risk)*
## ESG Investing Framework [CFA L2–3: ESG Investing — Materiality Analysis]
## Sensitivity Analysis [CFA L2: Equity Valuation — Sensitivity & Scenario Analysis]
```

### CFA Studied ปัจจุบัน (จาก learning-log)
| Level | Concepts ที่เรียนแล้ว |
|-------|---------------------|
| L1 | Financial Reporting, DuPont, Sharpe Ratio, Beta, VaR, Hypothesis Testing, CAPM, TVM |
| L2 | DCF (FCFF/FCFE), EV/EBITDA, PEG, Economic Moat, Porter's 5 Forces, Carhart 4-Factor, Scenario Analysis |
| L3 | Kelly Criterion, CVaR/Expected Shortfall, Behavioral Finance, Portfolio Construction |

---

# ตัวอย่างที่ 2: ESG Risk Scorecard

---

## NVDA — ESG Risk Scorecard [CFA L2–3: ESG Investing — Materiality Analysis]

| Dimension | Score (1–10) | Key Issues |
|-----------|-------------|-----------|
| **Environmental** | 5/10 | Data center energy consumption สูงมาก (AI training cluster ใช้ไฟฟ้า ~GW level), water cooling usage, supply chain carbon (TSMC fabrication) |
| **Social** | 7/10 | ไม่มี major labor controversy, H-1B visa dependency risk, ผลกระทบ AI job displacement ต่อสังคมวงกว้าง |
| **Governance** | 8/10 | Jensen Huang ถือ dual-class shares (voting power เหนือกว่า), แต่ board independence ดี, exec comp สมเหตุสมผล |
| **Overall ESG** | **6.7/10** | **Medium Risk** |

**ESG Rating: Medium Risk**

### Material ESG Risks (กระทบ Valuation)
1. **Data Center Energy Consumption** — AI boom ผลักดัน electricity demand ของ data centers +300% ภายใน 2030 กฎระเบียบ energy ของ EU และสหรัฐที่อาจออกมาเพิ่ม compliance cost → valuation impact: **-2 ถึง -5% fair value**
2. **Export Restriction Risk (Governance/Geopolitical)** — กระทรวงพาณิชย์สหรัฐอาจขยาย chip export ban ต่อจีน → China revenue ~20% ของรายได้ทั้งหมด → valuation impact: **-5 ถึง -15% fair value** ใน bear scenario
3. **AI Regulation & Liability** — EU AI Act บังคับใช้ปี 2026 อาจกำหนด liability สำหรับ AI hardware makers → regulatory compliance cost → valuation impact: **-1 ถึง -3% fair value**

**Bear Challenge on NVDA ESG:** "Score 5/10 Environmental ยังประเมิน optimistic เกินไป — hyperscaler data centers รวมกันใช้ไฟฟ้ามากกว่าบางประเทศ และ NVDA เป็น enabler หลัก carbon tax ที่อาจมาถึงจะกระทบ customer CapEx โดยตรง"

---

## CCJ — ESG Risk Scorecard [CFA L2–3: ESG Investing — Materiality Analysis]

| Dimension | Score (1–10) | Key Issues |
|-----------|-------------|-----------|
| **Environmental** | 4/10 | Mining operations มีผลกระทบต่อ environment: tailings management, water contamination risk, mine reclamation cost $800M+, radioactive waste |
| **Social** | 6/10 | Indigenous community relations ที่ Saskatchewan เป็น ongoing concern, mining safety record ดีขึ้นแต่ยังมี incident risk, แรงงาน union relations |
| **Governance** | 7/10 | Board มีความหลากหลาย, ไม่มี dual-class shares, executive comp tied to ESG metrics แต่ disclosure ยังไม่ครบ |
| **Overall ESG** | **5.7/10** | **Medium-High Risk** |

**ESG Rating: Medium-High Risk**

### Material ESG Risks (กระทบ Valuation)
1. **Mine Reclamation Liability** — Off-balance sheet obligations $800M+ ที่ต้องจ่ายเมื่อปิดเหมือง Emma และ Quinn ไม่ได้รวมใน EV calculation → valuation impact: **-$2.00 ถึง -$3.00 per share**
2. **Tailings & Water Contamination Risk** — ประวัติอุตสาหกรรม uranium mining ใน Saskatchewan มีเหตุการณ์ contamination แม้ CCJ มี record ที่ดีกว่าค่าเฉลี่ย → ถ้าเกิดเหตุ → regulatory shutdown → valuation impact: **-10 ถึง -30% fair value**
3. **Indigenous Land Rights** — พื้นที่เหมืองส่วนหนึ่งอยู่ใน traditional territory ของ First Nations → ถ้ามีข้อพิพาทกฎหมาย → permitting risk สำหรับ future expansion → valuation impact: **-3 ถึง -8% fair value**

**Bear Challenge on CCJ ESG:** "Score 4/10 Environmental อาจยังสูงเกินไป — uranium tailings มี half-life เป็นพัน ๆ ปี liability จริงอาจสูงกว่า $800M ที่ประเมินไว้ และ IFRS 9/16 กำหนดให้ต้องบันทึก present value ของ reclamation ทั้งหมด ซึ่งทีมยังไม่ได้รวมใน DCF"

---

# ตัวอย่างที่ 3: Sensitivity Matrix 5×5

---

## NVDA — Sensitivity Matrix [CFA L2: Equity Valuation — Sensitivity Analysis]

**Variable 1 (แกนแนวตั้ง):** Revenue Growth Rate Y1–Y3 | Range: 5% → 35%
**Variable 2 (แกนแนวนอน):** WACC | Range: 8.5% → 12.5%
**Base Case:** Growth 25%, WACC 10.5% → **Bold**

*ราคา Fair Value per Share ($)*

| Growth \ WACC | 8.5% | 9.5% | **10.5%** | 11.5% | 12.5% |
|--------------|------|------|-----------|-------|-------|
| **5%**  | $62  | $54  | $47  | $41  | $36  |
| **15%** | $95  | $82  | $71  | $62  | $54  |
| **25%** | $148 | $127 | **$109** | $94  | $82  |
| **30%** | $178 | $152 | $130 | $112 | $97  |
| **35%** | $212 | $181 | $154 | $133 | $115 |

*ราคาปัจจุบัน: ~$110 | Bold = Base Case ($109) ≈ ราคาตลาด*

**Color Guide:**
- ≥$130 (สูงกว่าตลาด >18%): Upside Zone
- $95–$129: Fair Value Zone
- <$95 (ต่ำกว่าตลาด >14%): Downside Zone

**Quinn's Insight:** NVDA fair value **ไวต่อ Revenue Growth มากกว่า WACC** — ถ้า growth ลงจาก 25% → 15% (ไม่เปลี่ยน WACC) fair value ลด $109 → $71 (-35%) แต่ถ้าเปลี่ยนแค่ WACC +2% fair value ลดแค่ $109 → $82 (-25%) → **นักลงทุนควร monitor hyperscaler capex guidance เป็นตัวแปรหลัก**

---

## CCJ — Sensitivity Matrix [CFA L2: Equity Valuation — Sensitivity Analysis]

**Variable 1 (แกนแนวตั้ง):** Uranium Spot Price | Range: $40/lb → $100/lb
**Variable 2 (แกนแนวนอน):** WACC | Range: 9.5% → 13.5%
**Base Case:** Uranium $70/lb, WACC 11.37% → **Bold**

*ราคา Fair Value per Share ($)*

| U3O8 Price \ WACC | 9.5% | 10.5% | **11.37%** | 12.5% | 13.5% |
|------------------|------|-------|------------|-------|-------|
| **$40/lb**  | $18  | $15  | $12  | $10  | $8   |
| **$55/lb**  | $35  | $29  | $24  | $19  | $15  |
| **$70/lb**  | $58  | $48  | **$40** | $33  | $27  |
| **$85/lb**  | $82  | $68  | $57  | $47  | $39  |
| **$100/lb** | $108 | $90  | $75  | $62  | $52  |

*ราคาปัจจุบัน: ~$52.50 | Bold = Base Case ($40) ต่ำกว่าราคาตลาด 24%*

**Color Guide:**
- ≥$60 (สูงกว่าตลาด >14%): Upside Zone → ต้องการ uranium $85/lb+ หรือ WACC <10.5%
- $45–$59: Fair Value Zone
- <$45 (ต่ำกว่าตลาด >14%): Downside Zone → base case ปัจจุบัน!

**Quinn's Insight:** CCJ fair value **ไวต่อ Uranium Price มากกว่า WACC** — ถ้า uranium ขึ้นจาก $70 → $85 (WACC คงที่) fair value เพิ่ม $40 → $57 (+43%) แต่ถ้าเปลี่ยนแค่ WACC -2% fair value เพิ่มแค่ $40 → $58 (+45%) → **ทั้งสองตัวแปรมีผลพอๆ กัน แต่ uranium price ควบคุมไม่ได้** Base case ปัจจุบัน ($40) ต่ำกว่าราคา $52.50 อย่างมีนัย — ยืนยัน Bear's call ว่า margin of safety ไม่มี

---

*ตัวอย่างนี้จัดทำโดย Quinn | House Rules Version 1.0 | 2026-04-24*
*รายงานรอบถัดไปจะรวม 3 sections นี้ใน full research report อัตโนมัติ*
