"""Adversarial identity checks for OR3 Theorem D; run only on dirichlet.

Seed 20261018. No optimization/ILP. All floating tests are NUMERICAL;
the report gives a paper proof independent of these tests.
"""
from __future__ import annotations

import itertools
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import minimize_scalar

SEED = 20261018
rng = np.random.default_rng(SEED)
records = []
global_errors = {name: 0.0 for name in (
    "lift", "projection", "derivative", "orthogonality", "e_l2", "K_l2"
)}


def trig_min(freq, coeff):
    """Numerical minimum of Re sum coeff[a] exp(i freq[a] u)."""
    freq = np.asarray(freq, dtype=float)
    coeff = np.asarray(coeff, dtype=complex)
    size = max(256, 32 * (int(max(freq, default=0)) + 1))
    u = 2 * math.pi * np.arange(size) / size
    vals = np.real(np.exp(1j * np.outer(u, freq)) @ coeff)
    candidates = np.where((vals <= np.roll(vals, 1)) &
                          (vals <= np.roll(vals, -1)))[0]
    best = float(vals.min())
    witness = float(u[vals.argmin()])
    step = 2 * math.pi / size
    for i in candidates:
        ans = minimize_scalar(
            lambda v: float(np.real(np.exp(1j * freq * v) @ coeff)),
            bounds=(u[i] - step, u[i] + step), method="bounded",
            options={"xatol": 1e-13},
        )
        if ans.fun < best:
            best, witness = float(ans.fun), float(ans.x)
    return best, witness


