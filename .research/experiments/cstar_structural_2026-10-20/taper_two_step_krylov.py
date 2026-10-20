from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,json,time
from scipy.fft import rfft,irfft,next_fast_len
from scipy.sparse.linalg import LinearOperator,eigsh
rng=np.random.default_rng(20261021);out=[]
for target in [1000,4000,16000]:
 for ex in [.5,1/3,.25]:
  alpha=target**(-ex);X=round(target/alpha);aa=np.arange(1,X+1);A=aa[rng.random(X)<2*alpha*(1-aa/X)]
  if ex!=1/3:continue
  t=time.time();S=np.r_[A,-A];L=next_fast_len(6*X+1);ids=np.r_[0,S]%L;kernel=np.zeros(L);kernel[S%L]=1;fk=rfft(kernel)
  def conv(v):return irfft(rfft(v)*fk,L)
  def mv(v):
   q=np.zeros(L);q[ids]=v;return conv(q)[ids]
  op=LinearOperator((len(ids),len(ids)),matvec=mv,dtype=float);vals,vec=eigsh(op,k=1,which='SA',tol=1e-8,ncv=40,maxiter=2000);K=-vals[0];u=np.zeros(L);u[ids]=vec[:,0];g=conv(u)+K*u;g[ids]=0;a=g@g;cost=(g@conv(g))/a+K;delta=2*a/(np.sqrt(cost**2+4*a)+cost)
  rec=dict(n=len(A),N=len(S),K1=float(K),leak=float(a),leak_over_N=float(a/len(S)),exterior_cost=float(cost),cost_over_sqrt_N=float(cost/np.sqrt(len(S))),two_step_K=float(K+delta),ratio=float(len(S)/(K+delta)**2),seconds=time.time()-t);print(rec,flush=True);out.append(rec)
  open(str(HERE / 'taper_two_step_krylov.json'),'w').write(json.dumps(out,indent=2))
