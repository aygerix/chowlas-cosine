from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import itertools, math, functools,json
from fractions import Fraction as F
from collections import defaultdict
@functools.lru_cache(None)
def parts(n):
 if n==0:return ((),)
 ans=[]
 for p in parts(n-1):
  ans.append(p+((n-1,),))
  for j in range(len(p)):ans.append(p[:j]+(p[j]+(n-1,),)+p[j+1:])
 return tuple(ans)
@functools.lru_cache(None)
def stir(n,r):return int(n==r==0) if n==0 or r==0 else r*stir(n-1,r)+stir(n-1,r-1)
@functools.lru_cache(None)
def scalar(key):
 total=0
 for xs in itertools.product(range(-2,3),repeat=len(key)):
  if sum(x*t[0] for x,t in zip(xs,key)):continue
  z=math.prod((3-abs(x))**t[2] for x,t in zip(xs,key))
  total+=z*(-1 if sum(x*t[1] for x,t in zip(xs,key))%2 else 1)
 return F(total,3**sum(t[2] for t in key))
@functools.lru_cache(None)
def full(a,b):
 n=a+b;ans=defaultdict(int)
 if not n:return {F(1):1}
 for p in parts(n):
  opts=[]
  for block in p:
   op=[];l=len(block)
   for rest in itertools.product([-1,1],repeat=l-1):
    signs=(1,)+rest;c=sum(signs);h=sum(s for i,s in zip(block,signs) if i>=a)%2
    for r in range(1,l+1):op.append(((c,h,r),(-1)**(r-1)*math.factorial(r-1)*stir(l,r)))
   opts.append(op)
  for combo in itertools.product(*opts):
   key=tuple(sorted(t[0] for t in combo));ans[scalar(key)]+=math.prod(t[1] for t in combo)
 return {k:v for k,v in ans.items() if v}
def actual(a,b):
 out=defaultdict(int)
 for i in range(a+1):
  for j in range(b+1):
   coeff=math.comb(a,i)*math.comb(b,j)*(-1)**(a+b-i-j)
   for x,v in full(i,j).items():out[x]+=coeff*v
 return {x:v for x,v in out.items() if v}
if __name__=='__main__':
 out={}
 for a in [1,2,3]:
  terms=actual(a,2);ts=sorted(terms.items(),reverse=True)
  print(a,[(str(x),v) for x,v in ts],flush=True)
  out[str(a)]=[(str(x),v) for x,v in ts]
 open(str(HERE / 'parity_mixed_expectation.json'),'w').write(json.dumps(out,indent=2))
