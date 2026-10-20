from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from scipy.linalg import eigh,block_diag
from scipy.signal import fftconvolve
rng=np.random.default_rng(42);target=128;alpha=target**(-.45);X=round(target/alpha);a=np.arange(1,X+1);A=a[rng.random(X)<2*alpha*(1-a/X)];T=np.r_[-A[::-1],A];NT=len(T);Ts=set(T);BT=np.array([[int(x-y in Ts) for y in T]for x in T]);WT=np.block([[np.zeros((1,1)),np.ones((1,NT))],[np.ones((NT,1)),BT]]);kt=-eigh(WT,eigvals_only=True,subset_by_index=[0,0])[0]
out=[]
for L in [32,64,128]:
 I=np.arange(-L,L+1);BU=((abs(I[:,None]-I[None,:])<=L)&(I[:,None]!=I[None,:])).astype(float);ev,v=eigh(BU,subset_by_index=[0,0]);ku=-ev[0];q=v[:,0];S=((abs(I)<=L)&(I!=0)).astype(float);g=fftconvolve(q,q[::-1]);h=fftconvolve(S,g);diff=I[:,None]-I[None,:];G=g[2*L+diff];H=h[3*L+diff];c=g[2*L+I];cross=np.ones((NT,1))*c[None,:];HG=np.block([[BT-ku*np.eye(NT),cross],[cross.T,H]]);GG=block_diag(np.eye(NT),G);kp=-eigh(HG,GG,eigvals_only=True,subset_by_index=[0,0])[0]
 C=np.zeros((NT,len(I)));C[:,L]=1;WF=np.block([[BT,C],[C.T,BU]]);kf=-eigh(WF,eigvals_only=True,subset_by_index=[0,0])[0]
 rec=dict(NT=NT,L=L,kT=kt,kU=ku,kFullW1=kf,localizedIsGround=bool(abs(kf-ku)<1e-7),Kproduct=kp,upper=kt+2*L);print(rec,flush=True);out.append(rec)
open(str(Path(__file__).resolve().parent / 'implant_check.json'),'w').write(json.dumps(out,indent=2))
