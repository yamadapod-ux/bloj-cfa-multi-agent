# usage: python -I quinn_rpo_test.py <cf_ADBE.json>   (SEC XBRL companyfacts CIK 796343)
import json,sys,math,statistics as st
from datetime import date
d=json.load(open(sys.argv[1],encoding='utf-8'))['facts']['us-gaap']
def inst(tag):
    o={}
    for u in d[tag]['units'].values():
        for x in u:
            if x.get('form') in('10-Q','10-K'): o[x['end']]=x['val']
    return dict(sorted(o.items()))
def dur(tag,lo,hi):
    o={}
    for u in d[tag]['units'].values():
        for x in u:
            if 'start' in x and lo<=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<=hi: o[x['end']]=x['val']
    return o
rpo=inst('RevenueRemainingPerformanceObligation'); pc=inst('RevenueRemainingPerformanceObligationPercentage')
dr=inst('ContractWithCustomerLiabilityCurrent')
qa=dur('Revenues',80,100); an=dur('Revenues',350,380); q=dict(qa)
for e in an:
    ed=date.fromisoformat(e); pr=[k for k in qa if 0<(ed-date.fromisoformat(k)).days<300]
    if len(pr)==3: q[e]=an[e]-sum(qa[k] for k in pr)
def yoy(series):
    ks=sorted(series); out={}
    for k in ks:
        kd=date.fromisoformat(k)
        c=[j for j in ks if 350<=(kd-date.fromisoformat(j)).days<=380]
        if c: out[k]=series[k]/series[c[0]]-1
    return out
crpo={k:rpo[k]*pc[k] for k in rpo if k in pc}
Y={'RPO':yoy(rpo),'cRPO':yoy(crpo),'DefRevCur':yoy(dr),'Revenue':yoy(q)}
ks=sorted(Y['RPO'])
print("Quarter     RPO_yoy cRPO_yoy DefRev_yoy Rev_yoy  RPO-Rev gap")
for k in ks:
    r=Y['Revenue'].get(k); dv=Y['DefRevCur'].get(k)
    print(f"{k} {Y['RPO'][k]:7.1%} {Y['cRPO'][k]:8.1%} {('%8.1f%%'%(dv*100)) if dv is not None else '     n/a'} {('%7.1f%%'%(r*100)) if r is not None else '    n/a'} {('%7.1f'%((Y['RPO'][k]-r)*100)) if r is not None else ''}")
def tstats(name,s):
    ks=sorted(s); v=[s[k] for k in ks]
    last8=v[-8:]; x=list(range(8))
    mx,my=st.mean(x),st.mean(last8)
    b=sum((a-mx)*(c-my) for a,c in zip(x,last8))/sum((a-mx)**2 for a in x)
    res=[c-(my+b*(a-mx)) for a,c in zip(x,last8)]
    se=math.sqrt(sum(e*e for e in res)/6/sum((a-mx)**2 for a in x)); t=b/se
    hist=v[:-1]; z=(v[-1]-st.mean(hist))/st.stdev(hist)
    a4=v[-4:]; p8=v[-12:-4]
    sp=math.sqrt(st.variance(a4)/4+st.variance(p8)/8); tw=(st.mean(a4)-st.mean(p8))/sp
    # Welch df
    df=(st.variance(a4)/4+st.variance(p8)/8)**2/((st.variance(a4)/4)**2/3+(st.variance(p8)/8)**2/7)
    print(f"{name}: latest {v[-1]:.2%} | hist mean {st.mean(hist):.2%} sd {st.stdev(hist):.2%} n={len(hist)} z={z:.2f} | 8Q slope {b*100:.2f}pp/qtr t={t:.2f} (df=6) | last4 mean {st.mean(a4):.2%} vs prior8 {st.mean(p8):.2%} Welch t={tw:.2f} df={df:.1f}")
for n in ('RPO','cRPO','DefRevCur','Revenue'): tstats(n,Y[n])
# gap test: RPO yoy - revenue yoy, last 4 vs prior 8
g={k:Y['RPO'][k]-Y['Revenue'][k] for k in Y['RPO'] if k in Y['Revenue']}
tstats('RPO-Rev gap',g)
