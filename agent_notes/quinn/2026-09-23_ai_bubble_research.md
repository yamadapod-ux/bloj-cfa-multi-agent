# Quinn's Notes — AI "Circular Financing" Bubble Thematic Research (2026-09-23)

**Analyst:** Quinn | **Type:** Thematic Research Note (ไม่ใช่ ticker analysis ปกติ) — สำหรับ Charlie รวบรวมตีพิมพ์ dashboard "Research"
**Trigger:** CIO concern เรื่อง circular financing (Nvidia/OpenAI/Microsoft/Oracle/AMD/Broadcom) + AI revenue monetization โตไม่ทันความคาดหวังตลาด
**บริบทเสริม:** ทีม reject AMD 2 รอบ (2026-05-06, 2026-05-18), AVGO 2 รอบ, NVDA 1 รอบ (2026-05-16) ด้วย Forward Sharpe/Kelly negative + MOS ติดลบหนัก — ราคาวิ่งต่อหลังจากนั้น (AMD >$1T mkt cap, ก.ย. 2026)

**⛔ Training Knowledge Ban compliance:** ทุกตัวเลขในไฟล์นี้มาจาก WebSearch/WebFetch ที่รันในเซสชันนี้เท่านั้น (2026-09-23) พร้อม URL กำกับ ยกเว้นตัวเลขที่ดึงจาก Quinn's own prior verified notes (2026-05 series) ซึ่งระบุไว้ชัดเจนว่าเป็น "stale FV / internal reference" ไม่ใช่ fresh data

---

## 1. Capex-vs-Revenue Growth Gap เชิงปริมาณ

### 1.1 Hyperscaler AI Capex 2026 (YoY)

