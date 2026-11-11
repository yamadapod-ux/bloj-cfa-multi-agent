
## Scout Report § Round 92 (Leisure & Recreation) — 2026-11-11

**Sector mandate:** Leisure Facilities + Leisure Products — theme parks (FUN, PRKS) · ski resorts (MTN) · fitness clubs/franchisors (PLNT, LTH, XPOF, PTON) · golf equipment (GOLF, CALY) · bowling/location entertainment (LUCK) · toys/collectibles (HAS, JAKK, FNKO) · outdoor gear (YETI) · sporting-goods retail (ASO) · cruise-ship wellness (OSW) · ก่อนหน้า: R89 Office REIT · R90 Memory/Storage · R91 Airlines
**Coverage check (30-day window = ตั้งแต่ 2026-10-12):** `grep -w` ใน watchlist.md / decisions.md — 14/16 ticker **0 hits** ในทั้งสองไฟล์. ข้อยกเว้น: **HAS** อยู่แค่ใน near-miss list ของ R77 (−7.4%, ไม่เคยสแกนเต็ม) · **MAT** สแกนเต็มแล้วใน R77 (10-16, ตก Tier 1 2b) → **ตัดออกจากรอบนี้** (อยู่ในหน้าต่าง 30 วัน). Sub-industry ใกล้เคียงที่เคยทำ: RV & Marine/Powersports ad-hoc (10-24: WGO/PII/BC/MBUU) · Gaming & Lodging (R67, R80) · Cruise (R44b, R79) · DKS (10-27 specialty-retail ad-hoc) → ไม่ซ้ำ ticker. Auto Dealers ถูกพิจารณาก่อนแต่ตัดทิ้ง เพราะ AN/ABG ถูกดูไปแล้วใน informal scan 10-22. **สรุป: sector ใหม่จริง (ไม่ใช่ re-scout)**
**Trigger:** CIO สั่ง Scout Round 92 — sector ที่ยังไม่เคยสแกน (2026-11-11) · **scout/screen เท่านั้น — ไม่ dispatch full pipeline · ไม่เรียก Atlas/Emma/Quinn/Bear**
**Hard exclusions:** PODD/ZTS/NKE/MMS/SLM/CRI/NBIX/BYD/WGO/OWL — ไม่มีตัวไหนอยู่ใน universe · holdings (ADBE/NOW/CRM/REGN/ADSK) ไม่ซ้ำ · `decisions.md` 0 hits ทุกตัว
**Ticker hygiene:** MODG ไม่มีข้อมูลแล้ว — บริษัทกลับมาใช้ชื่อ Callaway Golf (**CALY**, SEC CIK 837465) · SEAS → **PRKS** (United Parks) · FUN = Six Flags Entertainment Corp/NEW (CIK 1999001, หลังควบรวม Cedar Fair)
**Portfolio state:** 5 OPEN (ADBE / NOW / CRM / REGN / ADSK) ตาม `dashboard/portfolio.js` (re-mark `1ca3b3f`, close 11-10)
**Regime:** **TRANSITIONAL-CAUTIOUS** (`agent_notes/atlas/2026-11-06_regime.md`, อายุ 5 วัน — ไม่ stale) → Force Deploy suspended + ห้าม open position ใหม่ → survivor (ถ้ามี) เป็นแค่ buy-list candidate
**Data sources:** ราคา + 52W high = **Yahoo chart API** (`px.py`, `px2.py` → `data/px*.json`) cross-check **stockanalysis.com** ([FUN](https://stockanalysis.com/stocks/fun/) · [PLNT](https://stockanalysis.com/stocks/plnt/) · [XPOF](https://stockanalysis.com/stocks/xpof/) · [PTON](https://stockanalysis.com/stocks/pton/) · [GOLF](https://stockanalysis.com/stocks/golf/) · [LUCK](https://stockanalysis.com/stocks/luck/) · [YETI](https://stockanalysis.com/stocks/yeti/) · [PRKS](https://stockanalysis.com/stocks/prks/)) — **ตรงกันทุกตัวที่เช็ค (Δ 0%)**. Nasdaq.com API ตอบ 403 รอบนี้. Filter-A fail ที่ห่างเกณฑ์ ≥5.7pp (MTN/LTH/HAS/JAKK/FNKO/OSW/ASO/CALY) ใช้ Yahoo แหล่งเดียว — ไม่กระทบผล. งบการเงิน = **SEC EDGAR companyfacts** (`sec.py`, 10-Q งวด ก.ย. 2026; PTON/LUCK ปีบัญชีสิ้น มิ.ย. → TTM = FY26 + Q1 FY27 − Q1 FY26). คำนวณทั้งหมดใน `scripts/scout/2026-11-11_leisure/calc.py`
**WACC:** scout-level proxy ตามขนาด (Filter D): GOLF 9% · PLNT 9.5% · FUN 10% · PTON/LUCK 11% · XPOF 13% — **ไม่ใช่ VS2 §1.1** · ไม่มีผลใดพลิกเมื่อขยับ ±1pp
**FCF definition:** OCF − capex (SEC cash-flow statement)

### Step 0 — Prune
🗄️ Prune: de-listed **0** | SLA fixed **0** | live **9** (WYNN / VICI / ALLY / MMS / CRI / NBIX / BYD / WGO / CMRE)
- **Rule #1:** ไม่มี target ผ่านกำหนด — CRI 11-12 (พรุ่งนี้) · WYNN/VICI/ALLY/NBIX/BYD 11-14 · CMRE 11-17 · MMS 11-20 · WGO 12-19. ⚠️ **WYNN/VICI ครบ 60 วันวันที่ 11-19** (ย้ำจาก R91)
- **Rule #2 (ราคา close 11-10, Yahoo):** WYNN $87.30 · VICI $24.99 · ALLY $37.67 · MMS $66.12 · CRI $34.29 · NBIX $169.14 · BYD $78.29 · WGO $31.19 · CMRE $12.94 → ไม่มีตัวไหน >2× ขอบบน zone (สูงสุด NBIX = 1.25× ของ $135) · ไม่มี formal MOS < −30%. ⚠️ **NBIX ฟื้นมาอยู่ −9.1% จาก high $186.12** (ไม่ผ่าน Filter A ถ้าสแกนวันนี้) และ **BYD −14.4%** — flag ให้ Charlie ทบทวนตอน Tier 1 วันที่ 11-14 ว่ายังควรเก็บไว้หรือไม่
- **Rule #3:** `decisions.md` 0 hits ทุก live ticker · OPEN ไม่เปลี่ยน

### Filter A — ลง ≥20% จาก 52W high (close 2026-11-10)
| Ticker | Sub-industry | ราคา (Yahoo / stockanalysis) | 52W high (Yahoo) | % จาก high | ผล |
|---|---|---|---|---|---|
| **FUN** | Theme parks | $10.16 / $10.16 | $26.28 (06-17) | **−61.3%** | ✅ |
| PRKS | Theme parks | $42.36 / $42.36 | $50.00 (08-04) | −15.3% | ❌ |
| MTN | Ski resorts | $156.51 | $163.99 (11-05) | −4.6% | ❌ |
| **PLNT** | Fitness franchisor | $61.34 / $61.34 | $114.26 (2025-12-16) | **−46.3%** | ✅ |
| LTH | Fitness clubs | $47.42 | $48.61 (11-05) | −2.4% | ❌ |
| **XPOF** | Boutique fitness franchisor | $4.59 / $4.59 | $9.25 (02-02) | **−50.4%** | ✅ |
| **PTON** | Connected fitness | $5.81 / $5.81 | $7.69 (Yahoo) / $7.92 (SA, หน้าต่างเริ่มก่อนหนึ่งวัน) | **−24.4%** (SA −26.6%) | ✅ |
| **GOLF** | Golf equipment (Titleist/FootJoy) | $85.03 / $85.03 | $119.65 (07-06) | **−28.9%** | ✅ |
| CALY | Golf equipment (Callaway) | $17.37 | $20.28 (07-16) | −14.3% | ❌ |
| **LUCK** | Bowling / location entertainment | $3.40 / $3.40 | $9.59 (01-15) | **−64.5%** | ✅ |
| HAS | Toys / games | $121.82 | $124.00 (11-05) | −1.8% | ❌ |
| JAKK | Toys | $36.39 | $36.42 (11-10) | −0.1% | ❌ |
| FNKO | Collectibles | $7.24 | $7.48 (11-09) | −3.1% | ❌ |
| YETI | Outdoor gear | $44.77 / $44.77 | $53.99 (08-05) | −17.1% | ❌ (ใกล้สุด) |
| ASO | Sporting-goods retail | $70.39 | $71.29 (11-09) | −1.3% | ❌ |
| OSW | Cruise-ship spa/wellness | $32.22 | $33.05 (11-09) | −2.5% | ❌ |

**Filter A: 6/16 ผ่าน.** sector แยกเป็น 2 กลุ่มชัด: ของเล่น / ski / club ระดับบน (HAS/JAKK/MTN/LTH/ASO/OSW) อยู่ใกล้ ATH · ที่ร่วงหนักคือธุรกิจที่มีปัญหาเฉพาะตัวหรือหนี้สูง

### Beaten-down reason (Filter A survivors)
| Ticker | เหตุผล | จัดกลุ่ม |
|---|---|---|
| FUN | impairment ต่อเนื่อง: 2025 ~$1.5B + YTD 2026 ~$717M (Q3 $687.7M), Q3 net loss $366.1M; same-park attendance −0.2%, ต.ค. แย่ลงจากอากาศ + อุบัติเหตุร้ายแรงที่ Six Flags Over Georgia; ลด guide Q4 adj. EBITDA เป็น $140–150M ([8-K Q3 2026](https://www.sec.gov/Archives/edgar/data/0001999001/000199900126000103/sixflags-exh991xq32026.htm), [Panabee](https://www.panabee.com/news/six-flags-earnings-q3-2026)) | **ปนกัน** — attendance/อากาศ = temporary · impairment ซ้ำ 2 ปีบอกว่า asset base หลังควบรวมไม่สร้างผลตอบแทนตามที่คาด = เอียงไปทาง permanent |
| PLNT | ร่วง >31% วันเดียว (07 พ.ค.) หลังลด guide FY26 เพราะสมาชิกใหม่ช่วง ม.ค. ต่ำกว่าคาด + ยกเลิกแผนขึ้นราคา, CFO ลาออก; ความกังวลเดิม: GLP-1 + การแข่งขัน ([SGI Europe](https://www.sgieurope.com/financial-results/planet-fitness-cuts-outlook-shares-crash/121032.article), [rallies.ai](https://rallies.ai/news/planet-fitness-cuts-2026-revenue-outlook-cancels-price-hikes-after-25-stock-drop), [Zacks](https://www.zacks.com/commentary/2940481/bear-of-the-day-planet-fitness-plnt)) | **ไม่ชัด — เขียน 2 มุม:** ✅ sentiment overreaction (Jefferies: "massively oversold", [iTiger](https://www.itiger.com/news/2634511469)) · ❌ ถ้า GLP-1/HVLP competition ทำให้ member growth ชะลอถาวร = moat erosion |
| XPOF | ขาดทุนสุทธิ 5 ใน 6 ปี, หยุดขายแฟรนไชส์ในหลายรัฐจาก regulatory inquiry (USAO investigation + FTC consent order ที่เสนอ), revenue หด ([Panabee FY25](https://www.panabee.com/news/xponential-fitness-fy-2025-99-million-net-loss-franchise-sales-halted-amid-regulatory-sc)) | ❌ **permanent / unresolved regulatory overhang** |
| PTON | ไม่มี event เดียว — ราคาค่อยๆ ลงจาก high พ.ย. 2025; ธุรกิจเพิ่งพลิกเป็นกำไรจากการดำเนินงาน FY26 (op income $161M หลังขาดทุนจากการดำเนินงานรวม ~$4.5B FY22–25, SEC) | ✅ sentiment (turnaround ยังไม่ได้รับความเชื่อ) — แต่ประวัติขาดทุนคือประเด็นหลัก |
| GOLF | Q3 2026 EPS $0.83 vs consensus $1.00 (−17%) จาก launch timing + ERP cutover + apparel เอเชียอ่อน; tariff cost ~$70M ปี 2026 (มี IEEPA refund $44.7M ใน 9M); บริษัท reaffirm guide FY26 ([Earnings Whispers](https://www.earningswhispers.com/article/GOLF/r1737), [finviz](https://finviz.com/news/417250/acushnet-misses-on-eps-as-launch-timing-and-erp-hiccups-stall-q3-but-reaffirmed-guidance-and-cash-flow-keep-the-story-intact), [Panabee](https://www.panabee.com/news/acushnet-earnings-q3-2026-ended-2026-09-30)) | ✅ cyclical/temporary (tariff + one-off execution) |
| LUCK | revenue/EPS miss ติดกันหลายไตรมาสตลอดปี 2026, ราคาร่วงอีก −9.6% วันที่ 11-10 ([finviz FQ4](https://finviz.com/news/386281/lucky-strike-entertainment-shares-tumble-after-q4-revenue-misses-forecasts), [Barchart](https://www.barchart.com/story/news/1740547/lucky-strike-nyseluck-misses-q1-cy2026-sales-expectations-stock-drops-11-4)) | ✅ consumer-discretionary slowdown — บวกหนี้สูง |

### Filter B-Zero — Balance sheet (SEC 10-Q ล่าสุด, $M)
| Ticker | Equity | Accumulated deficit | Net debt (ex-op-lease) | สาเหตุ equity ติดลบ | ผล |
|---|---|---|---|---|---|
| FUN | **−$250** | −$2,601 | $4,638 (debt $4,906 − cash $268) | impairment ต่อเนื่อง (goodwill impairment YTD $616M + 2025) + ขาดทุนสุทธิ 2024/2025/2026 | 🔴 **REJECT** — สาขา "operating losses/impairment ต่อเนื่อง" · FCF yield TTM 14.2% ($148M ÷ mcap $1,039M) คือ **leverage artifact** (EV $5.7B, equity เป็นแค่ ~18% ของ EV) · บน FCF ÷ 10% − ND naive FV ติดลบ |
| PLNT | **−$609** | −$1,241 | $2,069 (securitized debt $2,469 − cash $310 − marketable $90) | **recap + buyback** (buyback FY22–9M26 รวม ~$1.3B) — กำไรสุทธิเป็นบวกทุกปีตั้งแต่ 2021 | 🟡 ผ่านต่อ — flag: FCF yield/ROIC ที่ดูดีมาจาก leverage (IC เล็กเพราะ equity ติดลบ) · ND/EBITDA 3.5× (EBITDA TTM $592M) |
| XPOF | **−$316** | −$741 | $477 | ขาดทุนสะสม + goodwill impairment ($55.4M YTD) | 🔴 **REJECT** — operating losses สะสม · OCF TTM −$10M |
| PTON | **−$5** | **−$5,443** | ≈ −$4 (cash $1,342 vs debt $1,338) | ขาดทุนสะสมยุค FY22–FY25 | 🔴 **REJECT** ตามตัวอักษรกฎ (operating losses) — ดูหมายเหตุ 2 มุมด้านล่าง |
| GOLF | +$867 | +$281 | $747 (debt $855 − cash+restricted $108; cash-only ไม่มี XBRL tag แยก — flag) | — | ✅ clean · ND/EBITDA 2.0× |
| LUCK | **−$434** | −$375 | $2,208 (debt $1,791 + finance lease $455 − cash $38) | ปนกัน: buyback FY22–26 ~$488M + ปันผล + ขาดทุนสุทธิ 5 ใน 6 ปี | 🟡 ผ่านต่อแบบมีธงแดง — ND/EBITDA **8.3×** (EBITDA TTM $266M) |

**PTON — 2 มุม (เคสก้ำกึ่งที่สุดในรอบ):** equity ติดลบแค่ $5M และมี net cash · FCF FY26 $378M (OCF $388M − capex $9.9M) = **12.4% yield** บน mcap $3.05B (diluted 525.4M sh) · บน TTM FCF naive FV ($378M ÷ 11%) = $6.55 → **0.89×** · แต่ through-cycle 5Y FCF เฉลี่ย **−$442M/ปี** (FY22 −$2.36B) → naive FV ติดลบ, และเฉลี่ย 2 ปีหลัง restructuring ($351M) = $6.08 → **0.96×** (อยู่ในแถบ ±10% = Tier 1 2b SKIP อยู่ดี). สรุป: ต่อให้ข้าม B-Zero ก็ไม่ผ่าน D. **Re-screen เมื่อ** equity กลับเป็นบวก + FCF บวก ≥3 ปีเต็ม (เร็วสุดหลัง FY28)

### Bucket
ทุก survivor = **Value bucket** (B-Legacy / D-Legacy) — revenue growth TTM: PLNT +8.7% · GOLF ~+7% (9M) · LUCK +3.7% · ไม่มีตัวไหน >15% หรืออยู่ใน reinvestment phase → ไม่เข้า B-V1/D-V1. ไม่มีตัวไหนเข้า Lane AI/Infra (AI/DC revenue = 0)

### Filter B + C (SEC, $M) — PLNT, GOLF, LUCK
| Ticker | FCF TTM (yield) | FCF เฉลี่ย 5Y (yield) | EV/EBITDA TTM | ROIC TTM vs WACC | ผล B | ผล C |
|---|---|---|---|---|---|---|
| PLNT | $214 (4.7%) | FY21–25 $182 (4.0%) | **11.2×** (EV $6.64B ÷ $592M; SA 12.4×) — ต่ำกว่า multiple ปกติของบริษัท แต่**ไม่ได้ verify 5Y percentile** | 22.1% (EBIT×0.75 ÷ (equity+ND) — สูงเกินจริงเพราะ equity ติดลบ) · SA 11.6% → ทั้งสองค่า > 9.5% | 🟡 FCF ❌ · EV/EBITDA น่าจะ bottom-third (ไม่ verify) → ส่งต่อ Tier 1 | ✅ |
| GOLF | $239 (4.9%) | FY21–25 $147 (3.0%; FY22 OCF −$68M จาก inventory build) | **15.2×** (EV $5.61B ÷ adj. EBITDA $369M หัก IEEPA refund $44.7M) — ไม่ verify 5Y percentile | **15.0%** (adj. EBIT $314M × 0.77 ÷ (equity $867M + ND $747M)) vs 9% | 🟡 FCF ❌ · EV/EBITDA ไม่ชัด → ส่งต่อ Tier 1 (ผลไม่ขึ้นกับ B ดูด้านล่าง) | ✅ |
| LUCK | $18 (3.9%) | FY22–26 $14 (3.1%) | 10.0× (EV $2.67B ÷ $266M) | **5.9%** (EBIT $137M × 0.77 ÷ IC $1,774M) vs ~11% = **54%** ของ WACC · op income FY23 $201M → FY24 $92M → FY25/26 $137M (ไม่มี trend ดีขึ้นต่อเนื่อง) | ❌ | ❌ |

**LUCK ตายที่ B+C.** ROIC ต่ำกว่า 80% ของ WACC มาก + หนี้รวม finance lease 8.3× EBITDA

### Filter D + Tier 1 Quick-Screen (PLNT, GOLF)
| Ticker | Naive FV (normalized FCF ÷ WACC − net debt) | P / naive FV | Sensitivity | ผล |
|---|---|---|---|---|
| **PLNT** | TTM $214M ÷ 9.5% − ND $2,069M = $184M → **$2.46/หุ้น** (74.52M sh, [SA](https://stockanalysis.com/stocks/plnt/statistics/)) · 5Y avg → **ติดลบ** | **24.9×** | WACC 8%: $8.13 (7.5×) · **กรณีใจดีสุด** NOPAT ($430M × 0.75) แทน FCF: $17.79 (**3.4×**) | Tier 1 **check 2a: >1.5× → `QUICK-SCREEN SKIP`** · หนี้ securitization $2.47B กิน FCF เกือบหมดในโมเดล no-growth — มูลค่าหุ้นขึ้นกับการเติบโตของจำนวนสาขาเกือบทั้งหมด |
| **GOLF** | TTM $239M ÷ 9% − ND $747M = **$33.37/หุ้น** · 5Y avg $147M → $15.46 | **2.55×** (5Y: 5.50×) | WACC 8%: $39.17 (2.17×) · NOPAT-based: $33.95 (2.50×) | Tier 1 **check 2a: >1.5× → `QUICK-SCREEN SKIP`** |

**Check 3 (red-flag search):** ไม่ได้รัน — enrichment ไม่ใช่ gate และทั้ง 2 ตัวตกที่ arithmetic แล้ว · **Filter E:** ไม่ประเมิน (ไม่มีตัวผ่าน D) — หมายเหตุ: GOLF น่าจะผ่าน E1 (Titleist Pro V1 brand/pricing power) + E2 (ROIC 15% vs 9%) + E3 → ถ้าราคาลงถึงเกณฑ์ D จะเป็นตัวที่คุณภาพดีที่สุดใน sector แต่ราคาที่ผ่าน D (≤0.80× ของ $33.37) ≈ **$27** (−68%) — ไกลมาก

### Final routing — Round 92
| Ticker | ตกที่ | Tag |
|---|---|---|
| PRKS, MTN, LTH, CALY, HAS, JAKK, FNKO, YETI, ASO, OSW | A (−0.1% ถึง −17.1%) | reject |
| FUN | B-Zero (equity −$250M จาก impairment/ขาดทุนต่อเนื่อง) | reject |
| XPOF | A-reason (regulatory overhang) + B-Zero (ขาดทุนสะสม) | reject |
| PTON | B-Zero (accumulated deficit −$5.4B) — และ D ≥0.89× แม้จะข้าม B-Zero | reject |
| LUCK | B + C (FCF 3.9%, ROIC 5.9% vs 11%) | reject |
| PLNT | Tier 1 check 2a (24.9× naive FV; ใจดีสุด 3.4×) | `QUICK-SCREEN SKIP` |
| GOLF | Tier 1 check 2a (2.55× naive FV) | `QUICK-SCREEN SKIP` |

**0 fast-track · 0 learning-queue · 16 reject (10 A · 3 B-Zero · 1 B/C · 2 `QUICK-SCREEN SKIP`: PLNT / GOLF)** · ไม่เพิ่ม row ใน Pending Analysis · ไม่เพิ่ม `buy_list.md` · บันทึก tag ใน `deployment_log.md` แล้ว (พร้อม backfill 2 แถวที่ R91 ค้างไว้: SKYW/RYAAY)

### ข้อสังเกตถึง CIO / Charlie
1. **Sector นี้ไม่มี value ที่ชัดเจน** — ตัวคุณภาพดี (HAS, MTN, LTH, ASO, OSW, JAKK) อยู่ใกล้ ATH; ตัวที่ร่วงหนักมีปัญหาโครงสร้างทุนเกือบทุกตัว: 5 ใน 6 survivor มี equity ติดลบ (FUN, PLNT, XPOF, PTON, LUCK) — leisure ที่เป็น franchise/asset-heavy มักถูก lever ผ่าน securitization/LBO
2. **PLNT ซ้ำบทเรียน B-Zero ของ BBWI** — FCF yield/ROIC ดูดีเพราะ recap ไม่ใช่เพราะถูก: หักหนี้ $2.07B แล้ว naive FV แทบเป็นศูนย์
3. **GOLF** เป็นธุรกิจที่ดีที่สุดในกลุ่ม (ROIC 15%, หนี้ต่ำ, Q3 miss เป็นเรื่อง one-off) แต่ตลาดยังให้ ~15× EBITDA — ไม่มี MOS ในกรอบ no-growth
4. **PTON** — turnaround จริง (FCF $378M, net cash) แต่ประวัติสั้นเกินไปสำหรับ through-cycle FCF; ไม่ผ่าน D แม้ใช้ TTM
5. **ไม่แนะนำสแกน sector นี้ซ้ำ** จนกว่า HAS/MTN/LTH จะลงมา ≥20% หรือ GOLF จะลงอีก ≥30%

**Target analysis date:** ไม่มี (0 candidates)

*Max — 2026-11-11 | Scout Round 92 (Leisure & Recreation — 16 screened [FUN/PRKS/MTN/PLNT/LTH/XPOF/PTON/GOLF/CALY/LUCK/HAS/JAKK/FNKO/YETI/ASO/OSW], 0 fast-track / 0 learning-queue / 16 reject [10 A · 3 B-Zero · 1 B/C · 2 QUICK-SCREEN SKIP PLNT/GOLF]; MAT excluded (R77 within 30 days); MODG→CALY rename; new sector, not a re-scout)*
