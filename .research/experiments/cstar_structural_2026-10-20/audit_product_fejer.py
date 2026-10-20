from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
from itertools import product
from fractions import Fraction as F
from collections import Counter
import random
rng=random.Random(120)
for d in [1,2,3]:
 U=list(product(range(-2,3),repeat=d));zero=(0,)*d;pos=[s for s in U if s>zero]
 idx={a:i for i,a in enumerate(pos)}
 def key(s):
  if s==zero or s not in US:return None
  return idx[s if s>zero else tuple(-x for x in s)]
 US=set(U);actual=Counter();pred=Counter()
 for s in U:
  for t in U:
   v=tuple(a-b for a,b in zip(s,t));ks=[key(s),key(t),key(v)]
   if None not in ks:actual[tuple(sorted(ks))]+=1
 for ia,a in enumerate(pos):
  for ib in range(ia+1,len(pos)):
   b=pos[ib];c=tuple(x+y for x,y in zip(a,b))
   if c in US:pred[tuple(sorted([ia,ib,idx[c]]))]+=12
  aa=tuple(2*x for x in a)
  if aa in US:pred[tuple(sorted([ia,ia,idx[aa]]))]+=6
 assert actual==pred,(d,actual-pred,pred-actual)
 print('EXACT_CUBIC',d,'signclasses',len(pos),'monomials',len(actual),'totalordered',sum(actual.values()))
 for t in U:
  if t==zero:continue
  edgecounter=Counter();degrees=Counter()
  for s in U:
   u=tuple(x-y for x,y in zip(t,s))
   if s==zero or u==zero or u not in US or s==u:continue
   a,b=key(s),key(u)
   assert a!=b
   edgecounter[tuple(sorted([a,b]))]+=1
  assert all(v==2 for v in edgecounter.values())
  for a,b in edgecounter:degrees[a]+=1;degrees[b]+=1
  assert max(degrees.values(),default=0)<=2
 print('EXACT_FILL_GRAPH',d,'targets',len(U)-1)
