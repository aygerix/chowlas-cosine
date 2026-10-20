from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import json,math
A=list(range(1,19))+list(range(20,38))+[39,40,41,42,47,48,50,52,57,61,62,64,65,68]
def odd(a):
 a=abs(a)
 while a and a%2==0:a//=2
 return a
O=sorted(set(map(odd,A)));R=max(O);D=int(math.floor(math.log2(2*R)))
deg={}
for r in O:
 u=r*2**D;cnt=0
 for s in O:
  for sign in [-1,1]:
   for delta in range(-D,D+1):
    v=sign*s*2**(D+delta);diff=u-v
    if diff and odd(diff) in O:cnt+=1
 deg[r]=cnt
rec=dict(odd_seed=O,R=R,exponent_span=D,bulk_degrees=deg,exact_uniform_degree_bound=max(deg.values()),bulk_average_degree=sum(deg.values())/len(O))
print(json.dumps(rec,indent=2));open(str(ARCHIVE_ROOT / 'multiscale/dyadic_degree.json'),'w').write(json.dumps(rec,indent=2))
