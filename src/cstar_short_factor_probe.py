"""Boolean, incomplete-fiber witnesses for the short-factor residue test.

Run on Dirichlet. A point proves a lower bound, never an all-circle upper.
"""
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import socket
import flint
import numpy as np


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=192;out=[]
    for X,p in [(16,5),(64,11)]:
        B=math.isqrt(X);assert B*B==X and B<p<=2*B
        matrices=[]
        for a in range(X+1):
            for b in range(-X,X+1):
                d=a*a+b*b
                if not (a>0 or b>0) or math.gcd(a,abs(b))!=1 or d<X or d>X*X:continue
                r=math.isqrt(X*X//d)
                for c in range(r+1):
                    for e in range(-r,r+1):
                        if not (c>0 or e>0) or not 0<c*c+e*e<=X*X//d:continue
                        # Deliberately incomplete, direction-dependent fibers.
                        if (3*a+5*b+7*c+11*e+a*e)%5 in [0,1]:continue
                        matrices.append((a*c,a*e,b*c,b*e))
        h=[6*X**3+i for i in [1,3,5,7]];P=math.prod(h);C=[P//z for z in h]
        A=sorted(abs(sum(c*m for c,m in zip(C,M))) for M in matrices)
        assert 0 not in A and len(set(A))==len(A) and len(set(matrices))==len(A)
        assert all(any(x%p for x in M) and M[0]*M[3]==M[1]*M[2] for M in matrices)
        # Choose a residue phase using a histogram; certify the actual
        # scalar point below without relying on this floating search.
        counts={}
        for M in matrices:
            key=tuple(x%p for x in M);counts[key]=counts.get(key,0)+1
        residues=np.array(list(counts));weights=np.array(list(counts.values()))
        G=[H for H in itertools.product(range(p),repeat=4) if (H[0]*H[3]-H[1]*H[2])%p]
        cosine=np.cos(2*math.pi*np.arange(p)/p);best=None
        for start in range(0,len(G),256):
            chunk=np.array(G[start:start+256]);values=cosine[(chunk@residues.T)%p]@weights
            index=int(np.argmin(values));candidate=(float(values[index]),tuple(chunk[index]))
            if best is None or candidate[0]<best[0]:best=candidate
        H=[int(x) for x in best[1]]
        k=[(2*hi*hi_phase+p)//(2*p) for hi,hi_phase in zip(h,H)]
        j=sum(ki*ci*pow(ci,-1,hi) for ki,ci,hi in zip(k,C,h))%P
        assert [j%hi for hi in h]==k
        value=flint.arb(0);alternate=flint.arb(0)
        for M,a in zip(matrices,[abs(sum(c*m for c,m in zip(C,M))) for M in matrices]):
            z=a*j%P;value+=(2*flint.arb.pi()*z/P).cos()
            phase=sum(F(mi*ki,hi) for mi,ki,hi in zip(M,k,h))%1
            alternate+=(2*flint.arb.pi()*phase.numerator/phase.denominator).cos()
            assert phase==F(z,P) or (-phase)%1==F(z,P)
        assert (value-alternate).contains(0)
        lower=F(max(0,math.floor(-float(value.mid())*10**6)-2),10**6)
        assert value+flint.arb(lower.numerator)/lower.denominator<0
        theoretical=F(len(A),p*p-1)-F(44*X*len(A),7*min(h))
        assert theoretical>=F(len(A),8*B*B)>0
        row=dict(X=X,B=B,p=p,n=len(A),max_A=max(A),
                 generator='canonical primitive u, ||u||>=sqrt(X); ||uw^T||<=X; canonical w; '
                           'exclude (3u1+5u2+7w1+11w2+u1w2) mod5 in {0,1}',
                 sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                 h=h,phase_matrix=H,crt_residues=k,j=j,P=P,
                 residue_average_M_lower=str(theoretical),
                 scalar_point_f_ball=str(value),point_M_lower=str(lower),
                 point_ratio_lower_float=float(lower)/math.sqrt(len(A)),
                 two_scalar_evaluations_agree=True,
                 qualification='Boolean set; certified negative point and positive-average lower bound only.')
        out.append(row);print(json.dumps(row),flush=True)
    Path('.research/experiments/wide_mean_2026-10-20/boolean_residue.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
