from collections import Counter
import numpy as np, sympy as sp, json
from pathlib import Path

def label(v):
 t=tuple(sorted((x for x in v if x),reverse=True))
 return {():0,(1,-1):1,(2,-2):2,(2,-1,-1):3,(1,1,-2):3,(1,1,-1,-1):4}.get(t,-1)
def counts(r):
 reps=[[],[1,-1],[2,-2],[2,-1,-1],[1,1,-1,-1]]
 ns=[1,r*(r-1),r*(r-1),r*(r-1)*(r-2),r*(r-1)*(r-2)*(r-3)//4]
 Q=[]
 for a in reps:
  v=a+[0]*(r-len(a));row=[0]*5
  for i in range(r):
   for j in range(r):
    if i==j:continue
    w=v.copy();w[i]+=1;w[j]-=1;t=label(w)
    if t>=0:row[t]+=1
  Q.append(row)
 assert all(ns[i]*Q[i][j]==ns[j]*Q[j][i] for i in range(5)for j in range(5))
 return ns,Q
x=sp.symbols('r',positive=True,integer=True)
qs=[counts(r)[1] for r in range(5,10)]
Q=sp.Matrix(5,5,lambda i,j: sp.expand(sp.interpolate([(r,qs[r-5][i][j])for r in range(5,10)],x)))
assert all(sp.degree(Q[i,j],x)<=2 for i in range(5) for j in range(5) if Q[i,j]!=0)
assert Q.subs(x,4)==sp.Matrix(counts(4)[1])
print(Q)
print('Punctured characteristic polynomial:',sp.factor(Q[1:,1:].charpoly().as_expr()))
print('Punctured leading determinants:',[sp.factor(Q[1:k,1:k].det()) for k in range(2,6)])
for r in [5,10,20,100,1000]:
 ns,q=counts(r) if r<100 else ([1,r*(r-1),r*(r-1),r*(r-1)*(r-2),r*(r-1)*(r-2)*(r-3)//4],np.array(Q.subs(x,r)).astype(float))
 M=np.sqrt(np.array(ns))[:,None]*np.array(q,dtype=float)/np.sqrt(np.array(ns))[None,:]
 lam,vec=np.linalg.eigh(M[1:,1:]);mass=sum(vec[0,lam<=0]**2)
 print(r,'Jmin',lam[0],'mass',mass,'fullK',-np.linalg.eigvalsh(M)[0])
