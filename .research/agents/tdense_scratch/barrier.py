"""Exact polynomial certificate for fixed-multiplier profile obstruction.
Run on VM through dirun.sh. No numerical optimization.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from math import comb

p = [F((-1)**k*comb(4,k),2) for k in range(5)]
p2 = [sum((p[i]*p[k-i] for i in range(5) if 0<=k-i<5),F(0)) for k in range(9)]
variance = [(p[k] if k<5 else F(0))-p2[k] for k in range(9)]
rows = []
for name,e in [("variance",variance),("square",p2)]:
    E = sum((a/F(k+1) for k,a in enumerate(e)),F(0))
    # S(z)/z = integral_0^1 e(zu)*(1-u)^2 du.
    sz = [a*F(2,(k+1)*(k+2)*(k+3)) for k,a in enumerate(e)]
    D = [F(0)]*(len(sz)+1)
    for k,a in enumerate(sz):
        D[k] += a
        D[k+1] += a
    D[0] -= E
    n = len(D)-1
    bern = [sum((D[k]*F(comb(i,k),comb(n,k)) for k in range(i+1)),F(0))
            for i in range(n+1)]
    assert all(b>=0 for b in bern), bern
    mu1 = sum((a/F(k+2) for k,a in enumerate(e)),F(0))/E
    mu2 = sum((a/F(k+3) for k,a in enumerate(e)),F(0))/E
    assert mu1<=F(1,4)
    rows.append({"name":name,"e_power_coefficients":list(map(str,e)),"E":str(E),
                 "S_div_z_power_coefficients":list(map(str,sz)),
                 "D_power_coefficients":list(map(str,D)),"bernstein_degree":n,
                 "bernstein_coefficients":list(map(str,bern)),
                 "mu1":str(mu1),"mu2":str(mu2)})
result = {"status":"EXACT polynomial certificate PASS", "profiles":rows}
Path(".research/agents/tdense_scratch/barrier.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result),flush=True)
