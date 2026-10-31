# KNSL (insurer: residual income on book) + RACE (IFRS 20-F, EUR) screen-level FV
from screen import sa, nasdaq, beta, Rf, ERP, TGR, path
from hist import *
import json
out={}
# ---- KNSL residual income: ROE fades TTM -> 15% over 10y, BV grows at ROE*retention capped by consensus premium growth path
f=facts('KNSL'); y=ych('KNSL','1y','1d'); p=y['meta']['regularMarketPrice']; np_,nd_,rng=nasdaq('KNSL'); s=sa('KNSL')
ni=ttm_at(f,['NetIncomeLoss']); eqs=sorted([x for x in series(f,['StockholdersEquity']) if not x.get('start')],key=lambda x:x['end'])
bv=eqs[-1]['val']; bv1y=[x for x in eqs if x['end']<=str(D(eqs[-1]['end'])-dt.timedelta(360))][-1]['val']
roe=ni/((bv+bv1y)/2); sh=shares_cover(f)[0]
fyni={x['end']:x['val'] for x in series(f,['NetIncomeLoss']) if x.get('start') and 350<=dur(x)<=380}
fyeq={x['end']:x['val'] for x in eqs}
roeh=[]
for e in sorted(fyni)[-5:]:
    pe=[k for k in fyeq if k<=str(D(e)-dt.timedelta(360))]
    if e in fyeq and pe: roeh.append((e,fyni[e]/((fyeq[e]+fyeq[max(pe)])/2)))
b=beta('KNSL'); bb=0.67*b+0.33; ke=Rf+bb*ERP
def ri(roe_t=0.15,k=ke,kmult=1.0):
    B=bv; pv=0; g=[kmult*x for x in path(s['g'])]
    for i in range(10):
        r=roe+(roe_t-roe)*i/9; pv+=(r-k)*B/(1+k)**(i+1); B*=1+min(g[i],r*0.95)
    tv=(roe_t-k)*B/(k-TGR); pv+=tv/(1+k)**10
    return (bv+pv)/sh, (tv/(1+k)**10)/(bv+pv)
fv,tvs=ri()
lo,hi=-1,6
for _ in range(80):
    m=(lo+hi)/2
    if ri(kmult=m)[0]<p: lo=m
    else: hi=m
out['KNSL']=dict(price=p,np=np_,ndate=nd_,rng52=rng,bv=bv,bvps=bv/sh,roe=roe,roeh=roeh,ni=ni,sh=sh,beta=b,bb=bb,ke=ke,cg=s['g'],pt=s['pt'],fv=fv,tvshare=tvs,
    fv_wm=ri(k=ke-0.01)[0],fv_wp=ri(k=ke+0.01)[0],fv_r30=ri(roe_t=0.20)[0],k=m,pb=p/(bv/sh),end=eqs[-1]['end'])
print('KNSL',{k:(round(v,3) if isinstance(v,float) else v) for k,v in out['KNSL'].items()})
# ---- RACE: FY2025 IFRS (EUR) -> USD at spot EURUSD, NOPAT DCF same as screen.py
fx=ych('EURUSD=X','5d','1d')['meta']['regularMarketPrice']
f=facts('RACE'); I=f['facts']['ifrs-full']
def fy(c,yr='2025-12-31'):
    return [x['val'] for un in I[c]['units'].values() for x in un if x['end']==yr and x.get('form')=='20-F' and (not x.get('start') or (D(x['end'])-D(x['start'])).days>350)][-1]
rev=fy('Revenue'); oi=fy('ProfitLossFromOperatingActivities'); tax=fy('IncomeTaxExpenseContinuingOperations')/fy('ProfitLossBeforeTax')
eq=fy('Equity'); debt_=fy('Borrowings'); cash=fy('CashAndCashEquivalents'); ic=eq+debt_-cash; roic=oi*(1-tax)/ic
rh=[]
for yr in ['2021-12-31','2022-12-31','2023-12-31','2024-12-31','2025-12-31']:
    t_=fy('IncomeTaxExpenseContinuingOperations',yr)/fy('ProfitLossBeforeTax',yr); rh.append((yr,fy('ProfitLossFromOperatingActivities',yr)*(1-t_)/(fy('Equity',yr)+fy('Borrowings',yr)-fy('CashAndCashEquivalents',yr))))
cfo=fy('CashFlowsFromUsedInOperatingActivities'); cx=fy('PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities')+fy('PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities')
sh=fy('AdjustedWeightedAverageShares'); y=ych('RACE','1y','1d'); p=y['meta']['regularMarketPrice']; np_,nd_,rng=nasdaq('RACE'); s=sa('RACE')
b=beta('RACE'); bb=0.67*b+0.33; E_=p*sh; Dusd=debt_*fx; ke=Rf+bb*ERP; kd=(Rf+0.008)*0.76; W=(E_*ke+Dusd*kd)/(E_+Dusd)
o=dict(rev=rev*fx,m=oi/rev,tax=tax,roic=roic,cg=s['g'],nd=(debt_-cash)*fx,sh=sh,price=p,wacc=W)
from screen import dcf, solvek
o['fv'],o['tvshare']=dcf(o); o.update(fv_wm=dcf(o,W=W-0.01)[0],fv_wp=dcf(o,W=W+0.01)[0],fv_r30=dcf(o,ront=0.30)[0],k=solvek(o),np=np_,ndate=nd_,rng52=rng,beta=b,bb=bb,ke=ke,fx=fx,roic_hist=rh,pt=s['pt'],
    ownfcf=(cfo-cx)*fx,end='2025-12-31',naive=(oi*(1-tax)*fx/W-(debt_-cash)*fx)/sh,yoy=rev/fy('Revenue','2024-12-31')-1)
out['RACE']=o
print('RACE',{k:(round(v,3) if isinstance(v,float) else v) for k,v in o.items()})
json.dump(out,open('special.json','w'),default=str)
