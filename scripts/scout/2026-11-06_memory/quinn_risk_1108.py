# Quinn MU risk stats 2026-11-08. Sources: Yahoo chart API (adjclose) daily 2000-01-03..2026-11-06; monthly 5Y files y_*_5y.json
import json,math,os,statistics as st,datetime as dt
B=os.path.dirname(os.path.abspath(__file__))
def load(p):
    r=json.load(open(p))['chart']['result'][0]; ts=r['timestamp']; a=r['indicators']['adjclose'][0]['adjclose']
    return [(dt.datetime.utcfromtimestamp(t).date(),x) for t,x in zip(ts,a) if x]
mu=load(f'{B}/data/q1108/d_MU.json'); sp=load(f'{B}/data/q1108/d_GSPC.json')
# cut at 2026-11-05 close (price base)
mu=[x for x in mu if x[0]<=dt.date(2026,11,5)]; sp=[x for x in sp if x[0]<=dt.date(2026,11,5)]
print('last',mu[-1],sp[-1])
# --- 5Y monthly beta (month-end from daily) ---
def monthly(s):
    m={}
    for d,p in s: m[(d.year,d.month)]=p
    return m
mm=monthly(mu); sm=monthly(sp); ks=sorted(set(mm)&set(sm))
def rets(m,ks): return [m[ks[i]]/m[ks[i-1]]-1 for i in range(1,len(ks))]
for yrs,lab in [(5,'5Y'),(3,'3Y'),(10,'10Y')]:
    k=ks[-(12*yrs+1):]; a=rets(mm,k); b=rets(sm,k)
    cov=st.covariance(a,b); beta=cov/st.variance(b); corr=st.correlation(a,b)
    print(lab,'monthly n',len(a),'beta %.3f corr %.3f R2 %.3f ann vol MU %.1f%% SPX %.1f%%'%(beta,corr,corr**2,st.stdev(a)*math.sqrt(12)*100,st.stdev(b)*math.sqrt(12)*100))
# --- daily vol ---
dm={d:p for d,p in mu}; ds={d:p for d,p in sp}; dk=sorted(set(dm)&set(ds))
dr=[math.log(dm[dk[i]]/dm[dk[i-1]]) for i in range(1,len(dk))]
for n,lab in [(252,'1Y'),(756,'3Y'),(1260,'5Y'),(len(dr),'since2000')]:
    print('daily vol',lab,'%.1f%%'%(st.stdev(dr[-n:])*math.sqrt(252)*100))
# --- drawdowns ---
def dd(s,start=None,end=None):
    pk=None;pkd=None;worst=0;w=None
    for d,p in s:
        if start and d<start: continue
        if end and d>end: break
        if pk is None or p>pk: pk=p;pkd=d
        x=p/pk-1
        if x<worst: worst=x;w=(pkd,d,pk,p)
    return worst,w
print('MaxDD since 2000',dd(mu)); print('MaxDD 5Y',dd(mu,dt.date(2021,11,5)))
for lab,a,b in [('2000-02 dotcom',dt.date(2000,1,1),dt.date(2003,6,30)),('2007-08 cycle+GFC',dt.date(2006,1,1),dt.date(2009,6,30)),('2011-12 DRAM bust',dt.date(2010,1,1),dt.date(2012,12,31)),('2014-16 cycle',dt.date(2014,1,1),dt.date(2016,6,30)),('2018-19 cycle',dt.date(2018,1,1),dt.date(2019,6,30)),('2021-22 cycle',dt.date(2021,1,1),dt.date(2022,12,31)),('2024 HBM pullback',dt.date(2024,6,1),dt.date(2024,12,31)),('2026 current',dt.date(2026,6,1),dt.date(2026,11,5))]:
    w,x=dd(mu,a,b); ws,xs=dd(sp,a,b); print('%-20s MU %.1f%% %s | SPX %.1f%%'%(lab,w*100,(x[0],x[1],round(x[2],2),round(x[3],2)) if x else '',ws*100))
# --- 1Y VaR / CVaR ---
# Parametric (lognormal) on 5Y monthly mean/vol; historical on overlapping 252d returns since 2000
k=ks[-61:]; a=[math.log(1+x) for x in rets(mm,k)]
mu_a=st.mean(a)*12; sd_a=st.stdev(a)*math.sqrt(12)
for z,lab in [(1.645,'95'),(2.326,'99')]:
    print('Param 1Y VaR%s (5Y monthly lognormal, hist drift %.1f%%): %.1f%% ; zero-drift: %.1f%%'%(lab,mu_a*100,(math.exp(mu_a-z*sd_a)-1)*100,(math.exp(-z*sd_a)-1)*100))
pr=[p for d,p in mu]; yr=sorted(pr[i]/pr[i-252]-1 for i in range(252,len(pr)))
i5=int(.05*len(yr)); i1=int(.01*len(yr))
print('Hist 1Y (overlapping since 2000, n=%d): VaR95 %.1f%% CVaR95 %.1f%% VaR99 %.1f%% CVaR99 %.1f%% P(1Y ret<0) %.1f%%'%(len(yr),yr[i5]*100,st.mean(yr[:i5])*100,yr[i1]*100,st.mean(yr[:i1])*100,100*sum(1 for x in yr if x<0)/len(yr)))
print('Hist 1-day VaR95 5Y %.2f%%'%(sorted(dr[-1260:])[63]*100))
# --- peers corr (monthly 5Y files) ---
def ym(t):
    r=json.load(open(f'{B}/data/y_{t}_5y.json'))['chart']['result'][0]
    o={}
    for ts,p in zip(r['timestamp'],r['indicators']['adjclose'][0]['adjclose']):
        if p: d=dt.datetime.utcfromtimestamp(ts).date(); o[(d.year,d.month)]=p
    return o
P={t:ym(t) for t in ['MU','WDC','STX','SNDK','SKHY','GSPC']}
for t in ['WDC','STX','SNDK','SKHY','GSPC']:
    kk=sorted(set(P['MU'])&set(P[t]))
    if len(kk)<6: print(t,'n',len(kk),'insufficient'); continue
    a=rets(P['MU'],kk); b=rets(P[t],kk); print('corr MU-%s monthly n=%d: %.2f'%(t,len(a),st.correlation(a,b)))