| Company | 2026 Capex Guidance | 2025 Actual/Base | Source |
|---------|---------------------|-------------------|--------|
| Amazon | $200B (mgmt raised to ~$220B per Q2 call) | $125B (2025) | [Techtimes — AWS Backlog $496B](https://www.techtimes.com/articles/322572/20260731/aws-backlog-hits-496b-amazon-raises-ai-spend-220b-capacity-runs-short.htm), [GPUSmith](https://gpusmith.com/articles/en/hyperscaler-ai-capex-2026) |
| Microsoft | $190B total (FY26) | $90B (2025, per one estimate) | [Fortune — Meta/MSFT/GOOGL capex](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/) |
| Alphabet/Google | $180–190B (raised from $175–185B) | $91B (2025) | [GPUSmith](https://gpusmith.com/articles/en/hyperscaler-ai-capex-2026) |
| Meta | $135–145B (raised guidance twice) | $72.22B (2025) | [ValueAddVC — Meta $145B capex 2026](https://valueaddvc.com/blog/meta-145b-ai-capex-2026-why-zuckerberg-raised-guidance-twice), [Fortune](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/) |
| **Big-4 Combined** | **$725B (2026E)** | **$410B (2025)** | [ValueAddVC AI Spending Tracker](https://valueaddvc.com/pulse/big-tech-ai-capex-725-billion-2026-guidance), [Fortune](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/) |
| Big-5 (+ Oracle) all hyperscalers | $775–800B (2026E), or $600–630B per conservative estimates | 36–77% YoY range depending on scope | [ALCapital Advisory — AI Capex Cycle 2026](https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html), [IEEE ComSoc](https://techblog.comsoc.org/2025/12/22/hyperscaler-capex-600-bn-in-2026-a-36-increase-over-2025-while-global-spending-on-cloud-infrastructure-services-skyrockets/) |

**Big-4 Capex Growth YoY = ($725B / $410B) − 1 = +76.8%** [calc: Quinn, source figures above]

*Note: sources disagree on exact totals ($600B–$800B range depending on which hyperscalers included and whether power/cooling infra counted) — this is itself a data-quality flag: even the "denominator" of this bubble debate isn't fully agreed upon across trackers. Used the $725B/$410B Big-4 figure as primary anchor because it has 2 consistent corroborating sources (Fortune + ValueAddVC) with the same underlying guidance numbers.*

### 1.2 AI-Attributable Revenue Growth YoY (disclosed run-rates)

| Company | AI Revenue Metric | Value | YoY Growth | Source |
|---------|-------------------|-------|-----------|--------|
| Microsoft | AI business annual revenue run-rate | $37B | **+123% YoY** | [GeekWire — MSFT Q3 FY26](https://www.geekwire.com/2026/microsoft-tops-wall-street-expectations-reports-accelerating-azure-growth-and-37b-ai-run-rate/) |
| Microsoft | Azure & cloud services revenue | — | +39% YoY (38% CC) | [Futurum — MSFT Q2 FY26](https://futurumgroup.com/insights/microsoft-q2-fy-2026-cloud-surpasses-50b-azure-up-38-cc/) |
| Amazon (AWS) | AWS AI business annualized run-rate | >$25B | Triple-digit % YoY | [Techtimes — AWS Q2 2026](https://www.techtimes.com/articles/322572/20260731/aws-backlog-hits-496b-amazon-raises-ai-spend-220b-capacity-runs-short.htm) |
| Amazon (AWS) | Total AWS revenue | $42.2B (Q2) | +37% YoY (fastest in 18 quarters) | [CNBC — AWS Q2 2026](https://www.cnbc.com/2026/07/30/aws-earnings-q2-2026.html) |
| Google | Google Cloud revenue | $24.77B (Q2) | +82% YoY | [PYMNTS — Google Cloud Q2 2026](https://www.pymnts.com/earnings/2026/google-cloud-rides-enterprise-ai-demand-to-82percent-growth/) |
| Google | AI-based cloud products revenue specifically | — | **~+800% YoY** (small base) | [Startup Fortune — Google Cloud Q2 2026](https://startupfortune.com/google-cloud-grew-82-in-q2-2026-and-the-514-billion-backlog-tells-you-everything-about-who-is-winning-the-ai-race/) |
| Meta | No AI-specific revenue line disclosed separately — ad revenue +30% YoY attributed partly to AI targeting | +30%+ | [SeekingAlpha — Meta AI ROI](https://seekingalpha.com/article/4866269-meta-when-ai-actually-generates-roi) |

### 1.3 Gap Ratio — the Honest Framing (สำคัญ — ห้าม cherry-pick)

**สิ่งที่น่าสนใจ:** ถ้าดูแค่ growth RATE (%) — AI revenue กำลังโตเร็วกว่า capex ด้วยซ้ำ (MSFT AI +123%, AWS AI triple-digit, Google Cloud AI products +800% vs capex +76.8%) เพราะฐานยังเล็กมาก (small-base effect) นี่คือจุดที่ bull case ใช้เถียง — **growth rate ไม่ใช่ปัญหา**

**ปัญหาจริงคือ absolute dollar gap:**
- Combined disclosed "AI-specific" revenue run-rate ที่หาได้ชัดเจน (MSFT $37B + AWS AI $25B) = **$62B**
- เทียบ Big-4 capex 2026 = **$725B**
- **Coverage ratio = $62B / $725B = 8.6%**
- **Capex ปี 2026 = 11.7× ของ disclosed AI-specific revenue run-rate**

[Calc: Quinn, จาก source data ข้างต้น — Google/Meta ไม่ได้แยก AI-specific revenue ออกมาชัดเจนเป็นตัวเลขเดียว ทำให้ตัวเลข coverage นี้ underestimate ฝั่ง revenue บ้าง (Google Cloud total $24.77B/quarter = ~$99B annualized รวม non-AI cloud ด้วย) — แต่ถึงจะรวม Google Cloud ทั้งหมดเข้าไป ($62B + $99B = $161B) coverage ratio ก็ยังอยู่แค่ ~22% ของ capex เท่านั้น]

**Interpretation:** นี่คือ core ของ "circular financing" concern — เงินทุน capex ($725B) ไหลเวียนระหว่าง hyperscaler/chip vendor แต่ revenue ที่ verify ได้ว่ามาจาก AI โดยตรง (ไม่ใช่ cloud โดยรวมที่โตอยู่แล้วจาก non-AI workload) ยังเป็นเศษเสี้ยวของ capex เดียว — ตลาด priced-in ว่า gap นี้จะปิดได้ภายในไม่กี่ปี ซึ่งเป็น key assumption ที่ต้อง monitor

### 1.4 GPU Depreciation — Accounting Red Flag ที่เสริม Gap นี้

[Source: Level Headed Investing, "Are AI Chips' Useful Lives Creating Useless Earnings?" published 2025-12-04](https://www.levelheadedinvesting.com/p/are-ai-chips-useful-lives-creating-useless-earnings)

| Company | Previous Server/GPU Useful Life | Current (Extended) Life | Earnings Impact |
|---------|----------------------------------|--------------------------|------------------|
| Alphabet | 4 years | 6 years (extended 2023) | −$3.9B depreciation, +$3B earnings boost (2023) |
| Amazon | 4 years | 5–6 years (extended 2022→2023) | −$3.6B depreciation (2022), +$3.1B operating income (2024E) |
| Meta | 3 years | 5.5 years (extended through 2025) | Not quantified in source |

**Michael Burry's claim (cited in same source):** GPU hardware มี true economic life ~2–3 ปี แต่ถูก depreciate ยาวถึง 5–6 ปี → understated depreciation ~**$176B ระหว่างปี 2026–2028** → operating income ที่บริษัทอย่าง Oracle และ Meta รายงาน อาจสูงเกินจริงกว่า **20%**

**Quant implication:** ถ้า assumption นี้ถูกต้อง reported EBITDA/operating income ของ hyperscaler capex-heavy names ถูก overstate อย่างมีนัยสำคัญ → ทุก multiple (EV/EBITDA, P/E) ที่คำนวณจากตัวเลขปัจจุบันจะดู "ถูกกว่าความเป็นจริง" — นี่คือ risk ต่อ valuation ฝั่ง hyperscaler มากกว่าฝั่ง chip vendor (NVDA/AMD/AVGO) โดยตรง เพราะ chip vendor รับเงินสดทันทีตอนขาย ไม่ได้แบก depreciation risk นี้เอง — risk นี้อยู่ที่งบของ "ผู้ซื้อ" ไม่ใช่ "ผู้ขาย"

---

## 2. Valuation Multiple Percentile — NVDA / AMD / AVGO (ก.ย. 2026)

### 2.1 Current Multiples (Verified 2 sources, 2026-09-22)

| Ticker | Price (9/22/26) | Fwd P/E | EV/EBITDA | P/S | Source |
|--------|------------------|---------|-----------|-----|--------|
| NVDA | $228.87 (close) / $227.38 (alt) | **18.87** | **27.35** (site) / 22.84 (gurufocus, diff EBITDA basis) | 18.25 | [stockanalysis.com/nvda](https://stockanalysis.com/stocks/nvda/statistics/), [Investing.com NVDA](https://www.investing.com/equities/nvidia-corp) |
| AMD | $623.77 (close) / $620.98 (alt) | **56.38** | **105.57** | 24.65 | [stockanalysis.com/amd](https://stockanalysis.com/stocks/amd/statistics/) |
| AVGO | $364.54 (close) / $365.48 (alt) | **20.95** | **34.01** | 19.55 | [stockanalysis.com/avgo](https://stockanalysis.com/stocks/avgo/statistics/) |

Market cap confirm: NVDA $5.53T, AMD $1.02T (**crossed $1T milestone** — confirms CIO's data point), AVGO $1.74T [all: stockanalysis.com, 2026-09-22 4:00PM EDT close]

### 2.2 10-Year Historical Percentile (GuruFocus EV/EBITDA)

| Ticker | Current EV/EBITDA | 10Y Median | vs Median | Percentile (sector) | Source |
|--------|---------------------|------------|-----------|----------------------|--------|
| **NVDA** | 22.84 | 42.73 | **47% BELOW median** | worse than 52.03% of semis (i.e., mid-pack, NOT expensive) | [GuruFocus NVDA EV/EBITDA, as of 2026-09-18](https://www.gurufocus.com/term/enterprise-value-to-ebitda/NVDA) |
| **AMD** | 102.59 (gurufocus date) / 105.57 (stockanalysis 9/22) | 44.84 | **+129% above median** | worse than 83.31% of 743 semis peers | [GuruFocus AMD EV/EBITDA, as of 2026-06-12](https://www.gurufocus.com/term/enterprise-value-to-ebitda/AMD) |
| **AVGO** | 33.14 (gurufocus 9/4) / 34.01 (stockanalysis 9/22) | 18.49 | **+79% above median** | worse than ~92.8% of sector (per secondary snippet, unverified exact %) | [GuruFocus AVGO EV/EBITDA, as of 2026-09-04](https://www.gurufocus.com/term/enterprise-value-to-ebitda/AVGO) |

**⚠️ Key Finding — ไม่ใช่ทุกตัวใน "AI bubble basket" แพงเท่ากัน:**
- **NVDA อยู่ต่ำกว่า 10-year median 47%** — ราคาปัจจุบันจริงๆ **ถูกกว่า** ค่าเฉลี่ยประวัติศาสตร์ตัวเองด้วยซ้ำ แม้ market cap แตะ $5.5T แล้ว เพราะกำไร/EBITDA โตเร็วกว่าราคาหุ้น (คล้ายที่ Motley Fool เขียนไว้: "Nvidia's Forward P/E Has Actually Fallen as Its Stock Price Rose") [Source: The Motley Fool, 2026-07-11](https://www.fool.com/investing/2026/07/11/nvidias-forward-pe-has-actually-fallen-as-its-stoc/)
- **AMD คือตัวที่แพงเวอร์ที่สุดในกลุ่ม** — EV/EBITDA สูงกว่า median 129%, อยู่ percentile 83+ เทียบ peer
- **AVGO อยู่กึ่งกลาง** — แพงกว่า median 79% แต่ไม่สุดโต่งเท่า AMD

**Data quality caveat:** gurufocus ตัวเลขแต่ละ ticker วัด ณ วันที่ต่างกัน (NVDA 9/18, AMD 6/12 — ค่อนข้าง stale, AVGO 9/4) และ EV/EBITDA basis อาจต่างกัน (GAAP vs non-GAAP EBITDA) ระหว่าง gurufocus กับ stockanalysis.com (เห็นได้จาก NVDA 22.84 vs 27.35) — ตัวเลข percentile จึงเป็น **directional indicator ไม่ใช่ precision figure**

### 2.3 Dot-Com Bubble Comparison (Cisco, JDS Uniphase, Nortel — March 2000 peak)

| Company (2000 peak) | Multiple | Value | Source |
|----------------------|----------|-------|--------|
| Cisco Systems | P/E | ~201× | Via WebSearch snippet citing ICIS.com/Harding Loevner analysis (direct fetch 403-blocked; number appeared in search result digest, not independently re-verified — **flag lower confidence**) |
| Cisco Systems | EV/Sales | ~31× | Same source as above |
| Cisco Systems | P/FCF | ~176× | Same source as above |
| Cisco Systems | Market cap vs Revenue | $500B+ mkt cap vs $19B revenue | Same source |
| JDS Uniphase | P/S | **100–110×** | [CNBC — The Curious Case of JDS Uniphase](https://www.cnbc.com/id/35663686), corroborated via WebSearch digest |
| JDS Uniphase | Market cap | $125–140B peak | Same |
| Nortel Networks | Market cap (mid-2000) | $366B | [Globe and Mail — After the bubble bursts](https://www.theglobeandmail.com/report-on-business/rob-magazine/after-the-bubble-bursts-are-nortel-and-other-tech-stocks-a-good-value-now/article4146633/) |
| Nortel Networks | Revenue (2000, optical networking) | $9.2B (+133% YoY that year) | Same |
| Nortel Networks | Implied P/S (calc) | **~40×** ($366B / $9.2B) | Quinn calc from 2 figures above — approximate, timing of mkt cap vs full-year revenue not perfectly aligned |

**⚠️ ห้ามสรุปเกินข้อมูล:** ตัวเลข Cisco (201× P/E, 31× EV/Sales) มาจาก WebSearch digest ที่ direct-fetch URL ไม่สำเร็จ (403 Forbidden ทั้ง 2 ครั้งที่ลอง) — ความมั่นใจต่ำกว่าตัวเลขอื่นในรายงานนี้ที่ verify ได้ตรงจาก WebFetch จริง แต่ JDS Uniphase P/S 100-110× ยืนยันจาก CNBC ได้ชัดเจน

**Comparison to today:** NVDA/AMD/AVGO forward P/E ปัจจุบัน (18.87× / 56.38× / 20.95×) **ต่ำกว่า Cisco's 201× P/E มาก** และ P/S ปัจจุบัน (18.25× / 24.65× / 19.55×) ก็ต่ำกว่า JDS Uniphase's 100-110× P/S อย่างชัดเจน — **ในเชิง multiple ล้วนๆ ยังไม่ถึงระดับ extreme ของ dot-com peak individual names** แต่ข้อควรระวัง: Cisco/JDSU peak เกิดกับบริษัทที่ **ไม่มี earnings จริงรองรับเลย** (P/E 201× หมายถึง earnings บางเพียงเศษเสี้ยวของ market cap) ในขณะที่ NVDA มี EBITDA/earnings จริงจำนวนมาก — **โครงสร้างความเสี่ยงต่างกัน ไม่ใช่ apples-to-apples 100%** — bubble ตอนนี้ (ถ้ามี) น่าจะเป็น "capex overinvestment bubble" ที่ hyperscaler มากกว่า "pure multiple bubble" ที่ chip vendor

---

## 3. Sharpe / Kelly Framing — ทำไม reject ตอนนั้น และยัง justify ได้ไหมตอนนี้

### 3.1 สรุป Quant Signal ที่ทีม reject ไว้ (2026-05)

| Ticker | Date | Price then | Forward Sharpe | Kelly | P-W EV | MOS | Source (internal) |
|--------|------|-----------|-----------------|-------|--------|-----|---------------------|
| NVDA | 2026-05-16 | $227 | **-0.57** | **-7.8** | $156.80 | -31% | `agent_notes/quinn/2026-05-16_NVDA.md` |
| AMD | 2026-05-18 | $455 | **-0.53** | **-1.61** | $110-125 (China-adj) | -72.5% to -75.8% | `agent_notes/quinn/2026-05-18_AMD.md` |
| AVGO | 2026-05-18 | $230 | **-0.09** | **0% (negative EV)** | $229.4 | -0.3% | `agent_notes/quinn/2026-05-18_AVGO.md` |

ทั้ง 3 ตัวถูก reject ด้วยเหตุผลเดียวกัน: **Forward Sharpe ติดลบ = แย่กว่าถือเงินสด**, Kelly negative = optimal position size 0%, Sensitivity Matrix ส่วนใหญ่ไม่ justify ราคา ณ ขณะนั้น

### 3.2 Recalibration Check — เอา FV เดิม (stale, พ.ค. 2026) มาเทียบราคาปัจจุบัน (ก.ย. 2026)

**⚠️ Methodology note (สำคัญมาก):** การคำนวณนี้ใช้ **Fair Value เดิมจาก พ.ค. 2026 แบบไม่ update** (ไม่ใช่ fresh DCF) — จุดประสงค์คือทดสอบว่า "ถ้าเราไม่เคย re-verify fundamentals เลย ตัวเลข quant จะเปลี่ยนยังไงจากราคาที่วิ่งไป" — **นี่ไม่ใช่ recommendation ใหม่ และไม่ควรใช้ตัดสินใจ trade จริง** (fundamentals จริงเปลี่ยนไปมากแล้วตาม Section 1 — capex/revenue โตขึ้นเยอะทั้งคู่) เป็นเพียง **honest calibration exercise** ตามที่ CIO ขอ

| Ticker | Price พ.ค. 2026 | Price ก.ย. 2026 | % Price Change | Stale-FV Fwd Return (พ.ค.) | Stale-FV Fwd Return (ก.ย., ใช้ FV เดิม) | Stale-FV Forward Sharpe (ก.ย.) |
|--------|------------------|-------------------|-----------------|------------------------------|---------------------------------------------|-----------------------------------|
| NVDA | $227 | $228.87 | **+0.8%** | -30.9% | -31.5% | -0.57 (unchanged) |
| AMD | $455 | $620.98 | **+36.5%** | -75.8% | -82.3% | -1.33 (worse) |
| AVGO | $230 | $364.54 | **+58.5%** | -0.3% | -37.1% | -2.32 (much worse) |

[Calc: Quinn, using price sources Section 2.1 + internal stale FV from May 2026 notes cited above; σ assumptions unchanged from May notes: NVDA 62%, AMD 65%, AVGO 17.7%; Rf ~4.0%]

### 3.3 การตีความ — honest, ไม่ defensive

**จุดที่สำคัญที่สุด: NVDA แทบไม่ขยับราคาเลย (+0.8% ใน 4 เดือน)** ขณะที่ AMD (+36.5%) และ AVGO (+58.5%) วิ่งไปไกล — นี่คือสัญญาณที่ต่างจาก narrative "AI ตัวไหนก็วิ่งหมด" อย่างมีนัยสำคัญ:
- NVDA ที่ quant signal บอก "แพงเกิน" (Forward Sharpe -0.57) — ราคาแทบไม่ไปไหนเลย 4 เดือน สอดคล้องกับ quant signal ไม่ได้ผิด
- AMD ที่ quant signal บอก "แพงเกิน" หนักสุด — ราคาวิ่งขึ้น +36.5% ต่อ **และ** valuation percentile confirmed ว่าแพงจริง (129% above 10Y median EV/EBITDA) → **นี่คือกรณีที่ quant signal (fundamental) ถูก แต่ price action (momentum) สวนทาง** ระยะสั้น — ยังไม่รู้จนกว่าจะเห็นรอบ correction
- AVGO วิ่งขึ้น +58.5% แต่ valuation percentile (+79% above median) ยังไม่สุดโต่งเท่า AMD — น่าจะเป็นตัวที่ "แพงขึ้นเร็วที่สุดเทียบ fundamental" ในกลุ่ม 3 ตัวนี้

**คำตอบตรงๆ ต่อคำถาม CIO — "signal ผิดหรือราคาแค่วิ่งสวนทาง":**
Forward Sharpe/Kelly เป็น **relative-value, mean-reversion-style signal** ไม่ใช่ momentum signal — มันถูกออกแบบมาเพื่อบอกว่า "risk-adjusted ไม่คุ้มเข้าใหม่ ณ ราคานี้" ไม่ใช่ "ราคาจะลง" สองเรื่องนี้ต่างกัน — การที่ราคาวิ่งต่อไม่ได้แปลว่า signal ผิด (Sharpe ต่ำไม่ได้ทำนายทิศทางราคา มันบอกแค่ risk-adjusted return ที่คาดหวัง) — แต่สิ่งที่ Quinn ต้อง honest คือ: **ถ้าเราปฏิเสธทุกครั้งที่ Sharpe ติดลบในธีมที่มี momentum แรงระดับนี้ (AI capex supercycle) เราจะ miss ทุก leg ของ rally จนกว่า cycle จะพลิกจริง** — trade-off ระหว่าง "ไม่ deploy ทุนเข้า overvalued asset" กับ "miss มหาศาลถ้า bubble ยังไม่แตกอีกหลายปี" คือสิ่งที่ CIO ต้องตัดสินใจเชิง philosophy ไม่ใช่สิ่งที่ quant framework แก้ให้ได้เอง — **นี่ไม่ใช่เหตุผลให้เปลี่ยนกฎ MOS/Conviction gate** (Return-side locked rule) แต่เป็น data point สำหรับ Rolling 8Q review ตาม Pre-commitment Rules

---

## 4. Sensitivity/Scenario — ถ้า AI Monetization ล่าช้า 2-3 ปี

### 4.1 Reverse-DCF Implied Growth (extrapolated จาก Quinn's own May-2026 Sensitivity Matrix)

**Method:** ใช้ AMD Sensitivity Matrix เดิม (`agent_notes/quinn/2026-05-18_AMD.md` Section 2) — log-interpolate ระหว่าง Rev CAGR 25%→$145 และ 42%→$365 (ที่ WACC 9.0%) เพื่อหา CAGR ที่ implied จากราคาปัจจุบัน — **นี่คือ extrapolation จาก model เดิม ไม่ใช่ fresh DCF เต็มรูปแบบ**

| Ticker | Price ก.ย. 2026 | Implied Rev CAGR ที่ WACC 9% (extrapolated) | เทียบ Analyst Consensus Growth |
|--------|-------------------|-----------------------------------------------|----------------------------------|
| AMD | $620.98 | **~52%** | ต้องสูงกว่า management's most bullish MI-series scaling case ที่เคยประเมินไว้ (~42% เป็น upper bound ของ matrix เดิม) |

**NVDA cross-check (จาก analyst consensus จริง, ไม่ใช่ extrapolation):**
- FY2027 revenue consensus: **$411.29B** [Seeking Alpha / Hudson Labs, 2026-09](https://seekingalpha.com/article/4875305-nvidia-accelerating-revenue-growth-into-fy2027-forward-pe-drops-to-25x-upgrade)
- FY2028 guidance (management): **~70% growth** → implies **$673–700B** FY2028 revenue [24/7 Wall St, 2026-09-22](https://247wallst.com/investing/2026/09/22/nvidia-price-prediction-wall-street-and-our-model-finally-agree/)
- FY2028 guidance เทียบ analyst average estimate: **70% (mgmt) vs 44% (analyst avg)** — mgmt guidance สูงกว่า street 26 percentage points [Same source]
- **สำคัญ:** ตัวเลข FY2027 consensus revenue ($411B) นี้ **สูงกว่าตัวเลขที่ Quinn ใช้ใน May 2026 analysis มาก** (May notes ใช้ FY2027E revenue $197.5B สำหรับ P/S calc) — นั่นหมายความว่า **street's revenue expectation เพิ่มขึ้น ~2 เท่าใน 4 เดือน** ขณะที่ราคาหุ้นแทบไม่ขยับ (+0.8%) — สอดคล้องกับ Section 2.2 ที่พบว่า NVDA valuation percentile ต่ำกว่า median: **NVDA ไม่ได้แพงขึ้น เพราะ earnings estimate โตเร็วกว่าราคา**

### 4.2 Scenario: ถ้า AI Monetization เลื่อนไป 2-3 ปี

**Framework:** ถ้า management's FY2028 guidance 70% growth ไม่เกิดขึ้นจริงในปีนั้น แต่เลื่อนไปเป็น FY2030-2031 แทน (monetization delay 2-3 ปี) — ผลกระทบต่อ DCF-based valuation:

- **Terminal value effect:** DCF fair value ส่วนใหญ่มาจาก cash flow ปีที่ 3-5 เป็นต้นไป (terminal value มักเป็น 60-75% ของ DCF total ในโมเดล high-growth) ถ้า growth ปีที่คาดหวังเลื่อนออกไป 2-3 ปี โดยที่ WACC ไม่เปลี่ยน → **PV ของ cash flow นั้นลดลงตาม discount factor ยกกำลัง** เช่น ที่ WACC 10%: (1.10)^2 = 1.21 → fair value จาก delayed cash flow ลดลงประมาณ **17-21%** เทียบ baseline ถ้า delay 2 ปี, หรือ **~25%** ถ้า delay 3 ปี [Quinn calc: standard DCF discounting mechanics, CFA L2 Equity Valuation]
- **สำหรับ NVDA:** ถ้า FY2028 guidance 70% growth เลื่อนเป็น FY2030-31 แทน — ด้วย current EV/EBITDA ที่ต่ำกว่า median อยู่แล้ว (22.84 vs 42.73) มี **cushion มากกว่า AMD/AVGO** ที่จะรับ delay scenario โดยไม่ทำให้ multiple ดู absurd — NVDA อาจแค่ "de-rate กลับสู่ median" ไม่ใช่ "crash จาก extreme premium"
- **สำหรับ AMD:** ที่ EV/EBITDA อยู่ 129% เหนือ median อยู่แล้ว **ไม่มี cushion เลย** — ถ้า monetization delay เกิดขึ้นจริง AMD มีความเสี่ยง multiple compression สูงสุดในกลุ่ม 3 ตัว เพราะราคาปัจจุบัน priced-in growth rate (~52% ตาม reverse-DCF, Section 4.1) ที่สูงกว่า NVDA's own guided growth (70% แต่ NVDA มี track record ส่งมอบแล้วจริง ในขณะที่ AMD ยังเป็น "narrative" มากกว่า "delivered revenue")
- **สำหรับ Hyperscaler capex-heavy names (MSFT/GOOGL/AMZN/META โดยตรง ไม่ใช่ chip vendor):** ผลกระทบต่างออกไป — hyperscaler รับความเสี่ยงทั้ง (a) depreciation ของ GPU ที่ซื้อมาแล้ว (Section 1.4 — Burry's $176B claim) และ (b) opportunity cost ของ capex ที่ยังไม่ monetize — ถ้า delay 2-3 ปี จะกระทบ hyperscaler's own ROIC/margin มากกว่ากระทบ NVDA/AMD/AVGO โดยตรง (เพราะ chip vendor ได้เงินสดจาก sale ไปแล้ว) — **นี่คือเหตุผลว่าทำไม circular-financing concern ควร frame เป็นความเสี่ยงต่อ hyperscaler equity มากกว่า chip-vendor equity** แม้จะเป็น ecosystem เดียวกัน

---

## 5. Quinn's Summary Signal สำหรับ Thematic Note

**Quant conclusion (ไม่ใช่ recommendation เปลี่ยน gate ใดๆ — เป็น research framing เท่านั้น):**

1. **Capex-revenue gap เป็นเรื่องจริงเชิงตัวเลข** — capex $725B (Big-4, 2026) vs disclosed AI-specific revenue run-rate $62B = coverage 8.6% — นี่คือตัวเลขที่ verify ได้ ไม่ใช่การกล่าวหาลอยๆ
2. **แต่ "bubble" ไม่ใช่ uniform ทั้ง basket** — NVDA (EV/EBITDA ต่ำกว่า median 47%) ≠ AMD (สูงกว่า median 129%) ≠ AVGO (สูงกว่า median 79%) — การพูดว่า "AI stocks are a bubble" รวมทั้งกลุ่มเป็นการ oversimplify ที่ตัวเลขไม่ support
3. **Quant signal (Forward Sharpe/Kelly negative) ที่ใช้ reject AMD/AVGO/NVDA ยังคง valid เป็น relative-value signal** — มันไม่เคยอ้างว่าทำนายทิศทางราคา (momentum) — ราคาวิ่งต่อไม่ใช่หลักฐานว่า signal ผิด — แต่เป็นหลักฐานว่า **momentum ชนะ valuation ในช่วง 4 เดือนที่ผ่านมา** ซึ่งเป็นเรื่องปกติของ late-cycle bull run ก่อนเกิด correction (หรืออาจไม่เกิดเลยถ้า monetization ตามทัน — ยังไม่รู้)
4. **ความเสี่ยงที่ verify ได้ชัดสุดคือ GPU depreciation accounting** (Section 1.4) — เพราะมี Burry's specific claim + 3 hyperscaler ที่ extend useful-life assumption ไปแล้วจริง (ไม่ใช่ hypothetical)
5. **AMD คือตัวที่ risk/reward แย่สุดในกลุ่ม 3 ตัวตาม valuation percentile ล้วนๆ** (129% above median, ไม่มี cushion) — ถ้า monetization delay เกิดขึ้นจริง AMD น่าจะโดนหนักสุด

**Quinn Conviction (สำหรับ thematic note นี้): 6/10** — ข้อมูล capex/revenue gap และ valuation percentile แข็งแรง verify ได้หลาย source แต่ Cisco dot-com comparison มี confidence ต่ำกว่า (fetch ไม่สำเร็จ ใช้ search digest) และ reverse-DCF implied growth เป็น extrapolation ไม่ใช่ fresh full model — เพียงพอสำหรับ thematic research note แต่ไม่ควรใช้เป็นฐาน trade decision โดยตรงโดยไม่มี fresh Emma/Bear analysis ประกอบ

---

## Sources & References (สรุปรวม)

| # | Data Point | Source | URL | Date Retrieved |
|---|-----------|--------|-----|------------------|
| 1 | Big-4 2026 capex $725B, +77% YoY | Fortune / ValueAddVC | https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/ , https://valueaddvc.com/pulse/big-tech-ai-capex-725-billion-2026-guidance | 2026-09-23 |
| 2 | Amazon capex $200-220B | Techtimes | https://www.techtimes.com/articles/322572/20260731/aws-backlog-hits-496b-amazon-raises-ai-spend-220b-capacity-runs-short.htm | 2026-09-23 |
| 3 | Meta capex $135-145B | ValueAddVC | https://valueaddvc.com/blog/meta-145b-ai-capex-2026-why-zuckerberg-raised-guidance-twice | 2026-09-23 |
| 4 | Hyperscaler total capex (broader estimates $600-800B) | IEEE ComSoc / ALCapital | https://techblog.comsoc.org/2025/12/22/hyperscaler-capex-600-bn-in-2026-a-36-increase-over-2025-while-global-spending-on-cloud-infrastructure-services-skyrockets/ , https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html | 2026-09-23 |
| 5 | Microsoft AI run-rate $37B, +123% YoY | GeekWire | https://www.geekwire.com/2026/microsoft-tops-wall-street-expectations-reports-accelerating-azure-growth-and-37b-ai-run-rate/ | 2026-09-23 |
| 6 | Azure revenue +39% YoY | Futurum | https://futurumgroup.com/insights/microsoft-q2-fy-2026-cloud-surpasses-50b-azure-up-38-cc/ | 2026-09-23 |
| 7 | AWS AI run-rate $25B+, triple-digit growth; AWS total +37% YoY | Techtimes / CNBC | https://www.techtimes.com/articles/322572/20260731/aws-backlog-hits-496b-amazon-raises-ai-spend-220b-capacity-runs-short.htm , https://www.cnbc.com/2026/07/30/aws-earnings-q2-2026.html | 2026-09-23 |
| 8 | Google Cloud +82% YoY, AI products +800% YoY | PYMNTS / Startup Fortune | https://www.pymnts.com/earnings/2026/google-cloud-rides-enterprise-ai-demand-to-82percent-growth/ , https://startupfortune.com/google-cloud-grew-82-in-q2-2026-and-the-514-billion-backlog-tells-you-everything-about-who-is-winning-the-ai-race/ | 2026-09-23 |
| 9 | GPU depreciation useful-life table + Burry $176B claim | Level Headed Investing (2025-12-04) | https://www.levelheadedinvesting.com/p/are-ai-chips-useful-lives-creating-useless-earnings | 2026-09-23 |
| 10 | NVDA price $228.87 / mkt cap $5.53T | stockanalysis.com | https://stockanalysis.com/stocks/nvda/ | 2026-09-22 close |
| 11 | NVDA price $227.38 (cross-check) | Investing.com (via search) | https://www.investing.com/equities/nvidia-corp | 2026-09-22 |
| 12 | AMD price $623.77 / mkt cap $1.02T (crossed $1T) | stockanalysis.com | https://stockanalysis.com/stocks/amd/ | 2026-09-22 close |
| 13 | AVGO price $364.54 / mkt cap $1.74T | stockanalysis.com | https://stockanalysis.com/stocks/avgo/ | 2026-09-22 close |
| 14 | NVDA/AMD/AVGO Fwd P/E, EV/EBITDA, P/S | stockanalysis.com statistics pages | https://stockanalysis.com/stocks/nvda/statistics/ , /amd/statistics/ , /avgo/statistics/ | 2026-09-22 |
| 15 | NVDA EV/EBITDA 47% below 10Y median | GuruFocus | https://www.gurufocus.com/term/enterprise-value-to-ebitda/NVDA | 2026-09-18 (per site) |
| 16 | AMD EV/EBITDA 129% above 10Y median | GuruFocus | https://www.gurufocus.com/term/enterprise-value-to-ebitda/AMD | 2026-06-12 (per site, stale) |
| 17 | AVGO EV/EBITDA 79% above 10Y median | GuruFocus | https://www.gurufocus.com/term/enterprise-value-to-ebitda/AVGO | 2026-09-04 (per site) |
| 18 | NVDA forward P/E fell as price rose | The Motley Fool | https://www.fool.com/investing/2026/07/11/nvidias-forward-pe-has-actually-fallen-as-its-stoc/ | 2026-07-11 |
| 19 | JDS Uniphase P/S 100-110×, mkt cap $125-140B | CNBC | https://www.cnbc.com/id/35663686 | 2026-09-23 (retrieved) |
| 20 | Nortel mkt cap $366B, revenue $9.2B (2000) | Globe and Mail | https://www.theglobeandmail.com/report-on-business/rob-magazine/after-the-bubble-bursts-are-nortel-and-other-tech-stocks-a-good-value-now/article4146633/ | 2026-09-23 (retrieved) |
| 21 | Cisco P/E 201×, EV/Sales 31×, P/FCF 176× (LOW CONFIDENCE — fetch 403'd, from search digest only) | ICIS.com / Harding Loevner (via WebSearch snippet) | https://www.icis.com/chemicals-and-the-economy/2024/06/stock-market-bubbles-follow-the-same-pattern-as-nvidia-and-cisco-confirm/ , https://www.hardingloevner.com/insights/nvidia-and-the-cautionary-tale-of-cisco-systems/ | 2026-09-23 (search only, not fetched) |
| 22 | NVDA FY2027 revenue consensus $411.29B | Seeking Alpha / Hudson Labs (via search) | https://seekingalpha.com/article/4875305-nvidia-accelerating-revenue-growth-into-fy2027-forward-pe-drops-to-25x-upgrade | 2026-09-23 |
| 23 | NVDA FY2028 guidance 70% growth vs 44% analyst avg | 24/7 Wall St | https://247wallst.com/investing/2026/09/22/nvidia-price-prediction-wall-street-and-our-model-finally-agree/ | 2026-09-22 |
| 24 | Prior team rejections (internal) | Quinn's own notes | `agent_notes/quinn/2026-05-16_NVDA.md`, `2026-05-18_AMD.md`, `2026-05-18_AVGO.md` | 2026-05-16/18 |

---

## CFA Concepts Referenced

- **Forward Sharpe Ratio** [CFA L1: Portfolio Management — Risk-Adjusted Performance]
- **Kelly Criterion** [CFA L3: Portfolio Management — Position Sizing]
- **Reverse DCF / Implied Growth Rate** [CFA L2: Equity Valuation — Sensitivity Analysis]
- **EV/EBITDA Percentile / Relative Valuation** [CFA L2: Equity Valuation — Market-Based Valuation]
- **Terminal Value Discounting Mechanics** [CFA L2: Equity Valuation — DCF Models]
- **Depreciation Policy & Earnings Quality** [CFA L1: Financial Reporting — Quality of Earnings] *(เสริมจาก non-CFA source แต่ concept ตรง กับ FRA)*

---

*Quinn | 2026-09-23 | Thematic Research Note — AI Circular Financing / Bubble Framing*
*ไม่ใช่ ticker-level BUY/SELL recommendation — สำหรับ Charlie ใช้ประกอบ Research publication เท่านั้น*
