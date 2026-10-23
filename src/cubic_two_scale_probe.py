"""Certify one practical localized cubic-dual discriminator on Dirichlet.

The normalized half-sine autocorrelation is decreasing; H is increasing.
Monotone endpoint enclosures cover the whole interval, not just samples.
This is a generator test, not an upper bound on the variational supremum.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import socket
import time


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    from cstar_zero_reciprocal import ball, bracket
    flint.ctx.prec = 192
    started = time.monotonic()
    c_upper = Q(962250449, 10**10)
    assert 108*c_upper*c_upper > 1
    c0 = flint.arb(3).sqrt()/18
    cu = ball(c_upper)
    left, right = Q(3, 16), Q(1, 4)
    def w(t):
        t = ball(t)
        angle = flint.arb.pi()*t
        return (1-t)*angle.cos()+angle.sin()/flint.arb.pi()
    def H(s):
        return s*s*(3-2*s*s).sqrt()
    rows = []
    largest = None
    for j in range(64):
        lo = left+(right-left)*Q(j, 64)
        hi = left+(right-left)*Q(j+1, 64)
        # Rational cU makes the exact PD inequality weaker than c0.
        # H(w(2t)) decreases and -H(w(t))^2 increases.
        upper = c0*H(w(2*lo))-2*c0*c0*H(w(hi))**2/cu+cu
        lower = c0*H(w(2*hi))-2*c0*c0*H(w(lo))**2/cu+cu
        assert upper/c0 < -ball(Q(1, 100))
        rows.append(dict(lo=str(lo), hi=str(hi), normalized_R_interval=bracket(lower/c0, upper/c0)))
        if largest is None or upper > largest:
            largest = upper
    assert w(Q(3, 8)) < ball(Q(27, 50))
    assert Q(2, 3)*Q(27, 50)**2 < Q(1, 5)
    assert Q(1, 5)**2*(1-Q(1, 5)) < Q(1, 27)
    result = dict(status='PASS', host=socket.gethostname(), precision_bits=192,
                  elapsed_seconds=time.monotonic()-started, interval=[str(left), str(right)],
                  shape='s(t)=(1-32*abs(t-7/32))_+', shape_area='1/32',
                  rho_range=['0', '1/24'], c_upper=str(c_upper),
                  monotone_endpoint_intervals=rows,
                  uniform_normalized_R_upper='-1/100',
                  child_w_at_3_over8=bracket(w(Q(3, 8)), w(Q(3, 8))),
                  child_caps_inactive=True,
                  parent_tangent_correction_conservative='-(2s/cU)G^2 is convex for v>=b>=b3>1/3',
                  qualification='Covers one explicit generator on an entire interval. '
                  'It proves a strict decrease for that generator, not for the supremum or a new Chowla bound.')
    root = Path('.research/experiments/cubic_two_scale_2026-10-23')
    root.mkdir(parents=True, exist_ok=True)
    (root/'probe.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'monotone_endpoint_intervals'}, indent=2))


if __name__ == '__main__':
    main()
