"""Exact quadratic-field falsifier of the negative-block P2 closure.

A={1,...,8}; lambda=4sqrt(2) has lambda²=32. Rational field
arithmetic and rational sign tests establish the finite inequality.
An independent Sturm check verifies M<=11/4 on the entire circle.
The complete inverse is checked separately; this is not a P2 claim.
"""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
import json
from pathlib import Path
import socket


@dataclass(frozen=True)
class E:
    a: Q = Q(0)
    b: Q = Q(0)

    @staticmethod
    def of(x):
        return x if isinstance(x,E) else E(Q(x))

    def __add__(self,other):
        other=E.of(other)
        return E(self.a+other.a,self.b+other.b)
    __radd__=__add__

    def __neg__(self):
        return E(-self.a,-self.b)

    def __sub__(self,other):
        return self+-E.of(other)

    def __rsub__(self,other):
        return E.of(other)+-self

    def __mul__(self,other):
        other=E.of(other)
        return E(self.a*other.a+32*self.b*other.b,
                 self.a*other.b+self.b*other.a)
    __rmul__=__mul__

    def inverse(self):
        norm=self.a*self.a-32*self.b*self.b
        assert norm
        return E(self.a/norm,-self.b/norm)

    def __truediv__(self,other):
        return self*E.of(other).inverse()

    def __rtruediv__(self,other):
        return E.of(other)*self.inverse()

    def __pow__(self,n):
        if n<0: return self.inverse()**(-n)
        result,base=E.of(1),self
        while n:
            if n&1: result=result*base
            base=base*base
            n//=2
        return result

    def sign(self):
        # Exact comparison of a+b*sqrt(32), without floating point.
        a,b=self.a,self.b
        if not b: return (a>0)-(a<0)
        if b>0:
            if a>=0: return 1
            difference=32*b*b-a*a
        else:
            if a<=0: return -1
            difference=a*a-32*b*b
        return (difference>0)-(difference<0)


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    from cstar_resolvent_verify import check_upper
    from cstar_zero_reciprocal import one,ball,bracket
    flint.ctx.prec=384
    A=list(range(1,9))
    lam=E(Q(0),Q(1))
    u=1/lam
    r=1-u
    assert lam*lam==E.of(32)
    p=[u]
    for j in range(1,17):
        p.append(-sum((p[j-a] for a in A if a<=j),E())/lam)
    q=[sum((p[j]*p[a-j] for j in range(a+1)),E()) for a in range(9)]
    T=sum((q[a] for a in A),E())
    y=-lam*T
    k=[lam*sum((q[a-j] for a in A if a>=j),E()) for j in range(1,9)]
    sums=Counter(a+b for a in A for b in A)
    t=sum(sums[a] for a in A)
    assert t==28
    C2=sum((count*p[j] for j,count in sums.items()),E())
    Nminus=sum((v*v for v in k),E())

    # Independently proved geometric-series closed forms.
    R=r**8
    assert y==u*(1-r**7*(1-9*u))
    assert C2==u+(1-10*u)*R-r*R*R
    assert all(k[7-s]==u*r**(s-1)*(1-(s+1)*u) for s in range(8))
    closed_N=u*u*sum((r**(2*s-2)*(1-(s+1)*u)**2 for s in range(8)),E())
    assert Nminus==closed_N
    gap=y/2-y*y-Nminus-5*lam*C2*C2/(2*t)
    Psi_minus=2*t*gap/(5*lam)
    assert gap.sign()>0
    v=(1+y)/lam+lam*p[8]
    floor_one=v*v/(1-u*u)
    floor_two=(v*v+p[8]*p[8])/(1-u*u)
    allpass_margin=Nminus+floor_two+5*lam*C2*C2/(2*t)-y/2+y*y
    allpass_S0_margin=Nminus+floor_two-y/2+y*y
    assert allpass_margin.sign()>0 and allpass_S0_margin.sign()>0
    # Independent full-norm formula from the finite reproducing kernel:
    # for a prefix, C=(lambda-1)*(lambda*I+J_8).
    g_exact=8/((lam-1)*(lam+8))
    H_exact=(y/2-g_exact)/lam
    Phi_exact=2*t*H_exact-C2*C2
    positive_exact=5*g_exact-2*y-y*y-Nminus
    assert Phi_exact.sign()<0 and (positive_exact-floor_two).sign()>0

    # These rational bounds independently imply the paper gap >449/62500.
    assert (y-Q(1,5)).sign()>0 and (Q(103,500)-y).sign()>0
    assert (C2+Q(1,25)).sign()>0 and C2.sign()<0
    assert (Q(13,250)-Nminus).sign()>0
    assert (Q(51,100)-5*lam/56).sign()>0
    assert (gap-Q(449,62500)).sign()>0
    sturm_length=check_upper(A,Q(11,4))
    assert Q(11,4)**2<8

    def arb(x):
        return ball(x.a)+ball(x.b)*flint.arb(32).sqrt()

    def record(x):
        return dict(rational_part=str(x.a),sqrt32_part=str(x.b),
                    exact_sign=x.sign(),ball=str(arb(x)))

    exact=one(A,Q(11,4),'P2_prefix8',band_multiple=32)
    Hlo,Hhi=map(Q,exact['H_bracket'])
    phi_lo=2*t*ball(Hlo)-arb(C2)**2
    phi_hi=2*t*ball(Hhi)-arb(C2)**2
    Sp,Se=Q(exact['S_P_exact']),Q(exact['S_error_upper'])
    glo,ghi=32*ball(Sp-Se)-1,32*ball(Sp+Se)-1
    positive_lo=5*glo-2*arb(y)-arb(y)**2-arb(Nminus)
    positive_hi=5*ghi-2*arb(y)-arb(y)**2-arb(Nminus)
    assert glo<arb(g_exact) and arb(g_exact)<ghi
    assert phi_lo<arb(Phi_exact) and arb(Phi_exact)<phi_hi
    out=dict(status='PASS',host=socket.gethostname(),A=A,n=8,D=8,
        field='Q(lambda), lambda positive, lambda²=32',
        all_circle_M_upper='11/4',Sturm_chain_length=sturm_length,
        paper_gap_lower='449/62500',t_exact=t,
        exact_quantities={name:record(v) for name,v in
            [('y',y),('T',T),('C2',C2),('Nminus',Nminus),
             ('negative_block_inequality_deficit',gap),('Psi_minus',Psi_minus)]},
        global_allpass_quantities={name:record(value) for name,value in
            [('p_D',p[8]),('v',v),('one_allpass_floor',floor_one),
             ('complete_cyclic_allpass_floor',floor_two),
             ('allpass_P2_margin',allpass_margin),('allpass_S0_margin',allpass_S0_margin),
             ('exact_g_from_kernel',g_exact),('exact_original_Phi',Phi_exact),
             ('exact_positive_phase_energy',positive_exact)]},
        allpass_recovers_S0_and_P2=True,
        independent_exact_kernel_norm_matches_residual=True,
        closed_forms_match_exact_recurrences=True,
        full_negative_strengthening_refuted=True,
        full_inverse_certificate=exact,
        original_P2_violation_bracket=bracket(phi_lo,phi_hi),
        original_P2_holds=bool(phi_hi<0),original_P2_refuted=bool(phi_lo>0),
        positive_phase_tail_energy_bracket=bracket(positive_lo,positive_hi),
        qualification=('Exact field arithmetic and independent geometric closed forms '
            'refute the stronger negative-block closure on an actual-lowM Boolean set. '
            'The original full determinant is evaluated separately by an infinite '
            'inverse residual certificate. No sampled minimum is used as proof.'))
    dest=Path('.research/experiments/P2_aggregation_2026-10-23/prefix8.json')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',artifact=str(dest),gap_ball=str(arb(gap)),
        Psi_minus_ball=str(arb(Psi_minus)),original_P2_holds=out['original_P2_holds'],
        original_P2_refuted=out['original_P2_refuted'],
        allpass_recovers=True,allpass_S0_margin=str(arb(allpass_S0_margin)),
        original_phi_ball_bounds=out['original_P2_violation_bracket'],
        positive_phase_tail=out['positive_phase_tail_energy_bracket'])),flush=True)


if __name__=='__main__':
    main()
