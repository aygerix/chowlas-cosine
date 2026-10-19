"""Independent QQ/Sturm checks of the long-Gram theorem and exact witness."""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import json
from pathlib import Path
from fractions import Fraction as F
from math import comb
import sympy as s
from flint import arb,ctx
ctx.prec=180
OUT=Path('.research/agents/tdense9_scratch')

def bernstein(P,x,lo,hi):
    if P.is_zero:return [s.Integer(0)]
    n=P.degree();y=s.Symbol('y');Q=s.Poly(P.as_expr().subs(x,lo+(hi-lo)*y).expand(),y,domain=s.QQ)
    return [sum(Q.nth(j)*s.Rational(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
def ball(q):
    q=F(q);return arb(q.numerator)/arb(q.denominator)

def run():
    z=s.Symbol('z');u=s.Symbol('u');x=s.Symbol('x');lines=json.loads((OUT/'long_gram_bounds.json').read_text());lchecks=[]
    for r in lines:
        N=r['N'];ll=list(map(s.Rational,r['lambda_coefficients']));assert min(ll)>=0
        expr=s.chebyshevt(2,z)-s.Rational(r['m'])*z-s.Rational(r['b'])-sum(ll[n-3]*s.chebyshevt(n,z) for n in range(3,N+1))
        P=s.Poly(expr,z,domain=s.QQ);roots=int(P.count_roots(-1,1));ends=[P.eval(-1),P.eval(1)]
        assert roots==0 and min(ends)>0
        lchecks.append(dict(x0=r['x0'],degree=N,sturm_roots=roots,endpoints_positive=True))
    r=json.loads((OUT/'long_scalar_d24_exact.json').read_text());m=r['degree'];bb=list(map(s.Rational,r['beta_bernstein']));kap=s.Rational(r['kappa'])
    beta=s.expand(sum(bb[k]*s.binomial(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)))
    assert beta.subs(x,0)==0 and all(s.Poly(beta,x).nth(i)==s.Rational(v) for i,v in enumerate(r['beta_power']))
    derivative=s.Poly(s.diff(beta,x),x,domain=s.QQ);assert derivative.count_roots(s.Rational(-1,100000),1)==0 and derivative.eval(0)>0
    branches=[s.Integer(0),1-4*u*u+2*u**4,1-u-u*u]+[s.Rational(v['m'])*(1-u*u)+s.Rational(v['b']) for v in lines]
    assert all(s.expand(br)==sum(s.Rational(v)*u**i for i,v in enumerate(raw)) for br,raw in zip(branches,r['branches']))
    A=kap*(1-u*u)-1+u-beta.subs(x,1-u*u)/2
    polys=[s.Poly(s.cancel(A/(1-u)),u,domain=s.QQ)]+[s.Poly(A+beta.subs(x,b),u,domain=s.QQ) for b in branches[1:]]
    leaves=sorted(r['leaves'],key=lambda leaf:s.Rational(leaf['lo']));assert s.Rational(leaves[0]['lo'])==0 and s.Rational(leaves[-1]['hi'])==1
    for j,leaf in enumerate(leaves):
        lo=s.Rational(leaf['lo']);hi=s.Rational(leaf['hi']);k=leaf['branch']
        if j:assert s.Rational(leaves[j-1]['hi'])==lo
        args=bernstein(s.Poly(branches[k],u),u,lo,hi);vals=bernstein(polys[k],u,lo,hi)
        assert min(args)>=-s.Rational(1,100000) and max(args)<=1 and min(vals)>=0
    rr=F(769801,10**6);kk=F(r['kappa']);C=F(34683,5000);margin=4-rr*kk*C;assert margin>0
    w=json.loads((OUT/'witness_B160_full_factor.json').read_text());gg=w['factor_integers'];norm=sum(v*v for v in gg);B=w['B'];qq=list(map(F,w['q']))
    assert len(gg)==B and all(q>=0 for q in qq)
    for i in range(B):assert qq[i]==F(sum(gg[j]*gg[j+i] for j in range(B-i)),norm)
    db=arb(0)
    for aa,bb0 in zip(qq[:-1],qq[1:]):
        U=ball(1-aa);V=ball(1-bb0)
        if aa==bb0:mean=U.sqrt()
        else:mean=(arb(2)/3)*(U+(U*V).sqrt()+V)/(U.sqrt()+V.sqrt())
        db+=(1-mean)/2
    db*=ball(w['phi'])/B
    assert ball(w['density_lower'])<db and db<ball(w['density_upper'])
    upper=F(7267398825422,10**12);assert 1/F(w['density_lower'])<upper
    new=dict(status='PROVED exact QQ and Arb checks',long_gram=lchecks,scalar_degree=m,kappa=r['kappa'],monotonicity_sturm_roots=0,leaf_count=len(leaves),interval_cover=True,C_exact=str(4/(rr*kk)),C_float=float(4/(rr*kk)),concrete_C=str(C),concrete_margin=str(margin),elementary_C_exact=str(4/(F(811,1000)*kk)),elementary_C_float=float(4/(F(811,1000)*kk)),witness_factor_identity=True,witness_density_ball=str(db),witness_reach_upper=str(upper),witness_reach_upper_proved=True)
    (OUT/'long_independent_verification.json').write_text(json.dumps(new,indent=2));print(json.dumps(new,indent=2),flush=True)
if __name__=='__main__':run()
