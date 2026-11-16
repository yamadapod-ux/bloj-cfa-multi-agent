import json,urllib.request,sys
UA={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
out={}
for t in sys.argv[1:]:
    try:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.nasdaq.com/api/analyst/{t}/targetprice",headers=UA),timeout=30).read())['data']
        c=d.get('consensusOverview',{}) ; out[t]=c; print(t,c)
    except Exception as e: print(t,'ERR',str(e)[:80])
json.dump(out,open('pt_nasdaq.json','w'),indent=1)
