from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
import numpy as np,itertools,sys,json,time
from scipy.fft import fftn,ifftn,next_fast_len
from scipy.sparse.linalg import LinearOperator,eigsh
sys.path.insert(0,str(REPO / 'src'))
import ast
_tree=ast.parse(open(str(REPO / 'src/e114_cp_group.py')).read());exec(compile(ast.Module(body=[x for x in _tree.body if isinstance(x,ast.FunctionDef) and x.name=='jl_set'],type_ignores=[]),'jl_set_extracted','exec'))
out=[]
def test(S,tag):
 t=time.time();S=np.unique(np.array(S,dtype=int),axis=0);S=S[np.any(S!=0,axis=1)];n,d=S.shape;maxs=np.abs(S).max(0);shape=tuple(next_fast_len(int(5*v+1)) for v in maxs);W=np.unique(np.r_[np.zeros((1,d),int),S,(S[:,None,:]+S[None,:,:]).reshape(-1,d)],axis=0)
 ids=tuple((W[:,i]%shape[i]) for i in range(d));kernel=np.zeros(shape);kernel[tuple((S[:,i]%shape[i]) for i in range(d))]=1;fk=fftn(kernel)
 def mv(v):
  x=np.zeros(shape);x[ids]=v;return ifftn(fftn(x)*fk).real[ids]
 op=LinearOperator((len(W),len(W)),matvec=mv,dtype=float);val,vec=eigsh(op,k=1,which='SA',tol=2e-8,maxiter=1200,ncv=40);res=np.linalg.norm(mv(vec[:,0])-val[0]*vec[:,0]);K=-val[0]
 rec=dict(tag=tag,n=n,W2=len(W),grid=int(np.prod(shape)),K=float(K),ratio=float(n/K**2),residual=float(res),seconds=time.time()-t);print(json.dumps(rec),flush=True);out.append(rec)
for p in [3,5,7]:
 D,n=jl_set(p,2,1);Z=np.array(sorted(D));Z=(Z+n//2)%n-n//2
 test(Z,f'JL_centered_p{p}_Zd')
 for b in [n,3*n]:test((Z@np.array([1,b]))[:,None],f'JL_centered_p{p}_base{b}')
 rng=np.random.default_rng(1729);half=np.array([g for g in sorted(D) if g<((-g[0])%n,(-g[1])%n)]);Z=[]
 for g in half:
  c=np.array([(g[0]+n*u,g[1]+n*v)for u in [-1,0]for v in [-1,0]]);w=np.prod(1-abs(c)/n,axis=1);z=c[rng.choice(4,p=w/w.sum())];Z.extend([z,-z])
 test(Z,f'JL_random_p{p}_Zd')
for p in [3,5]:
 Z=np.array([z for z in itertools.product(range(-(p//2),p//2+1),repeat=4) if any(z) and (z[0]*z[1]+z[2]*z[3])%p==0]);test(Z,f'quadric_p{p}_Zd')
 for b in [p,3*p]:test((Z@np.array([b**j for j in range(4)]))[:,None],f'quadric_p{p}_base{b}')
open(str(HERE / 'adversarial_w2_lifts.json'),'w').write(json.dumps(out,indent=2))
