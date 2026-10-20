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
