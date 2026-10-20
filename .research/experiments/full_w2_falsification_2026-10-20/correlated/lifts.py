from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,time,argparse
from scipy.fft import rfft,irfft,next_fast_len
from scipy.sparse.linalg import LinearOperator,eigsh

def evaluate(S,tag):
 t=time.time(); S=np.unique(S); S=S[S!=0];R=int(abs(S).max()); grid=next_fast_len(6*R+1)
 kernel=np.zeros(grid);kernel[S%grid]=1; fk=rfft(kernel)
 sums=irfft(fk*fk,n=grid); W=np.flatnonzero((sums>.5)|(kernel>.5));W=np.union1d(W,[0]);
 def mv(v):
  x=np.zeros(grid);x[W]=v;return irfft(rfft(x)*fk,n=grid)[W]
 op=LinearOperator((len(W),len(W)),matvec=mv,dtype=float)
 lam,v=eigsh(op,k=1,which='SA',tol=1e-8,ncv=30,maxiter=2000,v0=np.random.default_rng(2718).normal(size=len(W)))
 residual=np.linalg.norm(mv(v[:,0])-lam[0]*v[:,0]);K=-lam[0]
 rec={'tag':tag,'N':len(S),'radius':R,'W2':len(W),'K':K,'K_over_sqrtN':K/np.sqrt(len(S)),'residual':residual,'seconds':time.time()-t}
 print(json.dumps(rec),flush=True);return rec

def support(q,H,mode,seed=1):
 n=q//2;r=np.arange(1,n+1); rng=np.random.default_rng(seed)
 # Balanced quantiles from symmetric triangular density on [-H,H].
 u=(np.arange(n)+.5)/n;v=np.where(u<.5,-1+np.sqrt(2*u),1-np.sqrt(2-2*u));h=np.rint(H*v).astype(int)
 if mode=='random':rng.shuffle(h)
 elif mode=='quadratic':h=h[np.argsort((r*r)%q,kind='stable')]
 elif mode=='bitreverse':h=h[np.argsort([int(f'{x:0{n.bit_length()}b}'[::-1],2) for x in r])]
 elif mode=='saw':h=np.rint(H*(2*((r*0.61803398875)%1)-1)).astype(int)
 elif mode=='sorted':pass
 elif mode=='alternating':h=h[np.argsort((-1)**r*r)]
 a=r+q*h;return np.r_[a,-a]
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--qs',default='31,61,127,251');p.add_argument('--modes',default='random,quadratic,bitreverse,sorted,alternating');p.add_argument('--power',type=float,default=.5);args=p.parse_args();out=[]
 for q in map(int,args.qs.split(',')):
  H=max(1,round(q**args.power))
  for mode in args.modes.split(','):
   out.append(evaluate(support(q,H,mode),f'q{q}_H{H}_{mode}'))
   open(str(ARCHIVE_ROOT / 'correlated/lifts_results.json'),'w').write(json.dumps(out,indent=2))
