"""One predeclared real-root-reflection ensemble, with rigorous Arb bounds.

A={8,16,24}; exact optimal floor follows from the cubic identity in the
research note. Four reciprocal quadratic choices give all16 real factors.
Test the uniform negative-mass budget, and compare its covariance kernel
with explicit branch averaging. This is not a support search.
"""
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
    flint.ctx.prec = 192
    arb = flint.arb
    u = (arb(7).sqrt()-1)/6
    c = arb(1)/2+2*u
    a = c+(c*c-1).sqrt()
    lam = (17+7*arb(7).sqrt())/27
    S = (lam+3).sqrt()
    L = 8
    radius = a.root(L)
    scale = 1/(2*a).sqrt()
    unit = [arb(0)]*17
    unit[0] = unit[16] = scale
    unit[8] = -2*u*scale
    blocks = [[radius*radius, -2*radius*((2*j+1)*arb.pi()/8).cos(), arb(1)]
              for j in range(4)]
    assert u > 0 and c > 1 and a > 1 and lam*lam < 3

    def mul(p, q):
        out = [arb(0)]*(len(p)+len(q)-1)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                out[i+j] += x*y
        return out

    def bounds(value):
        return bracket(value, value)

    zero = arb('1e-45')
    def check_zero(value):
        assert value.contains(0) and abs(value) < zero

    branches = []
    rows = []
    V = arb(7*L*L)/S
    for choices in product((0, 1), repeat=4):
        q = unit
        for reverse, block in zip(choices, blocks):
            q = mul(q, block[::-1] if reverse else block)
        check_zero(sum(q)-S)
        for lag in range(25):
            corr = sum(q[j]*q[j+lag] for j in range(25-lag))
            target = lam if lag == 0 else arb(1)/2 if lag in (8, 16, 24) else arb(0)
            check_zero(corr-target)
        negative = [(abs(x)-x)/2 for x in q]
        Nminus = sum(negative)
        mu = sum(j*x for j, x in enumerate(q))/S
        Vminus = sum(n*(j-mu)**2 for j, n in enumerate(negative))
        fourth = sum((x*x)*(x*x) for x in q)
        joint_cost = 8*Nminus/S+6*Vminus/V+fourth
        qmax = max(abs(x) for x in q)
        qmax_bounds = bounds(qmax)
        assert all(abs(x) < ball(qmax_bounds[1]) for x in q)
        stable = bool(all(abs(x) < 1 for x in q) and Nminus < S/8 and Vminus < V/6)
        branches.append(q)
        rows.append(dict(choices=list(choices), negative_mass=bounds(Nminus),
                         negative_mass_over_S=bounds(Nminus/S),
                         negative_variance_over_intrinsic=bounds(Vminus/V),
                         coefficient_fourth_sum=bounds(fourth), joint_cost_C1_r2=bounds(joint_cost),
                         centroid=bounds(mu), coefficient_max=qmax_bounds,
                         stable_C1_certified=stable))

    # Product kernel: K(z,w)=U(z)U(w)*prod(A_j(z)A_j(w)+B_j(z)B_j(w)).
    kernel = {(i, j): x*y for i, x in enumerate(unit) for j, y in enumerate(unit)}
    for block in blocks:
        aa = [(x+y)/2 for x, y in zip(block, block[::-1])]
        bb = [(x-y)/2 for x, y in zip(block, block[::-1])]
        local = {(i, j): aa[i]*aa[j]+bb[i]*bb[j] for i in range(3) for j in range(3)}
        updated = {}
        for (i, j), x in kernel.items():
            for (k, ell), y in local.items():
                key = (i+k, j+ell)
                updated[key] = updated.get(key, arb(0))+x*y
        kernel = updated
    for i in range(25):
        for j in range(25):
            check_zero(sum(q[i]*q[j] for q in branches)/16-kernel[i, j])

    mean_mass = sum(sum((abs(x)-x)/2 for x in q) for q in branches)/16
    covariance_mass_upper = (sum(kernel[i, i].sqrt() for i in range(25))-S)/2
    theta = [((2*block[2]+block[1])/sum(block)-1) for block in blocks]
    mean_centroid = sum(sum(j*x for j, x in enumerate(q))/S for q in branches)/16
    centroid_variance = sum((sum(j*x for j, x in enumerate(q))/S-12)**2 for q in branches)/16
    check_zero(mean_centroid-12)
    check_zero(centroid_variance-sum(t*t for t in theta))
    check_zero(sum(kernel[i, i] for i in range(25))-lam)
    coherent_cost = sum(
        8*sum((abs(x)-x)/2 for x in q)/S
        +6*sum(((abs(x)-x)/2)*(j-sum(k*y for k, y in enumerate(q))/S)**2
               for j, x in enumerate(q))/V
        +sum((x*x)*(x*x) for x in q)
        for q in (branches[0], branches[-1]))/2
    assert coherent_cost < 1
    if mean_mass > S/8:
        mass_verdict = 'REFUTED: uniform mean negative mass exceeds S/8'
    elif mean_mass < S/8:
        mass_verdict = 'PASSES this finite example only'
    else:
        raise AssertionError('Insufficient precision for mass comparison')
    out = dict(status='PASS', host=socket.gethostname(), precision_bits=192,
               elapsed_seconds=time.monotonic()-started, A=[8, 16, 24], L=L,
               exact_M='(17+7*sqrt(7))/27', all_circle_M_proof='Cubic factorization at u=(sqrt(7)-1)/6',
               branch_count=16, branches=rows, uniform_mass_verdict=mass_verdict,
               mean_negative_mass_over_S=bounds(mean_mass/S),
               mean_negative_mass_minus_S_over8=bounds(mean_mass-S/8),
               covariance_mass_upper_over_S=bounds(covariance_mass_upper/S),
               stable_C1_branches=sum(r['stable_C1_certified'] for r in rows),
               coherent_same_marginal_joint_cost_C1_r2=bounds(coherent_cost),
               coherent_same_marginal_certificate_passes=True,
               covariance_product_checked_against_all_branch_second_moments=True,
               centroid_mean=bounds(mean_centroid), centroid_variance=bounds(centroid_variance),
               qualification='One complete real ensemble on a predeclared dilation. '
               'Arb certifies inequalities; the exact spectral-factor and kernel identities have paper proofs. '
               'No universal branch selection or Chowla conclusion follows.')
    root = Path('.research/experiments/root_ensemble_2026-10-23')
    root.mkdir(parents=True, exist_ok=True)
    (root/'results.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'branches'}, indent=2))


if __name__ == '__main__':
    main()
