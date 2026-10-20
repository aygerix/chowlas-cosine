from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,time
from scipy.fft import rfft,irfft,next_fast_len
from scipy.sparse.linalg import LinearOperator,eigsh
from lifts import evaluate

def kval(q,h,seed=2718):
 a=np.arange(1,len(h)+1)+q*h;S=np.r_[a,-a];R=max(abs(S));grid=next_fast_len(6*R+1);ker=np.zeros(grid);ker[S%grid]=1;fk=rfft(ker);W=np.flatnonzero((irfft(fk*fk,n=grid)>.5)|(ker>.5));W=np.union1d(W,[0])
 def mv(v):
  x=np.zeros(grid);x[W]=v;return irfft(rfft(x)*fk,n=grid)[W]
 op=LinearOperator((len(W),len(W)),matvec=mv,dtype=float)
 return -eigsh(op,k=1,which='SA',tol=2e-5,ncv=20,maxiter=400,v0=np.random.default_rng(seed).normal(size=len(W)),return_eigenvectors=False)[0]
res=[];rng=np.random.default_rng(9943)
for q,steps in [(31,1500),(61,1500),(127,1200),(251,800)]:
 n=q//2;H=round(q**.5);u=(np.arange(n)+.5)/n;h=np.rint(H*np.where(u<.5,-1+np.sqrt(2*u),1-np.sqrt(2-2*u))).astype(int);rng.shuffle(h);cur=kval(q,h);best=cur;bh=h.copy();start=time.time()
 for i in range(steps):
  p,j=rng.choice(n,2,replace=False)
  if h[p]==h[j]:continue
  h[p],h[j]=h[j],h[p];v=kval(q,h)
  temperature=.15*np.sqrt(q)*(1-i/steps)**2+.001
  if v<cur or rng.random()<np.exp((cur-v)/temperature):cur=v
  else:h[p],h[j]=h[j],h[p]
  if cur<best:best=cur;bh=h.copy()
  if i%200==0:print(json.dumps(dict(q=q,step=i,best=best,ratio=best/np.sqrt(q-1),seconds=time.time()-start)),flush=True)
 a=np.arange(1,n+1)+q*bh;rec=evaluate(np.r_[a,-a],f'optimized_q{q}_H{H}');rec['h']=bh.tolist();rec['steps']=steps;res.append(rec)
 open(str(ARCHIVE_ROOT / 'correlated/optimized_results.json'),'w').write(json.dumps(res,indent=2))
