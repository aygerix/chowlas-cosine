from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import numpy as np,json,time,sys
from scipy.fft import rfft,irfft,next_fast_len
from scipy.sparse.linalg import LinearOperator,eigsh
from scipy.linalg import eigh
from scipy.signal import fftconvolve
from pathlib import Path
OUT=Path(__file__).parent

def calc(A,tag,verify=False):
 A=np.unique(np.asarray(A,dtype=int));A=A[A>0];X=int(A.max());N=2*len(A)
 # Integer coefficient convolution support, numerically checked rounding gap.
 ker=np.zeros(2*X+1);ker[X+A]=ker[X-A]=1
 conv=fftconvolve(ker,ker);rounded=np.rint(conv);error=np.max(np.abs(conv-rounded))
 assert error<1e-6
 mask=rounded>0;mask[2*X+A]=True;mask[2*X-A]=True;mask[2*X]=True
 W=np.flatnonzero(mask)-2*X;L=next_fast_len(5*X+1);ids=W%L
 k=np.zeros(L);k[A]=k[-A]=1;fk=rfft(k)
 def mv(v):
  z=np.zeros(L);z[ids]=v;return irfft(rfft(z)*fk,n=L)[ids]
 op=LinearOperator((len(W),len(W)),matvec=mv,dtype=float)
 t=time.time();val,vec=eigsh(op,k=1,which='SA',tol=1e-9,ncv=30,maxiter=1500,v0=np.random.default_rng(991).normal(size=len(W)))
 K=-val[0];res=np.linalg.norm(mv(vec[:,0])-val[0]*vec[:,0])
 rec=dict(tag=tag,n=len(A),N=N,X=X,W=len(W),K=K,normalized=K/np.sqrt(N),rho=N/K**2,residual=res,convolution_rounding_error=error,seconds=time.time()-t)
 if verify and len(W)<1800:
  S=np.r_[A,-A];H=np.isin(W[:,None]-W,S).astype(float);kd=-eigh(H,subset_by_index=[0,0],eigvals_only=True)[0];rec['dense_K']=kd;assert abs(kd-K)<1e-6
 print(json.dumps(rec),flush=True)
 with (OUT/'results.jsonl').open('a') as f:f.write(json.dumps(rec)+'\n')
 np.savez_compressed(OUT/(tag+'.npz'),A=A,W=W,eigenvector=vec[:,0],K=K)
 return rec

def tri(n,kind):
 X=int(round(n**(4/3)));a=np.arange(1,X+1);p=2*n/X*(1-a/(X+1))
 if kind=='cumulative':return a[np.diff(np.floor(np.r_[0,np.cumsum(p)]+.5))>0]
 if kind=='golden':u=(a*((np.sqrt(5)-1)/2))%1
 if kind=='quadratic':u=(a*a*((np.sqrt(5)-1)/2))%1
 if kind=='random':u=np.random.default_rng(821+n).random(X)
 return a[u<p]
if __name__=='__main__':
 for n in [32,64,128,256,512,1024]:
  for kind in ['cumulative','golden','quadratic','random']:
   calc(tri(n,kind),f'tri_{kind}_{n}',verify=n<=64)
