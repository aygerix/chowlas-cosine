"""Exact conditional-cost lower bounds for a mismatched reference profile.

Actual points are a half-interval parabola. Compare isotropic k-subset
references with references keeping the actual horizontal interval.
All computations on Dirichlet. No global cosine upper bound is claimed.
"""
from collections import Counter
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import socket
import sys
import flint


def spectrum(B):
    S={(x-u,y-v) for x,y in B for u,v in B if (x,y)!=(u,v)}
    assert len(S)==len(B)*(len(B)-1)
    return S


def square(S):
    result=Counter()
    for x,y in S:
        for u,v in S:result[x+u,y+v]+=1
    return result


def cost_lower(p,k,S,kind,I=None):
    # Integer numerators for the exact ensemble-mean coefficients.
    r=p-1
    if kind=='isotropic':
        den=(p*p-1)*p*p
        mean={(x,y):k*(k-1)*(p-abs(x))*(p-abs(y)) for x in range(-r,r+1)
              for y in range(-r,r+1) if (x,y)!=(0,0)}
    else:
        den=p*p
        I=list(range(k)) if I is None else I
        counts=Counter(x-y for x in I for y in I if x!=y)
        mean={(x,y):count*(p-abs(y)) for x,count in counts.items() for y in range(-r,r+1)}
    assert F(sum(mean.values()),den)==k*(k-1)
    q={w:(den if w in S else 0)-mean.get(w,0) for w in set(mean)|S}
    base=4*r+1;coeff=[0]*((2*r+1)*base)
    for (x,y),c in q.items():coeff[x+r+(y+r)*base]=c
    product=flint.fmpz_poly(coeff)**2
    Hdet=F(sum(int(product[x+2*r+(y+2*r)*base]) for x,y in S),den*den)
    variance=F(k*(k-1))-F(sum(c*c for c in mean.values()),den*den)
    lower=Hdet-k*variance
    return dict(mean_denominator=den,H_fixed_mean=str(Hdet),reference_variance_integral=str(variance),
                conditional_H_lower=str(lower),conditional_H_lower_over_p3_float=float(lower)/p**3,
                conditional_H_lower_over_p4_float=float(lower)/p**4),mean


def exact_small(p,I=None):
    I=list(range((p-1)//2)) if I is None else I
    k=len(I);actual=[(t,t*t%p) for t in I];S=spectrum(actual);conv=square(S)
    law=Counter();parabolas=set()
    for d in range(p+1):
        for a in range(1,p):
            for b,c in itertools.product(range(p),repeat=2):
                B=[]
                for t in range(p):
                    z=(a*t*t+b*t+c)%p;B.append(((t-d*z)%p,z) if d<p else (z,t))
                parabolas.add(tuple(sorted(B)))
    for B in parabolas:law.update(itertools.combinations(B,k))
    laws={'isotropic':law,'matched':Counter(tuple((t,(a*t*t+b*t+c)%p) for t in I)
           for a in range(1,p) for b,c in itertools.product(range(p),repeat=2))}
    out={}
    for kind,law in laws.items():
        hist=Counter();second=Counter();N=sum(law.values())
        for B,weight in law.items():
            T=spectrum(B)
            for w in T:hist[w]+=weight
            for w,c in square(T).items():second[w]+=weight*c
        row,mean=cost_lower(p,k,S,kind,I);den=row['mean_denominator']
        assert all(F(hist[w],N)==F(mean.get(w,0),den) for w in set(hist)|set(mean))
        H=F(sum(conv[w] for w in S))-2*F(sum(c*hist.get((-w[0],-w[1]),0) for w,c in conv.items()),N)
        H+=F(sum(second.get(w,0) for w in S),N)
        assert H>=F(row['conditional_H_lower'])
        out[kind]=dict(ensemble_size=N,distinct_reference_sets=len(law),exact_H=str(H),
                       lower=str(row['conditional_H_lower']),mean_identity_checked=True)
    return dict(p=p,k=k,cases=out)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    arc='--arc' in sys.argv
    small_I=[t for t in range(7) if 2*(t*t%7)<7] if arc else None
    out=dict(qualification='Conditional cubic COST lower bounds; no statement of a Chowla counterexample.',
             actual_kind='quadratic_arc' if arc else 'half_interval',
             small_reference_check=exact_small(7,small_I),cases=[])
    root=Path('.research/experiments/sidon_cutoff_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    for p in ([31,61,127,251] if arc else [31,61,127,251,509]):
        I=[t for t in range(p) if 2*(t*t%p)<p] if arc else list(range((p-1)//2))
        k=len(I);P=[(t,t*t%p) for t in I];S=spectrum(P)
        row=dict(p=p,k=k,actual_points=P,t_indices=I,means={})
        for kind in ['isotropic','matched']:
            row['means'][kind]=cost_lower(p,k,S,kind,I)[0]
        filename='profile_arc.json' if arc else 'profile_probe.json'
        out['cases'].append(row);(root/filename).write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(dict(p=p,k=k,means=row['means'])),flush=True)


if __name__=='__main__':main()
