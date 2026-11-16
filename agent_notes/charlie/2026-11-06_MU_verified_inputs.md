# MU Re-Analysis — Verified Inputs (main-conversation fetch, 2026-11-06)

ตัวเลขทั้งหมดดึงใน session นี้ · หน่วย $M เว้นแต่ระบุ · Raw XBRL: `scripts/scout/2026-11-06_memory/data/cf_MU.json` (ได้จาก `fund.py`)

## แหล่งหลัก
- [S1] 10-K FY2026 (filed 2026-10-09): https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm
- [S2] 8-K Q4 FY2026 press release (2026-09-30): https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm
- [S3] Prepared remarks Q4 FY2026: https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf
- [S4] SEC XBRL companyfacts CIK 723125: https://data.sec.gov/api/xbrl/companyfacts/CIK0000723125.json
- [S5] 8-K 2026-11-05 (director retirement): https://www.sec.gov/Archives/edgar/data/723125/000110465926123389/tm2629062d1_8k.htm

## ราคา
| วันที่ | Yahoo chart | Nasdaq historical | หมายเหตุ |
|---|---|---|---|
| close 2026-11-04 | $795.23 | $795.23 | |
| close 2026-11-05 | **$656.39** | **$656.39** | −17.46% · StockAnalysis ยืนยัน previous close $656.39 |
| intraday 2026-11-06 | ~$696.40 | — | StockAnalysis $692.51 (11:28 ET) · ยังไม่ปิด ไม่ใช้เป็นฐาน |

ฐานคำนวณ = **close 11-05 $656.39** · รายงาน MOS ที่ intraday $696 เป็น sensitivity ด้วย
52W: high $1,255.00 (2026-06-25) / low $192.59 (2025-11-21) — Yahoo, StockAnalysis ตรงกัน
- https://query1.finance.yahoo.com/v8/finance/chart/MU · https://api.nasdaq.com/api/quote/MU/historical · https://stockanalysis.com/stocks/mu/

## หุ้น
- Cover 10-K: 1,131,423,212 (2026-10-02) [S1]
- Diluted guidance FQ1 FY27: ~1.15B [S2][S3] · weighted diluted FY26: 1,143M [S4]
- **ใช้ diluted 1,150M ทั้งทีม** (VS2 1.3)

## ผลประกอบการ
| | FY2024 | FY2025 | FY2026 | Q3 FY26 | Q4 FY26 |
|---|---|---|---|---|---|
| Revenue | 25,111 | 37,378 | **133,188** | 41,456 | **54,229** |
| COGS | 19,498 | 22,505 | 25,684 | 6,400 | 7,182 |
| Gross margin (GAAP) | 22% | 40% | 80.7% | — | 86.8% |
| Operating income | 1,304 | 9,770 | **99,340** | 33,318 | **43,751** |
| Net income | 778 | 8,539 | **84,969** | 28,243 | **37,701** |
| Diluted EPS GAAP | | | $74.33 | | $32.87 |
| OCF | 8,507 | 17,525 | 89,675 | | 43,973 |
| Capex gross | 8,386 | 15,857 | 30,712 | | 11,110 |
| Capex net of incentives | | | 27,367 | | 10,774 |
| Adjusted FCF (บริษัท) | | | 62,308 | | 33,199 |
| D&A | 7,780 | 8,352 | 9,503 | 2,364 | 2,641 |
| SBC | 833 | 972 | 1,333 | | |
| Tax rate | 36.4% | 11.6% | 14.8% | | 15% |

**FY2026 มี 53 สัปดาห์ · Q4 มี 14 สัปดาห์** (end date 2026-09-03 เทียบ 2025-08-28 และ Q3 end 05-28) → run-rate ของ Q4 ต้องปรับก่อน annualize
**ตรวจตัวเลขที่ CIO ให้:** Revenue $54.23B ✓ · NI $37.7B ✓ · ROE 61.4% = NI FY26 ÷ equity **ปลายงวด** ($84,969 ÷ $138,378) ✓ แต่ถ้าใช้ equity เฉลี่ยได้ 88.2%

ประวัติ 11 ปี [S4]:
| FY | Revenue | Op margin |
|---|---|---|
| 2016 | 12,399 | 1.4% |
| 2017 | 20,322 | 28.9% |
| 2018 | 30,391 | 49.3% |
| 2019 | 23,406 | 31.5% |
| 2020 | 21,435 | 14.0% |
| 2021 | 27,705 | 22.7% |
| 2022 | 30,758 | 31.5% |
| 2023 | 15,540 | −37.0% |
| 2024 | 25,111 | 5.2% |
| 2025 | 37,378 | 26.1% |
| 2026 | 133,188 | 74.6% |

ค่าเฉลี่ย op margin 10 ปีก่อน FY26 (2016–2025) = 17.36% (แก้จาก 17.6% ที่ Charlie คำนวณผิด, Atlas พบ) · capex รวม FY16–25 / OCF รวม ดูใน S4

