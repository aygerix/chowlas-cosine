"""Final consistency/hash audit and outward display formatting. VM only."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0,'.research/agents/tdense18_scratch')
from probe18 import boundary
from finalize18 import write_minima_table

ROOT=Path('.research/agents/tdense18_scratch')


def main():
    manifest=json.loads((ROOT/'manifest.json').read_text())
    permitted_source_updates={str(ROOT/'probe18.py'),str(ROOT/'finalize18.py')}
    checked=0
    for name,digest in manifest['sha256'].items():
        if name in permitted_source_updates:
            continue
        assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
        checked+=1
    rows=json.loads((ROOT/'adversaries.json').read_text())
    assert len(rows)==33 and len({r['name'] for r in rows})==33
    for r in rows:
        A=np.load(ROOT/(r['name']+'.npz'))['A']
        assert len(A)==r['n'] and len(np.unique(A))==len(A)
        assert np.all(A>0) and int(max(A))==r['X']
        assert hashlib.sha256(A.astype('<i8').tobytes()).hexdigest()==r['sha256']
    sep=json.loads((ROOT/'reverse_separation.json').read_text())
    assert sep['epsilon']=='3/7' and Fraction(sep['threshold'])==Fraction(18,7)
    assert Fraction(sep['p28']['upper'])<Fraction(1424,1000)
    assert Fraction(sep['M']['lower'])>Fraction(3959921,10**6)
    assert Fraction(sep['M']['upper'])<Fraction(3960017,10**6)
    assert len(sep['p28']['rows'])==50 and sep['p28']['grid']==8192
    graph=json.loads((ROOT/'graph_exact.json').read_text())
    assert graph['shift']=='36/7' and graph['size']==73
    assert len(graph['charpoly_plus_coefficients'])==74
    assert all(int(c)>0 for c in graph['charpoly_plus_coefficients'])
    edge=boundary(sep['A'])
    assert edge['sharp_max_k']==edge['sharp_max_k_upper']==3
    assert Fraction(edge['upper_rational'])<Fraction(262,1000)
    sep['boundary']=edge
    (ROOT/'reverse_separation.json').write_text(json.dumps(sep,indent=2)+'\n')
    minima=json.loads((ROOT/'representative_minima.json').read_text())
    assert len(minima)==6
    for r in minima:
        assert Fraction(r['lower'])<Fraction(r['upper'])
        record=next(t for t in rows if t['name']==r['name'])
        assert r['sha256']==record['sha256']
    write_minima_table(minima)
    verification=json.loads((ROOT/'verification.json').read_text())
    assert verification['exhaustive_boundary_sets']==255
    assert verification['fractional_H_interpolation_checks']==3648
    assert len(verification['packet_theorem'])==10
    for key in ('block_theorem','variable_occupancy_blocks'):
        rec=verification[key]
        assert Fraction(rec['symmetrized_L2'])==2*Fraction(rec['v'])
        assert Fraction(rec['symmetrized_L4'])<=Fraction(rec['fourth_upper'])
    audit=dict(passed=True,adversarial_sets=33,saved_set_hashes_verified=33,
        existing_artifact_hashes_verified=checked,representative_M_certificates=6,
        exact_boundary_sets=255,fractional_window_interpolations=3648,
        periodic_packet_cases=10,correlated_block_cases=2,
        reverse_epsilon='3/7',reverse_M_lower='3.959921',reverse_M_upper='3.960017',
        complete_P28_upper='1.424',complete_boundary_upper='0.262',
        graph_M_upper='18/7',largest_sharp_boundary_k=3,
        note='No new numerical optimization. Hashes, exact inequalities, stored certificates, and outward rounding checked.')
    (ROOT/'final_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
    manifest['sha256']={str(p):hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(ROOT.iterdir()) if p.suffix in ('.py','.json','.md','.npz') and p.name!='manifest.json'}
    command='DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 8 -t 120 python .research/agents/tdense18_scratch/audit18.py'
    if command not in manifest['reproduction_commands']:
        manifest['reproduction_commands'].append(command)
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(audit),flush=True)


if __name__=='__main__':
    main()
