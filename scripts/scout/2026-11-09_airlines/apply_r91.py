# Insert Round 91 header (new line 3, demote old "ล่าสุด" to "ก่อนหน้า") and append the R91 section.
# Usage (repo root): python -I scripts/scout/2026-11-09_airlines/apply_r91.py SRC DST
import sys
src, dst = sys.argv[1], sys.argv[2]
d = 'scripts/scout/2026-11-09_airlines/'
t = open(src, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in t else '\n'
hdr = open(d + 'r91_header.md', encoding='utf-8').read().strip()
sec = open(d + 'r91_section.md', encoding='utf-8').read().rstrip('\n')
assert 'Round 91' not in t, 'already applied'
lines = t.split(nl)
assert lines[2].startswith('*ล่าสุด'), lines[2][:40]
lines[2] = '*ก่อนหน้า' + lines[2][len('*ล่าสุด'):]
lines.insert(2, hdr)
out = nl.join(lines).rstrip(nl) + nl + sec.replace('\n', nl) + nl
open(dst, 'w', encoding='utf-8', newline='').write(out)
print('ok', dst, len(out.split(nl)))
