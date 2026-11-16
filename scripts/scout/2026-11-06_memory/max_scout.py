# Max targeted scout WDC/STX/SNDK (CIO-directed 2026-11-08). Usage: python -I max_scout.py px|fund|calc
import urllib.request as u, json, time, sys, os, statistics as st
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')
HY={'User-Agent':'Mozilla/5.0'}; H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
mode=sys.argv[1] if len(sys.argv)>1 else 'calc'
if mode=='px':
  for t in ['WDC','STX','SNDK','NTAP','PSTG']:
   try:
    d=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1y&interval=1d',headers=HY),timeout=30).read())['chart']['result'][0]
    q=d['indicators']['quote'][0]; days=[time.strftime('%Y-%m-%d',time.gmtime(x)) for x in d['timestamp']]; cc=dict(zip(days,q['close']))
    hi=max((x,i) for i,x in enumerate(q['high']) if x); hc=max((x,i) for i,x in enumerate(q['close']) if x); lo=min((x,i) for i,x in enumerate(q['low']) if x)
    print(t,'last',d['meta']['regularMarketPrice'],{k:round(cc[k],2) for k in days[-4:]},'hiIntra',round(hi[0],2),days[hi[1]],'hiClose',round(hc[0],2),days[hc[1]],'lo',round(lo[0],2),days[lo[1]])
    try:
        r=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate=2026-11-03&todate=2026-11-07&limit=5',headers=H2),timeout=25).read())['data']['tradesTable']['rows']
        print('  Nasdaq',{x['date']:x['close'] for x in r})
    except Exception as e: print('  Nasdaq ERR',repr(e)[:80])
   except Exception as e: print(t,'ERR',repr(e)[:80])

if mode=='fund':
  src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'fund.py'),encoding='utf-8').read()
  TAGS=eval(src.split('TAGS=')[1].split(chr(10)+'out=')[0])
  CIK={'WDC':106040,'STX':1137789,'SNDK':2023554}
  for t in CIK:
    f=json.load(open(f'{D}/cf_{t}.json','rb')); print('=====',t,f['entityName'])
    g=dict(f['facts'].get('us-gaap',{})); g.update(f['facts'].get('dei',{}))
    for k,tags in TAGS.items():
        ann={}; q={}; inst={}
        for tg in tags:
            for un,rows in g.get(tg,{}).get('units',{}).items():
                for r in rows:
                    if not r.get('form','').startswith('10-') or r['end']<'2016': continue
                    if 'start' in r:
                        days=(time.mktime(time.strptime(r['end'],'%Y-%m-%d'))-time.mktime(time.strptime(r['start'],'%Y-%m-%d')))/86400
                        if 340<days<380: ann.setdefault(r['end'],r['val'])
                        elif 80<days<100: q.setdefault(r['end'],r['val'])
                        elif r['end']>='2025-06': q.setdefault(r['end']+f'~{int(days)}d',r['val'])
                    else: inst.setdefault(r['end'],r['val'])
        fmt=lambda d,n:{a:(round(b/1e6) if abs(b)>1e5 else b) for a,b in sorted(d.items())[-n:]}
        if ann: print(k,'ANN',fmt(ann,11))
        if q: print(k,'QTR',fmt(q,7))
        if inst: print(k,'BAL',fmt(inst,4))
    fl=[r for rows in g.get('Assets',{}).get('units',{}).values() for r in rows]
    print('latest filing',max(((r['filed'],r['form'],r['accn'],r['end']) for r in fl)))
if mode=='hi':
  for t in ['WDC','STX','SNDK']:
    try:
      r=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/summary?assetclass=stocks',headers=H2),timeout=25).read())['data']['summaryData']
      print(t,{k:v.get('value') for k,v in r.items() if 'Week' in k or 'Target' in k})
    except Exception as e: print(t,'ERR',repr(e)[:80])
