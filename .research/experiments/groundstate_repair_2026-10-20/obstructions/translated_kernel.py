from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.linalg import eigh
from scipy.signal import fftconvolve
import json,time
rng=np.random.default_rng(20261020)
out=[]
for target in [32,64,128,256,512,1024]:
 alpha=target**(-1/3); X=round(target/alpha)
 a=np.arange(1,X+1); A=a[rng.random(X)<np.minimum(1,2*alpha*(1-a/X))]
 S=np.r_[-A[::-1],A]; I=np.r_[-A[::-1],0,A]; N=len(S); m=int(max(A)); lookup=np.zeros(2*m+1);lookup[m+S]=1
 diff=I[:,None]-I[None,:]; B=np.zeros(diff.shape); mask=abs(diff)<=m;B[mask]=lookup[m+diff[mask]]
 val,v=eigh(B,subset_by_index=[0,0]);k=-val[0];q=v[:,0]; qcoef=np.zeros(2*m+1);qcoef[m+I]=q
 gamma=fftconvolve(qcoef,qcoef[::-1]); h=fftconvolve(lookup,gamma)
 G=gamma[2*m+diff]; H=h[3*m+diff]
 gv=eigh(G,eigvals_only=True,subset_by_index=[0,0])[0]
 lo=eigh(H,G,eigvals_only=True,subset_by_index=[0,0])[0]
 r=fftconvolve(lookup,qcoef);r[m:3*m+1]+=k*qcoef
 R=float(r@r); dr=fftconvolve(lookup,r);g=float(r@dr[m:5*m+1]/R);Ktwo=-float(np.linalg.eigvalsh([[-k,np.sqrt(R)],[np.sqrt(R),g]])[0])
 rec=dict(q0sq=float(q[len(A)]**2),R_over_N15=R/N**1.5,gramMax=float(eigh(G,eigvals_only=True,subset_by_index=[N,N])[0]),R_over_N=R/N,exteriorCost=g,Ktwo=Ktwo,ratioTwo=Ktwo/np.sqrt(N),target=target,n=len(A),X=X,K1=k,Ktranslated=-lo,ratio1=k/np.sqrt(N),ratioTranslated=-lo/np.sqrt(N),gramMin=gv,parity=float(q@q[::-1]))
 out.append(rec);print(json.dumps(rec),flush=True)
 open(str(Path(__file__).resolve().parent / 'translated_kernel.json'),'w').write(json.dumps(out,indent=2))
