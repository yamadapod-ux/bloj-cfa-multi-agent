import json,urllib.request,datetime
UA={'User-Agent':'Mozilla/5.0'}
s=json.load(open('sec.json')); p=json.load(open('prices.json'))
SH={'BELFB':12.7e6}
CUR={'JBL':(28702,35954,30.1),'FLEX':(29832,30954,24.8),'SANM':(9278,12763,69.6),'TTMI':(8758,3828,59.9),'BHE':(2129,2948,18.6),'KN':(2865,666,20.3),'FN':(11083,5137,50.7),'BELFB':(2531,786,23.5),'VSH':(3209,3508,23.8),'PLXS':(5535,4034,0.0),'OSIS':(3733,1805,4.0)}
res={}
for t,(ev,rev,gr) in CUR.items():
    d=json.loads(urllib.request.urlopen(urllib.request.Request(f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=7y&interval=1mo",headers=UA)).read())['chart']['result'][0]
    ts=[datetime.date.fromtimestamp(x) for x in d['timestamp']]; cl=d['indicators']['quote'][0]['close']
    r=s[t]; revfy=r['rev']['fy']; dil={e[:7]:v for e,v in r['dil']['fy']} if r.get('dil') else {}
    nd_now=ev-(p[t]['y_close']*(SH.get(t) or 0)/1e6) if t in SH else None
    rows=[]
    for i in range(1,len(revfy)):
        e,rv=revfy[i]; g=(rv/revfy[i-1][1]-1)*100
        ed=datetime.date.fromisoformat(e)
        # month close nearest fy end
        j=min(range(len(ts)),key=lambda k:abs((ts[k]-ed).days))
        if abs((ts[j]-ed).days)>40 or cl[j] is None: continue
        sh=dil.get(e[:7]) or SH.get(t)
        if not sh: continue
        mc=cl[j]*sh/1e6
        nd=ev-p[t]['y_close']*(sh if t in SH else (r['shs']['last'] if r.get('shs') and r['shs'].get('end','')>='2026' else r['dil']['fy'][-1][1]))/1e6
        rows.append((e[:7],round(g,1),round((mc+nd)/(rv/1e6),2)))
    rows=rows[-5:]
    hist=[x[2] for x in rows]; cur=ev/rev
    srt=sorted(hist); p33=srt[max(0,round(len(srt)/3)-1)] if srt else None
    rank=sum(1 for h in hist if h<cur)/len(hist) if hist else None
    # self regression
    reg=None
    if len(rows)>=4:
        xs=[x[1] for x in rows]; ys=[x[2] for x in rows]; n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
        sxx=sum((x-mx)**2 for x in xs); b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sxx if sxx else 0; a=my-b*mx
        pred=a+b*gr; reg=(round(a,3),round(b,4),round(pred,2),round(cur/pred,2) if pred>0 else None)
    res[t]=dict(cur=round(cur,2),hist=rows,pct_rank=rank,min=min(hist) if hist else None,max=max(hist) if hist else None,reg=reg,gr=gr)
    print(t,'EV/Rev now',round(cur,2),'growth',gr,'| hist',rows,'| rank',rank,'| selfreg (a,b,pred,ratio)',reg)
json.dump(res,open('evrev.json','w'),indent=1)
