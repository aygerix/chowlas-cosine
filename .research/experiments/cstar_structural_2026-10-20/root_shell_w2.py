from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,itertools,time,json
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
out=[]
for r,k in [(4,1),(6,1),(8,1),(6,2),(7,2),(8,2),(6,3),(7,3),(8,3)]:
 t=time.time();powers=7**np.arange(r,dtype=np.int64);s=[]
 for p in itertools.combinations(range(r),k):
  for q in itertools.combinations([i for i in range(r)if i not in p],k):s.append(powers[list(p)].sum()-powers[list(q)].sum())
 S=np.array(sorted(s));W=np.unique(np.r_[0,S,(S[:,None]+S).ravel()]);N=len(W);rows=[];cols=[]
 print('building',r,k,len(S),N,flush=True)
 for s in S:
  idx=np.searchsorted(W,W+s);valid=idx<N;ii=np.flatnonzero(valid);ii=ii[W[idx[ii]]==W[ii]+s];rows.append(ii);cols.append(idx[ii])
 rr=np.concatenate(rows);cc=np.concatenate(cols);B=csr_matrix((np.ones(len(rr)),(rr,cc)),shape=(N,N));val,vec=eigsh(B,k=1,which='SA',tol=1e-8,ncv=40,maxiter=2000);K=-val[0];rec=dict(r=r,k=k,n=len(S),W2=N,edges=int(B.nnz),K=float(K),ratio=float(len(S)/K**2),residual=float(np.linalg.norm(B@vec[:,0]-val[0]*vec[:,0])),seconds=time.time()-t);print(rec,flush=True);out.append(rec)
 open(str(HERE / 'root_shell_w2.json'),'w').write(json.dumps(out,indent=2))
