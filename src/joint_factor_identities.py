"""Exact symbolic cross-checks of the joint-factor paper identities.

Run only through src/dirun.sh. This checks algebra, not the global
inequality arguments or existence of stable Boolean spectral factors.
The zero-first-moment example is deliberately NOT a Boolean support.
"""
from fractions import Fraction
import json
from pathlib import Path
import platform
import socket


def convolution(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, Fraction(0)) + a * b
    return {i: a for i, a in result.items() if a}


def add(left, right):
    result = dict(left)
    for i, a in right.items():
        result[i] = result.get(i, Fraction(0)) + a
    return {i: a for i, a in result.items() if a}


def reverse(left):
    return {-i: a for i, a in left.items()}


def main():
    host = socket.gethostname()
    if 'dirichlet' not in host:
        raise SystemExit('Use src/dirun.sh')
    import sympy as sp

    z = sp.Symbol('z')
    t, v = sp.symbols('t v', positive=True)
    u = sp.Symbol('u', real=True)
    S, N = sp.symbols('S N', positive=True)
    B = sp.Symbol('B', real=True)
    checks = []

    def check(label, expression):
        assert sp.cancel(expression) == 0, label
        checks.append(label)

    negative_filter = (1 + t*z)/(t + z)
    pair_filter = (1 - 2*u*z + v*z*z)/(z*z - 2*u*z + v)

    def phase_at(filter_, point):
        return sp.cancel(z*sp.diff(filter_, z)/filter_).subs(z, point)

    # This is generic algebra only. A factor of the actual doubled
    # Boolean spectrum has no real roots, so this is not its move.
    check('generic negative-real-root net phase increment, not admissible for doubled Boolean factors',
          phase_at(negative_filter, 1) - phase_at(negative_filter, -1)
          + 4*t/(t*t - 1))
    check('conjugate-pair net phase increment',
          phase_at(pair_filter, 1) - phase_at(pair_filter, -1)
          - 8*u*(v - 1)/((v + 1)**2 - 4*u*u))

    first = -B*(sp.Rational(1, 2) + N/S)
    target = B*B*(1 + 2*N/S)**2/(4*N)
    check('mass-variance intersection first quadratic', first*first/N - target)
    check('mass-variance intersection second quadratic',
          (first+B)**2/N + 2*B*B/S - target)
    check('mass-variance boundary N=S/2',
          target.subs(N, S/2) - 2*B*B/S)
    check('stable mass constant N=S/8',
          target.subs(N, S/8) - 25*B*B/(8*S))

    # An independent sparse rational Laurent calculation, with no SymPy
    # convolution, verifies the generic higher-order phase blindspot.
    E = {2: Fraction(1)}
    O = {0: Fraction(-1), 1: Fraction(3),
         2: Fraction(-3), 3: Fraction(1)}
    cross = add(convolution({i+1: a for i, a in O.items()}, reverse(E)),
                convolution(E, reverse(O)))
    assert not cross
    assert sum(O.values()) == 0
    assert sum(i*a for i, a in O.items()) == 0
    assert O
    checks.append('nonzero zero-sum, zero-first-moment channel with exact cross-phase zero')
    p = add(convolution(E, reverse(E)), convolution(O, reverse(O)))
    base = {0: Fraction(2), 1: Fraction(-1), -1: Fraction(-1)}
    proposed = add({0: Fraction(1)}, convolution(convolution(base, base), base))
    assert p == proposed
    assert p == {0: Fraction(21), 1: Fraction(-15), -1: Fraction(-15),
                 2: Fraction(6), -2: Fraction(6),
                 3: Fraction(-1), -3: Fraction(-1)}
    checks.append('exact generic p=1+(2-w-w^-1)^3, explicitly non-Boolean')

    # A stronger exact WEIGHTED example keeps positive capped Fourier
    # coefficients and actual optimality. No integer set is claimed.
    even = {0: Fraction(1), 1: Fraction(4), 2: Fraction(6),
            3: Fraction(4), 4: Fraction(1)}
    old_q = add({2*i: a for i, a in even.items()},
                {2*i+1: a for i, a in O.items()})
    q = convolution({0: Fraction(1), 18: Fraction(1)}, old_q)
    autocorrelation = convolution(q, reverse(q))
    raw = [82, 68, 14, 2, 1, 7, 34, 41, 90, 41, 34, 7, 1]
    assert autocorrelation[0] == 180
    assert {i: a for i, a in autocorrelation.items() if i > 0} == {
        2*j: Fraction(a) for j, a in enumerate(raw, 1)}
    assert all(Fraction(0) < Fraction(a, 90) <= 1 for a in raw)
    mass = sum(q.values())
    negative = -sum(a for a in q.values() if a < 0)
    centroid = sum(i*a for i, a in q.items())/mass
    negative_variance = -sum(a*(i-centroid)**2 for i, a in q.items() if a < 0)
    positive_variance = sum(a*(i-centroid)**2 for i, a in q.items() if a > 0)
    assert (mass, negative, centroid, negative_variance, positive_variance) == (
        32, 8, 13, 672, 3392)
    assert negative/mass == Fraction(1, 4)
    assert negative_variance/(positive_variance+negative_variance) == Fraction(21, 127)
    assert max(abs(a) for a in q.values())**2/Fraction(180) == Fraction(1, 5)
    assert sum(a for i, a in q.items() if i % 2) == 0
    assert sum(((i-1)//2)*a for i, a in q.items() if i % 2) == 0
    assert sum(i*a for i, a in q.items())/mass == sum(
        i*a*(-1)**i for i, a in q.items())/sum(a*(-1)**i for i, a in q.items())
    checks.append('optimal positive capped WEIGHTED example; first phase jet zero but both signed budgets fail')

    weighted = dict(qualification='WEIGHTED relaxation only; not a set of unit coefficients',
                    cosine_weights={str(j): str(Fraction(a, 90)) for j, a in enumerate(raw, 1)},
                    lambda_exact='1', actual_M_exact='1',
                    global_certificate=('Q2=(1+z^18)*[(1+z^2)^4+z*(z^2-1)^3]/sqrt(180); '
                        '|Q2(z)|^2=1+sum(weights[a]*cos(2*a*x)), z=exp(ix). '
                        'The common factor vanishes at x=pi/18, so the weighted cosine '
                        'polynomial in the undoubled convention attains -1 at pi/9.'),
                    unscaled_q={str(i): str(a) for i, a in sorted(q.items())},
                    qmax_squared='1/5', negative_mass_ratio='1/4', alpha='21/127',
                    phase_imbalance='0', zero_channel_first_moment='0',
                    existence_qualification='No claim that every spectral branch fails; this is a prescribed-factor countermodel')

    w = sp.Symbol('w')
    U = (1+w)**4
    V = (w-1)**3
    K = 1+w**9
    check('weighted example gcd of full polyphase channels', sp.gcd(K*U, K*V)-K)
    check('reduced reciprocal U identity', U.subs(w, 1/w)-w**(-4)*U)
    check('reduced anti-reciprocal V identity', V.subs(w, 1/w)+w**(-3)*V)
    p_weighted = 1+sum(sp.Rational(a, 180)*(w**j+w**(-j))
                       for j, a in enumerate(raw, 1))
    check('full canonical polynomial norm on exact weighted example',
          p_weighted-K*K.subs(w, 1/w)*w**(-4)*(U*U-w*V*V)/180)

    out = dict(status='PASS', host=host, python=platform.python_version(),
               sympy=sp.__version__, checks=checks,
               generic_example=dict(E={'2': '1'},
                   O={str(i): str(a) for i, a in sorted(O.items())},
                   p_laurent_coefficients={str(i): str(a) for i, a in sorted(p.items())},
                   certificate_status='exact generic polynomial identity; not a Boolean A'),
               optimal_weighted_phase_countermodel=weighted,
               qualification=('Exact symbolic identities and sparse rational convolution only. '
                   'The minimax inequalities and polyphase concentration have separate paper proofs. '
                   'No stable-factor selection theorem, universal Chowla bound or Lean check.'))
    destination = Path('.research/experiments/joint_factor_2026-10-23/identities.json')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', checks=len(checks), artifact=str(destination))), flush=True)


if __name__ == '__main__':
    main()
