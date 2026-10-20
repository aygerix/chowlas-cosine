from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,json
from scipy.linalg import eigh
mins=(1e9,None);maxcost=(-1e9,None);worst=(0,None)
for mask in range(1,2**13):
 A=np.array([i+1 for i in range(13)if mask>>i&1]);S=np.r_[-A,A];I=np.r_[0,S];N=len(S);B=np.isin(I[:,None]-I[None,:],S).astype(float);lam,u=eigh(B,subset_by_index=[0,0]);K=-lam[0];u=u[:,0]
 W=np.unique(np.r_[I,(S[:,None]+S).ravel()]);J=np.setdiff1d(W,I);C=np.isin(J[:,None]-I[None,:],S).astype(float);g=C@u;a=g@g
 if a<1e-10:continue
 cost=K+g@np.isin(J[:,None]-J[None,:],S)@g/a;newK=K+(np.sqrt(cost**2+4*a)-cost)/2;ratio=N/newK**2
 if ratio>worst[0]:worst=(ratio,A.tolist(),K,a/N,cost/np.sqrt(N))
 if N/K**2>2:
  if a/N<mins[0]:mins=(a/N,A.tolist(),N/K**2,cost/np.sqrt(N))
  if cost/np.sqrt(N)>maxcost[0]:maxcost=(cost/np.sqrt(N),A.tolist(),N/K**2,a/N)
print('worst scalar extension',worst);print('min leakage with ratio>2',mins);print('max cost with ratio>2',maxcost)
