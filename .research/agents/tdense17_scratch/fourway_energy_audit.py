"""Joint-condition values and reproducibility manifest. All execution on VM."""
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy

ROOT=Path('.research/agents/tdense17_scratch')


def main():
    recs=json.load(open(ROOT/'fourway_seeds.json'))+json.load(open(ROOT/'fourway_extras.json'))
    search=json.load(open(ROOT/'fourway_search.json'))
    for r in search:
        d=r['fine'].copy();d['name']='search_'+r['start'];recs.append(d)
    out=[]
    for r in recs:
        A=np.load(ROOT/(r['name']+'.npz'))['A']; n=len(A); X=int(A.max())
        H=max(1,X//2); step=max(1,H//2)
        centers=list(range(H,X+H,step));q=len(centers)
        G=1<<(4*(X+H)).bit_length()
        phi=np.zeros(G);S=0.;maxs2=-1.;best=None
        for m in centers:
            w=np.maximum(1-np.abs(A-m)/H,0)
            s2=float(w@w)
            c=np.zeros(G);c[A]=w
            f=np.fft.fft(c);square=np.abs(f)**2
            phi+=square;S+=s2
            if s2>maxs2:
                maxs2=s2;best=dict(m=m,s2=s2,E4=float(np.mean(square*square)),
                    B=float(np.sqrt(square).mean()/2))
        assert abs(phi.mean()-S)<1e-8*max(1.,S)
        eta=float(np.sqrt(phi).mean()**2/S)
        assert eta<=1+1e-9
        row=dict(name=r['name'],n=n,X=X,H=H,q=q,G=G,S=S,
            eta=eta,S_over_qn=S/(q*n),
            RMS_over_sqrtn=.5*math.sqrt(eta*S/q/n),
            window=best,window_E4_over_s2sq=best['E4']/best['s2']**2,
            triple_over_n32=r['triple_over_n32'],beta1=r['beta1'],
            negative_energy=r['negative_energy'])
        out.append(row)
    (ROOT/'fourway_energy.json').write_text(json.dumps(out,indent=2)+'\n')
    lines=['### Energy factors in the joint necessary conditions','',
        'NUMERICAL quadrature for eta; Fourier second/fourth moments evaluated by a no-alias grid in floating arithmetic. H=floor(X/2), centers spaced by max(1,H//2); eta always includes the actual S/q energy factor. E4/s2² is for the tested center with largest s2. All 58 seeds/adversaries and ten search winners appear.','',
        '| family | n | eta | S/(q n) | RMS certificate/sqrt n | E4/s2² | e/n^(3/2) | beta1 |',
        '|---|---:|---:|---:|---:|---:|---:|---:|']
    for d in out:
        keys=('eta','S_over_qn','RMS_over_sqrtn','window_E4_over_s2sq','triple_over_n32','beta1')
        lines.append('| '+d['name']+' | '+str(d['n'])+' | '+' | '.join(f'{d[k]:.6g}' for k in keys)+' |')
    (ROOT/'fourway_energy_tables.md').write_text('\n'.join(lines)+'\n')
    paths=list(ROOT.glob('fourway*.py'))+list(ROOT.glob('fourway*.json'))
    paths+=list(ROOT.glob('search_*.npz'))
    commands=[
        'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 900 python .research/agents/tdense17_scratch/fourway.py seeds',
        'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 900 python .research/agents/tdense17_scratch/fourway.py search --steps 400',
        'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense17_scratch/fourway.py audit',
        'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense17_scratch/fourway_verify.py',
        'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense17_scratch/fourway_extras.py',
        'DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense17_scratch/fourway_energy_audit.py']
    manifest=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        seed_count=len(recs)-len(search),search_starts=len(search),
        swap_proposals=sum(r['steps'] for r in search),commands=commands,
        sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (ROOT/'continuation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(seed_count=manifest['seed_count'],search_starts=len(search),
        swap_proposals=manifest['swap_proposals'],energy_rows=len(out),
        first=out[0],last=out[-1])),flush=True)


if __name__=='__main__':main()
