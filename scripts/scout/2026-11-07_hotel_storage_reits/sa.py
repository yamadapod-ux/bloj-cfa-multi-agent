# Scout Round 88 -- Nasdaq 52W range (2nd source for Filter A high) + StockAnalysis statistics/forecast pages (saved to data/).
import urllib.request as u, json, re, os, time
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'}; H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
def txt(url,p):
    if not os.path.exists(p): open(p,'wb').write(u.urlopen(u.Request(url,headers=H),timeout=30).read()); time.sleep(.5)
    s=open(p,encoding='utf-8',errors='ignore').read()
    return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s))
for t in 'HST PK RHP APLE SHO XHR DRH EXR CUBE PSA'.split():
    try:
        d=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/info?assetclass=stocks',headers=H2),timeout=20).read())['data']
        n=d['keyStats']['fiftyTwoWeekHighLow']['value']
    except Exception as e: n='ERR '+repr(e)[:50]
    out=[f'{t:5} N52W {n}']
    try:
        s=txt(f'https://stockanalysis.com/stocks/{t.lower()}/statistics/',f'data/st_{t}.html')
        for k in ['Debt / EBITDA','EV / EBITDA','52-Week Price Change','Shares Outstanding','Market Cap']:
            m=re.search(re.escape(k)+r'\s+([^ ]+)',s); out.append(f'{k}={m.group(1) if m else None}')
    except Exception as e: out.append('STAT ERR '+repr(e)[:50])
    try:
        s=txt(f'https://stockanalysis.com/stocks/{t.lower()}/forecast/',f'data/fc_{t}.html')
        m=re.search(r'(Target Low Average Median High.{0,120})',s) or re.search(r'(price target of .{0,120})',s)
        a=re.search(r'(\d+) analysts',s)
        out.append('PT: '+(m.group(1) if m else 'none')+' | '+(a.group(0) if a else ''))
    except Exception as e: out.append('FC ERR '+repr(e)[:50])
    print(' · '.join(out),flush=True)
