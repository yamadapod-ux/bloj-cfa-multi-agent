# Emma MYRG mid-cycle DCF (VS2) - 2026-11-21. Inputs: Atlas Data Package 2026-11-21 (locked WACC 9.81%).
import copy
BASE=dict(wacc=0.0981, tgr=0.03, mid_margin=0.045, norm_years=5, ronic=0.15, tax=0.26,
          nwc=0.06, rev_g=[0.0,0.155,0.09,0.07,0.05,0.05,0.045,0.04,0.04,0.035], # idx0 = 2026 (consensus rev fixed)
          rev26=4540.0, rev25=3657.889, m26=0.063, capex_term=0.026, da_term=0.022,
          netdebt=255.10, nonop=3.258, shares=15.721, cost_eq=0.1016, rf_shift=0.0, ni_dil=0.0)
def run(p, detail=False):
    rev=[p['rev26']]; 
    for g in p['rev_g'][1:]: rev.append(rev[-1]*(1+g))   # 2026..2035
    n=len(rev)
    # margin path 2026 m26 -> mid over norm_years starting 2027
    m=[p['m26']]
    for i in range(1,n):
        k=min(i/p['norm_years'],1.0); m.append(p['m26']+(p['mid_margin']-p['m26'])*k)
    capex=[0.030,0.033]+[0.033+(p['capex_term']-0.033)*min((i-1)/4,1) for i in range(2,n)]
    da=[0.0181+(p['da_term']-0.0181)*min(i/5,1) for i in range(n)]
    fc=[];prev=p['rev25']
    for i in range(n):
        ebit=rev[i]*m[i]; nopat=ebit*(1-p['tax'])
        f=nopat+rev[i]*(da[i]-capex[i])-p['nwc']*(rev[i]-prev); prev=rev[i]; fc.append(f)
    w=p['wacc']; ev=0; pv=[]
    # stub Q4'26 (0.25 of FY26), t=0.125 ; 2027 mid t=0.25+0.5 ...
    pv_stub=0.25*fc[0]/(1+w)**0.125; ev+=pv_stub
    for i in range(1,n):
        t=0.25+(i-1)+0.5; v=fc[i]/(1+w)**t; pv.append(v); ev+=v
    # terminal at end of 2035 (t=0.25+9)
    g=p['tgr']; nopat_T=rev[-1]*(1+g)*p['mid_margin']*(1-p['tax'])
    fcff_T=nopat_T*(1-g/p['ronic']); tv=fcff_T/(w-g); pv_tv=tv/(1+w)**(0.25+9)
    ev+=pv_tv
    eq9=ev+p['nonop']-p['netdebt']
    eq=eq9*(1+p['cost_eq'])**(52/365)
    ps=eq/p['shares']
    out=dict(ev=ev,tvpct=pv_tv/ev,ps=ps,fc=fc,rev=rev,m=m,tv=tv,fcff_T=fcff_T)
    if detail:
        # FV5 at 2031-12-31: value at end of 2031 of FCFF 2032..2035 + TV, net debt roll-forward
        t0=0.25+5-1+1  # end of 2031 relative to 9/30/26 = 0.25+5
        ev5=0
        for i in range(6,n): ev5+=fc[i]/(1+w)**((i-5)-0.5)
        ev5+=tv/(1+w)**(4)
        nd=p['netdebt']-0  # roll forward: FCFF after-tax interest
        nd=p['netdebt']
        for i in range(0,6):
            f=fc[i]*(0.25 if i==0 else 1)
            r=0.0497 if nd>0 else 0.036
            nd=nd-f+nd*r*(1 if i>0 else 0.25)
        eq5=ev5+p['nonop']-nd
        sh5=p['shares']*(1+p['ni_dil'])**5
        out.update(ev5=ev5,nd5=nd,eq5=eq5,fv5=eq5/sh5,
                   chk=eq5/( eq9*(1+p['cost_eq'])**(5.25) ))
    return out
