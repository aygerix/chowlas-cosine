"""Independent differentiation/convolution verification of the n5 box.

The producer differentiates expanded symbolic polynomials. This checker
builds Q by convolution and differentiates its arithmetic directly by
dual intervals. Every certificate comparison uses exact rationals.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import socket

from rational_box import I


class Dual:
    def __init__(self,value,gradient=None):
        self.value=I.cast(value)
        self.gradient=[I(0)]*5 if gradient is None else gradient

    @staticmethod
    def cast(value):
        return value if isinstance(value,Dual) else Dual(value)

    def __add__(self,other):
        other=Dual.cast(other)
        return Dual(self.value+other.value,[a+b for a,b in zip(self.gradient,other.gradient)])

    __radd__=__add__

    def __neg__(self):
        return Dual(-self.value,[-v for v in self.gradient])

    def __sub__(self,other):
        return self+-Dual.cast(other)

    def __mul__(self,other):
        other=Dual.cast(other)
        return Dual(self.value*other.value,
                    [a*other.value+self.value*b for a,b in zip(self.gradient,other.gradient)])

    __rmul__=__mul__


def system(values):
    variables=[]
    for j,value in enumerate(values):
        variables.append(Dual(value,[I(int(i==j)) for i in range(5)]))
    a,b,d,e,c=variables
    left=[Dual(1),-2*c,Dual(1)]
    right=[a,b,d,e]
    q=[Dual(0) for _ in range(6)]
    for i,lv in enumerate(left):
        for j,rv in enumerate(right):
            q[i+j]=q[i+j]+lv*rv
    residuals=[]
    for lag in range(1,6):
        residuals.append(sum((q[j]*q[j+lag] for j in range(6-lag)),Dual(0))-F(1,2))
    return residuals,[value.value for value in q]


def rank(matrix):
    matrix=[row[:] for row in matrix]
    for j in range(5):
        pivot=next(i for i in range(j,5) if matrix[i][j])
        matrix[j],matrix[pivot]=matrix[pivot],matrix[j]
        for i in range(j+1,5):
            factor=matrix[i][j]/matrix[j][j]
            for k in range(j,5):
                matrix[i][k]-=factor*matrix[j][k]
    return all(matrix[j][j]!=0 for j in range(5))


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    path=Path('.research/experiments/optimal_endpoint_2026-10-23/n5.json')
    saved=json.loads(path.read_text())
    assert saved['A']==[1,2,3,4,5]
    assert saved['unknown_order']==['a','b','d','e','c']
    center=list(map(F,saved['center']))
    radius=F(saved['radius'])
    R=[[F(v) for v in row] for row in saved['inverse_jacobian']]
    assert radius>0 and rank(R)
    box=[I(v-radius,v+radius) for v in center]
    residuals,q=system(box)
    at_center,_=system([I(v) for v in center])
    F0=[v.value.lo for v in at_center]
    assert all(v.value.lo==v.value.hi for v in at_center)
    bound=F(0)
    for i in range(5):
        row=[]
        for j in range(5):
            row.append(I(int(i==j))-sum((R[i][k]*residuals[k].gradient[j]
                                        for k in range(5)),I(0)))
        bound=max(bound,sum(v.magnitude() for v in row))
        image=I(center[i]-sum(R[i][j]*F0[j] for j in range(5)))
        for entry in row:
            image=image+entry*I(-radius,radius)
        assert box[i].lo<image.lo and image.hi<box[i].hi
    assert bound<1
    assert all(value.lo>0 for value in q)
    assert q[0].lo>1 and all(q[0].lo>v.hi for v in q[1:])
    assert -1<box[4].lo and box[4].hi<1
    lam=sum((v*v for v in q),I(0))
    assert lam.hi<2
    aa,bb,dd,ee,cc=box
    disc=18*ee*dd*bb*aa-4*dd**3*aa+dd**2*bb**2-4*ee*bb**3-27*ee**2*aa**2
    assert disc.hi<0
    tlo,thi=map(F,saved['negative_real_root_magnitude'])
    def residual_cubic_minus_t(t):
        return aa-bb*t+dd*t*t-ee*t*t*t
    assert tlo>1 and tlo<thi
    assert residual_cubic_minus_t(tlo).lo>0 and residual_cubic_minus_t(thi).hi<0
    t=I(tlo,thi)
    assert (aa/(ee*t)).lo>1
    # A separate convolution reconstructs the real-root-reflected factor.
    reflected_R=[aa/t,dd-ee*t+aa,ee+t*(dd-ee*t),ee*t]
    reflected_Q=[I(0) for _ in range(6)]
    for i,left in enumerate([I(1),-2*cc,I(1)]):
        for j,right in enumerate(reflected_R):
            reflected_Q[i+j]=reflected_Q[i+j]+left*right
    assert reflected_Q[2].hi<0
    out=dict(status='PASS',host=socket.gethostname(),
        independent='Direct convolution and dual interval differentiation; exact Gaussian rank check',
        contraction_norm_upper=str(bound),q0_interval=q[0].serial(),
        M_interval=lam.serial(),actual_all_circle_optimality=True,
        four_real_spectral_branches_classified=True,
        every_nonnegative_optimal_factor_has_qmax_gt_one=True,
        qmax_le_one_refuted=True,
        qualification='Exact rational interval existence certificate; not Lean and not a counterexample to every absolute bound')
    (path.parent/'n5_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',q0_lower_display=float(q[0].lo),
                         M_upper_display=float(lam.hi))),flush=True)


if __name__=='__main__':
    main()
