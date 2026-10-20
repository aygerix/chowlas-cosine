"""Independent alias grouping and exact hypotheses for cone certificates.

Reconstructs matrices, groups unwanted Fourier terms by integer kernel
vectors, and rechecks the positive-measure lower bound at 160-bit precision.
Run on Dirichlet.
"""
from collections import defaultdict
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import flint
from cstar_integer_cone import cone_pairs


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=160
    root=Path('.research/experiments/cone_comparable_2026-10-20')
    search=json.loads((root/'results.json').read_text())
    certificates=json.loads((root/'alias.json').read_text())
    out=dict(qualification='Exact hypothesis and alias grouping checks; not an independent audit of the asymptotic proof.',
             sampled_hypotheses_checked=0,front_series_orders=12,cases=[])
    packing=95**3;threshold=30000000
    assert 3*threshold>=32*(45+3*packing)
    assert threshold>64*100*47**2
    out['theorem_constants']=dict(packing_bound=packing,X_threshold=threshold,
                                  long_direction_threshold_multiple=47,verified=True)
    for group in search['groups']:
        for row in group['cases']:
            C=row['C'];H=max(map(abs,C))
            assert math.gcd(*C)==1 and 10*min(map(abs,C))>=H
            assert abs(C[0]*C[3]-C[1]*C[2])<=H
            assert 64*H>=row['X']**3
            out['sampled_hypotheses_checked']+=1
    # Coefficients of the two rank-one-front expressions agree exactly.
    for k in range(13):
        direct=F((-1)**k*math.factorial(2*k),(k+1)*16**k*math.factorial(k)**4)
        squared=F((-1)**k,16**k*(k+1))*sum(
            F(1,math.factorial(j)**2*math.factorial(k-j)**2) for j in range(k+1))
        assert direct==squared
    assert 2*32**2<46**2
    for source,certificate in zip(search['global_probes'],certificates['cases']):
        X,C,A=source['X'],source['C'],source['A'];m=32*X;den=(m+1)**2
        mapping={}
        for u1,u2,w1,w2 in cone_pairs(X):
            M=(u1*w1,u1*w2,u2*w1,u2*w2)
            f=sum(a*b for a,b in zip(C,M))
            assert f and f not in mapping and -f not in mapping
            mapping[f]=M;mapping[-f]=tuple(-z for z in M)
        assert sorted(z for z in mapping if z>0)==A
        g=math.gcd(C[0],C[1])
        assert C[0]**2+C[1]**2>(47*X*g)**2
        by_r=[0]*(2*m+1);groups=defaultdict(int);alias_weight=0;main_count=0
        for r in range(-m,m+1):
            for s in range(-m,m+1):
                f=C[0]*r+C[1]*s
                if f==0:assert r==0 and s==0
                if f not in mapping:continue
                M=mapping[f];T=(r-M[0],s-M[1],-M[2],-M[3])
                weight=(m+1-abs(r))*(m+1-abs(s))
                by_r[r+m]+=weight
                if any(T):
                    assert sum(a*b for a,b in zip(C,T))==0
                    assert sum(z*z for z in T)<(47*X)**2
                    assert T[2] or T[3]
                    groups[T]+=1;alias_weight+=weight
                else:
                    main_count+=1
                    assert 0<r*r+s*s<=X*X
        assert len(groups)<=95**3
        assert all(count<=2*X+1 for count in groups.values())
        assert alias_weight==certificate['fejer']['alias_weight_numerator']
        H=sum((z*(flint.arb(5*r)/X).cos() for r,z in zip(range(-m,m+1),by_r)),flint.arb(0))/den
        lower=F(certificate['fejer']['M_lower_rational'])
        assert H+flint.arb(2*lower.numerator)/lower.denominator<0
        result=dict(X=X,n=len(A),alias_pairs=sum(groups.values()),kernel_groups=len(groups),
                    max_pairs_per_kernel=max(groups.values(),default=0),main_plane_points=main_count,
                    M_lower_rational=str(lower),verified=True)
        out['cases'].append(result);print(json.dumps(result),flush=True)
    critical=json.loads((root/'critical.json').read_text())['cases']
    out['critical_checks']=[]
    for row in critical:
        X,h,C=row['X'],row['moduli'],row['C'];P=math.prod(h)
        assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
        assert all(a*b==P for a,b in zip(h,C))
        assert min(h)**2>2*X*X
        assert C[0]*C[3]-C[1]*C[2]==8*P>max(C)
        j=row['root_of_unity']['j']
        assert all(j%m==r%m for r,m in zip([0,1,-1,0],h))
        assert all(v<=(47*X)**2 for v in row['primitive_row_column_squared'])
        out['critical_checks'].append(dict(X=X,n=row['n'],verified=True))
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
