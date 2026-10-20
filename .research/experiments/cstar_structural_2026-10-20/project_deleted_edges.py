from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
from w2_operator import *
from scipy.fft import fftn,ifftn,next_fast_len
out=[]
def run(S,modulus,tag):
 S=np.array(S,int);d=S.shape[1];shape=(modulus,)*d;V=modulus**d;D=np.zeros(shape);D[tuple(S[:,j]%modulus for j in range(d))]=1;F=fftn(D).real;kg=-float(F.min());bg=np.isclose(F,-kg);N=len(S)
 W=np.unique(np.r_[np.zeros((1,d),int),S,(S[:,None,:]+S[None,:,:]).reshape(-1,d)],axis=0);order=np.argsort((W.astype(float)**2).sum(1));Wr=W[order];res=np.ravel_multi_index(tuple(Wr[:,j]%modulus for j in range(d)),shape);classes,idx=np.unique(res,return_index=True)
 assert len(classes)==V,(tag,len(classes),V)
 R=Wr[idx];bound=2*np.abs(R).max(0)+np.abs(S).max(0);pad=tuple(next_fast_len(int(x+1))for x in bound);ids=tuple(R[:,j]%pad[j] for j in range(d));ker=np.zeros(pad);ker[tuple(S[:,j]%pad[j]for j in range(d))]=1;fk=fftn(ker)
 def proj(v):return ifftn(fftn(v.reshape(shape))*bg).real.ravel()
 def E(v):
  circ=ifftn(fftn(v.reshape(shape))*F).real.ravel();x=np.zeros(pad);x[ids]=v;lin=ifftn(fftn(x)*fk).real[ids];return circ-lin
 def mv(v):return proj(E(proj(v)))
 op=LinearOperator((V,V),matvec=mv,dtype=float);val,vec=eigsh(op,k=1,which='LA',tol=1e-8,ncv=40,maxiter=2000);lam=float(val[0]);u=vec[:,0];rec=dict(tag=tag,N=N,V=V,Kgroup=kg,background_rank=int(bg.sum()),lambda_bg_E=lam,lambda_over_sqrtN=lam/np.sqrt(N),K_certificate=kg+lam,ratio=N/(kg+lam)**2,residual=float(np.linalg.norm(mv(u)-lam*u)),maxrep=int(abs(R).max()));print(rec,flush=True);out.append(rec)
 open(str(HERE / 'project_deleted_edges.json'),'w').write(json.dumps(out,indent=2))
for p,a in [(3,2),(5,2),(7,2),(3,3),(3,4)]:
 D,m=jl_set(p,a,1);Z=(np.array(sorted(D))+m//2)%m-m//2;run(Z,m,f'JL_p{p}_a{a}_centered')
for p,d in [(3,4),(5,4),(3,6)]:
 Z=np.array([z for z in itertools.product(range(-(p//2),p//2+1),repeat=d)if any(z)and sum(z[2*j]*z[2*j+1]for j in range(d//2))%p==0]);run(Z,p,f'quad_p{p}_d{d}')
