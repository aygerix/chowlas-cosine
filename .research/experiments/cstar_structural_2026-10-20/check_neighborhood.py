from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np
best=(0,None,None)
for mask in range(1,2**13):
 a=np.array([i+1 for i in range(13) if mask>>i&1]); s=np.r_[-a,0,a]; adj=np.isin(s[:,None]-s[None,:],np.r_[-a,a]).astype(float)
 k=-np.linalg.eigvalsh(adj)[0]; ratio=2*len(a)/k**2
 if ratio>best[0]:best=(ratio,a.tolist(),k)
print(best)
for m in [5,9,17,33]:
 R=(np.arange(m)[:,None]>=np.arange(1,m)).astype(float); P=np.eye(m)-np.ones((m,m))/m; Q=np.eye(m-1)-np.ones((m-1,m-1))/(m-1)
 sigma=np.linalg.svd(P@np.c_[R,1-R]@np.kron(np.eye(2),Q),compute_uv=False)[0]
 print(m,sigma,sigma/m)
