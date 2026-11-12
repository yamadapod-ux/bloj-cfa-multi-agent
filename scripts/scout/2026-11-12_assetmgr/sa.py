# Round 93 -- stockanalysis.com statistics page: market cap, shares, P/B, FCF yield, EV/EBITDA, ROIC/ROE, SBC (2nd source for SEC figures).
import urllib.request as u,re,json,sys
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36'}
K=['Market Cap','Enterprise Value','Shares Outstanding','PB Ratio','FCF Yield','EV / EBITDA','Return on Equity (ROE)','Return on Invested Capital (ROIC)','Stock-Based Compensation','Free Cash Flow','Total Debt','Cash &amp; Equivalents','Shareholders\' Equity']
out={}
for t in sys.argv[1:]:
    h=u.urlopen(u.Request(f'https://stockanalysis.com/stocks/{t.lower()}/statistics/',headers=H),timeout=30).read().decode('utf8','ignore')
    txt=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h)); r={}
    for k in K:
        m=re.search(re.escape(k)+r' ([-\d.,]+[A-Z%]?)',txt); r[k]=m.group(1) if m else None
    out[t]=r; print(t,r)
json.dump(out,open('data/sa.json','w'),indent=1)
