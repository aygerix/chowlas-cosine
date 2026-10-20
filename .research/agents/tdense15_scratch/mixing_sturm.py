"""Independent exact algebraic certificate; run on the VM only."""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
s = sp.symbols('s')
a, b = sp.Rational(233809, 10**6), sp.Rational(117344, 10**6)
R = 1-a-2*b+a*s+2*b*s*s
assert all(c > 0 for c in sp.Poly(R, s).all_coeffs())
H = sp.Poly((1+2*s*s)/3-R**2, s)
T, rem = sp.div(H, sp.Poly(1-s, s))
assert rem.is_zero and T.eval(0) > 0 and T.eval(1) > 0
sturm = sp.sturm(T.as_expr(), s)
def variations(x):
    signs = [sp.sign(p.subs(s, x)) for p in sturm]
    signs = [int(v) for v in signs if v]
    return sum(v != w for v, w in zip(signs, signs[1:]))
v0, v1 = variations(0), variations(1)
assert v0 == v1 and T.count_roots(0, 1) == 0
result = dict(status='PROVED', substitution='s=sqrt(1-x)',
              R=str(R), H=str(H.as_expr()), T=str(T.as_expr()),
              sturm=list(map(str, sturm)), variations=[v0, v1],
              T0=str(T.eval(0)), T1=str(T.eval(1)),
              meaning='sqrt((1+2s^2)/3)>=R(s)>=0; squaring is equivalent')
ROOT.joinpath('mixing_sturm.json').write_text(json.dumps(result, indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='sturm'}, indent=2))
