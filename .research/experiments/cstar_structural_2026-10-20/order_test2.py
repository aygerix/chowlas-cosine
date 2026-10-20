from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np
rng=np.random.default_rng(83)
best=[(0,None) for _ in range(3)]
for z in range(12000):
 X=int(rng.integers(12,130)); A=np.flatnonzero(rng.random(X)<rng.uniform(.08,.95))+1
 if len(A)==0:continue
 C=np.isin(abs(A[:,None]-A),A).astype(float)-np.isin(A[:,None]+A,A)
 lam=np.linalg.eigvalsh(C); k=-lam[0]; f2=sum(lam*lam)
 if k<1e-9:continue
 vals=[lam[-1]/k,f2/(len(A)*k*k),sum(lam**3)/(f2**1.5)]
 for j,v in enumerate(vals):
  if v>best[j][0]:best[j]=(float(v),A.tolist())
print(best)
