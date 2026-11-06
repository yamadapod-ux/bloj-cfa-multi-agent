# Insert Round 87 into watchlist.md/deployment_log.md, preserving each file's line endings. Refuses to run twice.
root = '../../../portfolio/'
wl = open(root + 'watchlist.md', 'rb').read()
nl = '\r\n' if b'\r\n' in wl[:400] else '\n'


def enc(path, eol):
    return open(path, encoding='utf-8', newline='').read().replace('\r\n', '\n').replace('\n', eol).encode()


assert 'Scout Round 87'.encode() not in wl
latest = ('*ล่าสุด (2026-11-06): **Scout Round 87 — Niche/Specialty REITs** (ครั้งแรก; SUI/ELS/UMH · OUT/LAMR · CXW/GEO · '
          'OHI/NHI/LTC/SBRA/CTRE + เช็คซ้ำ WELL/VTR, Yahoo/Nasdaq close 11-05). Filter A 3/14 (GEO/CXW/NHI) → B 3 → C 3 → D 0. '
          '**0 fast-track · 0 learning-queue · 14 reject**. CXW/GEO ไม่ใช่ REIT ตั้งแต่ 2021 และผ่าน A เพราะการลงวันเดียว 11-05; '
          'naive FV through-cycle 0.99–1.62× และ E 0/3. NHI 1.09× งบ Q3 ออก 11-09 → re-check. Prune: 0 de-listed.*' + nl).encode()
old = '*ล่าสุด (2026-11-05):'.encode()
assert wl.count(old) == 1
wl = wl.replace(old, latest + '*ก่อนหน้า (2026-11-05):'.encode())
key = '**Prune Pass 2026-11-05 (Mode 1 Step 0 — Round 86):**'.encode()
assert wl.count(key) == 1
wl = wl.replace(key, enc('prune.md', nl) + key)
wl = wl.rstrip() + nl.encode() + enc('r87.md', nl)
open(root + 'watchlist.md', 'wb').write(wl)

d = open(root + 'deployment_log.md', 'rb').read()
assert 'Scout Round 87'.encode() not in d
nd = '\r\n' if b'\r\n' in d[:400] else '\n'
open(root + 'deployment_log.md', 'wb').write(d.rstrip() + nd.encode() + enc('dep.md', nd))
print('ok', repr(nl), repr(nd))
