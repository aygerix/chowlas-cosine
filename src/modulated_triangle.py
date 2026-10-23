"""One certified finite probe of quadratic modulated-convolution loss.

The asymptotic proof uses eight conditional Spencer rounding stages.
This fixed-seed Bernoulli probe is a separate finite mechanism check.
All research calculation runs on Dirichlet; no minimum grid is a proof.
"""
from collections import defaultdict
from fractions import Fraction as R
import hashlib
import json
import math
from pathlib import Path
import platform
import socket
import time


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    import numpy as np
    from cstar_zero_reciprocal import ball,bracket
    started=time.monotonic()
    Q=65536
    t=Q//4
    seed=20261023
    rng=np.random.default_rng(seed)
    occupied=np.zeros(Q,dtype=np.int8)
    occupied[1:]=(rng.random(Q-1)<1-np.arange(1,Q)/Q).astype(np.int8)
    occupied[t]=1
    A=np.flatnonzero(occupied).tolist()
    S=set(A)|{-a for a in A}
    assert len(S)==2*len(A) and 0 not in S and t in S and -t in S
    degree=Q+t-1

    def a(s):
        s=abs(s)
        return int(occupied[s]) if s<Q else 0

    numerators=[0]+[Q-j for j in range(1,Q)]
    numerators[t]=Q
    def pn(s):
        s=abs(s)
        return numerators[s] if s<Q else 0
    def pair(i,j):
        i,j=abs(i),abs(j)
        if i==j: return pn(i)*Q
        return pn(i)*pn(j)

    real=[0]*(degree+1)
    imag=[0]*(degree+1)
    mean_real=[0]*(degree+1)
    mean_imag=[0]*(degree+1)
    for s in range(degree+1):
        base,plus,minus=a(s),a(s+t),a(s-t)
        # h_-t coefficients are 2*a_s-i*(a_(s+t)-a_(s-t)).
        real[s]=4*base-(plus-minus)**2
        imag[s]=-4*base*(plus-minus)
        mean_real[s]=4*pn(s)*Q-pn(s+t)*Q-pn(s-t)*Q+2*pair(s+t,s-t)
        mean_imag[s]=-4*(pair(s,s+t)-pair(s,s-t))
    assert real[0]==imag[0]==mean_real[0]==mean_imag[0]==0

    # Independent set-intersection identity, including the zero in E_t.
    E={s+t for s in S if s+2*t in S}
    At={s for s in S if s-t in S}
    for s in range(degree+1):
        rr=4*int(s in S)-int(s-t in S)-int(s+t in S)+2*int(s in E)
        ii=4*(int(s in At)-int(-s in At))
        assert real[s]==rr and imag[s]==ii

    # Every quadratic interaction lies in a block of size at most eight.
    blocks=defaultdict(list)
    def component(j):
        return min(j%t,(-j)%t)
    for j in range(1,Q): blocks[component(j)].append(j)
    assert max(map(len,blocks.values()))<=8
    for s in range(-degree,degree+1):
        js=[abs(j) for j in (s,s+t,s-t) if 0<abs(j)<Q]
        assert len({component(j) for j in js})<=1

    flint.ctx.prec=192
    theta=4*flint.arb.pi()/Q
    z=flint.acb(theta.cos(),theta.sin())
    def horner(rr,ii):
        value=flint.acb(0)
        for j in range(len(rr)-1,0,-1):
            value=value*z+flint.acb(rr[j],ii[j])
        return value*z
    point=2*horner(real,imag).real
    expectation=2*horner(mean_real,mean_imag).real/(Q*Q)
    theoretical_constant=(flint.arb.pi()+12)/(8*flint.arb.pi()**3)
    assert abs(expectation+Q*theoretical_constant)<350

    # Independent ball DFT evaluation, after exact frequency folding.
    control=flint.acb.dft([flint.acb(0),flint.acb(1)]+[flint.acb(0)]*6)
    assert control[1].imag<0
    folded_real=[0]*Q
    folded_imag=[0]*Q
    for s in range(1,degree+1):
        folded_real[s%Q]+=real[s]
        folded_imag[s%Q]+=imag[s]
        folded_real[(-s)%Q]+=real[s]
        folded_imag[(-s)%Q]-=imag[s]
    vals=flint.acb.dft([flint.acb(r,i) for r,i in zip(folded_real,folded_imag)])
    independent_point=vals[Q-2].real
    assert abs(independent_point-point)<flint.arb('1e-35')
    del vals
    point_bracket=bracket(point,point)

    # ALL-circle upper M: ball DFT plus nearest-minimizer Taylor error.
    flint.ctx.prec=96
    grid=16*Q
    coeff=[flint.acb(0)]*grid
    for j in A: coeff[j]=flint.acb(1)
    values=flint.acb.dft(coeff)
    hint=math.ceil(max(-float(v.real.mid()) for v in values))+1
    assert all(v.real+hint>0 for v in values)
    del values,coeff
    remainder=R(242*sum(j*j for j in A),49*grid*grid)
    M_upper=R(hint)+remainder
    K_upper=2*M_upper
    certificate=dict(method='96-bit Arb DFT plus all-circle second derivative remainder',
        grid=grid,grid_M_upper_integer=hint,Taylor_remainder=str(remainder),
        M_upper_rational=str(M_upper),K_upper_rational=str(K_upper),all_circle=True)

    out=dict(status='PASS',host=socket.gethostname(),python=platform.python_version(),
        numpy=np.__version__,flint=flint.__version__,elapsed_seconds=time.monotonic()-started,
        Q=Q,t=t,modulation_frequency=-t,angle_exact='4*pi/Q',seed=seed,
        A=A,n=len(A),max_A=max(A),distinct_positive=True,
        support_sha256=hashlib.sha256(json.dumps(A,separators=(',',':')).encode()).hexdigest(),
        generator='Independent X_a with probability1-a/Q, then force X_(Q/4)=1',
        convolution='h*h at4*pi/Q, h=2*(1+sin(-t*x))*D_A, probability Haar',
        G_point_bracket=point_bracket,expected_G_ball=str(expectation),
        asymptotic_mean_constant_ball=str(theoretical_constant),
        independent_integer_identity_verified=True,independent_ball_DFT_verified=True,
        interaction_blocks=len(blocks),maximum_block_size=max(map(len,blocks.values())),
        all_circle_certificate=certificate,
        negative_linear_Q_point_certified=bool(point<-flint.arb(Q)/100),
        negative16K_refutation_certified=bool(point+16*ball(K_upper)<0),
        finite_G_over_Kupper_squared_ball=str(point/ball(K_upper*K_upper)),
        proof_qualification=('This fixed Bernoulli example is not the existential '
            'eight-stage Spencer construction. Its own convolution point and all-circle '
            'M upper are certified independently. No Chowla counterexample is claimed.'))
    dest=Path('.research/experiments/modulated_triangle_2026-10-23/pilot.json')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',artifact=str(dest),Q=Q,n=len(A),
        G_point=point_bracket,expected_G=str(expectation),
        M_upper=str(M_upper),negative_linear_Q=out['negative_linear_Q_point_certified'],
        negative16K_refutation_certified=out['negative16K_refutation_certified'],
        seconds=out['elapsed_seconds'])),flush=True)


if __name__=='__main__':
    main()
