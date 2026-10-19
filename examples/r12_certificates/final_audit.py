"""Final reproducibility, actual-degree and independent progression audit, VM only."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,py_compile
import numpy as np
from flint import arb,ctx
ctx.prec=220
ROOT=Path(__file__).resolve().parent

def main():
    previous=json.loads((ROOT/'manifest.json').read_text())
    matches={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest for name,digest in previous.items()}
    assert all(matches.values())
    for path in ROOT.glob('*.py'):py_compile.compile(str(path),doraise=True)
    progression=[]
    for ell in range(1,65):
        t=3*arb.pi()/(2*ell+1)
        direct=sum(((j*t).cos() for j in range(1,ell+1)),arb(0))
        margin=-direct-2*ell/(3*arb.pi())
        assert margin.lower()>0
        progression.append(str(margin))
    raw=json.loads((ROOT/'roughness_results.json').read_text())
    checks=json.loads((ROOT/'independent_checks.json').read_text())
    bykey={(r['N'],r['family']):r for r in raw['rows']}
    for n in (29,61):
        row=json.loads((ROOT/f'milp_N{n}.json').read_text())['probe'];bykey[(n,row['family'])]=row
    actual=[]
    for cert in checks['schedule_certificates']:
        N=cert['N'];H=cert['X'];row=bykey[(N,cert['family'])]
        u=[Q(float(v)).limit_denominator(100000) for v in row['u']]
        maxima=[];count=0
        for c,cutoff in enumerate(u):
            endpoint=H*cutoff.numerator//cutoff.denominator
            first=c if c else N
            ell=max(0,1+(endpoint-first)//N)
            count+=ell
            if ell:maxima.append(first+(ell-1)*N)
        assert count==cert['n']
        actual.append(dict(N=N,family=cert['family'],ambient_H=H,X=max(maxima),n=count))
    nonnested=[]
    for H in (65536,262144,1048576):
        data=json.loads((ROOT/f'nonnested_X{H}.json').read_text())
        assert sum(hi-lo+1 for lo,hi in data['runs'])==data['n']
        nonnested.append(dict(ambient_H=H,X=max(hi for lo,hi in data['runs']),n=data['n']))
    xi=np.unique(np.r_[np.linspace(0,60,121),np.linspace(.1,4,20)])
    out=dict(status='PROVED arithmetic/hash/Arb point audit; no new global minimum certificate',
             prior_hashes_match=matches,compiled_sources=[p.name for p in ROOT.glob('*.py')],
             progression_checks=64,structured_schedule_count=len(raw['rows']),milp_offset_count=len(xi),
             actual_schedule_degrees=actual,nonnested_degrees=nonnested)
    (ROOT/'final_audit.json').write_text(json.dumps(out,indent=2))
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.iterdir() if p.is_file() and p.name!='manifest.json'}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
