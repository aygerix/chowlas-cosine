"""Independent exact Sturm reconstruction of scalar certificates + effective constants."""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import sys,json,platform
from pathlib import Path
from fractions import Fraction as F
import sympy as sp
OUT=Path('.research/agents/tdense9_scratch')

def ceilrat(v):return -((-v.numerator)//v.denominator)
def pow10ceil(q):
    # Exact ceil(log10(q)), q positive, no floating transcendental arithmetic.
    if q<=1:return 0
    v=len(str(q.numerator))-len(str(q.denominator));v=max(v,0)
    while F(10**v)<q:v+=1
    return v

def check_certificates():
    u=sp.Symbol('u');x=sp.Symbol('x');rows=[]
    for m in (4,8,12,24):
        path=OUT/f'scalar_d{m}_exact.json'
        if not path.exists():continue
        r=json.loads(path.read_text());assert r['status']=='PROVED'
        kap=sp.Rational(r['kappa']);bb=list(map(sp.Rational,r['beta_bernstein']))
        beta=sp.expand(sum(bb[k]*sp.binomial(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)))
        assert beta.subs(x,0)==0
        assert all(sp.Poly(beta,x).nth(i)==sp.Rational(v) for i,v in enumerate(r['beta_power']))
        A=kap*(1-u*u)-1+u-beta.subs(x,1-u*u)/2
        exprs=[(sp.diff(beta,x),x,sp.Rational(-1,100000),sp.Integer(1)),
               (A+beta.subs(x,1-4*u*u+2*u**4),u,sp.Integer(0),sp.Rational(366026,10**6)),
               (A+beta.subs(x,1-u-u*u),u,sp.Rational(366025,10**6),sp.Rational(618035,10**6)),
               (sp.cancel(A/(1-u)),u,sp.Rational(618033,10**6),sp.Integer(1))]
        checks=[]
        for p,v,l,h in exprs:
            poly=sp.Poly(p,v,domain=sp.QQ);n=int(poly.count_roots(l,h));vs=[poly.eval(l),poly.eval((l+h)/2),poly.eval(h)]
            assert n==0 and min(vs)>0
            checks.append(dict(degree=poly.degree(),roots=n,positive_endpoints=True))
        # Enlarged middle beta argument remains inside monotonicity interval.
        assert 1-sp.Rational(618035,10**6)-sp.Rational(618035,10**6)**2>=-sp.Rational(1,100000)
        rr=F(769801,10**6);reach=4/(rr*F(r['kappa']))
        rows.append(dict(degree=m,kappa=r['kappa'],checks=checks,C_exact=str(reach),C_float=float(reach)))
    return rows

def effective():
    eta=sp.Symbol('eta');a=sp.Symbol('a');rho=sp.Rational(203819,250000)
    def positive(p,v,l,h):
        P=sp.Poly(p,v,domain=sp.QQ)
        return dict(roots=int(P.count_roots(l,h)),positive=bool(P.eval(l)>0 and P.eval(h)>0 and P.count_roots(l,h)==0))
    checks={
      'F_increasing':positive(1-2*a+rho*a*a,a,0,sp.Rational(501,1000)),
      'F_derivative_le4':positive(4*(1-rho*a)**2-(1-2*a+rho*a*a),a,0,sp.Rational(501,1000)),
      'denominator_ge_half':bool(1-rho*sp.Rational(501,1000)>sp.Rational(1,2)),
      'F0_ge_point4':bool(1/(2*(2-rho))>sp.Rational(2,5)),
      'crossing_bound':bool(sp.Rational(56)+sp.Rational(2,4000)+sp.Rational(49,10**8)<64),
      'omega_bound':bool(sp.Rational(12,10**8)<1),
      'pigeonhole_bound':bool(sp.Rational(42,400000)<1),
      'final_error':bool(sp.Rational(720,10**8)*sp.Rational(1,1000)<sp.Rational(4,5)),
      'lower_t_998':bool(sp.Rational(999,1)/sp.Rational(1001,1000)>998)
    }
    assert all(v.get('positive',False) if isinstance(v,dict) else v for v in checks.values())
    rows=[]
    for C,rr,base,D in [(F(3),F(77,100),F(769801,10**6),21),(F(5),F(77,100),F(769801,10**6),21),(F(6),F(77,100),F(769801,10**6),21),(F(123,20),F(77,100),F(769801,10**6),21),(F(29,5),F(203,250),F(811,1000),1)]:
        rh=F(203819,250000);g=4*(2-rh)/(rr*C)-1;assert g>0
        et=min(F(1,1000),g/1000);J=ceilrat(F(10**8)/(et*et));X0=ceilrat((F(D)/(rr-base))**2)+100
        E=2+pow10ceil(F(4*J*(X0+1))/et)+3*J*pow10ceil(F(J))
        rows.append(dict(C=str(C),r=str(rr),base_upper=str(base),D=D,X0=X0,eta=str(et),J=J,
                         c_power10_exponent=E,c=f'10^(-{E})',status='PROVED rational comparisons'))
    return dict(checks=checks,examples=rows)

if __name__=='__main__':
    rec=dict(status='EXACT',python=platform.python_version(),sympy=sp.__version__,scalar=check_certificates(),effective=effective())
    OUT.joinpath('independent_verification.json').write_text(json.dumps(rec,indent=2))
    print(json.dumps(rec,indent=2),flush=True)
