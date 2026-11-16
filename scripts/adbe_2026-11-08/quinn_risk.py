import json,sys,math,statistics as st
from datetime import datetime,timezone
D=sys.argv[1]
def load(f):
    r=json.load(open(f"{D}/{f}"))['chart']['result'][0]
    ts=r['timestamp']; q=r['indicators']
    adj=q.get('adjclose',[{}])[0].get('adjclose') or q['quote'][0]['close']
    cl=q['quote'][0]['close']
    out=[]
    for t,a,c in zip(ts,adj,cl):
        if a is None: continue
        out.append((datetime.fromtimestamp(t,timezone.utc).date(),a,c))
    return out
A=load('ADBE.json'); S=load('%5EGSPC.json'); I=load('IRX.json')
print('ADBE last',A[-3:]); print('SPX last',S[-3:]); print('IRX last',I[-2:])
da={d:a for d,a,c in A}; ds={d:a for d,a,c in S}; di={d:c for d,a,c in I}
dates=[d for d,_,_ in A if d in ds]
def rets(dd,src):
    return [src[dd[i]]/src[dd[i-1]]-1 for i in range(1,len(dd))]
def window(days):
    end=dates[-1]; 
    from datetime import timedelta
    return [d for d in dates if (end-d).days<=days]
res={}
for lab,days in [('1Y',365),('3Y',365*3),('5Y',365*5)]:
    w=window(days); ra=rets(w,da); rs=rets(w,ds)
    rf=[di.get(d) for d in w[1:]]; rfv=[x for x in rf if x is not None]; rfann=st.mean(rfv)/100
    rfd=rfann/252
    ma,ms=st.mean(ra),st.mean(rs)
    cov=sum((x-ma)*(y-ms) for x,y in zip(ra,rs))/(len(ra)-1)
    beta=cov/st.variance(rs)
    corr=cov/(st.stdev(ra)*st.stdev(rs))
    vol=st.stdev(ra)*math.sqrt(252); vols=st.stdev(rs)*math.sqrt(252)
    yrs=(w[-1]-w[0]).days/365.25
    cagr=(da[w[-1]]/da[w[0]])**(1/yrs)-1; cagrs=(ds[w[-1]]/ds[w[0]])**(1/yrs)-1
    shA=(cagr-rfann)/vol; shS=(cagrs-rfann)/vols
    shA2=(ma-rfd)/st.stdev(ra)*math.sqrt(252); shS2=(ms-rfd)/st.stdev(rs)*math.sqrt(252)
    dn=[min(0,x-rfd) for x in ra]; dd=math.sqrt(sum(x*x for x in dn)/len(dn))*math.sqrt(252)
    sortino=(cagr-rfann)/dd
    # max drawdown
    pk=0;mdd=0
    for d in w:
        p=da[d]; pk=max(pk,p); mdd=min(mdd,p/pk-1)
    pk=0;mdds=0
    for d in w:
        p=ds[d]; pk=max(pk,p); mdds=min(mdds,p/pk-1)
    alpha=cagr-(rfann+beta*(cagrs-rfann))
    treynor=(cagr-rfann)/beta
    te=st.stdev([x-y for x,y in zip(ra,rs)])*math.sqrt(252); ir=(cagr-cagrs)/te
    print(f"{lab}: {w[0]}->{w[-1]} n={len(ra)} rf={rfann:.4f} betaD={beta:.3f} corr={corr:.3f} volA={vol:.3f} volS={vols:.3f} CAGR A={cagr:.4f} S={cagrs:.4f} SharpeA={shA:.3f} SharpeS={shS:.3f} (arith A {shA2:.3f} S {shS2:.3f}) SortinoA={sortino:.3f} MDD A={mdd:.3f} S={mdds:.3f} JensenA={alpha:.4f} Treynor={treynor:.4f} IR={ir:.3f}")
# monthly beta 5Y
import collections
def monthly(src):
    m=collections.OrderedDict()
    for d in dates:
        m[(d.year,d.month)]=src[d]
    k=list(m); return k,[m[x] for x in k]
k,ma_=monthly(da); _,ms_=monthly(ds)
k=k[-61:];ma_=ma_[-61:];ms_=ms_[-61:]
ra=[ma_[i]/ma_[i-1]-1 for i in range(1,len(ma_))]; rs=[ms_[i]/ms_[i-1]-1 for i in range(1,len(ms_))]
mA,mS=st.mean(ra),st.mean(rs)
b=sum((x-mA)*(y-mS) for x,y in zip(ra,rs))/(len(ra)-1)/st.variance(rs)
print('5Y monthly beta',round(b,3),'n',len(ra), k[0],k[-1])
# full history drawdown and current dd
pk=0;mdd=0;pkd=None
for d,a,c in A:
    if c>pk: pk=c;pkd=d
    mdd=min(mdd,c/pk-1)
print('10Y close MDD',round(mdd,3),'peak',pk,pkd,'current dd from 10Y peak',A[-1][2]/pk-1)
# stop-loss hit prob (GBM, barrier) 6 months
P=239.30;K=185.0
for lab,days in [('1Y',365),('3Y',365*3)]:
    w=window(days); ra=rets(w,da); sig=st.stdev([math.log(1+x) for x in ra])*math.sqrt(252)
    T=0.5
    for mu in [0.0, 0.05]:
        nu=mu-0.5*sig*sig; b_=math.log(K/P)
        from math import erf,sqrt,exp
        N=lambda x:0.5*(1+erf(x/sqrt(2)))
        p_end=N((b_-nu*T)/(sig*sqrt(T)))
        p_touch=N((b_-nu*T)/(sig*sqrt(T)))+exp(2*nu*b_/sig**2)*N((b_+nu*T)/(sig*sqrt(T)))
        print(f"stop {lab} sigma={sig:.3f} mu={mu}: P(end<185)={p_end:.3f} P(touch within 6m)={p_touch:.3f} dist={K/P-1:.3f}")
# VaR 1-day 95% param & hist (1Y)
w=window(365); ra=rets(w,da); m=st.mean(ra); s=st.stdev(ra)
srt=sorted(ra); h=srt[int(0.05*len(srt))]; cv=st.mean(srt[:int(0.05*len(srt))])
print(f"VaR95 1d param={m-1.645*s:.4f} hist={h:.4f} CVaR hist={cv:.4f}")
