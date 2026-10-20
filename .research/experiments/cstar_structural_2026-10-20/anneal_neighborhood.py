from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np, math, json
rng=np.random.default_rng(493); out=[]
for X in [20,35,60]:
 best=(0,[],0)
 for restart in range(5):
  mask=rng.random(X)<.35
  def score(mask):
   a=np.flatnonzero(mask)+1; s=np.r_[-a,0,a]; B=np.isin(s[:,None]-s[None,:],np.r_[-a,a]); k=-np.linalg.eigvalsh(B.astype(float))[0]; return (2*len(a)/k**2,k)
  val,k=score(mask)
  for step in range(2500):
   j=rng.integers(X); mask[j]=~mask[j]; v,kk=score(mask); t=.12*(1-step/2500)+.004
   if v>val or rng.random()<math.exp(max(-700,(v-val)/t)): val,k=v,kk
   else:mask[j]=~mask[j]
   if val>best[0]:best=(val,(np.flatnonzero(mask)+1).tolist(),k)
 print(X,best,flush=True);out.append((X,best))
open(str(HERE / 'neighborhood_search.json'),'w').write(json.dumps(out))
