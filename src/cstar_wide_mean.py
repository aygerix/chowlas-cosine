"""Widened staggered-radius fractional means and transposed heat tests.

Exact integer lens counts define the profile. Floating scores choose a
radius assignment; Arb and an explicit Gaussian-alias tail certify it.
Run every research computation on Dirichlet.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint
import numpy as np


def disk_data(q):
    r=math.isqrt(q);columns=[2*math.isqrt(q-j*j)+1 for j in range(r+1)]
    total=columns[0]+2*sum(columns[1:]);parity=[0]*4
    for j in range(r+1):
        bound=(columns[j]-1)//2;mult=1 if j==0 else 2
        parity[2*(j%2)]+=mult*(2*(bound//2)+1)
        parity[2*(j%2)+1]+=mult*(2*((bound+1)//2))
    assert sum(parity)==total
    numerators=[0]*(r+1);tail=0
    for k in range(r,0,-1):numerators[k]=columns[k]+2*tail;tail+=columns[k]
    mean_n=F(sum(z*z for z in parity)-total,2*total)
    return dict(q=q,r=r,total=total,axis=numerators,mean_n=mean_n)


def directions(X):
    V=math.isqrt(math.isqrt(X**3))
    return V,[(a,b,a*a+b*b) for a in range(V+1) for b in range(-V,V+1)
              if (a>0 or b>0) and math.gcd(a,abs(b))==1 and X<=a*a+b*b<=V*V]


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=128
    out=dict(qualification='Positive heat-measure lower certificates for exact fractional means; '
             'not global upper bounds for Boolean sets or a Chowla solution.',
             heat_width_multiple=4,phase_s='5',radius_options=['1','3/4','1/2'],cases=[])
    root=Path('.research/experiments/wide_mean_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    for X in [256,1024,4096]:
        V,U=directions(X);m=4*V;cache={}
        def get(q):
            if q not in cache:cache[q]=disk_data(q)
            return cache[q]
        assignments={name:bytearray() for name in ['cyclic','greedy_heat']}
        for a,b,d in U:
            choices=[X*X//d,9*X*X//(16*d),X*X//(4*d)]
            assignments['cyclic'].append((a+2*b)%3)
            scores=[]
            for q in choices:
                info=get(q);k=np.arange(1,info['r']+1,dtype=float)
                scores.append(float((np.array(info['axis'][1:],dtype=float)/info['total']
                    *np.exp(-d*k*k/(2*m*m))*np.cos(5*a*k/V)).sum()))
            assignments['greedy_heat'].append(int(np.argmax(scores)))
        cosines=[(flint.arb(5*a)/V).cos() for a in range(X+1)]
        exp_cache={}
        for name,assignment in assignments.items():
            grouped=Counter();radial_counts=Counter();nmax=0
            for (a,b,d),index in zip(U,assignment):
                q=[X*X//d,9*X*X//(16*d),X*X//(4*d)][index];info=get(q)
                radial_counts[q]+=1;nmax+=(info['total']-1)//2
                for k in range(1,info['r']+1):
                    grouped[(d*k*k,a*k,info['total'])]+=info['axis'][k]
            H=flint.arb(0)
            for (norm2,x1,denominator),numerator in grouped.items():
                if norm2 not in exp_cache:exp_cache[norm2]=(-flint.arb(norm2)/(2*m*m)).exp()
                H+=2*numerator*exp_cache[norm2]*cosines[x1]/denominator
            mu=sum((flint.arb(n)*info['mean_n'].numerator/info['mean_n'].denominator
                    for q,n in radial_counts.items() for info in [get(q)]),flint.arb(0))
            mass_upper=math.ceil(float(mu.mid()))+1;mass_lower=math.floor(float(mu.mid()))-1
            assert mu<mass_upper and mu>mass_lower
            h=[6*X**3+i for i in [1,3,5,7]]
            assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
            r0=min(h)-X;assert r0*r0>=400*m*m
            tail=F(25*(m+1)**2,2**100);tail_ball=flint.arb(tail.numerator)/tail.denominator
            lower=F(0)
            if H+tail_ball<0:
                approximate=-float(H.mid())/(2*(1+float(tail)))
                lower=F(max(0,math.floor(approximate*10**6)-2),10**6)
                assert H+tail_ball+2*flint.arb(lower.numerator)/lower.denominator*(1+tail_ball)<0
            sqrt_mass=math.isqrt(mass_upper)+int(math.isqrt(mass_upper)**2<mass_upper)
            sqrt_max=math.isqrt(nmax)+int(math.isqrt(nmax)**2<nmax)
            row=dict(X=X,V=V,pattern=name,fibers=len(U),radius_indices_hex=assignment.hex(),
                     radius_sha256=hashlib.sha256(assignment).hexdigest(),m=m,
                     expected_mass_interval=[mass_lower,mass_upper],max_boolean_cardinality=nmax,
                     heat_H_main_ball=str(H),heat_H_over_V2_float=float(H.mid())/(V*V),
                     gaussian_alias_tail_upper=str(tail),heat_mean_interval=['1-tail','1+tail'],
                     fractional_mean_M_lower_rational=str(lower),
                     fractional_mean_M_global_upper_rational=str(F(len(U),2)),
                     mean_ratio_lower_rational=str(lower/sqrt_mass),
                     any_coupling_expected_ratio_lower_rational=str(lower/sqrt_max),
                     verified=True)
            out['cases'].append(row);(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
            print(json.dumps({k:row[k] for k in ['X','V','pattern','fibers','expected_mass_interval',
                        'heat_H_over_V2_float','fractional_mean_M_lower_rational','mean_ratio_lower_rational']}),flush=True)


if __name__=='__main__':main()
