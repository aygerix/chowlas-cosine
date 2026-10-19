"""Exact support geometry plus 180-bit Arb checks of the partial-convolution construction."""
from pathlib import Path
from fractions import Fraction as Q
import json, math
from flint import arb,ctx
import sympy as sp
ctx.prec=180
ROOT=Path(__file__).resolve().parent

def barrier(q,J):
    # q is an integer cube in these rational checks. The paper proof covers every sufficiently large odd prime.
    u=round(q**(1/3));assert u**3==q
    H=4*u*u;C=q*u*(u-2);ell=u
    residual=[None]+[Q(C-2*(u-1)*H if d==1 else C-H*H if d==2 else C) for d in range(1,J+1)]
    assert all(v>0 for v in residual[1:])
    special={0:(0,1),1:(1,1),q-1:(1,1)}
    # Symbolic labels: 0=h0, 1=H, 1+d=dedicated-pair amplitude, J+2/J+3=repair levels.
    levels=[arb(u-1),arb(H)]+[(arb(v.numerator)/v.denominator/(2*ell)).sqrt() for v in residual[1:]]
    t=4*J+10
    for d in range(1,J+1):
        for _ in range(ell):
            for a in (t,t+d,q-t,q-t-d):
                assert a not in special;special[a]=(d+1,1)
            t+=3*J+3
    T=arb(q*(u-1))-levels[0]-2*levels[1]
    E=arb(q*q+q*u*(u-2))-levels[0]**2-2*levels[1]**2
    for d in range(1,J+1):
        T-=4*ell*levels[d+1];E-=arb(2*residual[d].numerator)/residual[d].denominator
    assert T.lower()>0 and E.lower()>0
    ratio=T*T/E;m=4*math.ceil(float((3*ratio/8).mid()))
    assert (arb(m)-ratio).lower()>0 and (2*ratio-m).lower()>0
    mean=T/m;var=E/m-mean*mean
    assert var.lower()>0 and (mean*mean-var).lower()>0
    levels += [mean+var.sqrt(),mean-var.sqrt()]
    assert (levels[1]-levels[-2]).lower()>0
    for idx in range(m//2):
        t+=2*J+2
        label=J+2 if idx<m//4 else J+3
        for a in (t,q-t):assert a not in special;special[a]=(label,1)
    assert t+3*J<q//2
    correlations=[]
    for d in range(1,J+1):
        counts={}
        for a,(la,_) in special.items():
            b=(a+d)%q
            if b in special:
                lb=special[b][0];key=tuple(sorted((la,lb)))
                counts[key]=counts.get(key,0)+1
        expected={(d+1,d+1):2*ell}
        if d==1:expected[(0,1)]=2
        if d==2:expected[(1,1)]=1
        assert counts==expected,(d,counts,expected)
        value=sum((mult*levels[a]*levels[b] for (a,b),mult in counts.items()),arb(0))
        assert (value-C).contains(0)
        correlations.append(dict(gamma=d,exact_monomial_counts={str(k):v for k,v in counts.items()},
                                 residual_ball=str(value-C)))
    mass=levels[0]+2*levels[1]+sum((4*ell*levels[d+1] for d in range(1,J+1)),arb(0))+m*mean
    energy=levels[0]**2+2*levels[1]**2+sum((4*ell*levels[d+1]**2 for d in range(1,J+1)),arb(0))+m*(mean*mean+var)
    assert (mass-q*(u-1)).contains(0)
    assert (energy-(q*q+q*u*(u-2))).contains(0)
    gap=2*J+2;outside=arb(0)
    for a,(la,_) in special.items():
        b=(a+gap)%q
        if b in special:outside+=levels[la]*levels[special[b][0]]
    repair_lower=E-2*(levels[-2]**2+levels[-1]**2-levels[-2]*levels[-1])
    assert (outside-repair_lower).contains(0)
    assert (outside-C-arb(q*q)/2).lower()>0
    return dict(q=q,prime=False,J=J,u=u,repair_sites=m,support_sites=len(special),last_positive=t,
                K_sign=u,Lambda_sign=H-u,mass_residual=str(mass-q*(u-1)),
                energy_residual=str(energy-(q*q+q*u*(u-2))),correlations=correlations,
                first_tested_outside_segment=gap,sign_defect_over_q2_ball=str((outside-C)/(q*q)),
                status='Exact support-count check and Arb arithmetic; infinite-prime claim proved in report')

def fake_cubic():
    # Work in Q[u]/(u^3-q); m is the even support count of R12-S.
    u,q,m=sp.symbols('u q m')
    T=(q-1)*(u-1)
    E=q*q+q*u*(u-2)-(u-1)**2
    H=T/m;v=E/m-H*H
    moment=sp.expand(m*((H-u)**3+3*(H-u)*v)+(q-1-m)*(-u)**3)
    rem=sp.rem(moment,u**3-q,u)
    return dict(sign_third_moment=str(sp.factor(rem)),coefficients={str(k):str(sp.factor(rem.coeff(u,k))) for k in range(3)},
                note='Nonzero u or u^2 coefficient implies irrationality for prime q.')

if __name__=='__main__':
    result=dict(barrier=[barrier(u**3,J) for u,J in ((200,3),(400,5),(800,8))],fake_cubic=fake_cubic())
    (ROOT/'barrier_checks.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2),flush=True)
