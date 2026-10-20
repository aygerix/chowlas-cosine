"""Exact deterministic full/empty-center countercontrol and point checks."""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import flint
import numpy as np
from scipy.special import jn_zeros
from cstar_fiber_centers import geometry,encoding,residues_for_phase,matrices_for_choices,point_certificate,crt


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=160;tau=2*float(jn_zeros(1,1)[0])
    root=Path('.research/experiments/fiber_centers_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    classes={(1,0),(4,0),(0,1),(0,4),(1,1),(4,4)}
    out=dict(qualification='Deterministic correlated countercontrol; finite zero-circle samples '
             'are not a uniform finite-X certificate. Separate t=5 negative point is rigorous.',cases=[])
    upper=sum((F((-1)**k,math.factorial(k)*math.factorial(k+1))*F(25,4)**k for k in range(21)),F(0))
    assert upper<F(-1,8);out['disk_at_5_upper_rational']=str(upper)
    for X in [64,128,256]:
        fibers=geometry(X);h,P,C=encoding(X);choices=[]
        for fiber in fibers:
            B=fiber['B'];u=fiber['u']
            if (u[0]%5,u[1]%5) in classes:
                i=int(np.where((B==[0,0]).all(axis=1))[0][0])
                assert fiber['incidence'][i].all()
            else:
                i=len(B)-1;assert not fiber['incidence'][i].any()
            choices.append(i)
        matrices=matrices_for_choices(fibers,choices);n=len(matrices)
        negative=point_certificate(matrices,h,C,residues_for_phase([5/X,0,0,5/X],h))
        assert F(negative['M_lower_rational'])>F(n,16)
        values=[];targets=[]
        for j in range(8):
            c=math.cos(math.pi*j/8);s=math.sin(math.pi*j/8)
            residues=residues_for_phase(np.array([c,-s,s,c])*tau/X,h)
            point=crt(residues,h)
            value=sum((flint.arb.cos_pi_fmpq(flint.fmpq(2*(point*sum(a*b for a,b in zip(C,M))%P),P))
                       for M in matrices),flint.arb(0))/n
            values.append(value);targets.append(residues)
        lower=F(math.floor(min(float(v.mid()) for v in values)*10**8)-1,10**8)
        assert all(v>flint.arb(lower.numerator)/lower.denominator for v in values)
        row=dict(X=X,n=n,choices=choices,zero_circle_targets=targets,
                 grid_f_over_n_lower_rational=str(lower),zero_grid_balls=list(map(str,values)),
                 t5_point=negative,verified=True)
        out['cases'].append(row)
        print(json.dumps(dict(X=X,n=n,zero_grid_lower=str(lower),t5_R_lower=negative['R_lower_float'])),flush=True)
    (root/'countercontrol.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