if mode=='calc':
  # Prices close 2026-11-06 (Yahoo chart = Nasdaq historical); 52W high Yahoo intraday = Nasdaq summary
  Rf,ERP=4.84,4.41   # ^TNX 11-05 (Charlie verified inputs) ; Damodaran implied ERP 2026-11-01
  # SEC XBRL $M. cash/debt/lease at 2026-10-02 10-Q; FCF annual = OCF - capex
  N={'WDC':dict(px=263.78,hi=799.87,sh=374.32,beta=2.34,cash=1314,debt=789,lease=133,nonop=0,
        rev={2017:19093,2018:20647,2019:16569,2020:16736,2021:16922,2022:18793,2023:12318,2024:13003,2025:9520,2026:12919},
        ocf={2017:3437,2018:4205,2019:1547,2020:824,2021:1898,2022:1880,2023:-408,2024:-294,2025:1691,2026:3929},
        cap={2017:578,2018:835,2019:876,2020:647,2021:1146,2022:1122,2023:821,2024:487,2025:412,2026:418},
        ttm_rev=3017+3337+(12919-9172)+4381, ttm_fcf=4290, q_fcf=1604-227, pt=(622.5,600.0)),
     'STX':dict(px=460.99,hi=1145.0,sh=229.56,beta=2.20,cash=1258,debt=2383,lease=333,nonop=0,
        rev={2016:11160,2017:10771,2018:11184,2019:10390,2020:10509,2021:10681,2022:11661,2023:7384,2024:6551,2025:9097,2026:12195},
        ocf={2016:1680,2017:1916,2018:2113,2019:1761,2020:1714,2021:1626,2022:1657,2023:942,2024:918,2025:1083,2026:3674},
        cap={2016:587,2017:434,2018:366,2019:602,2020:585,2021:498,2022:381,2023:316,2024:254,2025:265,2026:569},
        ttm_rev=2825+3112+(12195-8566)+4233, ttm_fcf=4160, q_fcf=1690-211, pt=(1045.0,1050.0)),
     'SNDK':dict(px=835.06,hi=2354.39,sh=142.29,beta=None,beta_blume=1.99,cash=5136,debt=0,lease=201,nonop=2289,
        rev={2023:6086,2024:6663,2025:7355,2026:20248},
        ocf={2023:-713,2024:-309,2025:84,2026:11671},
        cap={2023:219,2024:166,2025:204,2026:177},
        ttm_rev=3025+5950+(20248-11283)+11031, ttm_fcf=17370, q_fcf=6363-54, pt=(2050.0,2025.0))}
  sfcf=lambda x,ys: sum(x['ocf'][y]-x['cap'][y] for y in ys)
  S=N['STX']; stx_m=sfcf(S,S['ocf'])/sum(S['rev'].values())
  print(f"STX 11y through-cycle FCF margin FY16-26 = {100*stx_m:.2f}%  (ex-FY26: {100*sfcf(S,range(2016,2026))/sum(S['rev'][y] for y in range(2016,2026)):.2f}%)")
  for t,x in N.items():
    b=x.get('beta_blume') or round(.67*x['beta']+.33,2); w=(Rf+b*ERP)/100
    mc=x['px']*x['sh']; net=x['cash']+x['nonop']-x['debt']-x['lease']
    fcf={y:x['ocf'][y]-x['cap'][y] for y in x['ocf']}
    avg=sum(fcf.values())/len(fcf); m=sum(fcf.values())/sum(x['rev'].values())
    fv=lambda f:(f/w+net)/x['sh']
    print(f"\n== {t} px {x['px']} hi {x['hi']} off-high {100*(x['px']/x['hi']-1):.1f}% | mcap {mc/1e3:.1f}B net(cash+nonop-debt-lease) {net} | Blume beta {b} WACC~CoE {100*w:.2f}%")
    print('  FCF by FY',fcf, f'avg {avg:.0f} | own through-cycle FCF margin {100*m:.1f}% | TTM rev {x["ttm_rev"]} TTM FCF {x["ttm_fcf"]} yield {100*x["ttm_fcf"]/mc:.2f}%')
    cases={'own-history avg FCF':avg,'TTM FCF (peak, reference only)':x['ttm_fcf'],'latest Q x4 (reference only)':4*x['q_fcf']}
    if t=='WDC':
      nr=(9520+12919+x['ttm_rev'])/3; cases['STX 11y margin x WDC HDD-only norm rev %.0f'%nr]=stx_m*nr
    if t=='SNDK':
      nr=(6086+6663+7355+20248+x['ttm_rev'])/5; cases['own FY23-26 FCF margin x norm rev %.0f'%nr]=m*nr
    for k,f in cases.items():
      v=fv(f); print(f"  naive FV [{k}] FCF {f:.0f} -> ${v:.0f}  price/FV {x['px']/v:.2f}x")
    need=(x['px']/1.5*x['sh']-net)*w; print(f"  FCF needed so price = 1.5x naive FV: ${need:.0f}M = {100*need/x['ttm_rev']:.0f}% of TTM rev")
    for p in x['pt']: print(f"  Street PT {p}: gap +{100*(p/x['px']-1):.0f}%  price/PT {x['px']/p:.2f}")
  EVR={'WDC':6.79,'STX':7.77,'SNDK':3.85,'NTAP':4.36,'P':7.38}  # StockAnalysis statistics, close 11-06
  G={'NTAP':12.15,'P':27.21}
  for t in ['WDC','STX','SNDK']:
    f=json.load(open(f'{D}/cf_{t}.json','rb'))['facts']['us-gaap']; q={}
    for tg in ['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues']:
      for rows in f.get(tg,{}).get('units',{}).values():
        for r in sorted(rows,key=lambda r:r.get('filed','')):
          if 'start' in r and r.get('form','').startswith('10-'):
            d=(time.mktime(time.strptime(r['end'],'%Y-%m-%d'))-time.mktime(time.strptime(r['start'],'%Y-%m-%d')))/86400
            if 80<d<100: q[r['end']]=r['val']/1e6
    if t=='WDC': q['2026-07-03']=12919-9172
    if t=='STX': q['2026-07-03']=12195-8566
    if t=='SNDK': q['2026-07-03']=20248-11283
    ks=sorted(q); print(t,'quarters (latest filed)',{k:round(q[k]) for k in ks[-9:]})
    G[t]=100*(sum(q[k] for k in ks[-4:])/sum(q[k] for k in ks[-8:-4])-1) if len(ks)>=8 else None
  print('TTM growth %',{k:(round(v,1) if v is not None else v) for k,v in G.items()})
  peers={'WDC':['STX','SNDK','NTAP','P'],'STX':['WDC','SNDK','NTAP','P'],'SNDK':['WDC','STX','NTAP','P']}
  sect=6.63
  for t,ps in peers.items():
    med=st.median(EVR[p] for p in ps)
    xs=[G[p] for p in ps if G.get(p) is not None]; ys=[EVR[p] for p in ps if G.get(p) is not None]; msg=''
    if len(xs)>=3 and G.get(t) is not None:
      sl,ic=st.linear_regression(xs,ys); pred=ic+sl*G[t]
      msg=f"| peer-regression n={len(xs)} slope {sl:.4f} int {ic:.2f} -> pred {pred:.2f}x at g={G[t]:.0f}% actual/pred {EVR[t]/pred:.2f}" if pred>0 else f"| peer-regression pred {pred:.2f}x unusable"
    print(f"{t} EV/Rev {EVR[t]} | peers {dict((p,EVR[p]) for p in ps)} median {med:.2f} ratio {EVR[t]/med:.2f} | sector 6.63 ratio {EVR[t]/sect:.2f} {msg}")
  y=json.load(open(f'{D}/y_STX_5y.json','rb'))['chart']['result'][0]
  px=dict(zip(y['timestamp'],y['indicators']['quote'][0]['close'])); rv=S['rev']; sh={2021:245,2022:224,2023:207,2024:212,2025:217,2026:229}
  fyend={2021:'2021-07-02',2022:'2022-07-01',2023:'2023-06-30',2024:'2024-06-28',2025:'2025-06-27',2026:'2026-07-03'}
  ps=[]
  for ts,p in sorted(px.items()):
    if not p: continue
    ds=time.strftime('%Y-%m-%d',time.gmtime(ts)); fy=[k for k,v in fyend.items() if v<=ds]
    if fy: ps.append((ds,p*sh[fy[-1]]/rv[fy[-1]]))
  v=sorted(a for _,a in ps); cur=460.99*229.56/12195
  print(f"STX self-history P/S (mcap/last-FY rev) n={len(v)} {ps[0][0]}..{ps[-1][0]} min {v[0]:.2f} p33 {v[len(v)//3]:.2f} med {st.median(v):.2f} p70 {v[int(len(v)*.7)]:.2f} max {v[-1]:.2f} | current same basis {cur:.2f} pctile {100*sum(1 for a in v if a<cur)/len(v):.0f}")
  pts=[]
  for fy in range(2022,2027):
    vals=[a for d,a in ps if fyend[fy-1]<d<=fyend[fy]]
    if vals: pts.append((100*(rv[fy]/rv[fy-1]-1),sum(vals)/len(vals)))
  print('STX self-regression pts (FY growth %, avg P/S during FY)',[(round(a,1),round(b,2)) for a,b in pts])
  sl,ic=st.linear_regression([a for a,_ in pts],[b for _,b in pts]); pred=ic+sl*G['STX']
  print(f"  fit slope {sl:.4f} int {ic:.2f} -> pred P/S {pred:.2f} at TTM g {G['STX']:.0f}% ; current {cur:.2f} ratio {cur/pred:.2f}")
