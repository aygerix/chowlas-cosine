"""Independent endpoint-pair reconstruction and high-precision checks.

No imports from producers. Research computation only on Dirichlet.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import socket
import flint
import sympy as sp


def independent_geometry(X):
    bound=math.isqrt(math.isqrt(math.isqrt(X**5)))
    directions=sorted((a,b) for b in range(-bound,bound+1) for a in range(bound+1)
                      if (a>0 or b>0) and math.gcd(a,abs(b))==1
                      and a*a+b*b>=X and (a*a+b*b)**4<=X**5)
    cache={};fibers=[]
    for a,b in directions:
        q=X*X//(a*a+b*b)
        if q not in cache:
            r=math.isqrt(q)
            B=sorted((x,y) for y in range(-r,r+1) for x in range(-r,r+1) if x*x+y*y<=q)
            cache[q]=(B,set(B))
        B,S=cache[q];fibers.append((a,b,q,B,S))
    return fibers


def reconstruct(fibers,choices):
    assert len(fibers)==len(choices)
    matrices=[]
    for (a,b,q,B,S),i in zip(fibers,choices):
        assert 0<=i<len(B);t=B[i]
        for x in B:
            y=(2*t[0]-x[0],2*t[1]-x[1])
            if y not in S:continue
            w=(x[0]-t[0],x[1]-t[1])
            if w[0]>0 or (w[0]==0 and w[1]>0):
                matrices.append((a*w[0],a*w[1],b*w[0],b*w[1]))
    assert matrices and len(matrices)==len(set(matrices))
    return matrices


def enc(X):
    h=[6*X**3+i for i in [1,3,5,7]];P=math.prod(h);C=[P//m for m in h]
    assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
    return h,P,C


def value(matrices,h,residues):
    P=math.prod(h);counts=Counter()
    for M in matrices:
        r=sum(z*m*(P//modulus) for z,m,modulus in zip(residues,M,h))%P
        counts[min(r,P-r)]+=1
    return sum((count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P))
                for r,count in counts.items()),flint.arb(0))


def check_point(matrices,X,row):
    h,P,C=enc(X);A=sorted(abs(sum(c*m for c,m in zip(C,M))) for M in matrices)
    assert all(M[0]*M[3]==M[1]*M[2] and sum(z*z for z in M)<=X*X for M in matrices)
    assert A[0]>0 and len(A)==len(set(A)) and row.get('n',len(A))==len(A)
    assert all(j>=0 for j in A)
    assert row['q']==P and all(row['j']%m==z%m for m,z in zip(h,row['residues']))
    assert hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest()==row['encoded_set_sha256']
    upper=F(row['f_over_n_upper_rational']);v=value(matrices,h,row['residues'])
    assert v<flint.arb(upper.numerator)*len(A)/upper.denominator
    assert F(row['M_lower_rational'])==max(F(0),-len(A)*upper)


def exact_parity(fiber):
    a,b,q,B,S=fiber
    via_centers=Counter();via_pairs=Counter()
    for t in B:
        for x in B:
            y=(2*t[0]-x[0],2*t[1]-x[1])
            if y in S:via_centers[(x[0]-t[0],x[1]-t[1])]+=1
    for x in B:
        for y in B:
            if (x[0]-y[0])%2==0 and (x[1]-y[1])%2==0:
                via_pairs[((x[0]-y[0])//2,(x[1]-y[1])//2)]+=1
    assert via_centers==via_pairs and via_centers[(0,0)]==len(B)
    return dict(q=q,disk_points=len(B),coefficients=len(via_pairs),verified=True)


def expected_mean_certificate(fibers,X,residues):
    h,P,C=enc(X);mean=flint.arb(0);maximum_n=0
    for a,b,q,B,S in fibers:
        maximum_n+=(len(B)-1)//2
        parts=[(flint.arb(0),flint.arb(0)) for _ in range(4)]
        for x,y in B:
            # q_u.z/2 uses half of the original matrix phase. This direct
            # parity square avoids summing all center/window pairs.
            rational=F(residues[0]*a*x,h[0])+F(residues[1]*a*y,h[1])+F(residues[2]*b*x,h[2])+F(residues[3]*b*y,h[3])
            angle=flint.arb.pi()*rational.numerator/rational.denominator
            index=2*(x%2)+(y%2);re,im=parts[index]
            parts[index]=(re+angle.cos(),im+angle.sin())
        mean+=sum((re*re+im*im for re,im in parts),flint.arb(0))/len(B)-1
    upper=F(math.ceil(float(mean.mid())*10**6)+2,10**6)
    assert mean<flint.arb(upper.numerator)/upper.denominator and upper<-F(len(fibers),2)
    expected_M_lower=-upper/2
    sqrt_upper=math.isqrt(maximum_n)+int(math.isqrt(maximum_n)**2<maximum_n)
    return dict(fibers=len(fibers),max_n=maximum_n,mean_D_upper_rational=str(upper),
                expected_M_lower_rational=str(expected_M_lower),
                fractional_mean_M_lower_rational=str(expected_M_lower),
                fractional_mean_M_global_upper_rational=str(F(len(fibers),2)),
                expected_R_lower_rational=str(expected_M_lower/sqrt_upper),
                qualification='Expectation bounds for ANY coupling with the specified coefficient marginals; '
                              'not a deterministic bound on each output.',verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=192
    root=Path('.research/experiments/fiber_centers_2026-10-20')
    independent=json.loads((root/'independent.json').read_text())
    # A second exact sign algorithm (Sturm) rather than producer Bernstein.
    x=sp.symbols('x');P=sum((-1)**k*x**k/sp.Integer(math.factorial(k)*math.factorial(k+1)) for k in range(22))
    poly=sp.Poly(P-sp.Rational(1,100),x)
    lo,hi=sp.Rational(361,25),sp.Rational(1521,100)
    assert poly.count_roots(lo,hi)==0 and poly.eval(lo)>0
    def endpoint(t,n):
        return sum((F((-1)**k,math.factorial(k)*math.factorial(k+1))*(t*t/4)**k
                    for k in range(n+1)),F(0))
    assert endpoint(F(19,5),21)>0 and endpoint(F(39,10),20)<0
    assert 57344*F(1,300)**2<1
    out=dict(qualification='Independent finite exact endpoint-pair/hash checks and 192-bit point/floor verification; '
             'not an independent-agent or Lean audit of the asymptotic theorem.',
             python=platform.python_version(),flint=flint.__version__,arb_precision=flint.ctx.prec,
             root_sign_sturm_verified=True,origin_fiber_tradeoff_constant_verified=True,
             independent_samples=[],correlated=[],countercontrol=[])
    geometries={}
    for row in independent['cases']:
        X=row['X'];fibers=independent_geometry(X);geometries[X]=fibers
        assert len(fibers)==row['fibers']
        assert all(a*a+b*b>=X and (a*a+b*b)**4<=X**5 for a,b,q,B,S in fibers)
        matrices=reconstruct(fibers,row['best_choices']);check_point(matrices,X,row['point'])
        parity=[exact_parity(fibers[i]) for i in sorted({0,len(fibers)//2,len(fibers)-1})]
        result=dict(X=X,n=len(matrices),hash_and_point_verified=True,parity=parity,
                    any_coupling_mean=expected_mean_certificate(fibers,X,row['point']['residues']))
        out['independent_samples'].append(result);print(json.dumps(result),flush=True)
    correlated=json.loads((root/'correlated.json').read_text());X=correlated['X'];fibers=geometries[X]
    h,P,C=enc(X)
    for row in correlated['rounds']:
        assert all(i in options for i,options in zip(row['choices'],correlated['option_center_indices']))
        matrices=reconstruct(fibers,row['choices']);assert len(matrices)==correlated['target_n']
        cert=row['finite_floor'];floor=F(cert['B_rational'])
        assert len(cert['target_residues'])==row['targets']
        for residues in cert['target_residues']:
            assert value(matrices,h,residues)+flint.arb(floor.numerator)/floor.denominator>0
        check_point(matrices,X,row['adversarial_point'])
        result=dict(iteration=row['iteration'],n=len(matrices),listed_floors_verified=True,
                    missed_negative_point_verified=True)
        out['correlated'].append(result);print(json.dumps(result),flush=True)
    control=json.loads((root/'countercontrol.json').read_text())
    for row in control['cases']:
        X=row['X'];fibers=geometries[X];classes={(1,0),(4,0),(0,1),(0,4),(1,1),(4,4)}
        for (a,b,q,B,S),i in zip(fibers,row['choices']):
            assert B[i]==((0,0) if (a%5,b%5) in classes else max(B))
        matrices=reconstruct(fibers,row['choices']);assert len(matrices)==row['n']
        h,P,C=enc(X);lower=F(row['grid_f_over_n_lower_rational'])
        for residues in row['zero_circle_targets']:
            assert value(matrices,h,residues)>flint.arb(lower.numerator)*len(matrices)/lower.denominator
        check_point(matrices,X,row['t5_point'])
        assert F(row['t5_point']['M_lower_rational'])>F(len(matrices),16)
        result=dict(X=X,n=len(matrices),full_empty_choices_verified=True,
                    listed_positive_curve_bounds_verified=True,t5_negative_verified=True)
        out['countercontrol'].append(result);print(json.dumps(result),flush=True)
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
