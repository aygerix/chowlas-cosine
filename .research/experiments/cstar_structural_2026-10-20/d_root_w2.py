from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
exec(open(str(HERE / 'root_shell_w2.py')).read().split('for r,k in ')[0])
for r in [4,6,8,10]:
 t=time.time();powers=7**np.arange(r,dtype=np.int64);S=np.array(sorted({a*powers[i]+b*powers[j] for i in range(r)for j in range(i+1,r)for a in [-1,1]for b in [-1,1]}));W=np.unique(np.r_[0,S,(S[:,None]+S).ravel()]);N=len(W);rows=[];cols=[]
 for s in S:
  idx=np.searchsorted(W,W+s);ii=np.flatnonzero(idx<N);ii=ii[W[idx[ii]]==W[ii]+s];rows.append(ii);cols.append(idx[ii])
 rr=np.concatenate(rows);cc=np.concatenate(cols);B=csr_matrix((np.ones(len(rr)),(rr,cc)),shape=(N,N));val,vec=eigsh(B,k=1,which='SA',tol=1e-9,ncv=40);K=-val[0];rec=dict(r=r,n=len(S),W2=N,K=float(K),ratio=float(len(S)/K**2),residual=float(np.linalg.norm(B@vec[:,0]-val[0]*vec[:,0])),seconds=time.time()-t);print(rec,flush=True);out.append(rec)
 open(str(HERE / 'd_root_w2.json'),'w').write(json.dumps(out,indent=2))
