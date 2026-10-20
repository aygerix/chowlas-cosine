from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,math,time
from scipy.fft import rfft,irfft,next_fast_len
from scipy.optimize import minimize_scalar
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh,LinearOperator
ROOT=str(REPO) + '/'
def conv(a,b):
 l=next_fast_len(len(a)+len(b)-1);return irfft(rfft(a,l)*rfft(b,l),l)[:len(a)+len(b)-1]
def setup(A):
 A=np.array(A,dtype=int);X=max(A);d=np.zeros(2*X+1);d[X+A]=1;d[X-A]=1;c=np.rint(conv(d,d));W=c>0;W[2*X+A]=1;W[2*X-A]=1;W[2*X]=1
 z=np.flatnonzero(~W[2*X:]);rad=int(z[0]-1) if len(z) else 2*X
 return A,X,d,c,W,rad
def optimize(N,dt,tt,ddd,ddt,dtt,ttt):
 if tt<1e-15:return None
 def calc(alpha):
  V=N-2*alpha*dt+alpha*alpha*tt
  if V<1e-12:return (-1e100,)*2+(0,)*6
  sv=V**.5;a=(N-alpha*dt)/sv;b=(ddd-2*alpha*ddt+alpha*alpha*dtt)/V
  fixed=a-b/2;two=(np.hypot(b,2*a)-b)/2
  ppen=alpha*(2-2*(dt-alpha*tt)/sv+(ddt-2*alpha*dtt+alpha*alpha*ttt)/V)/2
  cubic=(ddd-3*alpha*ddt+3*alpha*alpha*dtt-alpha**3*ttt)/(2*V)
  return fixed,two,sv,ppen,cubic,a,b,V
 scale=max((N/tt)**.5,abs(dt/tt),1e-8)
 grid=np.r_[0,np.geomspace(scale*1e-5,scale*100,90)]
 vals=[calc(x) for x in grid];out={}
 for k,name in [(0,'fixed'),(1,'two')]:
  ids=np.argsort([v[k] for v in vals])[-4:];opts=[(vals[i][k],grid[i]) for i in ids]
  for i in ids:
   lo=grid[max(0,i-1)];hi=grid[min(len(grid)-1,i+1)]
   if hi>lo:
    res=minimize_scalar(lambda x:-calc(x)[k],bounds=(lo,hi),method='bounded',options={'xatol':1e-10});opts.append((-res.fun,res.x))
  value,alpha=max(opts);v=calc(alpha);out[name]=dict(bound=float(value),alpha=float(alpha),fixed_at_alpha=float(v[0]),two_at_alpha=float(v[1]),sqrtV=float(v[2]),P_penalty=float(v[3]),cubic_penalty=float(v[4]),a=float(v[5]),b=float(v[6]),V=float(v[7]),P_penalty_over_sqrtV=float(v[3]/v[2]),cubic_penalty_over_sqrtV=float(v[4]/v[2]))
 G=np.array([[1,0,0],[0,N,dt],[0,dt,tt]],float);H=np.array([[0,N,dt],[N,ddd,ddt],[dt,ddt,dtt]],float)
 ev,U=eigh(G);U=U[:,ev>1e-9]/np.sqrt(ev[ev>1e-9]);out['three']=-float(eigh(U.T@H@U,eigvals_only=True)[0]);return out
def fejer_stats(A,c,X,L):
 N=len(A)*2;aa=A[A<L];dt=2*np.sum(1-aa/L);tt=(L-1)*(2*L-1)/(3*L);ddd=2*np.sum(c[2*X+A]);ks=np.arange(1,min(L,2*X+1));ddt=2*np.sum(c[2*X+ks]*(1-ks/L))
 def fc(k):
  z=k+2*L-2
  return sum((-1)**j*math.comb(4,j)*math.comb(z-j*L+3,3) for j in range(5) if z-j*L>=0)/L**2
 dtt=2*sum(fc(int(a))-2*max(0,1-a/L) for a in A if a<2*L-1)
 ttt=(math.comb(3*L+2,5)-6*math.comb(2*L+2,5)+15*math.comb(L+2,5))/L**3-(2*L*L+1)/L+2
 return N,dt,tt,ddd,ddt,dtt,ttt
def order_stats(A,d,c,X):
 n=len(A);u=np.zeros(X+1);u[A]=1;t=conv(u,u[::-1])/n;t[X]=0;ttconv=conv(t,t)
 return 2*n,float(np.dot(d,t)),float(np.dot(t,t)),float(2*sum(c[2*X+A])),float(np.dot(c[X:3*X+1],t)),float(2*sum(ttconv[2*X+A])),float(np.dot(ttconv[X:3*X+1],t))
def w2(A,d,W,X):
 ids=np.flatnonzero(W);m=len(W)
 if m<600:
  ww=ids-2*X;H=np.isin(ww[:,None]-ww[None,:],np.r_[A,-A]).astype(float);return -float(eigh(H,eigvals_only=True,subset_by_index=[0,0])[0]),'dense_eigh'
 fl=next_fast_len(m+len(d)-1);fd=rfft(d,fl)
 def mv(v):
  z=np.zeros(m);z[ids]=v;return irfft(rfft(z,fl)*fd,fl)[X:X+m][ids]
 op=LinearOperator((len(ids),len(ids)),matvec=mv);lam,vec=eigsh(op,k=1,which='SA',tol=2e-7,maxiter=2000);res=np.linalg.norm(mv(vec[:,0])-lam[0]*vec[:,0]);return -float(lam[0]),'eigsh_residual_'+str(res)
def run(name,A):
 st=time.time();A,X,d,c,W,rad=setup(A);N=2*len(A)
 if rad<250:Ls=range(2,rad+2)
 else:Ls=sorted(set(np.r_[np.rint(np.geomspace(2,rad+1,100)),np.rint(np.linspace(max(2,.5*X),min(rad+1,1.5*X),80)),X,X+1].astype(int)));Ls=[l for l in Ls if 2<=l<=rad+1]
 profiles=[]
 for L in Ls:
  o=optimize(*fejer_stats(A,c,X,int(L)));o['L']=int(L);profiles.append(o)
 best={kind:max(profiles,key=lambda o:o[kind]['bound']) for kind in ['fixed','two']};best3=max(profiles,key=lambda o:o['three'])
 order=optimize(*order_stats(A,d,c,X));kw,method=w2(A,d,W,X)
 out=dict(name=name,n=len(A),X=int(X),W2_size=int(W.sum()),contained_radius=int(rad),K_W2=kw,W2_method=method,fejer_best_fixed=best['fixed'],fejer_best_two=best['two'],fejer_best_three=best3,order_profile=order,elapsed=time.time()-st)
 print(json.dumps(out),flush=True);return out
if __name__=='__main__':
 out=[];dense=json.load(open(ROOT+'examples/dense_runs/X30_s0.json'));out.append(run('dense_n20',dense['A']))
 for name,r in json.load(open(ROOT+'examples/construct/N50_certified.json')).items():out.append(run(name,r['A']))
 for n in [20,50]:out.append(run('interval_'+str(n),list(range(1,n+1))))
 rng=np.random.default_rng(20261021)
 for target in [1000]:
  for ex in [.5,1/3,.25]:
   alpha=target**(-ex);X=round(target/alpha);a=np.arange(1,X+1);A=a[rng.random(X)<2*alpha*(1-a/X)];out.append(run('E99c_'+str(target)+'_'+str(ex),A))
 json.dump(out,open(str(HERE / 'profile_certificate_results.json'),'w'),indent=2)
