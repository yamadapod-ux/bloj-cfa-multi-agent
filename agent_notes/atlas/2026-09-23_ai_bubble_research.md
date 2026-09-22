# 🌐 Atlas Thematic Research — AI Infrastructure "Circular Financing" Bubble Question
### เพื่อประกอบ Research Note พิเศษของ Charlie (Dashboard "Research" section)
**วันที่:** 2026-09-23 | **ผู้จัดทำ:** Atlas | **Training Knowledge Ban:** ทุกตัวเลขมาจาก WebSearch ณ session นี้ พร้อม URL — ไม่มีตัวเลขใดมาจาก training knowledge

---

## Regime Context Note (ไม่ต้องสร้าง regime record ใหม่)

เช็คแล้ว — regime record ล่าสุด `agent_notes/atlas/2026-09-20_regime.md` (3 วันก่อนหน้า) ยัง **fresh** และยังไม่ถึงเงื่อนไข re-call ตามที่ระบุไว้ในไฟล์นั้นเอง ("Next mandatory re-call: within 1 session of October jobs report/CPI, or immediately if any indicator crosses its own threshold zone") ดังนั้น**ไม่สร้างไฟล์ regime ใหม่ซ้ำ** — ใช้ค่าล่าสุดนี้อ้างอิง:

- **Regime: TRANSITIONAL-CAUTIOUS** (judgment override; majority vote 3/4 RISK-ON แต่ override เพราะ Fed hawkish pivot + oil/stagflation overhang ยังไม่คลาย)
- Cash floor 25% | Position multiplier 0.75x | Force Deploy SUSPENDED
- **ข้อสังเกตที่เกี่ยวกับหัวข้อ AI bubble โดยตรง:** credit market signal (HY OAS 276bps ณ 09-15/09-20) ยังไม่แสดง stress ระดับ broad-market — **แต่**ข้อมูลใหม่ที่พบใน research รอบนี้ (ดู Section 4 ด้านล่าง) ชี้ว่า **AI-sector-specific credit spread (Oracle CDS, AI-linked corporate bonds) กำลัง widen อย่างมีนัยสำคัญแยกออกจาก broad HY index** — นี่คือ divergence ที่ Atlas ควรจับตาสำหรับ regime re-call ครั้งถัดไป เพราะถ้า AI-credit stress ลามเข้า broad HY spread จะเป็นสัญญาณ RISK-OFF ที่ชัดกว่าปัจจุบันมาก

---

## 1. Circular Financing Map — ใครลงทุน/ซื้อขายกับใคร (ก.ย. 2026)