def check_case(t, L, fibres, label):
    fibres = {int(y): sorted(rs) for y, rs in fibres.items() if rs}
    residues = sorted({r for rs in fibres.values() for r in rs})
    assert fibres and min(fibres) >= 0
    assert 0 not in fibres.get(0, [])
    zero_mode = 0 in fibres
    assert all(0 <= r <= L*t for r in residues)
    assert all(abs(r-s) not in (t, 2*t)
               for rs in fibres.values() for r, s in itertools.combinations(rs, 2))
    ys = {r: sorted(y for y, rs in fibres.items() if r in rs) for r in residues}
    counts = {r: len(ys[r]) for r in residues}
    n = sum(counts.values())
    k = len(residues)
    B, J = L*L+(L+1)*(L+1), 2*L+3
    # Small q tests the exact identities without allocating the very large
    # sufficient q of Theorem D. The theorem threshold is saved separately.
    # In particular, most cases have t NOT dividing q.
    q = 8*(L+2)*t+1
    threshold_q = math.ceil((24 if zero_mode else 16)*B*J*t*math.sqrt((L+1)*k))
    S = sorted(q*y+r for y, rs in fibres.items() for r in rs)
    A = sorted(S+[s+t for s in S])
    assert len(S) == n and len(set(A)) == 2*n and min(S) > 0
    assert zero_mode or min(S) >= q
    Sset = set(S)
    assert not any(s+j*t in Sset for s in S for j in (1, 2))
    hslots = [h for h in range(L+1) if h*t in ys]
    N = sum(counts[h*t] for h in hslots)
    by_y = {y: sum((-1)**h for h in hslots if y in ys[h*t]) for y in fibres}
    C0 = sum(b*b for y, b in by_y.items() if y > 0)
    Nalt = sum((-1)**h*counts[h*t] for h in hslots)
    assert (Nalt-by_y.get(0, 0))**2 <= N*C0

    freq = residues + [r+t for r in residues]
    realcoeff = [counts[r] for r in residues]*2
    fmin, _ = trig_min(freq, realcoeff)
    m = max(0., -fmin)
    assert n <= 2*k*(counts.get(0, 0)+m)+1e-7
    assert N <= J*J*C0+(J*J-1)*m+(2*J*(L+1) if zero_mode else 0)+1e-7
    vm = 2*math.pi*np.arange(J)/J
    qvals = sum(counts[h*t]*(-1)**h*(np.ones(J)+2*sum((-1)**a*np.cos(a*vm)
                    for a in range(1, h+1))) for h in hslots)
    if hslots:
        assert abs(qvals[0]-N) < 1e-7
        assert abs(np.mean(qvals)-Nalt) < 1e-7
    assert abs(np.sum(1/(1+np.cos(vm)))-J*J/2) < 1e-7

    # Orthogonality uses an independent exact-degree quadrature.
    Q = 2*max(fibres)+1
    theta = 2*math.pi*np.arange(Q)/Q
    zz = {r: np.sum(np.exp(1j*np.outer(theta, ys[r])), axis=1) for r in residues}
    alt = sum((-1)**h*zz[h*t] for h in hslots) if hslots else np.zeros(Q)
    orthoerr = abs(float(np.mean(alt.imag**2))-C0/2)
    global_errors["orthogonality"] = max(global_errors["orthogonality"], orthoerr)
    assert orthoerr < 1e-8
    lam = sum((r*r+(r+t)**2)*abs(zz[r]) for r in residues)
    ee = math.pi**2*lam/(2*q*q)
    e_bound = math.pi**2*B*t*t*math.sqrt(k*n)/(2*q*q)
    K = sum((h*h+(h+1)**2)*abs(zz[h*t]) for h in hslots) if hslots else np.zeros(Q)
    assert float(np.mean(ee*ee)) <= e_bound*e_bound+1e-8
    assert float(np.mean(K*K)) <= B*B*(L+1)*N+1e-8
    global_errors["e_l2"] = max(global_errors["e_l2"],
                                max(0., float(np.mean(ee*ee))-e_bound*e_bound))
    global_errors["K_l2"] = max(global_errors["K_l2"],
                                max(0., float(np.mean(K*K))-B*B*(L+1)*N))

    min_projected_derivative_margin = math.inf
    for th in rng.uniform(0, 2*math.pi, size=3):
        z = {r: sum(np.exp(1j*y*th) for y in ys[r]) for r in residues}
        curvature = sum((r*r+(r+t)**2)*abs(z[r]) for r in residues)
        err = math.pi**2*curvature/(2*q*q)
        us = (th+2*math.pi*np.arange(q))/q
        hv = ((1+np.exp(1j*t*us))*sum(z[r]*np.exp(1j*r*us) for r in residues)).real
        Mg = max(0., -float(hv.min()))
        # Direct evaluation uses actual frequencies, independent of lifting.
        select = rng.choice(q, size=min(q, 9), replace=False)
        direct = sum(np.cos(a*us[select]) for a in A)
        lift_err = float(np.max(np.abs(direct-hv[select])))
        global_errors["lift"] = max(global_errors["lift"], lift_err)
        assert lift_err < 1e-8
        v = rng.uniform(0, 2*math.pi, size=11)
        projected = np.zeros(len(v))
        for j in range(t):
            u = (v+2*math.pi*j)/t
            projected += ((1+np.exp(1j*t*u))*sum(z[r]*np.exp(1j*r*u)
                                               for r in residues)).real/t
        low = sum(z[h*t]*np.exp(1j*h*v) for h in hslots) if hslots else np.zeros(len(v), complex)
        formula = ((1+np.exp(1j*v))*low).real
        projerr = float(np.max(np.abs(projected-formula)))
        global_errors["projection"] = max(global_errors["projection"], projerr)
        assert projerr < 1e-8
        hfmin, _ = trig_min(freq, [z[r] for r in residues]*2)
        assert hfmin >= -Mg-err-1e-7
        if hslots:
            gfmin, _ = trig_min(hslots+[h+1 for h in hslots], [z[h*t] for h in hslots]*2)
            assert gfmin >= -Mg-err-1e-7
            d = sum((-1)**h*z[h*t] for h in hslots).imag
            ddirect = np.real(sum((1j*h*np.exp(1j*h*math.pi)+
                             1j*(h+1)*np.exp(1j*(h+1)*math.pi))*z[h*t] for h in hslots))
            derr = abs(float(d-ddirect))
            global_errors["derivative"] = max(global_errors["derivative"], derr)
            assert derr < 1e-8
            curv0 = sum((h*h+(h+1)**2)*abs(z[h*t]) for h in hslots)
            margin = 2*curv0*(Mg+err)-d*d
            min_projected_derivative_margin = min(min_projected_derivative_margin, margin)
            assert margin > -1e-7

    records.append({"label": label, "t": t, "L": L, "n": n, "k": k,
                    "q_identity_test": q, "q_theorem_sufficient": threshold_q,
                    "N": N, "C0": C0, "macro_m_numerical": m,
                    "branch": "macro" if m >= n/((16 if zero_mode else 8)*k*J*J) else "derivative",
                    "zero_mode": zero_mode,
                    "theorem_bound": math.sqrt(n/k)/((64 if zero_mode else 32)*B*J*J*math.sqrt(L+1)),
                    "projection_derivative_margin": min_projected_derivative_margin if hslots else None,
                    "fibres": fibres})


for t in (1, 2, 3, 6, 12):
    for L in (0, 1, 3, 5):
        for trial in range(4):
            fibres = {}
            for y in range(1, 10):
                selected = []
                for r in rng.permutation(L*t+1):
                    r = int(r)
                    if rng.random() < .45 and all(abs(r-s) not in (t, 2*t) for s in selected):
                        selected.append(r)
                if selected:
                    fibres[y] = selected
            if not fibres:
                fibres = {1: [0]}
            check_case(t, L, fibres, f"random_{trial}")

