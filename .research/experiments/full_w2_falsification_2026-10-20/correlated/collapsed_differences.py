from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from lifts import evaluate
rng=np.random.default_rng(888731);out=[]
for m in [16,32,64]:
 for lam in [1,.25,1/np.sqrt(m)]:
  X=round(m*m/lam);T=np.sort(rng.choice(X,m,replace=False));diff=(T[:,None]-T[None,:]).ravel();S=np.unique(diff);S=S[S!=0];r=evaluate(S,f'collapsed_m{m}_lambda{lam:.6g}_X{X}');r.update(T=T.tolist(),m=m,X=X,collision_excess=int(m*(m-1)-len(S)),lambda_=lam);out.append(r)
  open(str(ARCHIVE_ROOT / 'correlated/collapsed_results.json'),'w').write(json.dumps(out,indent=2))
