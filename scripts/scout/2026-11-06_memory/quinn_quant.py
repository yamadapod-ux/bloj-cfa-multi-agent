# Quinn MU re-analysis 2026-11-06. Inputs: agent_notes/charlie/2026-11-06_MU_verified_inputs.md + Atlas Re-Analysis Update.
# Run: python -I quinn_quant.py [--mask]   (--mask hides FV, used to calibrate margin paths before seeing valuation)
import json,math,os,statistics as st,sys,datetime as dt
BASE=os.path.dirname(os.path.abspath(__file__)); MASK='--mask' in sys.argv
PX=656.39; SH=1150.; BR=55601.; WACC=.125; TAX=.155; G=.025
MEV=PX*SH-BR
# FY26 anchors ($M) [Inputs]
REV0=133188.; COGS0=25684.; OI0=99340.; DA0=9503.; PPE0=63310.; PPE_1=46590.
CASH0=REV0-OI0-DA0                      # cash cost = revenue - EBIT - D&A
DAR=DA0/((PPE0+PPE_1)/2)                # D&A / avg PP&E
NWC=(89675-84969-9503-1333)/-(133188-37378)   # net WC build per $ revenue growth FY26
ASP_FY25=1/2.9                           # FY26 ASP +~180-200% YoY: FY25 ASP ~ 1/2.9 of FY26 (rev-weighted DRAM 2.8x, NAND 3.0x)
YRS=list(range(2027,2037))
SC={
'Bull':dict(p=.20,bits=[18,20,22,20,18,16,15,14,13,12],asp=[85,0,-22,-28,-15,-5,-12,-8,-5,-5],cost=[3]+[-4]*9,capex=[58000,80000,85000],cx=.30,ronic=.25),
'Base':dict(p=.45,bits=[18,20,20,18,15,15,15,14,13,12],asp=[72,-5,-40,-35,-22,-5,-15,-15,-4,-4],cost=[3]+[-4]*9,capex=[55000,70000,55000],cx=.35,ronic=.15),
'Bear':dict(p=.35,bits=[18,18,15,10,10,12,12,12,12,12],asp=[56,-40,-50,-35,8,12,-12,-15,-4,-4],cost=[5,0,0,0]+[-4]*6,capex=[52000,50000,25000],cx=.35,ronic=.10),
}
def path(s,dasp=None):
    r=[];rev=REV0;cash=CASH0;ppe=PPE0;lvl=1.;bitl=1.
    for i,y in enumerate(YRS):
        b=s['bits'][i]/100;a=s['asp'][i]/100;c=s['cost'][i]/100
        prev=rev;rev=rev*(1+b)*(1+a);cash=cash*(1+b)*(1+c);lvl*=1+a;bitl*=1+b
        cx=s['capex'][i] if i<len(s['capex']) else s['cx']*rev
        da=DAR*(ppe+cx/2)/(1+DAR/2)            # D&A on average PP&E, solved for closing balance
        ppe0=ppe;ppe=ppe+cx-da
        ebit=rev-cash-da
        tax=max(0,ebit)*TAX;nopat=ebit-tax
        dn=max(0,rev-prev)*NWC                 # no release when revenue falls (FY23: AR -2.8B, inventory +3.6B net ~0)
        r.append(dict(y=y,rev=rev,g=rev/prev-1,asp=lvl,asp25=lvl/ASP_FY25,bits=bitl,cash=cash,da=da,ebit=ebit,m=ebit/rev,nopat=nopat,cx=cx,cxr=cx/rev,dn=dn,ppe=ppe,fcff=nopat-(cx-da)-dn,roic=nopat/((ppe0+ppe)/2+.1*rev)))
    return r
def value(r,wacc=WACC,g=G,ronic=.15,midyear=False):
    mid=st.mean(x['m'] for x in r[4:])         # terminal margin = average FY31-36 (one full cycle, not peak or trough)
    n=r[-1]['rev']*(1+g)*mid*(1-TAX);tf=n*(1-g/ronic);tv=tf/(wacc-g)
    adj=.5 if midyear else 0
    pv=[x['fcff']/(1+wacc)**(i+1-adj) for i,x in enumerate(r)]
    pvtv=tv/(1+wacc)**(10-adj)
    ev=sum(pv)+pvtv
    return dict(ev=ev,fv=ev/SH+BR/SH,pv=pv,pvtv=pvtv,tv=tv,mid=mid,tn=n,tf=tf)
if __name__=='__main__':
    print('DAR %.4f NWC %.4f CASH0 %.0f MEV %.0f'%(DAR,NWC,CASH0,MEV))
    for k,s in SC.items():
        r=path(s);print('\n',k)
        for x in r: print(x['y'],'rev %6.0f g %5.1f%% aspxFY25 %.2f bits %.2f ebit %6.0f m %5.1f%% cx %5.0f cx/rev %3.0f%% da %5.0f ppe %6.0f fcff %6.0f roic %5.1f%%'%(x['rev']/1e3,x['g']*100,x['asp25'],x['bits'],x['ebit']/1e3,x['m']*100,x['cx']/1e3,x['cxr']*100,x['da']/1e3,x['ppe']/1e3,x['fcff']/1e3,x['roic']*100))
        m=[x['m'] for x in r[4:]];print(' FY31-36 avg margin %.1f%% rev-weighted FY29-36 %.1f%%; FY27 EPS approx %.1f'%(st.mean(m)*100,sum(x['ebit'] for x in r[2:])/sum(x['rev'] for x in r[2:])*100,r[0]['nopat']/SH))
        if not MASK:
            v=value(r,ronic=s['ronic']);print(' FV %.2f'%v['fv'],v['pvtv']/v['ev'])
