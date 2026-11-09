# list us-gaap tags matching a regex with latest 10-K/10-Q annual values (for filling gaps in sec.py)
import json, sys, re
from datetime import date
t=sys.argv[1]; pat=re.compile(sys.argv[2]); f=json.load(open(f'data/cf_{t}.json'))
for tag,v in f['facts']['us-gaap'].items():
    if not pat.search(tag): continue
    us=[x for x in list(v['units'].values())[0] if x.get('form') in ('10-K','10-Q')]
    if not us or max(x['end'] for x in us)<'2025-06-30': continue
    ann={x['end'][:4]:x['val'] for x in us if 'start' in x and 350<(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<380}
    ytd=[x for x in us if 'start' in x and 250<(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<290]
    inst=[x for x in us if 'start' not in x]
    s=' '.join(f"{y}:{a/1e6:,.0f}" for y,a in sorted(ann.items())[-6:])
    if ytd: l=max(ytd,key=lambda x:x['end']); p=[x for x in ytd if x['end']==f"{int(l['end'][:4])-1}{l['end'][4:]}"]; s+=f" | 9M{l['end'][:4]} {l['val']/1e6:,.0f} 9M{int(l['end'][:4])-1} {p[-1]['val']/1e6 if p else float('nan'):,.0f}"
    if inst: l=max(inst,key=lambda x:x['end']); s+=f" | bal {l['val']/1e6:,.0f}@{l['end']}"
    print(f"{tag}: {s}")