def S(**k):
    p=copy.deepcopy(BASE); p.update(k); return run(p)['ps']
if __name__=='__main__':
    r=run(BASE,True); print('FV',round(r['ps'],2),'TV%',round(r['tvpct'],3),'EV',round(r['ev'],1))
    print('rev',[round(x) for x in r['rev']]); print('m',[round(x,4) for x in r['m']]); print('fcff',[round(x,1) for x in r['fc']])
    print('TV',round(r['tv']),'fcffT',round(r['fcff_T'],1))
    print('FV5',round(r['fv5'],2),'ev5',round(r['ev5']),'nd5',round(r['nd5']),'chk',round(r['chk'],3))
    print('exp ret/yr',(r['fv5']/247.71)**(1/5.11)-1)
    b=r['ps']
    tests={'mid 3.6%':dict(mid_margin=0.036),'mid 5.5%':dict(mid_margin=0.055),'mid 6.1% (TTM peak)':dict(mid_margin=0.061),
     'WACC 9.65':dict(wacc=0.0965),'WACC 9.97':dict(wacc=0.0997),'WACC 10.81 (+100)':dict(wacc=0.1081),'WACC 8.81':dict(wacc=0.0881),
     'TGR 2.5':dict(tgr=0.025),'TGR 3.5':dict(tgr=0.035),'RONIC=WACC':dict(ronic=0.0981),'RONIC 25%':dict(ronic=0.25),
     'norm 2y':dict(norm_years=2),'norm 8y':dict(norm_years=8),'nwc 10%':dict(nwc=0.10),'nwc 3%':dict(nwc=0.03),
     'growth -3pp 2028-35':dict(rev_g=[0,0.155,0.06,0.04,0.02,0.02,0.015,0.01,0.01,0.005]),
     'growth +3pp':dict(rev_g=[0,0.155,0.12,0.10,0.08,0.08,0.075,0.07,0.07,0.065]),
     'rev27 +15.0%':dict(rev_g=[0,0.15,0.09,0.07,0.05,0.05,0.045,0.04,0.04,0.035]),
     'capex term 3.0/da2.2':dict(capex_term=0.030),'tax 28':dict(tax=0.28)}
    for k,v in tests.items(): s=S(**v); print(f'{k:28s} {s:8.2f} {s/b-1:+.1%}')
    # Gap closing
    import math
    def solve(key,lo,hi,f=None):
        for _ in range(80):
            mid=(lo+hi)/2; s=S(**{key:mid})
            if (s<247.71)==(lo<hi and S(**{key:lo})<247.71): lo=mid
            else: hi=mid
        return mid
    print('gap close mid margin',solve('mid_margin',0.03,0.12)); print('gap close WACC',solve('wacc',0.12,0.05)); print('gap TGR',solve('tgr',0.02,0.06))
    # reverse DCF: uniform CAGR 2027-2031 then fade to 4,3.5..., margin base path
    def revg(c): return [0,c,c,c,c,c,0.045,0.04,0.04,0.035]
    lo,hi=0.0,0.5
    for _ in range(80):
        mid=(lo+hi)/2
        if S(rev_g=revg(mid))<247.71: lo=mid
        else: hi=mid
    print('implied CAGR 2027-31 base margins',mid)
    lo,hi=0.0,0.5
    for _ in range(80):
        mid=(lo+hi)/2
        if S(rev_g=revg(mid),mid_margin=0.061)<247.71: lo=mid
        else: hi=mid
    print('implied CAGR 2027-31 @6.1% terminal margin',mid)
    # multiples cross-check
    sh=15.721;nd=255.10-3.258
    ttm_rev=4314.683; ebitda_ttm=338.7
    for lbl,e in [('TTM EBITDA',ebitda_ttm),('normalized EBITDA (4.5%+1.81%)',ttm_rev*(0.045+0.0181))]:
        for mlt in (9.45,13.48,20.60,12.14): print(lbl,mlt,round((e*mlt-nd)/sh,1))
