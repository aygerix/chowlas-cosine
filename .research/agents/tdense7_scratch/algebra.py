"""VM-only algebra and exact rational checks, no optimization package needed."""
import json, math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

OUT=Path('.research/agents/tdense7_scratch')
def maxcubic(t):
    a=(1+t+math.sqrt(1-t+t*t))/3
    return a, a*(1-a)*(a-t)
def reach(r):
    k=2/r
    d=brentq(lambda d:maxcubic(k*d)[1]-k*d**3/12, .2, r/2)
    a,m=maxcubic(k*d)
    return dict(rho=r, density=d,C=1/d,a=a,cubic=m,rhs=k*d**3/12)

def exact_C3():
    # Rationally weaken 2/(3r) to 821/1000 and 1/(162r) to 76/10000.
    r=F(811,1000); t=F(2,3)/r; rhs=F(1,162)/r
    # For a>=t, a(1-a)(a-t) <= (1-t)^2/4 because a<=1.
    q=F(15,16)
    upper1=q*(1-t)**2/4
    upper2=(1-q)*(q-t)
    return dict(t=str(t),rhs=str(rhs),split=str(q),upper1=str(upper1),upper2=str(upper2),
                margin=str(rhs-max(upper1,upper2)),valid=rhs>max(upper1,upper2))

if __name__=='__main__':
    results=dict(reaches=[reach(.811),reach(4/(3*math.sqrt(3))),reach(.687)],exact_C3=exact_C3())
    OUT.joinpath('algebra.json').write_text(json.dumps(results,indent=2))
    print(json.dumps(results,indent=2))
