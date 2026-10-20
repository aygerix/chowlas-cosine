"""Uniform mixed-place-value resonance test for the rank-one integer cone.

Execute on Dirichlet. These are exact/ball lower witnesses for M, not
sampled global upper bounds. The infinite-family conclusion is in the note.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import time
import flint
import sympy as sp
from cstar_integer_cone import cone_pairs


def disk_sign():
    u=sp.symbols('u');order=20
    P=sum((-1)**k*u**k/sp.Integer(math.factorial(k)*math.factorial(k+1))
          for k in range(order+1))
    certificate=sp.Poly(P+sp.Rational(1,2000),u)
    lo,hi=sp.Rational(5929,1600),sp.Rational(49,4)
    assert hi<(order+1)*(order+2)
    roots=certificate.count_roots(lo,hi)
    assert roots==0 and certificate.eval(lo)<0
    return dict(t_interval=['77/20','7'],u_interval=[str(lo),str(hi)],
                polynomial_order=order,sturm_root_count=int(roots),
                polynomial_coefficients_low_to_high=[str(P.expand().coeff(u,k)) for k in range(order+1)],
                disk_transform_upper='-1/2000',verified=True)


def evaluate(X,S,R,pairs):
    assert S>2*X and R>2*X*(S+1)
    A=sorted(abs((u1+R*u2)*(w1+S*w2)) for u1,u2,w1,w2 in pairs)
    assert A and A[0]>0 and len(set(A))==len(A)
    n=len(A);N=2*n;k=S//X;q=R*S
    j=S*math.ceil((77*R/(40*math.pi*X)+k)/S)-k
    assert (j+k)%S==0
    lam1=2*flint.arb.pi()*X*j/R
    lam2=2*flint.arb.pi()*X*k/S
    assert lam1>flint.arb(77)/20 and lam1<7
    assert lam2>flint.arb(77)/20 and lam2<7
    counts=Counter()
    for a in A:
        residue=j*a%q
        counts[min(residue,q-residue)]+=1
    value=flint.arb(0)
    for residue,count in counts.items():
        value+=2*count*flint.arb.cos_pi_fmpq(flint.fmpq(2*residue,q))
    scale=10**6
    upper=F(math.ceil(float(value.mid())/N*scale)+1,scale)
    assert value<flint.arb(upper.numerator)*N/upper.denominator
    lower=max(F(0),-n*upper)
    return dict(X=X,S=S,R=R,n=n,N=N,max_A=A[-1],
                encoded_set_sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                root_of_unity=dict(numerator=j,denominator=q),
                lambda1_float=float(lam1.mid()),lambda2_float=float(lam2.mid()),
                D_over_N_upper_rational=str(upper),M_lower_rational=str(lower),
                R_lower_float=float(lower)/math.sqrt(n),
                arb_precision=flint.ctx.prec,flint_version=flint.__version__,
                qualification='One rigorous root-of-unity lower witness for M',verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=96;start=time.time()
    path=Path('.research/experiments/integer_cone_2026-10-20/mixed.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    out=dict(disk_sign=disk_sign(),cases=[])
    for X in [8,16,32,64]:
        pairs=cone_pairs(X)
        for multiplier in [2,4,16]:
            S=multiplier*X+1
            for R in [2*X*(S+1)+1,5*X*(S+1)+X+3]:
                row=evaluate(X,S,R,pairs)
                out['cases'].append(row)
                path.write_text(json.dumps(out,indent=2)+'\n')
                print(json.dumps({k:row[k] for k in ['X','S','R','n',
                      'D_over_N_upper_rational','R_lower_float']}),flush=True)
    out['seconds']=time.time()-start
    path.write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
