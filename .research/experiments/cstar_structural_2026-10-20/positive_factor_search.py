from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,itertools,json
from scipy.optimize import least_squares
out=[]
for L in range(2,10):
 for mask in range(1<<(L-1)):
  B=np.array([0]+[j for j in range(1,L) if mask>>(j-1)&1]+[L]);m=len(B);A=sorted(set(int(y-x) for x in B for y in B if y>x));pairs=[np.array([(i,j) for i,x in enumerate(B) for j,y in enumerate(B) if y-x==a]) for a in A]
  def fun(q):return np.array([sum(q[i]*q[j] for i,j in ps)-1 for ps in pairs])
  def jac(q):
   z=np.zeros((len(A),m))
   for k,ps in enumerate(pairs):
    for i,j in ps:z[k,i]+=q[j];z[k,j]+=q[i]
   return z
  q=np.ones(m)
  for lam in [.01,.0001]:
   r=least_squares(lambda x:np.r_[fun(x),np.sqrt(lam)*x],q,jac=lambda x:np.r_[jac(x),np.sqrt(lam)*np.eye(m)],bounds=(1e-10,np.inf),max_nfev=100,ftol=1e-10,gtol=1e-10,xtol=1e-10);q=r.x
  r=least_squares(fun,q,jac=jac,bounds=(1e-10,np.inf),max_nfev=200,gtol=1e-12,ftol=1e-12,xtol=1e-12);q=r.x
  if np.max(abs(fun(q)))<1e-7 and min(q)>1e-6:
   K=float(q@q);out.append(dict(B=B.tolist(),q=q.tolist(),K=K,ratio=K/m,N=2*len(A),residual=float(np.max(abs(fun(q))))))
 best=min(out,key=lambda x:x['ratio']);print(L,len(out),best,flush=True)
open(str(HERE / 'positive_factor_search.json'),'w').write(json.dumps(out,indent=2))
