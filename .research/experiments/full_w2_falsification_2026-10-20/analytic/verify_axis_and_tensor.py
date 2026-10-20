from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
"""Independent dense checks of full W1 axis certificates and exact tensor identities."""
import itertools,json
import numpy as np
from pathlib import Path
out=[]
c=np.sqrt((np.sqrt(2)-1)/(np.sqrt(2)+5))
for lengths in [(1,),(2,),(5,),(1,1,1),(2,3),(1,2,4),(2,2,2,2),(1,1,1,8)]:
 J=len(lengths);S=set()
 for j,L in enumerate(lengths):
  for t in range(-L,L+1):
   if t:
    a=[0]*J;a[j]=t;S.add(tuple(a))
 W=sorted(S|{(0,)*J});B=np.array([[int(tuple(a-b for a,b in zip(u,v)) in S) for v in W]for u in W]);K=-np.linalg.eigvalsh(B)[0];N=len(S)
 assert K>=c*np.sqrt(N)-1e-10
 out.append(dict(lengths=lengths,N=N,K_W1=float(K),ratio=float(K/np.sqrt(N)),proved_lower=float(c*np.sqrt(N))))
print(json.dumps(out,indent=2))
Path(__file__).with_name('axis_sanity.json').write_text(json.dumps(out,indent=2))
