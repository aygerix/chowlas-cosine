from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
from search import *
seed=np.r_[np.arange(1,19),np.arange(20,38),[39,40,41,42,47,48,50,52,57,61,62,64,65,68]]
S=set(seed)|set(-seed);W=sorted({a+b for a in S for b in S});assert S<=set(W)
B=np.isin(np.subtract.outer(W,W),list(S)).astype(float);eb=eigh(B,eigvals_only=True)
records=[]
for h in [0,1,2,4,8,16,32]:
 q=5*h+1;A=np.concatenate([q*a+np.arange(-h,h+1) for a in seed]);r=calc(A,f'symmetric_blowup_h{h}')
 rgrid=np.arange(-2*h,2*h+1);T=(np.abs(rgrid[:,None]-rgrid)<=h).astype(float);et=eigh(T,eigvals_only=True)
 exactK=-min(eb[0]*et[-1],eb[-1]*et[0]);r['kronecker_K']=exactK;r['difference']=r['K']-exactK;r['elementary_lower_bound']=(-eb[0])*((2*h+1)-h*(h+1)/(4*h+1));assert abs(r['K']-exactK)<1e-6
 records.append(r)
open(OUT/'blowup_verification.json','w').write(json.dumps(records,indent=2))
