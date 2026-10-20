"""Final VM-only artifact audit; do not infer kernel verification from these checks."""
from pathlib import Path
import contextlib,json,hashlib,ast,platform
import barrier_check,audit
ROOT=Path(__file__).resolve().parent
with open(ROOT/'final_audit_vm.log','w') as log,contextlib.redirect_stdout(log):
    result=dict(barrier=[barrier_check.barrier(u**3,J) for u,J in ((200,3),(400,5),(800,8))],
                fake_cubic=barrier_check.fake_cubic())
    (ROOT/'barrier_checks.json').write_text(json.dumps(result,indent=2))
    audit.main()
data=json.loads((ROOT/'audit_results.json').read_text())
assert len(data['cyclic_certificates'])==36
assert len(data['binary_diagnostics'])==20
assert all(r['R_point_lower_float']>.6 for r in data['binary_diagnostics'])
for p in ROOT.glob('*.py'):ast.parse(p.read_text())
summary=dict(python=platform.python_version(),arb_bits=data['arb_bits'],
             cyclic_certificates=len(data['cyclic_certificates']),binary_certificates=len(data['binary_diagnostics']),
             exact_curve_candidates=[r['candidates'] for r in data['exact_curves']],
             moment_orders=[r['order'] for r in data['moments']['finite_order_repair_jacobians']],
             barrier_outside_defects=[r['sign_defect_over_q2_ball'] for r in result['barrier']],
             binary_large_X=[r for r in data['binary_diagnostics'] if r['X']==1048576],
             status='All stated finite checks passed; paper proofs remain independent of these finite tests')
(ROOT/'final_summary.json').write_text(json.dumps(summary,indent=2))
manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.iterdir()
          if p.is_file() and p.name!='manifest.json' and p.suffix not in ('.so','.log')}
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({k:v for k,v in summary.items() if k!='binary_large_X'},indent=2),flush=True)
