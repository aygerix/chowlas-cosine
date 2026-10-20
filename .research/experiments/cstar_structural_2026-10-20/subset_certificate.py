from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
"""Exact arithmetic certification; floating roots only propose rational witnesses."""
import itertools,json
import sympy as s
from numpy.polynomial import Chebyshev
A=[1,2,3,4,5,6,7,9]; t=s.symbols('t')
P=2+sum(s.chebyshevt(a,t) for a in A)
Q=s.div(P,t+1)[0]
assert s.expand(P-(t+1)*Q)==0
assert Q.subs(t,0)>0 and s.Poly(Q,t).count_roots(-1,1)==0
assert P.subs(t,-1)==0
witnesses=[]
for n in range(1,8):
 for B in itertools.combinations(A,n):
  p=Chebyshev([0]+[int(a in B) for a in range(1,max(B)+1)])
  ts=[-1.,1.]+[r.real for r in p.deriv().roots() if abs(r.imag)<1e-8 and -1<r.real<1]
  z=min(ts,key=p); num=round(10000*z); z=s.Rational(num,10000)
  v=sum(s.chebyshevt(a,z) for a in B)
  assert v<0 and 2*v*v>n,(B,z,v)
  witnesses.append({'A':B,'t_numerator':num,'t_denominator':10000})
json.dump(witnesses,open(str(HERE / 'subset_certificate.json'),'w'))
print('Certified M(A)=2 by Sturm and strict hereditary ratio-minimality by',len(witnesses),'exact rational witnesses.')
