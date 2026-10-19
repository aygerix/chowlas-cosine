"""Exact integer triple-count audit of the localized-moment certificates.
Only execute through src/dirun.sh -c 2. Uses VM python-flint.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from flint import nmod_poly

OUT=Path(".research/agents/tdense_scratch")
sets=json.load(open(OUT/"probe.json"))["records"]
floating={r["name"]:r for r in json.load(open(OUT/"third_moment.json"))["records"]}
records=[]
prime=998244353
for row in sets:
    A=row["A"]
    n=len(A)
    X=max(A)
    assert 4*n*n<prime
    coeff=[0]*(2*X+1)
    for a in A:
        coeff[X+a]=coeff[X-a]=1
    poly=nmod_poly(coeff,prime)
    cube=poly*poly*poly
    aset=set(A)
    def av(j):
        return int(abs(j) in aset)
    moments=[]
    for f in floating[row["name"]]["moments"]:
        q=f["q"]
        C=[int(cube[3*X+k*q]) if 3*X+k*q<len(cube) else 0 for k in range(4)]
        V=F(sum((2*av(j)-av(j-q)-av(j+q))**2 for j in range(1,X+q+1)),8)
        Delta=10*C[0]-15*C[1]+6*C[2]-C[3]
        W=F(Delta,32)+F(3*av(q),2)*V+F(av(q),8)
        assert abs(float(W/V**F(3,2))-f["third_over_V_threehalves"])<1e-7
        assert abs(float(V/n)-f["V_over_n"])<1e-12
        criteria=(V>=F(n,10) and (W<=0 or W*W<=4*V**3))
        moments.append({"q":q,"V":str(V),"W":str(W),"c_0_q_2q_3q":C,
                        "sixth_difference_numerator":Delta,
                        "V_ge_n_over_10_and_W_le_2V_threehalves":criteria})
    assert any(m["V_ge_n_over_10_and_W_le_2V_threehalves"] for m in moments)
    records.append({"name":row["name"],"n":n,"X":X,"moments":moments})
result={"status":"EXACT finite moment criteria PASS, not the universal missing lemma",
        "modulus":prime,"why_no_wrap":"Every triple count <= (2n)^2 < modulus",
        "records":records}
(OUT/"third_moment_exact.json").write_text(json.dumps(result,indent=2))
print(json.dumps({"status":result["status"],"sets_checked":len(records),
                  "all_have_q_le_16_with_V_ge_n_over_10_and_W_le_2V_threehalves":True}),flush=True)
