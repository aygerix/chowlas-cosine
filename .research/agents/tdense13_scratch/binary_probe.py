"""Profile-preserving binary laws. FFT estimates, refined dips, Arb point certificates."""
from pathlib import Path
import ctypes,json,math,subprocess,sys,gc,platform
import numpy as np
from scipy.optimize import minimize_scalar
from sympy import nextprime
import gurobipy as gp
from gurobipy import GRB
from flint import arb,ctx
ctx.prec=180
ROOT=Path(__file__).resolve().parent

def profile(X):
    rows=[json.loads(l) for l in open('examples/e82/e82.jsonl')]
    row=max((r for r in rows if r['N']==320),key=lambda r:r['D'])
    g=np.array(row['g']);w0=np.r_[np.correlate(g,g,'full')[319:]/(g@g),0]
    w=np.interp(np.arange(1,X+1)/X,np.arange(321)/320,w0)
    return (1-np.sqrt(np.maximum(0,1-w*w)))/2,w

def prime1(x):
    q=int(nextprime(max(4,int(x)-1)))
    while q%4!=1:q=int(nextprime(q))
    return q

def counted(p,scores,B=256):
    out=np.zeros(len(p),dtype=np.uint8);carry=0.
    for lo in range(0,len(p),B):
        hi=min(lo+B,len(p));target=float(p[lo:hi].sum())+carry
        cnt=int(round(target));carry=target-cnt
        take=np.argsort(-scores[lo:hi],kind='stable')[:cnt]+lo;out[take]=1
    return out

def minimum(bits):
    X=len(bits);A=np.flatnonzero(bits).astype(np.int64)+1
    L=1<<(16*(X+1)-1).bit_length();coef=np.zeros(X+1);coef[1:]=bits
    vals=np.fft.rfft(coef,n=L).real
    js=np.argpartition(vals,min(16,len(vals)-1))[:16]
    j=int(vals.argmin());best=float(vals[j]);phase=j/L
    del vals;gc.collect()
    def f(t):return float(np.cos(2*np.pi*A*t).sum())
    for jj in js:
        sol=minimize_scalar(f,bounds=(max(0,(jj-1)/L),min(.5,(jj+1)/L)),method='bounded',
                            options={'xatol':1e-16,'maxiter':40})
        if sol.fun<best:best=float(sol.fun);phase=float(sol.x)
    # Evaluate an exact rational phase, so the point is unambiguous and independently reproducible.
    den=1<<60;num=int(round(phase*den));v=arb(0)
    for a in A:v+=(2*arb.pi()*int((int(a)*num)%den)/den).cos()
    assert v.upper()<0
    return dict(X=X,n=len(A),actual_max=int(A[-1]),M_estimate=-best,R_estimate=-best/math.sqrt(len(A)),
                M_over_sqrtX=-best/math.sqrt(X),phase_num=num,phase_den=den,FFT_length=L,
                point_ball=str(v),M_point_interval=[float(np.nextafter(-float(v.upper()),-np.inf)),
                                                    float(np.nextafter(-float(v.lower()),np.inf))],
                certificate_status='Arb point dip; global minimum NUMERICAL',arb_bits=ctx.prec),A

def save(family,bits,extra):
    row,A=minimum(bits);row.update(family=family,**extra)
    np.savez_compressed(ROOT/(family+'_X'+str(len(bits))+'.npz'),A=A)
    with open(ROOT/'binary_results.jsonl','a') as fh:fh.write(json.dumps(row)+'\n')
    print(json.dumps(row),flush=True)
    if row['R_estimate']<.56:
        raise RuntimeError('Promising R<0.56: require all-x Arb certification before continuing.')
    return row

def diffusion(p,w,X):
    # Initial adverse frequencies are the worst residual dips of a deterministic counted random seed.
    rng=np.random.default_rng(1913+X);b=counted(p,rng.random(X))
    L=1<<(4*(X+1)-1).bit_length();c=np.zeros(X+1);c[1:]=b-p
    vals=np.fft.rfft(c,n=L).real;idx=np.argpartition(vals,48)[:48]
    angles=np.r_[2*np.pi*idx/L,2*np.pi*rng.random(16)].astype(np.float64)
    so=ROOT/'diffuse.so'
    if not so.exists():subprocess.run(['cc','-O3','-shared','-fPIC',str(ROOT/'diffuse.c'),'-o',str(so),'-lm'],check=True)
    lib=ctypes.CDLL(str(so));fn=lib.diffuse
    ptr=ctypes.POINTER(ctypes.c_double)
    fn.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_int,ptr,ptr,ptr,ctypes.POINTER(ctypes.c_ubyte)]
    out=np.zeros(X,dtype=np.uint8)
    fn(X,len(angles),256,p.ctypes.data_as(ptr),w.ctypes.data_as(ptr),angles.ctypes.data_as(ptr),
       out.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)))
    return out

def milp(X):
    p,w=profile(X);B=16;target=counted(p,np.cos(np.arange(X)),B=B);cuts=np.arange(16*X+1)/(32*X)
    b0=target
    for it in range(3):
        model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=4;model.Params.TimeLimit=10
        model.Params.Seed=1913
        b=model.addMVar(X,vtype=GRB.BINARY);M=model.addVar(lb=0)
        b.Start=b0
        for lo in range(0,X,B):model.addConstr(b[lo:lo+B].sum()==int(target[lo:lo+B].sum()))
        for cs in np.array_split(cuts,16):
            C=np.cos(2*np.pi*np.outer(cs,np.arange(1,X+1)))
            model.addConstr(C@b+M>=0)
        model.setObjective(M);model.optimize()
        if not model.SolCount:break
        b0=(b.X>.5).astype(np.uint8)
        row,A=minimum(b0);cuts=np.r_[cuts,row['phase_num']/row['phase_den']]
    return save('gurobi_round',b0,dict(block=B,solver=gp.gurobi.version(),solver_status=int(model.Status),
                    solver_bound=float(model.ObjBound),grid_objective=float(model.ObjVal),iterations=3))

def main():
    (ROOT/'binary_results.jsonl').write_text('')
    for X in (4096,65536,1048576):
        p,w=profile(X);k=np.arange(1,X+1)
        for theta in (.5,2/3,1.):
            q=prime1(X**theta);chi=np.zeros(q);r=np.arange(1,(q+1)//2,dtype=np.int64)
            chi[(r*r)%q]=1
            rng=np.random.default_rng(191300+q);tie=rng.random((q+1)//2)
            scores=chi[k%q]+tie[np.minimum(k%q,(-k)%q)]*.1
            save('paley_'+str(theta),counted(p,scores),dict(q=q,theta=theta,block=256,seed=191300+q))
        for theta in (.5,1.):
            q=prime1(X**theta)
            # Near-interval local order, dilated by 3; exact block counts enforce the E82 profile.
            scores=-np.minimum((3*k)%q,(-3*k)%q).astype(float)
            save('nearinterval_'+str(theta),counted(p,scores),dict(q=q,theta=theta,dilation=3,block=256))
        save('spectral_diffusion',diffusion(p,w,X),dict(modes=64,block=256,seed=1913+X))
    for X in (128,256):milp(X)

if __name__=='__main__':
    if sys.argv[1:]==['milp_only']:
        rows=[json.loads(l) for l in (ROOT/'binary_results.jsonl').read_text().splitlines()]
        (ROOT/'binary_results.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rows if r['family']!='gurobi_round'))
        for X in (128,256):milp(X)
    else:main()
