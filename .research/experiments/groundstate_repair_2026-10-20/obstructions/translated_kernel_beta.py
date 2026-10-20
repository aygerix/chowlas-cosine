from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,time
from scipy.fft import rfft,irfft,next_fast_len
from scipy.signal import fftconvolve
from scipy.sparse.linalg import LinearOperator,eigsh,cg
rng=np.random.default_rng(20261022)
out=[]
for beta,target in [(b,n) for b in [.4,.45] for n in [128,512,2048]]:
 t=time.time();alpha=target**(-beta);X=round(target/alpha);a=np.arange(1,X+1);A=a[rng.random(X)<2*alpha*(1-a/X)];I=np.r_[-A[::-1],0,A];N=len(I)-1;m=int(max(A));L=next_fast_len(4*m+1);idx=I%L
 def op(coef,offset):
  kernel=np.zeros(L);lags=np.arange(len(coef))-offset;kernel[lags%L]=coef;f=rfft(kernel)
  def mv(v):
   z=np.zeros(L);z[idx]=np.asarray(v).reshape(-1);return irfft(rfft(z)*f,L)[idx]
  return LinearOperator((N+1,N+1),matvec=mv,dtype=float)
 d=np.zeros(2*m+1);d[m+A]=1;d[m-A]=1;B=op(d,m);val,vec=eigsh(B,k=1,which='SA',tol=1e-10,ncv=30);k=-val[0];q=vec[:,0]
 qc=np.zeros(2*m+1);qc[m+I]=q;gamma=fftconvolve(qc,qc[::-1]);h=fftconvolve(d,gamma)
 r=fftconvolve(d,qc);r[m:3*m+1]+=k*qc;R=float(r@r);dr=fftconvolve(d,r);g=float(r@dr[m:5*m+1]/R);ktwo=-np.linalg.eigvalsh([[-k,np.sqrt(R)],[np.sqrt(R),g]])[0]
 print("moment",beta,target,"q0",q[len(A)]**2,"R/N",R/N,"g",g,flush=True)
 G=op(gamma,2*m);H=op(h[m:5*m+1],2*m)
 def inv(v):
  u,info=cg(G,v,rtol=2e-10,maxiter=1000)
  if info:raise RuntimeError(info)
  return u
 Gi=LinearOperator(G.shape,matvec=inv,dtype=float)
 vals,vs=eigsh(H,k=1,M=G,Minv=Gi,which='SA',tol=2e-8,ncv=30,maxiter=2000)
 u=vs[:,0];res=np.linalg.norm(H@u-vals[0]*(G@u));rec=dict(beta=beta,q0sq=float(q[len(A)]**2),R_over_N=R/N,exteriorCost=g,ratioTwo=ktwo/np.sqrt(N),target=target,n=len(A),X=X,K1=k,Ktranslated=-vals[0],ratio1=k/np.sqrt(N),ratioTranslated=-vals[0]/np.sqrt(N),residual=res,seconds=time.time()-t)
 out.append(rec);print(json.dumps(rec),flush=True);open(str(Path(__file__).resolve().parent / 'translated_kernel_beta.json'),'w').write(json.dumps(out,indent=2))
