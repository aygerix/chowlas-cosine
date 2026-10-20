from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys,json,numpy as np
from scipy.linalg import eigh
sys.path.insert(0,str(HERE))
from profile_certificate import setup,ROOT
out=[]
sets=[('dense_n20',json.load(open(ROOT+'examples/dense_runs/X30_s0.json'))['A'])]+[(k,v['A']) for k,v in json.load(open(ROOT+'examples/construct/N50_certified.json')).items()]
for name,A in sets:
 A,X,d,c,W,r=setup(A);N=len(A)*2;freq=np.arange(-r,r+1);Ls=list(range(2,r+2));F=np.maximum(0,1-np.abs(freq[:,None])/np.array(Ls)[None,:]);F[r,:]=0
 b=np.isin(freq,np.r_[A,-A]).astype(float);one=(freq==0).astype(float);V=np.c_[one,b,F];Adj=np.isin(freq[:,None]-freq[None,:],np.r_[A,-A]).astype(float);G=V.T@V;H=V.T@Adj@V
 best=None
 for i in range(len(Ls)):
  for j in range(i+1,len(Ls)):
   ids=[0,1,2+i,2+j];gg=G[np.ix_(ids,ids)];hh=H[np.ix_(ids,ids)]
   try:lam,vec=eigh(hh,gg,subset_by_index=[0,0])
   except:continue
   v=vec[:,0]
   if abs(v[1])<1e-9:continue
   alphas=-v[2:]/v[1]
   if min(alphas)<-1e-8:continue
   bound=-lam[0]
   if best is None or bound>best['bound']:best=dict(bound=float(bound),Ls=[Ls[i],Ls[j]],alphas=alphas.tolist(),ritz_coefficients=v.tolist())
 out.append(dict(name=name,best=best));print(out[-1],flush=True)
json.dump(out,open(str(HERE / 'profile_two_fejer_results.json'),'w'),indent=2)
