#!/usr/bin/env python3
# atlas_news_merge.py — Atlas News Merge Script 2026-05-27
# Usage: python scripts/atlas_news_merge.py

import re
import os

NEWS_JS_PATH = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\news.js"

# ── ข่าวใหม่ที่ Atlas scan ได้ 2026-05-27 (เรียงใหม่→เก่า) ────────────────
NEW_NEWS_BLOCK = '''
  // ── 2026-05-27 ──────────────────────────────────────────────────────────────
  {
    date: "2026-05-27", category: "MACRO",
    headline: "S&P 500 7,515.90 (-0.04%) Dow +224 pts record close — Iran Strait of Hormuz เปิดกลับ 1 เดือน น้ำมันร่วง 3%",
    summary: "S&P 500 ปิดที่ ~7,515.90 (-0.04%) Nasdaq -0.09% วันที่ 27 พ.ค. — Dow +224 pts ทำ record close ใหม่ — Iran state TV ประกาศ committed เปิด Strait of Hormuz กลับสู่ระดับ pre-war ภายใน 1 เดือน ดัน oil ร่วงกว่า 3% ลงต่ำกว่า $91/bbl — Micron (MU) +19% ทะลุ $1T market cap เป็น catalyst หลักของ Nasdaq Tue (May 26) — Zscaler ร่วง -23% กดดัน cybersecurity sector — P&G +3% Home Depot +2% ดัน Dow — NVDA ปิด $216.10 (+0.36%) หลัง record Q1 earnings ผ่านไปแล้ว — ตลาดโดยรวม cautious รอ Iran deal confirmation",
    impact: "MIXED", tickers: ["ADBE", "NOW", "GOOGL", "NVDA", "AAPL", "META", "MSFT", "AMZN", "TSLA"],
    url: "https://www.thestreet.com/latest-news/stock-market-today-may-27-2026-nasdaq-sp-500-open-higher-as-unprecedented-chip-sector-continues-rally",
  },
  {
    date: "2026-05-27", category: "MACRO",
    headline: "Kevin Warsh Fed Chair confirmation advancing — Senate Banking Committee party-line vote passed, full Senate expected to follow",
    summary: "Senate Banking Committee ผ่านการ confirm Kevin Warsh เป็น Fed Chair ด้วย party-line vote — full Senate คาดว่าจะ confirm ในเร็วๆ นี้ — Warsh มีแนวโน้ม hawkish มากกว่า Powell ซึ่งเป็น headwind เพิ่มเติมต่อ growth stocks — ตลาดปรับ pricing: zero rate movement ปี 2026 + 1 cut ธ.ค. 2027 — probability hike ก่อนสิ้นปีเพิ่มขึ้น — Fed rate ปัจจุบันยังคงที่ 3.5-3.75% — FOMC ถัดไป June 16-17 เป็น first meeting ภายใต้ Warsh (หรือ Powell เป็น Governor) + Dot Plot update",
    impact: "NEGATIVE", tickers: ["ADBE", "NOW", "GOOGL", "MSFT", "META", "VEEV", "FICO"],
    url: "https://www.cnbc.com/2026/04/29/fed-interest-rate-decision-april-2026.html",
  },
  {
    date: "2026-05-27", category: "MACRO",
    headline: "Trump Taiwan Trade Deal — tariff ลดจาก 20% เป็น 15% + India ลดจาก 25% เป็น 18% — effective rate 11.8%",
    summary: "Trump ประกาศ trade deal กับ Taiwan ลด reciprocal tariff จาก 20% เป็น 15% + India จาก 25% เป็น 18% — Section 122 authority จะ expire July 24 หากไม่ต่ออายุ — Administration reconstruct ผ่าน Section 301 + 232 เพื่อ maintain 'virtually unchanged tariff revenue' — China 145% tariff (IEEPA border security + fentanyl) ยังคงมีผล — US-China truce 90 วันจะหมดประมาณกรกฎาคม 2026 — TSM ได้ประโยชน์โดยตรงจาก Taiwan deal + Nvidia $150B annual Taiwan investment ประกาศพร้อมกัน",
    impact: "POSITIVE", tickers: ["TSM", "NVDA", "AVGO", "AMD", "AAPL"],
    url: "https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "NVDA Nvidia — $150B annual Taiwan investment + Vera CPU $200B TAM + Q2 guidance $91B (+95% YoY) — ราคา $216.10",
    summary: "Jensen Huang ประกาศ Nvidia จะ invest ~$150B/ปี ใน Taiwan (เพิ่มจาก $100B เดิม) + ground-breaking Taipei HQ ปี 2030 — Vera CPU targets $200B TAM ใหม่นอกจาก GPU — Q2 FY2027 guidance $91B revenue (+95% YoY) สูงกว่า consensus $88B — stock ปิด $216.10 (+0.36%) หลัง post-earnings digest — stock -5.78% WoW เพราะ 'sell the news' หลัง beat แต่ fundamental ยังแข็ง — China exposure ยังเป็น risk แต่ Intel CEO เดินทางมาไต้หวันพบ TSMC + Nvidia leadership สัปดาห์นี้",
    impact: "POSITIVE", tickers: ["NVDA", "TSM", "AVGO", "AMD"],
    url: "https://www.tradingkey.com/analysis/stocks/us-stocks/261930703-tsmc-tsm-3nm-pricing-power-ai-demand-capacity-shortage-gross-margin-nvidia-analyst-upgrades-risk-tradingkey",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "TSM TSMC — ราคา $412-428 (new 52W high) + 3nm price hike 15% H2 2026 + YTD +49% — Taiwan market cap แซง India",
    summary: "TSMC ราคา $412.32-$427.96 วันที่ 27 พ.ค. แตะ 52-week high ใหม่ — ประกาศขึ้นราคา 3nm process quotes 15% ใน H2 2026 (เพิ่มอีก 5-10% ปีหน้า) — นี่คือ price hike ครั้งที่สอง ปี 2026 — Taiwan's total market cap แตะ $4.95T แซง India $4.92T = 5th largest ในโลก — NVDA $150B annual Taiwan investment เป็น demand signal ต่อ TSMC โดยตรง — Intel CEO Lip-Bu Tan เดินทางมาไต้หวันสัปดาห์นี้ ก่อน COMPUTEX Jun 2 — Motley Fool: 'odds stacked in favor of this AI stock' — watchlist Big 10 ยังรอ analysis",
    impact: "POSITIVE", tickers: ["TSM", "NVDA", "AMD", "AVGO", "AAPL"],
    url: "https://www.fool.com/investing/2026/05/27/the-odds-are-stacked-in-favor-of-this-ai-stock-her/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "AVGO Broadcom — Q2 FY2026 earnings June 3 consensus EPS $2.40 (+51.9% YoY) revenue $22.04B (+46.87% YoY) — custom AI chip +140%",
    summary: "Broadcom เตรียมรายงาน Q2 FY2026 วันที่ 3 มิ.ย. — consensus: EPS $2.40 (vs $1.58 prior year +51.9%), revenue $22.04B (+46.87% YoY) — Q1 actual: custom AI chip sales +140%, data-center networking +60% — customers รวม Google (largest), Anthropic, OpenAI (ใหม่) — ราคา $422.01 (+1.9%) outpace S&P 500 — 50G PON gateway chip launch ดัน momentum — watchlist: entry zone $200-215 ล้าสมัยมาก ราคาจริง $422 — ต้อง re-analysis ก่อน deploy",
    impact: "POSITIVE", tickers: ["AVGO", "GOOGL", "META"],
    url: "https://stockanalysis.com/stocks/avgo/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "ADBE Adobe — ราคา $240.49 + Adobe Summit ปิด analysts ชมเชย + acquisition Semrush เสร็จ + CEO transition",
    summary: "Adobe ราคา $240.49 (range $238.57-$243.57) วันที่ 27 พ.ค. — หุ้น +4% ช่วง AH หลัง analysts ชื่นชม Adobe Summit showcase (AI productivity tools) — acquisition Semrush Holdings เสร็จสมบูรณ์แล้ว — CEO transition อยู่ระหว่างดำเนินการ + brand visibility solution ใหม่ — Mizuho downgrade neutral ยัง overhang (PT $270) แต่ D.A. Davidson คง Buy $300 — 15 Buy / 4 Sell avg PT $327.28 — portfolio: T1+T2 OPEN avg $247.03 ราคาต่ำกว่า entry เล็กน้อย — next earnings June 11 2026 (15 วัน) ⚠️",
    impact: "MIXED", tickers: ["ADBE"],
    url: "https://www.marketbeat.com/stocks/NASDAQ/ADBE/news/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "NOW ServiceNow — Oppenheimer Buy rating May 24 + shareholder approved equity incentive plan + ราคา $99.92",
    summary: "ServiceNow ราคา $99.92 (ลงจาก $102.13) — Oppenheimer initiate/maintain Buy rating วันที่ 24 พ.ค. — shareholder approved expanded equity incentive plan วันที่ 22 พ.ค. — +14.5% rebound จาก mid-May low แต่ยัง YTD -32% — 43 Buy / 1 Sell avg PT $142.77 (+42.88% upside) — Seeking Alpha article 'Big Mispricing of 2026' highlight — portfolio: T1 OPEN 2 shares @ $89.47 (+11.7% unrealized @ $99.92) — FV re-verified $121.45 — thesis intact",
    impact: "POSITIVE", tickers: ["NOW"],
    url: "https://seekingalpha.com/article/4906814-servicenow-stock-big-mispricing-of-2026",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "GOOGL Alphabet — ราคา $390.96 (+0.76%) + EU Digital Markets Act penalty risk + earnings estimates +25% YTD",
    summary: "Alphabet ราคา $390.96 (+0.76%) — Q1 revenue $109.9B EPS $5.11 beat consensus — GCP +63.4% YoY operating margin 32.9% (จาก 17.8% YoY) — $15B Missouri AI data hub investment — dividend $0.22 ex-date Jun 8 — EU กำลัง advance toward major penalty under Digital Markets Act (DMA) linked to search practices — Trefis: analysts ตั้งคำถามเรื่อง momentum — earnings estimates +25% YTD driven by AI — portfolio: T1 OPEN 1 share @ $388.91 (+0.54% unrealized) thesis intact — T2 trigger ยังรอ $360-375",
    impact: "MIXED", tickers: ["GOOGL"],
    url: "https://www.trefis.com/stock/googl/articles/600476/should-you-pay-attention-to-alphabet-stocks-momentum-5/2026-05-27",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "MSFT Microsoft — ราคา $418-419 + Bill Ackman 5.65M shares ใหม่ + EY $1B AI deal + Azure +40% thesis intact",
    summary: "Microsoft ราคา ~$418-419 — Bill Ackman Pershing Square เปิดเผย 5,654,078 shares ใหม่ (Q1 ซื้อ / ขาย GOOGL ออก) = institutional confidence signal — EY $1B 5-year global AI partnership ยังดำเนินต่อ — Azure +40% YoY thesis intact — market cap $3.1T+ — next earnings July 28 2026 — analyst consensus Strong Buy avg PT $560 (+33% upside) — watchlist pending full analysis",
    impact: "POSITIVE", tickers: ["MSFT"],
    url: "https://www.cnbc.com/quotes/MSFT",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "META Meta Platforms — ราคา $610.64 + Q2 guidance $59.5B (+25.2% YoY) + analyst PT $1,000 by late 2026",
    summary: "Meta ราคา $610.64 (range $605.30-$614.47 May 26) — Q2 2026 guidance midpoint $59.5B (+25.2% YoY, เร็วกว่า Alphabet) — Q1 revenue $56.3B (+33% YoY) net income +61% YoY — capex FY2026 $114-125B — IndexBox: analysts project $1,000 by late 2026 (+64% upside จากราคาปัจจุบัน) — 73 analysts avg PT $862.85 (+41% upside) — Zuckerberg ประกาศ no more company-wide layoffs ปีนี้ — watchlist pending full analysis",
    impact: "POSITIVE", tickers: ["META"],
    url: "https://www.indexbox.io/blog/meta-stock-could-hit-1000-by-late-2026-analyst-outlook/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "AAPL Apple — ราคา $308.65 ATH ใหม่ + BofA PT ปรับขึ้น $380 + WWDC 2026 approaching + agentic AI $30B revenue potential",
    summary: "Apple ราคา $308.65 (range $308.49-$308.88) ทำ ATH ใหม่ on split-adjusted basis ใกล้ $5T market cap — BofA ปรับ PT เพิ่มจาก $330 เป็น $380 คง Buy — multiple Wall St firms ปรับ PT ขึ้นก่อน WWDC 2026 — analysts มอง Apple hardware+software integration เป็น 'significant advantage' ใน agentic AI market = potential $30B revenue by 2030 — iOS 27 AI features กำลัง prep — market cap $4.53T — watchlist Big 10 ยังรอ analysis",
    impact: "POSITIVE", tickers: ["AAPL"],
    url: "https://www.marketbeat.com/stocks/NASDAQ/AAPL/news/",
  },
  {
    date: "2026-05-27", category: "TECH",
    headline: "TSLA Tesla — ราคา $432-442 + SpaceX-Tesla merger speculation + Wedbush Ives 'holy grail' note + FSD China ongoing",
    summary: "Tesla ราคา $432.33 market cap $1.62T P/E 389x — pre-market +2% $442.27 จาก SpaceX-Tesla merger speculation — Wedbush Dan Ives: 'holy grail combining SpaceX and Tesla...expecting merge by next year' — Tesla regained EV lead Q1 2026 (358K vs BYD 310K) — FSD China expansion ongoing — $250M solar manufacturing facility Texas — SpaceX IPO timeline กลับมาเป็น overhang — watchlist Big 10 ยังรอ analysis แต่ P/E 389x = extreme valuation risk",
    impact: "MIXED", tickers: ["TSLA"],
    url: "https://www.investing.com/news/stock-market-news/why-is-tesla-stock-rallying-today-93CH-4661875",
  },
  {
    date: "2026-05-27", category: "EARNINGS",
    headline: "AVGO Broadcom earnings June 3 — EPS $2.40 est (+51.9%) Revenue $22.04B est (+46.87%) — custom AI chip +140% Q1",
    summary: "Broadcom รายงาน Q2 FY2026 วันที่ 3 มิ.ย. 2026 (6 วันข้างหน้า) ⚠️ — consensus EPS $2.40 (vs $1.58 PY +51.9%), revenue $22.04B (+46.87%) — Q1 custom AI chip revenue +140%, data-center networking +60% — UBS PT $490, Evercore ISI PT $582 — ข่าวนี้ระบุด้วยว่า VEEV Veeva รายงานวันเดียวกัน June 3 — ราคา AVGO $422.01 ณ วันที่ 27 พ.ค. — watchlist entry zone $200-215 ล้าสมัย ต้อง re-analysis ก่อน deploy",
    impact: "POSITIVE", tickers: ["AVGO"],
    url: "https://stockanalysis.com/stocks/avgo/",
  },
  {
    date: "2026-05-27", category: "EARNINGS",
    headline: "VEEV Veeva Systems — ประกาศ Falcon agentic platform + earnings June 3 approaching + ราคา ~$161",
    summary: "Veeva ประกาศ Falcon วันนี้ (27 พ.ค.): agentic platform สำหรับ drug development processes (clinical, regulatory, safety) — early adopter availability November 2026 เป็น part of Veeva AI — YTD -28.6% แม้ customer adoption แข็ง — next earnings June 3 2026 (7 วัน) ⚠️ — consensus EPS +8.1% YoY growth — ราคา ~$161 ยังเหนือ entry zone $148-158 + Conv 6.7 < 7.0 threshold — Falcon อาจเป็น conviction upgrade catalyst ถ้า earnings beat",
    impact: "POSITIVE", tickers: ["VEEV"],
    url: "https://www.stocktitan.net/news/VEEV/veeva-announces-falcon-an-agentic-platform-and-standard-agents-to-4fzhcfg5fjp8.html",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "V Visa — ราคา $329.62 + Agentic Commerce Global Expansion + Stablecoin USDC pilot Canada — DOJ case overhang",
    summary: "Visa ราคา $329.62 (range $325.37-$331.46) — ประกาศ 2 initiatives ใหม่: (1) Agentic Ready program ขยายไปยัง Asia Pacific + Latin America รองรับ agent-led commerce (2) stablecoin USDC settlement pilot Canada กับ Wealthsimple (ข้อมูลเดิมใน news.js) — Commercial Solutions Hub expand กับ Accounts Receivable Manager — 35 analysts Strong Buy avg PT $387.25 (+17.5% upside) — DOJ debit case ยังคงเป็น overhang — watchlist: ราคา $329.62 เหนือ entry zone $285-300 แต่ใกล้ trigger $315 มากขึ้น",
    impact: "MIXED", tickers: ["V"],
    url: "https://stockanalysis.com/stocks/v/",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "FICO Fair Isaac — ราคา $1,273.36 + Smart Plans/Score Potential features ใหม่ + BofA coverage + P/E 39.9x",
    summary: "FICO ราคา $1,273.36 (range $1,242.50-$1,289.50) — ประกาศ Smart Plans และ Score Potential features ใหม่สำหรับ FICO Score Mortgage Simulator — Q2 FY2026 strong revenue growth + FICO Platform ecosystem expand (Pindrop, Mitek partners) — 21 analysts avg Buy PT $1,560.02 (+22.5% upside) — market cap $29.53B P/E 39.9x — watchlist: ราคา $1,273.36 ยังเหนือ IPS trigger $1,071 มาก — ต้องรอ pullback",
    impact: "POSITIVE", tickers: ["FICO"],
    url: "https://www.gurufocus.com/news/8867349/fair-isaac-corp-fico-stock-up-76-and-still-undervalued-gf-score-83100",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "GEV GE Vernova — ราคา $1,072.50 (-3.16% open) + H-class turbine 4M hours + dividend $0.50 ex-Jun 16 + valuation concern",
    summary: "GE Vernova ราคา $1,072.50 เปิดตัวลง -3.16% — analysts ระบุ AI data center demand อาจ 'priced in' หลัง +124% surge ในปีที่ผ่านมา — H-class gas turbine fleet แตะ 4 million commercial operating hours (milestone) — dividend $0.50/qtr ex-date Jun 16 — market cap $287.97B — analyst avg PT $1,217.17 (+13.5% upside) — watchlist: ALERT ราคา $1,072 vs FV $263 ล้าสมัยมากต้อง re-analysis ด่วน — next earnings July 22 2026",
    impact: "MIXED", tickers: ["GEV"],
    url: "https://www.tradingkey.com/news/market-movers/261931313-market-movers-gev-20260527",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "BRK.B Berkshire — ราคา $482.80 + Lingering mysteries จาก portfolio update + cash $397B ยังสูง + Abel strategy",
    summary: "Berkshire ราคา $482.80 (range $482.80-$483.40) — CNBC รายงาน 'lingering mysteries' จาก portfolio update: Abel ยังไม่ deploy cash $397B อย่างชัดเจน — full exit from Amazon, Visa, Mastercard, UnitedHealth + ซื้อ Macy's, Delta ใหม่ + triple Alphabet — สัญญาณว่า Abel เน้น value rotation (financial, consumer staples, airlines) แทน tech heavy BofA ลด PT $581 เป็น $570 คง Buy — watchlist Big 10 ยังรอ analysis",
    impact: "NEUTRAL", tickers: ["BRK.B"],
    url: "https://www.cnbc.com/2026/05/23/lingering-mysteries-from-berkshires-portfolio-update.html",
  },
  {
    date: "2026-05-27", category: "SECTOR",
    headline: "JPM JPMorgan — ราคา $307.43-307.80 + dividend $1.50/qtr July 31 + Micron แซง JPM market cap + AI workforce balance",
    summary: "JPMorgan ราคา $307 market cap $822B — Micron Technology แซง JPM ใน market cap หลัง MU +20% วันที่ 26 พ.ค. — dividend $1.50/qtr payable July 31 (ex-date Jul 6) — Jamie Dimon ยังคงระมัดระวัง AI workforce: gradual transition สมดุล AI roles vs traditional banking — P/E 14.68x dividend yield 1.9% — watchlist Big 10 ยังรอ analysis",
    impact: "NEUTRAL", tickers: ["JPM"],
    url: "https://finance.yahoo.com/quote/JPM/",
  },
  {
    date: "2026-05-27", category: "EARNINGS",
    headline: "WMT Walmart — ราคา $118.57 ร่วง 4 วันติด + Q1 FY2027 beat revenue $177.8B แต่ guidance กดดัน consumer sentiment",
    summary: "Walmart ราคา $118.57 (ลดลง -1.41% จาก $120.27) ร่วง 4 วันติดต่อกัน — Q1 FY2027 actual (revised): revenue $177.8B (beat by $2.97B) EPS $0.66 met estimate — comp sales US +4.1%, e-commerce +26% global, advertising +50% — แต่ stock ยังร่วงเพราะ P/E 48x overvaluation concern + cautious guidance tone — FY guidance reaffirmed: 3.5-4.5% constant currency growth Q2 EPS $0.72-0.74 — consumer spending สัญญาณ softening ยังเป็น macro concern",
    impact: "MIXED", tickers: ["WMT"],
    url: "https://www.cnbc.com/2026/05/21/walmart-wmt-earnings-q1-2027.html",
  },
  {
    date: "2026-05-27", category: "EARNINGS",
    headline: "LLY Eli Lilly — ราคา $1,067-1,069 + $3.8B vaccine acquisitions (Curevo/LimmaTech) + BofA PT $1,251 + gene therapy PCSK9 cut 88%",
    summary: "Eli Lilly ราคา $1,067-1,069 market cap $1T — ประกาศ 3 ข่าวสำคัญวันที่ 27 พ.ค.: (1) $3.8B vaccine acquisitions: Curevo $1.5B + LimmaTech $780M + another $1.55B — diversify นอก GLP-1 (2) gene therapy Phase 1b data: single infusion ลด PCSK9 88% + LDL-C 62% (fast-track FDA) (3) BofA ปรับ PT $1,133 เป็น $1,251 คง Buy — retatrutide TRIUMPH-1 28.3% weight loss เป็น thesis backbone — next catalyst Bernstein conference + TRIUMPH-2/3 results",
    impact: "POSITIVE", tickers: ["LLY"],
    url: "https://www.gurufocus.com/news/8882263/bofa-revamps-eli-lilly-stock-price-target-for-rest-of-2026",
  },
  {
    date: "2026-05-27", category: "AMZN",
    headline: "AMZN Amazon — ราคา $264.65 market cap $2.85T + billionaires loaded up Q1 + supply chain services launch",
    summary: "Amazon ราคา $264.65 (range $264.62-$265.53) market cap $2.85T — Q1 2026: EPS $2.78, revenue +17% YoY, AWS +28% — hedge fund managers ซื้อ Q1: David Tepper (Appaloosa) double stake = largest position + Bill Ackman (Pershing Square) +2M shares + Larry Robbins (Glenview) 6% stake — Amazon Supply Chain Services ใหม่ (freight, fulfillment, parcel delivery) — 66 analysts Strong Buy avg PT $312.63 (+18% upside) — Trefis: 'simple path to 20% upside' — watchlist Big 10 ยังรอ analysis",
    impact: "POSITIVE", tickers: ["AMZN"],
    url: "https://www.fool.com/investing/2026/05/27/several-billionaires-just-loaded-up-on-amazon/",
  },
'''

