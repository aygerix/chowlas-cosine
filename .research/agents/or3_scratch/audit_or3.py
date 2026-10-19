"""Independent exact certificate reconstruction and F2 checks, on dirichlet.

This audit reconstructs the saved Bernstein certificate in the original
monomial variable, instead of repeating the generator's conversion.
"""
from fractions import Fraction
import json
import math
from pathlib import Path

import numpy as np

directory = Path(__file__).parent
data = json.loads((directory/"verification.json").read_text())


def add(p, q):
    ans = [Fraction(0)]*max(len(p), len(q))
    for i in range(len(ans)):
        ans[i] = (p[i] if i < len(p) else 0)+(q[i] if i < len(q) else 0)
    return ans


def product(p, q):
    ans = [Fraction(0)]*(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            ans[i+j] += p[i]*q[j]
    return ans


def power(p, n):
    ans = [Fraction(1)]
    for _ in range(n):
        ans = product(ans, p)
    return ans


target = list(map(Fraction, [Fraction(5, 2), -2, -8, 4, 8]))
intervals = sorted(data["exact_macro_bernstein"], key=lambda d: Fraction(d["a"]))
assert Fraction(intervals[0]["a"]) == -1 and Fraction(intervals[-1]["b"]) == 1
smallest = Fraction(100)
for i, cert in enumerate(intervals):
    a, b = Fraction(cert["a"]), Fraction(cert["b"])
    assert a < b
    if i:
        assert Fraction(intervals[i-1]["b"]) == a
    coeffs = list(map(Fraction, cert["coefficients"]))
    assert len(coeffs) == 5 and min(coeffs) > 0
    smallest = min(smallest, min(coeffs))
    s, one_minus_s = [-a/(b-a), 1/(b-a)], [b/(b-a), -1/(b-a)]
    reconstructed = [Fraction(0)]
    for j, bj in enumerate(coeffs):
        term = product(power(s, j), power(one_minus_s, 4-j))
        reconstructed = add(reconstructed, [bj*math.comb(4, j)*v for v in term])
    assert reconstructed == target, (cert, reconstructed)
assert smallest == Fraction(1, 24)

rng = np.random.default_rng(20261019)
max_formula_error = 0.
max_ratio = 0.
minimum_kernel = 1.
for rec in data["records"]:
    fibres = {int(y): rs for y, rs in rec["fibres"].items()}
    residues = sorted({r for rs in fibres.values() for r in rs})
    ys = {r: [y for y, rs in fibres.items() if r in rs] for r in residues}
    q, t = rec["q_identity_test"], rec["t"]
    H = min(q//2, max(2, 4*t))
    w = np.maximum(0., 1-np.minimum(np.arange(q), q-np.arange(q))/H)
    mu = np.fft.ifft(w)
    assert np.max(np.abs(mu.imag)) < 1e-10
    assert mu.real.min() >= -1e-10 and abs(mu.real.sum()-1) < 1e-10
    minimum_kernel = min(minimum_kernel, float(mu.real.min()))
    difference = np.array([w[(r+t) % q]-w[r] for r in residues])
    bound = sum(abs(difference[i])*math.sqrt(len(ys[r])) for i, r in enumerate(residues))
    assert bound <= min(1, t/H)*math.sqrt(rec["k"]*rec["n"])+1e-8
    # Independent direct expansion of the localized and re-paired profiles.
    th = rng.uniform(0, 2*math.pi)
    u = rng.uniform(0, 2*math.pi, size=31)
    z = np.array([sum(np.exp(1j*y*th) for y in ys[r]) for r in residues])
    phase = np.exp(1j*np.outer(u, residues))
    direct = np.real(sum((w[r]+np.exp(1j*t*u)*w[(r+t) % q])*z[i]*phase[:, i]
                         for i, r in enumerate(residues)))
    repaired = np.real((1+np.exp(1j*t*u))*sum(w[r]*z[i]*phase[:, i]
                                           for i, r in enumerate(residues)))
    error = np.real(np.exp(1j*t*u)*(phase @ (difference*z)))
    max_formula_error = max(max_formula_error, float(np.max(abs(direct-repaired-error))))
    assert np.max(abs(direct-repaired-error)) < 1e-8
    # Finite sampling of the L2-in-theta/supremum-in-u inequality; proof in report.
    theta = 2*math.pi*np.arange(2*max(fibres)+1)/(2*max(fibres)+1)
    zz = np.array([np.exp(1j*np.outer(theta, ys[r])).sum(axis=1) for r in residues])
    ug = 2*math.pi*np.arange(128)/128
    delta = np.real(np.exp(1j*t*ug)[:, None]*(np.exp(1j*np.outer(ug, residues)) @
                                              (difference[:, None]*zz)))
    norm = float(np.sqrt(np.mean(np.max(abs(delta), axis=0)**2)))
    assert norm <= bound+1e-8
    if bound:
        max_ratio = max(max_ratio, norm/bound)

out = {"exact_certificate": "PROVED by exact rational reconstruction",
       "covered_interval": "[-1,1]", "pieces": len(intervals),
       "minimum_bernstein_coefficient": str(smallest),
       "certified_macro_lower_bound": "-11/24",
       "F2_status": "NUMERICAL finite checks; independent paper proof in report",
       "F2_seed": 20261019, "F2_cases": len(data["records"]),
       "F2_formula_max_error": max_formula_error,
       "F2_sampled_L2_over_bound_max": max_ratio,
       "cyclic_kernel_min_numerical": minimum_kernel}
(directory/"audit.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
