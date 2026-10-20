"""Changed-window probe: box rank-one cone at the minimum balanced base.

All calculations run on Dirichlet. Arb DFT evaluations give rigorous point
lower bounds on M, not global upper bounds or asymptotic extrapolations.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint


def box_set(X):
    B=2*X+1;A=[]
    for u1 in range(X+1):
        for u2 in range(-X,X+1):
            if u1==0 and u2<=0:continue
            if math.gcd(u1,abs(u2))!=1:continue
            H=max(u1,abs(u2))
            if not H:continue
            radius=X//H
            for w1 in range(radius+1):
                for w2 in range(-radius,radius+1):
                    if w1==0 and w2<=0:continue
                    A.append(abs((u1+B*B*u2)*(w1+B*w2)))
    A.sort()
    assert A[0]>0 and len(set(A))==len(A)
    expected=8*sum(sum(math.gcd(a,H)==1 for a in range(1,H+1))
                   *(X//H)*((X//H)+1) for H in range(1,X+1))
    assert len(A)==expected
    return A


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=96
    path=Path('.research/experiments/integer_cone_2026-10-20/box.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    out=dict(qualification='Finite certified negative witnesses only; no global upper bound or infinite-family conclusion.',cases=[])
    for X in [8,16,32,64]:
        B=2*X+1;A=box_set(X);n=len(A);rows=[]
        for c in range(-3,4):
            q=B*B+c*B+1
            counts=Counter(a%q for a in A)
            z=[flint.acb(0)]*q
            for a,count in counts.items():z[a]=flint.acb(count)
            values=flint.acb.dft(z)
            j=min(range(q),key=lambda k:float(values[k].real.mid()))
            point=values[j].real
            scale=10**6
            upper=F(math.ceil(float(point.mid())/n*scale)+1,scale)
            assert point<flint.arb(upper.numerator)*n/upper.denominator
            lower=max(F(0),-n*upper)
            row=dict(c=c,root_of_unity=dict(numerator=j,denominator=q),
                     f_over_n_upper_rational=str(upper),M_lower_rational=str(lower),
                     R_lower_float=float(lower)/math.sqrt(n),verified=True)
            rows.append(row)
        best=max(rows,key=lambda r:r['R_lower_float'])
        result=dict(X=X,B=B,n=n,max_A=A[-1],
                    encoded_set_sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                    cases=rows,best=best,arb_precision=96,flint_version=flint.__version__)
        out['cases'].append(result)
        path.write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(dict(X=X,n=n,best=best)),flush=True)


if __name__=='__main__':main()
