import json,sys
d=json.load(open(sys.argv[1],encoding='utf-8'))
g=d['facts']['us-gaap']
def inst(tag):
    out={}
    for u in g[tag]['units'].values():
        for x in u:
            if x.get('form') in ('10-Q','10-K'):
                out[x['end']]=x['val']
    return dict(sorted(out.items()))
def dur(tag,days=(80,100)):
    out={}
    if tag not in g: return out
    for u in g[tag]['units'].values():
        for x in u:
            if 'start' not in x: continue
            from datetime import date
            s=date.fromisoformat(x['start']);e=date.fromisoformat(x['end'])
            n=(e-s).days
            if days[0]<=n<=days[1]: out[x['end']]=x['val']
    return dict(sorted(out.items()))
for t in ['RevenueRemainingPerformanceObligation','ContractWithCustomerLiabilityCurrent']:
    print(t, inst(t))
for t in ['RevenueRemainingPerformanceObligationPercentage']:
    print(t, inst(t) if t in g else 'MISSING')
print('RevQ',dur('Revenues'))
print('RevA',dur('Revenues',(350,380)))
print('OpIncQ',dur('OperatingIncomeLoss'))
print('SharesDilQ',dur('WeightedAverageNumberOfDilutedSharesOutstanding'))
