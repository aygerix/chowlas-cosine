from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np
rng=np.random.default_rng(42);best=(-1,None)
for mask in range(1,1<<12):
 A=np.array([a+1 for a in range(12) if mask>>a&1]); C=np.isin(abs(A[:,None]-A),A).astype(float)-np.isin(A[:,None]+A,A);w=1./A; v=C@w
 if v@v<1e-10:continue
 r=(v@C@v)/(v@v)
 if r>best[0]:best=(float(r),A.tolist())
print(best)
