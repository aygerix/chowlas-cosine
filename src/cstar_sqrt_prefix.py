"""A discriminating exact/ball test of pointwise analytic-root coupling.

The one saved t3 plateau input has a previously certified global upper.
We reuse that certificate and evaluate only coefficients through its fully
occupied prefix, by two different algebraic formulae. No sampled minimum.
"""
import json
from fractions import Fraction
from pathlib import Path
import socket

from flint import arb, ctx


def rational_ball(value):
    value = Fraction(value)
    return arb(value.numerator) / value.denominator


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    ctx.prec = 256
    path = Path('.research/experiments/forced_plateau_2026-10-20/results.json')
    saved = json.loads(path.read_text())
    row = next(r for r in saved['cases'] if r['t'] == 3)
    A, n, b = row['A'], row['n'], row['b']
    assert n == len(set(A)) == 337 and b == 243
    assert set(range(1, b+1)).issubset(A)
    upper = Fraction(row['certificate']['M_upper_rational'])
    assert row['certificate']['verified'] and upper*upper < n
    # Original paper parameter, without the rational rounding of the
    # previous finite-seed test.
    lam = 2*arb(n).sqrt()
    r = 1-1/lam
    assert 0 < r < 1
    # Positive derivative formula:
    # j*v_j = [z^(j-1)] (1-z)^(-3/2) (1-r*z)^(-1/2).
    half = [arb(1)]
    for k in range(1, b):
        half.append(half[-1]*(2*k-1)/(2*k))
    three_halves = [(2*k+1)*half[k] for k in range(b)]
    rpower = [arb(1)]
    for k in range(1, b):
        rpower.append(rpower[-1]*r)
    derivative = [arb(0)]
    for j in range(1, b+1):
        derivative.append(sum((three_halves[j-1-k]*half[k]*rpower[k]
                               for k in range(j)), arb(0))/j)
    # Independent formal square-root equation through the prefix.
    recurrence = [arb(0)]
    for j in range(1, b+1):
        recurrence.append(1-sum((recurrence[u]*recurrence[j-u]
                                for u in range(1, j)), arb(0))/(4*lam))
        assert recurrence[j].overlaps(derivative[j])
        assert derivative[j] > 0
        assert derivative[j] < 2*(lam/j).sqrt()
    vb = derivative[b]
    assert 0 < vb < rational_ball(Fraction(1, 2)), str(vb)
    total = sum(derivative[1:], arb(0))
    assert total < 4*(lam*b).sqrt()
    # This input lies beyond the automatic half-coupling calibration
    # branch n<=46 at the original lambda. Test the AGGREGATE separately.
    full = list(recurrence)
    support = set(A)
    for j in range(b+1, max(A)+1):
        full.append(int(j in support)-sum((full[u]*full[j-u]
                    for u in range(1, j)), arb(0))/(4*lam))
    coupling = sum((full[j] for j in A), arb(0))
    c0 = 1+1/arb(2).sqrt()
    elementary_lower = n/(1+n/(2*lam*c0))
    assert coupling > elementary_lower
    half_holds = bool(coupling > rational_ball(Fraction(n, 2)))
    half_fails = bool(coupling < rational_ball(Fraction(n, 2)))
    assert half_holds or half_fails
    result = dict(status='PASS', host=socket.gethostname(), precision_bits=ctx.prec,
        saved_input=str(path), t=row['t'], A=A, n=n, X=max(A), prefix=b,
        global_M_upper=str(upper), actual_lowM_verified_from_prior_certificate=True,
        global_upper_recomputed=False, lambda_ball=str(lam),
        v_prefix_endpoint_ball=str(vb), v_prefix_endpoint_rational_bracket=['0','1/2'],
        prefix_coupling_ball=str(total), prefix_coupling_upper_ball=str(4*(lam*b).sqrt()),
        all_prefix_coefficients_positive=True, two_formulae_overlap=True,
        aggregate_coupling_ball=str(coupling), aggregate_coupling_over_n_ball=str(coupling/n),
        elementary_aggregate_lower_ball=str(elementary_lower),
        automatic_half_coupling_branch=False, aggregate_half_coupling_holds=half_holds,
        qualification='A pointwise coefficient diagnostic; does not refute aggregate coupling, L25 or Chowla.')
    out = Path('.research/experiments/sqrt_boolean_2026-10-21/prefix.json')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status','n','prefix',
        'v_prefix_endpoint_ball','prefix_coupling_ball','aggregate_coupling_over_n_ball',
        'aggregate_half_coupling_holds','two_formulae_overlap')}), flush=True)


if __name__ == '__main__':
    main()
