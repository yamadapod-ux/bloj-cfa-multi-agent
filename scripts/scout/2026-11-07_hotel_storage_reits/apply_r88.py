# Insert Round 88 into watchlist.md/deployment_log.md, preserving each file's line endings. Refuses to run twice.
root = '../../../portfolio/'
wl = open(root + 'watchlist.md', 'rb').read()
nl = '\r\n' if b'\r\n' in wl[:400] else '\n'


def enc(path, eol):
    return open(path, encoding='utf-8', newline='').read().replace('\r\n', '\n').replace('\n', eol).encode()


assert 'Scout Round 88'.encode() not in wl
latest = ('*ล่าสุด (2026-11-07): **Scout Round 88 — Hotel/Lodging + Self-Storage REITs** (HST/PK/RHP/APLE/SHO/XHR/DRH · EXR/CUBE, '
          'Yahoo/Nasdaq close 11-06; LSI และ NSA ถูกซื้อกิจการแล้ว). Filter A 0/9 (−0.5% ถึง −8.2%). '
          '**0 fast-track · 0 learning-queue · 9 reject**. Prune: 0 de-listed, SLA fixed CRI → 11-12.*' + nl).encode()
old = '*ล่าสุด (2026-11-06):'.encode()
assert wl.count(old) == 1
wl = wl.replace(old, latest + '*ก่อนหน้า (2026-11-06):'.encode())
key = '**Prune Pass 2026-11-06 (Mode 1 Step 0 — Round 87):**'.encode()
assert wl.count(key) == 1
wl = wl.replace(key, enc('prune.md', nl) + key)
cri = 'expected late Oct / early Nov 2026); fallback 2026-11-06** |'.encode()
assert wl.count(cri) == 1
wl = wl.replace(cri, ('expected late Oct / early Nov 2026); fallback 2026-11-06** **SLA re-fix 2026-11-07 (Round 88 prune): Target 2026-11-12** — '
                      'fallback ผ่านไปแล้วโดยไม่ได้รัน lightweight; งบ Q3 ออก 10-30 · ราคา $32.01 (close 11-06, Yahoo = Nasdaq) = −28.0% จาก high อยู่ใน entry zone |').encode())
wl = wl.rstrip() + nl.encode() + enc('r88.md', nl)
open(root + 'watchlist.md', 'wb').write(wl)

d = open(root + 'deployment_log.md', 'rb').read()
assert 'Scout Round 88'.encode() not in d
nd = '\r\n' if b'\r\n' in d[:400] else '\n'
open(root + 'deployment_log.md', 'wb').write(d.rstrip() + nd.encode() + enc('dep.md', nd))
print('ok', repr(nl), repr(nd))
