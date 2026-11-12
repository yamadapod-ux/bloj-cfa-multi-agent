# Round 93 -- apply edits to BOTH the working tree and the HEAD blob (staged via git update-index), so the commit contains only R93 changes
# and leaves the pre-existing uncommitted Round 90 hunks in watchlist.md / deployment_log.md unstaged.
import subprocess as sp, os
root=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..')); os.chdir(root)
d='scripts/scout/2026-11-12_assetmgr/'
hdr=open(d+'r93_header.md',encoding='utf8').read().rstrip('\n'); sec=open(d+'r93_section.md',encoding='utf8').read(); dl=open(d+'r93_deploylog.md',encoding='utf8').read()
def wl(s):
    assert s.count('\n*ล่าสุด (2026-11-11)')==1
    s=s.replace('\n*ล่าสุด (2026-11-11)','\n'+hdr+'\n*ก่อนหน้า (2026-11-11)',1)
    return s.rstrip('\n')+'\n'+sec
def dep(s): return s.rstrip('\n')+'\n'+dl
for path,f in (('portfolio/watchlist.md',wl),('portfolio/deployment_log.md',dep)):
    head=sp.run(['git','show','HEAD:'+path],capture_output=True,check=True).stdout.decode('utf8')
    wt=open(path,encoding='utf8',newline='').read()
    nl='\r\n' if '\r\n' in head else '\n'
    new_head=f(head.replace('\r\n','\n')).replace('\n',nl)
    h=sp.run(['git','hash-object','-w','--stdin'],input=new_head.encode('utf8'),capture_output=True,check=True).stdout.decode().strip()
    sp.run(['git','update-index','--cacheinfo','100644,'+h+','+path],check=True)
    open(path,'w',encoding='utf8',newline='').write(f(wt.replace('\r\n','\n')).replace('\n',nl))
    print(path,'staged',h)
