"""Joint low-minimum/L1 probes, with rigorous optional L1 quadrature.

The finite grid is enclosed by Arb. A distributional-second-derivative
bound supplies a rigorous O(N^-2) all-circle remainder for |D|.
Singer controls test L25, not their already known square-root dip bound.
"""
import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import time

import flint
import numpy as np
from singer import singer, is_perfect_difference_set


def rational_enclosure(value, scale=10**9):
    middle = float(value.mid())
    lo = math.floor(middle*scale)-4
    hi = math.ceil(middle*scale)+4
    while not value > flint.arb(lo)/scale:
        lo -= 4
    while not value < flint.arb(hi)/scale:
        hi += 4
    return F(lo,scale), F(hi,scale)


def certify_absolute_mean(A, grid):
    assert grid > 2*max(A)
    flint.ctx.prec = 96
    coeff = [flint.acb(0)]*grid
    for a in A:
        coeff[a] = flint.acb(1)
        coeff[-a] = flint.acb(1)
    values = flint.acb.dft(coeff)
    absolute = sum((abs(z.real) for z in values), flint.arb(0))/grid
    lo, hi = rational_enclosure(absolute)
    root = math.isqrt(2*sum(a**4 for a in A))+1
    remainder = F(7*root, grid*grid)
    # A global minimum has derivative zero. Taylor remainder for D is
    # <= pi^2 sum a^2/grid^2 < 10 sum a^2/grid^2.
    grid_hint = F(math.ceil(max(-float(z.real.mid()) for z in values)*10**6)+4,10**6)
    assert all(z.real+flint.arb(grid_hint.numerator)/grid_hint.denominator > 0 for z in values)
    Kupper = grid_hint+F(10*sum(a*a for a in A),grid*grid)
    return dict(grid=grid, precision_bits=96, grid_absolute_lower=str(lo),
                grid_absolute_upper=str(hi), absolute_remainder=str(remainder),
                L1_lower=str(max(F(0),lo-remainder)), L1_upper=str(hi+remainder),
                K_upper=str(Kupper),
                method='Arb DFT plus distributional-second-derivative L1 remainder; separate Taylor minimum bound')


def triple_count(A):
    coefficients = [0]*(max(A)+1)
    for a in A:
        coefficients[a] = 1
    square = flint.fmpz_poly(coefficients)**2
    return 6*sum(int(square[a]) for a in A)


def probe(label,A,upper=None,certificate=False,oversample=16,metadata=None):
    start = time.perf_counter()
    A=sorted(A);n=len(A);assert n and min(A)>0 and len(set(A))==n
    grid=1 << (oversample*max(A)).bit_length()
    coefficients=np.zeros(grid//2+1,dtype=np.complex128)
    coefficients[A]=1
    D=np.fft.irfft(coefficients,n=grid,norm='forward')
    ell=float(np.mean(np.abs(D)))/math.sqrt(n)
    third=triple_count(A)
    output=dict(label=label,A=A,n=n,max_A=max(A),grid=grid,
                diagnostic_L1_over_sqrt_n=ell,
                diagnostic_K_over_sqrt_n=float(-D.min())/math.sqrt(n),
                exact_third_moment=third,third_over_n32=third/n**1.5,
                numerical_status='Uncertified diagnostics; exact third moment separately counted',
                metadata=metadata)
    del D,coefficients
    if certificate:
        output['certificate']=certify_absolute_mean(A,grid)
        if upper is None:upper=F(output['certificate']['K_upper'])
        lo=F(output['certificate']['L1_lower']);hi=F(output['certificate']['L1_upper'])
        output['L1_conclusion_certified']=25*lo*lo>=n
        output['L1_below_threshold_certified']=25*hi*hi<n
    if upper is not None:
        upper=F(upper)
        output['K_upper_exact']=str(upper)
        output['low_ratio_hypothesis_certified']=upper*upper<=4*n
        moment=F(8*n*n,third+4*n*upper)
        output['moment_L1_lower']=str(moment)
        output['moment_alone_certifies_L1_conclusion']=25*moment*moment>=n
    output['seconds']=time.perf_counter()-start
    print(json.dumps({k:v for k,v in output.items() if k not in ['A','certificate']}),flush=True)
    return output


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--primes',default='31,127,257,509')
    parser.add_argument('--certify-small',action='store_true')
    parser.add_argument('--output',default='.research/experiments/l25_2026-10-21/probe.json')
    args=parser.parse_args()
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    records=[]
    if args.certify_small:
        for A,expected in [([1],4/flint.arb.pi()),([101],4/flint.arb.pi()),
                           ([1,2],3*flint.arb(3).sqrt()/flint.arb.pi())]:
            row=probe('analytic_'+str(A),A,certificate=True,oversample=32)
            c=row['certificate']
            assert expected>flint.arb(F(c['L1_lower']).numerator)/F(c['L1_lower']).denominator
            assert expected<flint.arb(F(c['L1_upper']).numerator)/F(c['L1_upper']).denominator
            records.append(row)
        A=json.loads(Path('examples/construct/N50_certified.json').read_text())['N50_x72']['A']
        records.append(probe('N50_x72',A,F(40309358,5000000),True,32))
        records.append(probe('interval4096',list(range(1,4097)),None,True,16))
    for p in map(int,args.primes.split(',')):
        B,modulus=singer(p)
        assert is_perfect_difference_set(B,modulus)
        A=sorted({abs(b-c) for b in B for c in B if b!=c})
        assert len(A)==len(B)*(len(B)-1)//2
        records.append(probe(f'singer_integer_differences_p{p}',A,len(B),
                             args.certify_small and p<=31,16,
                             dict(B=B,modulus=modulus,upper_proof='D_A=|F_B|^2-|B|>=-|B|; distinct integer differences checked')))
        path.write_text(json.dumps(dict(host=socket.gethostname(),cases=records),indent=2)+'\n')
    print(json.dumps(dict(status='PASS',output=str(path))),flush=True)


if __name__=='__main__':main()
