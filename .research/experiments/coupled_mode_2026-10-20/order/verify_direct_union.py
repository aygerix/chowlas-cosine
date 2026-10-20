"""Small exact assembly check, not asymptotic evidence or a spectral proof."""
import itertools, json
import numpy as np
from scipy.linalg import eigvalsh

X=8; m=3; A={1,2,3,4,6,7}; T=A|{-a for a in A}; I={0}|T
WT={a+b for a in I for b in I}; ET=WT-I
assert set(range(-X,X+1)) <= WT
z={s:16*int(abs(s) in A)-(X-abs(s)) for s in range(-X+1,X) if s}
S={tuple(s if i==j else 0 for i in range(m)) for j in range(m) for s in T}
o=(0,)*m; IS=S|{o}; W={tuple(x+y for x,y in zip(u,v)) for u in IS for v in IS}; E=W-IS

def mat(rows, SS):
 return np.array([[tuple(a-b for a,b in zip(u,v)) in SS for v in rows] for u in rows],dtype=np.int64)

def scalar(rows):
 return np.array([[u-v in T for v in rows] for u in rows],dtype=np.int64)

rows=sorted(W); B=mat(rows,S)
C=scalar(sorted(T)); BEbase=scalar(sorted(ET))
pred=[]
for j in range(m):pred.extend([('axis',j)]*len(ET))
for i in range(m):
 for j in range(i+1,m):pred.extend([('pair',i,j)]*(len(T)**2))
blocks=[]
for j in range(m):
 blocks.append([tuple(t if k==j else 0 for k in range(m)) for t in sorted(ET)])
for i in range(m):
 for j in range(i+1,m):
  blocks.append([tuple(t if k==i else u if k==j else 0 for k in range(m)) for t in sorted(T) for u in sorted(T)])
erows=sum(blocks,[]); BE=mat(erows,S); offset=0; maxoff=0
for k,block in enumerate(blocks):
 n=len(block); expected=BEbase if k<m else np.kron(C,np.eye(len(T),dtype=np.int64))+np.kron(np.eye(len(T),dtype=np.int64),C)
 assert np.array_equal(BE[offset:offset+n,offset:offset+n],expected)
 assert not np.any(BE[offset:offset+n,:offset]); assert not np.any(BE[offset:offset+n,offset+n:]); offset+=n
assert set(erows)==E and len(erows)==len(E)
Q=5*X+2
encoded={sum(x*Q**i for i,x in enumerate(s)) for s in S}
e_rows=[sum(x*Q**i for i,x in enumerate(u)) for u in rows]
assert len(set(e_rows))==len(rows)
assert np.array_equal(B,np.array([[u-v in encoded for v in e_rows] for u in e_rows],dtype=np.int64))

h=np.zeros(len(rows),dtype=np.int64)
for r,u in enumerate(rows):
 nz=[i for i,x in enumerate(u) if x]
 if len(nz)==1 and u[nz[0]] in z:h[r]=z[u[nz[0]]]
e0=np.array([u==o for u in rows],dtype=np.int64)
zrows=sorted(z); zvec=np.array([z[t] for t in zrows],dtype=np.int64)
V=int(zvec@zvec); c=sum(z[t] for t in T); R=int(zvec@scalar(zrows)@zvec)
assert int(h@h)==m*V
assert int(e0@B@h)==m*c
assert int(h@B@h)==m*R
assert int(e0@h)==0
result={'X':X,'m':m,'A':sorted(A),'N':len(S),'W2_rows':len(W),'E_rows':len(E),'integer_base':Q,'exact_exterior_blocks':len(blocks),'integer_Z_norm2':V,'integer_DZ':c,'integer_DZ2':R,'normalized_compression':[[0,float(np.sqrt(m)*c/np.sqrt(V))],[float(np.sqrt(m)*c/np.sqrt(V)),float(R/V)]],'K_W1':float(-eigvalsh(mat(sorted(IS),S),subset_by_index=[0,0])[0]),'K_E':float(-eigvalsh(BE,subset_by_index=[0,0])[0]),'K_W2':float(-eigvalsh(B,subset_by_index=[0,0])[0]),'note':'Matrix identities above checked with integers; eigenvalues here are floating diagnostics only.'}
print(json.dumps(result,indent=2))
