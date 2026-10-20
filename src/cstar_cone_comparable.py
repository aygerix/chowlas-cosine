"""Comparable almost-rank-one encodings: collision-filtered mechanism probe.

Run on Dirichlet. All reported M bounds are rigorous lower witnesses at
exact roots of unity; sampled minima never certify a global upper bound.
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
import numpy as np
import scipy
from scipy import fft
from cstar_integer_cone import cone_pairs


def build(X,C):
    matrices=np.array([(u1*w1,u1*w2,u2*w1,u2*w2)
                      for u1,u2,w1,w2 in cone_pairs(X)],dtype=np.int64)
    A=np.abs(matrices@np.array(C,dtype=np.int64))
    if not len(A) or np.any(A==0) or len(np.unique(A))!=len(A):return None
    return np.sort(A).tolist()


def point_certificate(A,j,q):
    counts=Counter()
    for a in A:
        r=j*a%q;counts[min(r,q-r)]+=1
    value=sum((count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,q))
               for r,count in counts.items()),flint.arb(0))
    n=len(A);scale=10**7
    upper=F(math.ceil(float(value.mid())/n*scale)+1,scale)
    assert value<flint.arb(upper.numerator)*n/upper.denominator
    lower=max(F(0),-n*upper)
    return dict(j=j,q=q,f_over_n_upper_rational=str(upper),
                M_lower_rational=str(lower),R_lower_float=float(lower)/math.sqrt(n),
                arb_precision=flint.ctx.prec,verified=True)


def probe(A,C):
    a,b,c,d=C
    denominators=sorted({z for z in [a,b,c,d,a+d,b+c,abs(a-d),abs(b-c),abs(a*d-b*c)]
                         if 2<=z<=2**20})
    best=None
    for q in denominators:
        histogram=np.bincount(np.asarray(A)%q,minlength=q)
        values=fft.rfft(histogram).real
        j=int(np.argmin(values));estimate=float(values[j])
        if best is None or estimate<best[0]:best=(estimate,j,q)
    assert best is not None
    return point_certificate(A,best[1],best[2]),denominators


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=96;seed=20261021;rng=np.random.default_rng(seed);start=time.time()
    root=Path('.research/experiments/cone_comparable_2026-10-20')
    root.mkdir(parents=True,exist_ok=True)
    path=root/'results.json'
    out=dict(qualification='Bounded collision-filtered search; lower witnesses only, no global upper or family exclusion.',
             seed=seed,numpy=np.__version__,scipy=scipy.__version__,flint=flint.__version__,
             groups=[],global_probes=[])
    for X in [4,8,12,16]:
        candidates=[]
        for scale in [4,16]:
            H=scale*X**3;rows=[];rejected=0;attempts=0
            while len(rows)<6 and attempts<128:
                attempts+=1
                a,b,c=map(int,rng.integers(H,2*H+1,size=3))
                d=(b*c+a//2)//a
                raw=[a,b,c,d];g=math.gcd(*raw);C=[z//g for z in raw]
                A=build(X,C)
                if A is None:
                    rejected+=1;continue
                certificate,denominators=probe(A,C)
                row=dict(X=X,H=H,C=C,raw_C=raw,gcd_removed=g,
                         determinant=C[0]*C[3]-C[1]*C[2],n=len(A),max_A=A[-1],
                         encoded_set_sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                         denominators=denominators,point=certificate)
                rows.append(row);candidates.append((certificate['R_lower_float'],A,row))
            group=dict(X=X,H=H,attempts=attempts,rejected_collisions=rejected,cases=rows)
            out['groups'].append(group)
            path.write_text(json.dumps(out,indent=2)+'\n')
            print(json.dumps(dict(X=X,H=H,valid=len(rows),rejected=rejected,
                  best_probe_R_lower=min((r['point']['R_lower_float'] for r in rows),default=None))),flush=True)
        if candidates:
            _,A,row=min(candidates,key=lambda z:z[0])
            grid=1<<math.ceil(math.log2(4*A[-1]+1))
            coefficients=np.zeros(grid);coefficients[A]=1
            values=fft.rfft(coefficients).real;j=int(np.argmin(values))
            certificate=point_certificate(A,j,grid)
            result=dict(X=X,C=row['C'],n=len(A),max_A=A[-1],A=A,
                        initial_point=row['point'],fine_grid_point=certificate,
                        grid=grid,qualification='Grid selected a point; only its certified negative value is used.')
            out['global_probes'].append(result)
            path.write_text(json.dumps(out,indent=2)+'\n')
            print(json.dumps(dict(X=X,n=len(A),grid=grid,fine_R_lower=certificate['R_lower_float'])),flush=True)
            del coefficients,values
    out['seconds']=time.time()-start
    path.write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
