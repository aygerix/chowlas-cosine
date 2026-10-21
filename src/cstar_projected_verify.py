"""Exact reconstruction and independent convolution check of Fourier proposals."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import socket

import numpy as np
from cstar_resolvent_witness import rational_polynomial
from cstar_l25_probe import certify_absolute_mean


def independent_square_moments(A,nums):
    """Three ordinary Python integer products, with nonnegative no-carry digits.

    Separate +/- parts avoid signed-digit borrowing. This does not use FLINT.
    """
    B=len(nums);z=nums[::-1]+[0]+nums;total=sum(map(abs,z))
    width=(2*total.bit_length()+10)//8
    basebits=8*width;mask=(1<<basebits)-1
    assert total*total<1<<basebits
    plus=bytearray(len(z)*width);minus=bytearray(len(z)*width)
    for j,c in enumerate(z):
        target=plus if c>=0 else minus
        target[j*width:(j+1)*width]=abs(c).to_bytes(width,'little')
    p=int.from_bytes(plus,'little');m=int.from_bytes(minus,'little')
    pp=p*p;mm=m*m;pm=p*m
    def coefficient(j):
        shift=basebits*j
        return ((pp>>shift)&mask)+((mm>>shift)&mask)-2*((pm>>shift)&mask)
    Q=coefficient(2*B);H=2*sum(coefficient(2*B+a) for a in A)
    return Q,H


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',required=True)
    parser.add_argument('--output',required=True)
    parser.add_argument('--certify-L1',action='store_true')
    args=parser.parse_args()
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    source=json.loads(Path(args.input).read_text())
    caps=json.loads(Path('.research/experiments/l25_2026-10-21/scalar_singer.json').read_text())
    capmap={r['label']:r for r in caps['cases']}
    original=json.loads(Path('.research/experiments/l25_2026-10-21/probe.json').read_text())
    originals={r['label']:r for r in original['cases']}
    output=dict(host=socket.gethostname(),input=args.input,cases=[])
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    for row in source['cases']:
        A=row['A'];n=len(A);B=row['band'];cosine=row['cosine_coefficients']
        coeff=np.array([0.]+[c/2 for c in cosine])
        exact=rational_polynomial(A,coeff,B)
        Q,H=independent_square_moments(A,exact['positive_numerators'])
        assert Q==exact['norm_numerator'] and H==exact['energy_numerator']
        den=exact['denominator'];K=2*F(exact['global_M_lower'])
        assert Q*K*K+H*K-n*n*den*den<0
        result=dict(label=row['label'],A=A,n=n,certificate=exact,
                    independent_Python_convolution_match=True)
        if row['label'] in capmap:
            bestcap=capmap[row['label']]['degree_caps'][-1]
            assert bestcap['H_positive_definite']
            result['all_degree4_polynomial_M_cap']=bestcap['M_certificate_cap']
            result['strictly_exceeds_entire_degree4_space']=F(exact['global_M_lower'])>F(bestcap['M_certificate_cap'])
        if row['label'] in originals:
            result['all_circle_M_upper']=str(F(originals[row['label']]['K_upper_exact'])/2)
        if args.certify_L1:
            grid=1<<(16*max(A)).bit_length()
            result['absolute_mean']=certify_absolute_mean(A,grid)
            lower=F(result['absolute_mean']['L1_lower'])
            result['L25_conclusion_certified']=25*lower*lower>=n
        output['cases'].append(result)
        path.write_text(json.dumps(output,indent=2)+'\n')
        print(json.dumps(dict(label=row['label'],n=n,M_lower=exact['global_M_lower'],
                             Q_over_n=exact['Q_over_n'],H_over_n32=float(F(exact['H']))/n**1.5,
                             independent_check=True,exceeds_degree4=result.get('strictly_exceeds_entire_degree4_space'),
                             certified_L25=result.get('L25_conclusion_certified'))),flush=True)
    print(json.dumps(dict(status='PASS',output=str(path))),flush=True)


if __name__=='__main__':main()
