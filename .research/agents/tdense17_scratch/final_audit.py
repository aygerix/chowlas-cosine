"""Last independent parameter/identity checks; VM only."""
import json
import math
import hashlib
import platform
from pathlib import Path

import numpy as np
from scipy.linalg import eigvalsh

ROOT=Path('.research/agents/tdense17_scratch')


def main():
    out=[]
    rng=np.random.default_rng(1717)
    for r in (32,128,512):
        B=np.triu(rng.random((r,r))<0.5,1)
        B=(B+B.T).astype(float)
        w=eigvalsh(B)
        s=r*r; n=r*s
        out.append(dict(r=r,twin_size=s,n=n,alpha=float(np.sum(w*w)/r**2),
            normalized_C4=float(np.sum(w**4)/r**4),
            residual_square=float((np.sum(w*w)-w[-1]**2)/r**2),
            beta1=float(np.sum(w[np.abs(w)<=math.sqrt(n)/s]**2)/r**2)))
    candidates=json.load(open(ROOT/'cliques.json'))
    verification=json.load(open(ROOT/'verification.json'))
    probes=json.load(open(ROOT/'probe.json'))
    for rec in probes:
        if rec['test']=='forced_spline' and 'unforced_expected_n' not in rec:
            rec['unforced_expected_n']=rec['expected_n']
            rec['expected_n']+=rec['forcing_l1']
    (ROOT/'probe.json').write_text(json.dumps(probes,indent=2)+'\n')
    large=json.load(open(ROOT/'large_spectra.json'))
    q61=next(d for d in json.load(open(ROOT/'zoo.json'))['records'] if d['name']=='singer_bu_61')
    first=large[0]['depth96']
    comparison={k:dict(dense=q61[k],stochastic=first[k]) for k in ('beta1','beta2','psd_distance','r_eff','bd_over_sqrtn')}
    assertions=[]
    for t in (4,5,8,16,32):
        L=t**6;k=t**5
        Q=L*(2*L*L+1)//3
        # Exact forcing cost from the closed cubic autocorrelation on 1<=a<=k<=L.
        sum_a=k*(k+1)//2
        sum_a2=k*(k+1)*(2*k+1)//6
        sum_a3=sum_a**2
        Dnum=L*sum_a2-(sum_a3-sum_a)//2
        assert 2*Dnum<=3*t**3*Q
        G=16*L*L
        R=(128*L*L-1).bit_length()
        u=math.isqrt(L*R)
        if u*u<L*R:u+=1
        assert 2*G*4<=2**R
        assert u*u>=L*R
        assert 3*t**3*32<=2*L
        assertions.append(dict(t=t,L=L,k=k,r=R,u=u,B_upper=u+2*t**3+1,
                               guaranteed_ratio=(k+1)/(2*(u+2*t**3+1))))
    result=dict(blowup_cgw=out,dense_vs_stochastic_q61=comparison,
                exact_parameter_checks=assertions)
    if (ROOT/'large_validation.json').exists():
        validation=json.load(open(ROOT/'large_validation.json'))
        result['q61_80_probes']={k:dict(dense=q61[k],stochastic=validation['depth96'][k])
            for k in ('beta1','beta2','psd_distance','r_eff','bd_over_sqrtn')}
    (ROOT/'final_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    lines=['## Large near-extremal spectral audit','',
        'NUMERICAL STOCHASTIC estimates: 10 Rademacher probes, seed 20261019, 24 explicitly computed positive outliers, fully reorthogonalized Lanczos of depths 48 and 96 on their orthogonal complement. Standard errors are sampling estimates, not certified enclosures; the depth comparison assesses quadrature sensitivity. The bottom eigenvalue is separately computed by FFT-Lanczos. These rows do not prove any spectral inequality.','',
        '| q | n | B1 depth96 | standard error | B1 depth48 | B2 | Dpsd | BD/sqrt n | eff rank | bottom/sqrt n |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for d in large:
        x=d['depth96']; y=d['depth48']
        lines.append(f"| {d['q']} | {d['n']} | {x['beta1']:.7g} | {x['beta1_standard_error']:.3g} | {y['beta1']:.7g} | {x['beta2']:.7g} | {x['psd_distance']:.7g} | {x['bd_over_sqrtn']:.7g} | {x['r_eff']:.7g} | {d['bottom_over_sqrtn']:.7g} |")
    lines += ['', 'NUMERICAL STOCHASTIC moment and trace audit, same probes. Values and raw standard errors for cutoff means, variances, positive/negative square masses and traces are in large_spectra.json.','',
        '| q | alpha | tr3/n³ | tr4/n⁴ | residual4/n³ | traceP/n^(3/2) | cutoff mean | cutoff variance |',
        '|---|---:|---:|---:|---:|---:|---:|---:|']
    for d in large:
        x=d['depth96']
        lines.append(f"| {d['q']} | {d['alpha']:.7g} | {x['tr3_n3']:.7g} | {x['tr4_n4']:.7g} | {x['residual4_n3']:.7g} | {x['traceP_n32']:.7g} | {x['mu_cut']:.7g} | {x['variance_cut']:.7g} |")
    (ROOT/'large_tables.md').write_text('\n'.join(lines)+'\n')
    paths=list(ROOT.glob('*.py'))+list(ROOT.glob('*.npz'))
    paths += [Path('examples/e99/e99.jsonl'),Path('examples/smallN_best.json'),
              Path('examples/singer_bu/certified.json'),Path('src/chowla.py'),Path('src/bu.py')]
    manifest=dict(python=platform.python_version(),numpy=np.__version__,
        commands=[
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 8 -t 600 python .research/agents/tdense17_scratch/probe.py',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 900 python .research/agents/tdense17_scratch/zoo.py',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 8 -t 500 python .research/agents/tdense17_scratch/sidon_completion.py',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 8 -t 600 python .research/agents/tdense17_scratch/verify.py',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 8 -t 900 python .research/agents/tdense17_scratch/large_spectra.py',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 8 -t 300 python .research/agents/tdense17_scratch/large_spectra.py validate',
            'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 8 -t 300 python .research/agents/tdense17_scratch/final_audit.py'],
        sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


if __name__=='__main__':main()
