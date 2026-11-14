import json
s=json.load(open('sec.json')); p=json.load(open('prices.json'))
M=1e6
def v(r,k,f='ttm'):
    x=r.get(k); 
    if not x: return None
    return x.get(f) if f in x else x.get('last')
for t,r in s.items():
    pr=p[t]['y_close']
    rev=v(r,'rev');oi=v(r,'oi');ocf=v(r,'ocf');cap=v(r,'capex');sbc=v(r,'sbc');da=v(r,'da')
    eq=v(r,'eq','last');ltd=v(r,'ltd','last') or 0;std=v(r,'std','last') or 0;cash=(v(r,'cash','last') or 0)+(v(r,'sti','last') or 0)
    dil=v(r,'dil')  # ttm on shares is sum - use latest fy/period instead
    dl=r['dil']; shares=None
    if dl: shares=dl['fy'][-1][1] if dl['fy'] else None
    print('=====',t,r['name'],'ttm_end',r['rev']['ttm_end'] if r.get('rev') else '', 'ytd_m',r['rev']['ytd_m'] if r.get('rev') else '')
    print(' eq_end',r['eq'] and r['eq'].get('end'),'eq',eq and round(eq/M),'ltd',round(ltd/M),'std',round(std/M),'cash',round(cash/M),'gw',v(r,'gw','last') and round(v(r,'gw','last')/M))
    def f(x): return None if x is None else round(x/M,1)
    print(' TTM rev',f(rev),'oi',f(oi),'ocf',f(ocf),'capex',f(cap),'sbc',f(sbc),'da',f(da),'dil(fy)',shares and round(shares/M,2))
    for k in ['rev','oi','ocf','capex','sbc']:
        if r.get(k): print('  FY',k,[(e[:7],round(x/M)) for e,x in r[k]['fy']])
    if dl: print('  dil fy',[(e[:7],round(x/M,1)) for e,x in dl['fy']])
