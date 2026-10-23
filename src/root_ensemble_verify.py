"""Independent complex-linear-root verification of the fixed L8 ensemble.

The producer multiplies real quadratics and uses a covariance product.
This verifier uses conjugate complex linear factors at256 bits and
recomputes every signed budget. All-circle optimality is an exact
cubic identity checked here in Q(sqrt7), not a minimum grid.
"""
from fractions import Fraction as R
from itertools import product
import json
from pathlib import Path
import socket
import time


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    from cstar_zero_reciprocal import ball, bracket
    started = time.monotonic()
    root = Path('.research/experiments/root_ensemble_2026-10-23')
    saved = json.loads((root/'results.json').read_text())
    assert saved['status'] == 'PASS' and saved['A'] == [8, 16, 24]

    # Exact Q(sqrt7) arithmetic for f(v)+lambda=4(v-u)^2(v+c).
    def add(x, y):
        return x[0]+y[0], x[1]+y[1]
    def neg(x):
        return -x[0], -x[1]
    def mul(x, y):
        return x[0]*y[0]+7*x[1]*y[1], x[0]*y[1]+x[1]*y[0]
    def scalar(x, n):
        return x[0]*n, x[1]*n
    def polymul(p, q):
        out = [(R(0), R(0))]*(len(p)+len(q)-1)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                out[i+j] = add(out[i+j], mul(x, y))
        return out
    one = (R(1), R(0))
    uq = (R(-1, 6), R(1, 6))
    cq = (R(1, 6), R(1, 3))
    lambdaq = (R(17, 27), R(7, 27))
    rhs = [scalar(x, 4) for x in polymul(polymul([neg(uq), one], [neg(uq), one]), [cq, one])]
    assert rhs == [add((R(-1), R(0)), lambdaq), (R(-2), R(0)), (R(2), R(0)), (R(4), R(0))]

    flint.ctx.prec = 256
    arb, acb = flint.arb, flint.acb
    u = (arb(7).sqrt()-1)/6
    c = (1+2*arb(7).sqrt())/6
    a = c+(c*c-1).sqrt()
    radius = a.root(8)
    lam = (17+7*arb(7).sqrt())/27
    S = (3+lam).sqrt()
    V = arb(448)/S
    assert c > 1 and -1 < u < 1 and lam*lam < 3
    scale = 1/(2*a).sqrt()

    def cmul(p, q):
        out = [acb(0)]*(len(p)+len(q)-1)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                out[i+j] += x*y
        return out
    def enclosed(value, interval):
        lower, upper = interval
        assert ball(lower) < value < ball(upper)

    values = []
    joint_costs = []
    stable_choices = []
    positive_mass_choices = []
    for choices, row in zip(product((0, 1), repeat=4), saved['branches']):
        assert list(choices) == row['choices']
        q = [acb(1)]
        for j, reverse in enumerate(choices):
            angle = (2*j+1)*arb.pi()/8
            root_phase = acb(angle.cos(), angle.sin())
            if reverse:
                q = cmul(cmul(q, [-root_phase, acb(radius)]), [-root_phase.conjugate(), acb(radius)])
            else:
                q = cmul(cmul(q, [-radius*root_phase, acb(1)]), [-radius*root_phase.conjugate(), acb(1)])
        # Independent direct sparse convolution with the fixed unit-circle part.
        whole = [acb(0)]*25
        for shift, coefficient in ((0, scale), (8, -2*u*scale), (16, scale)):
            for j, x in enumerate(q):
                whole[j+shift] += coefficient*x
        assert all(x.imag.contains(0) and abs(x.imag) < arb('1e-60') for x in whole)
        reals = [x.real for x in whole]
        negative = [(abs(x)-x)/2 for x in reals]
        mass = sum(negative)
        mu = sum(j*x for j, x in enumerate(reals))/S
        variance = sum(n*(j-mu)**2 for j, n in enumerate(negative))
        fourth = sum((x*x)*(x*x) for x in reals)
        cost = 8*mass/S+6*variance/V+fourth
        enclosed(mass/S, row['negative_mass_over_S'])
        enclosed(variance/V, row['negative_variance_over_intrinsic'])
        enclosed(mu, row['centroid'])
        enclosed(fourth, row['coefficient_fourth_sum'])
        enclosed(cost, row['joint_cost_C1_r2'])
        assert all(abs(x) < ball(row['coefficient_max'][1]) for x in reals)
        stable = bool(all(abs(x) < 1 for x in reals) and mass < S/8 and variance < V/6)
        assert stable == row['stable_C1_certified']
        if stable:
            stable_choices.append(list(choices))
        if mass > S/8:
            positive_mass_choices.append(list(choices))
        values.append(mass)
        joint_costs.append(cost)

    mean = sum(values)/16
    assert mean > S/8
    enclosed(mean/S, saved['mean_negative_mass_over_S'])
    assert stable_choices == [[0, 0, 0, 0], [1, 1, 1, 1]]
    coherent_cost = (joint_costs[0]+joint_costs[-1])/2
    assert coherent_cost < 1
    enclosed(coherent_cost, saved['coherent_same_marginal_joint_cost_C1_r2'])
    # Advisor identified this strict bad local minimum from the saved cube.
    # Verify only its exact rational inequalities, without new root inputs.
    cost_intervals = {tuple(row['choices']): row['joint_cost_C1_r2'] for row in saved['branches']}
    local_traps = []
    for vertex in ((0, 1, 1, 0), (1, 0, 0, 1)):
        lower, upper = map(R, cost_intervals[vertex])
        assert lower > 1
        neighbors = []
        for j in range(4):
            neighbor = list(vertex)
            neighbor[j] ^= 1
            neighbor_lower = R(cost_intervals[tuple(neighbor)][0])
            assert upper < neighbor_lower
            neighbors.append(dict(choices=neighbor, cost_lower=str(neighbor_lower)))
        local_traps.append(dict(choices=list(vertex), cost_interval=cost_intervals[vertex],
                                all_one_flip_neighbor_lowers=neighbors))
    # Uniform independence is bad here despite a known stable lift.
    # No claim that every mixed branch fails the mass condition alone.
    result = dict(status='PASS', host=socket.gethostname(), precision_bits=256,
                  elapsed_seconds=time.monotonic()-started,
                  A=[8, 16, 24], complete_branch_count=16,
                  exact_quadratic_field_cubic_identity=True,
                  complex_linear_root_budget_verification=True,
                  mean_negative_mass_over_S=bracket(mean/S, mean/S),
                  mean_negative_mass_minus_S_over8=bracket(mean-S/8, mean-S/8),
                  stable_C1_choices=stable_choices,
                  mass_budget_failing_choices=positive_mass_choices,
                  naive_uniform_mean_mass_bound_refuted=True,
                  coherent_same_marginal_joint_cost_C1_r2=bracket(coherent_cost, coherent_cost),
                  coherent_same_marginal_certificate_passes=True,
                  certified_bad_one_block_local_minima=local_traps,
                  qualification='Independent factor multiplication and higher ball precision; '
                  'both use Arb. This refutes the uniform mean-mass bound, not stable-branch existence.')
    (root/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
