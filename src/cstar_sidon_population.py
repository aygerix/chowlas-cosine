"""Exhaustive conditional mixed-reference moments for small parabola orbits.

Distinct affine images, not random samples. Integer triple counts and
integer matrix products; all computations run on Dirichlet.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import socket
import sys
import numpy as np


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    out=[]
    primes=list(map(int,sys.argv[1:])) or [3,5,7]
    for p in primes:
        sets=set()
        if p<=7:
            for a,b,c,d in itertools.product(range(p),repeat=4):
                if (a*d-b*c)%p==0:continue
                curve=[((a*t+b*t*t)%p,(c*t+d*t*t)%p) for t in range(p)]
                for sx,sy in itertools.product(range(p),repeat=2):
                    sets.add(tuple(sorted(((x+sx)%p,(y+sy)%p) for x,y in curve)))
        else:
            # Same full affine orbit, parameterized by its quadratic
            # direction and its graph in transverse coordinates.
            for direction in range(p+1):
                for a in range(1,p):
                    for b,c in itertools.product(range(p),repeat=2):
                        points=[]
                        for t in range(p):
                            z=(a*t*t+b*t+c)%p
                            points.append(((t-direction*z)%p,z) if direction<p else (z,t))
                        sets.add(tuple(sorted(points)))
        assert len(sets)==p*p*(p*p-1)
        sets=sorted(sets);N=len(sets)
        W=[(x,y) for x in range(-p+1,p) for y in range(-p+1,p) if (x,y)!=(0,0)]
        index={w:i for i,w in enumerate(W)};eta=np.zeros((N,len(W)),dtype=np.int64);third=[]
        for i,B in enumerate(sets):
            S={(x-x1,y-y1) for x,y in B for x1,y1 in B if (x,y)!=(x1,y1)}
            assert len(S)==p*(p-1)
            for w in S:eta[i,index[w]]=1
            third.append(sum((a+c,b+d) in S for a,b in S for c,d in S))
        hist=eta.sum(axis=0);second=eta.T@eta
        for i,(x,y) in enumerate(W):
            assert F(int(hist[i]),N)==F(p,p+1)*F(p-abs(x),p)*F(p-abs(y),p)
        Toeplitz=np.array([[int(hist[index[x+u,y+v]]) if (x+u,y+v) in index else 0
                           for u,v in W] for x,y in W],dtype=np.int64)
        covariance_sum=np.array([sum(int(second[i,index[x-u,y-v]]) for i,(u,v) in enumerate(W)
                              if (x-u,y-v) in index) for x,y in W],dtype=np.int64)
        G=((eta@Toeplitz)*eta).sum(axis=1);R=eta@covariance_sum
        Hnum=N*np.array(third,dtype=np.int64)-2*G+R
        anum=N*p*(p-1)-eta@hist
        assert min(anum)>0
        Hmax=int(Hnum.max());amin=int(anum.min())
        roots=[]
        for a,h in zip(anum,Hnum):
            a=float(a)/N;h=float(h)/N;Q=2*a
            roots.append(2*a*a/(h+math.sqrt(h*h+4*Q*a*a)) if h>=0 else (-h+math.sqrt(h*h+4*Q*a*a))/(2*Q))
        k=F(max(0,math.floor(min(roots)*10**8)-2),10**8)
        for a,h in zip(anum,Hnum):
            # Clear N^2, so this is exact integer/rational algebra.
            assert 2*int(a)*N*k*k+int(h)*N*k-int(a)*int(a)<0
        worst=int(np.argmax(Hnum));n=p*(p-1)//2
        row=dict(p=p,distinct_affine_parabolas=N,normalization='uniform over distinct point sets; '
                 'equivalent to uniform GL2 and cyclic translations by constant stabilizer multiplicity',
                 enumeration_sha256=hashlib.sha256(repr(sets).encode()).hexdigest(),
                 conditional_H_max=str(F(Hmax,N)),conditional_H_max_over_p3=str(F(Hmax,N*p**3)),
                 conditional_a_min=str(F(amin,N)),conditional_a_min_over_n=str(F(amin,N*n)),
                 reference_averaged_global_M_lower=str(k/2),
                 uniform_mixed_ratio_lower=float(k)/(2*math.sqrt(n)),
                 worst_H_points=sets[worst],worst_H_a=str(F(int(anum[worst]),N)),
                 average_H=str(F(int(Hnum.sum()),N*N)),all_exact_certificate_inequalities_pass=True)
        out.append(row);print(json.dumps(row),flush=True)
    filename='population.json' if primes==[3,5,7] else 'population_extra.json'
    Path('.research/experiments/sidon_fibers_2026-10-20',filename).write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
