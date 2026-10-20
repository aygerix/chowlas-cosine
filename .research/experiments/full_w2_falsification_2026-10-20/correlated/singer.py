from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from lifts import evaluate

def singer(p):
 a,b=next((a,b) for a in range(p) for b in range(1,p) if all((x**3+a*x+b)%p for x in range(p)))
 def mul(x,y):
  z=[0]*5
  for i in range(3):
   for j in range(3):z[i+j]+=x[i]*y[j]
  for k in [4,3]:z[k-3]-=b*z[k];z[k-2]-=a*z[k]
  return tuple(v%p for v in z[:3])
 def power(x,n):
  r=(1,0,0)
  while n:
   if n&1:r=mul(r,x)
   x=mul(x,x);n//=2
  return r
 order=p**3-1;fac=[];n=order
 for k in range(2,order+1):
  if k*k>n:break
  if n%k==0:
   fac.append(k)
   while n%k==0:n//=k
 if n>1:fac.append(n)
 alpha=next((i%p,(i//p)%p,i//p**2) for i in range(2,p**3) if all(power((i%p,(i//p)%p,i//p**2),order//f)!=(1,0,0) for f in fac))
 q=p*p+p+1;z=(1,0,0);T=[]
 for k in range(q):
  zp=power(z,p);zp2=power(zp,p);tr=tuple((z[i]+zp[i]+zp2[i])%p for i in range(3))
  if tr==(0,0,0):T.append(k)
  z=mul(z,alpha)
 assert len(T)==p+1
 S=np.array([x-y for x in T for y in T if x!=y]);assert len(set(S%q))==q-1
 return q,T,S
out=[]
for p in [2,3,5,7,11,17,23,31,47,61,89]:
 q,T,S=singer(p);r=evaluate(S,f'Singer_p{p}_q{q}');r['T']=T;r['global_K_upper']=p+1;out.append(r)
 open(str(ARCHIVE_ROOT / 'correlated/singer_results.json'),'w').write(json.dumps(out,indent=2))
