import urllib.request as u,json,re,sys,os,html
UA={'User-Agent':'CFA research yamadapod@gmail.com'}
cik,acc=sys.argv[1],sys.argv[2]; a=acc.replace('-','')
idx=json.loads(u.urlopen(u.Request(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/index.json',headers=UA)).read())
for it in idx['directory']['item']:
    n=it['name']
    if n.endswith('.htm') and 'index' not in n:
        fn=f'ex_{a}_{n}.txt'
        if not os.path.exists(fn):
            h=u.urlopen(u.Request(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{n}',headers=UA)).read().decode('utf8','ignore')
            t=re.sub(r'<[^>]+>',' ',h); t=html.unescape(t); t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
            open(fn,'w',encoding='utf8').write(t)
        print(fn, os.path.getsize(fn))
