from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
"""Exact symbolic audit of the continuum shape integrals (no numerical fitting)."""
import sympy as s
x,y=s.symbols('x y')
d=lambda z:2*(1-z)
h=lambda z:s.Rational(2,3)*(1-z)**2*(2+z)
def tri(f):return s.integrate(s.integrate(s.expand(f),(y,0,1-x)),(x,0,1))
J11=6*tri(d(x)*d(y)*d(x+y))
J12=2*tri(d(x)*d(y)*h(x+y)+2*d(x)*d(x+y)*h(y))
J22=2*tri(d(x+y)*h(x)*h(y)+2*d(x)*h(y)*h(x+y))
J=s.Matrix([[J11,J12],[J12,J22]])
assert J==s.Matrix([[s.Rational(22,5),s.Rational(736,315)],[s.Rational(736,315),s.Rational(2369,1890)]])
assert J.det()==s.Rational(5543,99225)
assert 4*J.inv()[0,0]==s.Rational(21630,241)
conv=s.expand(2*s.integrate(h(y)*h(y-x),(y,x,1))+s.integrate(h(y)*h(x-y),(y,0,x)))
assert conv==x**7/s.Integer(105)-2*x**5/s.Integer(5)+4*x**4/s.Integer(9)+4*x**3/s.Integer(3)-32*x**2/s.Integer(15)+s.Rational(88,105)
assert 2*s.integrate(d(x)*h(x),(x,0,1))==s.Rational(22,15)
assert 2*s.integrate(h(x)**2,(x,0,1))==s.Rational(88,105)
print('J=',J,'det=',J.det(),'constant=',4*J.inv()[0,0], 'all exact checks passed')
