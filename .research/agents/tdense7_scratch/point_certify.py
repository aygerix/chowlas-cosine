"""VM-only rigorous point evaluations: lower bounds for M, not all-circle minima."""
from pathlib import Path
from fractions import Fraction as F
import json,math
from flint import arb,ctx
ctx.prec=192
OUT=Path('.research/agents/tdense7_scratch')
rows=[]
for prefix in ['adversarial','realized']:
    sets=json.loads(OUT.joinpath(prefix+'_sets.json').read_text())
    checks=json.loads(OUT.joinpath(prefix+'_checks.json').read_text())
    for row in checks:
        A=sets[row['name']];n=len(A)
        q=round(row['minimum']['angle']*10**14);x=arb(q)/arb(10**14)
        f=sum((x*a).cos() for a in A)
        rr=F(math.floor(row['R_estimate']*100),100)
        slack=f+(arb(rr.numerator)/arb(rr.denominator))*arb(n).sqrt()
        assert slack<0
        rows.append(dict(name=row['name'],n=n,X=max(A),rational_angle=str(F(q,10**14)),
                         cosine_ball=str(f),R_lower=str(rr),negative_slack_ball=str(slack),
                         status='PROVED ball-arithmetic point certificate M>=R_lower sqrt(n); not an upper bound on M'))
OUT.joinpath('point_certificates.json').write_text(json.dumps(rows,indent=2))
print(json.dumps([dict(name=r['name'],R_lower=r['R_lower']) for r in rows],indent=2))
