"""Exact off-left triple counts from primitive relation kernels.

Mechanism probe for the crude U^4 bound, not a proof of a better exponent.
Run on Dirichlet.
"""
from collections import Counter
import itertools
import json
import math
from pathlib import Path
import socket
import flint


def dirs(U):
    return [(a,b) for a in range(U+1) for b in range(-U,U+1)
            if (a>0 or b>0) and math.gcd(a,abs(b))==1 and a*a+b*b<=U*U]


def relation_counts(U):
    hist=Counter()
    for u,v,w in itertools.combinations(dirs(U),3):
        determinants=[v[0]*w[1]-v[1]*w[0],w[0]*u[1]-w[1]*u[0],u[0]*v[1]-u[1]*v[0]]
        g=math.gcd(*determinants);assert g>0 and all(determinants)
        a=[x//g for x in determinants]
        assert all(sum(c*t[j] for c,t in zip(a,[u,v,w]))==0 for j in [0,1])
        ell2=max(c*c*(t[0]*t[0]+t[1]*t[1]) for c,t in zip(a,[u,v,w]))
        hist[ell2]+=6
    return hist


def disk(q):
    r=math.isqrt(q)
    return sum(2*math.isqrt(q-y*y)+1 for y in range(-r,r+1))


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=192;cache={};out=[]
    for U in [2,3,4,6,8,10,12,16]:
        hist=relation_counts(U);D=sum((flint.arb(count)/ell for ell,count in hist.items()),flint.arb(0))
        finite=[]
        for X in [64,256,1024]:
            total=0
            for ell,count in hist.items():
                q=X*X//ell
                if q not in cache:cache[q]=disk(q)
                total+=count*(cache[q]-1)
            finite.append(dict(X=X,ordered_nonleft_triples=total,over_X2_U2_float=total/(X*X*U*U)))
        row=dict(U=U,directions=len(dirs(U)),primitive_relation_denominators=len(hist),
                 D_ball=str(D),D_over_U2_float=float(D.mid())/(U*U),
                 D_over_U4_float=float(D.mid())/(U**4),finite=finite)
        out.append(row);print(json.dumps(row),flush=True)
    # Independent direct enumeration at a genuinely small finite control.
    X=4;U=2;M={};target={}
    for u in dirs(U):
        r=math.isqrt(X*X//(u[0]*u[0]+u[1]*u[1]))
        for x in range(-r,r+1):
            for y in range(-r,r+1):
                if not 0<(x*x+y*y)*(u[0]*u[0]+u[1]*u[1])<=X*X:continue
                z=(u[0]*x,u[0]*y,u[1]*x,u[1]*y);M[z]=u
    direct=0
    for a,u in M.items():
        for b,v in M.items():
            if u==v:continue
            c=tuple(-a[j]-b[j] for j in range(4))
            if c in M:direct+=1
    formula=sum(count*(disk(X*X//ell)-1) for ell,count in relation_counts(U).items())
    assert direct==formula
    root=Path('.research/experiments/sidon_cutoff_2026-10-20')
    (root/'triple_counts.json').write_text(json.dumps(dict(qualification='Exact counts and interval limiting weights; '
       'not a uniform asymptotic exponent theorem.',cases=out,
       direct_control=dict(X=X,U=U,ordered=direct,formula=formula,passed=True)),indent=2)+'\n')


if __name__=='__main__':main()
