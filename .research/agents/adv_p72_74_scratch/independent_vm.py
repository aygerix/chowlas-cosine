#!/usr/bin/env python3
"""Independent high-precision checks; run only on dirichlet."""
from fractions import Fraction
from pathlib import Path
import json
import math
import mpmath as mp
import numpy as np

out=Path('.research/agents/adv_p72_74_scratch')
mp.mp.dps=90
best=np.load(out/'p73_best_vm.npz')
weights=[mp.mpf(float(v)) for v in best['weights']]
ks=[int(v) for v in best['ks']]
mask=best['mask']
N=len(mask)
# Arc integration uses actual endpoints with arbitrary precision, independently of FFT.
centers=[mp.mpf(int(j))/N for j in np.flatnonzero(mask)]
def a(k):
    if k==0: return mp.mpf(len(centers))/N
    t=mp.pi*k/N
    return mp.sin(t)/t/N*sum(mp.cos(2*mp.pi*k*x) for x in centers)
mu=mp.mpf(len(centers))/N
gamma=sum(weights)
delta=min(mp.mpf('.499'),(4-3*gamma)/5*mp.mpf('.999'))
E=sum(w*w for w in weights)+mu-2*sum(w*a(k) for w,k in zip(weights,ks))
rhs=delta**2*mu/3
C=mp.sqrt(mp.mpf(3)/56)/(288*mp.pi)
# pi<22/7 plus this rational comparison proves C>1/4000 without floating arithmetic.
left=Fraction(3,56)
right=(Fraction(9,125)*Fraction(22,7))**2
assert left>right
assert Fraction(1,300)>Fraction(1,4000)
# Bernstein/Taylor edge value: (7/6)*(1-2*(3/56))=25/24 exactly.
edge=Fraction(7,6)*(1-2*Fraction(3,56))
assert edge==Fraction(25,24)
answer={'p73_best_independent':{'mu':str(mu),'gamma':str(gamma),'delta':str(delta),
                              'E':str(E),'rhs':str(rhs),'ratio':str(E/rhs)},
        'p74_rational_constant_check':{'left':str(left),'right':str(right),
                                       'strict_difference':str(left-right),'edge':str(edge),
                                       'C':str(C)},
        'p74_semicircle':{'U':str(mp.mpf(1)/4-2/mp.pi**2),
                          'ratio':str(mp.mpf(1)/2-4/mp.pi**2)},
        'source_unchanged':(out/'PROOFS_at_audit_start.md').read_bytes()==Path('.research/PROOFS.md').read_bytes()}
(out/'independent_results_vm.json').write_text(json.dumps(answer,indent=2))
print(json.dumps(answer,indent=2))
