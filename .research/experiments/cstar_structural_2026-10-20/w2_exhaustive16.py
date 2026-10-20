from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np, scipy.linalg as la,json,time
X=16;best=(0,None);t=__import__('time').time()
for mask in range(1,1<<X):
 A=[j+1 for j in range(X) if mask>>j&1];S=set(A)|{-a for a in A};W=sorted({0}|S|{a+b for a in S for b in S});w=np.array(W)
 H=np.isin(w[:,None]-w,list(S)).astype(float);k=-la.eigh(H,subset_by_index=[0,0],check_finite=False,eigvals_only=True)[0];rho=len(S)/k**2
 if rho>best[0]:best=(rho,A);print(json.dumps(dict(mask=mask,A=A,rho=rho,K=k,W=len(W))),flush=True)
print('DONE',2**X-1,time.time()-t,flush=True)
