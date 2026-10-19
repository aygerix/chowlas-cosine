"""Round 18 independent Sturm, representative Arb minima, reproducibility ledger.
Run only on dirichlet through src/dirun.sh, <=4 cores.
"""
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys

import flint
import numpy as np

sys.path.insert(0,'.research/agents/tdense18_scratch')
from certify18 import certify_M, graph_certificate

ROOT=Path('.research/agents/tdense18_scratch')


def write_minima_table(minima):
    lines=['# Representative all-circle M enclosures','',
           'PROVED finite enclosures, directed Arb arithmetic. Each row combines an Arb value at a rational angle with an all-grid DFT and the global second derivative bound at a global minimizer. Displayed bounds are rounded outward to six decimal places; exact rational bounds are in representative_minima.json.','',
           '| family | n | X | M lower | M upper | grid |',
           '|---|---:|---:|---:|---:|---:|']
    scale=10**6
    for r in minima:
        lo=(Fraction(r['lower'])*scale)//1
        hi=-((-Fraction(r['upper'])*scale)//1)
        low=f'{lo//scale}.{lo%scale:06d}'
        high=f'{hi//scale}.{hi%scale:06d}'
        lines.append(f"| {r['name']} | {r['n']} | {r['X']} | {low} | {high} | {r['grid']} |")
    (ROOT/'certified_minima_table.md').write_text('\n'.join(lines)+'\n')


def sturm(A,xmin):
    X=max(A)
    polynomials=[flint.fmpz_poly([1]),flint.fmpz_poly([0,1])]
    t=flint.fmpz_poly([0,1])
    for j in range(2,X+1):
        polynomials.append(2*t*polynomials[-1]-polynomials[-2])
    f=sum((polynomials[a] for a in A),flint.fmpz_poly([0]))
    p=flint.fmpq_poly(1000*f+3961)
    seq=[p,p.derivative()]
    while seq[-1]:
        r=-(seq[-2]%seq[-1])
        if not r:
            break
        seq.append(r)
    def signs(x):
        return [int(q(x)>0)-int(q(x)<0) for q in seq]
    def variations(ss):
        nz=[s for s in ss if s]
        return sum(a!=b for a,b in zip(nz,nz[1:]))
    left=signs(-1)
    right=signs(1)
    assert p(-1)>0 and p(1)>0 and p(0)>0
    assert variations(left)==variations(right)
    tt=Fraction(str(math.cos(xmin))).limit_denominator(1000000)
    value=flint.fmpq_poly(f)(flint.fmpq(tt.numerator,tt.denominator))
    assert -value>flint.fmpq(39599,10000)
    result=dict(M_lower='39599/10000',M_upper='3961/1000',
                degree=X,sturm_length=len(seq),left_signs=left,right_signs=right,
                left_variations=variations(left),right_variations=variations(right),
                lower_witness_t=str(tt),lower_witness_value=str(value),
                method='exact rational Chebyshev polynomial; Sturm zero count and exact rational point',
                sturm_sha256=hashlib.sha256('\n'.join(map(str,seq)).encode()).hexdigest())
    (ROOT/'sturm_independent.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


def main():
    flint.ctx.prec=120
    separation=json.loads((ROOT/'reverse_separation.json').read_text())
    assert separation['all_certificates_below_threshold']
    rows=json.loads((ROOT/'adversaries.json').read_text())
    winner=next(r for r in rows if r['name']=='r17_search_smallN_36')
    A=separation['A']
    exact=sturm(A,winner['xmin'])
    # Tighten the same-epsilon reverse counterexample with a fresh exact graph
    # certificate; retain the complete previously certified P28 upper bound.
    bound=Fraction(18,7)
    graph=graph_certificate(A,bound)
    assert Fraction(separation['p28']['upper'])<bound
    assert Fraction(separation['boundary']['upper_rational'])<bound
    assert Fraction(separation['M']['lower'])>bound
    separation['threshold']=str(bound)
    separation['epsilon']='3/7'
    separation['graph']=graph
    separation['independent_sturm']='sturm_independent.json'
    (ROOT/'reverse_separation.json').write_text(json.dumps(separation,indent=2)+'\n')
    chosen=['cum_p1_96','antithetic_96','nested_Bohr_r1_96',
            'dilation_union_96','singer_taper_q31_k9','forced_thin_96']
    minima=[]
    for name in chosen:
        row=next(r for r in rows if r['name']==name)
        A=np.load(ROOT/(name+'.npz'))['A'].tolist()
        G=1<<(64*max(A)-1).bit_length()
        cert=certify_M(A,row['xmin'],G)
        cert.update(name=name,n=len(A),X=max(A),sha256=row['sha256'])
        minima.append(cert)
        (ROOT/'representative_minima.json').write_text(json.dumps(minima,indent=2)+'\n')
        print(json.dumps(cert),flush=True)
    write_minima_table(minima)
    outputs=[p for p in ROOT.iterdir() if p.suffix in ('.py','.json','.md','.npz') and p.name!='manifest.json']
    manifest=dict(computation='VM dirichlet only, bash shell, at most 4 cores',
        reproduction_commands=[
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense18_scratch/probe18.py',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense18_scratch/verify18.py',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense18_scratch/certify18.py 8192',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense18_scratch/finalize18.py'],
        run_notes=[
            'Initial probe stopped on repeated quantile sample; phases were restricted to [.25,.75] and actual distinctness asserted.',
            'First complete probe resumed after replacing the redundant H=1 FFT loop by its exact value 1/2.',
            'NumPy bool in provenance converted to Python bool before JSON serialization; completed numerical rows retained.',
            'All retries and control operations used dirun.sh; no mathematical computation on host.'],
        sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(outputs)})
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(reverse_epsilon=separation['epsilon'],
        reverse_threshold=separation['threshold'],p28_upper=separation['p28']['decimal'],
        exact_Sturm_M=[exact['M_lower'],exact['M_upper']],
        representative_minima=len(minima),manifest_files=len(outputs))),flush=True)


if __name__=='__main__':
    main()
