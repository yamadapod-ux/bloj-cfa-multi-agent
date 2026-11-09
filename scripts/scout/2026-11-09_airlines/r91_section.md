
## Scout Report § Round 91 (Airlines) — 2026-11-09

**Sector mandate:** Airlines — US passenger carriers + 2 ADRs (RYAAY, CPA) ตามคำสั่ง CIO · ก่อนหน้า: R88 Hotel/Storage REIT · R89 Office REIT · R90 Memory/Storage (MU peers)
**⚠️ Coverage correction:** คำสั่งระบุว่า Airlines "ไม่เคยถูกสแกนเลย" — **ไม่ตรง:** **Round 51 (2026-09-30)** สแกน DAL/UAL/LUV/AAL (+CSX) ไปแล้ว ผล 0/5 (AAL ตาย B-Zero · LUV ตาย D ที่ Street PT +19.3%). รอบนี้จึงเป็น **pass ที่ 2** สำหรับ 4 ตัวนั้น (ไม่อยู่ใน live table/Archive/decisions.md จึงไม่ติด hard exclusion) และเป็น **ครั้งแรก** สำหรับ ALK/JBLU/ALGT/SKYW/RYAAY/CPA
**Trigger:** CIO สั่ง "Scout Round 91 — Airlines" (2026-11-09) · **scout/screen เท่านั้น ไม่ dispatch full pipeline · ไม่เรียก Atlas/Emma/Quinn/Bear**
**Portfolio state:** 5 OPEN (ADBE / NOW / CRM / REGN / ADSK) ตาม `dashboard/portfolio.js` (re-mark `de0c3cc`, close 11-06) · ไม่มี airline ในพอร์ต
**Regime:** **TRANSITIONAL-CAUTIOUS** (`agent_notes/atlas/2026-11-06_regime.md`, อายุ 3 วัน — ไม่ stale) · 2/4 RISK-ON, VIX 28.18, Fed hike odds Dec ~77–78% · Force Deploy suspended + ห้าม open position ใหม่ → ถ้ามี survivor ก็เป็นแค่ buy-list candidate
**Market:** วันนี้จันทร์ 11-09 (เวลาไทย) ตลาดสหรัฐยังไม่เปิด → ใช้ close ศุกร์ 11-06

### Step 0 — Prune
🗄️ Prune: de-listed **0** | SLA fixed **0** | live **9** (WYNN / VICI / ALLY / MMS / CRI / NBIX / BYD / WGO / CMRE)
- **Rule #1:** ไม่มี target ผ่านกำหนด — CRI 11-12 · WYNN/VICI/ALLY/NBIX/BYD 11-14 · CMRE 11-17 · MMS 11-20 · WGO 12-19. ⚠️ **WYNN/VICI (scout 09-20) ครบ 60 วันวันที่ 11-19** — ถ้ายังไม่รัน Tier 1 ภายใน target 11-14 ต้อง archive ใน prune แรกหลัง 11-19
- **Rule #2:** ไม่มีวันเทรดใหม่ตั้งแต่ prune R89 (close 11-06 เท่าเดิม) → ไม่มีตัวไหน >2× ขอบบน zone (สูงสุด NBIX $164.63 = 1.22× ของ $135) · ไม่มี formal MOS < −30%
- **Rule #3:** `decisions.md` 0 hits ทุก live ticker · OPEN ไม่เปลี่ยน

