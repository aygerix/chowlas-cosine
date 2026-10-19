"""Final VM audit of saved sources, exact exponent budget and saved binary dip certificates."""
import json,hashlib,platform
from pathlib import Path
from fractions import Fraction as Q
import gurobipy as gp
import sympy
from flint import arb,ctx
OUT=Path('.research/agents/tdense10_scratch');ctx.prec=220
ind=json.loads((OUT/'independent_verification.json').read_text());cert=OUT/'certificate_td.json'
assert ind['status']=='PROVED' and hashlib.sha256(cert.read_bytes()).hexdigest()==ind['sha256']['certificate_td.json']
compiled=[]
for p in sorted(OUT.glob('*.py')):compile(p.read_text(),str(p),'exec');compiled.append(p.name)
a=Q(4,5);h=Q(2,5);b=Q(9,10)
exponents=dict(l1_cost=1-2*a/3,coefficient_amplitude=a/3,second_profile=-a/3,fourth_growth=a/3,smoothing_sup=a/3-h,base_minimum=b/2)
assert exponents['l1_cost']<Q(1,2) and exponents['base_minimum']<Q(1,2) and exponents['smoothing_sup']<0
proofs=[]
for row in json.loads((OUT/'third_direct.json').read_text())['demos']:
    p=row['point_certificate'];A=list(map(int,(OUT/p['A_file']).read_text().split()));assert len(A)==p['n'] and A==sorted(set(A)) and A[0]>0 and A[-1]==p['X']
    ff=row['rounded_fft'];xx=arb.pi()*(2*ff['index'])/ff['grid'];value=arb(0)
    for k in A:value+=(xx*k).cos()
    q=Q(p['R_strict_lower']);assert value<-(arb(q.numerator)/q.denominator)*arb(len(A)).sqrt()
    proofs.append(dict(file=p['A_file'],n=len(A),X=A[-1],value_ball=str(value),R_lower=str(q)))
manifest={p.name:dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='manifest.json'}
out=dict(status='PROVED_VERIFICATIONS',certificate_sha256=manifest['certificate_td.json']['sha256'],compiled_sources=compiled,exponents={k:str(v) for k,v in exponents.items()},independent_dips=proofs,python=platform.python_version(),sympy=sympy.__version__,gurobi=gp.gurobi.version(),files=manifest)
(OUT/'manifest.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
