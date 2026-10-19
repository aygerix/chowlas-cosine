"""Round 12, VM-only adversarial nested-removal probes. No grid is a proof."""
from pathlib import Path
import json, math, time, platform
import numpy as np
from scipy.optimize import minimize_scalar

ROOT=Path(__file__).resolve().parent
SEED=2026101912
rng=np.random.default_rng(SEED)

def prime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))

def primitive_root(p):
    for g in range(2,p):
        if len({pow(g,j,p) for j in range(p-1)})==p-1:
            return g
    raise ValueError(p)

def assign_pairs(n, active, scores):
    pairs=[c for c in range(1,(n+1)//2) if c in active]
    pairs.sort(key=lambda c:(scores[c],c))
    u=np.zeros(n)
    for j,c in enumerate(pairs):
        u[c]=u[-c]=(j+0.5)/len(pairs)
    if 0 in active: u[0]=0.5
    if n%2==0 and n//2 in active: u[n//2]=0.5
    return u

def families(n):
    c=np.arange(n)
    bohr=set(int(x) for x in c if np.cos(2*np.pi*x/n)>0)
    even=set(range(0,n,2)) if n%2==0 else None
    if prime(n) and n%4==1:
        qr={pow(j,2,n) for j in range(1,n)}
        g=primitive_root(n); logs={pow(g,j,n):j for j in range(n-1)}
        mult=np.array([logs.get(int(x),0)%(max(1,(n-1)//4)) for x in c])
        yield 'multiplicative_cosets',assign_pairs(n,qr,mult)
        yield 'paley_bohr_removal',assign_pairs(n,qr,np.cos(2*np.pi*3*c/n))
        yield 'paley_random_removal',assign_pairs(n,qr,rng.random(n))
    if even is not None:
        bits=int(math.log2(n))
        reverse=np.array([int(format(int(x),f'0{bits}b')[::-1],2) for x in c])
        yield 'coset_bit_removal',assign_pairs(n,even,reverse)
        yield 'coset_bohr_removal',assign_pairs(n,even,np.cos(2*np.pi*3*c/n))
    yield 'bohr_slices',assign_pairs(n,bohr,np.cos(2*np.pi*3*c/n))
    yield 'bohr_random_removal',assign_pairs(n,bohr,rng.random(n))
    reps=np.arange(1,(n+1)//2)
    chosen=rng.choice(reps,size=len(reps)//2,replace=False)
    active=set(map(int,chosen))|set(int(n-x) for x in chosen)
    yield 'random_pairs',assign_pairs(n,active,rng.random(n))

def analyze(n,name,u):
    s=np.arange(n)
    mat=np.cos(2*np.pi*np.outer(s,s)/n)/n
    xis=np.linspace(0,200,1601)
    vals=np.sinc(xis[:,None]*u[None,:]/np.pi)*u[None,:]
    cs=vals@mat.T
    candidates=np.argsort(cs.min(axis=1))[:12]
    best=(float(cs.min()),float(xis[np.unravel_index(cs.argmin(),cs.shape)[0]]),int(np.unravel_index(cs.argmin(),cs.shape)[1]))
    for j in candidates:
        sc=int(cs[j].argmin())
        fun=lambda xi:float(mat[sc]@(u*np.sinc(xi*u/np.pi)))
        rr=minimize_scalar(fun,bounds=(max(0,xis[j]-.15),xis[j]+.15),method='bounded')
        if rr.fun<best[0]:best=(float(rr.fun),float(rr.x),sc)
    xi=24.125
    bc=np.where(u>0,np.expm1(1j*xi*u)/(1j*xi),0)
    z=np.fft.fft(bc)/n
    z2=float(np.sum(np.abs(z[1:])**2))
    direct=float(np.mean(np.abs(bc)**2)-abs(bc.mean())**2)
    real=mat@(u*np.sinc(xi*u/np.pi))
    energy=float(real@real)
    pos=np.maximum(real,0)**2
    top=float(np.sort(pos)[-4:].sum()/energy) if energy else 0
    return dict(N=n,family=name,p0=float(np.mean(u>0)),d=float(u.mean()),
      sampled_mu=-best[0],xi=best[1],character=best[2],
      mu_sqrt_N=-best[0]*math.sqrt(n),mu_N=-best[0]*n,
      complex_identity_error=abs(z2-direct),real_identity_error=abs(energy-np.mean((np.sin(xi*u)/xi)**2)),
      rough_xi=xi,positive_top4_energy_fraction=top,negative_energy_fraction=float(np.minimum(real,0)@np.minimum(real,0)/energy),
      u=u.tolist())

def checks():
    errors=[]
    for n in (5,7,13):
        for _ in range(8):
            u=rng.integers(0,8,n)/7
            xi=float(rng.uniform(.2,20))
            b=np.expm1(1j*xi*u)/(1j*xi)
            z=np.fft.fft(b)/n
            er=abs(np.sum(z.real**2)-(np.sum(abs(b)**2+np.real(b*b[(-np.arange(n))%n]))/(2*n)))
            errors.append(float(er))
    # Independent O(N^2) and FFT Fejer transfer, including Y=q and Y=3q.
    cyclic=[]
    for q in (5,13,29):
        ss=rng.choice([-1,1],q);ss[(-np.arange(q))%q]=ss
        # enforce evenness explicitly
        for j in range(1,(q+1)//2): ss[-j]=ss[j]
        hh=np.fft.fft(ss).real
        for y in (2,q,3*q):
            x=.431
            def fj(t):
                return abs(np.exp(1j*t*np.arange(y)).sum())**2/y
            lhs=sum((1-k/y)*ss[k%q]*math.cos(k*x) for k in range(1,y))
            rhs=sum(hh[g]*fj(x+2*np.pi*g/q) for g in range(q))/(2*q)-ss[0]/2
            cyclic.append(abs(lhs-rhs))
    return dict(real_general_parseval_max_error=max(errors),fejer_transfer_max_error=max(cyclic))

def main():
    started=time.time(); rows=[]
    for n in (29,61,127,257,64,128,256):
        for name,u in families(n):
            r=analyze(n,name,u);rows.append(r)
        print(json.dumps({'N':n,'best':min((r for r in rows if r['N']==n),key=lambda r:r['sampled_mu'])|{'u':'saved'}}),flush=True)
    out=dict(status='NUMERICAL; continuous minima not certified',seed=SEED,python=platform.python_version(),
        numpy=np.__version__,xi_grid=[0,200,1601],checks=checks(),seconds=time.time()-started,rows=rows)
    (ROOT/'roughness_results.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out['checks']),flush=True)

if __name__=='__main__':main()