if mode=='roic':
  # 5Y (FY22-26) through-cycle ROIC ~ sum(OpInc*(1-tax rate)) / sum(avg invested capital = equity + debt - cash) at FY-ends, SEC XBRL 10-K
  def bal(g,tags):
    d={}
    for tg in tags:
      for rows in g.get(tg,{}).get('units',{}).values():
        for r in rows:
          if r.get('form','').startswith('10-K') and 'start' not in r: d.setdefault(r['end'],r['val']/1e6)
    return d
  def ann(g,tags):
    d={}
    for tg in tags:
      for rows in g.get(tg,{}).get('units',{}).values():
        for r in rows:
          if r.get('form','').startswith('10-K') and 'start' in r:
            dd=(time.mktime(time.strptime(r['end'],'%Y-%m-%d'))-time.mktime(time.strptime(r['start'],'%Y-%m-%d')))/86400
            if 340<dd<380: d.setdefault(r['end'],r['val']/1e6)
    return d
  for t in ['WDC','STX','SNDK']:
    g=json.load(open(f'{D}/cf_{t}.json','rb'))['facts']['us-gaap']
    eq=bal(g,['StockholdersEquity']); debt=bal(g,['LongTermDebt','DebtLongtermAndShorttermCombinedAmount']); dn=bal(g,['LongTermDebtNoncurrent']); dc=bal(g,['LongTermDebtCurrent','DebtCurrent']); cash=bal(g,['CashAndCashEquivalentsAtCarryingValue'])
    op=ann(g,['OperatingIncomeLoss']); tx=ann(g,['IncomeTaxExpenseBenefit']); pti=ann(g,['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'])
    ends=sorted(k for k in op if k>='2021-06')[-5:]; rows=[]
    for e in ends:
      de=debt.get(e, (dn.get(e,0)+dc.get(e,0)))
      ic=eq.get(e,float('nan'))+de-cash.get(e,0); rate=min(max(tx.get(e,0)/pti[e],0),0.25) if pti.get(e,0)>0 else 0.15
      rows.append((e,round(op[e]),round(ic),round(100*op[e]*(1-rate)/ic,1) if ic==ic and ic>0 else None))
    ics=[r[2] for r in rows if r[2]==r[2] and r[2]>0]; nop=sum(r[1]*(0.85) for r in rows)
    print(t,rows,'| 5Y pooled after-tax(15%) ROIC ~',round(100*nop/sum(ics),1) if len(ics)==len(rows) else 'IC missing')
