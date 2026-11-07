# Scout Round 88 -- daily closes around Q3 prints: Yahoo vs Nasdaq vs StockAnalysis history, to test big recent moves.
import urllib.request as u, json, sys, time, re, os
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120'}; H2={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
for t in sys.argv[1:]:
    y=json.loads(u.urlopen(u.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1mo&interval=1d',headers=H),timeout=30).read())['chart']['result'][0]
    Y={time.strftime('%m/%d',time.gmtime(a)):round(b,2) for a,b in zip(y['timestamp'],y['indicators']['quote'][0]['close']) if b}
    r=json.loads(u.urlopen(u.Request(f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate=2026-10-20&limit=20&todate=2026-11-07',headers=H2),timeout=25).read())['data']['tradesTable']['rows']
    N={x['date'][:5]:x['close'].replace('$','') for x in r}
    print(t,' '.join(f"{d}:{Y.get(d)}/{N.get(d)}" for d in sorted(N)))
    p=f'data/hist_{t}.html'
    if not os.path.exists(p): open(p,'wb').write(u.urlopen(u.Request(f'https://stockanalysis.com/stocks/{t.lower()}/history/',headers=H),timeout=30).read())
    s=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',open(p,encoding='utf-8',errors='ignore').read()))
    m=re.search(r'(Nov \d+, 2026.{0,90})',s); print('   SA',m.group(1) if m else 'none')
