#!/usr/bin/env python3
"""Independent exact-entry checks of exterior decomposition and W1 bound."""
from itertools import product,combinations
from pathlib import Path
import json, math
import numpy as np
from scipy.linalg import eigvalsh

def build(A,m):
 T=sorted(set(A)|{-a for a in A});S=set()
 for j in range(m):
  for t in T:
   x=[0]*m;x[j]=t;S.add(tuple(x))
 I=S|{(0,)*m};W={tuple(a+b for a,b in zip(x,y)) for x in I for y in I};E=sorted(W-I)
 def cls(x):
  support=tuple(j for j,t in enumerate(x) if t)
  return support
 B=np.array([[tuple(a-b for a,b in zip(x,y)) in S for y in E]for x in E],int)
 # No cross-components, and each diagonal block has the asserted entries.
 for a,x in enumerate(E):
  for b,y in enumerate(E):
   cx,cy=cls(x),cls(y)
   expected=0
   if cx==cy:
    if len(cx)==1: expected=int(x[cx[0]]-y[cx[0]] in T)
    else:
     i,j=cx
     expected=int(x[i]==y[i] and x[j]-y[j] in T)+int(x[j]==y[j] and x[i]-y[i] in T)
   assert B[a,b]==expected,(A,m,x,y)
 C=np.array([[x-y in T for y in T]for x in T],int)
 IT=T+[0];ET=sorted({x+y for x in IT for y in IT}-set(IT));BE=np.array([[x-y in T for y in ET]for x in ET],int)
 kC=-eigvalsh(C,subset_by_index=[0,0])[0]
 kET=-eigvalsh(BE,subset_by_index=[0,0])[0] if ET else 0
 kE=-eigvalsh(B,subset_by_index=[0,0])[0]
 assert abs(kE-max(kET,2*kC))<1e-8
 # Choose arbitrary positive a, derive actual best scalar e, and verify cone upper bound.
 a=.13;e=-eigvalsh(C-a*np.ones_like(C),subset_by_index=[0,0])[0]
 II=sorted(I);BI=np.array([[tuple(a-b for a,b in zip(x,y)) in S for y in II]for x in II],int)
 kI=-eigvalsh(BI,subset_by_index=[0,0])[0]
 assert kI<=max(e,m/a)+1e-8
 # Integer encoding preserves all W2 entries, including mixed ones.
 X=max(A);Q=10*X+1
 enc=lambda x:sum(v*Q**j for j,v in enumerate(x))
 SS={enc(x)for x in S};WW=sorted(W)
 assert len({enc(x)for x in WW})==len(WW)
 for x in WW:
  for y in WW:
   assert ((enc(x)-enc(y))in SS)==(tuple(a-b for a,b in zip(x,y))in S)
 return dict(A=A,m=m,N=len(S),I=len(I),E=len(E),K_I=float(kI),K_E=float(kE),K_E_formula=float(max(kET,2*kC)),K_C=float(kC),K_E_base=float(kET))

out=[]
for A in ([1],[1,2],[1,3],[1,2,4],[1,3,4],[1,2,3,4],[2,5,9]):
 for m in (2,3):
  out.append(build(list(A),m))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
