import sys, subprocess
R=open('scripts/scout/2026-11-14_r96/r96.md',encoding='utf-8').read()
HDR=("*ล่าสุด (2026-11-14): **Scout Round 96 — Electronic Components / EMS / PCB / Optical** — CIO สั่ง Metals & Mining แต่ซ้ำ R79 (10-18) / R80 (10-19) ใน 30 วัน และตัวเลือกสำรองทั้ง 4 ก็ซ้ำ → เปลี่ยนเป็น sector ที่ไม่เคยสแกน. "
     "close 11-13 (Yahoo = Nasdaq). 15 screened → A 13/15 (TTMI −66.9% · VSH −61.7% · FN −56.2% · FLEX −55.1% ฯลฯ; TEL/CTS ตก) → B-Zero 13 → B 8 (FLEX/KN/PLXS/ROG ตก) → C 7 (VSH/LFUS ตก) → D-V1 ทุกตัว \"เห็นต่างกันเอง\" → Tier 1 check 2a 3.4×–7.6× naive FV. "
     "**0 fast-track · 0 learning-queue · 15 reject (7 QUICK-SCREEN SKIP: JBL/SANM/TTMI/FN/BELFB/BHE/OSIS)**. ไม่มีตัวเข้า AI/Infra lane (TTMI ผ่าน 2/3). Prune: ทำแล้วใน R95*\n")
DL=("\n## Scout Round 96 — Electronic Components / EMS / PCB / Optical — 2026-11-14\n\n| Ticker | Tag | เหตุผล |\n|---|---|---|\n"
"| JBL | `QUICK-SCREEN SKIP` (Tier 1 check 2a) | $254.25 (11-13) −40.7% จาก $428.93 · A ✅ (AI-hardware de-rate) · B-Zero ✅ · B-V1 ✅ เฉพาะ sector-avg · C ✅ ROIC 24.5% · naive FV $74.20 (5Y FCF $890M ÷ 9% − ND) → **3.43×** (TTM 2.02×) |\n"
"| SANM | `QUICK-SCREEN SKIP` (Tier 1 check 2a) | $158.31 −45.2% · B-V1 ✅ sector-avg · C ✅ 8.1%/12.7% · naive FV $33.79 → **4.69×** (TTM 1.62×) |\n"
"| TTMI | `QUICK-SCREEN SKIP` (Tier 1 check 2a) | $74.08 −66.9% · B-V1 ✅ sector-avg · C ✅ · 5Y FCF avg $100M (TTM $15M) → naive FV ≈ $0.44 → **n/m** · AI/Infra lane FAIL ข้อ 1 (capex/rev 8.4%, capex 9M +13%) |\n"
"| FN | `QUICK-SCREEN SKIP` (Tier 1 check 2a) | $327.98 −56.2% · B-V1 ✅ sector-avg · C ✅ 15.6% · naive FV $66.21 → **4.95×** (FCF TTM −$190M) |\n"
"| BELFB | `QUICK-SCREEN SKIP` (Tier 1 check 2a) | $225.49 −32.7% · B-V1 ✅ peer-median 0.93× · C ✅ 10.8% · naive FV $65.83 → **3.43×** (TTM 2.50×) |\n"
"| BHE | `QUICK-SCREEN SKIP` (Tier 1 check 2a) | $63.03 −37.2% · B-V1 ✅ sector-avg · C ✅ borderline 8.1% ex-cash · naive FV $8.34 → **7.56×** (TTM 1.74×) |\n"
"| OSIS | `QUICK-SCREEN SKIP` (Tier 1 check 2a) | $192.92 −38.1% · B-Legacy ✅ FCF yield 8.7% TTM · C ✅ 9.7% · 5Y FCF avg $67M < ND $699M × 10% → naive FV ติดลบ (TTM 1.56×) |\n\n"
"- **Action:** ไม่มี trade · TEL/CTS ตก A · FLEX/KN ตก B-V1 · PLXS/ROG ตก B-Legacy · VSH/LFUS/ROG ตก C — ไม่นับเป็น QUICK-SCREEN SKIP\n"
"- **Regime:** TRANSITIONAL-CAUTIOUS (Atlas 11-06) — ห้าม open ใหม่อยู่แล้ว\n"
"- **Data:** ราคา Yahoo + Nasdaq (close 2026-11-13) · SEC XBRL companyfacts · `scripts/scout/2026-11-14_r96/`. ตารางเต็ม: `portfolio/watchlist.md` § Scout Report Round 96.\n\n"
"*Max — 2026-11-14 | Scout Round 96 — 0 fast-track, 0 learning-queue, 7 QUICK-SCREEN SKIP; no trade.*\n")
def wl(s):
    old="*ล่าสุด (2026-11-14): **Scout Round 95"
    assert s.count(old)==1
    s=s.replace(old,"*ก่อนหน้า (2026-11-14): **Scout Round 95",1)
    i=s.index("*ก่อนหน้า (2026-11-14): **Scout Round 95")
    s=s[:i]+HDR+s[i:]
    return s.rstrip('\n')+'\n'+R
def dl(s): return s.rstrip('\n')+'\n'+DL
def run(*a,inp=None): return subprocess.run(a,capture_output=True,input=inp,check=True).stdout
for path,fn in [('portfolio/watchlist.md',wl),('portfolio/deployment_log.md',dl)]:
    head=run('git','show','HEAD:'+path).decode('utf-8')
    work=open(path,encoding='utf-8',newline='').read()
    assert 'Round 96' not in work
    staged=fn(head)
    open(path,'w',encoding='utf-8',newline='').write(fn(work))
    h=run('git','hash-object','-w','--stdin',inp=staged.encode('utf-8')).decode().strip()
    run('git','update-index','--cacheinfo','100644,'+h+','+path)
    print(path,'staged',h)
