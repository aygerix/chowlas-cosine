from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
from w2_operator import *
out=[]
def run(S,m,tag):
 S=np.array(S,int);d=S.shape[1];N=len(S);W=np.unique(np.r_[np.zeros((1,d),int),S,(S[:,None,:]+S[None,:,:]).reshape(-1,d)],axis=0);V=len(W);group=(m,)*d;res=np.ravel_multi_index(tuple(W[:,j]%m for j in range(d)),group);counts=np.bincount(res,minlength=m**d);pad=tuple(next_fast_len(int(5*x+1))for x in abs(S).max(0));ids=tuple(W[:,j]%pad[j]for j in range(d));ker=np.zeros(pad);ker[tuple(S[:,j]%pad[j]for j in range(d))]=1;fk=fftn(ker)
 def avg(v):return (np.bincount(res,weights=v,minlength=len(counts))/np.maximum(counts,1))[res]
 def Q(v):return v-avg(v)
 def B(v):
  x=np.zeros(pad);x[ids]=v;return ifftn(fftn(x)*fk).real[ids]
 def mv(v):return Q(B(Q(v)))
 op=LinearOperator((V,V),matvec=mv,dtype=float);val,vec=eigsh(op,k=1,which='SA',tol=1e-8,ncv=40,maxiter=2000);K=-val[0];rec=dict(tag=tag,N=N,W2=V,occupied_residues=int((counts>0).sum()),alias_dimension=int(V-(counts>0).sum()),Kalias=float(K),Kalias_over_sqrtN=float(K/np.sqrt(N)),ratio=float(N/K**2),residual=float(np.linalg.norm(mv(vec[:,0])-val[0]*vec[:,0])));print(rec,flush=True);out.append(rec);open(str(HERE / 'alias_modes.json'),'w').write(json.dumps(out,indent=2))
for p,a in [(3,2),(5,2),(7,2),(3,3),(3,4)]:
 D,m=jl_set(p,a,1);Z=(np.array(sorted(D))+m//2)%m-m//2;run(Z,m,f'JL_p{p}_a{a}_center')
for p,d in [(3,4),(5,4),(3,6)]:
 Z=np.array([z for z in itertools.product(range(-(p//2),p//2+1),repeat=d)if any(z)and sum(z[2*j]*z[2*j+1]for j in range(d//2))%p==0]);run(Z,p,f'quad_p{p}_d{d}')
