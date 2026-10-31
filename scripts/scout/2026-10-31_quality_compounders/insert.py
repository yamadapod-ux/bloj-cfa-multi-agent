# Insert Quality Compounder section into portfolio/watchlist.md (before "## Scout History")
import os
here=os.path.dirname(os.path.abspath(__file__))
t=open(os.path.join(here,'tbl.md'),encoding='utf8').read().strip().split('\n')
tbl='\n'.join([t[0],t[1]]+t[2:][::-1])  # closest-to-trigger first
sec=open(os.path.join(here,'section.md'),encoding='utf8').read().replace('{TABLE}',tbl)
p=os.path.join(here,'..','..','..','portfolio','watchlist.md'); s=open(p,encoding='utf8').read()
assert 'Quality Compounder Watchlist -- Expensive Wide-Moat' not in s
i=s.index('## Scout History'); s=s[:i]+sec+'\n---\n\n'+s[i:]
old='*ล่าสุด (2026-10-31): **AI Selloff Watch'
assert old in s
s=s.replace(old,'*ล่าสุด (2026-10-31): **Quality Compounder Watchlist -- Expensive Wide-Moat** (CIO-directed 2026-10-28 — 26 screened → 16 listed across 11 sectors, trigger = MOS 15% on screen FV; closest: PAYX −29.7% / RMD −29.9% / ORLY −32.3%)*\n*ก่อนหน้า (2026-10-31): **AI Selloff Watch',1)
open(p,'w',encoding='utf8').write(s)
print('inserted')
