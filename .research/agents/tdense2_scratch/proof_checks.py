"""Exact supplemental checks; run ONLY on dirichlet via dirun.sh -c 2."""
import json
import importlib.metadata
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from flint import fmpz_poly

OUT=Path('.research/agents/tdense2_scratch')


def solve(M,b):
    aug=[list(row)+[v] for row,v in zip(M,b)]
    n=len(b)
    for i in range(n):
        pivot=aug[i][i]
        assert pivot
        aug[i]=[v/pivot for v in aug[i]]
        for j in range(n):
            if j==i:
                continue
            u=aug[j][i]
            aug[j]=[v-u*w for v,w in zip(aug[j],aug[i])]
    return [row[-1] for row in aug]


def main():
    exact=[]
    for r in range(1,4):
        a=lambda k:F(2**(k+1)-1,k+1)
        D=[[a(i+j+1) for j in range(1,r+1)] for i in range(1,r+1)]
        b=[1+a(2)]+[a(j+1) for j in range(2,r+1)]
        z=solve(D,b)
        schur=sum(u*v for u,v in zip(b,z))
        exact.append(dict(r=r,highest_moment=2*r+1,
            Schur_threshold=str(schur),constant_m=str(schur+1)))
    # A sufficient asymptotic inequality used in TD5, checked at the explicit
    # endpoint as integers; monotonicity thereafter is proved in the report.
    t=1024
    assert 2**(t//2) >= 2**64*(t+1)**4
    independent=[]
    for name in ['bohr_X200000','bohr4_X200000','fejer_X200000']:
        row=json.load(open(OUT/(name+'.json')))
        X=row['X']
        coeff=[0]*(2*X+1)
        for a in row['A']:
            coeff[X-a]=coeff[X+a]=1
        p=fmpz_poly(coeff)
        cube=p*p*p
        expected=np.load(OUT/(name+'_counts.npz'))['c']
        assert all(int(cube[3*X+k])==int(v) for k,v in enumerate(expected))
        independent.append(dict(name=name,all_cube_coefficients_rechecked=len(expected),
            method='fmpz_poly over Z, independent of modular CRT'))
    # Independent random direct rational Fourier audit (no CRT): every stored
    # rational witness is checked by its defining quadratic-form inequality.
    checked=0
    finite_bohr_bounds=[]
    for path in OUT.glob('*.json'):
        row=json.load(open(path))
        if not isinstance(row,dict) or 'higher_moments' not in row:
            continue
        n=row['n']
        for mm in row['higher_moments']:
            mus=list(map(F,mm['moments']))
            assert mus[0]==1 and mus[1]==0
            for w in mm['witnesses']:
                pp=w['integer_polynomial_coefficients']
                scale=w['scale']
                d=w['degree']
                den=sum(F(pp[i]*pp[j],scale**(i+j))*mus[i+j]
                    for i in range(d+1) for j in range(d+1))
                num=sum(F(pp[i]*pp[j],scale**(i+j))*mus[i+j+1]
                    for i in range(d+1) for j in range(d+1))
                lb=F(w['exact_m_lower_bound'])
                assert den>0 and num+lb*den==0
                mlb=F(w['exact_M_lower_bound'])
                assert mlb==((lb+F(int(mm['q'] in row['A']),2))/2 if mm['q'] else lb)
                if row['name'].startswith('bohr') and mm['q'] and d==3:
                    target=F(4,5) if row['name'].startswith('bohr4_') else F(1)
                    assert mlb>0 and mlb*mlb>=target*target*n
                    finite_bohr_bounds.append(dict(name=row['name'],q=mm['q'],
                        exact_claim=f'M >= ({target}) sqrt(n)',passed=True))
                checked+=1
    out=dict(status='EXACT checks PASS',endpoint_t=t,
        sufficient_endpoint_inequality=True,abstract_moment_obstruction=exact,
        rational_witnesses_rechecked=checked,independent_CRT_rechecks=independent,
        exact_finite_Bohr_seventh_moment_bounds=finite_bohr_bounds,
        versions={name:importlib.metadata.version(name) for name in ['python-flint','numpy','scipy']})
    (OUT/'proof_checks.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out),flush=True)


if __name__=='__main__':
    main()