### Coverage-check + universe
| Ticker | สถานะ | การจัดการ |
|---|---|---|
| DAL, UAL, AAL, LUV | `grep -w` = 0 hits ใน `decisions.md` / `dashboard/portfolio.js` / Archive · มีอยู่ใน Scout History R51 เท่านั้น | สแกนซ้ำ (pass 2) |
| ALK, JBLU, ALGT, SKYW, RYAAY, CPA | 0 hits ทุกไฟล์ · ไม่อยู่ใน exclusion list (PODD, ZTS, NKE, MMS, SLM, CRI, NBIX, BYD, WGO, OWL) | สแกนเต็ม |
| **SAVE (Spirit)** | ⚠️ ไม่มีราคาเทรด — Chapter 11 ครั้งที่ 2 (2025-08-29), NYSE delist → OTC `FLYYQ`, common stock คาดว่าถูกยกเลิก ([ch-aviation](https://www.ch-aviation.com/news/157874-uss-spirit-to-delist-from-nyse-receives-chapter-11-nod), [CAPA](https://centreforaviation.com/news/nyse-american-to-delist-spirit-airlines-common-stock-1330502)); ข่าวปี 2026 ระบุว่าสายการบิน "collapse" ก่อน ALGT ปิดดีล ([AJC/AP](https://www.ajc.com/news/2026/05/allegiant-air-and-sun-country-complete-merger-creating-larger-budget-airline-for-travelers/)) | ตัดออก |
| **SNCY (Sun Country)** | ⚠️ ถูก Allegiant ซื้อแล้ว ปิดดีล 2026-05-13 ([Las Vegas Sun](https://lasvegassun.com/news/2026/may/13/allegiant-air-and-sun-country-complete-merger-crea/), [Washington Times/AP](https://www.washingtontimes.com/news/2026/may/13/allegiant-air-sun-country-complete-merger-creating-larger-budget/)) · Yahoo ไม่มี timestamp | ตัดออก (รวมอยู่ใน ALGT) |
| ULCC (Frontier) — เช็คเพิ่ม | $7.43 / high $8.40 = −11.5% | ไม่นับใน 10 ตัว · ตก A |

**Data sources:** ราคา + 52W high/low = **Yahoo chart API (1y daily) และ Nasdaq.com quote API** ตรงกันทุกตัว (ต่างกัน ≤$0.02) — `scripts/scout/2026-11-09_airlines/px.py` → `data/px.json`. งบการเงิน = **SEC EDGAR companyfacts** (`data.sec.gov/api/xbrl/companyfacts/CIK##########.json`) — `sec.py` / `tags.py`, 10-Q งวด 2026-09-30, TTM = FY25 + 9M26 − 9M25. RYAAY = 20-F IFRS (EUR, ปีบัญชีสิ้น มี.ค.; XBRL มีถึง FY25 = Mar-2025) + ผล H1 FY27 จาก 6-K. EURUSD 1.1228 (Yahoo, close 11-06 — แหล่งเดียว, ไม่กระทบผล). คำนวณทั้งหมดใน `calc.py`.
**WACC:** scout-level proxy ตาม Filter D (ตามขนาด): AAL/SKYW 10% · ALK 10.5% · ALGT 11.5% · JBLU 13% · RYAAY 8.5% (แสดง ±1pp) — **ไม่ใช่ VS2 §1.1** · ไม่มีผลใดที่พลิกเมื่อขยับ ±1pp
**FCF definition:** OCF − capex ทั้งหมด (รวม flight equipment / pre-delivery deposits) — airline capex ส่วนใหญ่คือเครื่องบิน ห้ามตัดออก

### Filter A — ลง ≥20% จาก 52W high (close 11-06)
| Ticker | ราคา (Yahoo / Nasdaq) | 52W high (วันที่) | % จาก high | ผล |
|---|---|---|---|---|
| DAL | $87.20 / $87.21 | $95.68 (07-02) | −8.9% | ❌ (R51: −10.6%) |
| UAL | $112.74 / $112.74 | $138.77 (06-30) | −18.8% | ❌ (R51: −18.9% — ใกล้สุดอีกครั้ง) |
| **AAL** | $13.18 / $13.18 | $18.79 (07-02) | **−29.9%** | ✅ |
| LUV | $44.45 / $44.46 | $55.11 (02-17) | −19.3% | ❌ (R51 ผ่านที่ −23.6%; ฟื้นขึ้นมา) |
| **ALK** | $38.94 / $38.945 | $60.63 (02-09) | **−35.8%** | ✅ (52W low $32.33 เมื่อ 10-22) |
| **JBLU** | $3.67 / $3.67 | $6.62 (08-04) | **−44.6%** | ✅ (52W low $2.16 เมื่อ 10-26) |
| **ALGT** | $91.97 / $91.97 | $123.63 (07-02) | **−25.6%** | ✅ |
| **SKYW** | $79.38 / $79.38 | $117.72 (08-05) | **−32.6%** | ✅ (52W low $77.68 เมื่อ 11-03) |
| **RYAAY** | $59.30 / $59.30 | $74.24 (01-05) | **−20.1%** | ✅ (borderline — 0.1pp) |
| CPA | $142.80 / $142.78 | $160.47 (06-25) | −11.0% | ❌ |

**Filter A: 6/10 ผ่าน.**

### Beaten-down reason (Filter A survivors)
| Ticker | เหตุผล | จัดกลุ่ม |
|---|---|---|
| AAL | ราคาน้ำมันเครื่องบินพุ่งตั้งแต่ ส.ค. 2026 (ทั้ง sector) ซ้อนบนงบดุลอ่อนที่สุดใน majors: ขาดทุนสุทธิ 9M26 −$580M (SEC 10-Q), equity −$4.2B | **ปนกัน** — fuel = cyclical · งบดุลเปราะ = โครงสร้าง (เหมือน R51) |
| ALK | Q3 2026 ขาดทุนสุทธิ GAAP −$147M แม้รายได้ +14% — fuel headwind ~$1.8B ทั้งปี, guide FY26 adj. EPS −$5.00 ถึง −$5.50 ([Quiver Quant](https://www.quiverquant.com/news/Alaska+Air+Reports+%24147+Million+Third-Quarter+Loss+as+Revenue+Reaches+%244.3+Billion), [FMP/BMO](https://site.financialmodelingprep.com/market-news/alaska-air-group-outperform-rating-fuel-costs)) + ต้นทุน integrate Hawaiian (D&A FY23 $451M → TTM $826M, SEC) | ✅ cyclical/temporary (fuel) — แต่ ROIC ก่อน fuel spike ก็ต่ำอยู่แล้ว (ดู C) |
| JBLU | ขาดทุนจากการดำเนินงาน **ทุกปี FY21–TTM** (SEC: op income −$80M / −$298M / −$230M / −$684M / −$368M / TTM −$609M) + หนี้ ~$8.4B, ตลาดกังวลสภาพคล่อง ([FXLeaders](https://www.fxleaders.com/news/2026/07/13/jblu-stock-slips-toward-5-50-as-jetblue-debt-concerns-overshadow-cheap-valuation-signals/)) | ❌ ใกล้ **permanent impairment** — ขาดทุนต่อเนื่อง 5 ปีก่อน fuel spike (เขียน 2 มุม: fuel = cyclical, แต่ปัญหาหลักเกิดก่อนนั้น) |
| ALGT | fuel + ต้นทุน integrate Sun Country ($18.9M ใน Q3, Sun Country ขาดทุน GAAP $4.1M, นักบิน MSP ลาออกจนต้องลด capacity ครึ่งหลัง 2026) ([Panabee](https://www.panabee.com/news/allegiant-travel-earnings-q3-2026), [finviz/PR](https://finviz.com/news/415748/allegiant-travel-company-third-quarter-2026-financial-results)) — Investor Day **12-07** | ✅ cyclical + M&A integration (temporary) |
| SKYW | ร่วง ~13% วันที่ 10-30 หลังลด guide FY26 EPS เป็น ~$10.60 (จาก ~$11) เพราะ prorate fuel และบอกว่า 2027 ใกล้เคียง 2026 (consensus เดิม $12.12) ([TIKR](https://www.tikr.com/de/blog/skywest-sinks-13-on-lower-2026-outlook-as-2027-earnings-seen-similar-to-2026)) | ✅ cyclical/sentiment (contract flying ส่วนใหญ่ไม่แบกราคาน้ำมัน — เฉพาะ prorate) |
| RYAAY | H1 FY27 PAT €2.15B −15% เพราะน้ำมันส่วนที่ไม่ hedge แพงขึ้นราว 2 เท่า + ค่าโดยสารเฉลี่ย −4%; ไม่ให้ FY27 PAT guidance ([Kalkine/6-K](https://kalkine.com/news/announcements/ryanair-h1-fy27-pat-falls-15-to-215bn), [Quartr](https://quartr.com/events/ryanair-holdings-plc-rya-q2-2027_3PZzOl6V)) | ✅ cyclical/temporary |

### Filter B-Zero — Balance sheet (SEC 10-Q 2026-09-30; RYAAY 6-K)
| Ticker | Equity | Net debt (ex-lease) | ND/EBITDA TTM (lease-adj.) | ผล |
|---|---|---|---|---|
| AAL | **−$4,224M** | $18,041M (debt $26.3B − cash+AFS $8.3B) | 5.7× (7.8×) | 🔴 **REJECT** — equity ติดลบจากขาดทุนสะสม + หนี้ยุค COVID, ไม่ใช่ buyback/recap (SEC: buyback ≈ 0 ตั้งแต่ 2021) → สาขา "operating losses" ของกฎ (เหมือน R51) |
| ALK | +$3,530M | $3,745M | **7.0×** (9.5×) — FY25 3.4× | 🟡 ผ่านต่อ — flag leverage สูงจาก EBITDA ที่ตกเพราะ fuel → ส่งต่อ E3 |
| JBLU | +$1,337M | $6,884M | **59.9×** (EBITDA TTM แค่ $115M) | 🟡 ผ่านต่อแบบมีธงแดง — equity ยังบวก แต่หดจากขาดทุน |
| ALGT | +$1,765M | $2,720M (รวม finance lease $636M) | **6.1×** | 🟡 ผ่านต่อ — flag (หนี้รับมาจาก Sun Country) |
| SKYW | +$2,810M | $1,796M | **1.9×** (2.0×) | ✅ clean |
| RYAAY | €7.0B (Mar-25, SEC 20-F) | **net cash €2.7B** (30 มิ.ย. 2026; ปลอดหนี้หลังชำระ bond €1.2B ใน พ.ค.) ([Quartr Q1 FY27](https://quartr.com/events/ryanair-holdings-plc-rya-q1-2027_3PZzAfmo)) | n/a | ✅ clean |

### Bucket
ทุกตัว = **Value bucket** (B-Legacy / D-Legacy). ALGT รายได้ TTM +26% แต่มาจากการซื้อ Sun Country ไม่ใช่ organic และไม่มี reinvestment phase ที่กด FCF โดยตั้งใจ → ไม่เข้า B-V1. ไม่มีตัวไหนเข้า Lane AI/Infra

### Filter B + C (SEC, $M)
| Ticker | FCF TTM (yield) | FCF เฉลี่ย 5Y (yield) | EV/EBITDA TTM | ROIC TTM (EBIT×0.77 ÷ (equity+ND)) vs WACC | ผล B | ผล C |
|---|---|---|---|---|---|---|
| ALK | −$434M (−9.9%) | FY21–25 $161M (3.7%) | 15.2× (EBITDA ต่ำเพราะขาดทุน) | **−3.1%** vs 10.5% | ❌ | ❌ |
| JBLU | −$1,135M (−82%) | FY21–25 −$577M | 71.9× | **−5.7%** vs 13% | ❌ | ❌ |
| ALGT | −$26M (−1.0%) | FY21–25 $34M (1.4%) | 11.7× | **3.1%** vs 11.5% (27%) | ❌ | ❌ |
| SKYW | **$199M (6.6%)** | FY21–25 $268M (8.9%) | 5.1× | **9.9%** vs 10% (99%) | ✅ (FCF yield >6%) | ✅ (≥80%; op income FY23 $104M → FY25 $618M) |
| RYAAY | — (FY26 ยังไม่อยู่ใน XBRL) | FY25 €1,864M (**6.7%** ของ mcap €27.8B) · FY23–25 avg €1,535M (5.5%) | P/E FY26 12.3× | ROE FY25 22.9% · net cash → ROIC > WACC ชัด | ✅ (FY25 FCF yield >6%) | ✅ |

**ALK / JBLU / ALGT ตายที่ B+C.** ALK ก่อน fuel spike ROIC ก็ไม่ถึง WACC (op income FY22–25 $70–570M) จึงไม่ใช่แค่ปัญหาชั่วคราว · JBLU ROIC ติดลบ 5 ปี = value trap ตามนิยาม C · ALGT ROIC 3.1% ต่ำกว่า 80% ของ WACC มาก และไม่มี trend ดีขึ้นต่อเนื่อง (op income FY23 $221M → FY24 −$240M → FY25 $37M → TTM $180M)

### Filter D + Tier 1 Quick-Screen (SKYW, RYAAY)
| Ticker | Naive FV (normalized FCF ÷ WACC ± net debt/cash) | P / naive FV | Sensitivity | Street PT | ผล |
|---|---|---|---|---|---|
| **SKYW** | FY21–25 avg FCF $268M ÷ 10% − ND $1,796M = **$23.19/หุ้น** | **3.42×** | WACC 9–11%: 2.6–4.7× · TTM FCF: 15.6× · **กรณีใจดีที่สุด** OCF − D&A (สมมติ capex = ค่าเสื่อม ไม่มี fleet growth): $70.58 = **1.12×** | $115–125 (MarketBeat/Investing.com, ก.ค. 2026 — **ก่อน guide cut 10-30, เก่า**) ([MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/SKYW/price-target/), [Investing.com](https://www.investing.com/equities/skywest-consensus-estimates)) | Tier 1 **check 2a: >1.5× → `QUICK-SCREEN SKIP`** · แม้กรณีใจดีสุดก็ >0.90× ตก D |
| **RYAAY** | FY23–25 avg FCF €1,535M ÷ 8.5% + net cash €2.7B = €20.8B vs mcap **€27.8B** ($59.30 × 526.23M ADS [ChartMill] ÷ EURUSD 1.1228) | **1.34×** | WACC 7.5–9.5%: 1.20–1.47× · 6Y non-COVID avg (FY18–20, 23–25) €1,098M: 1.78× · **กรณีใจดีสุด** FY26 PAT €2.26B แทน FCF: 0.85–1.05× (0.95× ที่ 8.5%) | ไม่ได้ดึงรอบนี้ (D ตกแล้วทุก base ที่เป็น FCF) | Tier 1 check 2a ไม่ติด (1.34× < 1.5×) แต่ **D > 0.90× → Reject lane** — log เป็น `QUICK-SCREEN SKIP` (ผ่าน A–C แล้วตกที่ Tier 1/1.5) |

**Check 3 (red-flag search):** ไม่ได้รัน — check 3 เป็น enrichment ไม่ใช่ gate และทั้ง 2 ตัวตกที่ arithmetic แล้ว
**Filter E:** ไม่ได้ประเมิน (ไม่มีตัวไหนผ่าน D) — หมายเหตุ: RYAAY น่าจะผ่าน E1 (cost leadership) + E2 (ROE ~23%, net cash) → ถ้าราคาลงถึงเกณฑ์ D จะเป็น candidate ที่ดีที่สุดใน sector

### Final routing — Round 91
| Ticker | ตกที่ | Tag |
|---|---|---|
| DAL | A (−8.9%) | reject |
| UAL | A (−18.8%) | reject |
| LUV | A (−19.3%) | reject |
| CPA | A (−11.0%) | reject |
| AAL | B-Zero (equity −$4.2B จากขาดทุนสะสม) | reject |
| JBLU | A-reason (ใกล้ permanent) + B + C (ROIC −5.7%, ขาดทุน 5 ปี) | reject |
| ALK | B + C (FCF −9.9%, ROIC −3.1%) | reject |
| ALGT | B + C (FCF ≈ 0, ROIC 3.1% vs 11.5%) | reject |
| SKYW | Tier 1 check 2a (3.42× naive FV) | `QUICK-SCREEN SKIP` |
| RYAAY | Filter D / Tier 1.5 Reject lane (1.34×) | `QUICK-SCREEN SKIP` |

**0 fast-track · 0 learning-queue · 10 reject (2 `QUICK-SCREEN SKIP`: SKYW / RYAAY)** · ไม่เพิ่ม row ใน Pending Analysis · ไม่เพิ่ม `buy_list.md`
⚠️ **`deployment_log.md` ยังไม่ได้บันทึก tag 2 ตัวนี้** — ไฟล์นั้นมีงานค้าง (Round 90) ที่ยังไม่ commit จึงไม่แตะในรอบนี้. แถวที่ต้องเพิ่มภายหลัง: `SKYW | QUICK-SCREEN SKIP (check 2a) | 3.42× naive FV` และ `RYAAY | QUICK-SCREEN SKIP (D >0.90×) | 1.34× naive FV`

### ข้อสังเกตถึง CIO / Charlie
1. **Airline ไม่เข้ากับ naive FV แบบ no-growth FCF** — capex เครื่องบินกิน OCF เกือบหมดทุกปี (SKYW FY22 FCF ติดลบ, ALK ติดลบ 3 ใน 5 ปี) → FCF ÷ WACC ต่ำกว่าราคาตลาดเกือบทุกตัว. ไม่ใช่ filter ผิด — แปลว่าผู้ถือหุ้นไม่เคยได้ FCF จริงมากพอ (sector ROIC ต่ำโดยโครงสร้าง)
2. **ตัวเดียวที่น่าตามคือ RYAAY** — net cash, ROE สูง, cost leader ในยุโรป, ปัญหาตอนนี้คือ fuel + fare. ราคาที่ D ผ่าน (≤0.80× ของ naive FV €20.8B) ≈ mcap €16.6B ≈ **$35/ADS** (−41% จากตอนนี้) — ไกลมาก. ถ้า FY26 FCF (ใน 20-F) สูงกว่า avg มาก ให้ re-screen
3. **SKYW** ถูกบน EV/EBITDA (5.1×) แต่ FCF หลัง fleet capex ต่ำ — คำถามคือ capex E175 เป็น growth capex ที่มีสัญญา capacity purchase รองรับหรือไม่ (ถ้าใช่ naive FV แบบ OCF − D&A 1.12× ใกล้ความจริงกว่า แต่ก็ยังไม่ผ่าน D)
4. **SAVE ล้ม + SNCY ถูกซื้อ** = leisure/ULCC consolidation — อาจดีต่อราคาตั๋วระยะยาว แต่ ALGT ยังไม่มี ROIC พิสูจน์ → ดู Investor Day 12-07
5. R51 กับ R91 ห่างกัน 40 วัน ผลเหมือนเดิม (AAL ตาย B-Zero ทั้งสองรอบ) — **ไม่แนะนำสแกน airline ซ้ำจนกว่า jet fuel จะลงมา หรือ RYAAY/SKYW ราคาลงอีก ≥15%**

**Target analysis date:** ไม่มี (0 candidates)

*Max — 2026-11-09 | Scout Round 91 (Airlines — 10 screened [DAL/UAL/AAL/LUV/ALK/JBLU/ALGT/SKYW/RYAAY/CPA], 0 fast-track / 0 learning-queue / 10 reject [4 A · 1 B-Zero · 3 B/C · 2 QUICK-SCREEN SKIP SKYW/RYAAY]; SAVE bankrupt/delisted, SNCY acquired by ALGT; pass 2 for DAL/UAL/AAL/LUV after R51)*
