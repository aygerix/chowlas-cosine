"""Numerical localized third-moment diagnostics, VM only.

FFT quadrature has enough samples for cubic exactness algebraically; floating
arithmetic is not certified. Records both moment and window certificates.
"""
import json
import math
from pathlib import Path
import numpy as np

OUT=Path(".research/agents/tdense_scratch")
data=json.load(open(OUT/"probe.json"))
records=[]
for row in data["records"]:
    A=row["A"]
    X=max(A)
    a=np.zeros(X+1)
    a[A]=1
    def av(j):
        return a[abs(j)] if abs(j)<=X else 0
    qs=[1,2,3,4,8,16]
    out=[]
    for q in qs:
        D=X+q
        b=np.r_[0,[av(j)-(av(j-q)+av(j+q))/2 for j in range(1,D+1)]]
        E=float(np.dot(b,b))
        V=E/2
        G=1<<math.ceil(math.log2(4*D+1))
        cf=np.zeros(G)
        cf[:D+1]=b
        vals=np.fft.fft(cf).real
        W=float(np.mean(vals**3))
        B=W/V**1.5
        tau=2/(math.sqrt(B*B+4)+B)
        Mlb=(tau*math.sqrt(V)+av(q)/2)/2
        out.append({"q":q,"V_over_n":V/len(A),"third_over_V_threehalves":B,
                    "third_moment_M_lower_bound":Mlb,
                    "third_moment_R_lower_bound":Mlb/math.sqrt(len(A))})
    records.append({"name":row["name"],"n":len(A),"X":X,"moments":out})
Path(OUT/"third_moment.json").write_text(json.dumps({"status":"NUMERICAL, uncertified",
                                                   "records":records},indent=2))
for row in records:
    best=max(row["moments"],key=lambda z:z["third_moment_R_lower_bound"])
    print(json.dumps({"name":row["name"],"n":row["n"],"best":best}),flush=True)
