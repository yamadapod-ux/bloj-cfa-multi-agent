# Round 92 -- apply edits to watchlist.md / deployment_log.md text. Used on both the HEAD blob (for staging only R92 changes)
# and the working tree (which also holds uncommitted Round 90 edits the CIO asked not to commit).
# Matches the target file's line ending (HEAD blob = LF, Windows working tree = CRLF).
import sys, os
D = os.path.dirname(os.path.abspath(__file__))
LF, CRLF = chr(10), chr(13) + chr(10)
kind, src, dst = sys.argv[1:]
s = open(src, encoding='utf-8', newline='').read()
NL = CRLF if CRLF in s else LF
def rd(n):
    return open(os.path.join(D, n), encoding='utf-8').read().replace(CRLF, LF).strip(LF).replace(LF, NL)
def wl(s):
    old = '*ล่าสุด (2026-11-09): **Scout Round 91'
    assert s.count(old) == 1 and 'Scout Round 92' not in s, 'unexpected watchlist state'
    s = s.replace(old, rd('r92_header.md') + NL + '*ก่อนหน้า (2026-11-09): **Scout Round 91', 1)
    return s.rstrip(CRLF) + NL + NL + rd('r92_section.md') + NL
def dl(s):
    assert 'Scout Round 92' not in s, 'already applied'
    return s.rstrip(CRLF) + NL + NL + rd('r92_deploylog.md') + NL
open(dst, 'w', encoding='utf-8', newline='').write(wl(s) if kind == 'wl' else dl(s))
