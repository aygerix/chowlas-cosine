from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import itertools, numpy as np
from scipy.sparse.linalg import eigsh
for r,k in [(6,2),(8,2),(10,2),(7,3),(8,3)]:
 v=[]
 for p in itertools.combinations(range(r),k):
  for q in itertools.combinations([i for i in range(r) if i not in p],k):
   x=np.zeros(r,dtype=np.int8); x[list(p)]=1;x[list(q)]=-1;v.append(x)
 v=np.array(v);n=len(v);B=np.zeros((n,n),dtype=float)
 for i,x in enumerate(v):
  delta=v-x;B[i]=((abs(delta).max(axis=1)<=1)&((delta==1).sum(axis=1)==k)&((delta==-1).sum(axis=1)==k))
 low=eigsh(B,k=1,which='SA',return_eigenvectors=False)[0];deg=B[0].sum();root=(deg-np.sqrt(deg*deg+4*n))/2;cost=max(-low,-root)
 print(r,k,n,deg,low,root,n/cost**2,flush=True)