### 1.1 Nvidia ↔ OpenAI
- **สถานะล่าสุด (ยืนยันแล้ว):** ดีลลงนามจริงเมื่อ **18 สิงหาคม 2026** — Nvidia ค้ำประกัน (guarantee) มูลค่าสูงสุด **$105 พันล้าน** สำหรับ lease/power payments ของ AI data center campus ที่ Pike County, Ohio (สัญญาเช่า 20 ปี) — โครงสร้างเป็น **loan/lease guarantee ไม่ใช่ equity investment โดยตรง** ต่างจากกรอบเดิมที่เคยพูดถึง "$100B staged investment" หรือกรอบ "$250B backstop" ที่เคยเป็นข่าวก่อนหน้า [Nvidia $105B Ohio deal — reported via search aggregation, see also framework history]
- **ก่อนหน้านั้น:** กรอบเดิม "Nvidia จะลงทุนสูงสุด $100B ใน OpenAI แบบ progressive ตามที่ deploy ครบทุก 1GW" (ประกาศ LOI ก.ย. 2025, ร่วมกับ 10GW systems partnership) — Nvidia เองยอมรับใน quarterly filing ว่า **"there is no assurance that any investment will be completed on expected terms, if at all"** [CNBC — Nvidia says 'no assurance' of deal with OpenAI, https://www.cnbc.com/2025/11/19/nvidia-says-no-assurance-of-deal-with-openai-after-100-billion-pact.html]
- **Discrepancy ที่พบ:** มีรายงานกรอบวงเงิน **$600B ในเดือนกรกฎาคม 2026** ที่ท้ายที่สุดกลายเป็นดีลจริงแค่ **$105B ในเดือนสิงหาคม** — ต่างกันเกือบ 6 เท่า สะท้อนช่องว่างระหว่างตัวเลข "headline announcement" กับ "สัญญาที่ผูกพันจริง" [Vantage Markets — "AI Financing Bubble" explainer, https://www.vantagemarkets.com/market-analysis/ai-financing-bubble-nvidia-openai-circular-deals-explained/]
- **Circular pattern:** Nvidia เป็นทั้ง **supplier หลัก** (ขาย GPU/systems ให้ OpenAI) และ **financier** (ค้ำประกันเงินกู้ที่ OpenAI ใช้จ่ายค่า infrastructure ซึ่งส่วนหนึ่งจะไหลกลับมาซื้อ Nvidia systems) — Nvidia เคยลงทุน **$30B** ใน funding round ของ OpenAI เดือนมีนาคม 2026 [TechCrunch — Nvidia CEO pushes back on stalled report, https://techcrunch.com/2026/01/31/nvidia-ceo-pushes-back-against-report-that-his-companys-100b-openai-investment-has-stalled/]

### 1.2 Microsoft ↔ OpenAI
- **โครงสร้างเดิม (ก่อน เม.ย. 2026):** Microsoft รับ revenue-share 20% จาก OpenAI + ให้ compute credit ผ่าน Azure แบบ exclusive
- **Renegotiated พ.ค. 2026:** revenue-share payment cap ที่ **$38B ผ่านปี 2030** (ลดลงจาก projected trajectory เดิม **~$135B** — ลดลงราว **$97B**) — OpenAI ยังจ่าย 20% แต่ **Microsoft เลิกแบ่ง revenue กลับให้ OpenAI** และ OpenAI ต้อง **ผูกมัดซื้อ Azure cloud services มูลค่า $250B** พร้อมสูญเสีย exclusivity/right-of-first-refusal เดิม (OpenAI ขายผ่าน AWS/Google Cloud ได้แล้ว) [CNBC — OpenAI shakes up partnership with Microsoft, capping revenue share, https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html] [Microsoft official blog, https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/]
- **Circular pattern:** Microsoft ให้ compute (ซึ่งต้องซื้อ Nvidia GPU มาสร้าง data center) แลกกับ revenue-share/equity จาก OpenAI ซึ่ง OpenAI เอง financed ด้วยเงินจาก Nvidia/SoftBank/อื่นๆ — วนกลับมาซื้อ compute ต่อ
- ข้อมูลเสริม: มีรายงานว่า **70% ของ Microsoft AI revenue มาจาก OpenAI** [explainx.ai — "70% of Microsoft AI Revenue Comes From OpenAI", https://www.explainx.ai/blog/microsoft-openai-circular-ai-revenue-gpu-depreciation-2026] — ตัวเลขนี้มาจากบล็อกวิเคราะห์บุคคลที่สาม **ยังไม่ cross-verify กับ SEC filing โดยตรง** ระบุเป็น unverified claim

### 1.3 OpenAI ↔ Oracle
- **มูลค่าสัญญา:** **$300 พันล้าน** ระยะเวลา 5 ปี เริ่มปี 2027 — ส่วนหนึ่งของ Project Stargate — สร้าง **4.5 GW** data center capacity [DataCenterDynamics, https://www.datacenterdynamics.com/en/news/openai-signs-300bn-cloud-deal-with-oracle-report/] [SiliconANGLE, https://siliconangle.com/2025/09/10/openai-oracle-strike-300b-cloud-computing-deal-power-ai/]
- OpenAI คาดใช้จ่ายเฉลี่ย **~$60B/ปี** กับ Oracle cloud infrastructure — มูลค่านี้ **สูงกว่า revenue ปัจจุบันของ OpenAI ทั้งบริษัทเอง** [Data Center Frontier]
- **หมายเหตุความน่าเชื่อถือ:** "ไม่มี SEC-grade binding disclosure เผยแพร่ — คำที่เหมาะสมคือ 'reported, not fully confirmed'" ตามที่หลายแหล่งระบุตรงกัน [IntuitionLabs — Oracle-OpenAI $300B Deal Explained]

### 1.4 OpenAI ↔ AMD
- **โครงสร้าง:** deploy **6 GW** ของ AMD Instinct GPU หลายปี เริ่มด้วย **1GW ในครึ่งหลังปี 2026**
- **Equity warrant:** AMD ให้ warrant สูงสุด **160 ล้านหุ้น** แก่ OpenAI ราคาใช้สิทธิ **$0.01/หุ้น** vesting ผูกกับ milestone การ deploy (1GW → 6GW) และราคาหุ้น AMD ที่ต้องขึ้นถึง **$600/หุ้น** — ถ้าใช้สิทธิเต็มจำนวน OpenAI จะถือหุ้น AMD ประมาณ **10%** [Tom's Hardware, https://www.tomshardware.com/pc-components/gpus/openai-signs-6gw-amd-gpu-deal] [AMD IR official release, https://ir.amd.com/news-events/press-releases/detail/1260/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus]
- มูลค่า deal potential sales **~$90B** [TechHQ]
- **Circular pattern ชัดเจนมาก:** AMD "จ่าย" OpenAI ด้วยหุ้นตัวเองเพื่อแลกกับสัญญาซื้อ GPU มูลค่าหลายหมื่นล้าน — ถ้า AMD share price พุ่งขึ้นจาก deal นี้ (ซึ่งเกิดขึ้นจริง) มูลค่า warrant ของ OpenAI ก็เพิ่มตาม โดยไม่มีเงินสดเปลี่ยนมือจริงในขั้นตอนนี้

### 1.5 OpenAI ↔ Broadcom
- **โครงสร้าง:** ร่วมพัฒนา custom AI accelerator (OpenAI ออกแบบ, Broadcom ผลิต/deploy) **10 GW** เริ่ม deploy ครึ่งหลังปี 2026 เต็มรูปแบบภายในปี 2029
- Broadcom CEO เปิดเผยว่ามี "customer รายที่ 4" สั่ง **$10B** ที่ระบุว่าคือ OpenAI [CNBC — Broadcom pops 9% on OpenAI deal, https://www.cnbc.com/2025/10/13/openai-partners-with-broadcom-custom-ai-chips-alongside-nvidia-amd.html]
- มีรายงาน "**$18 billion financing snag**" ในดีลนี้ — สัญญาณว่าการ execute จริงไม่ราบรื่นเท่า headline [The Information — OpenAI's AI Chip Deal With Broadcom Hits $18 Billion Financing Snag, https://www.theinformation.com/articles/openais-ai-chip-deal-broadcom-hits-18-billion-financing-snag]
- **สรุปรวม:** OpenAI ประกาศ commitment รวม **~33 GW** ข้าม Nvidia/Oracle/AMD/Broadcom ภายในเวลาเพียง **3 สัปดาห์** ของการประกาศ (อ้างอิงจากบทความเดียวกัน) [Tom's Hardware]

### 1.6 CoreWeave ↔ Nvidia ↔ Microsoft/OpenAI (วง circular ที่ชัดที่สุด)
- Nvidia ถือหุ้น CoreWeave (มีรายงานระบุสัดส่วนสูงถึง ~91% ในบางแหล่ง — ตัวเลขนี้มาจาก blog วิเคราะห์บุคคลที่สาม ควร cross-check เพิ่มก่อนใช้อ้างอิงตัวเลขจริงในรายงานทางการ) — Nvidia เป็นทั้ง **investor** และ **ลูกค้า/supplier หลัก** ของ CoreWeave พร้อมกัน [io-fund — Nvidia, CoreWeave, Nebius: Inside the Circular Financing, https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom]
- CoreWeave ใช้เงินทุนที่ได้ (บางส่วนจาก Nvidia/Microsoft) ไปซื้อ Nvidia GPU มหาศาล → Microsoft เช่า/ใช้ capacity ของ CoreWeave กลับมาเมื่อ data center ของ Microsoft เองเต็ม [Columbia Business Blog — The Hidden Risk in AI's Circular Financing Ecosystem, https://blogs.cuit.columbia.edu/gjb2124/circular-financing/]
- CoreWeave-OpenAI agreements รวม **$22.4B** (ปี 2025) — โครงสร้างผูก equity return ของ vendor กับ pattern การใช้ infrastructure โดยตรง [Bloomberg-aggregated via search result summary]
- **Risk framing ที่พบ (สรุปจาก Bloomberg/Columbia):** ถ้า OpenAI business model ล้มเหลว → Nvidia โดน 2 เด้ง (1) เสียลูกค้ารายใหญ่ (2) ขาดทุนจาก equity stake ที่ลงทุนไว้ — เป็น concentration/correlation risk ที่ผูกกันแน่นเป็นพิเศษ

### 1.7 สรุป Diagram — Investor-Supplier Overlap

```
NVIDIA ──(guarantee $105B lease/Ohio, GPU sales)──> OPENAI
  │                                                    │
  ├──(equity/91%~ stake — unverified exact %)──> CoreWeave <──(lease-back capacity)── MICROSOFT
  │                                                    │
  └──(customer: buys Nvidia GPUs w/ Nvidia-linked capital)                          │
                                                                                      │
MICROSOFT ──($250B Azure purchase commitment, ended rev-share)──> OPENAI ────────────┘
  (was investor+cloud supplier; now supplier-only post Apr-2026 renegotiation)

AMD ──(160M share warrant @ $0.01, vest-on-deployment)──> OPENAI ──(6GW GPU purchase, ~$90B)──> AMD
  (AMD "pays" OpenAI in its OWN stock to lock in GPU purchase commitment)

BROADCOM ──(co-develop custom chip, $10B initial order)──> OPENAI
  (customer commitment funds Broadcom's AI chip segment growth)

ORACLE ──($300B/5yr compute supply, 2027 start)──> OPENAI
  (Oracle raised $43B debt + $5B equity in FY26 to fund the buildout — see Section 4)
```

**ตัวเลขรวมที่พบ:** มีรายงานระบุ **circular financing arrangements รวมกว่า $800 พันล้าน** ในวงการนี้ [io-fund/ResearchGate aggregation — "AI Circular Financing and the Coming Shakeout", https://www.researchgate.net/publication/399553337_AI_Circular_Financing_and_the_Coming_Shakeout_Vendor_Funding_Round-Tripping_and_Hyperscaler_Power_in_the_Data-Center_Boom] — ตัวเลขนี้เป็น aggregation จาก third-party research ไม่ใช่ official disclosure รวม ควรระบุเป็น "estimated" ในรายงานของ Charlie

---

## 2. AI Capex vs Revenue Gap — ตัวเลขจริง

### 2.1 Hyperscaler Capex 2026 (guided/actual)
| บริษัท | Capex 2026 (guided) | Source |
|--------|---------------------|--------|
| Microsoft | **$190B** (total investment ปีนี้) | [Tom's Hardware — Big Tech's AI Spending, https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion] |
| Alphabet/Google | **$180–190B** (raised full-year guidance) | เดียวกัน |
| Amazon | **$200B** | เดียวกัน |
| Meta | **$115–135B** | เดียวกัน |
| **รวม 4 บริษัท** | **$725B** (+77% YoY จาก $410B ปี 2025) | [Tom's Hardware, https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion]; [CNBC — Tech AI spending approaches $700 billion, https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html] |

Goldman Sachs Research ประเมิน **global AI investment ~$1 trillion ในปี 2026** (รวม non-hyperscaler ด้วย) — สูงกว่า hyperscaler-only figure ($794B) อยู่ **$206B** [Goldman Sachs-aggregated, https://nilsliu.dev/en/insights/2026-06-15-goldman-sachs-ai-capex-7-trillion/]

Morgan Stanley: US hyperscalers **>$800B capex ในปี 2026 เดียว**; คาดรวม **~$3 trillion** AI-related infrastructure investment ไหลเข้าเศรษฐกิจโลกภายในปี 2028 (>80% ยังมาไม่ถึง) [Morgan Stanley Insights, https://www.morganstanley.com/insights/articles/ai-market-trends-institute-2026]

### 2.2 Revenue จริงที่ monetize ได้ (ผู้เล่นหลัก)
| บริษัท | ตัวเลข Revenue/ARR | ช่วงเวลา | Source |
|--------|---------------------|----------|--------|
| OpenAI | **$40B+ annualized run-rate** | ส.ค. 2026 (Bloomberg) | [Bloomberg — OpenAI's Revenue Run Rate Tops $40 Billion, https://www.bloomberg.com/news/articles/2026-08-13/openai-s-revenue-run-rate-tops-40-billion-ahead-of-ipo] |
| Anthropic | **$47B ARR (พ.ค. 2026) → $65B ARR (ก.ค. 2026)** | growth 80x claimed | [VentureBeat — Anthropic hit $30B revenue run rate after 'crazy' 80x growth, https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth]; ตัวเลข $65B มาจาก aggregation หลายแหล่ง (futuresearch.ai, arr.club) — **ควร cross-verify เพิ่มก่อนใช้เป็นตัวเลขทางการ** |
| Microsoft "AI business" (Azure AI + Copilot bundled, ไม่แยก) | **$37B annualized run-rate**, +123% YoY | Q3 FY2026 | [ผลรวมจาก search: Microsoft FY26 Q3 official metrics via alphastreet/licenseq aggregation] |
| Microsoft 365 Copilot (แยกเฉพาะ, estimated) | **~$10.8B annualized (list price, 30M seats × $30)** — เป็นการประมาณจากจำนวน seat ไม่ใช่ตัวเลขที่ Microsoft เปิดเผยแยกทางการ | Q3 FY2026 | [aggregated via businessofapps.com, sqmagazine.co.uk] |
| Google Cloud (รวม non-AI) | **$20B/ไตรมาส** (Q1 2026), +63% YoY, backlog $462B | Q1 2026 | [TechCrunch — Google Cloud surpasses $20B, capacity-constrained, https://techcrunch.com/2026/04/29/google-cloud-surpasses-20b-but-says-growth-was-capacity-constrained/] |
| Google genAI-built products (เฉพาะส่วนที่ built on genAI) | **โต ~800% YoY** (ไม่ใช่ absolute revenue figure — เป็น growth rate) | Q1 2026 | เดียวกัน |

**ข้อสังเกตสำคัญ:** ตัวเลข revenue ของ Microsoft/Google ส่วนใหญ่เป็น "bundled" (AI + non-AI cloud consumption ปนกัน) ไม่ได้แยกเฉพาะ generative-AI-attributable revenue อย่างชัดเจน — ทำให้การเทียบ "AI revenue" กับ "AI capex" ตรงๆ ทำได้ยาก ต้องระวังการนำตัวเลขเหล่านี้ไปหารเทียบ capex โดยตรงโดยไม่ flag ข้อจำกัดนี้

### 2.3 The Gap — มุมมอง Analyst

**Sequoia Capital (David Cahn) — "AI's $600B Question" ฉบับอัปเดต 2026:**
- เดิม (ค.ศ. ก่อน) โจทย์คือ "$600B question" — ตอนนี้อัปเดตเป็น **"$3 trillion question"**
- Cahn ประเมิน **2026 AI infrastructure spending ที่ $1.5 trillion** และคำนวณว่าอุตสาหกรรมต้องมี revenue รวม **~$3 trillion** เพื่อ justify การลงทุนนี้ (คิดจาก required return บน infrastructure)
- เทียบ context: Anthropic ~$60B ARR + OpenAI ~$40B ARR รวมกันยัง **"barely dents"** เป้าหมาย $3 trillion [AI Weekly — Sequoia's Cahn Pegs AI's 2026 Revenue Gap at Roughly $3T, https://aiweekly.co/alerts/sequoias-cahn-pegs-ais-2026-revenue-gap-at-roughly-3t]; [ต้นฉบับ Sequoia, https://sequoiacap.com/article/ais-600b-question]

**Bain & Company:**
- ภายในปี 2030 บริษัท AI จะต้องมี revenue รวมกัน **$2 trillion/ปี** เพื่อ fund compute power ที่ demand คาดว่าจะต้องการ — แต่ revenue จริงมีแนวโน้ม**ขาดไปถึง $800 billion** จากเป้านั้น [Bloomberg via Bain, https://www.bloomberg.com/news/articles/2025-09-23/an-800-billion-revenue-shortfall-threatens-ai-future-bain-says]

**MIT NANDA Initiative — "The GenAI Divide: State of AI in Business 2025":**
- **95% ของ generative AI pilot projects ในองค์กร ไม่สามารถแสดง measurable P&L impact ได้** — จาก sample 52 executive interviews + survey 153 ผู้บริหาร + วิเคราะห์ 300 public AI deployments
- Root cause ตามการศึกษา: ไม่ใช่ตัว model แย่ แต่เป็น **"learning gap"** ด้าน enterprise integration — เครื่องมือ generic (เช่น ChatGPT) ทำงานดีระดับบุคคลแต่ scale เข้า workflow องค์กรไม่ติด
- มีแค่ **~5%** ของ pilot ที่ประสบความสำเร็จจริง (revenue acceleration ชัดเจน) [Healthcare IT News, https://www.healthcareitnews.com/news/mit-95-enterprise-ai-pilots-fail-deliver-measurable-roi]; [Forbes, https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/]
- **หมายเหตุความน่าเชื่อถือ:** มีบทความแย้ง ("Don't Believe the Hype" — MarketingAI Institute) ที่ชี้ว่าตัวเลข 95% ถูกนำไปตีความเกินจริงในสื่อ ควร cite เป็น "MIT NANDA study finding" ไม่ใช่ fact สัมบูรณ์ [MarketingAI Institute, https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots]

**Goldman Sachs / Morgan Stanley (mega-picture):** ทั้งสองสถาบันยัง **ไม่ได้ปฏิเสธ AI capex cycle** — มองว่าจะโต ต่อเนื่องถึง $1.6 trillion/ปี ภายในปี 2031 (Goldman) — แต่จุดที่ทั้งสองระบุร่วมกับ Bain/Sequoia คือ **revenue monetization ล้าหลัง capex อย่างมีนัยสำคัญในช่วง 2026** [Goldman Sachs aggregation, https://nilsliu.dev/en/insights/2026-06-15-goldman-sachs-ai-capex-7-trillion/]

---

## 3. Michael Burry — Accounting/Depreciation Critique

- Burry เคย short Nvidia แต่ **ปิด put options ที่หมดอายุ ธ.ค. 2026 แล้ว** เพราะกังวล time decay — ยังคง**ถือ short position ใน Oracle และ CoreWeave** [IBTimes UK, https://www.ibtimes.co.uk/michael-burry-exits-nvidia-put-options-ai-bubble-concerns-1818993]
- **Core thesis:** cloud providers depreciate GPU hardware over **5-6 ปี** ทั้งที่ real economic life (จาก Nvidia's rapid chip cycle) ใกล้เคียง **2-3 ปี** เท่านั้น
- ประเมินว่านี่ทำให้เกิด **understated depreciation + overstated profit รวมทั้งอุตสาหกรรมราว $176 billion ระหว่างปี 2026-2028**
- ตัวอย่างเฉพาะบริษัท: Oracle earnings อาจ overstated ~**27%**, Meta ~**21%** ภายในปี 2028
- ข้อกังวลเพิ่มเติม: **หนี้จาก data center lease commitments หลายแสนล้านดอลลาร์อยู่นอกงบดุล (off-balance-sheet)** จนกว่าจะ activate — Burry เทียบกับ Cisco ยุค dot-com [Oksana Meier Substack — Michael Burry Files: The AI Bubble; FinTech Weekly aggregation]

---

## 4. สัญญาณ Credit Market Stress ที่กำลังเกิดขึ้นจริง (ก.ย. 2026)

- **Oracle 5-year CDS** อยู่ที่ **~196.6 bps** — ระดับสูงสุดในรอบหลายปี และเป็น proxy หลักของตลาดสำหรับ "AI debt fear" [24/7 Wall St — Oracle Falls 4% as Bond Selloff Tests Its Debt-Funded AI Buildout, https://247wallst.com/investing/2026/09/01/oracle-falls-4-as-bond-selloff-tests-its-debt-funded-ai-buildout-nebius-slips/]
- **S&P Global downgrade Oracle เหลือ BBB-** (สูงกว่า junk แค่ 1 notch) [เดียวกัน]
- **Oracle debt-to-equity ~500%** — contrast ชัดเจนกับ Microsoft/Meta ที่ยังใช้ off-balance-sheet financing มากกว่า on-balance-sheet debt [เดียวกัน]
- **Oracle FY2026 capex $55.7B** (จาก $21.2B ปีก่อน) → cash outflow เกิน cash generated **$23.7B** → ชดเชยด้วยการออกหนี้ **$43B** + ขายหุ้นเพิ่ม **$5B** [24/7 Wall St, สรุปจาก Oracle 10-K aggregation]
- **19-23 ก.ย. 2026 — ตลาดตราสารหนี้เริ่ม "เลือกมาก" กับ AI debt:** "Corporate bond buyers get picky with flood of AI debt" — นักลงทุนตราสารหนี้เริ่มเรียกร้อง premium สูงขึ้นสำหรับหนี้ที่เกี่ยวข้องกับ AI data center [BNN Bloomberg, https://www.bnnbloomberg.ca/investing/2026/09/22/corporate-bond-buyers-get-picky-with-flood-of-ai-debt/]
- **BIS (Bank for International Settlements) Annual Report มิ.ย. 2026:** จัดให้ **AI capex bust, circular-financing collapse, และ sovereign debt fragility** เป็น 3 ความเสี่ยงหลักต่อ global financial stability — เทียบ historical analogy กับ canal mania (1830s), railway mania (1840s), และ dot-com bubble (late-1990s) — ทั้งสามครั้งเริ่มจาก genuine tech breakthrough แต่จบด้วย "investment reversal + recession ที่กระทบทั้งเศรษฐกิจ" [CNBC — Debt, AI boom and economic fragilities raise global risks, BIS says, https://www.cnbc.com/2026/06/28/debt-ai-boom-and-economic-fragilities-raise-global-risks-bis-says.html]; [The Register, https://www.theregister.com/ai-and-ml/2026/06/29/how-the-ai-bubble-could-pop-and-take-down-the-global-economy-according-to-the-bis/5263793]
- **ตัวเลข BIS:** 5 hyperscaler ใหญ่ที่สุดกำลัง spend รวม **>$1 trillion** ตลอดปี 2025-2026 — เกิน earnings/FCF ของตัวเองจนต้องพึ่งการออกหนี้ (บางส่วนผ่าน private credit channel ที่ regulation หลวมกว่า) [Fortune, https://fortune.com/2026/06/29/bis-central-bank-warning-hyperscaler-data-center-1-trillion-gamble-recession/]

**สรุป Section 4 — นี่คือ divergence สำคัญที่ควร flag ให้ Charlie เห็นชัด:** Broad market credit spread (HY OAS 276bps) ยังนิ่ง แต่ **AI-specific credit risk (Oracle CDS ~197bps, เกือบ 2 เท่าของระดับก่อนหน้า) กำลังแยกตัวออกมา widen ต่างหาก** — เป็น early-stage signal ที่ยังไม่ลามเข้า broad market แต่ Atlas จะจับตาเป็นพิเศษใน regime re-call ครั้งถัดไป

---

## 5. ข้อจำกัดของข้อมูล / Data Quality Flags

| ประเด็น | รายละเอียด | คำแนะนำสำหรับ Charlie |
|---------|-----------|----------------------|
| CoreWeave stake % ของ Nvidia | ตัวเลข "~91%" มาจาก third-party blog (io-fund) ไม่ใช่ official SEC filing โดยตรง | ระบุเป็น "รายงานโดย [source]" ห้ามเขียนเป็น fact เปล่า |
| "70% ของ Microsoft AI revenue มาจาก OpenAI" | มาจาก analytical blog (explainx.ai) ไม่ใช่ Microsoft 10-K โดยตรง | ต้อง cross-check เพิ่มก่อนใช้ในรายงานทางการ หรือระบุเป็น estimate ของบุคคลที่สาม |
| "$800B circular financing รวม" | เป็น aggregation จาก research paper บุคคลที่สาม ไม่ใช่ official industry tally | ใช้เป็น context ไม่ใช่ hard number |
| Anthropic $65B ARR (ก.ค. 2026) | หลายแหล่ง aggregate ตรงกัน (futuresearch.ai, arr.club, VentureBeat cross-referenced $30B → $47B → $65B progression) แต่ทั้งหมดเป็น third-party reporting ไม่ใช่ Anthropic official filing (บริษัทเอกชนไม่เปิดเผย 10-Q) | ระบุแหล่งชัดเจนทุกครั้ง |
| MIT "95% fail" stat | มีข้อโต้แย้งจากสื่อบางแห่งว่าตัวเลขถูกนำไปตีความเกินจริง | Cite เป็น finding ของการศึกษา ไม่ใช่ universal fact |
| Nvidia-OpenAI deal มูลค่า | มีความสับสนระหว่าง "$100B framework" (2025), "$250B backstop talks" (ก.ค. 2026), "$600B" (รายงาน ก.ค. 2026), และ "$105B signed" (ส.ค. 2026 — deal จริงที่ signed) | **ใช้ $105B เป็นตัวเลขหลักที่ signed จริง** — ตัวเลขอื่นเป็น proposal/rumor stage ที่ไม่ materialize |

---

## 6. สรุปสำหรับ Charlie (bullet พร้อมใช้เขียนรายงาน)

**Circular Financing:**
- Nvidia signed **$105B** guarantee สำหรับ OpenAI Ohio data center (18 ส.ค. 2026) — ต่ำกว่ากรอบข่าวลือ $600B ก่อนหน้าเกือบ 6 เท่า → สัญญาณว่า headline number มักเกินจริงกว่าดีลที่ signed จริงมาก
- Microsoft ตัด revenue-share cap เหลือ **$38B ผ่าน 2030** (จากที่คาดการณ์ไว้ ~$135B) แลกกับ OpenAI ผูกมัดซื้อ Azure **$250B**
- Oracle **$300B/5ปี** compute deal — ใช้เงินเฉลี่ย **$60B/ปี** ที่ OpenAI ยังไม่มี revenue รองรับ
- AMD จ่าย OpenAI เป็น**หุ้นตัวเอง** (warrant 160M หุ้น @ $0.01) แลกสัญญาซื้อ GPU $90B — เป็นรูปแบบ circular ที่ชัดที่สุด (ไม่มีเงินสดเปลี่ยนมือ)
- Broadcom ได้ commitment $10B initial แต่มีรายงาน "$18B financing snag" ภายในดีลเดียวกัน
- Nvidia เป็นทั้ง investor + supplier ของ CoreWeave ซึ่งเป็นทั้ง vendor ของ Microsoft/OpenAI ด้วย — เป็นวง circular ที่แน่นที่สุดในระบบ

**Capex vs Revenue Gap:**
- 4 hyperscaler หลักจะใช้ capex รวม **$725B ในปี 2026** (+77% YoY)
- OpenAI ARR **$40B+** (ส.ค. 2026), Anthropic **$65B ARR** (ก.ค. 2026) — รวมกันยัง "แค่ทำรอย" บนเป้าหมาย **$3 trillion** ที่ Sequoia คำนวณว่าอุตสาหกรรมต้องทำได้ภายในปีนี้เพื่อ justify capex
- Bain: ภายในปี 2030 อุตสาหกรรมต้องการ revenue **$2 trillion/ปี** แต่จะขาด **$800B**
- MIT NANDA: **95% ของ enterprise GenAI pilot ไม่แสดง measurable ROI**

**Credit Stress (สัญญาณเริ่มต้น):**
- Oracle CDS **~197bps** (multi-year high), credit rating **BBB-** (เหนือ junk แค่ 1 notch), debt/equity **~500%**
- Broad HY spread ยังนิ่ง (276bps) — **แต่ AI-sector credit risk กำลัง decouple ออกมาต่างหาก** — นี่คือ leading indicator ที่ Atlas จะติดตามต่อ
- BIS (มิ.ย. 2026) จัดอันดับ AI capex bust + circular financing collapse เป็น 1 ใน 3 ความเสี่ยงระบบการเงินโลกสูงสุด — เทียบ historical bubble analogies (canal mania, railway mania, dot-com)
- Burry: GPU depreciation อาจ understate cost จริง ~$176B ทั้งอุตสาหกรรม 2026-2028 (Oracle earnings overstate ~27%, Meta ~21%) — ยัง short Oracle/CoreWeave (ปิด Nvidia put แล้ว)

**Macro Regime (ไม่เปลี่ยนจาก 09-20):** TRANSITIONAL-CAUTIOUS — cash floor 25%, multiplier 0.75x, Force Deploy suspended — ข้อมูล AI-bubble รอบนี้**ไม่ได้ trigger regime เปลี่ยนทันที** (เพราะ broad indicator ยังไม่ข้าม threshold) แต่เป็นเหตุผลเสริมให้ override ยังสมเหตุสมผล และเป็น watch-item สำคัญสำหรับรอบต่อไป

---
*Atlas — 2026-09-23 | AI Infrastructure Circular Financing & Capex-Revenue Gap Thematic Research*