# Adversarial common fibres, exact cancellation, arithmetic progressions,
# no zero residue, disjoint fibres, and sharply unequal fibre counts.
check_case(2, 3, {y: [0, 6] for y in range(1, 33)}, "complete_cancellation")
check_case(4, 5, {y: [0, 6, 12, 18] for y in range(1, 17)}, "AP_step_3t_over_2")
check_case(3, 5, {y: [0, 9] for y in range(1, 33)}, "AP_step_3t")
check_case(12, 1, {y: list(range(6)) for y in range(1, 33)}, "common_short_arc")
check_case(12, 1, {y: list(range(1, 7)) for y in range(1, 33)}, "no_multiples_of_t")
check_case(6, 3, {**{y: [0] for y in range(1, 65)}, 65: [1], 66: [2], 67: [18]}, "unbalanced")
check_case(6, 3, {y: [y % 19] for y in range(1, 65)}, "disjoint_residues_per_level")
check_case(1, 3, {0: [3]}, "zero_level_only")
check_case(2, 3, {0: [1, 6], **{y: [0, 6] for y in range(1, 17)}}, "zero_level_cancellation")
check_case(3, 5, {0: [3, 12], **{y: [0, 9] for y in range(1, 100)}}, "zero_level_with_large_mass")

# Exhaust every admissible fibre subset on {0,1,2,3} at t=1,
# at positive quotient levels {1,2}; empty overall set is omitted.
independent = [list(v) for j in range(5) for v in itertools.combinations(range(4), j)
               if all(abs(r-s) not in (1, 2) for r, s in itertools.combinations(v, 2))]
exhaustive = 0
for f1, f2 in itertools.product(independent, repeat=2):
    if f1 or f2:
        check_case(1, 3, {1: f1, 2: f2}, "exhaustive_2_levels")
        exhaustive += 1

# Exact polynomial checks use rational arithmetic in the standard library;
# no additional VM packages or shared environment changes are needed.
def add(p, q):
    ans = [Fraction(0)]*max(len(p), len(q))
    for i, v in enumerate(p):
        ans[i] += v
    for i, v in enumerate(q):
        ans[i] += v
    return ans


def scale(p, a):
    return [a*v for v in p]


def mul(p, q):
    ans = [Fraction(0)]*(len(p)+len(q)-1)
    for i, v in enumerate(p):
        for j, w in enumerate(q):
            ans[i+j] += v*w
    return ans


cheby = [[Fraction(1)], [Fraction(0), Fraction(1)]]
for h in range(1, 13):
    cheby.append(add(mul([0, 2], cheby[-1]), scale(cheby[-2], -1)))
symbolic = []
for h in range(13):
    quotient = [Fraction(1)]
    for a in range(1, h+1):
        quotient = add(quotient, scale(cheby[a], 2*(-1)**a))
    quotient = scale(quotient, (-1)**h)
    residual = add(mul([1, 1], quotient), scale(add(cheby[h], cheby[h+1]), -1))
    assert all(v == 0 for v in residual)
    symbolic.append(h)
H = add(add([1], cheby[1]), add(cheby[3], cheby[4]))
factorized = scale(mul(mul([1, 1], [-1, 2]), [-1, 0, 2]), 2)
assert all(v == 0 for v in add(H, scale(factorized, -1)))


def bernstein_on_interval(p, a, b):
    d = len(p)-1
    power = [sum(p[h]*math.comb(h, j)*a**(h-j)*(b-a)**j
                 for h in range(j, d+1)) for j in range(d+1)]
    return [sum(power[j]*Fraction(math.comb(i, j), math.comb(d, j))
                for j in range(i+1)) for i in range(d+1)]


# Exact positive Bernstein coefficients certify H+1/2 on all of [-1,1].
p = add(H, [Fraction(1, 2)])
pending = [(Fraction(-1), Fraction(1))]
bernstein = []
while pending:
    a, b = pending.pop()
    coeff = bernstein_on_interval(p, a, b)
    if min(coeff) > 0:
        bernstein.append({"a": str(a), "b": str(b), "coefficients": list(map(str, coeff))})
    else:
        assert b-a > Fraction(1, 1024)
        mid = (a+b)/2
        pending.extend([(a, mid), (mid, b)])

out = {"status": "NUMERICAL, with exact symbolic identities explicitly listed",
       "seed": SEED, "python": platform.python_version(), "numpy": np.__version__,
       "scipy": scipy.__version__,
       "cases": len(records), "exhaustive_cases": exhaustive,
       "maximum_errors": global_errors,
       "zero_C0_cases": sum(r["C0"] == 0 for r in records),
       "no_t_multiple_cases": sum(r["N"] == 0 for r in records),
       "nondivisible_q_t_cases": sum(r["q_identity_test"] % r["t"] != 0 for r in records),
       "macro_branch_cases": sum(r["branch"] == "macro" for r in records),
       "symbolic_quotient_h": symbolic,
       "exact_macro_bernstein": bernstein,
       "records": records}
path = Path(__file__).with_name("verification.json")
path.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({key: value for key, value in out.items() if key != "records"}, indent=2))
