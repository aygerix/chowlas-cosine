"""Adversarial checks for the OR2 residue-strip theorem; run only on dirichlet.

No frequency optimization or ILP is performed. The project's Newton polish
evaluates a fixed trigonometric polynomial. Seed 20261018.
Floating checks are evidence only; the report contains the paper proof.
"""
from __future__ import annotations

import itertools
import json
import math
import platform
import sys
from pathlib import Path

import flint
import numpy as np
import scipy

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
from chowla import certify_lower_bound, f_direct, min_estimate_fft

SEED = 20261018
OUT = Path(__file__).parent / "verification.json"
rng = np.random.default_rng(SEED)


def ceil_sqrt(n):
    z = math.isqrt(n)
    return z + (z * z != n)


def make_set(t, residues, ys, q):
    s = sorted({q * y + r for r in residues for y in ys[r]})
    assert len(s) == sum(len(ys[r]) for r in residues)
    assert min(s) > 0
    assert not any(v + j * t in s for v in s for j in (1, 2))
    a = sorted(s + [v + t for v in s])
    assert len(set(a)) == 2 * len(s)
    return s, a


def phase_case(t, residues, ys, q, trials=7):
    n = sum(map(len, ys.values()))
    k = len(residues)
    D = t + max(residues)
    u0 = math.pi / t
    eps = math.pi**2 * D**2 / (2 * q**2)
    errs = {"lifting": 0., "derivative_formula": 0., "root": 0.,
            "sample_margin": math.inf, "derivative_margin": math.inf}
    _, a = make_set(t, residues, ys, q)
    for theta in rng.uniform(0, 2 * math.pi, size=trials):
        z = np.array([np.exp(1j * theta * np.array(ys[r])).sum()
                      for r in residues])
        U = 2 * math.sqrt(k) * float(np.linalg.norm(z))
        L = D**2 * U
        u = (theta + 2 * math.pi * np.arange(q)) / q

        def macro(v):
            v = np.atleast_1d(v)
            b = (np.exp(1j * np.outer(v, residues)) * z).sum(axis=1)
            return ((1 + np.exp(1j * t * v)) * b).real

        vals = macro(u)
        errs["lifting"] = max(errs["lifting"],
                              float(np.max(np.abs(vals - f_direct(a, u)))))
        M_grid = max(0., -float(vals.min()))
        fine = np.linspace(0, 2 * math.pi, 16 * q + 1)
        fine_min = float(macro(fine).min())
        errs["sample_margin"] = min(errs["sample_margin"],
                                    fine_min + M_grid + eps * U)
        d = t * float(np.imag(np.dot(np.exp(1j * np.array(residues) * u0), z)))
        dc = float(np.real(np.dot(
            1j * np.array(residues) * np.exp(1j * np.array(residues) * u0)
            + 1j * (np.array(residues) + t)
            * np.exp(1j * (np.array(residues) + t) * u0), z)))
        errs["derivative_formula"] = max(errs["derivative_formula"], abs(d - dc))
        errs["root"] = max(errs["root"], abs(float(macro(u0)[0])))
        errs["derivative_margin"] = min(errs["derivative_margin"],
                                        2 * L * (M_grid + eps * U) - d * d)

    # Independent orthogonality computation, compared with equally spaced theta.
    by_y = {}
    for r in residues:
        for y in ys[r]:
            by_y.setdefault(y, []).append(r)
    coeff = {y: sum(np.exp(1j * np.array(rs) * u0)) for y, rs in by_y.items()}
    exact_formula = t*t * (coeff.get(0, 0j).imag**2
                           + .5 * sum(abs(v)**2 for y, v in coeff.items() if y > 0))
    theta = 2 * math.pi * np.arange(2 * max(by_y) + 1) / (2 * max(by_y) + 1)
    b = sum(v * np.exp(1j * y * theta) for y, v in coeff.items())
    quadrature = float(np.mean((t * b.imag)**2))
    errs["orthogonality_error"] = abs(exact_formula - quadrature)
    positive_count = sum(len(rs) for y, rs in by_y.items() if y > 0)
    errs["positive_level_count"] = positive_count
    errs["energy_ratio_to_claim"] = (exact_formula / (t*t*positive_count/4)
                                     if positive_count else None)
    # Independent test of the sharper, direct sampled derivative lemma.
    # Curvature is now the weighted sum, rather than the earlier uniform U bound.
    weighted_curvature_margin = math.inf
    for theta in rng.uniform(0, 2 * math.pi, size=3):
        z = np.array([np.exp(1j * theta * np.array(ys[r])).sum() for r in residues])
        weights = np.array([r*r+(r+t)**2 for r in residues])
        curv = float(np.dot(weights, np.abs(z)))
        d = t * float(np.imag(np.dot(np.exp(1j*np.array(residues)*u0), z)))
        u = (theta + 2*math.pi*np.arange(q))/q
        vals = ((1+np.exp(1j*t*u))
                * (np.exp(1j*np.outer(u, residues))*z).sum(axis=1)).real
        m = max(0., -float(vals.min()))
        weighted_curvature_margin = min(weighted_curvature_margin,
                                        2*curv*m + math.pi**2*curv**2/q**2-d*d)
    errs["weighted_curvature_margin"] = weighted_curvature_margin
    assert errs["lifting"] < 1e-7
    assert errs["derivative_formula"] < 1e-8
    assert errs["root"] < 1e-8
    assert errs["sample_margin"] > -1e-8
    assert errs["derivative_margin"] > -1e-6
    assert errs["orthogonality_error"] < 1e-7
    if positive_count:
        assert errs["energy_ratio_to_claim"] > 1 - 1e-10
    assert weighted_curvature_margin > -1e-6
    return {"t": t, "residues": residues, "q": q, "n": n, "errors": errs}


