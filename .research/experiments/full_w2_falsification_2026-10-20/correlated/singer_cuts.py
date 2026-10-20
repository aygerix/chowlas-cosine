from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from lifts import evaluate
out=[]
source=json.load(open(str(ARCHIVE_ROOT / 'correlated/singer_results.json')))
for rec in source:
 p=int(rec['tag'].split('_')[1][1:]);q=p*p+p+1
 if p not in [7,11,17,23,31]:continue
 T=np.array(rec['T']);best=None
 for i,t in enumerate(T):
  U=(T-t)%q;S=np.array([x-y for x in U for y in U if x!=y]);r=evaluate(S,f'Singer_p{p}_cut{i}')
  if best is None or r['K']<best['K']:best=r;best['T']=U.tolist()
 out.append(best);open(str(ARCHIVE_ROOT / 'correlated/singer_cuts_results.json'),'w').write(json.dumps(out,indent=2))
