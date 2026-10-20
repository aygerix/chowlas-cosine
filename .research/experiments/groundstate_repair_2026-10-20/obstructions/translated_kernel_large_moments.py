from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,time
from scipy.fft import rfft,irfft,next_fast_len
from scipy.signal import fftconvolve
from scipy.sparse.linalg import LinearOperator,eigsh,cg
rng=np.random.default_rng(20261022)
out=[]
for target in [2048,4096,8192]:
 t=time.time();alpha=target**(-1/3);X=round(target/alpha);a=np.arange(1,X+1);A=a[rng.random(X)<2*alpha*(1-a/X)];I=np.r_[-A[::-1],0,A];N=len(I)-1;m=int(max(A));L=next_fast_len(4*m+1);idx=I%L
 def op(coef,offset):
  kernel=np.zeros(L);lags=np.arange(len(coef))-offset;kernel[lags%L]=coef;f=rfft(kernel)
  def mv(v):
   z=np.zeros(L);z[idx]=np.asarray(v).reshape(-1);return irfft(rfft(z)*f,L)[idx]
  return LinearOperator((N+1,N+1),matvec=mv,dtype=float)
 d=np.zeros(2*m+1);d[m+A]=1;d[m-A]=1;B=op(d,m);val,vec=eigsh(B,k=1,which='SA',tol=1e-10,ncv=30);k=-val[0];q=vec[:,0]
 qc=np.zeros(2*m+1);qc[m+I]=q;gamma=fftconvolve(qc,qc[::-1]);h=fftconvolve(d,gamma)
 r=fftconvolve(d,qc);r[m:3*m+1]+=k*qc;R=float(r@r);dr=fftconvolve(d,r);g=float(r@dr[m:5*m+1]/R)
 G=op(gamma,2*m);gmin=eigsh(G,k=1,which='SA',tol=1e-7,return_eigenvectors=False)[0];gmax=eigsh(G,k=1,which='LA',tol=1e-7,return_eigenvectors=False)[0]
 rec=dict(target=target,n=len(A),N=N,K1=k,q0sq=float(q[len(A)]**2),R_over_N=R/N,R_over_N15=R/N**1.5,exteriorCost=g,gramMin=gmin,gramMax=gmax,parity=float(q@q[::-1]),seconds=time.time()-t)
 out.append(rec);print(json.dumps(rec),flush=True);open(str(Path(__file__).resolve().parent / 'translated_kernel_large_moments.json'),'w').write(json.dumps(out,indent=2))
