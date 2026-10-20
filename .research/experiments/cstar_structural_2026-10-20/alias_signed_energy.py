from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
from w2_operator import *
from scipy.linalg import helmert,eigvalsh
out=[]
for p,a in [(3,2),(5,2),(3,3)]:
 D,m=jl_set(p,a,1);S=(np.array(sorted(D))+m//2)%m-m//2;W=np.unique(np.r_[np.zeros((1,2),int),S,(S[:,None,:]+S[None,:,:]).reshape(-1,2)],axis=0);V=len(W);res=np.ravel_multi_index((W[:,0]%m,W[:,1]%m),(m,m));r=V-len(np.unique(res));Q=np.zeros((V,r));off=0
 for g in np.unique(res):
  ids=np.flatnonzero(res==g);mm=len(ids)
  if mm>1:Q[np.ix_(ids,np.arange(off,off+mm-1))]=helmert(mm).T;off+=mm-1
 base=5*abs(S).max()+1;sk=S@np.array([1,base]);wk=W@np.array([1,base]);B=np.isin(wk[:,None]-wk[None,:],sk).astype(float);A=Q.T@B@Q;vals=eigvalsh(A);pos=float(sum(vals[vals>0]**2));neg=float(sum(vals[vals<0]**2));rec=dict(p=p,a=a,N=len(S),rank=r,positive_energy=pos,negative_energy=neg,energy_ratio=pos/neg,Frob_over_Nrank=(pos+neg)/len(S)/r,lambda_min=float(vals[0]),lambda_max=float(vals[-1]));print(rec,flush=True);out.append(rec)
open(str(HERE / 'alias_signed_energy.json'),'w').write(json.dumps(out,indent=2))
