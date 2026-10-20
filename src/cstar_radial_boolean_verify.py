"""Independent exact quantization and reverse-factor lens verification.

Uses no producer imports. Research computation only on Dirichlet.
"""
from collections import Counter,defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import socket
import flint


def line_minimum(p):
    l=len(p)
    return min(sum((F(z)-a)**2 for z,a in zip(bits,p))
               -sum((F(z)-a for z,a in zip(bits,p)),F(0))**2/l
               for bits in itertools.product([0,1],repeat=l))


def verify_quantization(root):
    source=json.loads((root/'quantization.json').read_text())
    for row in source['line_tests']:
        b=list(map(F,row['p']));D=line_minimum(b)
        assert D==F(row['minimum'])>=F(row['pair_lower'])
        if max(b)-min(b)<=F(1,2):assert D==sum(z*z for z in b)-sum(b)**2/len(b)
    cases=[];cache={}
    for row in source['cone_tests']:
        p=row['prime'];key=(p,row['profile']);values=list(map(F,row['profile_values']))
        if key not in cache:
            Q=[M for M in itertools.product(range(p),repeat=4) if (M[0]*M[3]-M[1]*M[2])%p==0]
            lines=[(1,t) for t in range(p)]+[(0,1)];order=[];groups=defaultdict(list)
            def norm(a,b):
                divisor=a or b;inv=pow(divisor,-1,p)
                return (a*inv%p,b*inv%p)
            for M in Q:
                if not any(M):order.append(0);continue
                a,b,c,d=M;u=norm(a,c) if a or c else norm(b,d)
                v=norm(a,b) if a or b else norm(c,d)
                ui,vi=lines.index(u),lines.index(v)
                scalar=M[(0 if u[0] else 2)+(0 if v[0] else 1)]
                index=1+(ui*(p+1)+vi)*(p-1)+scalar-1
                order.append(index);groups[(ui,vi)].append(index)
            D=sum((line_minimum([values[i] for i in group]) for group in groups.values()),F(0))
            cache[key]=(Q,order,D)
        Q,order,D=cache[key]
        assert D==F(row['quantization_sum'])
        mask=int(row['mask_hex'],16);den=math.lcm(*(a.denominator for a in values))
        E=[int((F((mask>>index)&1)-values[index])*den) for index in order]
        numerator=0
        for i,x in enumerate(Q):
            for j,y in enumerate(Q):
                delta=[(a-b)%p for a,b in zip(x,y)]
                B=p*p*(i==j)+p*int((delta[0]*delta[3]-delta[1]*delta[2])%p==0)-1
                numerator+=E[i]*B*E[j]
        inside=F(numerator,p**3*den*den);energy=F(sum(x*x for x in E),den*den)
        leakage=energy-inside
        assert energy==F(row['energy']) and inside==F(row['inside'])
        assert leakage==F(row['leakage'])>=(1-F(1,p))*D==F(row['proved_lower'])
        cases.append(dict(prime=p,profile=row['profile'],selector=row['selector'],verified=True))
    return dict(line_profiles=len(source['line_tests']),cone_cases=cases,verified=True)


def independent_center(k):
    parts=[]
    for base in [2,3]:
        value=k;digits=[]
        while value:value,r=divmod(value,base);digits.append(r)
        num=0
        for r in digits:num=num*base+r
        parts.append(2*F(num,base**len(digits))-1)
    q=math.lcm(*(a.denominator for a in parts))
    return (int(parts[0]*q),int(parts[1]*q),q)


