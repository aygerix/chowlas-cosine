"""Certify one optimal positive-factor branch for A={1,...,5}.

Floating algebra only proposes a center and inverse Jacobian. Exact
rational intervals prove an invariant contraction box for the five
autocorrelation equations. A unit-circle factor proves optimality on
the entire circle, without a sampled minimum. Run on Dirichlet.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import socket
import sys

import mpmath as mp
import sympy as sp

from rational_box import I


def interval_poly(poly,box):
    result=I(0)
    for powers,coefficient in poly.terms():
        term=I(F(int(coefficient.p),int(coefficient.q)))
        for value,power in zip(box,powers):
            term=term*value**power
        result=result+term
    return result


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    variables=sp.symbols('a b d e c')
    a,b,d,e,c=variables
    q=[a,b-2*c*a,d-2*c*b+a,e-2*c*d+b,d-2*c*e,e]
    expressions=[sum(q[j]*q[j+lag] for j in range(6-lag))-sp.Rational(1,2)
                 for lag in range(1,6)]
    polys=[sp.Poly(expression,*variables) for expression in expressions]
    jpolys=[[sp.Poly(sp.diff(expression,var),*variables) for var in variables]
            for expression in expressions]
    function=sp.lambdify(variables,expressions,'mpmath')
    jacobian=sp.lambdify(variables,sp.Matrix(expressions).jacobian(variables),'mpmath')
    mp.mp.dps=110
    root=mp.findroot(function,(mp.mpf('1.04'),mp.mpf('1.43'),mp.mpf('1.126'),
                               mp.mpf('.48'),mp.mpf('.68')),tol=mp.mpf('1e-100'))
    denominator=10**70
    center=[F(int(mp.nint(value*denominator)),denominator) for value in root]
    inv=mp.inverse(jacobian(*root))
    R=[[F(int(mp.nint(inv[i,j]*denominator)),denominator) for j in range(5)]
       for i in range(5)]
    # Exact nonzero determinant is a separate rank check.
    assert sp.Matrix([[sp.Rational(v.numerator,v.denominator) for v in row]
                      for row in R]).det()!=0
    radius=F(1,10**45)
    box=[I(value-radius,value+radius) for value in center]
    F0=[interval_poly(poly,[I(v) for v in center]).lo for poly in polys]
    J=[[interval_poly(poly,box) for poly in row] for row in jpolys]
    error=[[I(int(i==j))-sum((R[i][k]*J[k][j] for k in range(5)),I(0))
            for j in range(5)] for i in range(5)]
    norm=max(sum(value.magnitude() for value in row) for row in error)
    assert norm<1
    images=[]
    for i in range(5):
        mid=center[i]-sum(R[i][j]*F0[j] for j in range(5))
        image=I(mid)+sum((entry*I(-radius,radius) for entry in error[i]),I(0))
        assert box[i].lo<image.lo and image.hi<box[i].hi
        images.append(image)
    qbox=[interval_poly(sp.Poly(expr,*variables),box) for expr in q]
    assert all(value.lo>0 for value in qbox)
    assert qbox[0].lo>1 and all(qbox[0].lo>value.hi for value in qbox[1:])
    assert -1<box[4].lo and box[4].hi<1
    lam=sum((value*value for value in qbox),I(0))
    assert lam.hi<2
    aa,bb,dd,ee,cc=box
    discriminant=18*ee*dd*bb*aa-4*dd**3*aa+dd**2*bb**2-4*ee*bb**3-27*ee**2*aa**2
    assert discriminant.hi<0
    def real_root_test(t):
        return aa-bb*t+dd*t*t-ee*t*t*t
    tlo,thi=F(1),F(2)
    assert real_root_test(tlo).lo>0 and real_root_test(thi).hi<0
    for _ in range(40):
        middle=(tlo+thi)/2
        test=real_root_test(middle)
        if test.lo>0:
            tlo=middle
        elif test.hi<0:
            thi=middle
        else:
            break
    tbox=I(tlo,thi)
    assert tbox.lo>1 and (aa/(ee*tbox)).lo>1
    reflected_q2=ee+tbox*dd-ee*tbox*tbox-2*cc*(dd-ee*tbox+aa)+aa/tbox
    assert reflected_q2.hi<0
    out=dict(host=socket.gethostname(),A=[1,2,3,4,5],unknown_order=list(map(str,variables)),
        parametrization='Q=(z²-2cz+1)*(a+bz+dz²+ez³)',
        center=list(map(str,center)),radius=str(radius),
        inverse_jacobian=[[str(value) for value in row] for row in R],
        contraction_norm_upper=str(norm),image_intervals=[v.serial() for v in images],
        q_intervals=[v.serial() for v in qbox],M_interval=lam.serial(),
        residual_cubic_discriminant=discriminant.serial(),
        negative_real_root_magnitude=tbox.serial(),
        complex_pair_modulus_squared=(aa/(ee*tbox)).serial(),
        real_reflected_q2=reflected_q2.serial(),
        all_nonnegative_factor_branches_have_qmax_gt_one=True,
        q0_display=float(qbox[0].lo),M_display=float(lam.lo),
        proof='Exact rational contraction box; autocorrelations1/2 and a unit-circle zero imply actual M=lambda',
        interpretation='Refutes qmax<=1 even after choosing any optimal nonnegative real factor; no unbounded-qmax family or refutation of every absolute C',
        python=sys.version,mpmath=mp.__version__,sympy=sp.__version__,status='PASS')
    path=Path('.research/experiments/optimal_endpoint_2026-10-23/n5.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',output=str(path),q0=out['q0_display'],
                         M=out['M_display'],all_circle_optimal=True)),flush=True)


if __name__=='__main__':
    main()