def read_existing_news(filepath):
    """อ่าน news.js และ extract ข่าวเดิม"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def extract_existing_headlines(content):
    """ดึง headlines ทั้งหมดจาก JS content เพื่อ dedup"""
    pattern = r'headline:\s*"([^"]+)"'
    return set(re.findall(pattern, content))

def build_new_file(existing_content, new_block):
    """สร้างไฟล์ใหม่โดย insert ข่าวใหม่ก่อน // ── 2026-05-22 ──"""

    # เปลี่ยน NEWS_LAST_UPDATED
    new_content = re.sub(
        r'const NEWS_LAST_UPDATED = "[^"]+";',
        'const NEWS_LAST_UPDATED = "2026-05-27 08:00";',
        existing_content
    )

    # Insert ข่าวใหม่หลัง const NEWS = [
    insert_after = 'const NEWS = [\n'
    pos = new_content.find(insert_after)
    if pos == -1:
        insert_after = 'const NEWS = ['
        pos = new_content.find(insert_after)

    if pos == -1:
        print("ERROR: cannot find 'const NEWS = [' in file")
        return None

    insert_pos = pos + len(insert_after)
    new_content = new_content[:insert_pos] + new_block + new_content[insert_pos:]

    return new_content

def main():
    print(f"Reading: {NEWS_JS_PATH}")
    existing_content = read_existing_news(NEWS_JS_PATH)

    # Check existing headlines for dedup
    existing_headlines = extract_existing_headlines(existing_content)
    print(f"Found {len(existing_headlines)} existing headlines")

    # Check for duplicates in new block
    new_headlines = re.findall(r'headline:\s*"([^"]+)"', NEW_NEWS_BLOCK)
    duplicates = [h for h in new_headlines if h in existing_headlines]

    if duplicates:
        print(f"WARNING: {len(duplicates)} duplicate headlines found (will be skipped by insert):")
        for d in duplicates:
            print(f"  - {d[:80]}...")

    print(f"New headlines to add: {len(new_headlines)}")

    # Build new file
    new_content = build_new_file(existing_content, NEW_NEWS_BLOCK)

    if new_content is None:
        print("ERROR: Failed to build new content")
        return

    # Write file
    with open(NEWS_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"SUCCESS: news.js updated with {len(new_headlines)} new items")
    print(f"NEWS_LAST_UPDATED set to: 2026-05-27 08:00")

    # Verify
    with open(NEWS_JS_PATH, 'r', encoding='utf-8') as f:
        verify_content = f.read()

    total_headlines = len(re.findall(r'headline:\s*"[^"]+"', verify_content))
    print(f"Total headlines in file: {total_headlines}")

if __name__ == "__main__":
    main()
