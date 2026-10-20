from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,scipy.linalg as la, json,time
rng=np.random.default_rng(6526)
def calc(A):
 S=set(A)|{-a for a in A};W=sorted({0}|S|{a+b for a in S for b in S});w=np.array(W)
 H=np.isin(w[:,None]-w, list(S)).astype(float)
 k=-la.eigh(H,subset_by_index=[0,0],check_finite=False,eigvals_only=True)[0]
 return len(S)/(k*k),k,len(W)
best=(0,None)
for X,n,steps in [(24,8,1200),(48,12,1200),(80,16,1000),(160,12,600),(1000,10,400)]:
 A=set(rng.choice(np.arange(1,X+1),n,replace=False));score,k,ws=calc(A)
 for i in range(steps):
  old=int(rng.choice(list(A)));new=int(rng.integers(1,X+1))
  if new in A:continue
  B=(A-{old})|{new};sc,k,w=calc(B);temp=.03*(1-i/steps)+.001
  if sc>score or rng.random()<np.exp((sc-score)/temp):A=B;score=sc
  if sc>best[0]:
   best=(sc,sorted(B));print(json.dumps(dict(X=X,n=n,step=i,ratio=sc,K=k,W=w,A=list(map(int,sorted(B))))),flush=True)
 print('DONE',X,n,score,flush=True)
