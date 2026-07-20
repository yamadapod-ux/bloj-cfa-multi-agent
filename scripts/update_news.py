#!/usr/bin/env python3
# update_news.py — Atlas News Scan 2026-05-20
# ใช้ python binary เขียน news.js เพื่อป้องกัน newline collapse จาก Write tool

import re
import os

NEWS_JS_PATH = r"C:\Users\user\Desktop\บลจ\บลจ CFA\dashboard\news.js"

NEW_NEWS_ITEMS = r"""  // ── 2026-05-20 ──────────────────────────────────────────────────────────────
  {
    date: "2026-05-20", category: "EARNINGS",
    headline: "NVDA Nvidia Q1 FY2027 Earnings Day — consensus $78.8B revenue, $1.77 EPS รายงาน AH วันนี้",
    summary: "Nvidia รายงาน Q1 FY2027 หลังปิดตลาด 20 พ.ค. 5PM ET — consensus revenue $78.8B (+78% YoY), EPS $1.77 — Q2 guidance ที่ตลาดคาด ~$87B เป็นตัวชี้วัดสำคัญที่สุด — 3 ประเด็นที่ตลาดจับตา: (1) gross margin direction vs guidance 75% (2) Q2 guidance vs $87B bar (3) China policy + Vera Rubin transition — options market price in 5-10% move — AVGO ADD trigger $200-215 active ถ้า NVDA miss + ราคา AVGO ร่วง — ณ ตอนที่ scan ข่าว actual results ยังไม่ออก: NVDA ปิด $220.61 pre-market $223.92",
    impact: "MIXED", tickers: ["NVDA", "AVGO", "AMD", "MRVL", "TSM"],
    url: "https://www.marketbeat.com/earnings/reports/2026-5-20-nvidia-co-stock/",
  },
  {
    date: "2026-05-20", category: "EARNINGS",
    headline: "INTU Intuit Q3 FY2026 Earnings Day — consensus EPS $12.57 Revenue $8.54B รายงาน AH วันนี้",
    summary: "Intuit รายงาน Q3 FY2026 หลังปิดตลาด 20 พ.ค. 4PM ET — consensus EPS $12.57 revenue $8.54B (+10% YoY) — company guidance: GAAP EPS $10.56-10.62, non-GAAP EPS $12.45-12.51 — Intuit beat consensus 4 ไตรมาสติดต่อกัน avg beat 7.97% — portfolio impact: T1 OPEN 0.67 shares @ $445 — T2 trigger: miss → $395-430 / T3 trigger: beat → $450-480 — ราคา INTU วันที่ 19 พ.ค. $403.12 ต่ำกว่า entry $445 = unrealized -9.4%",
    impact: "MIXED", tickers: ["INTU"],
    url: "https://news.alphastreet.com/intuit-q3-2026-earnings-preview-may-20-street-expects-12-57-eps/",
  },
  {
    date: "2026-05-20", category: "EARNINGS",
    headline: "WMT Walmart Q1 FY2027 Earnings พรุ่งนี้ (21 พ.ค.) — consensus revenue $174.95B EPS $0.66",
    summary: "Walmart รายงาน Q1 FY2027 เช้าวันที่ 21 พ.ค. 6AM CDT — consensus: revenue $174.95B (+5.6% YoY), EPS $0.66 (+8.2%), operating income $7.75B — หุ้น WMT ทำ ATH ก่อนงบ ราคา $134.26 YTD +19% — 3 ประเด็นหลัก: US same-store sales 3.9-4.5%, e-commerce +24%, advertising revenue +30% — consumer confidence ต่ำสุดในประวัติศาสตร์เป็น headwind — Walmart ในฐานะ Big 10 watchlist: ไม่มี analysis เดิม",
    impact: "MIXED", tickers: ["WMT"],
    url: "https://www.businesswire.com/news/home/20260514910833/en/Walmart-To-Host-First-Quarter-Earnings-Conference-Call-May-21-2026",
  },
  {
    date: "2026-05-20", category: "EARNINGS",
    headline: "MRVL Marvell Technology — Q1 FY2027 earnings May 27 consensus revenue $2.4B EPS $0.79 analyst upgrades",
    summary: "Marvell รายงาน Q1 FY2027 วันที่ 27 พ.ค. — consensus: revenue $2.4B (+27% YoY), EPS $0.79 (+27% YoY) — FY2027 guidance approach $11B (+30% YoY) vs prior $10B — FY2028 guidance ~$15B (+40% YoY) — analyst upgrades: BofA PT $200, Goldman $200, Melius $220, B.Riley $205 — NVDA invest $2B ใน Marvell optical business — AMD เปิดเผย equity stake ใน MRVL ผ่าน 13F — หุ้น +135% ตั้งแต่ March 5 — ⚠️ watchlist analysis เดิม FV $120 ล้าสมัย",
    impact: "POSITIVE", tickers: ["MRVL", "NVDA", "AMD"],
    url: "https://www.tipranks.com/news/marvell-stock-mrvl-gets-price-target-hikes-from-top-analysts-ahead-of-q1-earnings",
  },
  {
    date: "2026-05-20", category: "TECH",
    headline: "AVGO Broadcom — Evercore ISI ปรับ PT $490→$582 (Outperform) UBS ปรับ $475→$490 ราคาปิด $420.71",
    summary: "Broadcom ได้รับ analyst upgrades ต่อเนื่อง: Evercore ISI ปรับ PT $582 (+18.7% จาก $490), UBS ปรับ $490 — consensus analyst Buy rating ทั้ง 26 คน, avg PT $463.58 — LSEG (London Stock Exchange Group) เซ็น 5-year technology partnership ใหม่กับ Broadcom — ราคาปิด $420.71 (vs portfolio.js ที่บันทึก $230 ซึ่งผิด) — ⚠️ CRITICAL: portfolio.js AVGO entry zone $200-215 และ analysis price $230 ต้อง re-verify เนื่องจากราคาจริงคือ ~$420 — NVDA earnings วันนี้ = สัญญาณสำหรับ AVGO กลุ่ม AI semi",
    impact: "POSITIVE", tickers: ["AVGO"],
    url: "https://www.marketbeat.com/stocks/NASDAQ/AVGO/forecast/",
  },
  {
    date: "2026-05-20", category: "TECH",
    headline: "NOW ServiceNow — BofA reinstates Buy $130 PT, 47 analysts Strong Buy, next earnings Jul 29 2026",
    summary: "ServiceNow รับ Bank of America reinstate Buy rating ที่ PT $130 — 47 analysts consensus Strong Buy, avg 12M PT $143.06 (+38% upside จาก $101.83) — NOW ราคา $101.83 (52W range $81.24-$211.48) YTD -39% — Knowledge 2026 conference: AI-native products, autonomous AI specialist agents — partnership ใหม่กับ Experian (multi-year AI) — next earnings Jul 29 2026 — ⚠️ portfolio: T1 OPEN @ $89.47 (+15.26%) แต่ FV $226 ยังไม่ verified pending re-analysis",
    impact: "POSITIVE", tickers: ["NOW"],
    url: "https://finance.yahoo.com/quote/NOW/",
  },
  {
    date: "2026-05-20", category: "TECH",
    headline: "ADBE Adobe — ราคา $255.64 (19 พ.ค.) อยู่เหนือ avg entry $247.03 | next earnings Jun 11 2026",
    summary: "Adobe ราคา $255.64 (May 19) ขึ้นจาก $241 entry T2 = unrealized gain ~6.1% บน avg basis $247.03 — 52W range $224.13-$422.95 — analyst avg PT $327.28 (Buy consensus 15 vs Sell 4) — Product: AI productivity agent + PDF Spaces launched May 6 — Semrush acquisition ดำเนินต่อ — $25B buyback 2030 expire — next earnings Jun 11 2026 AMC, Q2 guidance revenue $6.43-6.48B — portfolio: OPEN 4 shares avg $247.03, costbasis $988.10",
    impact: "POSITIVE", tickers: ["ADBE"],
    url: "https://finance.yahoo.com/quote/ADBE/",
  },
  {
    date: "2026-05-20", category: "TECH",
    headline: "TSLA Tesla — ราคา $404.68 FSD probe NHTSA engineering analysis + SpaceX IPO overhang",
    summary: "Tesla ราคา $404.68 (May 20, range $393-406) market cap $1.52T P/E 374.56 — NHTSA upgrade FSD probe เป็น engineering analysis (Mar 2026): 3.2M vehicles, 9 incidents (1 fatality) visibility failure — Australian court criticize Tesla ใน class action (May 15) — SpaceX IPO overhang กดดัน Musk attention split — แต่มี positive: Piper Sandler 'Buy Optimus for Free' note, FSD progress, Q1 EPS $0.41 beat $0.36 — deliveries Q1 358K ต่ำกว่า consensus 365K",
    impact: "MIXED", tickers: ["TSLA"],
    url: "https://finance.yahoo.com/quote/TSLA/",
  },
  {
    date: "2026-05-20", category: "TECH",
    headline: "AAPL Apple — ราคา $298.98 Fortnite กลับ App Store + hardware team reorg รองรับ AI",
    summary: "Apple ราคา $298.98 (May 20, range $296-300) 52W range $193-$303 near ATH — Fortnite กลับ App Store global หลัง Epic lawsuit settlement — Apple Intelligence หนุน iOS 20 AI subscription path — hardware development team reorg เพื่อรองรับ AI integration — wheelchair control via Vision Pro eye tracking (accessibility milestone) — analyst Buy consensus 30 vs Sell 2, avg PT $308 — next catalyst: WWDC 2026",
    impact: "POSITIVE", tickers: ["AAPL"],
    url: "https://finance.yahoo.com/quote/AAPL/",
  },
  {
    date: "2026-05-20", category: "SECTOR",
    headline: "BRK.B Berkshire Hathaway — Greg Abel era: $2.65B Delta stake, triple Alphabet, dump Amazon ใน Q1 2026",
    summary: "Berkshire 13F Q1 2026 (เปิดเผย May 15) แสดงการเปลี่ยนแปลงครั้งใหญ่ที่สุดในรอบปีภายใต้ Greg Abel CEO: (1) ซื้อ Delta Air Lines $2.65B (39.8M shares) — airline กลับมาครั้งแรกหลัง 2020 exit (2) triple Alphabet stake แทนที่ GOOGL (3) ขาย Amazon ออก — ราคา BRK.B $488.28 (May 19) — strategy shift ชัด: Abel เน้น value กว่า Buffett ในด้านการ rotate sectors",
    impact: "POSITIVE", tickers: ["BRK.B"],
    url: "https://fortune.com/2026/05/15/berkshire-hathaway-alphabet-stock-delta-stock-amazon-shares-ceo-greg-abel-13f-q1/",
  },
  {
    date: "2026-05-20", category: "MACRO",
    headline: "Fed Leadership Transition — Powell อาจสิ้นสุด term, new Fed Chair ใกล้เข้ามา uncertainty สูง",
    summary: "FOMC เมษายน 2026 อาจเป็น meeting สุดท้ายของ Powell — Fed rate คง 3.5-3.75% ด้วยมติ 8-4 (dissent สูงสุดตั้งแต่ Oct 1992) — J.P. Morgan Global Research: Fed hold ทั้งปี 2026, next move likely hike 25 bps ใน Q3 2027 — uncertainty สูงจาก leadership transition + inflation 3.8% ยังเกิน target 2% — เป็น headwind เพิ่มเติมต่อ growth stocks ทุกตัวใน portfolio",
    impact: "NEGATIVE", tickers: ["ADBE", "NOW", "INTU", "MSFT", "VEEV"],
    url: "https://www.cnbc.com/2026/04/29/fed-interest-rate-decision-april-2026.html",
  },
  {
    date: "2026-05-20", category: "REGULATION",
    headline: "GOOGL Google DOJ antitrust — ถูกสั่งห้ามทำ exclusive contracts, share data กับ competitors",
    summary: "ผล DOJ antitrust case ต่อ Google (Sept 2025): ไม่ต้องแยก Chrome/Android แต่ถูกสั่ง: (1) ห้าม exclusive search contracts (2) share user data กับ competitors (3) เปิดเผย AI training methodology — ทั้ง Google และ DOJ appeal portions ต่อไป — Morgan Stanley: choice screens อาจกระทบ Google search traffic 5-8% ใน 3 ปี = $15-25B annual ad revenue at risk — GOOGL ราคา context: Berkshire เพิ่ม stake ถึง 3x ใน Q1 2026",
    impact: "NEGATIVE", tickers: ["GOOGL"],
    url: "https://tech-insider.org/google-antitrust-appeal-doj-search-monopoly-2026/",
  },
"""

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    content = read_file(NEWS_JS_PATH)

    # Update timestamp
    content = re.sub(
        r'const NEWS_LAST_UPDATED = "[^"]*";',
        'const NEWS_LAST_UPDATED = "2026-05-20 08:30";',
        content
    )

    # Find insertion point — after "const NEWS = [" and before first comment/item
    insert_marker = "const NEWS = [\n"
    insert_pos = content.find(insert_marker)
    if insert_pos == -1:
        print("ERROR: Could not find 'const NEWS = [' in news.js")
        return False

    insert_at = insert_pos + len(insert_marker)
    content = content[:insert_at] + NEW_NEWS_ITEMS + content[insert_at:]

    write_file(NEWS_JS_PATH, content)
    print("SUCCESS: news.js updated with 2026-05-20 news items")
    return True

if __name__ == "__main__":
    main()
