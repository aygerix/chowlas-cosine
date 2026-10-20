"""Critical CRT encoding: it escapes long-row isolation but has another phase.

Run on Dirichlet. Point certificates are rigorous lower bounds for M.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint
from cstar_integer_cone import cone_pairs


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=96
    root=Path('.research/experiments/cone_comparable_2026-10-20')
    root.mkdir(parents=True,exist_ok=True)
    out=dict(qualification='Explicit critical family and certified point lower witnesses, not a Chowla counterexample.',cases=[])
    for X in [48,64,96,128]:
        assert X%4==0
        base=3*X//2;h=[base+i for i in [1,3,5,7]]
        assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
        assert min(h)**2>2*X*X
        P=math.prod(h);C=[P//a for a in h]
        assert math.gcd(*C)==1
        determinant=C[0]*C[3]-C[1]*C[2]
        assert determinant==8*P>max(C)
        lines=[C[:2],C[2:],[C[0],C[2]],[C[1],C[3]]]
        primitive_squared=[sum(z*z for z in line)//math.gcd(*line)**2 for line in lines]
        assert all(z<=(47*X)**2 for z in primitive_squared)
        A=sorted(abs(C[0]*u1*w1+C[1]*u1*w2+C[2]*u2*w1+C[3]*u2*w2)
                 for u1,u2,w1,w2 in cone_pairs(X))
        assert A[0]>0 and len(set(A))==len(A)
        residues=[0,1,-1,0]
        j=sum(r*(P//m)*pow(P//m,-1,m) for r,m in zip(residues,h))%P
        assert all(j%m==r%m for r,m in zip(residues,h))
        lam1=2*flint.arb.pi()*X/h[1];lam2=2*flint.arb.pi()*X/h[2]
        assert lam1>flint.arb(77)/20 and lam1<7
        assert lam2>flint.arb(77)/20 and lam2<7
        counts=Counter()
        for a in A:
            r=j*a%P;counts[min(r,P-r)]+=1
        value=sum((count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P))
                   for r,count in counts.items()),flint.arb(0))
        n=len(A);scale=10**6
        upper=F(math.ceil(float(value.mid())/n*scale)+1,scale)
        assert value<flint.arb(upper.numerator)*n/upper.denominator
        assert upper<0
        lower=-n*upper
        row=dict(X=X,n=n,moduli=h,C=C,determinant=determinant,
                 primitive_row_column_squared=primitive_squared,
                 root_of_unity=dict(j=j,q=P,residues=residues),
                 lambda1_float=float(lam1.mid()),lambda2_float=float(lam2.mid()),
                 f_over_n_upper_rational=str(upper),M_lower_rational=str(lower),
                 R_lower_float=float(lower)/math.sqrt(n),
                 encoded_set_sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                 verified=True)
        out['cases'].append(row)
        (root/'critical.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:row[k] for k in ['X','n','moduli','f_over_n_upper_rational','R_lower_float']}),flush=True)


if __name__=='__main__':main()
