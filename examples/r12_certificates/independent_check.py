"""Independent exact-count and Arb point checks. Execute only on dirichlet."""
from pathlib import Path
from fractions import Fraction as Q
import json,math,random,hashlib,platform
import numpy as np
from flint import arb,ctx
ctx.prec=220
ROOT=Path(__file__).resolve().parent

def aq(q):return arb(q.numerator)/q.denominator

def certify_schedule(row):
    n=row['N'];u=[Q(float(v)).limit_denominator(100000) for v in row['u']]
    xi=Q(float(row['xi'])).limit_denominator(1000000);s=row['character']
    value=arb(0)
    for c,v in enumerate(u):
        av=aq(v) if not xi else (aq(xi*v)).sin()/aq(xi)
        value+=av*(2*arb.pi()*s*c/n).cos()/n
    assert value.upper()<0
    # Realize each schedule as initial residue columns at a large finite X.
    X=n*4096;counts=[]
    for c,v in enumerate(u):
        endpoint=(X*v.numerator)//v.denominator
        first=c if c else n
        counts.append(max(0,1+(endpoint-first)//n))
    actual=arb(0)
    x=2*arb.pi()*s/n+aq(xi)/X
    for c,ell in enumerate(counts):
        if not ell:continue
        first=c if c else n
        # Geometric sum, with exact resonance handled separately.
        z=aq(xi)*n/X
        if not xi:
            actual+=ell*(2*arb.pi()*s*c/n).cos()
        else:
            actual+=(ell*z/2).sin()*(first*x+(ell-1)*z/2).cos()/(z/2).sin()
    assert actual.upper()<0
    return dict(N=n,family=row['family'],xi=str(xi),character=s,
                continuum_point_ball=str(value),X=X,n=sum(counts),actual_point_ball=str(actual),
                model_error_ball=str(actual-X*value),status='PROVED point dips only; no global upper bound on M')

def count_checks():
    rng=random.Random(2026101912);cases=0
    for N in range(1,50):
        for _ in range(20):
            counts=[rng.randrange(30) for _ in range(N)]
            n=sum(counts);r=sum(x>0 for x in counts)
            if not n:continue
            E=sum(Q(counts[c]+counts[-c],2)**2 for c in range(N))
            assert E>=Q(n*n,2*r)
            # polynomial coefficients, folded modulo N, independently check root trace
            folded=[Q(0)]*N
            for c,l in enumerate(counts):folded[c]+=Q(l,2);folded[-c]+=Q(l,2)
            trace_sq=sum(folded[c]*folded[-c] for c in range(N))
            assert trace_sq==E
            cases+=1
    return cases

def relaxed_example(p):
    # lambda=m integer, p=m^3 need not be prime for this scalar barrier check.
    lam=round(p**(1/3));assert lam**3==p
    h0=lam-1;T=p*(lam-1);E=p*p+p*lam*(lam-2)
    tp=T-h0;ep=E-h0*h0
    r=4*math.ceil(Q(tp*tp,ep)/4)
    mean=Q(tp,r);var=Q(ep,r)-mean*mean
    assert var>=0 and mean*mean>=var
    assert r*mean==tp and r*(mean*mean+var)==ep
    # rational sufficient bounds for both scalar peak constraints
    assert 4*mean*mean<=p*lam*(lam-2)
    assert 2*mean<=Q(lam**3,2)
    return dict(p=p,lam=lam,nonzero_slots=r,high_mean=str(mean),variance=str(var))

def nonnested():
    rng=np.random.default_rng(2026101913);out=[]
    for X in (65536,262144,1048576):
        L=math.isqrt(X);T=X//L
        active=rng.random(T)<.5*(1-(np.arange(T)+.5)/T)
        b=np.repeat(active,L).astype(float)
        b[:L]=np.arange(1,L+1)%2==0
        coeff=np.zeros(X+1);coeff[1:]=b
        K=1<<(32*(X+1)-1).bit_length()
        vals=np.fft.rfft(coeff,n=K).real
        j=int(vals.argmin());x=2*arb.pi()*j/K
        runs=[];start=None
        for i,v in enumerate(b,1):
            if v and start is None:start=i
            if not v and start is not None:runs.append((start,i-1));start=None
        if start is not None:runs.append((start,X))
        value=arb(0)
        for lo,hi in runs:
            value+=((hi-lo+1)*x/2).sin()*((lo+hi)*x/2).cos()/(x/2).sin()
        assert value.upper()<0
        rec=dict(X=X,L=L,T=T,n=int(b.sum()),N=2,fft_min=float(vals[j]),
                 sampled_M_over_X=-float(vals[j])/X,point_ball=str(value),grid=K,index=j,
                 status='NUMERICAL global minimum, PROVED negative point evaluation',runs=runs)
        (ROOT/f'nonnested_X{X}.json').write_text(json.dumps(rec))
        out.append({k:v for k,v in rec.items() if k!='runs'})
    return out

def main():
    data=json.loads((ROOT/'roughness_results.json').read_text());rows=data['rows']
    selected=[min((r for r in rows if r['N']==N),key=lambda r:r['sampled_mu']) for N in (29,61,64,257)]
    for N in (29,61):selected.append(json.loads((ROOT/f'milp_N{N}.json').read_text())['probe'])
    result=dict(python=platform.python_version(),arb_bits=ctx.prec,count_cases=count_checks(),
      schedule_certificates=[certify_schedule(r) for r in selected],
      scalar_barrier=[relaxed_example(m**3) for m in (10,20,50,100)],nonnested=nonnested())
    (ROOT/'independent_checks.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2),flush=True)
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.iterdir() if p.is_file() and p.name!='manifest.json'}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))

if __name__=='__main__':main()
