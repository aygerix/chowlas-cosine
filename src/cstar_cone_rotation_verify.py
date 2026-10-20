"""Independent reverse enumeration and direct four-residue phase check."""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=176
    root=Path('.research/experiments/cone_confinement_2026-10-20')
    data=json.loads((root/'rotation.json').read_text())
    sign=data['sign'];a=[F(x) for x in sign['coefficients_low_to_high']];n=len(a)-1
    assert a==[F((-1)**k,math.factorial(k)**2)+(F(1,10) if k==0 else 0) for k in range(n+1)]
    partitions=sign['bernstein_partitions']
    assert F(partitions[0]['interval'][0])==F(9,4)
    assert F(partitions[-1]['interval'][1])==F(25,4)
    previous=F(9,4)
    for row in partitions:
        lo,hi=map(F,row['interval']);assert lo==previous;previous=hi
        power=[sum((a[k]*math.comb(k,j)*lo**(k-j)*(hi-lo)**j for k in range(j,n+1)),F(0)) for j in range(n+1)]
        b=[sum((power[j]*F(math.comb(i,j),math.comb(n,j)) for j in range(i+1)),F(0)) for i in range(n+1)]
        assert max(b)==F(row['maximum_control'])<0
    out=dict(qualification='Exact independent sign-certificate and factor-enumeration checks, '
             'plus 176-bit direct phase rechecks. No external-agent or Lean audit.',
             sign_verified=True,cases=[])
    for X in sorted({row['X'] for row in data['cases']}):
        raw=[]
        for c in range(X+1):
            for d in range(-X,X+1):
                if c==0 and d<=0:continue
                w=c*c+d*d
                if not w or w>X*X:continue
                limit=math.isqrt(X*X//w)
                for a0 in range(limit+1):
                    for b0 in range(-limit,limit+1):
                        if a0==0 and b0<=0:continue
                        u=a0*a0+b0*b0
                        if not u or u*w>X*X or 25*u*w<9*X*X:continue
                        if math.gcd(a0,abs(b0))==1:raw.append((a0,b0,c,d))
        raw.sort()
        digest=hashlib.sha256((' '.join(','.join(map(str,z)) for z in raw)).encode()).hexdigest()
        for row in [r for r in data['cases'] if r['X']==X]:
            assert digest==row['raw_factor_sha256']
            h=row['moduli'];C=row['C'];P=math.prod(h);k=row['phase_residues']
            assert min(h)>=1000*X and math.gcd(*C)==1
            assert all(c*m==P for c,m in zip(C,h))
            assert all(math.gcd(x,y)==1 for i,x in enumerate(h) for y in h[i+1:])
            mask=int(row['selection_mask_hex'],16);A=[];counts=Counter()
            for i,(a0,b0,c,d) in enumerate(raw):
                chosen=bool((mask>>i)&1);name=row['pattern']
                M=(a0*c,a0*d,b0*c,b0*d)
                if name=='full_annulus':assert chosen
                elif name=='two_ruling_threshold':
                    assert chosen==(a0*a0*(c*c+d*d)+c*c*(a0*a0+b0*b0)>=(a0*a0+b0*b0)*(c*c+d*d))
                elif name=='coupled_modular':assert chosen==((M[0]+M[3])%7 in [0,1,6])
                if not chosen:continue
                A.append(abs(sum(z*m for z,m in zip(C,M))))
                r=sum(z*m*(P//modulus) for z,m,modulus in zip(k,M,h))%P
                counts[min(r,P-r)]+=1
            A.sort();assert len(A)==row['n'] and A[0]>0 and len(A)==len(set(A))
            assert hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest()==row['encoded_set_sha256']
            value=sum((count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P))
                       for r,count in counts.items()),flint.arb(0))
            upper=F(row['f_over_n_upper_rational'])
            assert value<flint.arb(upper.numerator)*len(A)/upper.denominator and upper<-F(1,12)
            assert F(row['M_lower_rational'])==-len(A)*upper
            result=dict(X=X,pattern=name,n=len(A),hash_verified=True,point_bound_verified=True)
            out['cases'].append(result);print(json.dumps(result),flush=True)
    (root/'rotation_verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
