"""Exact verification of the saved threshold-deletion miss; run on Dirichlet."""
from collections import defaultdict
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import sympy as sp
from box_minlam import true_min


def evaluate(A, t):
    values=[F(1),t]
    for k in range(2,max(A)+1):
        values.append(2*t*values[-1]-values[-2])
    return sum(values[a] for a in A)


def witness(A):
    _, x = true_min(A,over=64)[0]
    t=F(round(math.cos(x)*10**7),10**7)
    value=evaluate(A,t)
    assert value<0
    return t,value


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run on Dirichlet through src/dirun.sh')
    path=Path('.research/experiments/dual_deletion_2026-10-20')
    miss=json.loads((path/'probe.json').read_text())['miss']
    A=miss['A'];B=miss['known_improving_subset'];n=len(A)
    row=miss['parent_completion'];cert=row['exact_primal'];c=cert['positive_coefficients'];bound=len(c)
    coefficients={s:v for a,v in enumerate(c,start=1) if v for s in [-a,a]}
    squared=defaultdict(int)
    for a,u in coefficients.items():
        for b,v in coefficients.items():squared[a+b]+=u*v
    cube=defaultdict(int)
    for a,u in squared.items():
        for b,v in coefficients.items():cube[a+b]+=u*v
    weights={a:cube[a] for a in A}
    assert all(str(weights[a])==miss['weights'][str(a)] for a in A)
    order=sorted(A,key=lambda a:(weights[a],a))
    expected={tuple(sorted(order[:k])) for k in range(1,n)}|{tuple(sorted(order[-k:])) for k in range(1,n)}
    actual={tuple(r['A']) for r in miss['thresholds']}
    assert actual==expected
    t=sp.symbols('t')
    P=sum(sp.chebyshevt(a,t) for a in A)
    estimate=-true_min(A,over=64)[0][0]
    upper=F(math.ceil(estimate*10**6)+1,10**6)
    parentpoly=sp.Poly(P+sp.Rational(upper.numerator,upper.denominator),t)
    assert parentpoly.eval(0)>0 and parentpoly.count_roots(-1,1)==0
    tw,vl=witness(A)
    assert len(B)*vl*vl>4*n
    PB=sp.Poly(2+sum(sp.chebyshevt(a,t) for a in B),t)
    quotient,remainder=sp.div(PB,sp.Poly(t+1,t))
    assert remainder.is_zero and quotient.eval(0)>0 and quotient.count_roots(-1,1)==0
    assert evaluate(B,F(-1))==-2
    checks=[]
    for subset in sorted(expected,key=lambda z:(len(z),z)):
        w,v=witness(list(subset))
        assert n*v*v>len(subset)*upper*upper
        checks.append(dict(A=list(subset),t=str(w),value=str(v),
                           comparison='n*f_subset(t)^2 > |subset|*parent_upper^2',verified=True))
    out=dict(status='exact rational/Sturm counterexample to this computed rational-dual threshold heuristic',
             A=A,known_improving_subset=B,subset_M_exact='2',parent_M_upper=str(upper),
             parent_lower_witness=dict(t=str(tw),value=str(vl)),
             parent_positivity_root_count=0,threshold_count=len(checks),
             dual_weights_exact={str(a):str(v) for a,v in weights.items()},thresholds=checks,
             qualification='The dual candidate is derived from a finite-degree completion. This does not certify the ordering of the true unrestricted optimizer or refute a large-cost theorem for exact minimizers.')
    (path/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['dual_weights_exact','thresholds']},indent=2))


if __name__=='__main__':main()
