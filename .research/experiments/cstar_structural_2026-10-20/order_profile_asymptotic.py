from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,time
from scipy.fft import rfft,next_fast_len
from scipy.linalg import eigh
J=np.array([[22/5,736/315],[736/315,2369/1890]])
C=21630/241
out=[]
for target in [1000,4000,16000,64000,100000]:
 for replicate in [0,1]:
  st=time.time();alpha=target**(-1/3);X=round(target/alpha);rng=np.random.default_rng(650200+target+replicate)
  a=np.arange(1,X);A=a[rng.random(len(a))<2*alpha*(1-a/X)];del a;n=len(A);M=next_fast_len(3*X+1);coef=np.zeros(M);coef[A]=1;F=rfft(coef);del coef
  vals=np.zeros(7)
  for lo in range(0,len(F),500000):
   hi=min(len(F),lo+500000);z=F[lo:hi];D=2*z.real;t=(z.real*z.real+z.imag*z.imag)/n-1;wt=np.full(hi-lo,2.);
   if lo==0:wt[0]=1
   if M%2==0 and hi==len(F):wt[-1]=1
   mon=[D*D,D*t,t*t,D**3,D*D*t,D*t*t,t**3]
   vals+=np.array([np.dot(wt,v) for v in mon])/M
  del F
  N,dt,tt,ddd,ddt,dtt,ttt=vals;G=np.array([[1,0,0],[0,2*n,dt],[0,dt,tt]]);H=np.array([[0,2*n,dt],[2*n,ddd,ddt],[dt,ddt,dtt]])
  lam,vec=eigh(H,G);K=-lam[0];v=vec[:,0];scale=target**3/X;Hb=H[1:,1:]/scale
  rec=dict(target=target,replicate=replicate,n=n,X=X,fft_length=M,K3D=float(K),K_over_sqrt_2n=float(K/(2*n)**.5),K_over_n13=float(K/n**(1/3)),asymptotic_C=C,alpha_fit=float(-v[2]/v[1]),shape_gram=Hb.tolist(),shape_eigenvalues=eigh(Hb,eigvals_only=True).tolist(),shape_max_error=float(np.max(abs(Hb-J))),dt_identity_relative_error=float(abs(dt-ddd/(3*n))/max(1,abs(dt))),moments=vals.tolist(),seconds=time.time()-st)
  print(json.dumps(rec),flush=True);out.append(rec)
  json.dump(out,open(str(HERE / 'order_profile_asymptotic_results.json'),'w'),indent=2)
