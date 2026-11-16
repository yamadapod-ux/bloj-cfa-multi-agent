

---
---

# Re-Analysis Update — 2026-11-08 (VS2, Full)

> **Trigger:** Re-Analysis Trigger #5 (Street PT median $260 vs internal Blended FV $369 = −29.5%) + Citi Sell PT $207 (2026-11-04) · OPEN position 4 หุ้น @ $247.03, stop $185
> **Data:** Atlas Data Package `agent_notes/atlas/2026-11-08_ADBE.md` (SEC XBRL/10-Q/8-K; ราคา close 11-06 **$239.30** verified Yahoo + StockAnalysis) · ข้อมูล SEC เพิ่มเติม (acquisitions, interest, amortization, deferred revenue, RPO) ดึงจาก XBRL companyfacts ไฟล์เดียวกับ Atlas ผ่าน `scripts/adbe_2026-11-08/sec_more.py`
> **Model:** `scripts/adbe_2026-11-08/emma_dcf.py` (run `python -I`) + `extra.py` (gap-closing เพิ่มเติม) + `fv5check.py` — ทุกตัวเลขในส่วนนี้ reproduce ได้จาก script
> **Bucket: Value** (revenue growth Q3 +12.9% < 20%) · **ประเภท VS2: ธุรกิจทั่วไป (รอง: subscription software)** — ยืนยันเกณฑ์: recurring 97.1% (ผ่าน) แต่ growth TTM +12.0% < 15% (ไม่เข้า SaaS โตเร็ว) — เห็นด้วยกับ Atlas ไม่ flag
> **ไม่ได้อ่านงานใหม่ของ Quinn/Bear ก่อนสรุป FV นี้**

## สรุปผล (Emma)

| รายการ | ค่า |
|---|---|
| **Emma FV (DCF FCFF, 100% — ชั้น 2 ไม่ trigger)** | **$308.39** |
| MOS @ $239.30 (FV/P − 1, convention ทีม) | **+28.9%** · (FV−P)/FV = +22.4% |
| PV(TV)/EV | **51.3%** (≤70% → VS2 ชั้น 2 ไม่ trigger, multiples = cross-check เท่านั้น) |
| No-growth floor (NOPAT FY26E ÷ WACC) | $180.39 |
| FV₅ (VS2 1.4, Emma) | **$488.24** → ผลตอบแทนคาด **+15.3%/ปี** vs S&P 500 implied ~9.7%/ปี |
| Citi scenario (ARR 5.3%/4.5%, GM −70bp) | $254.19 (MOS +6.2%) |
| Citi scenario + terminal RONIC = WACC | **$228.74 ≈ ราคาตลาด** |
| เทียบ Emma FV เดิม (2026-09-11) | $369 → **$308.39 (−16.4%)** |
| Emma Conviction | **6.5/10** (เดิม 7.5) |

**ทำไม FV ลดจาก $369:** (1) เดิม blend DCF $431 + EV/EBITDA 16x $405 + PEG $272 — VS2 ใช้ DCF เป็นวิธีหลัก (TV 51% → ไม่ถ่วง multiples) (2) DCF เดิมใช้ FCFF margin 31.6% ที่ไม่หัก M&A + growth 13%→9% 5 ปี + TV ~75% ของ EV · DCF ใหม่ใช้ growth 9%→3.5% (FY27 ตาม consensus + ARR ชะลอ) + tax 22.6% (เดิม 19%) + terminal reinvestment g/RONIC 12% ของ NOPAT (3) net debt $724M (เดิม ~$2.0B carried) และ shares 391.5M (เดิม 397.4M) ช่วยเล็กน้อย

---

## 1. DCF Valuation [CFA L2: Equity Valuation — FCFF Model]

### 1.1 Inputs (ทุกค่าตาม Atlas 🔒 Pre-registered Judgment Calls — ไม่มีการเปลี่ยนค่าที่ล็อก)

