from support_io import load_saved_support
from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import numpy as np,json,time
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from pathlib import Path
p=Path(__file__).parent;z=load_saved_support('dyadic_extended_J8');A=z['A'];S=np.r_[A,-A];W=z['W'];exactW=np.unique(np.r_[0,S,(S[:,None]+S).ravel()]);assert np.array_equal(exactW,W)
rows=[];cols=[]
for s in S:
 targets=W+s;j=np.searchsorted(W,targets);ok=j<len(W);i=np.flatnonzero(ok);j=j[ok];eq=W[j]==targets[i];rows.append(i[eq]);cols.append(j[eq])
r=np.concatenate(rows);c=np.concatenate(cols);H=coo_matrix((np.ones(len(r)),(r,c)),shape=(len(W),len(W))).tocsr();val,vec=eigsh(H,k=2,which='SA',tol=2e-10,ncv=50,v0=np.random.default_rng(123).normal(size=len(W)))
rec=dict(tag='dyadic_extended_J8',W=len(W),nnz=H.nnz,smallest_eigenvalues=val.tolist(),FFT_K=float(z['K']),difference=float(-val[0]-z['K']),residuals=[float(np.linalg.norm(H@vec[:,i]-val[i]*vec[:,i])) for i in range(2)])
print(json.dumps(rec,indent=2));(p/'sparse_verification.json').write_text(json.dumps(rec,indent=2))
