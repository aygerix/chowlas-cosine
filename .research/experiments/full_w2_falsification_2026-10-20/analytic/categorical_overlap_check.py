from pathlib import Path
ARCHIVE_ROOT = Path(__file__).resolve().parent.parent
import numpy as np,json,time
from scipy.sparse.linalg import LinearOperator,eigsh
from scipy.fft import rfft,irfft,next_fast_len
from pathlib import Path

def run(A,tag):
 S=set(map(int,A))|{-int(a) for a in A}; T={s+t for s in S for t in S};W=T|S|{0};n=len(S)
 bound=2*max(S);length=next_fast_len(6*max(S)+1)
 kernel=np.zeros(length)
 for s in S:kernel[s%length]=1
 fk=rfft(kernel)
 def getk(U):
  ids=np.array(sorted(U))%length
  def mv(v):
   a=np.zeros(length);a[ids]=v;return irfft(rfft(a)*fk,n=length)[ids]
  op=LinearOperator((len(ids),len(ids)),matvec=mv,dtype=float)
  vals,vec=eigsh(op,k=1,which='SA',tol=1e-9,ncv=30,maxiter=3000)
  return float(-vals[0]),float(np.linalg.norm(mv(vec[:,0])-vals[0]*vec[:,0]))
 kt,rt=getk(T);kw,rw=getk(W)
 rec=dict(tag=tag,n=n,missing=len(S-T),missing_fraction=len(S-T)/n,T=len(T),W2=len(W),K_T=kt,K_W2=kw,K_T_over_K_W2=kt/kw,K_T_over_sqrtN=kt/np.sqrt(n),K_W2_over_sqrtN=kw/np.sqrt(n),residual=max(rt,rw))
 print(json.dumps(rec),flush=True);return rec
out=[]
out.append(run([1,2,3,4,5,6,7,9],'record8'))
A=list(range(1,19))+list(range(20,38))+[39,40,41,42,47,48,50,52,57,61,62,64,65,68]
out.append(run(A,'known50'))
for m in [2,4,8,16,32,64]:
 out.append(run(list(range(1,m+1))+[5*m],f'interval{m}_one_outlier'))
for core in [[1,3,6], [1,4,8], [1,3,6,9], [1,3,6,9,12], list(range(1,8))+[9,50], A+[300]]:
 out.append(run(core,'special_'+str(len(core))+'_'+str(max(core))))
for n in [64,256]:
 X=round(n**(4/3));alpha=n**(-1/3);a=np.arange(1,X+1);p=2*alpha*(1-a/X)
 for seed in [31,32]:
  rng=np.random.default_rng(seed);A=a[rng.random(X)<p];out.append(run(A,f'taper{n}_seed{seed}'))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
