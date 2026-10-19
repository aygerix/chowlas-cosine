from pathlib import Path
import json,hashlib,platform
import numpy,sympy,flint
ROOT=Path(__file__).resolve().parent
report=ROOT.parent/'tdense16_report.md'
f=json.loads((ROOT/'adaptive_fake.json').read_text())['records']
a=json.loads((ROOT/'adversaries.json').read_text())['records']
v=json.loads((ROOT/'verification.json').read_text())
assert len(f)==3 and len(v['independent_fake_checks'])==3
assert len(a)==25 and v['genuine_numerical_cases']==23
assert sum(x['exact_rational_sumset_equations'] for x in v['independent_fake_checks'])==30
assert all(x['boolean_square_residual']==0 for x in a if 'fake' not in x['name'])
assert all(x['boolean_mellin_quadratic_error']>.1 for x in a if 'fake' in x['name'])
assert 'Status: COMPLETED' in report.read_text()
inputs=[report,Path('.research/PROOFS.md'),Path('.research/agents/tdense16_brief.md'),
        Path('.research/agents/tdense15_report.md'),Path('examples/r15_certificates/stability_probe.json'),
        Path('examples/r15_certificates/support_counterexample.json')]
artifacts=[p for p in ROOT.iterdir() if p.is_file() and p.suffix in ('.py','.json','.md') and p.name!='manifest.json']
files=sorted(set(inputs+artifacts))
manifest={'status':'FINAL_REPRODUCIBILITY_AUDIT','versions':{'python':platform.python_version(),'numpy':numpy.__version__,
  'sympy':sympy.__version__,'python_flint':flint.__version__},
  'counts':{'genuine_numerical_halfsets':23,'old_scalar_fakes':2,'new_exact_fake_instances':3,'new_exact_offzero_equations':30},
  'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({k:z for k,z in manifest.items() if k!='hashes'},indent=2))
print('Final reproducibility audit passed; hashed',len(files),'inputs and artifacts.')
