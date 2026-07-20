import re

# อ่านไฟล์เดิม
with open(r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\news.js", "r", encoding="utf-8") as f:
    old_content = f.read()

# ดึงส่วน NEWS array เดิม (เอาทุกอย่างหลัง "const NEWS = [" ถึง "];")
match = re.search(r'const NEWS = \[(.*?)\];', old_content, re.DOTALL)
if not match:
    print("ERROR: ไม่พบ NEWS array ในไฟล์เดิม")
    exit(1)

old_news_body = match.group(1).strip()

# ข่าวใหม่วันที่ 2026-05-27
new_news = """  // ── 2026-05-27 ──────────────────────────────────────────────────────────────
  {
    date: "2026-05-27", category: "MACRO",
    headline: "S&P 500 ทำ ATH ใหม่ 7,519.12 (+0.61%) วันที่ 26 พ.ค. — Nasdaq ATH 26,656.18 (+1.19%) นำโดย Tech + Iran peace talks",
    summary: "S&P 500 ปิดที่ 7,519.12 (+0.61%) วันที่ 26 พ.ค. 2026 ทำ all-time high ใหม่ — Nasdaq +1.19% ที่ 26,656.18 ก็ ATH ใหม่ — Dow Jones -0.23% ที่ 50,461.68 — ตลาดถูกหนุนโดย: (1) Trump ระบุ US-Iran negotiations 'proceeding nicely' ลด geopolitical risk (2) Micron MU พุ่ง +19-25% หลัง UBS ปรับ PT เป็น $1,625 (triple) และ market cap ทะลุ $1T (3) Tech sector lead ยืนยัน AI spending thesis — S&P 500 futures วันที่ 27 พ.ค. +0.15% เช้า — ยืนยัน RISK-ON regime ต่อเนื่อง",
    impact: "POSITIVE", tickers: ["ADBE", "NOW", "GOOGL", "MSFT", "META", "AMZN", "TSLA"],
    url: "https://www.cnbc.com/2026/05/26/stock-market-today-live-updates.html",
  },
  {
    date: "2026-05-27", category: "MACRO",
    headline: "Fed rate คง 3.5-3.75% — Kevin Warsh เตรียมนำ FOMC June 16-17 + dot plot ใหม่ — ตลาด price in hike 40%",
    summary: "Fed Funds Rate ยังคงที่ 3.5-3.75% จาก FOMC Apr 29 (มติ 8-4 dissent สูงสุดตั้งแต่ Oct 1992) — Kevin Warsh เข้ารับตำแหน่ง Fed Chair แทน Powell ที่พ้น term พ.ค. — FOMC ถัดไป June 16-17 จะมี updated dot plot (SEP) ซึ่งตลาดจับตาใกล้ชิด — Fed H.15 วันที่ 26 พ.ค.: 10Y Treasury 4.58% — ตลาด price in ~40% probability rate hike ก่อนสิ้นปี 2026 vs median dot plot ยังชี้ 2 cuts ใน 12M ถัดไป (แต่ timing เลื่อนออกไป) — หมายเหตุ: ถ้า Warsh hawkish กว่า Powell → หุ้น growth ทุกตัวใน portfolio มี downside risk",
    impact: "NEGATIVE", tickers: ["ADBE", "NOW", "GOOGL", "MSFT", "META"],
    url: "https://www.federalreserve.gov/releases/h15/",
  },
  {
    date: "2026-05-27", category: "EARNINGS",
    headline: "MRVL Marvell Technology — Q1 FY2027 รายงานคืนนี้ AH — consensus $2.4B revenue +27% EPS $0.80 — หุ้น +100% YTD",
    summary: "Marvell Technology (MRVL) รายงาน Q1 FY2027 หลังปิดตลาดวันที่ 27 พ.ค. 2026 — consensus: revenue $2.4B (+27% YoY), EPS $0.80 — ราคาปัจจุบัน $196.33 หลังขึ้นมา ~100% ในปี 2026 — MRVL สร้าง custom AI chips (XPUs) ให้ hyperscalers — FY2026 revenue $8.195B (+42% YoY) — Q4 FY2026 EPS $0.80 beat $0.71 (12.68%) — analyst upgrades: BofA PT $200, Goldman $200, Melius $220 — AI-driven custom silicon thesis แข็งแกร่ง — เป็น high-impact event สำหรับ AI semiconductor ecosystem",
    impact: "MIXED", tickers: ["MRVL", "NVDA", "AVGO", "TSM"],
    url: "https://moneymorning.com/2026/05/25/marvell-technology-mrvl-stock-earnings-may-2026",
  },
  {
    date: "2026-05-27", category: "EARNINGS",
    headline: "AVGO Broadcom — earnings June 3 approaching — custom AI chip +140% QoQ + BCM68850 home gateway launch — ราคา $422",
    summary: "Broadcom ราคา $422.59 (26 พ.ค. range $413-$435) — earnings June 3 กำลังจะมา — Q1 FY2026 (Jan 2026): custom AI chip revenue +140% QoQ, data-center networking +60% — BCM68850 new home-gateway chip ด้วย built-in AI ทำ AVGO ขึ้น +2% วันที่ 26 พ.ค. — Evercore ISI ปรับ PT $490 เป็น $582 (Outperform) — consensus: 26 analysts Buy avg PT $463.58 — watchlist alert: entry zone $200-215 ล้าสมัยมาก (ราคาจริง $422) — CIO review required",
    impact: "POSITIVE", tickers: ["AVGO", "META"],
    url: "https://stockanalysis.com/stocks/avgo/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "GOOGL Alphabet — ราคา $388.76 + capex $190B FY2026 + ¥576.5B yen bond (record) + FOMC dividend ex-date Jun 8",
    summary: "Alphabet ราคา $388.76 (26 พ.ค. range $382.60-$389.26) — Q1 2026: revenue $109.9B (+22% YoY), operating income $39.7B (+30%), GCP +63% YoY, backlog $460B+ — FY2026 capex $190B (record) + issued ~$60B multi-currency bonds รวม record ¥576.5B yen deal เพื่อ fund AI data centers — FY2026 EPS consensus เพิ่มเป็น $14.22/share (จาก $11.63) — dividend $0.22 ex-date Jun 8 — portfolio: T1 OPEN 1 share @ $388.91 unrealized -0.04% — thesis intact แต่ capex pressure เพิ่ม",
    impact: "POSITIVE", tickers: ["GOOGL"],
    url: "https://finance.yahoo.com/quote/GOOGL/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "AAPL Apple — ราคา $308.41 ATH zone + Wedbush PT $400 + BofA PT $380 + $100B buyback + WWDC approaching",
    summary: "Apple ราคา $308.41 (26 พ.ค.) market cap $4.54T ใกล้ ATH — company ประกาศ $100B share repurchase ใหม่ + dividend เพิ่ม 4% เป็น $0.27/qtr — Wedbush ปรับ PT $350 เป็น $400, BofA ปรับ PT เป็น $380, Melius $385 — Wall Street focus: AI roadmap + iPhone upgrade cycle จาก Apple Intelligence — WWDC 2026 เป็น next major catalyst — CEO transition: John Ternus (Sep 1) Tim Cook เป็น Executive Chairman — AAPL up 50% ใน 52 weeks",
    impact: "POSITIVE", tickers: ["AAPL"],
    url: "https://www.tikr.com/blog/apple-rose-14-in-30-days-heres-how-much-the-stock-could-rise-in-2026",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "META Meta Platforms — ราคา $611.29 + Beijing blocks $2B Manus AI deal + layoff batch 1 เสร็จ + no more layoffs 2026",
    summary: "Meta ราคา $611.29 (26 พ.ค. range $605.30-$614.47) — Beijing ordered Meta ยกเลิก $2B attempt ซื้อ AI startup Manus (regulatory block ใน China) — layoff batch 1 ~10% workforce เสร็จสมบูรณ์ — Zuckerberg ยืนยัน no more company-wide layoffs ปีนี้ — capex FY2026 $114-125B ยืนยัน AI infrastructure commitment — Q1 2026 revenue $56.3B (+33% YoY), net income +61% — analyst consensus: 55 analysts Strong Buy avg PT $826 (+35% upside) — Big 10 watchlist รอ analysis",
    impact: "MIXED", tickers: ["META"],
    url: "https://stockanalysis.com/stocks/meta/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "TSLA Tesla — ราคา $433.59 (+ATH zone) + robotaxi Texas early challenges + SpaceX IPO overhang — earnings Jul 29",
    summary: "Tesla ราคา $433.59 (26 พ.ค. range $426.12-$433.67) market cap $1.62T P/E 389.19 — robotaxi rollout in Texas encounters early challenges (Cybercab fully autonomous deployment เผชิญ operational hiccups) — SpaceX IPO overhang ยังกดดัน attention split — Q1 2026 deliveries 358K ต่ำกว่า consensus 365K แต่ EPS $0.41 beat $0.36 + automotive gross margin 21.1% (จาก 16.2%) — next earnings Jul 29 2026 — 52W recovery strong จาก April lows",
    impact: "MIXED", tickers: ["TSLA"],
    url: "https://www.heygotrade.com/en/blog/Tesla-TSLA-May-2026-Buy-Hold-Or-Sell-Delivery-Slowdown/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "MSFT Microsoft — ราคา $416-419 + LinkedIn layoff 600+ + EY $1B AI partnership active + Azure thesis intact",
    summary: "Microsoft ราคา ~$416-419 (26 พ.ค. range $413.02-$419.77) — LinkedIn จะ layoff 600+ workers ช่วงฤดูร้อน 2026 เป็น cost optimization — EY $1B AI partnership ดำเนินต่อ (ประกาศ May 22) — Azure +40% YoY thesis intact — analyst: Outperform rating PT $555 (+33% upside) — next earnings July 28 2026 — ราคายัง -13% จาก AI capex pressure บน FCF แต่ recovery trend ชัดเจน",
    impact: "NEUTRAL", tickers: ["MSFT"],
    url: "https://stockanalysis.com/stocks/msft/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "AMZN Amazon — ราคา $267.99 constructive pullback + AWS thesis intact + analyst median PT $317",
    summary: "Amazon ราคา $267.99 (26 พ.ค. range $265.30-$269.79) — technical pattern: falling wedge retest of prior highs + supported near 20-day EMA (constructive pullback) — AI momentum strong: AWS re-acceleration + margin discipline — 10 Buy ratings / 0 Sell ratings — median analyst PT $317 (+18.3% upside) — Q1 2026 AWS +28% YoY — market cap $2.89T ใกล้ $3T milestone — Big 10 watchlist รอ analysis",
    impact: "POSITIVE", tickers: ["AMZN"],
    url: "https://www.quiverquant.com/news/Amazon+Stock+(AMZN)+Opinions+on+AI+Momentum+and+AWS+Growth",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "TSM TSMC — ราคา $412 premarket + Taiwan market cap แซง India (#5 ในโลก) + TSMC YTD +49% full-year guidance >30%",
    summary: "TSMC ราคา $412 premarket (26 พ.ค.) — Taiwan stock market ทะลุ India เป็น world's 5th largest ($4.95T vs India $4.92T) ขับเคลื่อนโดย TSMC rally — TSMC YTD +49% — Q2 guidance $39-40.2B revenue (+30-34% sequential) — full-year guidance revenue growth >30% — foundry market share 64-71% (near-monopoly) — analyst median PT $450 — 2nm AMD EPYC Venice production start ยืนยัน technology leadership — tailwind ต่อ NVDA AVGO AMD thesis ทั้งหมด",
    impact: "POSITIVE", tickers: ["TSM", "NVDA", "AMD", "AVGO"],
    url: "https://eciks.org/5848-27558-tsmc-stock-rises-to-412-in-premarket-trading-as-ai-demand-boosts-semiconductor-o",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "NOW ServiceNow — ราคา $99.92 + Oppenheimer Buy (May 24) + Barclays/Bernstein PT raised — earnings Jul 29",
    summary: "ServiceNow ราคา $99.92 (26 พ.ค. prev close $102.13) — Oppenheimer ออก Buy rating (May 24) — Barclays และ Bernstein ต่าง raise PT citing AI-driven innovation + larger addressable market — avg 12M PT $142.77 (+42.8% upside จาก $99.92) — Q1 2026: 22% subscription revenue growth, 97% retention, raised FY guidance — shareholders approved expanded equity incentive plan (May 22) — next earnings Jul 29 2026 — portfolio: T1 OPEN 2 shares @ $89.47, ราคาปัจจุบัน $99.92 = unrealized +11.7% — thesis intact",
    impact: "POSITIVE", tickers: ["NOW"],
    url: "https://seekingalpha.com/article/4906814-servicenow-stock-big-mispricing-of-2026",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "ADBE Adobe — earnings June 11 approaching — consensus EPS $5.61 Revenue $6.43B — Q1 2026 record operating CF $2.96B",
    summary: "Adobe earnings June 11 2026 AMC — analyst consensus: EPS $5.61 (Q2 FY2026), revenue guidance $6.43B (from company) — Q1 2026 actual: EPS $6.06 beat $5.46 (+10.99%), record operating CF $2.96B, non-GAAP op margin 47.4% — CEO Narayen highlight AI integration success แต่ยังมี competitive pressure จาก Canva/Runway — ราคา ADBE ~$248-255 range ล่าสุด — portfolio: T1+T2 OPEN 4 shares avg $247.03 — Mizuho Neutral PT $270 vs D.A. Davidson Buy PT $300 — earnings June 11 เป็น major catalyst สำคัญที่สุดใน 30 วัน",
    impact: "MIXED", tickers: ["ADBE"],
    url: "https://www.marketbeat.com/stocks/NASDAQ/ADBE/earnings/",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "MU Micron Technology — ATH: ราคาพุ่ง +19-25% ทะลุ $900 Market Cap $1T หลัง UBS ปรับ PT $535 เป็น $1,625",
    summary: "Micron หุ้นพุ่ง +19-25% วันที่ 26 พ.ค. ทำ ATH ใหม่ (intraday $916.76) market cap ทะลุ $1T เป็นครั้งแรก — catalyst: UBS analyst Timothy Arcuri ปรับ PT จาก $535 เป็น $1,625 (triple) พร้อม re-frame Micron เป็น 'AI-native infrastructure giant' ไม่ใช่ cyclical memory maker — long-term supply agreements cover 60-70% of server DDR5 volumes ผ่าน 2029 (Nvidia-like visibility) — MU YTD +178% ที่ $876 — ยืนยัน AI memory demand thesis + อาจเป็น leading indicator ว่า AI capex ยังไม่ถึง peak",
    impact: "POSITIVE", tickers: ["MRVL", "NVDA", "AVGO", "TSM"],
    url: "https://markets.financialcontent.com/stocks/article/stockstory-2026-5-26-why-micron-mu-stock-is-up-today",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "GEV GE Vernova — ราคา $1,072.50 (+5.31% วันที่ 26 พ.ค.) + dividend $0.50/qtr Q3 2026 + data center orders ทะลุ 2025 ทั้งปี",
    summary: "GE Vernova ราคา $1,072.50 market cap $287.97B (+5.31% วันที่ 26 พ.ค.) — Q1 2026: EPS $17.44 beat, revenue $9.34B, orders +71% organically, backlog +$13B, raised guidance — Electrification segment: data center equipment orders Q1 2026 = $2.4B (เกิน 2025 ทั้งปีในไตรมาสเดียว) — Q3 2026 dividend $0.50/share payable Jul 14 — analyst consensus: Strong Buy avg PT >$1,100 — watchlist: ราคา $1,072 ยังต้องการ re-analysis ด่วน FV เดิม $263 ล้าสมัยมาก (MOS -307%)",
    impact: "POSITIVE", tickers: ["GEV"],
    url: "https://www.tradingkey.com/news/market-movers/261928793-market-movers-gev-20260526",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "VEEV Veeva Systems — earnings June 3 — consensus EPS $2.13 +8% revenue $857M +13% — ราคา $161 + Ostro acquisition",
    summary: "Veeva Systems ประกาศ Q1 FY2027 results June 3 2026 AMC (period ending Apr 30) — consensus: EPS $2.13 (+8.12% YoY), revenue $857.33M (+12.95% YoY) — FY2026: revenue $3.195B (+16%), Q4 revenue $836M — acquired Ostro ~$100M cash (life sciences engagement) — ราคา VEEV ~$161 ยังเหนือ entry zone $148-158 — Conv 6.7 < 7.0 threshold — earnings June 3 เป็น catalyst สำคัญ: beat + raised guidance อาจ unlock T1 deploy decision",
    impact: "NEUTRAL", tickers: ["VEEV"],
    url: "https://www.stocktitan.net/news/VEEV/veeva-to-release-fiscal-2027-first-quarter-results-on-june-3-oh0s5meq231o.html",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "JPM JPMorgan — ราคา $307.40 + AI hiring slowdown + $50B private credit exposure + living wills regulatory milestone",
    summary: "JPMorgan ราคา $307.40 (26 พ.ค. range $303.10-$307.45) — JPM กำลัง hire fewer bankers เนื่องจาก lean into AI (cost optimization) — $50B private credit exposure ยังอยู่ในระดับที่ comfortable ตาม management — non-traded BDCs limiting withdrawals เป็น industry concern — passed Fed 'living wills' regulatory milestone (confidence signal) — dividend: $1.50/share Q1 2026 (14-year streak) — Big 10 watchlist รอ analysis",
    impact: "NEUTRAL", tickers: ["JPM"],
    url: "https://www.cnbc.com/quotes/JPM",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "LLY Eli Lilly — ราคา $1,064.59 (+2.24%) + Heart-2 Verve-102 Phase 1b results + $3.8B vaccine acquisitions + market cap $1T",
    summary: "Eli Lilly ราคา $1,064.59 (+$23.35, +2.24% วันที่ 26 พ.ค.) market cap $1T — ประกาศ Phase 1b Heart-2 study results สำหรับ Verve-102 (investigational medicine) — expanding portfolio ด้วย $3.8B vaccine acquisitions — TRIUMPH-1 obesity data (retatrutide -28.3% weight loss) ยังเป็น headline driver — Mizuho analyst Jared Holz positive response ต่อ obesity data — Bernstein conference May 28 เป็น next catalyst — analyst consensus PT $1,210 (+13.7% upside จากราคาปัจจุบัน) — Big 10 watchlist รอ analysis",
    impact: "POSITIVE", tickers: ["LLY"],
    url: "https://finance.yahoo.com/quote/LLY/",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "BRK.B Berkshire Hathaway — ราคา $485.95 + Greg Abel era: triple GOOGL + buy Delta + dump Visa/Mastercard/Amazon",
    summary: "Berkshire ราคา $485.95 (26 พ.ค. range $479.00-$487.19) — Q1 2026 earnings: revenue $93.68B (vs $89.73B prior year) — Greg Abel era major moves: (1) GOOGL stake +224% (triple) (2) Delta Air Lines $2.8B stake (39.8M shares) airline กลับมาครั้งแรกหลัง 2020 (3) ขาย Visa, Mastercard, Amazon, UnitedHealth Group ออกทั้งหมด — cash pile $397B (ยังไม่ deploy ก้าวกระโดด) — analyst avg PT $520.33 (+7% upside) — 'core four': AAPL, AmEx, Moody's, Coca-Cola",
    impact: "NEUTRAL", tickers: ["BRK.B", "GOOGL"],
    url: "https://stockanalysis.com/stocks/brk.b/",
  },
  {
    date: "2026-05-27", category: "REGULATION",
    headline: "Trump Tariff — Section 301 rebuilt สำหรับ 16 ประเทศ + Section 232 pharma 100% — EU deadline Jul 4 — effective rate 11.8%",
    summary: "Admin ใช้ Section 301 investigations ใหม่ครอบคลุม 16 ประเทศ (75%+ US imports) แทน IEEPA ที่ถูก Supreme Court ยกเว้น (Feb 2026) — Section 232 pharma tariff 100% บน patented pharmaceutical imports เพิ่ม cost pressure ต่อ branded pharma (LLY, ผลบวกน้อยกว่าคาด) — EU deadline Jul 4 ลงนาม trade deal ไม่อย่างนั้น car imports 25% — Section 122 authority expire Jul 24 2026 (under appeal) — effective tariff rate 11.8% (ลงจาก peak 27%) — US-China truce 90 วัน ยังมีผลถึง กรกฎาคม 2026 — semiconductor stocks ยังได้ประโยชน์จาก truce",
    impact: "MIXED", tickers: ["LLY", "NVDA", "AVGO", "AMD", "TSM", "AAPL"],
    url: "https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/",
  },"""

# สร้าง content ใหม่
new_content = """// ─── NEWS DATA ───────────────────────────────────────────
// Managed by Atlas · อัปเดตอัตโนมัติทุกวัน 08:00
// Category "AI" — เพิ่มมือได้ ไม่ต้องรอ script (Claude/Anthropic updates)
// ห้ามแก้ category อื่น — ใช้ atlas-news-scan script เท่านั้น

const NEWS_LAST_UPDATED = "2026-05-27 08:30";

const NEWS = [
""" + new_news + "\n  " + old_news_body + "\n];"

with open(r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\news.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("SUCCESS: news.js updated with new articles prepended")
print("New articles count: 18")
