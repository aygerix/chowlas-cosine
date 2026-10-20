"""Exact finite parity obstructions for integer-disk lens marginals.

Mod-four disk counts and six GL(2,F2) phases need no floating Fourier
evaluation. Scalar CRT transfer uses a rational Lipschitz bound.
Run on Dirichlet.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
from cstar_wide_mean import disk_data,directions


MATRICES=[(a,b,c,d) for a in [0,1] for b in [0,1] for c in [0,1] for d in [0,1]
          if (a*d-b*c)%2==1]


def parity_data(q):
    info=disk_data(q);r=info['r'];counts=[[0]*4 for _ in range(4)]
    for x in range(-r,r+1):
        y=math.isqrt(q-x*x)
        for residue in range(4):
            counts[x%4][residue]+=(y-residue)//4-(-y-1-residue)//4
    assert sum(map(sum,counts))==info['total']
    budgets={}
    for u,v in [(1,0),(0,1),(1,1)]:
        re=[0]*4;im=[0]*4
        for x in range(4):
            for y in range(4):
                phase=(u*x+v*y)%4;index=2*(x%2)+y%2;n=counts[x][y]
                re[index]+=n*[1,0,-1,0][phase];im[index]+=n*[0,1,0,-1][phase]
        numerator=sum(a*a+b*b for a,b in zip(re,im));budgets[(u,v)]=numerator-info['total']
    total=info['total'];diamond=2*r*r+2*r+1
    assert total>=diamond
    assert budgets[(1,0)]==budgets[(0,1)]<=0
    assert 5*budgets[(1,1)]<=-total
    info.update(budgets=budgets,mod4=counts)
    return info


def certify_profile(X,V,U,assignment,cache,mass_upper=None):
    groups=Counter();nmax=0;mass=F(0)
    for (a,b,d),index in zip(U,assignment):
        q=[X*X//d,9*X*X//(16*d),X*X//(4*d)][index]
        if q not in cache:cache[q]=parity_data(q)
        info=cache[q];assert q>=1
        groups[(q,a%2,b%2)]+=1;nmax+=(info['total']-1)//2
    # Exact lower/upper integer enclosures for the mass, avoiding giant lcms.
    mass_scaled_upper=0;scale=10**6
    for (q,a,b),count in groups.items():
        z=cache[q]['mean_n'];mass_scaled_upper+=-((-count*z.numerator*scale)//z.denominator)
    certified_mass_upper=(mass_scaled_upper+scale-1)//scale
    if mass_upper is not None:assert certified_mass_upper<=mass_upper
    upper_D=[]
    for A in MATRICES:
        numerator=0
        for (q,a,b),count in groups.items():
            v=((A[0]*a+A[2]*b)%2,(A[1]*a+A[3]*b)%2)
            info=cache[q];z=count*info['budgets'][v]
            numerator+=-((-z*scale)//info['total'])
        upper_D.append(F(numerator,scale))
    index=min(range(6),key=lambda i:upper_D[i]);upper=upper_D[index]
    h=[6*X**3+i for i in [1,3,5,7]];A=MATRICES[index]
    residues=[(m-1)//2 if bit else 0 for bit,m in zip(A,h)]
    error=F(88*X*certified_mass_upper,7*min(h))
    scalar_upper=upper+error;lower=max(F(0),-scalar_upper/2)
    sqrt_mass=math.isqrt(certified_mass_upper)+int(math.isqrt(certified_mass_upper)**2<certified_mass_upper)
    sqrt_max=math.isqrt(nmax)+int(math.isqrt(nmax)**2<nmax)
    return dict(matrix_D_upper_rationals=list(map(str,upper_D)),best_matrix=list(A),
                best_residues=residues,matrix_D_upper_rational=str(upper),
                scalar_transfer_error_upper=str(error),fractional_mean_M_lower_rational=str(lower),
                fractional_mean_M_global_upper_rational=str(F(len(U),2)),
                certified_mass_upper=certified_mass_upper,max_boolean_cardinality=nmax,
                mean_ratio_lower_rational=str(lower/sqrt_mass),
                any_coupling_expected_ratio_lower_rational=str(lower/sqrt_max),verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    root=Path('.research/experiments/wide_mean_2026-10-20')
    old=json.loads((root/'results.json').read_text());cache={}
    # Validate the elementary finite inequalities over all small disk radii.
    for q in range(1,4097):parity_data(q)
    for u in [(1,0),(0,1),(1,1)]:
        orbit=Counter(((A[0]*u[0]+A[2]*u[1])%2,(A[1]*u[0]+A[3]*u[1])%2) for A in MATRICES)
        assert orbit==Counter({(1,0):2,(0,1):2,(1,1):2})
    out=dict(qualification='Exact finite parity counts plus rational CRT error bounds for fractional means; '
             'not a theorem for individual Boolean sets.',finite_q_inequalities_checked=4096,matrices=MATRICES,
             widened_cases=[],near_linear_cases=[])
    for row in old['cases']:
        X=row['X'];V,U=directions(X);assignment=bytes.fromhex(row['radius_indices_hex'])
        assert len(U)==len(assignment) and hashlib.sha256(assignment).hexdigest()==row['radius_sha256']
        result=certify_profile(X,V,U,assignment,cache,row['expected_mass_interval'][1])
        result.update(X=X,V=V,pattern=row['pattern'],fibers=len(U))
        out['widened_cases'].append(result)
        print(json.dumps({k:result[k] for k in ['X','V','pattern','fibers','fractional_mean_M_lower_rational','mean_ratio_lower_rational']}),flush=True)
    for X in [256,1024,4096]:
        L=X.bit_length()-1;g=max(2,(L-1).bit_length());V=X//g
        U=[(a,b,a*a+b*b) for a in range(V+1) for b in range(-V,V+1)
           if (a>0 or b>0) and math.gcd(a,abs(b))==1 and X<=a*a+b*b<=V*V]
        assignment=bytearray()
        for a,b,d in U:
            options=[X*X//d,9*X*X//(16*d),X*X//(4*d)]
            scores=[]
            for q in options:
                if q not in cache:cache[q]=parity_data(q)
                info=cache[q]
                scores.append(F(2*info['budgets'][(1,0)]+info['budgets'][(1,1)],3*info['total']))
            assignment.append(max(range(3),key=lambda i:scores[i]))
        result=certify_profile(X,V,U,assignment,cache)
        result.update(X=X,V=V,pattern='greedy_parity',fibers=len(U),cutoff_divisor=g,
                      radius_indices_hex=assignment.hex(),radius_sha256=hashlib.sha256(assignment).hexdigest())
        out['near_linear_cases'].append(result)
        print(json.dumps({k:result[k] for k in ['X','V','pattern','fibers','fractional_mean_M_lower_rational','mean_ratio_lower_rational']}),flush=True)
    (root/'parity.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
