import json, time as T, urllib.request as U
from hist import *
from sec import *
AM=['AmortizationOfIntangibleAssets','AmortizationOfAcquiredIntangibleAssets']
f=facts('EFOR'); e='2026-09-30'
am=ttm_at(f,AM,e); oi=ttm_at(f,['OperatingIncomeLoss'],e); eq=inst1(f,EQ,e); d=debt(f,e); m=mkt(f,e); gw=inst1(f,['Goodwill'],e); ia=inst1(f,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],e)
print('EFOR am',am,'oi',oi,'eq',eq,'debt',d,'cash',m,'gw',gw,'ia',ia)
if am: print(' ROIC ex-amort @21%',round(100*(oi+am)*.79/(eq+d-m),2),' on tangible IC',round(100*(oi+am)*.79/(eq+d-m-(gw or 0)-(ia or 0)),2))
for fy_e in ['2021-12-31','2022-12-31','2023-12-31','2024-12-31','2025-12-31']:
    pass
for t in ['RHI','MAN','KFRC','NSP','EFOR','UPWK','BBSI','TBI','KFY','TNET','RGP','KELYA','AMN','HQI']:
    y=ych(t,'1y','1d'); ts=y['timestamp']; c=y['indicators']['quote'][0]['close']; h=y['indicators']['quote'][0]['high']
    dd=[T.strftime('%Y-%m-%d',T.gmtime(x)) for x in ts]
    px=dict(zip(dd,c)); hi=max((v,k) for k,v in zip(dd,h) if v); lo=min((v,k) for k,v in zip(dd,y['indicators']['quote'][0]['low']) if v)
    last=[k for k in dd if px[k]][-1]
    print(t,'Oct16',round(px.get('2026-10-16') or 0,2),'Oct30',round(px.get('2026-10-30') or 0,2),last,round(px[last],2),'chg since Oct16',round(100*(px[last]/(px.get('2026-10-16') or 1)-1),1),'high',round(hi[0],2),hi[1],'low',round(lo[0],2),lo[1])
    if t in('UPWK','MAN','EFOR'):
        print('  last8',[(k[5:],round(px[k],2)) for k in dd[-8:]])
