from sec import *
import sys,re
t=sys.argv[1]; pat=sys.argv[2]; since=sys.argv[3] if len(sys.argv)>3 else '2024-06-30'
f=facts(t)
for tax,g in f['facts'].items():
  for k,n in g.items():
    if not re.search(pat,k): continue
    for un,arr in n['units'].items():
      rows=sorted({(x.get('start'),x['end'],x['val'],x['form'],x['filed']) for x in arr if x['end']>=since and x['form'] in ('20-F','6-K','20-F/A')},key=lambda r:(r[1],r[0] or ''))
      for r in rows[-8:]: print(f"{tax}:{k} [{un}] {r}")
