from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,itertools,json
from fractions import Fraction
from parity_mixed_expectation import actual
out=[]
for d in [1,2]:
 U=list(itertools.product(range(-2,3),repeat=d));half=[s for s in U if s>tuple(-x for x in s)];den=3**d;weights=[np.prod([3-abs(x) for x in s]).item() for s in half];acc=[0,0,0];shape=(11,)*d
 for mask in range(1<<len(half)):
  prob=1;D=np.zeros(shape);Q=np.zeros(shape)
  for i,(s,w) in enumerate(zip(half,weights)):
   on=(mask>>i)&1;prob*=w if on else den-w
   if on:
    for t in [s,tuple(-x for x in s)]:D[tuple(x%11 for x in t)]=1;Q[tuple(x%11 for x in t)]=(-1)**sum(t)
  f=np.fft.fftn(D).real;g=np.fft.fftn(Q).real
  for a in [1,2,3]:acc[a-1]+=prob*round(np.mean(f**a*g*g))
 got=[Fraction(x,den**len(half)) for x in acc];expect=[sum(c*x**d for x,c in actual(a,2).items()) for a in [1,2,3]]
 assert got==expect,(d,got,expect)
 out.append(dict(d=d,sets=1<<len(half),moments=list(map(str,got))));print(out[-1],flush=True)
open(str(HERE / 'verify_parity_moments.json'),'w').write(json.dumps(out,indent=2))
