from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,itertools,json
best=[(1e9,None) for _ in range(4)]
for mask in range(1,1<<14):
 A=np.array([a+1 for a in range(14) if mask>>a&1]); n=len(A)
 C=np.isin(abs(A[:,None]-A),A).astype(float)-np.isin(A[:,None]+A,A)
 f2=np.sum(C*C)
 if not f2:continue
 lam=np.linalg.eigvalsh(C); neg=lam[lam<0]; k=-lam[0]
 w=1./A
 assert abs(w@C@w)<1e-10
 vals=[k/np.sqrt(f2/n),sum(neg**2)/f2, -((1./A**2)@C@(1./A**2))/sum(1./A**4)/k, sum(-neg)/np.sqrt(f2)]
 for j,v in enumerate(vals):
  if v<best[j][0]:best[j]=(v,A.tolist())
print(best)
