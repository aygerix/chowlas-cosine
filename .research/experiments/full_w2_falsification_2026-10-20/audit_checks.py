from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent
"""Independent finite checks of the five existing analytic claims, not a search."""
import itertools,json
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
P=Path(__file__).parent

def one(S):
 S=set(S);W=sorted({0}|S|{a+b for a in S for b in S})
 B=np.array([[int(u-v in S) for v in W] for u in W]);e=eigvalsh(B)
 return W,B,-e[0],e[-1]
res={}
Ss=[{-1,1},{-2,-1,1,2},{-3,-1,1,3}]
checks=[]
for S1,S2 in itertools.product(Ss,Ss):
 W1,B1,K1,r1=one(S1);W2,B2,K2,r2=one(S2)
 U=set(itertools.product(S1|{0},S2|{0}))-{(0,0)}
 W=sorted(set(itertools.product(W1,W2)))
 B=np.array([[int((u[0]-v[0],u[1]-v[1]) in U) for v in W] for u in W])
 assert np.array_equal(np.eye(len(W))+B,np.kron(np.eye(len(W1))+B1,np.eye(len(W2))+B2))
 K=-eigvalsh(B,subset_by_index=[0,0])[0];formula=1+max((K1-1)*(1+r2),(K2-1)*(1+r1))
 assert abs(K-formula)<1e-10
 checks.append(dict(Ns=[len(S1),len(S2)],K=K,formula=formula))
res['heterogeneous_unitized']=checks
checks=[]
for S1,S2 in itertools.product(Ss,Ss):
 U=set(itertools.product(S1,S2));T1={a+b for a in S1 for b in S1};T2={a+b for a in S2 for b in S2}
 W=sorted(U|set(itertools.product(T1,T2)))
 B=np.array([[int((u[0]-v[0],u[1]-v[1]) in U) for v in W] for u in W])
 K=-eigvalsh(B,subset_by_index=[0,0])[0];N=len(U)
 leaf=np.sqrt(N-len(S1&T1)*len(S2&T2));assert K>=leaf-1e-10
 if S1<=T1 and S2<=T2:
  _,B1,K1,r1=one(S1);_,B2,K2,r2=one(S2)
  assert np.array_equal(B,np.kron(B1,B2));assert abs(K-max(K1*r2,K2*r1))<1e-10
 checks.append(dict(Ns=[len(S1),len(S2)],K=K,leaf_bound=float(leaf)))
res['categorical']=checks
checks=[]
c=np.sqrt((np.sqrt(2)-1)/(np.sqrt(2)+5))
for L in range(1,101):
 k=(L+2)//3;d=L-k+1
 blocks=[list(range(s,s+k)) for s in [-d,0,d]]
 assert min(blocks[0])>=-L and max(blocks[-1])<=L
 assert all(0<abs(a-b)<=L for block in blocks for a in block for b in block if a!=b)
 assert all(abs(a-b)<=L for i in [0,1] for a in blocks[i] for b in blocks[i+1])
 assert all(abs(a-b)>L for a in blocks[0] for b in blocks[2])
res['axis_block_lengths_checked']=[1,100];res['axis_constant']=float(c)
checks=[]
for b in [2,3,4,6,8,9,10]:
 R=[r for r in range(1,13) if r%b];H=0
 while b**(H+1)<=2*max(R):H+=1
 S={sgn*r*b**j for sgn in [-1,1] for r in R for j in range(4)}
 ex={sgn*r*b**j:j for sgn in [-1,1] for r in R for j in range(4)}
 deg=max(sum(u-v in S for v in S) for u in S)
 assert all(abs(ex[u]-ex[v])<=H for u in S for v in S if u-v in S)
 bound=2*len(R)*(2*H+1);assert deg<=bound
 checks.append(dict(base=b,N=len(S),H=H,maximum_degree=deg,bound=bound))
res['composite_orbits']=checks
S={-2,-1,1,2};W,B,K,rho=one(S);checks=[]
for h in [0,1,2,3]:
 q=5*h+1;Sp={q*s+r for s in S for r in range(-h,h+1)}
 Wp,Bp,Kp,rp=one(Sp);mapped=[q*w+r for w in W for r in range(-2*h,2*h+1)]
 assert Wp==mapped
 T=np.array([[int(abs(r-t)<=h) for t in range(-2*h,2*h+1)] for r in range(-2*h,2*h+1)])
 assert np.array_equal(Bp,np.kron(B,T));et=eigvalsh(T)
 exact=max(K*et[-1],rho*(-et[0]));assert abs(Kp-exact)<1e-10
 checks.append(dict(h=h,K=Kp,formula=exact))
res['interval_fibers']=checks
(P/'audit_checks.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
