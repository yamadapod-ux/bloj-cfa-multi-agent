"""Apply Round 95 edits to a watchlist.md text (CRLF). Usage: apply_r95.py IN OUT REPORT"""
import sys
src, dst, rep_path = sys.argv[1:4]
s = open(src, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in s[:5000] else '\n'
rep = open(rep_path, encoding='utf-8').read().replace('\r\n', '\n').replace('\n', nl)

old = '*ล่าสุด (2026-11-13): **Scout Round 94'
assert s.count(old) == 1, 'header anchor'
new = ('*ล่าสุด (2026-11-14): **Scout Round 95 — Digital Advertising / Ad Tech** — dedicated round แรกของ sector '
       '(TTD/SNAP/PINS/CRTO/ZD/QNST/STGW/MGNI/PUBM/DV; IAS take-private แล้ว). close 11-13 (Yahoo = Nasdaq). '
       'Filter A 4/10 → C 1 (TTD) → D 0. **0 fast-track · 0 learning-queue · 10 reject**. Prune: 0 de-listed, SLA 5 → 11-18*'
       + nl + '*ก่อนหน้า (2026-11-13): **Scout Round 94')
s = s.replace(old, new)

anchor = '**Prune Pass 2026-11-08 (Mode 1 Step 0 — Round 89):**'
assert s.count(anchor) == 1, 'prune anchor'
note = ('**Prune Pass 2026-11-14 (Mode 1 Step 0 — Round 95):** ตรวจ live Pending ทั้ง 9 แถวตาม De-list Rules #1-3 '
        'พร้อมราคาสด 2 แหล่ง (Yahoo = Nasdaq, close 11-13). **De-listed 0 · SLA fixed 5** · live 9.' + nl +
        '- **SLA re-fix → 2026-11-18:** WYNN / VICI / ALLY / NBIX / BYD (target 11-14 ผ่านไปโดยยังไม่ได้รัน Tier 1). '
        '⚠️ WYNN/VICI ครบ 60 วันในวันที่ 11-19 → ถ้ายังไม่รัน Tier 1 ภายใน 11-18 ให้ archive ใน prune รอบแรกหลัง 11-19' + nl +
        '- **Rule #2:** ไม่มีตัวไหนเกิน 2× ขอบบน zone (สูงสุด NBIX $167.40 ≈1.24×) · **Rule #3:** decisions.md ไม่มี hit · '
        '**ธง (ไม่ผ่าน Filter A):** VICI −18.3% · ALLY −19.0% · BYD −15.5% · NBIX −10.1%' + nl + nl)
s = s.replace(anchor, note + anchor)

lines = s.split(nl)
fixed = []
for i, l in enumerate(lines):
    for t in ('WYNN', 'VICI', 'ALLY', 'NBIX', 'BYD'):
        if l.startswith(f'| {t} |') and t not in fixed and 'Round 95 prune' not in l:
            r = l.rstrip()
            assert r.endswith('|')
            extra = ' · ครบ 60 วันในวันที่ 11-19 → archive ถ้ายังไม่รัน' if t in ('WYNN', 'VICI') else ''
            lines[i] = r[:-1].rstrip() + (f' **SLA re-fix 2026-11-14 (Round 95 prune): Target 2026-11-18** '
                                          f'(target 11-14 ผ่านไปโดยยังไม่ได้รัน Tier 1{extra}) |')
            fixed.append(t)
assert sorted(fixed) == sorted(['WYNN', 'VICI', 'ALLY', 'NBIX', 'BYD']), fixed
s = nl.join(lines)
s = s.rstrip('\r\n') + nl + rep.strip('\r\n').join([nl, nl]) if False else s.rstrip('\r\n') + nl + rep.rstrip('\r\n') + nl
open(dst, 'w', encoding='utf-8', newline='').write(s)
print('ok', fixed)
