"""One primitive adversary A={1,7,8}, actual M=3/2, exactly8 branches.

Propose degree6 roots numerically, then certify six disjoint one-root
disks by explicit Rouche inequalities. All budgets use256-bit Arb and
are recomputed through complex linear factors. No minimum sampling.
"""
from fractions import Fraction as R
from itertools import product
import json
import math
from pathlib import Path
import socket
import time


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    import sympy as sp
    from cstar_zero_reciprocal import ball, bracket
    started = time.monotonic()
    flint.ctx.prec = 256
    arb, acb = flint.arb, flint.acb
    z = sp.Symbol('z')
    F = 1+z+z**8
    H = 1-z**2+z**3-z**5+z**6
    assert sp.expand(H*(1+z+z**2)-F) == 0
    assert sp.gcd(F, sp.diff(F, z)) == 1
    assert sp.gcd(F, z**8+z**7+1) == z**2+z+1
    coefficients = [1, 0, -1, 1, 0, -1, 1]
    proposals = sp.nroots(H, n=90, maxsteps=200)
    radius = ball(R(1, 10**40))
    disks = []
    centers = []
    evidence = []
    for proposed in proposals:
        real = R(str(sp.re(proposed).evalf(65)))
        imag = R(str(sp.im(proposed).evalf(65)))
        center = acb(ball(real), ball(imag))
        taylor = [sum(coefficients[j]*math.comb(j, k)*center**(j-k)
                      for j in range(k, 7)) for k in range(7)]
        remainder = abs(taylor[0])+sum(abs(taylor[k])*radius**k for k in range(2, 7))
        linear = abs(taylor[1])*radius
        assert remainder < linear
        # Each true root is in its certified disk; this rectangle encloses it.
        disk = acb(arb(ball(real), radius), arb(ball(imag), radius))
        assert abs(disk) < 1 or abs(disk) > 1
        assert disk.imag > 0 or disk.imag < 0
        assert all(abs(center-other) > 2*radius for other in centers)
        disks.append(disk)
        centers.append(center)
        evidence.append(dict(center_real=str(real), center_imag=str(imag), radius='1/10^40',
                             rouche_remainder_over_linear=bracket(remainder/linear, remainder/linear)))
    assert len(disks) == 6
    upper = [disk for disk in disks if disk.imag > 0]
    assert len(upper) == 3
    # The true polynomial is real: conjugation pairs the six certified roots.
    for disk in upper:
        assert any(abs(disk.conjugate()-other) < 4*radius for other in disks if other.imag < 0)

    S = arb(3)/arb(2).sqrt()
    lam = arb(3)/2
    V = arb(57)/S
    scale = 1/arb(2).sqrt()
    fixed = [scale]*3
    blocks = [[(root*root.conjugate()).real, -2*root.real, arb(1)] for root in upper]
    def mul(p, q, zero):
        out = [zero]*(len(p)+len(q)-1)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                out[i+j] += x*y
        return out
    def near_zero(value):
        assert value.contains(0) and abs(value) < arb('1e-30')
    rows = []
    masses = []
    variances = []
    costs = []
    for choices in product((0, 1), repeat=3):
        q = fixed
        linear_q = [acb(1)]
        for choice, block, root in zip(choices, blocks, upper):
            q = mul(q, block[::-1] if choice else block, arb(0))
            if choice:
                linear_q = mul(linear_q, [acb(1), -root], acb(0))
                linear_q = mul(linear_q, [acb(1), -root.conjugate()], acb(0))
            else:
                linear_q = mul(linear_q, [-root, acb(1)], acb(0))
                linear_q = mul(linear_q, [-root.conjugate(), acb(1)], acb(0))
        linear_q = mul(linear_q, list(map(acb, fixed)), acb(0))
        for x, y in zip(q, linear_q):
            near_zero(x-y.real)
            near_zero(y.imag)
        near_zero(sum(q)-S)
        for lag in range(9):
            corr = sum(q[j]*q[j+lag] for j in range(9-lag))
            target = lam if lag == 0 else arb(1)/2 if lag in (1, 7, 8) else arb(0)
            near_zero(corr-target)
        negative = [(abs(x)-x)/2 for x in q]
        negative2 = [(abs(x.real)-x.real)/2 for x in linear_q]
        mass = sum(negative)
        independent_mass = sum(negative2)
        near_zero(mass-independent_mass)
        mu = sum(j*x for j, x in enumerate(q))/S
        variance = sum(n*(j-mu)**2 for j, n in enumerate(negative))
        independent_mu = sum(j*x.real for j, x in enumerate(linear_q))/S
        independent_variance = sum(n*(j-independent_mu)**2 for j, n in enumerate(negative2))
        near_zero(mu-independent_mu)
        near_zero(variance-independent_variance)
        fourth = sum((x*x)*(x*x) for x in q)
        cost = 8*mass/S+6*variance/V+fourth
        stable = bool(all(abs(x) < 1 for x in q) and mass < S/8 and variance < V/6)
        rows.append(dict(choices=list(choices), negative_mass_over_S=bracket(mass/S, mass/S),
                         negative_variance_over_intrinsic=bracket(variance/V, variance/V),
                         joint_cost_C1_r2=bracket(cost, cost), stable_C1_certified=stable))
        masses.append(mass)
        variances.append(variance)
        costs.append(cost)
    mean = sum(masses)/8
    mean_variance = sum(variances)/8
    mean_mass_variance_cost = 8*mean/S+6*mean_variance/V
    assert ball(R(1221, 10000)) < mean/S < ball(R(1223, 10000))
    assert ball(R(646, 10000)) < mean_variance/V < ball(R(647, 10000))
    assert mean_mass_variance_cost > ball(R(27, 20))
    verdict = 'REFUTED' if mean > S/8 else 'PASSES_THIS_CASE_ONLY' if mean < S/8 else 'UNDECIDED'
    assert verdict != 'UNDECIDED'
    result = dict(status='PASS', host=socket.gethostname(), precision_bits=256,
                  elapsed_seconds=time.monotonic()-started, A=[1, 7, 8], gcd=1,
                  actual_M='3/2', all_circle_proof='f=(|1+z+z^8|^2-3)/2, equality at primitive cube roots',
                  residual_coefficients=coefficients, certified_disjoint_root_disks=evidence,
                  complete_real_branch_count=8, branches=rows,
                  real_quadratic_and_complex_linear_budget_checks_agree=True,
                  primitive_uniform_mean_mass_verdict=verdict,
                  mean_negative_mass_over_S=bracket(mean/S, mean/S),
                  mean_negative_mass_minus_S_over8=bracket(mean-S/8, mean-S/8),
                  mean_negative_variance_over_intrinsic=bracket(mean_variance/V, mean_variance/V),
                  mean_mass_variance_cost=bracket(mean_mass_variance_cost, mean_mass_variance_cost),
                  uniform_joint_mean_certificate_refuted=bool(mean_mass_variance_cost > 1),
                  stable_C1_branch_count=sum(row['stable_C1_certified'] for row in rows),
                  base_reverse_joint_cost_C1_r2=bracket((costs[0]+costs[-1])/2, (costs[0]+costs[-1])/2),
                  qualification='One predeclared primitive support, no search or size sweep. '
                  'Numerical proposals are certified by explicit Rouche tests. '
                  'All-circle actual M is exact on paper. No universal selection theorem follows.')
    destination = Path('.research/experiments/root_ensemble_2026-10-23')
    destination.mkdir(parents=True, exist_ok=True)
    (destination/'primitive.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('branches', 'certified_disjoint_root_disks')}, indent=2))


if __name__ == '__main__':
    main()
