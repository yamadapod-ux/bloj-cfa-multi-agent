import json, urllib.request, sys
UA={'User-Agent':'CFA-scout research research@example.com'}
CIK={'TTD':1671933,'PINS':1506293,'SNAP':1564408,'CRTO':1576427}
for t in sys.argv[1:]:
    d=json.loads(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[t]:010d}.json",headers=UA),timeout=60).read())
    g=d['facts']['us-gaap']; print('==',t)
    for tg in ['WeightedAverageNumberOfDilutedSharesOutstanding','CommonStockSharesOutstanding']:
        if tg in g:
            u=g[tg]['units']['shares']; dd={}
            for x in u: dd[(x.get('start'),x['end'])]=x['val']
            print(tg,[(s,e,round(v/1e6,1)) for (s,e),v in sorted(dd.items(),key=lambda k:k[0][1])][-8:])
    for tg in ['StockholdersEquity','Goodwill','OperatingLeaseLiability','RestructuringCharges']:
        if tg in g:
            u=g[tg]['units']['USD']; dd={}
            for x in u: dd[(x.get('start'),x['end'])]=x['val']
            print(tg,[(s,e,round(v/1e6,1)) for (s,e),v in sorted(dd.items(),key=lambda k:k[0][1]) if e[5:7]=='12' or e>='2026'][-9:])
    print('dei keys', list(d['facts'].get('dei',{}).keys()))
    for k,v in d['facts'].get('dei',{}).items():
        if 'Shares' in k:
            for unit,arr in v['units'].items(): print(k,[(x['end'],x['val']) for x in arr][-4:])
