"""Exact algebra/parity and adversarial checks for the round-15 lemmas. VM only."""
from pathlib import Path
from itertools import product
import importlib.util, json, math
import numpy as np
import sympy as sp

ROOT=Path(__file__).resolve().parent
q,t,L,K,Lam=sp.symbols('q t L K Lam',positive=True)
E=(q-1)*(Lam*(K-sp.Rational(1,2))+K/2-(q+1)/4)
assert sp.expand(E.subs({K:t+sp.Rational(1,2),Lam:L-t-sp.Rational(1,2)})-(q-1)*(t*L-t*t-q/4))==0
ineq=sp.expand(q*t*t*(t*t-sp.Rational(1,4))-(t*t+q/4)**2)
assert sp.expand(ineq-((q-1)*t**4-sp.Rational(3,4)*q*t*t-q*q/16))==0
parity_sets=0
for p in (5,13,17):
    half=(p-1)//2
    for flags in product((0,1),repeat=half):
        D={a for j,z in enumerate(flags) if z for a in (j+1,p-j-1)}
        if not D or len(D)==p-1:continue
        reps=[sum((xi-a)%p in D for a in D) for xi in range(p)]
        assert reps[0]==len(D)
        assert all(reps[xi]%2==int((xi*pow(2,-1,p))%p in D) for xi in range(1,p))
        assert max(reps[1:])-min(reps[1:])>=1
        parity_sets+=1

records=json.loads(ROOT.joinpath('stability_probe.json').read_text())['records']
checks=[]
for r in records:
    if not r['is_exact_halfset'] or not r['pairs']:continue
    p=r['q'];b=np.zeros(p);pp=r['pairs'];b[pp]=1;b[[p-a for a in pp]]=1
    F=np.fft.fft(b).real;F[0]=0
    k=-min(F[1:]);la=max(F[1:]);ll=k+la;tt=k-.5
    h=F+k;h[0]=tt
    A=h>=ll/2;A[0]=False;s=int(sum(A))
    ee=float(sum((la-F[1:])*(F[1:]+k)))
    W=ee+tt*tt
    V=p*p/4+p*k*(k-1)
    assert abs(ll*math.sqrt(s)-math.sqrt(V))<=math.sqrt(max(0,W))+1e-7*p
    if 0<s<p-1:
        parity_lb=ll*ll/(4*(math.sqrt(s+.5)+math.sqrt(s))**2)
        assert W>=parity_lb-1e-6*p*p
    else:parity_lb=None
    rr=dict(name=r['name'],q=p,core=s,W=W,parity_lower_bound=parity_lb)
    if la>k:
        P=np.maximum(F,0);N=np.maximum(-F,0)
        assert sum((P-la*A)**2)<=ee+1e-6*p*p
        DN=k*k*(s+1)+3*k*ee/la
        assert sum((N-k)**2)<=DN+1e-6*p*p
        R=math.sqrt(max(0,DN)/(p*(p-1)))+1/(2*p)
        pi=np.fft.ifft(P).real
        actual=math.sqrt(float(np.mean((pi[1:]-(b[1:]-.5))**2)))
        assert actual<=R+1e-8
        coeff=np.fft.ifft(np.fft.fft(P)**2).real/p**2
        err=max(abs(coeff[1:]-(pi[0]**2-.25)/p))
        assert err<=(p-1)/p*(R+R*R)+1e-8
        for eta in (.1,.5):
            bad=sum(N[1:]<(1-eta)*k-1e-7)
            assert bad<=s+ee/(la*eta*k)+2*ee/(k*ll)+1e-6*p
        rr.update(negative_L2_bound=DN,flat_rms_bound=R,flat_rms_actual=actual,
                  square_fourier_error=err)
    checks.append(rr)

spec=importlib.util.spec_from_file_location('old_barrier','.research/agents/tdense13_scratch/barrier_check.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
old.ROOT=ROOT
partial=old.barrier(201**3,3)
out=dict(status='PROVED exact algebra and finite parity; NUMERICAL stability checks; Arb prior-fake checks',
         exact_parity_sets=parity_sets,stability_checks=checks,
         R13_partial_fake=partial,
         note='201^3 is an odd composite index size for this exact construction check, not a prime half-set.')
ROOT.joinpath('proof_checks.json').write_text(json.dumps(out,indent=2))
print('EXACT_PARITY_SETS',parity_sets,'NUMERICAL_STABILITY_CASES',len(checks))
print('R13_PARTIAL_FAKE',json.dumps(partial))
