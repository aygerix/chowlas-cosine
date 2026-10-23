"""Independent point and all-circle checks for the single saved pilot.

Rebuild the convolution point through set intersections. Certify a
second M upper from the triangular mean, ball noise DFT, and Bernstein.
Also verify the elementary rational constants in the paper theorem.
"""
from fractions import Fraction as R
import json
import math
from pathlib import Path
import socket


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    from cstar_zero_reciprocal import ball,bracket
    root=Path('.research/experiments/modulated_triangle_2026-10-23')
    saved=json.loads((root/'pilot.json').read_text())
    A=saved['A']
    Q,t=saved['Q'],saved['t']
    assert A==sorted(set(A)) and min(A)>0 and max(A)<Q
    assert Q==65536 and t==Q//4 and t in A
    S=set(A)|{-a for a in A}
    # Build actual shifted-set intersections, independently of local coefficients.
    E={s+t for s in S}&{s-t for s in S}
    At=S&{s+t for s in S}
    flint.ctx.prec=192
    x=4*flint.arb.pi()/Q
    z=flint.acb(x.cos(),x.sin())

    def value_of_set(B):
        low,high=min(B),max(B)
        value=flint.acb(0)
        for j in range(high,low-1,-1):
            value=value*z+int(j in B)
        power=z**low if low>=0 else 1/(z**(-low))
        return value*power

    D=value_of_set(S).real
    EV=value_of_set(E)
    AV=value_of_set(At)
    assert abs(EV.imag)<flint.arb('1e-35')
    G=6*D+2*EV.real-8*AV.imag
    lower,upper=map(R,saved['G_point_bracket'])
    assert ball(lower)<G and G<ball(upper)
    assert G<-flint.arb(Q)/100

    # Second all-circle upper: centered real cosine polynomial.
    flint.ctx.prec=96
    grid=16*Q
    occupied=set(A)
    coefficients=[flint.acb(0)]*grid
    for j in range(1,Q):
        pnum=Q if j==t else Q-j
        coefficients[j]=flint.acb(ball(R(Q*int(j in occupied)-pnum,Q)))
    values=flint.acb.dft(coefficients)
    hint=math.ceil(max(abs(float(v.real.mid())) for v in values))+1
    assert all(v.real+hint>0 and hint-v.real>0 for v in values)
    del values,coefficients
    # f_mean=(Fejer_Q-1)/2+cos(tx)/4>=-3/4.
    # ||noise||inf<=gridmax/(1-pi/16)<56*gridmax/45.
    second_M_upper=R(3,4)+R(56*hint,45)
    first_M_upper=R(saved['all_circle_certificate']['M_upper_rational'])
    ratio=G/ball(4*min(first_M_upper,second_M_upper)**2)

    # Rational paper constants; Spencer6sqrt(m) itself is cited, not computed.
    assert R(96)*R(33,8)*R(56,45)<493
    assert 8*60*6*R(33,8)<12000
    assert 493+R(3,2)<500
    assert R(15,1)/(8*R(22,7)**3)>R(3,50)
    assert 2+2*R(88,7)<30
    assert 9+2*(28+5)+8*(28+6)<400
    q0=10**12
    assert R(q0,50)-12000*10**6-400>0
    assert R(q0,3)>400*10**6+R(1,2)
    assert 25*500**2==6250000
    assert R(1,25)/16==R(1,400)

    out=dict(status='PASS',host=socket.gethostname(),Q=Q,n=len(A),
        independent_intersection_point=bracket(G,G),
        saved_point_interval_independently_verified=True,
        second_all_circle_certificate=dict(
            method='Triangular mean plus96-bit Arb noise DFT and Bernstein derivative bound',
            grid=grid,noise_grid_abs_upper=hint,mean_cosine_floor='-3/4',
            Bernstein_multiplier='56/45',M_upper_rational=str(second_M_upper),
            all_circle=True),
        first_M_upper_rational=str(first_M_upper),
        G_over_best_Kupper_squared_ball=str(ratio),
        G_decimal=float(G),M_upper_decimal=float(first_M_upper),
        second_M_upper_decimal=float(second_M_upper),
        paper_rational_constant_checks_pass=True,
        asymptotic_selection_implemented=False,
        qualification=('An independent exact set identity verifies the point. '
            'A different mean/noise Bernstein argument certifies an additional '
            'all-circle upper bound. The pilot is Bernoulli, not the Spencer-selected '
            'asymptotic family; no Chowla counterexample or formalization is claimed.'))
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',artifact=str(root/'verification.json'),
        G=float(G),first_M_upper=float(first_M_upper),
        second_M_upper=float(second_M_upper),ratio_ball=str(ratio))),flush=True)


if __name__=='__main__':
    main()
