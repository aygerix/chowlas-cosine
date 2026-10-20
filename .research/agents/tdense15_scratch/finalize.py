"""Record reproducibility and verify final artifact consistency. VM only."""
from pathlib import Path
import hashlib,json,platform
from fractions import Fraction as Q
import numpy, sympy, flint

ROOT=Path(__file__).resolve().parent
cert=json.loads((ROOT/'certificate_sigma.json').read_text())
verified=json.loads((ROOT/'sigma_independent.json').read_text())
sturm=json.loads((ROOT/'mixing_sturm.json').read_text())
checks=json.loads((ROOT/'proof_checks.json').read_text())
probe=json.loads((ROOT/'stability_probe.json').read_text())
assert cert['status']==verified['status']==sturm['status']=='PROVED'
assert cert['sigma']=='2/3' and Q(cert['D1'])==Q(73,1000)
assert Q(verified['D1'])==Q(73,1000)
assert verified['pointwise_leaves']==sum(len(x['leaves']) for x in cert['pointwise'])==767
assert len(cert['pointwise'])==128 and len(cert['schur'])==64
assert checks['exact_parity_sets']==318 and len(checks['stability_checks'])==19
assert not cert['failed'] and Q(cert['min_schur'])>0
assert sturm['variations']==[1,1]
sources=[
    Path('src/e94b_mix_certify.py'),
    Path('examples/r11_certificates/certify.py'),
    Path('examples/r11_certificates/independent_verify.py'),
    Path('examples/r11_certificates/support_lines.json'),
    Path('.research/agents/tdense9_scratch/long_gram_bounds.json'),
    Path('.research/agents/tdense8_scratch/potential.py'),
    Path('.research/agents/tdense13_scratch/barrier_check.py'),
    Path('examples/e95/discovery_sigma0.6667_K64_d10_s0.1_t0.json'),
    Path('.research/agents/tdense15_report.md'),
]
paths=sorted({*sources,*[p for p in ROOT.iterdir() if p.is_file() and p.name not in ('manifest.json','finalize.log')]})
sha={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
fake=next(r for r in probe['records'] if r['name']=='R12_S_nonboolean')
out=dict(status='artifact consistency passed; mathematical statuses retained in individual files',
         python=platform.python_version(),numpy=numpy.__version__,sympy=sympy.__version__,
         flint=flint.__version__,new_optimizer_calls=0,cores=4,VM='34.148.157.169',
         D_sigma='73/1000',dense_C_strict_upper='1000/73',
         verified_pointwise_leaves=767,schur_cells=64,exact_parity_sets=318,
         numerical_cases=len(probe['records']),
         R12_fake_boolean_square_error=fake['boolean_square_error'],
         R12_fake_positive_square_flat_rms=fake['positive_square_flat_rms'],sha256=sha)
ROOT.joinpath('manifest.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='sha256'},indent=2))
