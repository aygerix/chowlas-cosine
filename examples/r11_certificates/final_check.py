"""R11 independent algebra, saved point recertification, and reproducibility manifest.
VM only. No optimizers are called by this verifier.
"""
import ast,hashlib,json,math,platform
from pathlib import Path
from fractions import Fraction as Q
import sympy as sp
from flint import arb,ctx
OUT=Path('.research/agents/tdense11_scratch')
def main():
    ctx.prec=220
    for path in OUT.glob('*.py'):ast.parse(path.read_text())
    c=json.load(open(OUT/'certificate_td.json'));v=json.load(open(OUT/'independent_verification.json'))
    assert c['status']==v['status']=='PROVED' and Q(c['D1'])==Q(259,2000)
    assert not c['failed'] and v['schur_cells']==192
    assert v['sha256']['certificate_td.json']==hashlib.sha256((OUT/'certificate_td.json').read_bytes()).hexdigest()
    p,z=sp.symbols('p z',real=True);e=p*(1-p)
    assert sp.expand(p**3+3*p*e+e*(1-2*p)-p)==0
    assert sp.expand(p**4+6*p*p*e+3*e*e-(3*p*p-2*p**4))==0
    assert sp.expand(e*(1-3*e)-(p*(1-p)**4+(1-p)*p**4))==0
    assert sp.expand(z*z*(z-1)**2-(z**4-2*z**3+z*z))==0
    # Exact exponent inequalities for the actual-DC three-profile escape.
    assert Q(11,30)<Q(9,20)<Q(7,15)<Q(1,2)
    assert 1-3*Q(9,20)==Q(-7,20)
    assert Q(1,5)+3*(Q(4,15)-Q(9,20))==Q(-7,20)
    assert Q(4,15)-Q(9,20)<0
    d=(1-arb.pi()/4)/2;S=arb.pi()/64;F=arb(67)/120-5*arb.pi()/32
    energy=S*S/(d.sqrt()+(d*F).sqrt().sqrt()+F.sqrt())**2
    assert energy>arb(3)/1000
    probes=json.load(open(OUT/'fourth_probe.json'));checks=[]
    for row in probes['rows']:
        if row['family']!='random':continue
        cpt=row['rounded'];A=[int(k) for k in (OUT/cpt['file']).read_text().split()]
        assert len(A)==len(set(A))==cpt['n'] and min(A)>0 and max(A)==cpt['X']
        ff=row['fft']
        # Parse the exact rational angle from the saved certificate, not the weighted FFT angle.
        pieces=cpt['angle'].split('*');index,grid=map(int,pieces[-1].split('/'))
        angle=2*arb.pi()*index/grid;value=sum(((k*angle).cos() for k in A),arb(0))
        R=Q(cpt['R_lower']);assert value<-arb(len(A)).sqrt()*arb(R.numerator)/R.denominator
        checks.append(dict(file=cpt['file'],n=len(A),value_ball=str(value),R_lower=str(R)))
    files=list(OUT.glob('*.py'))+list(OUT.glob('*.json'))+list(OUT.glob('*.txt'))
    hashes={path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(files) if path.name not in ('manifest.json','final_checks.json')}
    result=dict(status='PROVED_CHECKS',python=platform.python_version(),fourth_and_cubic_identities=True,D1='259/2000',C11='2000/259',
       triangular=dict(d=str(d),S=str(S),F=str(F),repair_energy_lower_bound=str(energy)),binary_points=checks,
       actual_DC_exponent_checks=True,source_and_data_sha256=hashes)
    OUT.joinpath('final_checks.json').write_text(json.dumps(result,indent=2))
    OUT.joinpath('manifest.json').write_text(json.dumps(dict(files=hashes,python=platform.python_version(),constraint='All mathematical computation via specified dirun VM; <=4 cores; Gurobi for optimization'),indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='source_and_data_sha256'},indent=2),flush=True)
if __name__=='__main__':main()