## Segment [S1]
| BU | Rev FY26 | Rev FY25 | Op inc FY26 | Op inc FY25 | Q4 Rev | Q4 GM |
|---|---|---|---|---|---|---|
| CMBU (Cloud) | 43,090 | 13,520 | 31,225 (72%) | 6,129 | 16,300 | 83% |
| CDBU (Core DC) | 37,590 | 7,230 | 29,539 (79%) | 2,180 | 18,000 | 90% |
| MCBU (Mobile/Client) | 36,600 | 11,860 | 29,208 (80%) | 1,981 | 13,100 | 90% |
| AEBU (Auto/Embedded) | 15,890 | 4,750 | 11,217 (71%) | 557 | 6,800 | 84% |

DRAM FY26 $100,680 / NAND $31,790 [S1] · Q4: DRAM $39.8B (73%) bit +MSD, ราคา +high-teens QoQ · NAND $14.1B (26%) bit ~+10%, ราคา ~+30% QoQ [S3]
FY26 YoY: DRAM ASP ~+180%, bit +mid-20s · NAND ASP ~+200%, bit +mid-20s [S1] → **การเติบโตเกือบทั้งหมดมาจากราคา ไม่ใช่ปริมาณ**
Data center ~60% ของ revenue FY26 [S1]

## Balance sheet 2026-09-03 [S2][S3]
| รายการ | ค่า |
|---|---|
| Cash + equivalents | 38,364 |
| ST investments | 5,070 |
| LT marketable investments | 30,019 |
| รวม cash + investments + restricted | 73,480 |
| Total debt | 5,179 (current 491, LT 4,688) |
| Net cash (บริษัทรายงาน) | **68,300** |
| Customer SCA cash deposits | **12,700** (บัญชี noncurrent contract liabilities 12,895) — คืนลูกค้าในช่วงปลายสัญญา · ลงในกระแสเงินสดจัดหาเงิน ไม่อยู่ใน FCF [S3] |
| Operating lease liabilities (XBRL tag) | 2,387 |
| Total assets | 195,888 |
| Equity | 138,378 |
| PP&E net | 63,310 (FY25 46,590) |
| Inventories | 10,372 (DIO 129) |
| PP&E purchase commitments | ~4,180 |

**ประเด็นที่ VS2 1.2 ต้องตัดสิน:** net cash $68.3B รวมเงินมัดจำลูกค้า $12.7B ซึ่งต้องคืน → Atlas ระบุวิธีบันทึกใน bridge ให้ทุกคนใช้ค่าเดียวกัน

## Forward [S2][S3]
- FQ1 FY27: revenue $61.5B ±1.5 · GM non-GAAP ~86.25% · opex ~$2.06B · EPS non-GAAP $38.15 ±1.00 · ~1.15B shares · tax ~15.5%
- FY27: revenue เพิ่ม QoQ ทุกไตรมาส · FQ1 เป็น floor ของ GM ปีนี้ · ราคาขึ้นในอัตราที่ช้าลง · opex +~$2.5B
- Capex net FQ1 ~$11.5B · 1H FY27 ~$25B · 2H สูงกว่า 1H · **ไม่ได้ให้ตัวเลขทั้งปี** · เพิ่มจากแผนเดิม ส่วนใหญ่เป็น construction
- บริษัทคาด supply-demand ตึงกว่าเดิมมากใน CY2027–28 · "ไม่เห็นว่าเมื่อไหร่จะสมดุล" · industry DRAM bit โต low-20s, NAND mid-20s ใน CY27–28
- **SCA:** 26 ฉบับ · >35% ของ revenue ถึงปี 2030 (ประมาณการของบริษัท) · 3/4 มี pricing framework ส่วนใหญ่เป็น floor/ceiling · financial commitments $32B · RPO ~$150B (ที่ราคาต่ำสุด) · บริษัทอ้างว่า "แม้ที่ floor margin ก็สูงกว่า peak เดิมอย่างมีนัยสำคัญ" — **เป็นคำของ management ไม่มีตัวเลข floor เปิดเผย**
- ข้อกำหนดสัญญาบางส่วน: take-or-pay [S1]
- Capital return: เพิ่มได้ตั้งแต่ 2026-12-09 · ระยะยาวคืน 100% ของ excess cash [S3]
- Fabs: ID1 output กลาง CY27 · ID2 ปลาย CY28 · Tongluo (Taiwan) กลาง CY27 · Singapore HBM packaging ต้น CY27, NAND 2H CY28 · Japan ปลาย CY28 · New York CY30 [S3]

## Consensus (StockAnalysis, 2026-11-04/05) https://stockanalysis.com/stocks/mu/forecast/
- PT low $361 / avg $1,562 / median $1,550 / high $3,000 (49 analysts)
- FY27: revenue avg $275.5B (ช่วง $212.4–314.0B) · EPS avg $176.50 (ช่วง $161.00–214.70)
- ปีถัดไป (น่าจะ FY28, หน้าเว็บไม่ระบุชัด): revenue $320.06B (+16.2%) · EPS $207.76 (+17.7%) · **FY29 ไม่มีข้อมูล**
- Forward P/E 3.92 ที่ $692.51 (StockAnalysis)