def reverse_lenses(L):
    X=2**L;k0=(L+3)//4;k1=3*L//4-1
    centers={k:independent_center(k) for k in range(k0,k1+1)}
    pairs=[];wb=X//(2**k0);ub=2**(k1+1)
    for r in range(wb+1):
        for s in range(-wb,wb+1):
            if r==0 and s<=0:continue
            w=r*r+s*s
            if not w or w>wb*wb:continue
            bound=min(ub,math.isqrt(X*X//w))
            for a0 in range(bound+1):
                for b0 in range(-bound,bound+1):
                    if a0==0 and b0<=0:continue
                    d=a0*a0+b0*b0
                    if not d or math.gcd(a0,abs(b0))!=1:continue
                    k=(d.bit_length()-1)//2
                    if k not in centers:continue
                    a,b,q=centers[k]
                    Z=X*X*(q*q-a*a-b*b)-d*w*q*q
                    if Z<0:continue
                    N=4*X*X*q*q*d*(a*r+b*s)**2
                    floor=math.isqrt(N)
                    if Z>=floor+int(floor*floor<N):pairs.append((a0,b0,r,s))
    return pairs,centers


def verify_lenses(root):
    source=json.loads((root/'lens.json').read_text());cases=[]
    for row in source['cases']:
        L=row['L'];X=row['X'];pairs,centers=reverse_lenses(L)
        assert centers=={int(k):tuple(v) for k,v in row['centers'].items()}
        assert len(pairs)==row['n']
        h=row['moduli'];P=math.prod(h);C=row['C']
        assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
        assert all(c*z==P for c,z in zip(C,h))
        matrices=[(a*r,a*s,b*r,b*s) for a,b,r,s in pairs]
        assert len(set(matrices))==len(matrices)
        A=sorted(abs(sum(c*z for c,z in zip(C,M))) for M in matrices)
        assert A[0]>0 and len(set(A))==len(A)
        assert hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest()==row['encoded_set_sha256']
        residues=row['point']['residues'];counts=Counter()
        for M in matrices:
            r=sum(z*m*(P//modulus) for z,m,modulus in zip(residues,M,h))%P
            counts[min(r,P-r)]+=1
        value=sum((n*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P)) for r,n in counts.items()),flint.arb(0))
        upper=F(row['point']['f_over_n_upper_rational'])
        assert value<flint.arb(upper.numerator)*len(A)/upper.denominator
        cert=row['fejer'];u=tuple(cert['u']);d=sum(x*x for x in u);m=cert['m']
        a,b,q=cert['center'];assert (a,b,q)==centers[cert['shell']]
        assert (min(h)-X)**2>2*m*m*d
        factor=2*flint.arb.pi()*flint.arb(d).sqrt()*q/(X*flint.arb(q*q-a*a-b*b).sqrt()*flint.arb(a*a+b*b).sqrt())
        alpha=[-b*factor,a*factor]
        fiber=[(r,s) for a0,b0,r,s in pairs if (a0,b0)==u]
        assert len(fiber)==cert['fiber_pairs']
        H=2*sum(((m+1-abs(r))*(m+1-abs(s))*(alpha[0]*r+alpha[1]*s).cos()
                 for r,s in fiber),flint.arb(0))/(m+1)**2
        lower=F(cert['M_lower_rational'])
        assert H+2*flint.arb(lower.numerator)/lower.denominator<0
        result=dict(L=L,X=X,n=len(A),hash_verified=True,point_verified=True,
                    fejer_verified=True,aliases=0,mean=1)
        cases.append(result);print(json.dumps(result),flush=True)
    return cases


def lens_transform_checks():
    records=[]
    for t0 in [F(0),F(1,4),F(1,2),F(2,3),F(3,4),F(9,10),F(99,100)]:
        t=flint.arb(t0.numerator)/t0.denominator;b=(1-t*t).sqrt()
        integrals=[t.acos()]
        for k in range(1,23):
            integrals.append(((2*k-1)*integrals[-1]-b**(2*k-1)*t)/(2*k))
        moments=[(integrals[k]-integrals[k+1])/b**(2*k+1)-t/(2*k+1) for k in range(21)]
        s=2*flint.arb.pi()
        upper=sum(((-1)**k*s**(2*k)*moments[k]/math.factorial(2*k) for k in range(21)),flint.arb(0))/moments[0]
        assert upper<-flint.arb(1)/64
        records.append(dict(t=str(t0),normalized_upper_ball=str(upper),verified=True))
    assert F(9,16)*F(7,22)**3>F(1,64)
    assert F(3,8)*F(7,22)**2>F(1,64)
    assert (F(7,1536)-F(1,512))*100000>=201
    for L in range(64,257):
        k0=(L+3)//4;k=k0+(10-k0)%12;X=2**L;d=2**(2*k)+1
        a,b,q=independent_center(k)
        assert k<3*L//4 and 9*(a*a+b*b)<=4*q*q
        assert X*2**52>=d*d and X*X>=10**10*d
    return records


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=192
    root=Path('.research/experiments/radial_boolean_2026-10-20')
    out=dict(qualification='Independent finite exact/ball checks, not an external-agent or Lean audit.',
             python_version=platform.python_version(),flint_version=flint.__version__,arb_precision=flint.ctx.prec,
             quantization=verify_quantization(root),lens_transform=lens_transform_checks(),
             lenses=verify_lenses(root),verified=True)
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
