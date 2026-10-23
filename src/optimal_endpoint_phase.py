"""Exact signed-geometry check on the already certified n5 reflection.

No new root search or support sweep. The saved rational box and cubic
root bracket enclose the exact factor. Reflection preserves its circle
modulus; this checks the signed-centroid sufficient conditions.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import socket

from rational_box import I


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    base=Path('.research/experiments/optimal_endpoint_2026-10-23')
    saved=json.loads((base/'n5.json').read_text())
    center=list(map(F,saved['center']))
    radius=F(saved['radius'])
    a,b,d,e,c=[I(value-radius,value+radius) for value in center]
    t=I(*saved['negative_real_root_magnitude'])
    assert (a-b*t.lo+d*t.lo*t.lo-e*t.lo*t.lo*t.lo).lo>0
    assert (a-b*t.hi+d*t.hi*t.hi-e*t.hi*t.hi*t.hi).hi<0
    assert t.lo>1 and (a/(e*t)).lo>1
    residual=[a/t,d-e*t+a,e+t*(d-e*t),e*t]
    q=[I(0) for _ in range(6)]
    for i,left in enumerate([I(1),-2*c,I(1)]):
        for j,right in enumerate(residual):
            q[i+j]=q[i+j]+left*right
    assert q[2].hi<0
    assert all(value.lo>0 for j,value in enumerate(q) if j!=2)
    assert all(value.magnitude()<1 for value in q)
    S=sum(q,I(0))
    assert S.lo>0
    minus=-q[2]
    centroid=sum((j*value for j,value in enumerate(q)),I(0))/S
    Vplus=sum((value*(I(j)-centroid)**2 for j,value in enumerate(q) if j!=2),I(0))
    Vminus=minus*(I(2)-centroid)**2
    Vabs=Vplus+Vminus
    assert Vabs.lo>0
    alpha=Vminus/Vabs
    negative_mass_ratio=minus/S
    assert alpha.hi<F(1,8) and negative_mass_ratio.hi<F(1,8)
    intrinsic=I(F(55,2))/S
    assert Vminus.hi<intrinsic.lo/6
    out=dict(status='PASS',host=socket.gethostname(),A=[1,2,3,4,5],
        base_certificate='n5.json; independently verified by n5_verification.json',
        signed_factor_intervals=[value.serial() for value in q],
        S_interval=S.serial(),negative_mass_interval=minus.serial(),
        negative_mass_ratio_interval=negative_mass_ratio.serial(),
        signed_centroid_interval=centroid.serial(),
        negative_variance_interval=Vminus.serial(),
        absolute_variance_interval=Vabs.serial(),
        alpha_interval=alpha.serial(),intrinsic_signed_variance_interval=intrinsic.serial(),
        qmax_upper=str(max(value.magnitude() for value in q)),
        stable_conditions=dict(qmax_below_one=True,negative_mass_ratio_below_one_eighth=True,
                               alpha_below_one_eighth=True),
        qualification='One exact signed-branch recovery; no universal branch-selection theorem or improved finite minimum')
    (base/'phase_recovery.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',qmax_upper_display=float(F(out['qmax_upper'])),
                         negative_mass_ratio_upper=float(negative_mass_ratio.hi),
                         alpha_upper=float(alpha.hi))),flush=True)


if __name__=='__main__':
    main()
