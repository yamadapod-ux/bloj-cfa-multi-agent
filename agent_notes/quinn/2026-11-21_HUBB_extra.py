import json,math,statistics as st,datetime
exec(open('model.py').read().split("res={}")[0])
# implied TGR
lo,hi=0.0,0.0863
for _ in range(80):
    mid=(lo+hi)/2
    if run(SC['Base'],WACC0,0,None,mid)['fv']>P0: hi=mid
    else: lo=mid
print('implied TGR',mid)
# incremental ROIC base
r=run(SC['Base'],full=True); rev=r['rev']; 
reinv=sum(rev[i]*(0.03-(0.023+0.0004*i))+0.15*(rev[i]-(rev[i-1] if i else 6920)) for i in range(1,10))
print('inc NOPAT 2027->36',r['nopat'][-1]-r['nopat'][0],'reinv 28-36',reinv,'incROIC',(r['nopat'][-1]-r['nopat'][0])/reinv)
# FV5 and ER
res={k:run(s,full=True) for k,s in SC.items()}
pw5=sum(SC[k]['p']*res[k]['fv5'] for k in SC); print('pw5',pw5)
for k in res: print(k,'ER5.11',(res[k]['fv5']/P0)**(1/5.11)-1)
print('PW ER 5.11',(pw5/P0)**(1/5.11)-1,'5.0',(pw5/P0)**(1/5)-1)
# consistency w/ dividends for each
for k in res:
    eq0=res[k]['fv']*SH; ke=0.0995
    fvdiv=sum(SH*6.08*(1.07**i)*(1+ke)**(5.11-0.6-i) for i in range(5))
    print(k,'eq5/(eq0*(1+ke)^5.11 - FVdiv)', res[k]['eq5']/(eq0*(1+ke)**5.11-fvdiv))
# regression stats
def load(f):
    d=json.load(open(f))['chart']['result'][0]
    ts=d['timestamp']; c=d['indicators']['adjclose'][0]['adjclose']
    return {datetime.date.fromtimestamp(t):x for t,x in zip(ts,c) if x}
h=load('HUBB.json'); m=load('%5EGSPC.json'); ds=sorted(set(h)&set(m))
y=[h[ds[i]]/h[ds[i-1]]-1 for i in range(1,len(ds))]; x=[m[ds[i]]/m[ds[i-1]]-1 for i in range(1,len(ds))]
n=len(y); mx=st.mean(x); my=st.mean(y)
b=sum((a-mx)*(c-my) for a,c in zip(x,y))/sum((a-mx)**2 for a in x); a0=my-b*mx
res_=[c-(a0+b*a) for a,c in zip(x,y)]; s2=sum(e*e for e in res_)/(n-2)
seb=math.sqrt(s2/sum((a-mx)**2 for a in x)); sea=math.sqrt(s2*(1/n+mx**2/sum((a-mx)**2 for a in x)))
r2=1-sum(e*e for e in res_)/sum((c-my)**2 for c in y)
print('beta',b,'se',seb,'t',b/seb,'alpha_daily',a0,'t',a0/sea,'R2',r2)
rf=0.0492/252
exm=[a-rf for a in x]; print('SPX sharpe',st.mean(exm)/st.stdev(exm)*math.sqrt(252),'ann ret',mx*252,'vol',st.stdev(x)*math.sqrt(252))
# Blume beta
print('blume daily',0.67*b+0.33)
# downside capture on S&P down days
dn=[(a,c) for a,c in zip(x,y) if a<0]; print('down capture',st.mean([c for a,c in dn])/st.mean([a for a,c in dn]))
# worst 5 daily for HUBB last 20d
print([round(v,4) for v in y[-8:]])
