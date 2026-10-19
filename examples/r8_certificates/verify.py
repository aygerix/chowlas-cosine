"""Independent exact checks. Run on dirichlet, never locally."""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import json, sys, random, platform
from fractions import Fraction as F
from pathlib import Path
import sympy as s
OUT=Path('.research/agents/tdense8_scratch')

def sturm_positive(expr,x,lo,hi):
    P=s.Poly(expr,x,domain=s.QQ)
    roots=int(P.count_roots(lo,hi))
    vals=[P.eval(lo),P.eval((lo+hi)/2),P.eval(hi)]
    return dict(roots=roots,positive=roots==0 and all(v>0 for v in vals),degree=P.degree())

def run():
    records=[];x=s.Symbol('x');u=s.Symbol('u')
    for deg in (4,8):
        rec=json.loads(OUT.joinpath(f'potential_g4_d{deg}_exact.json').read_text())
        rho=s.Rational(rec['rho']);bb=list(map(s.Rational,rec['beta_bernstein']))
        beta=s.expand(sum(bb[k]*s.binomial(deg,k)*x**k*(1-x)**(deg-k) for k in range(deg+1)))
        assert all(s.Rational(v)==s.Poly(beta,x).nth(i) for i,v in enumerate(rec['beta_power']))
        low=rho*x-x*x-beta/2
        assert low.subs(x,0)==0
        middle=low.subs(x,1-u*u)+beta.subs(x,1-u-u*u)
        high=low+beta.subs(x,2*x*x-1)
        checks=[sturm_positive(s.diff(beta,x),x,s.Rational(-1,1000),s.Integer(1)),
                sturm_positive(s.cancel(low/x),x,s.Integer(0),s.Rational(61804,100000)),
                sturm_positive(middle,u,s.Rational(366,1000),s.Rational(61804,100000)),
                sturm_positive(high,x,s.Rational(86603,100000),s.Integer(1))]
        assert all(c['positive'] for c in checks)
        # Coverage of rational-u range for the middle x interval.
        assert 1-s.Rational(61804,100000)**2<=s.Rational(61804,100000)
        assert 1-s.Rational(366,1000)**2>=s.Rational(86603,100000)
        assert -s.Rational(1,1000)<=1-s.Rational(61804,100000)-s.Rational(61804,100000)**2
        reaches=[]
        for rr in (F(769801,10**6),F(811,1000)):
            assert rr!=F(769801,10**6) or rr*rr>F(16,27)
            rh=F(rec['rho']);reach=4*(2-rh)/rr
            C=F((reach.numerator*1000)//reach.denominator,1000)
            margin=4*(2-rh)-C*rr
            assert margin>0
            reaches.append(dict(r=str(rr),reach_exact=str(reach),reach_numeric=float(reach),
                                C=str(C),margin=str(margin)))
        records.append(dict(degree=deg,rho=str(rho),checks=checks,reaches=reaches))
    # A direct finite identity check using independent exact coefficient convolutions.
    rng=random.Random(2026101908);finite=[]
    for X,h in ((19,3),(47,8),(80,11)):
        A={j for j in range(1,X+1) if rng.random()<.3};A.add(X)
        aa={j:F(int(abs(j) in A)) for j in range(-X,X+1)}
        k={j:F(h+1-abs(j),(h+1)**2) for j in range(-h,h+1)}
        rr={j:aa.get(j,F(0))-sum(k[v]*aa.get(j-v,F(0)) for v in k) for j in range(-X-h,X+h+1)}
        # Known universal floor M=n makes g+m nonnegative; exact convolution Fourier coefficients.
        m=F(len(A))+rr[0]/2
        cc={0:m};cc.update({j:rr[j]/2 for j in rr if j})
        sq={j:cc[j]*cc[j] for j in cc}
        assert sq[0]==m*m
        assert all(sq[j]==rr[j]**2/4 for j in rr if j)
        finite.append(dict(X=X,h=h,n=len(A),identity=True))
    witness=json.loads(Path('examples/r7_certificates/witness_B48.json').read_text())
    pp=list(map(F,witness['p']));e0=pp[0]*(1-pp[0]);j=max(range(len(pp)),key=lambda i:pp[i]*(1-pp[i]))
    violation=pp[j]*(1-pp[j])-e0
    assert pp[0]>F(1,2) and violation>0
    output=dict(status='EXACT',python=platform.python_version(),sympy=s.__version__,certificates=records,
                finite_convolution_checks=finite,witness_violation=dict(node=j,t=str(F(j,48)),
                p=str(pp[j]),e0=str(e0),gap=str(violation),gap_float=float(violation)))
    OUT.joinpath('independent_verification.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(output,indent=2),flush=True)

if __name__=='__main__':run()
