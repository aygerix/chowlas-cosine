"""Numerical continuum probe, not a proof. VM only.

Independent rounding of p(t)=(1-t)^k/2. q/X=s, frequency t.
The formula retains both variance and the finite-difference profile mean.
"""
import json
from pathlib import Path
import numpy as np

def study(k, gridsize=8193):
    best = {"lb2_over_X":0.0}
    ss = np.unique(np.r_[np.geomspace(1e-5,.1,30),np.linspace(.1,2,70)])
    for shift in ss:
        D = 1+shift
        t = np.linspace(0,D,gridsize)
        def p(x):
            return .5*np.maximum(0,1-np.abs(x))**k
        ps = [p(t),p(t-shift),p(t+shift)]
        mean = ps[0]-(ps[1]+ps[2])/2
        energy = mean**2+ps[0]*(1-ps[0])+sum(v*(1-v)/4 for v in ps[1:])
        # Cumulative integrals of t^j e(t) evaluate all Fejer scales cheaply.
        dt = t[1]-t[0]
        cs=[]
        for j in range(3):
            z=energy*t**j
            cs.append(np.r_[0,np.cumsum((z[1:]+z[:-1])*dt/2)])
        E=cs[0][-1]
        ws=np.geomspace(1e-4*D,10*D,500)
        m=np.minimum(ws,D)
        S=sum(f*np.interp(m,t,cs[j])/ws**j for j,f in enumerate([1,-2,1]))
        W=2*ws/3
        C=.811*(D+ws)
        lb2=(W*E-C*S)/(2*(C-W))
        ix=int(np.argmax(lb2))
        if lb2[ix]>best["lb2_over_X"]:
            best={"lb2_over_X":float(lb2[ix]),"shift_over_X":float(shift),
                  "w_over_X":float(ws[ix]),"E_over_X":float(E)}
    return {"k":k,"gridsize":gridsize,"status":"NUMERICAL continuum diagnostic",
            "best":best,"scales_tested":len(ss)*500}

out=[study(k) for k in [2,4,8]]
Path(".research/agents/tdense_scratch/growing_shift.json").write_text(json.dumps(out,indent=2))
print(json.dumps(out),flush=True)