## WACC inputs (VS2 1.1)
- Rf: ^TNX close 11-05 = 4.837% (Yahoo) — Atlas ต้องหาอีก 1 แหล่ง · Damodaran home page แสดง T-Bond 5.29% (ไม่ตรงกับตลาด ต้องตรวจ ไม่ใช้จนกว่าจะอธิบายได้)
- ERP: **4.41%** Damodaran implied ERP 2026-11-01 (T12M adjusted payout) https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm
- Raw beta: 2.48 (5Y monthly vs ^GSPC, คำนวณเอง n=60, `fund.py`) · 2.40 (StockAnalysis) → Blume จาก 2.48 = 1.99
- Bottom-up: Semiconductor unlevered 1.49 / cash-corrected 1.50, D/E 2.59%, n=66 (Damodaran **ม.ค. 2026**) https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html
- External (ต้องลง stale-rate test): valueinvesting.io WACC 10.42–10.6%, Rf 4.15% https://valueinvesting.io/MU/valuation/wacc · Tickzen 14.7% (พ.ค. 2026, beta 1.92, Rf ไม่ระบุในผลค้น) https://tickzen-flask.onrender.com/insights/is-mu-stock-a-good-buy-right-now-2026 · FMP 8.36% (input ผิดปกติ FCF ติดลบ) https://site.financialmodelingprep.com/discounted-cash-flow-model/MU

## ข่าว selloff 11-05
- S&P 500 close 7,353.73 (−4.36%), Nasdaq −5.52%, Dow −3.44% https://www.stocktitan.net/articles/stock-market-today-live-november-5-2026 · https://cappnotes.substack.com/p/closing-look-thursday-november-5
- MU −17.46% · SNDK −22% · WDC/AMD −17% · STX ~−16%; ชนวน: พรรคเดโมแครตชนะเลือกตั้งกลางเทอม 11-03, ส.ส. Ansari เรียกร้อง pause AI, นโยบายให้ data center จ่ายค่าไฟเอง https://247wallst.com/investing/2026/11/05/sandisk-slides-7-micron-and-western-digital-fall-5-as-lawmakers-call-for-ai-pause-extends-memory-rout/ · https://finance.yahoo.com/markets/article/chip-stocks-slaughtered-as-wall-street-suffers-worst-post-midterm-day-since-1896-213204256.html
- **เฉพาะ MU:** Bloomberg (11-05) รายงานว่า Fab 11E Taoyuan ($3–4.5B, output 2028) หยุดก่อสร้างเกือบทั้งหมดจากข้อพิพาทสหภาพ (ขอ 15% ของ operating profit); Taiwan ผลิต ~60% ของ DRAM MU — ความเสี่ยงการหยุดงานสำคัญกว่าตัวโรงงาน; บริษัทยังไม่ยืนยันเลิกโครงการ https://en.sedaily.com/international/2026/11/06/micron-halts-taiwan-fab-construction-over-bonus-talks · https://www.thestreet.com/technology/micron-freezes-taiwan-plant-workers-union-pay-dispute-profit-sharing · **ดังนั้น "ทั้งที่งบดี" ถูกในแง่งบ แต่มีข่าวเฉพาะตัวร่วมด้วย ไม่ใช่ sentiment ล้วน**
- 8-K 11-05: Linnie Haynesworth ไม่ลงสมัครกรรมการต่อ — ไม่ใช่สัญญาณด้านการดำเนินงาน [S5]

## ราคา memory
- TrendForce: 4Q26 conventional DRAM contract +10–15% QoQ, รวม HBM +15–20%, NAND +15–20% (30 ก.ย.) · แนวโน้มชะลอจาก ~80% ใน 2Q, ~40% ใน 3Q https://www.trendforce.com/news/2026/10/20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook/ · https://ramtrend.com/news/4603-trendforce-expects-further-dram-and-nand-contract-price-increases-in-q4
- สัญญาณอุปสงค์: ผู้บริโภคอ่อนจากต้นทุนชิ้นส่วน, NAND หยุดขึ้นหลัง 21 เดือนในรายงาน spot เดือน ต.ค. (แหล่งรอง) https://tech-insider.org/dram-record-high-nand-flat-21-months-october-2026/

## Regime indicators (2026-11-05)
- VIX close 28.18 (Yahoo ^VIX; 11-04 = 16.61, intraday 11-06 ~24.8)
- 10Y−2Y +0.38 (FRED T10Y2Y) https://fred.stlouisfed.org/series/T10Y2Y
- HY OAS 3.48% = 348 bps (FRED) https://fred.stlouisfed.org/series/BAMLH0A0HYM2
- Fed: ดู regime call 2026-11-03 · Atlas ตรวจ December FOMC probability ล่าสุด

## FV เดิม (2026-08-27, v1 ก่อน VS2)
Emma $83.35 / Quinn $781.90 / Bear $80.02 → Blended $291.92, WACC 15.63% (beta 2.21, ERP 5.0%) · Emma/Bear fade margin กลับ historical; Quinn ใช้ P/E 21x คงที่ทุก scenario
