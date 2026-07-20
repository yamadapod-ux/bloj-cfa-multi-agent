import re, os

base = r"C:\Users\user\Desktop\บลจ\บลจ CFA"

with open(os.path.join(base, "dashboard", "news.js"), "r", encoding="utf-8") as f:
    old = f.read()

match = re.search(r'const NEWS = \[(.*)\];', old, re.DOTALL)
old_body = match.group(1).strip()

new_articles = '''  // ── 2026-05-27 ──────────────────────────────────────────────────────────────
  {
    date: "2026-05-27", category: "MACRO",
    headline: "S&P 500 ATH 7,519.12 (+0.61%) Nasdaq ATH 26,656.18 (+1.19%) วันที่ 26 พ.ค. — Micron +25% ทะลุ $1T — Iran peace talks หนุน",
    summary: "S&P 500 ปิดที่ 7,519.12 (+0.61%) วันที่ 26 พ.ค. ทำ all-time high ใหม่ — Nasdaq +1.19% ที่ 26,656.18 ATH ใหม่เช่นกัน — Dow -0.23% ที่ 50,461.68 — drivers: (1) Trump ระบุ US-Iran negotiations 'proceeding nicely' ลด geopolitical risk (2) Micron MU พุ่ง +19-25% หลัง UBS ปรับ PT $535 เป็น $1,625 ทำ market cap ทะลุ $1T (3) Tech sector lead ยืนยัน AI spending thesis — S&P 500 futures วันที่ 27 พ.ค. +0.15% เช้า — RISK-ON regime ยืนยันต่อเนื่อง",
    impact: "POSITIVE", tickers: ["ADBE", "NOW", "GOOGL", "MSFT", "META", "AMZN", "TSLA"],
    url: "https://www.cnbc.com/2026/05/26/stock-market-today-live-updates.html",
  },
  {
    date: "2026-05-27", category: "MACRO",
    headline: "Fed คง 3.5-3.75% — Kevin Warsh นำ FOMC June 16-17 + dot plot ใหม่ — ตลาด price in hike 40% — 10Y yield 4.58%",
    summary: "Fed Funds Rate คงที่ 3.5-3.75% จาก FOMC Apr 29 (มติ 8-4 dissent สูงสุดตั้งแต่ Oct 1992) — Kevin Warsh เข้าตำแหน่ง Fed Chair แทน Powell — FOMC ถัดไป June 16-17 มี updated dot plot (SEP) ตลาดจับตาใกล้ชิด — 10Y Treasury yield 4.58% (Fed H.15 May 26) — ตลาด price in ~40% probability rate hike ก่อนสิ้นปี 2026 vs median dot plot ยังชี้ 2 cuts ใน 12M ถัดไป — Warsh hawkish กว่า Powell = downside risk ต่อ growth stocks ทุกตัว",
    impact: "NEGATIVE", tickers: ["ADBE", "NOW", "GOOGL", "MSFT", "META"],
    url: "https://www.federalreserve.gov/releases/h15/",
  },
  {
    date: "2026-05-27", category: "MACRO",
    headline: "Trump Tariff — Section 301 rebuild 16 ประเทศ + pharma 100% + EU deadline Jul 4 — effective rate 11.8% — US-China truce ถึงก.ค.",
    summary: "Admin ใช้ Section 301 investigations ใหม่ครอบคลุม 16 ประเทศ (75%+ US imports) แทน IEEPA ที่ถูก Supreme Court ยกเว้น (Feb 2026) — Section 232 pharma tariff 100% บน patented pharmaceutical imports กด LLY — EU deadline Jul 4 ลงนาม trade deal ไม่อย่างนั้น car imports 25% — Section 122 authority expire Jul 24 2026 (under appeal) — effective tariff rate 11.8% (ลงจาก peak 27%) — US-China truce 90 วันยังมีผลถึง กรกฎาคม 2026 เป็น tailwind ต่อ semiconductor names",
    impact: "MIXED", tickers: ["LLY", "NVDA", "AVGO", "AMD", "TSM", "AAPL"],
    url: "https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/",
  },
  {
    date: "2026-05-27", category: "EARNINGS",
    headline: "MRVL Marvell — Q1 FY2027 รายงานคืนนี้ AH — consensus $2.4B +27% EPS $0.80 — หุ้น +100% YTD ราคา $196",
    summary: "Marvell Technology รายงาน Q1 FY2027 หลังปิดตลาด 27 พ.ค. — consensus: revenue $2.4B (+27% YoY), EPS $0.80 — ราคา $196.33 หลัง +100% YTD — FY2026 revenue $8.195B (+42% YoY) — Q4 FY2026 EPS $0.80 beat $0.71 (+12.68%) — สร้าง custom AI chips (XPUs) ให้ hyperscalers — BofA PT $200 Goldman $200 Melius $220 — เป็น high-impact event สำหรับ AI semiconductor ecosystem ทั้งกลุ่ม",
    impact: "MIXED", tickers: ["MRVL", "NVDA", "AVGO", "TSM"],
    url: "https://moneymorning.com/2026/05/25/marvell-technology-mrvl-stock-earnings-may-2026",
  },
  {
    date: "2026-05-27", category: "EARNINGS",
    headline: "AVGO Broadcom — earnings June 3 approaching — custom AI chip +140% QoQ + BCM68850 launch — ราคา $422 Evercore PT $582",
    summary: "Broadcom ราคา $422.59 (26 พ.ค. range $413-$435) — earnings June 3 — custom AI chip revenue +140% QoQ, data-center networking +60% — BCM68850 new home-gateway chip ด้วย built-in AI ดัน AVGO +2% วันที่ 26 พ.ค. — Evercore ISI ปรับ PT $490 เป็น $582 Outperform — consensus 26 analysts Buy avg PT $463.58 — watchlist: entry zone $200-215 ล้าสมัยมาก (ราคาจริง $422) CIO review required",
    impact: "POSITIVE", tickers: ["AVGO"],
    url: "https://stockanalysis.com/stocks/avgo/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "ADBE Adobe — ราคา $240.49 (-1.74%) — earnings June 11 AH — consensus EPS $5.61 Rev $6.43B — Q1 record CF $2.96B",
    summary: "Adobe ราคา $240.49 (26 พ.ค. -1.74%) 52W range $224.13-$421.48 — earnings June 11 2026 AMC สำคัญที่สุดใน 30 วัน — consensus Q2: EPS $5.61, revenue $6.43B (company guidance) — Q1 actual: EPS $6.06 beat $5.46 (+10.99%), record operating CF $2.96B, non-GAAP op margin 47.4% — Mizuho Neutral PT $270 vs D.A. Davidson Buy PT $300 — portfolio: T1+T2 OPEN 4 shares avg $247.03, ราคาปัจจุบัน $240.49 = unrealized -2.6% — watchlist: หุ้น YTD -31.29%",
    impact: "NEGATIVE", tickers: ["ADBE"],
    url: "https://finance.yahoo.com/quote/ADBE/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "NOW ServiceNow — ราคา $99.92 — Oppenheimer Buy (May 24) + Barclays/Bernstein PT raised — avg PT $142.77 — earnings Jul 29",
    summary: "ServiceNow ราคา $99.92 (26 พ.ค. prev close $102.13) YTD -32% — Oppenheimer Buy rating May 24 — Barclays + Bernstein raise PT citing AI-driven innovation + larger addressable market — avg 12M PT $142.77 (+42.8% upside) — Q1 2026: 22% subscription revenue growth, 97% retention, raised FY guidance — shareholders approved expanded equity incentive plan (May 22) — next earnings Jul 29 — portfolio: T1 OPEN 2 shares @ $89.47, ราคา $99.92 = unrealized +11.7% — thesis intact",
    impact: "POSITIVE", tickers: ["NOW"],
    url: "https://seekingalpha.com/article/4906814-servicenow-stock-big-mispricing-of-2026",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "GOOGL Alphabet — ราคา $388.76 + capex $190B + record yen bond + EPS consensus ปรับขึ้นเป็น $14.22 — dividend ex-date Jun 8",
    summary: "Alphabet ราคา $388.76 (26 พ.ค. range $382.60-$389.26) — Q1 2026: revenue $109.9B (+22%), GCP +63%, backlog $460B+ — FY2026 capex $190B + issued ~$60B multi-currency bonds รวม record yen deal ¥576.5B — FY2026 EPS consensus ปรับเป็น $14.22/share (จาก $11.63) — dividend $0.22 ex-date Jun 8 — portfolio: T1 OPEN 1 share @ $388.91, ราคาปัจจุบัน $388.76 = unrealized -0.04% — thesis intact แต่ capex pressure เพิ่ม",
    impact: "POSITIVE", tickers: ["GOOGL"],
    url: "https://finance.yahoo.com/quote/GOOGL/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "AAPL Apple — ราคา $308.41 + Wedbush PT $400 + BofA PT $380 + $100B buyback + dividend +4% — WWDC next catalyst",
    summary: "Apple ราคา $308.41 (26 พ.ค.) market cap $4.54T — $100B share repurchase ใหม่ + dividend +4% เป็น $0.27/qtr — Wedbush ปรับ PT $350 เป็น $400, BofA PT $380, Melius $385 — CEO transition: John Ternus (Sep 1), Tim Cook เป็น Executive Chairman — WWDC 2026 next major catalyst — AAPL YTD +13.6%, up 50% ใน 52 weeks",
    impact: "POSITIVE", tickers: ["AAPL"],
    url: "https://www.tikr.com/blog/apple-rose-14-in-30-days-heres-how-much-the-stock-could-rise-in-2026",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "META Meta — ราคา $611.29 + Beijing blocks $2B Manus AI deal + layoff batch 1 เสร็จ + no more layoffs 2026",
    summary: "Meta ราคา $611.29 (26 พ.ค. range $605.30-$614.47) — Beijing ordered Meta ยกเลิก $2B attempt ซื้อ AI startup Manus (China regulatory block) — layoff batch 1 ~10% workforce เสร็จแล้ว — Zuckerberg ยืนยัน no more company-wide layoffs ปีนี้ — capex $114-125B — Q1 revenue $56.3B (+33%), net income +61% — consensus 55 analysts Strong Buy avg PT $826 (+35% upside)",
    impact: "MIXED", tickers: ["META"],
    url: "https://stockanalysis.com/stocks/meta/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "TSLA Tesla — ราคา $433.59 + robotaxi Texas challenges + SpaceX IPO overhang — earnings Jul 29",
    summary: "Tesla ราคา $433.59 (26 พ.ค. range $426.12-$433.67) market cap $1.62T P/E 389 — robotaxi Texas encounters early challenges — SpaceX IPO overhang กดดัน attention split — Q1: EPS $0.41 beat $0.36, deliveries 358K ต่ำกว่า 365K consensus, automotive gross margin 21.1% (จาก 16.2%) — next earnings Jul 29",
    impact: "MIXED", tickers: ["TSLA"],
    url: "https://www.heygotrade.com/en/blog/Tesla-TSLA-May-2026-Buy-Hold-Or-Sell-Delivery-Slowdown/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "MSFT Microsoft — ราคา $416-419 + LinkedIn layoff 600+ + Azure thesis intact — earnings Jul 28",
    summary: "Microsoft ราคา ~$416-419 (26 พ.ค. range $413.02-$419.77) — LinkedIn layoff 600+ workers ฤดูร้อน 2026 — EY $1B AI partnership ดำเนินต่อ — Azure +40% YoY thesis intact — analyst Outperform PT $555 (+33% upside) — next earnings Jul 28",
    impact: "NEUTRAL", tickers: ["MSFT"],
    url: "https://stockanalysis.com/stocks/msft/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "AMZN Amazon — ราคา $267.99 constructive pullback + AWS thesis intact + median analyst PT $317",
    summary: "Amazon ราคา $267.99 (26 พ.ค. range $265.30-$269.79) — technical: falling wedge retest + supported near 20-day EMA — AWS re-acceleration + margin discipline — 10 Buy / 0 Sell ratings — median PT $317 (+18% upside) — Q1 2026 AWS +28% YoY — market cap $2.89T",
    impact: "POSITIVE", tickers: ["AMZN"],
    url: "https://www.bloomberg.com/news/articles/2026-05-14/amazon-s-ai-success-sends-stock-racing-toward-3-trillion-club",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "TSM TSMC — ราคา $412 premarket + Taiwan market #5 ในโลก แซง India + YTD +49% + full-year guidance >30%",
    summary: "TSMC ราคา $412 premarket (26 พ.ค.) — Taiwan stock market แซง India เป็น world's 5th largest ($4.95T vs $4.92T) ขับเคลื่อนโดย TSMC — YTD +49% — Q2 guidance $39-40.2B (+30-34% sequential) — full-year guidance >30% — foundry market share 64-71% near-monopoly — median analyst PT $450",
    impact: "POSITIVE", tickers: ["TSM", "NVDA", "AMD", "AVGO"],
    url: "https://eciks.org/5848-27558-tsmc-stock-rises-to-412-in-premarket-trading-as-ai-demand-boosts-semiconductor-o",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "MU Micron — ATH $916 market cap $1T หลัง UBS PT $535 เป็น $1,625 — 'AI-native infrastructure giant' re-framing",
    summary: "Micron พุ่ง +19-25% วันที่ 26 พ.ค. ATH intraday $916.76 market cap ทะลุ $1T ครั้งแรก — UBS Timothy Arcuri ปรับ PT จาก $535 เป็น $1,625 (triple) พร้อม re-frame เป็น 'AI-native infrastructure giant' — supply agreements cover 60-70% server DDR5 volumes ผ่าน 2029 (Nvidia-like visibility) — MU YTD +178% — ยืนยัน AI memory demand ยังไม่ถึง peak",
    impact: "POSITIVE", tickers: ["MRVL", "NVDA", "AVGO", "TSM"],
    url: "https://markets.financialcontent.com/stocks/article/stockstory-2026-5-26-why-micron-mu-stock-is-up-today",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "GEV GE Vernova — ราคา $1,072 (+5.31%) + dividend $0.50/qtr Q3 + data center orders Q1 เกิน 2025 ทั้งปี",
    summary: "GE Vernova ราคา $1,072.50 (+5.31% วันที่ 26 พ.ค.) market cap $287.97B — Q1 2026: EPS $17.44 beat, revenue $9.34B, orders +71% organically — Electrification segment: data center orders Q1 = $2.4B (เกิน 2025 ทั้งปีในไตรมาสเดียว) — dividend $0.50/qtr Q3 payable Jul 14 — watchlist: FV เดิม $263 ล้าสมัยมาก (MOS -307%) ต้องการ re-analysis ด่วน",
    impact: "POSITIVE", tickers: ["GEV"],
    url: "https://www.tradingkey.com/news/market-movers/261928793-market-movers-gev-20260526",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "VEEV Veeva — earnings June 3 AH — consensus EPS $2.13 +8% Rev $857M +13% — Ostro $100M acquisition",
    summary: "Veeva ประกาศ Q1 FY2027 results June 3 AMC — consensus: EPS $2.13 (+8.12% YoY), revenue $857.33M (+12.95%) — FY2026: revenue $3.195B (+16%) — acquired Ostro ~$100M cash — ราคา ~$161 เหนือ entry zone $148-158 — Conv 6.7 < 7.0 threshold — earnings June 3 เป็น catalyst: beat + raised guidance อาจ unlock T1 deploy",
    impact: "NEUTRAL", tickers: ["VEEV"],
    url: "https://www.stocktitan.net/news/VEEV/veeva-to-release-fiscal-2027-first-quarter-results-on-june-3-oh0s5meq231o.html",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "JPM JPMorgan — ราคา $307.40 + AI hiring slowdown + $50B private credit comfortable + living wills milestone",
    summary: "JPMorgan ราคา $307.40 (26 พ.ค. range $303.10-$307.45) — hire fewer bankers เพราะ lean into AI — $50B private credit exposure comfortable per management — passed Fed 'living wills' regulatory milestone — dividend $1.50/share (14-year streak) — Big 10 watchlist รอ analysis",
    impact: "NEUTRAL", tickers: ["JPM"],
    url: "https://www.cnbc.com/quotes/JPM",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "LLY Eli Lilly — ราคา $1,064.59 (+2.24%) + Heart-2 Phase 1b + $3.8B vaccine acquisitions + market cap $1T",
    summary: "Eli Lilly ราคา $1,064.59 (+2.24% วันที่ 26 พ.ค.) market cap $1T — ประกาศ Phase 1b Heart-2 study สำหรับ Verve-102 — $3.8B vaccine acquisitions — TRIUMPH-1 retatrutide obesity (-28.3% weight loss) ยังเป็น headline driver — Bernstein conference May 28 next catalyst — analyst consensus PT $1,210 (+13.7% upside)",
    impact: "POSITIVE", tickers: ["LLY"],
    url: "https://finance.yahoo.com/quote/LLY/",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "BRK.B Berkshire — ราคา $485.95 + triple GOOGL + buy Delta + dump Visa/Mastercard/Amazon + cash $397B",
    summary: "Berkshire ราคา $485.95 (26 พ.ค. range $479-$487) — Greg Abel era: GOOGL stake +224%, Delta $2.8B, ขาย Visa+Mastercard+Amazon+UnitedHealth ออกทั้งหมด — Q1 revenue $93.68B — cash $397B — 'core four': AAPL, AmEx, Moody's, Coca-Cola — analyst avg PT $520.33",
    impact: "NEUTRAL", tickers: ["BRK.B", "GOOGL"],
    url: "https://stockanalysis.com/stocks/brk.b/",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "V Visa — ราคา $328.88 + Class B exchange offer เสร็จ + DOJ debit case overhang — BRK exit เป็น negative signal",
    summary: "Visa ราคา $328.88 (25 พ.ค.) — Class B-1/B-2 exchange offer เสร็จ May 8: issued 60.6M Class B-3 + 23.3M Class C shares — Berkshire ขาย Visa ออกทั้งหมด (negative signal) — DOJ debit case overhang ยังคงอยู่ — watchlist: ราคา $328.88 ยังเหนือ entry zone $285-300 ห่าง trigger $315 อยู่",
    impact: "MIXED", tickers: ["V"],
    url: "https://www.cnbc.com/quotes/V",
  },'''

new_content = '''// ─── NEWS DATA ───────────────────────────────────────────
// Managed by Atlas · อัปเดตอัตโนมัติทุกวัน 08:00
// Category "AI" — เพิ่มมือได้ ไม่ต้องรอ script (Claude/Anthropic updates)
// ห้ามแก้ category อื่น — ใช้ atlas-news-scan script เท่านั้น

const NEWS_LAST_UPDATED = "2026-05-27 08:30";

const NEWS = [
''' + new_articles + "\n  " + old_body + "\n];"

out_path = os.path.join(base, "dashboard", "news.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"SUCCESS: wrote {len(new_content)} chars to {out_path}")
print(f"New articles prepended: 20")
