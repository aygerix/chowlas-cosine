"""Independent integer check of the forced-plateau energy pivot on Dirichlet.

The notch polynomial only interpolates the forced prefix. It is not a
certificate for the whole selected Boolean set.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import socket
import numpy as np


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    out=dict(qualification='Exact prefix/profile energy identities, not full-support certificates.',cases=[])
    for t in [2,3,4,5]:
        L,b=t**6,t**5
        v=np.array([j*(L-j) for j in range(L+1)],dtype=np.int64)
        c=np.array([0 if s==0 else (1 if abs(s)<=b else -1)
                    for s in range(-2*b,2*b+1)],dtype=np.int64)
        assert sum(map(int,c))==0
        assert sum(s*int(z) for s,z in zip(range(-2*b,2*b+1),c))==0
        assert sum(int(z)**2 for z in c)==4*b
        assert int(max(v))*sum(abs(int(z)) for z in c)<2**63
        product=np.convolve(v,c)
        numerator=sum(int(z)**2 for z in product)
        E=sum(int(z)**2 for z in v)
        assert E==(L**5-L)//30
        weighted=F(numerator,E)
        squared=np.convolve(c,c)
        quartic=sum(int(z)**2 for z in squared)
        assert quartic* (b+1)>=b**4
        if t>=4:
            assert weighted<=100000*F(b**5,L**3)
        row=dict(t=t,L=L,b=b,Q_exact=4*b,
                 weighted_energy_exact=str(weighted),
                 signed_profile_energy_exact=str(weighted-4*b),
                 fourth_power_exact=quartic,
                 weighted_energy_over_L3half_float=float(weighted)/(L**1.5),
                 fourth_power_over_L2_float=quartic/L**2,
                 verified=True)
        out['cases'].append(row)
        print(json.dumps(row),flush=True)
    path=Path('.research/experiments/forced_plateau_2026-10-20/energy.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
