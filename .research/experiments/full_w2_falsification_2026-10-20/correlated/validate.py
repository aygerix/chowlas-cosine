from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from scipy.linalg import eigvalsh
from lifts import support,evaluate
results=[]
for label,S in [('balanced_q31',support(31,6,'random')),('Singer_p5',np.array([x-y for x in [0,1,3,8,12,18] for y in [0,1,3,8,12,18] if x!=y]))]:
 # The handwritten p5 set is used solely to validate numerical construction.
 S=np.unique(S);W=np.unique(np.r_[0,S,(S[:,None]+S[None,:]).ravel()]);B=np.isin(W[:,None]-W[None,:],S).astype(float);K=-eigvalsh(B,subset_by_index=[0,0])[0];r=evaluate(S,label);r['dense_K']=K;r['dense_error']=abs(K-r['K']);assert r['dense_error']<1e-8;assert len(W)==r['W2'];results.append(r)
open(str(ARCHIVE_ROOT / 'correlated/validation.json'),'w').write(json.dumps(results,indent=2))