records = []
for t in (1, 2, 3, 6, 12):
    available = list(range(t//2 + 1))
    for k in sorted({1, min(2, len(available)), len(available)}):
        residues = sorted(available if k == len(available) else
                          rng.choice(available, size=k, replace=False).tolist())
        for mode in ("common", "disjoint", "random"):
            if mode == "common":
                ys = {r: list(range(1, 10)) for r in residues}
            elif mode == "disjoint":
                ys = {r: list(range(1 + 9*j, 10 + 9*j))
                      for j, r in enumerate(residues)}
            else:
                ys = {r: sorted(rng.choice(np.arange(1, 65), size=9,
                                          replace=False).tolist()) for r in residues}
            q = ceil_sqrt(48**2 * t*t*k)
            records.append(phase_case(t, residues, ys, q))

# Exhaustive small membership patterns, with all possible nonempty Y_r.
# This is a finite identity test, not an exhaustive search for optimal sets.
exhaustive = 0
for t in (2, 4):
    residues = [0, t//2]
    q = ceil_sqrt(48**2 * t*t*2)
    subsets = [list(v) for j in range(1, 4)
               for v in itertools.combinations(range(1, 4), j)]
    for y0, y1 in itertools.product(subsets, repeat=2):
        phase_case(t, residues, dict(zip(residues, (y0, y1))), q, trials=1)
        exhaustive += 1

boundaries = []
for t, residues, ys in [
    (2, [1], {1: [0]}),
    (4, [0, 1, 2], {0: [1, 2], 1: [0, 1, 3], 2: [0]}),
    (6, [1, 2, 3], {1: [0], 2: [0], 3: [0]}),
    (8, [0, 2, 4], {0: list(range(1, 51)), 2: [1], 4: [2]}),
]:
    q = ceil_sqrt(32**2*t*t*len(residues))
    boundaries.append(phase_case(t, residues, ys, q))

# Whole-circle finite examples; FFT gives estimates, and ball point evaluation
# gives a rigorous one-point witness for a lower bound on M(A).
flint.ctx.prec = 128
examples = []
specs = [
    (1, [0], {0: [1, 3, 8]}, 48),
    (2, [0, 1], {0: [1, 3, 7], 1: [2, 4, 9]}, ceil_sqrt(48**2 * 4 * 2)),
    (8, [0, 1, 4], {0: list(range(1, 33)), 1: list(range(1, 33)),
                     4: list(range(1, 33))}, ceil_sqrt(48**2 * 64 * 3)),
]
for t, residues, ys, q in specs:
    s, a = make_set(t, residues, ys, q)
    est = min_estimate_fft(a, oversample=8)
    # Explicit rational grid point near the numerical witness.
    denom = 1 << 28
    j = round(est.xmin / (2 * math.pi) * denom)
    value = sum((flint.arb(flint.fmpq(2 * aa * j, denom)).cos_pi()
                 for aa in a), flint.arb(0))
    analytic = math.sqrt(len(s) / len(residues)) / 32
    assert (-value).lower() > analytic
    rec = {"t": t, "residues": residues, "Y": ys, "q": q,
           "n": len(s), "N": len(a), "max_A": max(a),
           "analytic_M_lower": analytic, "estimated_M": -est.fmin,
           "estimated_R": est.R, "x_over_2pi": [j, denom],
           "rigorous_point_minus_f": str(-value)}
    if max(a) <= 1500:
        cert = certify_lower_bound(a, oversample=16, prec=128)
        rec["whole_circle_certificate"] = vars(cert)
    examples.append(rec)

# Two deliberate failure modes, each checked exactly at the coefficient level.
# (1) Signed quotient levels kill the claimed analytic L2 identity.
# (2) Residues 0 and 3t cancel the derivative despite valid 2-run conditions.
failures = {
    "signed_levels": "Y={-1,1}: Im F_Y is identically zero (excluded hypothesis).",
    "wide_residue_arc": "R={0,3t}, Y_0=Y_3t: derivative vanishes at pi/t; runs still have length two.",
}
assert (1 + (-1)**3) == 0
result = {"seed": SEED, "python": platform.python_version(),
          "numpy": np.__version__, "scipy": scipy.__version__,
          "flint": flint.__version__, "phase_cases": records,
          "exhaustive_membership_cases": exhaustive,
          "boundary_cases": boundaries,
          "examples": examples, "deliberate_failures": failures}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"phase_cases": len(records), "boundary_cases": len(boundaries),
                  "exhaustive_membership_cases": exhaustive,
                  "max_lifting_error": max(r["errors"]["lifting"] for r in records),
                  "examples": examples, "output": str(OUT)}, indent=2), flush=True)
