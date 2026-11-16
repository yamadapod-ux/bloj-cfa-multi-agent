P='portfolio/watchlist.md'
s=open(P,encoding='utf-8').read()
assert 'Round 97' not in s
R=open('scripts/scout/2026-11-15_gaming/r97.md',encoding='utf-8').read()
HDR=("*ล่าสุด (2026-11-15): **Scout Round 97 — Gaming Equipment / Lottery & Betting Technology** — universe ที่ CIO ให้มาเปลี่ยนไปแล้ว: IGT → Brightstar Lottery (BRSL) · EVRI/AGS/GAN ถูก take-private · LNW ย้ายไป ASX → เพิ่ม SRAD/GENI/ACEL. close 11-13 (Yahoo = Nasdaq). "
     "5 screened → A 4/5 (INSE −55.8% · SRAD −47.0% · GENI −45.9% · BRSL −41.4%; ACEL ตก) → B-Zero 3 (INSE ตก: equity ติดลบจากขาดทุนสะสม) → C 1 (BRSL/GENI ตก) → SRAD ตก E 0/3 (short report + class action). "
     "**0 fast-track · 0 learning-queue · 5 reject**. Prune: WYNN Tier 1 `QUICK-SCREEN SKIP` (1.08–1.74× naive FV) + VICI ตก A → archive 2 · live 9 → 7*\n")
old="*ล่าสุด (2026-11-14): **Scout Round 96"
assert s.count(old)==1
s=s.replace(old,"*ก่อนหน้า (2026-11-14): **Scout Round 96",1)
i=s.index("*ก่อนหน้า (2026-11-14): **Scout Round 96"); s=s[:i]+HDR+s[i:]
PR=("**Prune Pass 2026-11-15 (Mode 1 Step 0 — Round 97):** ตรวจ live Pending ทั้ง 9 แถวตาม De-list Rules #1-3 (ราคา close 11-13, Yahoo = Nasdaq — ไม่มีซื้อขายตั้งแต่ R95). **De-listed 2 · SLA fixed 0** · live 9 → **7**.\n"
"- **WYNN → Archive:** รัน Tier 1 ที่ค้างตั้งแต่ R75 (SEC 10-Q 2026-09-30) — naive FV (levered FCF ÷ CoE 10.3%) = TTM 1.74× · FCF หลัง maintenance capex ปกติ 1.14× · เฉลี่ย FY23–25 1.08× → ติด check 2a/2b → `QUICK-SCREEN SKIP` (equity −$217.5M · ND/EBITDA 6.1×) — ⚠️ ยังไม่ได้บันทึกใน `deployment_log.md` (scope commit รอบนี้ = watchlist.md เท่านั้น)\n"
"- **VICI → Archive:** re-screen ภายใต้ Filter A–E ปัจจุบันตามที่ R75 กำหนด — −18.3% (Nasdaq high → −18.9%) ตก A ติดกัน 2 prune\n"
"- **Rule #2:** ไม่มีตัวไหนเกิน 2× ขอบบน zone · **Rule #3:** decisions.md ไม่มี hit · **SLA:** ALLY/NBIX/BYD 11-18 · CMRE 11-17 · CRI/MMS 11-20 · WGO 12-19 ยังไม่ถึงกำหนด · ธง (ไม่ผ่าน A): ALLY −19.0% · BYD −15.5% · NBIX −10.1%\n\n")
anchor="**Prune Pass 2026-11-14 (Mode 1 Step 0 — Round 95):**"
assert s.count(anchor)==1
s=s.replace(anchor,PR+anchor,1)
L=s.split('\n')
rows={}
for t in ('WYNN','VICI'):
    idx=[k for k,l in enumerate(L) if l.startswith(f'| {t} | ')]
    assert len(idx)==1, (t,idx); rows[t]=idx[0]
for k in sorted(rows.values(),reverse=True): del L[k]
s='\n'.join(L)
AR=("| WYNN | Wynn Resorts, Limited | 2026-09-20 | 2026-11-15 | Superseded (Rule #3) — Round 97 prune: รัน Tier 1 Quick-Screen ที่ค้างตั้งแต่ R75 ผลคือ `QUICK-SCREEN SKIP` (check 2a/2b): naive FV = levered FCF ÷ CoE 10.3% → TTM FCF $515M 1.74× · FCF หลัง maintenance capex ปกติ $789M 1.14× · เฉลี่ย FY23–25 $835M 1.08× (ยังไม่หัก minority Wynn Macau) · equity −$217.5M · ND/EBITDA 6.1× (SEC 10-Q 2026-09-30) | $85.06 (11-13, Yahoo = Nasdaq) · −36.9% จาก high $134.72 |\n"
    "| VICI | VICI Properties Inc. | 2026-09-20 | 2026-11-15 | Superseded (Rule #3) — Round 97 prune: re-screen ภายใต้ Filter A–E ปัจจุบันตามเงื่อนไขที่ R75 ตั้งไว้ ('ถ้าไม่ผ่าน A → archive') — ตก A ติดกัน 2 prune (R95, R97) · REIT ยังไม่มี lane/framework เฉพาะ | $25.01 (11-13, Yahoo = Nasdaq) · −18.3% จาก high $30.60 (Nasdaq $30.83 → −18.9%) |")
h="| Ticker | Company | Original Scout Date | De-listed Date | Reason | Final Snapshot |\n|--------|---------|---------------------|-----------------|--------|-----------------|\n"
i=s.index('## 🗄️ Archive — De-listed Candidates'); j=s.index(h,i)+len(h)
s=s[:j]+AR+'\n'+s[j:]
s=s.rstrip('\n')+'\n'+R
open(P,'w',encoding='utf-8',newline=chr(13)+chr(10)).write(s)
print('ok')
