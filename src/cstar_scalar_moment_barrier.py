"""Exact limits of ALL fixed-degree polynomial-in-D mixed certificates.

This probes a method for arbitrary Boolean supports, not new minimum
bounds for the already studied rounded-profile construction.
"""
from fractions import Fraction as F
import argparse
import json
import math
from pathlib import Path
import socket

import flint


def solve_rational(matrix, vector):
    n=len(vector)
    rows=[[F(t) for t in row]+[F(vector[i])] for i,row in enumerate(matrix)]
    for i in range(n):
        pivot=next(j for j in range(i,n) if rows[j][i])
        rows[i],rows[pivot]=rows[pivot],rows[i]
        p=rows[i][i];rows[i]=[t/p for t in rows[i]]
        for j in range(n):
            if j!=i:
                c=rows[j][i];rows[j]=[x-c*y for x,y in zip(rows[j],rows[i])]
    return [row[-1] for row in rows]


def moments_flint(A,order):
    X=max(A);coeff=[0]*(2*X+1)
    for a in A:coeff[X-a]=coeff[X+a]=1
    P=flint.fmpz_poly(coeff);power=flint.fmpz_poly([1]);moments=[1]
    for k in range(1,order+1):
        power*=P
        moments.append(int(power[k*X]))
    return moments


def moments_packed(A,order):
    """Independent Python-integer convolution, with provable no-carry base."""
    X=max(A);width=(order*(2*len(A)).bit_length()+8)//8
    basebits=8*width;mask=(1<<basebits)-1
    assert (2*len(A))**order < 1<<basebits
    data=bytearray((2*X+1)*width)
    for a in A:data[(X-a)*width]=data[(X+a)*width]=1
    packed=int.from_bytes(data,'little');power=1;out=[1]
    for k in range(1,order+1):
        power*=packed
        out.append((power>>(basebits*k*X))&mask)
    return out


def analyze(A,degree):
    m=moments_flint(A,2*degree+1)
    H=[[m[i+j+1]-m[i]*m[j+1]-m[j]*m[i+1]
        for j in range(1,degree+1)] for i in range(1,degree+1)]
    a=[m[i+1] for i in range(1,degree+1)]
    minors=[int(flint.fmpz_mat([r[:k] for r in H[:k]]).det()) for k in range(1,degree+1)]
    out=dict(degree=degree,moments=m,H=H,a=a,leading_minors=minors,
             H_positive_definite=all(t>0 for t in minors))
    if out['H_positive_definite']:
        y=solve_rational(H,a);cap=sum(x*t for x,t in zip(a,y))
        assert cap>0
        assert all(sum(F(H[i][j])*y[j] for j in range(degree))==a[i] for i in range(degree))
        schur=[[F(x) for x in row] for row in H]
        for k in range(degree):
            pivot=schur[k][k];assert pivot>0
            for i in range(k+1,degree):
                for j in range(k+1,degree):
                    schur[i][j]-=schur[i][k]*schur[k][j]/pivot
        out.update(K_certificate_cap=str(cap),M_certificate_cap=str(cap/2),
                   norm_budget_independent=True,
                   meaning='All mean-zero real polynomials q=P(D), degree(P)<=degree, have mixed determinant root K<cap.')
    return out


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    parser=argparse.ArgumentParser()
    parser.add_argument('--singer', action='store_true')
    parser.add_argument('--output',default='.research/experiments/l25_2026-10-21/scalar_barrier.json')
    args=parser.parse_args()
    if args.singer:
        source=json.loads(Path('.research/experiments/l25_2026-10-21/probe.json').read_text())
        inputs=[dict(label=r['label'],A=r['A'],upper=r['K_upper_exact'])
                for r in source['cases'] if r['label'].endswith(('p31','p127'))]
    else:
        source=json.loads(Path('.research/experiments/forced_plateau_2026-10-20/results.json').read_text())
        inputs=[dict(label='plateau_L'+str(r['L']),A=r['A'],upper=str(2*F(r['certificate']['M_upper_rational'])))
                for r in source['cases']]
    output=dict(host=socket.gethostname(),cases=[],qualification='Exact finite scalar-polynomial witness-space caps, not bounds on actual M.')
    path=Path(args.output)
    path.parent.mkdir(parents=True,exist_ok=True)
    for row in inputs:
        A=row['A'];cases=[analyze(A,d) for d in [1,2,3,4]]
        independent=moments_packed(A,9)
        assert independent==cases[3]['moments']
        record=dict(label=row['label'],n=len(A),A=A,degree_caps=cases,
                    independent_degree4_moments_match=True,
                    existing_M_upper=str(F(row['upper'])/2))
        output['cases'].append(record)
        path.write_text(json.dumps(output,indent=2)+'\n')
        print(json.dumps(dict(label=row['label'],n=len(A),caps=[dict(degree=c['degree'],SPD=c['H_positive_definite'],Mcap=float(F(c['M_certificate_cap'])) if c.get('M_certificate_cap') else None) for c in cases])),flush=True)
    def mu(r):
        return F(sum((-1)**j*math.comb(2*r,j)*(r-j)**(2*r-1) for j in range(r)),math.factorial(2*r-1))
    output['limiting_Singer_caps']=[]
    for d in range(1,9):
        H=[[mu(i+j+1) for j in range(1,d+1)] for i in range(1,d+1)]
        a=[F(1)]+[mu(i+1) for i in range(2,d+1)]
        y=solve_rational(H,a);cap=sum(x*t for x,t in zip(a,y))
        assert all(sum(H[i][j]*y[j] for j in range(d))==a[i] for i in range(d))
        output['limiting_Singer_caps'].append(dict(degree=d,K_cap=str(cap),M_cap=str(cap/2)))
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',output=str(path))),flush=True)


if __name__=='__main__':main()
