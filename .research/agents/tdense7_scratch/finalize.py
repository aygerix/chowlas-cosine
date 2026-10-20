"""VM-only final independent audits, manifest and compact numerical summary."""
import json,math,hashlib,platform,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import gurobipy as gp
import mpmath
import sympy
from envelope_exact import certify
from witness import allwindows
from moment_gap import cert as gap_cert
OUT=Path('.research/agents/tdense7_scratch')

def moment_check():
    # Independent exact rational tests of the CF filling algebra, not proof by testing.
    tests=[]
    for r,C in [('0.811','4.164'),('0.77','4.331')]:
        rr=certify(C,r,100)
        assert rr['verified']
        # Each exact segment minimum must exceed this short rational lower bound.
        eps=F(1,25000) if C=='4.164' else F(1,100000)
        assert F(rr['margin'])>eps
        tests.append(dict(rho=r,C=C,minimum_float=rr['margin_float'],proved_margin_lower=str(eps)))
    return tests

def summary():
    ww=json.loads(OUT.joinpath('witness_B48.json').read_text())
    pp=[F(x) for x in ww['p']];B=ww['B'];d=F(ww['density']);a=pp[0]
    bb=F(ww['windows']['energy']['total'])
    assert ww['PD_proved'] and ww['symbol_roots_in_unit_interval']==0
    assert all(0<=p<=1 for p in pp) and pp[-1]==0 and pp[-2]>0
    wins=allwindows(pp,F(3849,5000))
    assert wins['density']['ok'] and wins['energy']['ok']
    search=json.loads(OUT.joinpath('adversarial_checks.json').read_text())
    real=json.loads(OUT.joinpath('realized_checks.json').read_text())
    def table(rows):
        return [dict(name=r['name'],n=r['n'],X=r['X'],R=r['R_estimate'],
                     elementary_window=r['family']['elem']['over_sqrtn'],
                     exact_elementary=r['exact_elementary']['bound_over_sqrtn'],
                     beckner_window=r['family']['beckner']['over_sqrtn'],
                     numerical_rho_window=r['family']['numerical_rho']['over_sqrtn'],
                     P29=r['P29']['over_sqrtn'],
                     prefix_dip=r['prefix_dip']['bound']/math.sqrt(r['n']),
                     P36=r['P36']['bound']/math.sqrt(r['n'])) for r in rows]
    v=math.pi**2/24+5/16;s=math.sqrt(1-v);rho=4/(3*math.sqrt(3))
    sine=dict(v=v,a=1/(1+s),density=(rho/2)/(1+s)**2,C=2/rho*(1+s)**2)
    res=dict(exact_CF_checks=moment_check(),profile=dict(C=ww['C'],a=float(a),density=float(d),
             energy=float(bb),energy_over_density=float(bb/d),PD_proved=True,windows_proved=True,
             density_origin_slack=float(a-2*d/F(3849,5000)),
             energy_origin_slack=float(a*(1-a)-2*bb/F(3849,5000)),
             density_Bernstein_leaves=sum(c['leaves'] for c in wins['density']['checks']),
             energy_Bernstein_leaves=sum(c['leaves'] for c in wins['energy']['checks'])),
             adversarial=table(search),realizations=table(real),sine_heuristic=sine)
    gap=[gap_cert('4.4393','.769801','.905646'),gap_cert('4.213','.811','.905646')]
    assert all(g['verified'] for g in gap)
    res['main_theorem_exact_certificates']=gap
    pointcerts=json.loads(OUT.joinpath('point_certificates.json').read_text())
    assert len(pointcerts)==len(search)+len(real)
    res['point_certificates_count']=len(pointcerts)
    OUT.joinpath('summary.json').write_text(json.dumps(res,indent=2))
    codefiles=sorted(OUT.glob('*.py'))+sorted(OUT.glob('*.c'))+sorted(OUT.glob('*.sh'))
    manifest=dict(python=sys.version,numpy=np.__version__,gurobi=gp.gurobi.version(),
                  sympy=sympy.__version__,mpmath=mpmath.__version__,seed=2026101907,
                  launcher='DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2',optimization_threads=2,
                  source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in codefiles},
                  numerical_minima='FFT at power of two >=128X, 24 direct local refinements; uncertified',
                  model_scope='PWL PD + macroscopic windows, not every microscopic alternative model',
                  dependency_change='SymPy 1.14 added on VM; original mpmath 1.4.1 restored after pip dependency downgrade')
    OUT.joinpath('manifest.json').write_text(json.dumps(manifest,indent=2))
    print(json.dumps(res,indent=2))
if __name__=='__main__':summary()
