"""Pure Arb all-window P28 and all-circle M; exact integer graph positivity.

Run ONLY on dirichlet via src/dirun.sh, at most four cores.
No optimizer. The input is the saved round 17 36-element certificate minimizer.
"""
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import flint
import numpy as np

sys.path.insert(0, '.research/agents/tdense18_scratch')
from probe18 import boundary, PI_HI

ROOT = Path('.research/agents/tdense18_scratch')
SOURCE = Path('.research/agents/tdense17_scratch/search_smallN_36.npz')


def rational_up(value):
    """An outward binary64 endpoint, saved as an exact rational."""
    return Fraction.from_float(math.nextafter(float(value.upper()), math.inf))


def full_triangular_p28(A, G):
    X = max(A)
    best = Fraction(0)
    rows = []
    start = time.time()
    for H in range(1, X+1):
        sup = [Fraction(0)]*G
        max_derivative = Fraction(0)
        for m in range(H, X+H):
            coeff = {a:max(0,H-abs(a-m)) for a in A}
            coeff = {a:w for a,w in coeff.items() if w}
            if not coeff:
                continue
            c = [flint.acb(0)]*G
            for a,w in coeff.items():
                c[a] = flint.acb(w)
            vals = flint.acb.dft(c)
            for j,z in enumerate(vals):
                u = rational_up(abs(z)) / H
                if u > sup[j]:
                    sup[j] = u
            max_derivative = max(max_derivative,
                Fraction(sum(a*w for a,w in coeff.items()), H))
        # Mean distance to the center of a length-2pi/G cell is pi/(2G).
        bound = sum(sup,Fraction(0))/(2*G) + max_derivative*PI_HI/(4*G)
        best = max(best,bound)
        rows.append(dict(H=H,upper=str(bound),decimal=float(bound),
                         max_derivative=str(max_derivative)))
        if H%5 == 0 or H == X:
            print(json.dumps(dict(H=H,p28_upper=float(best),seconds=time.time()-start)),flush=True)
        (ROOT/'full_p28_progress.json').write_text(json.dumps(dict(grid=G,rows=rows,
            upper=str(best)),indent=2)+'\n')
    return dict(grid=G,upper=str(best),decimal=float(best),rows=rows,
                all_H_reduction='H>=X dominated exactly by H=X')


def graph_certificate(A, bound):
    # Assert M_P9(W2) <= bound by proving 2*bound*I + H_W2 positive definite.
    S = set(A)
    W = sorted({0} | S | {-a for a in A})
    t = 2*bound
    den = t.denominator
    num = t.numerator
    matrix = flint.fmpz_mat([[num if i == j else den*int(abs(i-j) in S)
        for j in W] for i in W])
    p = matrix.charpoly()
    size = len(W)
    # det(xI+matrix)=(-1)^size charpoly(-x) has positive coefficients.
    # Symmetry makes all eigenvalues real; no root on [0,infinity)
    # therefore means every eigenvalue of matrix is strictly positive.
    coefficients = [int(p[j])*(-1)**(size+j) for j in range(size+1)]
    assert all(c>0 for c in coefficients)
    record = dict(size=size,shift=str(t),integer_scale=den,
                  charpoly_plus_coefficients=list(map(str,coefficients)),
                  all_coefficients_positive=True)
    (ROOT/'graph_exact.json').write_text(json.dumps(record,indent=2)+'\n')
    return dict(size=size,certificate='graph_exact.json',shift=str(t),passed=True)


def certify_M(A, xmin, G=32768):
    c = [flint.acb(0)]*G
    for a in A:
        c[a] = flint.acb(1)
    vals = flint.acb.dft(c)
    # At a global minimizer f'=0; compare to its nearest grid point.
    lo = min(z.real.lower() for z in vals)
    upper_ball = -lo+flint.arb(sum(a*a for a in A))*flint.arb.pi()**2/(2*G*G)
    upper = rational_up(upper_ball)
    xx = Fraction(str(xmin))
    x = flint.arb(xx.numerator)/xx.denominator
    point = sum(((a*x).cos() for a in A),flint.arb(0))
    lower = -rational_up(point)
    return dict(lower=str(lower),upper=str(upper),lower_decimal=float(lower),
                upper_decimal=float(upper),grid=G,point_x_rational=str(xx),
                point_enclosure=str(point),
                method='Arb DFT and nearest-global-minimizer second derivative; independent Arb point')


def main():
    start = time.time()
    flint.ctx.prec = 100
    A = np.load(SOURCE)['A'].tolist()
    assert len(A)==36 and len(set(A))==36
    records = json.load(open('.research/agents/tdense17_scratch/fourway_search.json'))
    row = next(r['fine'] for r in records if r['start']=='smallN_36')
    xmin = row['xmin_est']
    # Every assertion is checked after computation, not presumed from estimates.
    bound = Fraction(27,10)  # epsilon=9/20, sqrt(n)=6; adjust only with evidence.
    graph = graph_certificate(A,bound)
    edge = boundary(A)
    assert Fraction(edge['upper_rational']) < bound
    minimum = certify_M(A,xmin)
    assert Fraction(minimum['lower']) > bound
    print(json.dumps(dict(stage='M_and_graph',M=minimum,graph=graph,boundary=edge)),flush=True)
    G = int(sys.argv[1]) if len(sys.argv)>1 else 8192
    p28 = full_triangular_p28(A,G)
    result = dict(A=A,n=len(A),X=max(A),epsilon='9/20',threshold=str(bound),
                  M=minimum,graph=graph,boundary=edge,p28=p28,
                  all_certificates_below_threshold=Fraction(p28['upper'])<bound,
                  sha256=hashlib.sha256(np.array(A,dtype='<i8').tobytes()).hexdigest(),
                  seconds=time.time()-start,precision=100,flint=flint.__version__)
    (ROOT/'reverse_separation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='p28'}),flush=True)
    print(json.dumps(dict(p28_upper=p28['decimal'],threshold=float(bound),
                         passed=result['all_certificates_below_threshold'])),flush=True)


if __name__=='__main__':
    main()
