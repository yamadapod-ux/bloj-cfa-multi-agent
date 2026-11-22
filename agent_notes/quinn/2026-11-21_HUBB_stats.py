import json, math, statistics as st, datetime
def load(f):
    d=json.load(open(f))['chart']['result'][0]
    ts=d['timestamp']; c=d['indicators']['adjclose'][0]['adjclose'] if 'adjclose' in d['indicators'] else d['indicators']['quote'][0]['close']
    return {datetime.date.fromtimestamp(t):x for t,x in zip(ts,c) if x}
h=load('HUBB.json'); m=load('%5EGSPC.json')
dates=sorted(set(h)&set(m)); print(len(dates),dates[0],dates[-1], h[dates[-1]], m[dates[-1]])
rh=[h[dates[i]]/h[dates[i-1]]-1 for i in range(1,len(dates))]
rm=[m[dates[i]]/m[dates[i-1]]-1 for i in range(1,len(dates))]
rf=0.0492
def stats(rh,rm,label):
    n=len(rh); ex=[r-rf/252 for r in rh]
    mu=st.mean(rh)*252; sd=st.stdev(rh)*math.sqrt(252)
    sharpe=st.mean(ex)/st.stdev(ex)*math.sqrt(252)
    dd=math.sqrt(sum(min(0,r-rf/252)**2 for r in rh)/n)*math.sqrt(252)
    sortino=(st.mean(rh)*252-rf)/dd
    cov=sum((a-st.mean(rh))*(b-st.mean(rm)) for a,b in zip(rh,rm))/(n-1)
    beta=cov/st.variance(rm); corr=cov/(st.stdev(rh)*st.stdev(rm))
    alpha=(st.mean(rh)-rf/252-beta*(st.mean(rm)-rf/252))*252
    s=sorted(rh); var95=s[int(0.05*n)]; cvar=st.mean(s[:int(0.05*n)])
    mu_p=st.mean(rh); var_p=mu_p-1.645*st.stdev(rh)
    # max dd
    return dict(label=label,n=n,ann_ret=mu,ann_vol=sd,sharpe=sharpe,sortino=sortino,beta=beta,corr=corr,alpha=alpha,VaR95_hist=var95,CVaR95=cvar,VaR95_param=var_p)
print(stats(rh,rm,'3Y daily'))
print(stats(rh[-252:],rm[-252:],'1Y daily'))
# maxDD
def mdd(p):
    pk=0;mx=0
    for x in p:
        pk=max(pk,x); mx=min(mx,x/pk-1)
    return mx
print('MDD 3Y HUBB',mdd([h[d] for d in dates]),'SPX',mdd([m[d] for d in dates]))
# total return
print('3Y cum HUBB',h[dates[-1]]/h[dates[0]]-1,'SPX',m[dates[-1]]/m[dates[0]]-1)
# recent
for k in (5,20):
    print(k,'d HUBB',h[dates[-1]]/h[dates[-1-k]]-1,'SPX',m[dates[-1]]/m[dates[-1-k]]-1)
# monthly beta
def lm(f):
    d=json.load(open(f))['chart']['result'][0]; return [x for x in d['indicators']['quote'][0]['close'] if x]
a=lm('HUBBm.json'); b=lm('GSPCm.json'); n=min(len(a),len(b)); a=a[-n:]; b=b[-n:]
ra=[a[i]/a[i-1]-1 for i in range(1,n)]; rb=[b[i]/b[i-1]-1 for i in range(1,n)]
cov=sum((x-st.mean(ra))*(y-st.mean(rb)) for x,y in zip(ra,rb))/(len(ra)-1)
print('monthly beta',cov/st.variance(rb),len(ra))
# current vol 30d
print('30d vol ann',st.stdev(rh[-30:])*math.sqrt(252),'60d',st.stdev(rh[-60:])*math.sqrt(252))