| Input | ค่า | Source / เหตุผล |
|---|---|---|
| Base revenue FY26E | $26,601M | FY26 guide $26.576–26.626B midpoint ([8-K Q3 Ex 99.1](https://www.sec.gov/Archives/edgar/data/0000796343/000079634326000147/adbeex991q326.htm)) |
| Revenue growth FY27→FY36 | 9.0 / 8.0 / 7.0 / 6.5 / 6.0 / 5.5 / 5.0 / 4.5 / 4.0 / 3.5% (10y CAGR 5.89%) | FY27 = consensus +9.1% ([StockAnalysis forecast](https://stockanalysis.com/stocks/adbe/forecast/)) · organic ARR Q3 ~+9.3% (Atlas) · ต่ำกว่า company FY26 ARR target 10.2% เพราะ NNARR/RPO ชะลอ · FY28+ = *assumption ของ Emma* (fade เชิงเส้น) |
| GAAP EBIT margin | 34.5% FY27–28 → 35.0% FY29+ | FY26 guide GAAP op margin ~35% (8-K Q3) · TTM 35.7%, FY21–25 31.3–36.8% (XBRL) · −50bp ช่วงแรกสะท้อน Citi GM −70bp claim + Q3 GM −57bp YoY (Atlas §2) |
| **Tax rate** | **22.6%** | **เลือก 9M FY26 ETR** (XBRL: tax $1,589M ÷ pretax $7,017M) แทน FY25 18% / TTM 21.5% เพราะ (ก) run-rate ล่าสุดที่ขึ้นชัด 3 ไตรมาสติด (Q1–Q3 FY26: 22.0% / 23.5% / 22.5% — XBRL 533/2,422, 526/2,238, 530/2,357) (ข) สอดคล้องกับ tax ที่ Atlas ใช้ใน WACC (Kd after-tax + relever beta) — ไม่ใช้ tax สองค่าในโมเดลเดียว (ค) conservative · สาเหตุเชิงโครงสร้างไม่ทราบจาก XBRL → sensitivity 18%/21.5% ใน §9 |
| Capex | 0.85% rev → 1.2% (FY31+) | TTM $214M = 0.82% · FY20–23 1.9–3.3% (XBRL) → normalize ขึ้น |
| D&A | 2.95% rev → 2.0% (FY31+) | TTM $766M (รวม amortization of acquired intangibles TTM $221M = XBRL 310 − 248 + 159) |
| Tuck-in M&A | 2.0% rev ทุกปี | cash acquisitions FY21 $2,682M / FY22 $126M / FY23–24 $0 / FY25 $17M / 9M FY26 $1,560M (Semrush) ≈ $0.73B/ปี ≈ 3.3% ของ avg revenue (XBRL `PaymentsToAcquireBusinessesNetOfCashAcquired`) · ใช้ 2% เพราะ Semrush จบแล้ว · ทำให้ D&A > capex สอดคล้อง (amortization มาจาก M&A ที่จ่ายจริง) |
| ΔNWC (operating) | 0 | deferred revenue แยกออก (ดู 1.3) |
| WACC | **10.10%** | Atlas locked (Blume 9.98% / bottom-up 10.23%) |
| TGR | 3.0% | ทีม TGR cap · FY36 growth 3.5% < TGR + 3pp = 6% → **ไม่ต้องเพิ่ม fade** (VS2 1.3) |
| **Terminal RONIC** | **25%** | ROIC ปัจจุบัน 57.2% (SA) ลดลงสะท้อน moat ที่แคบลง (§3) แต่ยัง > WACC เพราะไม่มีหลักฐาน structural impairment ใน reported numbers · reinvestment rate ปีสุดท้าย = 3.0% ÷ 25% = **12.0% ของ NOPAT** |
| Equity bridge | FV/หุ้น = EV ÷ 391.5M − $1.85 | Atlas locked (net debt $724M; lease อยู่ใน FCF ไม่หักซ้ำ) |

### 1.2 SBC / Dilution / Buyback Treatment [CFA L2: Equity Valuation — FCFF Model Integrity]
- **SBC TTM $2,071M = 7.97% rev** (< 10% → ไม่บังคับ reconciliation table แต่เปิดเผยตามกฎ) — **หักเป็น expense อยู่ใน GAAP EBIT แล้ว** (FCFF เริ่มจาก NOPAT ไม่ใช่ reported FCF $10,592M ที่บวก SBC กลับ)
- เพราะหัก SBC เป็นต้นทุนแล้ว → ใช้ diluted shares 391.5M **โดยไม่บวก dilution เพิ่ม** (ไม่นับซ้ำ) · ข้อเท็จจริง: buyback TTM $9,295M ≫ SBC $2,071M → diluted shares −6.7% YoY (424.1M → 395.5M) และ −3.2%/ปี FY22→25 (XBRL)
- Buyback = financing (ไม่อยู่ใน FCFF) — ใช้เฉพาะใน FV₅ (§10)
- GAAP vs non-GAAP: FY26 guide GAAP EPS $18.145 vs non-GAAP $24.475 (midpoints, 8-K Q3) → **non-GAAP สูงกว่า 35%** — fwd P/E 8.91x ของตลาดคำนวณบนฐาน non-GAAP → บน GAAP FY26 = 13.2x
- เปรียบเทียบ margin: reported FCF 40.8% vs FCF − SBC 32.8% vs NOPAT-based FCFF FY27 26.8% (หลัง M&A 2%)

### 1.3 Deferred Revenue (แยกตามกฎ)
- Deferred revenue current $7,094M = 27.3% ของ TTM revenue (10-Q Q3) · ถ้านับ benefit (ΔDR = 27.3% × Δrevenue) เข้า FCFF → FV **$317.42 (+2.9%)** — **ไม่นับใน base** เพราะเป็น timing benefit ที่ขึ้นกับ growth + billing terms ไม่ใช่ operating economics

### 1.4 FCFF Table ($M)

| FY | g | Revenue | EBIT m | EBIT | NOPAT | Capex | D&A | M&A | Net reinv. | FCFF | PV @10.10% |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2027 | 9.0% | 28,995 | 34.5% | 10,003 | 7,743 | 246 | 855 | 580 | −29 | 7,772 | 7,059 |
| 2028 | 8.0% | 31,315 | 34.5% | 10,804 | 8,362 | 294 | 849 | 626 | 70 | 8,292 | 6,840 |
| 2029 | 7.0% | 33,507 | 35.0% | 11,727 | 9,077 | 343 | 829 | 670 | 184 | 8,893 | 6,663 |
| 2030 | 6.5% | 35,685 | 35.0% | 12,490 | 9,667 | 397 | 798 | 714 | 312 | 9,355 | 6,366 |
| 2031 | 6.0% | 37,826 | 35.0% | 13,239 | 10,247 | 454 | 757 | 757 | 454 | 9,793 | 6,053 |
| 2032 | 5.5% | 39,906 | 35.0% | 13,967 | 10,811 | 479 | 798 | 798 | 479 | 10,332 | 5,800 |
| 2033 | 5.0% | 41,901 | 35.0% | 14,666 | 11,351 | 503 | 838 | 838 | 503 | 10,848 | 5,532 |
| 2034 | 4.5% | 43,787 | 35.0% | 15,325 | 11,862 | 525 | 876 | 876 | 525 | 11,336 | 5,250 |
| 2035 | 4.0% | 45,539 | 35.0% | 15,938 | 12,336 | 546 | 911 | 911 | 546 | 11,790 | 4,959 |
| 2036 | 3.5% | 47,132 | 35.0% | 16,496 | 12,768 | 566 | 943 | 943 | 566 | 12,203 | 4,662 |
| **Terminal (FY37)** | 3.0% | | | | 13,151 | | | | 12.0% ของ NOPAT | 11,573 | TV 163,001 → PV 62,275 |

- Explicit-period implied RONIC FY36 ≈ 79% (g 3.5% ÷ reinvestment 4.4% ของ NOPAT) → step-down เป็น **25% ใน terminal** (conservative)
- **PV explicit $59,185M + PV(TV) $62,275M = EV $121,460M** · PV(TV)/EV **51.3%**
- **FV/หุ้น = 121,460 ÷ 391.5 − 1.85 = $308.39**
- DCF FV implies: EV/EBITDA TTM 12.1x · P/E FY27 non-GAAP ($27.43 consensus) 11.2x · P/E FY26 GAAP 17.0x
- **No-growth floor sanity (Multi-Segment ข้อ 5):** NOPAT FY26E ($26,601M × 35% × 77.4% = $7,206M) ÷ 10.10% = EV $71,349M → **$180.39/หุ้น** — Emma FV อยู่เหนือ floor ✓ · ราคาตลาด $239.30 = floor × 1.33 → ตลาดให้มูลค่าการเติบโตเพียง ~$59/หุ้น

### 1.5 VS2 ชั้น 2 — Weight Table
| TV ÷ EV | DCF | Multiples | ADBE |
|---|---|---|---|
| ≤ 70% | 100% | cross-check | **✅ 51.3% → DCF 100%** |
| 70–85% | 75% | 25% | |
| > 85% | 60% | 40% | |

---

## 2. Cross-check: P/E + EV/EBITDA vs Peers [CFA L2: Equity Valuation — Relative Valuation]

| วิธี | Multiple | Base | FV/หุ้น | vs DCF $308 |
|---|---|---|---|---|
| Fwd P/E peer median | 15.99x | fwd EPS $26.86 (= $239.30 ÷ 8.91x, SA) | **$429** | +39% |
| Fwd P/E peer min (INTU) | 14.34x | $26.86 | $385 | +25% |
| Fwd P/E ADBE 10Y low ([TIKR](https://www.tikr.com/blog/adobe-adbe-stock-citi-sell-downgrade-hard-reset-pe-ratio)) | 7.5x | $26.86 | $201 | −35% |
| GAAP-basis proxy (FY26 GAAP $18.145 × 1.10) × peer median | 15.99x | $19.96 | $319 | +3% |
| EV/EBITDA peer median | 23.64x | TTM EBITDA $10,037M | **$604** | +96% |
| EV/EBITDA peer min (INTU) | 13.50x | $10,037M | $344 | +12% |
| EV/EBIT peer median / min | 24.70x / 14.97x | TTM EBIT $9,271M | $583 / $353 | +89% / +14% |

Peer multiples: [StockAnalysis statistics](https://stockanalysis.com/stocks/adbe/statistics/) (Atlas Section G, close 11-06)

### Reconciliation (DCF vs peer P/E median ห่าง +39% ≥ 25% → ทดสอบทั้งสองทิศ)
| สาเหตุของ gap | ทิศ | ทดสอบ | ผล |
|---|---|---|---|
| Peer median รวม NOW (growth 19.7%) + ADSK (12.4%) ที่โตเร็วกว่า ADBE 3Y fcst 9.6% | peer **overstate** | ใช้เฉพาะ peer growth ใกล้เคียง (CRM 10.3%, INTU 9.0%): ~14.5x → $385 | อธิบายได้ ~1/3 ของ gap |
| Peer multiples เองอาจ de-rate ต่อ (software AI-fear ลบ ~$1T — [iTiger](https://www.itiger.com/news/1147642448)) | peer **overstate** | ทดสอบเชิงตัวเลขไม่ได้ | Open Item |
| AI-substitution ใน creative tools ตรงกว่าใน CRM/payroll/tax → ADBE ควรมี discount | peer **overstate** | ตลาดให้ 0.56× peer · Canva/Figma โต 30–43% (§3) | สมเหตุบางส่วน |
| DCF growth 9%→3.5% (CAGR 5.9%) ต่ำกว่าที่ peer multiple ฝังไว้ | DCF **understate** | Bull path (ARR ~10%, margin 36%) = $344 · margin 37% = $325 | แม้ bull ก็ไม่ถึง $429 → peer P/E ฝัง growth >10% ระยะยาว ซึ่ง ADBE ไม่มีหลักฐานรองรับ |
| DCF ใช้ GAAP EBIT (หัก SBC + amortization) vs peer non-GAAP P/E | basis ต่าง | GAAP-basis proxy × 16x = $319 ≈ DCF | **อธิบาย gap ได้เกือบทั้งหมดเมื่อเทียบบน basis เดียวกัน** (ข้อจำกัด: peer ไม่ได้แปลงเป็น GAAP) |
| EV/EBITDA median $604 | peer **overstate** | peers op margin 12–29% → EBITDA ฐานเล็ก ทำ multiple สูง (NOW 33x, WDAY 30x) | ไม่ใช้ median · peer min $344 |

**สรุป:** DCF $308 อยู่ **ระหว่าง** ADBE 10Y-low P/E ($201) กับ peer-min multiples ($344–385) และ ≈ GAAP-basis peer P/E ($319) → DCF ไม่ aggressive · ใช้ DCF เป็น FV (ตามประเภทธุรกิจ) — multiples ชี้ upside เพิ่มถ้า sector ไม่ de-rate ต่อ (ไม่นับใน FV)

---

## 3. Economic Moat [CFA L2: Industry Analysis — Economic Moat]

| แหล่ง Moat | เดิม (พ.ค.) | ตอนนี้ | หลักฐาน |
|---|---|---|---|
| Switching costs (pro workflow, .PSD/.AI/.PDF, enterprise) | ★★★★★ | ★★★★☆ | BP&C subscription +15.6%, CMP +13.0% Q3 (10-Q) — ฐานเดิมยังโต · แต่ AI ลด learning curve (HSBC: ArtCraft open-source clone 7 apps — [TIKR](https://www.tikr.com/blog/hsbc-downgrades-adobe-adbe-stock-ai-disruption-risks)) |
| Intangibles (brand, Acrobat/PDF, Firefly commercially-safe) | ★★★★★ | ★★★★☆ | Document Cloud แข็งแรงสุด · Adobe Stock หดเร็วกว่าคาด (mgmt Q1: ARR ex-Stock 11.2% vs 10.9% — [MarketBeat](https://www.marketbeat.com/instant-alerts/adobe-q1-earnings-call-highlights-2026-03-12)) = **gen-AI แทนที่ได้จริงใน stock content** |
| Network effects (file formats, collaboration) | ★★★☆☆ | ★★★☆☆ | Figma ครอง UI/UX collaboration (Q3 rev $391.4M +43%; FY26 guide $1.497–1.499B — [Figma Q3 PR](https://s206.q4cdn.com/973901332/files/content_files/Q3_26-Figma-Press-Release.pdf)) |
| Scale (R&D, distribution, >1B MAU) | ★★★★☆ | ★★★★☆ | MAU >1B (Q3 — [Constellation](https://www.constellationr.com/insights/news/adobe-reports-solid-q3-tops-1-billion-monthly-active-users)) · ROIC 57.2% ขึ้นจาก 36.8% FY22 (SA ratios) |

**ระดับ Moat: Wide → Narrow (ปรับลง 1 ขั้น — ความยั่งยืน 10–20 ปี)**
- **แคบลงจริงที่ขอบ:** entry/SMB (Canva ARR ~$4B, +30%+ — William Blair via [Parameter](https://parameter.io/william-blair-cuts-adobe-adbe-rating-amid-rising-ai-competition-concerns)), UI/UX (Figma), stock content (gen-AI แทน — mgmt ยืนยันเอง), image generation (Midjourney/OpenAI — ไม่มีตัวเลข revenue ที่ verify ได้ → ไม่ใช้เป็นหลักฐานเชิงตัวเลข)
- **ยังกว้างที่แกน:** pro creative + Acrobat/Document + enterprise DX — revenue เร่ง 12.0 → 12.7 → 12.9%, GM 88.7%, ROIC 57%
- ขนาดเทียบ: Figma ~$1.5B + Canva ~$4B ≈ 20% ของ ADBE ARR $27.5B แต่โตเร็วกว่า 3–4 เท่า → share ที่ขอบ **Losing**
- ใช้ terminal RONIC 25% (ไม่ใช่ 57%) ให้สอดคล้องกับ Narrow moat

---

## 4. Financial Quality [CFA L1: Financial Reporting — DuPont Decomposition]

| Metric | ค่า | Source |
|---|---|---|
| ROE (DuPont) | 28.0% net margin × 0.866 asset turnover × 2.55 equity multiplier = **61.9%** | XBRL: NI TTM $7,284M / rev $25,970M / assets $29,981M / equity $11,764M (Atlas B/C) |
| ROIC vs WACC | 57.2% vs 10.10% → spread +47pp | SA (Atlas E) / Atlas F |
| Debt/Equity | 0.54 (book) · Net debt/EBITDA 0.07x | Atlas E |
| Interest coverage | **35.7x** = EBIT TTM $9,271M ÷ interest TTM $260M (263 − 197 + 194) | XBRL `InterestExpenseNonoperating` (Emma คำนวณ — Atlas เดิม N/A) |
| FCF yield | 11.37% (reported) · FCF − SBC yield 9.1% ($8,521M ÷ $93,136M) | Atlas D |
| Revenue CAGR | 5Y 13.1% (FY20–25) · 3Y 10.5% | Atlas B |

---

## 5. Peer Comparison [CFA L2: Equity Valuation — Relative Valuation]

| Company | Ticker | Fwd P/E | EV/EBITDA | ROE | ROIC | Rev Growth (3Y fcst) | Gross Margin | Moat |
|---|---|---|---|---|---|---|---|---|
| Adobe | **ADBE** | **8.91x** | **9.51x** | **61.9%** | **57.2%** | **9.6%** (TTM 12.0%) | **89.25%** | **Narrow (จาก Wide)** |
| Salesforce | CRM | 14.57x | 16.03x | 19.38% | 10.96% | 10.3% | 77.28% | Wide |
| Intuit | INTU | 14.34x | 13.50x | 23.60% | 22.89% | 9.0% | 80.98% | Wide |
| Autodesk | ADSK | 20.13x | 23.64x | 53.85% | 57.64% | 12.4% | 92.50% | Wide |
| Workday | WDAY | 15.99x | 29.54x | 16.01% | 18.35% | 10.9% | 75.80% | Narrow+ |
| ServiceNow | NOW | 22.46x | 33.17x | 11.85% | 8.47% | 19.7% | 73.08% | Wide |
| **Sector Median** | — | 15.99x | 23.64x | 19.38% | 18.35% | 10.9% | 77.28% | |
| **ADBE vs Median** | — | **Discount −44%** | **Discount −60%** | +42.5pp | +38.9pp | −1.3pp | +12.0pp | |

Source: [StockAnalysis statistics](https://stockanalysis.com/stocks/adbe/statistics/) ต่อ ticker (Atlas G) · Moat ของ peer = Emma judgment
**สรุป:** ADBE ถูกกว่า median 44–60% ทั้งที่คุณภาพ (ROIC/margin) สูงสุดในกลุ่มและ growth ต่างแค่ ~1pp → discount สะท้อนความกลัว "terminal decline" เฉพาะ ADBE — สมเหตุบางส่วน (moat แคบลงที่ขอบ) แต่ขนาด discount เกินกว่าที่ตัวเลขรายงานรองรับ

---

## 6. 🏢 Business Deep Dive [CFA L2: Industry Analysis]

> **How does Adobe make money?**
> - ขายสมาชิกรายเดือน/รายปีของโปรแกรมแต่งภาพ วิดีโอ และออกแบบ (Photoshop, Premiere, Illustrator) ให้มืออาชีพและครีเอเตอร์
> - ขายสมาชิก Acrobat ให้คนทำงานและบริษัท สำหรับเปิด แก้ เซ็น PDF
> - ขายซอฟต์แวร์ให้บริษัทใหญ่ใช้ทำการตลาดออนไลน์ วัดผลเว็บไซต์ และจัดการคอนเทนต์ (Experience Cloud, Semrush)
> - เก็บเงินเพิ่มจากฟีเจอร์ AI (Firefly) ผ่าน credit และแพ็กเกจที่แพงขึ้น
> - รายได้ 97% เป็นค่าสมาชิกต่อเนื่อง (10-Q 9M FY26) → เงินเข้าสม่ำเสมอทุกไตรมาส

### Porter's Five Forces [CFA L2: Industry Analysis — Porter's Five Forces]
| Force | ระดับ | เหตุผล |
|---|---|---|
| Supplier Power | Low → Med | cloud/GPU (AI inference) ต้นทุนขึ้น — Q3 GM −57bp YoY (XBRL) แต่ยังเป็นส่วนน้อยของต้นทุน |
| Buyer Power | Med | ลูกค้ากระจาย (ไม่มีลูกค้า ≥10%) แต่ทางเลือกราคาถูก/ฟรีเพิ่ม (Canva, clone) กดอำนาจขึ้นราคา (Citi: lapping price increases −50bp) |
| New Entrants | **High** | AI auto-coding ลดต้นทุนสร้าง creative app (ArtCraft clone ใน 1 เดือน — HSBC) · gen-AI image/video native |
| Substitutes | **High** | gen-AI แทน stock content (mgmt ยืนยัน) และงานออกแบบระดับ entry |
| Rivalry | Med-High | Canva (entry), Figma (UI/UX), Microsoft/Google (document/AI) แต่ pro tier ยังไม่มีคู่แข่งครบวงจร |

**Industry Attractiveness: Medium** (เดิม High) — margin อุตสาหกรรมยังสูงแต่ barrier ลดลงจาก AI

### Market Share Trend
- 3 ปี: **DATA NOT AVAILABLE** (Atlas K — ไม่มีแหล่งที่มี methodology) · เชิงคุณภาพ: **Losing ที่ entry/UI-UX/stock · Stable ที่ pro + document** (ADBE revenue +10–13%/ปี FY22–TTM vs Canva +30%+, Figma +42–43%)

### Competitor Profiles [CFA L2: Industry Analysis — Competitive Positioning]
**Salesforce (CRM)**
- **เก่งอะไร:** CRM ecosystem + Agentforce, enterprise distribution
- **ไม่เก่งอะไร:** ROIC 11% (goodwill จาก M&A สูง)
- **Threat Level ต่อ ADBE:** 🟡 Medium — แข่งตรงใน marketing cloud (Digital Experience ~25% ของ ADBE FY25)

**Intuit (INTU)**
- **เก่งอะไร:** tax/SMB accounting lock-in
- **ไม่เก่งอะไร:** ไม่มี creative offering
- **Threat Level ต่อ ADBE:** 🟢 Low — คนละตลาด (peer ด้าน valuation เท่านั้น)

**Autodesk (ADSK)**
- **เก่งอะไร:** CAD/AEC standard, GM 92.5%
- **ไม่เก่งอะไร:** growth พึ่ง billing-model transition
- **Threat Level ต่อ ADBE:** 🟢 Low — คนละ vertical (3D/engineering design)

**Workday (WDAY)**
- **เก่งอะไร:** HCM/finance สำหรับ enterprise
- **ไม่เก่งอะไร:** GAAP op margin 12%
- **Threat Level ต่อ ADBE:** 🟢 Low — ไม่ทับซ้อนผลิตภัณฑ์

**ServiceNow (NOW)**
- **เก่งอะไร:** workflow platform + AI agents, growth 19.7%
- **ไม่เก่งอะไร:** ROIC 8.5%, valuation สูงกว่ากลุ่ม
- **Threat Level ต่อ ADBE:** 🟡 Medium-Low — แย่ง IT budget สำหรับ AI (Wells CIO survey: ADBE "เสีย budget share" — Atlas §3)

**Figma (FIG — reference)**
- **เก่งอะไร:** collaborative UI/UX, Q3 rev +43%
- **ไม่เก่งอะไร:** ยังขาดทุน (Q3 net loss $81.3M — [NewsBytes](https://www.newsbytesapp.com/news/business/figma-posts-strong-q3-revenue-doubles-expected-profit-shares-slip/tldr)), AI cost กด margin
- **Threat Level ต่อ ADBE:** 🔴 High ใน UI/UX และกำลังขยายเข้า creative

**Canva (private)**
- **เก่งอะไร:** entry/SMB design, ARR ~$4B +30%+
- **ไม่เก่งอะไร:** pro-grade tooling
- **Threat Level ต่อ ADBE:** 🔴 High ใน SMB/entry (ตรงกับ Citi SMB claim)

### Customer Concentration
- ไม่มีลูกค้า ≥10% ที่เปิดเผย (Atlas J) · ฐาน >1B MAU → concentration ต่ำ · **ไม่ flag**

### Geography Revenue Breakdown (Atlas K — 10-K FY25 / 10-Q Q3 FY26)
| ภูมิภาค | % Revenue (9M FY26) | YoY 9M FY26 |
|---|---|---|
| Americas (US = 52.7% ของ FY25) | 58.7% | +10.9% |
| EMEA | 27.3% | +16.7% |
| APAC (รวม China — ไม่เปิดเผยแยก) | 14.0% | +11.6% |

**Geopolitical Risk: Low** — China < 14% (APAC ทั้งก้อน) · FX: cc growth Q3 12% vs reported 13%

**Unit Economics: N/A** — Value bucket (section ใช้เฉพาะ Growth bucket) · อ้างอิง: Rule of 40 = 12.0% + FCF−SBC margin 32.8% = 44.8% · NRR ไม่เปิดเผย

---

## 7. Citi Thesis Verdict — Fundamental Deterioration หรือ AI-Fear Sentiment?

| ตัวชี้วัด (SEC) | ทิศทาง | ตีความ |
|---|---|---|
| Revenue YoY Q1→Q3 FY26: 12.0% → 12.7% → 12.9% (organic ~12%) | ⬆️ เร่ง | lagging — ไม่เสื่อม |
| GAAP op margin Q3 34.8% vs 36.3% Q3 FY25 · GM 88.71% vs 89.28% | ⬇️ −1.5pp / −57bp | **เสื่อมเล็กน้อยจริง** (AI cost + Semrush mix แยกไม่ได้) |
| GAAP EPS Q3 $4.62 vs $4.18 (+10.5%) · FCF TTM $10.6B | ⬆️ | ไม่เสื่อม (ช่วยด้วย buyback) |
| Total ARR: Q1 $26.06B ([10-Q Q1](https://www.sec.gov/Archives/edgar/data/796343/000079634326000056/adbe-20260227.htm)) → Q2 $27.10B (รวม Semrush ~$0.48B) → Q3 $27.50B · NNARR Q1 ~$0.40B / Q2 organic ~$0.56B / Q3 **$0.40B** | ⬇️ | **leading — ชะลอจริง** |
| ARR ฐาน FY25 (Atlas flag): Q1 $26.06B − revalued $25.66B = Q1 NNARR $0.40B (สมเหตุ) vs ฐาน $25.20B → Q1 NNARR $0.86B ซึ่งผิดฤดูกาล → **ยืนยันฐาน revalued $25.66B** → Q4 ต้อง ~$0.78B (1.95× Q3) vs Q4 FY25 $0.93B ($24.73B → $25.66B) = **−16% YoY แม้ทำได้ตาม target** | ⬇️ | leading — ชะลอ |
| RPO Q3 $22.16B +8.4% YoY vs revenue +12.9% (XBRL; Q3 FY25 $20.44B) | ⬇️ | backlog โตช้ากว่า revenue = **leading ชะลอ** |
| Adobe Stock หดเร็วกว่าคาด (mgmt Q1 call) | ⬇️ | **substitution จริง** (ส่วนเล็ก ~0.3pp ของ ARR growth) |

**Verdict (Emma): "Partial fundamental deceleration, priced as structural impairment"**
1. **ไม่ใช่ sentiment ล้วนแบบ GOOGL 2025** — Google ไม่มี leading metric ลด แต่ ADBE มี leading indicators 3 ตัวชะลอจริง (NNARR, RPO growth, GM) + substitution ที่ mgmt ยืนยันเอง (Stock) → forecast ของ Citi (FY27 ARR 5.3%) **เป็นไปได้ ไม่ใช่เกินจริง**
2. **แต่ยังไม่ใช่ deterioration ใน P&L** — revenue เร่ง, margin ลดแค่ 1.5pp, EPS/FCF โต → ส่วนนี้คล้าย META Q3 2025 (ตัวเลขดี หุ้นลงเพราะ narrative/cost)
3. **ราคาตลาด price Citi-case ไปแล้วเต็มๆ:** Citi growth + Citi margin + terminal RONIC = WACC (ไม่มีมูลค่าจากการเติบโตระยะยาว) = **$228.74 ≈ ราคา $239.30** — ตลาดไม่ได้ให้ราคาแค่ "ชะลอ" แต่ให้ "ชะลอ + moat หมดในระยะยาว"
4. **Citi PT $207 = 7.5x × EPS ที่ตัด ~17%** (Atlas §2) — ใช้ multiple ต่ำสุดในทศวรรษ ไม่ใช่ DCF · DCF ของ Citi-scenario (RONIC 25%) = $254
5. **เสนอ Bear Discount Classification:** NNARR ชะลอจาก freemium/MAU push + Firefly pricing = *Temporary/ambiguous* · Stock substitution + entry-tier share loss = *Structural (ส่วนเล็ก)* — ยังไม่มีหลักฐาน structural ใน pro/document core
6. **จุดพิสูจน์: 9 ธ.ค. 2026 (FY27 guide)** — ARR growth guide ≤6% = Citi ถูก (FV → ~$254 หรือต่ำกว่า) · ≥8.5% = sentiment overshoot

---

## 8. Market-Implied Sanity Check (Gap-Closing) [CFA L2: Equity Valuation — Reverse DCF]
*(|MOS| 28.9% < 35% → ไม่บังคับตามกฎ แต่ทำตามคำสั่ง Charlie)* · ตลาด fwd P/E 8.91x (SA) / 8.7x บน FY27 $27.43

| ตัวแปร (แก้ทีละตัว) | ค่าที่ใช้ | ค่าที่ปิด gap ($239.30) | ช่วงที่เป็นไปได้ + source | อยู่ในช่วง? |
|---|---|---|---|---|
| TGR | 3.0% | **−6.1%** (หดถาวรหลัง FY36) | 2–3.5% (ทีม TGR cap; nominal GDP) | ❌ |
| EBIT margin (ทุกปี) | 34.5–35% | **27.3%** | ADBE FY21–TTM 31.3–36.8% (XBRL) · peers GAAP op margin 12–29%, INTU 28.8%, ADSK 28.1% (SA) | ⚠️ **ต่ำกว่าประวัติ ADBE แต่อยู่ในช่วง peer** |
| Margin ครึ่งหลัง (FY32+) | 35% | 24.4% | เหมือนข้างบน | ❌ (ต่ำกว่า INTU/ADSK) |
| WACC | 10.10% | **12.12%** | 8.6% (external) – 10.62% (ERP-consistent) — Atlas F | ❌ |
| Revenue CAGR 10y | 5.89% (FY27 9.0%) | **2.56%** (FY27 3.9%) | Citi FY27 ARR 5.3% (ต่ำสุดของ Street) – consensus FY27 rev +9.1% ([SA](https://stockanalysis.com/stocks/adbe/forecast/)) | ❌ (ต่ำกว่า Citi) |
| **ARR-decel scenario รวม: Citi path (growth 6%→3%, margin 33.5%) + terminal RONIC = WACC** | — | **$228.74** | growth/margin อิง Citi note (Atlas §2) + RONIC = WACC = no-moat terminal | ✅ **ปิด gap ได้** |
| (Citi path อย่างเดียว / + WACC 10.62%) | — | $254.19 / $237.15 | | เกือบปิด |

**ตีความ:**
- **ไม่มีตัวแปรเดี่ยวใดปิด gap ภายในช่วงของ ADBE เอง** — ยกเว้น margin ที่ต้องลงสู่ระดับ peer (27%) ≈ GM −70bp/ปี ต่อเนื่อง ~10 ปี + S&M เพิ่ม · ทำไม 35% น่าเชื่อกว่า: FY26 guide ~35%, GM 88.7% สูงกว่า peer median 77% (โครงสร้างต้นทุนต่าง), op margin ไม่เคยต่ำกว่า 31% ใน FY20–TTM · **ทิศตรงข้าม:** ถ้า AI ทำให้ pricing power หาย margin เข้าหา peer ได้ — นี่คือ **ความเปราะหลักของโมเดล** (ส่งให้ Quinn/Bear)
- **Scenario ARR-decel ที่ plausible ปิด gap ได้** → ตลาดกำลัง price "Citi ถูก + moat หมดหลัง 10 ปี" · MOS +28.9% ของ Emma = เดิมพันว่า (ก) ARR ไม่ชะลอถึง ~5% **หรือ** (ข) ADBE ยังได้ RONIC > WACC ระยะยาว · ถ้าพลาดทั้งสอง MOS ≈ 0
- **ผล: "โมเดลเปราะต่อ scenario รวม" ไม่ใช่ "ตลาด mispriced ชัดเจน"** — ไม่เปลี่ยน recommendation อัตโนมัติ
- Historical context (ไม่ใช่เกณฑ์): fwd P/E 8.9x vs 10Y avg ~30x, low 7.5x (TIKR)

---

## 9. Judgment-Call Sensitivity (VS2 1.6) [CFA L2: Equity Valuation — Sensitivity Analysis]
*Blended FV ยังไม่มี (Quinn/Bear ยังไม่ส่ง) → แสดง Δ% ของ Emma FV $308.39 · ผลต่อ Blended ≈ Δ × 0.40 — Charlie คำนวณใหม่เมื่อมี Blended*

| # | Judgment call | ค่าที่ใช้ | ทางเลือก | FV | Δ% Emma FV | Source รองรับค่าที่ใช้ |
|---|---|---|---|---|---|---|
| 1 | WACC | 10.10% | external 8.6% (valueinvesting.io) | $391.78 | **+27.0% 🚩** | Rf: Treasury + Yahoo ^TNX · ERP: Damodaran · beta: Yahoo + SA raw 1.38, Damodaran bottom-up (≥2 ✓) — แหล่ง 8.6% ใช้ beta 0.79 ขัดกับ beta ที่วัดได้ |
| 1b | WACC | 10.10% | Blume 9.98% / bottom-up 10.23% / ERP-consistent 10.62% | $313.75 / $302.79 / $287.12 | +1.7% / −1.8% / −6.9% | Atlas F |
| 2 | Tax | 22.6% | 18% (FY25) / 21.5% (TTM) | $327.12 / $312.87 | +6.1% / +1.5% | XBRL 9M FY26 |
| 3 | TGR | 3.0% | 2.5% / 3.5% | $300.57 / $317.37 | −2.5% / +2.9% | ทีม cap |
| 4 | Terminal RONIC | 25% | = WACC 10.1% / 40% | $276.39 / $316.53 | −10.4% / +2.6% | ROIC 57.2% (SA) + moat Narrow |
| 5 | Deferred revenue | ไม่นับ | นับ benefit | $317.42 | +2.9% | DCF Cash Flow Consistency Rule |
| 6 | Tuck-in M&A | 2.0% rev | 0% / 3.3% (6y avg) | $319.95 / $300.88 | +3.7% / −2.4% | XBRL acquisitions |
| 7 | Steady EBIT margin | 35% | 33% / 37% | $291.65 / $325.13 | −5.4% / +5.4% | FY26 guide ~35% + XBRL history |
| 8 | Explicit length | 10y | 5y + 5y fade (g/RONIC) | $298.74 | −3.1% | Atlas locked 10y |
| 9 | Revenue path | base (FY27 9%) | Citi growth only / Citi growth + margin | $265.19 / $254.19 | −14.0% / **−17.6% 🚩** | consensus FY27 +9.1% (SA) + company FY26 ARR target 10.2% (8-K) + organic ARR ~9.3% (Atlas) (≥2 ✓) |
| 10 | Shares | 391.5M | 389.2M (cover 9-18) | $310.22 | +0.6% | Atlas |
| 11 | Excess cash | ทั้งหมด | กัน 2% rev | $307.07 | −0.4% | Atlas bridge |
| 12 | Debt value | carrying $6.36B | fair value $6.03B | $309.24 | +0.3% | 10-Q |

**Flags >15%:** (#1) WACC external 8.6% → +27.0% — ค่าที่ใช้ (10.10%) มี source ≥2 ✓ · (#9) Citi path + margin → −17.6% — ค่าที่ใช้มี source ≥2 ✓ · ทั้งสองต้องระบุใน ⚙️ Behind the Scenes · **Pre-registration: ใช้ค่าที่ล็อกทุกจุด ไม่มีการเปลี่ยน** (tax 22.6% อยู่ในเมนูที่ Atlas ให้เลือก)

---

## 10. VS2 1.4 — Forward Value ปีที่ 5 (FY31)

| ปี | EV_t ($M) | Net debt_t | FCFF | Buyback $ | Shares (M) | V/หุ้น |
|---|---|---|---|---|---|---|
| 1 (FY27) | 125,956 | −2,764 | 7,772 | 4,255 | 379.0 | $339.66 |
| 2 | 130,386 | −6,530 | 8,292 | 4,526 | 366.8 | $373.22 |
| 3 | 134,662 | −10,620 | 8,893 | 4,803 | 355.1 | $409.12 |
| 4 | 138,908 | −14,890 | 9,355 | 5,084 | 343.7 | $447.42 |
| 5 (FY31) | 143,145 | −19,313 | 9,793 | 5,371 | 332.7 | **$488.24** |

- สมมติ: net dilution −3.2%/ปี (FY22→25, XBRL diluted shares) ซื้อคืนที่ intrinsic value (value-neutral) · after-tax interest 5% × (1 − 22.6%) บน net debt บวกเท่านั้น · **ไม่คิดดอกเบี้ยรับบน net cash ที่สะสม (conservative — flag)** · non-operating assets: ไม่มีนอกจาก cash
- **Emma FV₅ = $488.24** → ผลตอบแทนคาด = (488.24 ÷ 239.30)^(1/5) − 1 = **+15.3%/ปี**
- Alt (buyback 88% ของ FCFF ที่ราคาตลาดโต 9.7%/ปี — accretive): FV₅ $549.09 → +18.1%/ปี (แสดงเพื่อทราบ ไม่ใช่ base)
- **Consistency check:** Equity₅ $162,458M + FV ของ buyback สะสม $29,084M = $191,542M vs Equity₀ $120,736M × 1.101⁵ = $195,332M → ห่าง **−1.9%** (< 10% ✓; ส่วนต่าง = ดอกเบี้ยรับที่ไม่นับ)
- **S&P 500 expected return:** ~**9.7%/ปี** = Damodaran implied ERP 4.41% + T-bond 5.29% ที่ Damodaran ใช้ (Atlas F — [Damodaran](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm)) → ADBE (Emma) เหนือกว่า ~5.6pp/ปี
- **Blended FV₅:** รอ Quinn/Bear — Charlie คำนวณ 40/30/30

---

## 11. ESG Risk Scorecard [CFA L2-3: ESG Investing — ESG Materiality Analysis]

| Dimension | Score (1–10) | Key Issues |
|---|---|---|
| Environmental | 8/10 | asset-light (capex 0.8% rev); AI inference energy เพิ่ม (moderate) · Sustainalytics/FactSet E component ~1.9–2.9 (ต่ำ) |
| Social | 6/10 | creator backlash ต่อ gen-AI/AI training data; consumer protection — DOJ/FTC ROSCA case (early termination fee) **settle มี.ค. 2026 $75M** ([ARY/Reuters](https://arynews.tv/adobe-settles-lawsuit-for-75-million-payment); อีกแหล่งรายงาน $150M — [HotHardware](https://hothardware.com/news/adobe-150-million-settle-lawsuit-deceptive-subscription-fees), ยังไม่ verify) |
| Governance | 6/10 (เดิม 7.5–8) | **leadership vacuum:** CEO ใหม่ (Chakravarthy) มีผล 1 ธ.ค. 2026, CFO = interim (Steve Day — 8-K Q3), Digital Media head ว่าง (Atlas §2) · ตรงกับ FY27 guide 9 ธ.ค. · buyback discipline ดี |
| **Overall ESG** | **6.7/10** | |

**ESG Rating: Low-Medium Risk** — third-party: Sustainalytics total ESG risk ~13.1 (Yahoo, ไม่ระบุปี) / 13.32 (Saxo/FactSet, 2026-07-17) = Low risk, rank 53/961 Software & Services ([Sustainalytics](https://sustainalytics.com/esg-rating/adobe-inc/1007902567), [Yahoo](https://finance.yahoo.com/quote/ADBE/sustainability), [Saxo](https://www.home.saxo/de-ch/markets/stocks/adbe-xnas)) · MSCI: **N/A — หาไม่ได้** (แหล่งเดียวอ้าง AAA ไม่ verify)

### Material ESG Risks (กระทบ Valuation)
1. **Leadership transition ตรงกับ "hard reset" guide** — risk ที่ FY27 guide ถูกตั้งต่ำแบบ kitchen-sink → **−2%** FV
2. **Creator backlash / AI IP** — กระทบ pro-user retention ที่เป็นแกน moat → **−1%**
3. **Consumer protection (subscription practice)** — settled แล้ว · ความเสี่ยงที่เหลือ: เงื่อนไขยกเลิกผ่อนลง → churn สูงขึ้นเล็กน้อย → **−0.5%**
- รวม ESG impact ≈ **−3.5%** → ESG-adj Emma FV ≈ **$297.6**

---

## 12. Investment Thesis & Recommendation [CFA L3: Investment Thesis & Portfolio Construction]

**Emma FV $308.39 · MOS +28.9% · Value gate: MOS ✅ (≥15%) · Conviction 6.5 ❌ (<7.0)**

- **Bull:** ราคา = no-growth floor × 1.33 · ROIC 57% · revenue เร่ง · FCF yield 11% + buyback ลดหุ้น 6.7%/ปี · ตลาด price Citi-case + no-moat แล้ว → asymmetric ถ้า FY27 guide ARR ≥ 8%
- **Bear:** leading indicators 3 ตัวชะลอจริง · moat แคบลงที่ขอบ (Wide → Narrow) · leadership vacuum · margin คือความเปราะหลัก (27% ปิด gap)
- **Recommendation (Emma): HOLD position เดิม — ไม่ add** (conviction < 7.0 + regime TC ห้ามเพิ่ม) · **ไม่ trim** (MOS บวกแข็ง, DCF Citi-case $254 ยังเหนือราคา)

**Reference prices (Emma FV เดี่ยว — Charlie ปรับตาม Blended):**
| ระดับ | ราคา | เหตุผล |
|---|---|---|
| Add zone (เมื่อ conv ≥ 7.0 + regime อนุญาต) | ≤ $268 | MOS ≥ 15% บน Emma FV ($308.39 ÷ 1.15) |
| Deep value | ≤ $229 | ≈ Citi + RONIC = WACC scenario |
| เริ่ม trim | ≥ $293 | 0.95 × FV |
| Trim/Exit | ≥ $308 | MOS ≤ 0 |
| Stop เดิม $185 | คงไว้ | ≈ no-growth floor $180 / structural-decline scenario $176.71 |

**Bull Flip (→ add):** FY27 ARR guide ≥ 8.5% · Q4 NNARR ≥ $0.78B · GM กลับ ≥ 89% · แต่งตั้ง CFO ถาวร
**Bear Flip (→ trim/exit):** FY27 ARR guide ≤ 6% · RPO YoY < revenue YoY อีก 2 ไตรมาส + RPO growth < 6% · GAAP op margin < 32% · revenue growth < 8% สองไตรมาสติด
**Thesis Invalidation:** organic ARR growth < 5% FY27 **และ** GAAP op margin < 30% → moat thesis ผิด → full re-analysis
**Scenario reference:** Bull (ARR ~10%) $343.63 · Base $308.39 · Citi $254.19 · Citi + no-moat $228.74 · Structural decline (g → 1%, margin 30%, RONIC = WACC) $176.71

### Emma Conviction: **6.5/10**
```
Emma   ██████▌░░░  6.5/10 — DCF ทนทาน (ไม่มีตัวแปรเดี่ยวในช่วงของ ADBE ปิด gap) แต่ Citi-case + no-moat อธิบายราคาตลาดได้ครบ, leading indicators ชะลอจริง, binary 9 ธ.ค. + ผู้บริหารว่าง
```

---

## CFA Concepts Referenced
- FCFF DCF (NOPAT-based, 10y explicit, terminal RONIC) [CFA L2: Equity Valuation — FCFF Model]
- Reinvestment = g ÷ RONIC / Value of growth [CFA L2: Equity Valuation — Terminal Value] *(ยังไม่เรียน — การเติบโตไม่สร้างมูลค่าถ้า RONIC = WACC เพราะเงินลงทุนใหม่ได้ผลตอบแทนเท่าต้นทุนทุน)*
- Reverse DCF / Market-implied assumptions [CFA L2: Equity Valuation] *(ยังไม่เรียน — แก้สมการหาค่า assumption ที่ทำให้ DCF เท่ากับราคาตลาด)*
- Relative Valuation (P/E, EV/EBITDA, EV/EBIT) + reconciliation [CFA L2: Equity Valuation — Relative Valuation]
- Economic Moat (5 sources) + Porter's Five Forces [CFA L2: Industry Analysis]
- DuPont ROE [CFA L1: Financial Reporting — DuPont Decomposition]
- SBC / deferred revenue quality of earnings [CFA L2: Equity Valuation — FCFF Model Integrity]
- ESG Materiality [CFA L2-3: ESG Investing]
- Bull/Bear Flip Triggers [CFA L3: Investment Thesis & Portfolio Construction]

## Open Items (ส่ง Charlie / Morgan)
1. Peer multiples อาจ de-rate ต่อ — ทดสอบเชิงตัวเลขไม่ได้ (reconciliation §2)
2. US revenue 9M FY26, NRR/seats/pricing — DATA NOT AVAILABLE
3. สาเหตุ ETR ขึ้นเป็น 22.6% — ไม่ทราบจาก XBRL extract
4. **Atlas flags resolved:** AI-first ARR — ใช้ ">$500M (Q2)" ไม่ใช่ $650M (Emma 09-11 อ้างแหล่งรองที่ 8-K ไม่ยืนยัน — แก้ไข) · ARR ฐาน FY25 revalued $25.66B ยืนยันด้วย Q1 FY26 ARR $26.06B (10-Q Q1) · FY24 Figma termination fee — ไม่ได้ใช้ normalize (base เริ่มจาก FY26 guide)
5. ROSCA settlement $75M vs $150M ยังไม่ verify กับ DOJ/FTC press release
6. FV₅ ไม่นับดอกเบี้ยรับบน net cash สะสม (conservative)

## Structured Data Block (Leo)
```javascript
businessSummary: {
  oneLiner: "Adobe ขายสมาชิกโปรแกรมสร้างคอนเทนต์ (Photoshop, Premiere), Acrobat PDF และซอฟต์แวร์การตลาดให้บริษัท",
  analogy: "เหมือนร้านให้เช่าเครื่องมือช่างระดับมืออาชีพรายเดือน — ช่างเก่งใช้ไม่เปลี่ยน แต่มีร้านเครื่องมือราคาถูก/ฟรี (Canva, AI) แย่งลูกค้ามือใหม่",
  moneyFlow: [
    "ลูกค้า (ครีเอเตอร์, พนักงานออฟฟิศ, บริษัท) สมัครสมาชิกรายเดือน/รายปี",
    "Adobe เก็บค่าสมาชิก — 97% ของรายได้เป็น subscription",
    "ต้นทุนผลิตต่ำมาก (gross margin ~89%) → กำไรจากการดำเนินงาน ~35%",
    "เงินสดส่วนใหญ่ใช้ซื้อหุ้นคืน (~$9.3B/ปี) ทำให้จำนวนหุ้นลด ~7%/ปี"
  ],
  whyDifferent: "Switching cost ของ workflow มืออาชีพ + มาตรฐานไฟล์ (.PSD/.PDF) + Firefly ที่ปลอดภัยทางลิขสิทธิ์ — แต่ moat แคบลงที่ระดับ entry/UI-UX/stock content",
  simpleRisk: "AI ทำให้งานออกแบบง่ายและถูกลง ลูกค้าใหม่อาจไม่ต้องจ่ายแพงให้ Adobe — ยอด ARR ใหม่เริ่มชะลอแล้ว"
},
thesisBullets: [
  { title: "ราคาเท่า Citi-case แล้ว", why: "DCF ของสมมติฐาน Citi + ไม่มี moat ระยะยาว = $229 ≈ ราคา $239 — ตลาด price ผลร้ายไว้แล้ว" },
  { title: "ตัวเลขที่รายงานยังแข็ง", why: "Revenue เร่ง 12.0→12.9%, ROIC 57%, FCF yield 11%" },
  { title: "Leading indicators ชะลอจริง", why: "NNARR Q3 $0.40B, RPO +8.4% < revenue +12.9%, GM −57bp — ไม่ใช่ sentiment ล้วนแบบ GOOGL" },
  { title: "Moat ลดจาก Wide เป็น Narrow", why: "Canva/Figma โต 30–43% ที่ขอบตลาด, Adobe Stock ถูก gen-AI แทน" },
  { title: "9 ธ.ค. คือจุดพิสูจน์", why: "FY27 ARR guide ≤6% = Citi ถูก, ≥8.5% = ตลาด overshoot; CEO ใหม่ + CFO interim" }
],
esgBreakdown: { e: 8, s: 6, g: 6, overall: 6.7 },
customerConcentration: { noSingleCustomerDisclosed: "ไม่มีลูกค้า ≥10% ที่เปิดเผย; ฐาน >1B MAU" },
geographyRevenue: { americas: "~58.7% (9M FY26; US 52.7% FY25)", emea: "~27.3% (+16.7% YoY 9M)", apac: "~14.0% (China ไม่เปิดเผยแยก, <14%)" },
unitEconomics: null
```

## Sources & References
| ข้อมูล | แหล่งที่มา | URL / เอกสาร | วันที่ดึง |
|---|---|---|---|
| ราคา, market cap, multiples, peers | Atlas Data Package (Yahoo + StockAnalysis) | `agent_notes/atlas/2026-11-08_ADBE.md` · https://stockanalysis.com/stocks/adbe/statistics/ | 2026-11-08 |
| Revenue, EBIT, tax, SBC, D&A, amortization, acquisitions, interest, deferred rev, RPO, shares, buyback | SEC XBRL companyfacts CIK 796343 | https://data.sec.gov/api/xbrl/companyfacts/CIK0000796343.json (`scripts/adbe_2026-11-08/sec_more.py`) | 2026-11-08 |
| FY26 guide, Q3 ARR, interim CFO | 8-K Q3 FY26 Ex 99.1 | https://www.sec.gov/Archives/edgar/data/0000796343/000079634326000147/adbeex991q326.htm | 2026-11-08 |
| Q1 FY26 ARR $26.06B (+10.9%), FY26 ARR target 10.2% | 10-Q Q1 FY26 / 8-K Q1 | https://www.sec.gov/Archives/edgar/data/796343/000079634326000056/adbe-20260227.htm · https://www.sec.gov/Archives/edgar/data/796343/000079634326000048/adbeex991q126.htm | 2026-11-08 |
| Adobe Stock drag (ARR ex-stock 11.2%) | MarketBeat Q1 call | https://www.marketbeat.com/instant-alerts/adobe-q1-earnings-call-highlights-2026-03-12 | 2026-11-08 |
| Consensus FY27, Street PT | StockAnalysis forecast | https://stockanalysis.com/stocks/adbe/forecast/ | 2026-11-08 (Atlas) |
| Figma Q3 2026 rev $391.4M +43%, FY26 guide, net loss | Figma PR / NewsBytes | https://s206.q4cdn.com/973901332/files/content_files/Q3_26-Figma-Press-Release.pdf · https://www.newsbytesapp.com/news/business/figma-posts-strong-q3-revenue-doubles-expected-profit-shares-slip/tldr | 2026-11-08 |
| Canva ARR ~$4B | William Blair via Parameter | https://parameter.io/william-blair-cuts-adobe-adbe-rating-amid-rising-ai-competition-concerns | Atlas |
| ESG risk ratings | Sustainalytics / Yahoo / Saxo | https://sustainalytics.com/esg-rating/adobe-inc/1007902567 · https://finance.yahoo.com/quote/ADBE/sustainability · https://www.home.saxo/de-ch/markets/stocks/adbe-xnas | 2026-11-08 |
| ROSCA settlement | ARY (Reuters) / HotHardware | https://arynews.tv/adobe-settles-lawsuit-for-75-million-payment · https://hothardware.com/news/adobe-150-million-settle-lawsuit-deceptive-subscription-fees | 2026-11-08 |
| WACC, ERP, beta, bridge | Atlas F/C (Treasury, Damodaran, Yahoo, SA) | Atlas Data Package | 2026-11-08 |
| ADBE 10Y P/E low 7.5x, avg ~30x | TIKR | https://www.tikr.com/blog/adobe-adbe-stock-citi-sell-downgrade-hard-reset-pe-ratio | Atlas |
| HSBC ArtCraft clone | TIKR | https://www.tikr.com/blog/hsbc-downgrades-adobe-adbe-stock-ai-disruption-risks | Atlas |

## Emma's Conclusion
ADBE ไม่ใช่กรณี "AI-fear ล้วน" แบบ GOOGL — leading indicators (NNARR, RPO, GM) ชะลอจริงและ moat แคบลงที่ขอบ จึงปรับ moat เป็น Narrow และลด FV จาก $369 เป็น **$308.39** (DCF 100%, PV(TV)/EV 51%) · แต่ราคา $239.30 ได้ price สมมติฐานของ Citi **บวก** การไม่มี value creation ระยะยาวไว้ครบแล้ว ($228.74) ขณะที่ revenue/EPS/FCF ที่รายงานยังโต → **MOS +28.9%, FV₅ $488 (+15.3%/ปี vs S&P ~9.7%)** · Conviction 6.5 ต่ำกว่า Value gate 7.0 → **HOLD ไม่ add ไม่ trim** รอ FY27 guide 9 ธ.ค.

*Emma — 2026-11-08 (Re-Analysis Update, VS2) | ADBE Analysis*
