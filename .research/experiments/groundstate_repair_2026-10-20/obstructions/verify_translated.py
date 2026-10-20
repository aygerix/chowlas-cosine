from pathlib import Path
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from scipy.linalg import eigh
from scipy.signal import fftconvolve
rng=np.random.default_rng(20261020);target=32;alpha=target**(-1/3);X=round(target/alpha);a=np.arange(1,X+1);A=a[rng.random(X)<2*alpha*(1-a/X)];S=set(map(int,np.r_[-A,A]));I=np.array(sorted(S|{0}));W=np.array(sorted(S|{0}|{s+t for s in S for t in S}));B=np.array([[int(int(i-j) in S) for j in I] for i in I]);val,v=eigh(B,subset_by_index=[0,0]);q=v[:,0];Q=dict(zip(I,q));F=np.array([[Q.get(int(w-i),0.) for i in I] for w in W]);BW=np.array([[int(int(i-j) in S) for j in W] for i in W]);G=F.T@F;H=F.T@BW@F
m=max(A);qc=np.zeros(2*m+1);qc[m+I]=q;d=np.zeros(2*m+1);d[m+np.array(sorted(S))]=1;gamma=fftconvolve(qc,qc[::-1]);h=fftconvolve(d,gamma);diff=I[:,None]-I[None,:];result=dict(n=len(A),W2=len(W),GramMaxError=float(np.max(abs(G-gamma[2*m+diff]))),CostMaxError=float(np.max(abs(H-h[3*m+diff]))),Ktranslated=float(-eigh(H,G,eigvals_only=True,subset_by_index=[0,0])[0]),Kfull=float(-eigh(BW,eigvals_only=True,subset_by_index=[0,0])[0]))
print(result);open(str(Path(__file__).resolve().parent / 'verification.json'),'w').write(json.dumps(result,indent=2))
