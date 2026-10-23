#!/usr/bin/env python3
"""Exact algebra checks for the paper continuum-profile countermodel.

Run through src/dirun.sh. This checks derivative identities and the
rational density bound. Positive definiteness is proved by the positive
series / triangular-kernel integrals in the linked paper note, not by
sampling a finite collection of matrices.
"""
import json
import socket
import time
from pathlib import Path

import sympy as sp


def main():
    if "dirichlet" not in socket.gethostname():
        raise SystemExit("Use src/dirun.sh")
    start = time.monotonic()
    u = sp.symbols("u", real=True)
    sigma = sp.Rational(1, 4)
    v = sigma * u**2
    h = v * sp.sqrt(1 - v) / 4
    second = sigma * (2 - 9*v + 6*v**2) / (4*(1-v)**sp.Rational(3, 2))
    assert sp.simplify(sp.diff(h, u, 2) - second) == 0
    assert h.subs(u, 0) == 0
    assert sp.diff(h, u).subs(u, 0) == 0
    z = sp.symbols("z", real=True)
    numerator = 2 - 9*z + 6*z**2
    # Its derivative is <= -6 on [0,1/4], and its minimum is 1/8.
    assert sp.diff(numerator, z).subs(z, sigma) == -6
    assert numerator.subs(z, sigma) == sp.Rational(1, 8)
    # Elementary antiderivative; avoids a numerical quadrature claim.
    primitive = u*sp.sqrt(1-u**2/4)/2 + sp.asin(u/2)
    assert sp.simplify(sp.diff(primitive, u) - sp.sqrt(1-u**2/4)) == 0
    density = (1 - (primitive.subs(u, 1) - primitive.subs(u, 0))) / 2
    exact_density = sp.Rational(1, 2) - sp.sqrt(3)/8 - sp.pi/12
    assert sp.simplify(density - exact_density) == 0
    sqrt_upper = sp.Rational(26, 15)
    assert sqrt_upper**2 > 3
    density_lower = sp.Rational(1, 2) - sqrt_upper/8 - sp.Rational(22, 7)/12
    assert density_lower == sp.Rational(3, 140)
    result = {
        "status": "EXACT_ALGEBRA_PASS",
        "scope": "Continuum necessary-condition countermodel; no Boolean set or Chowla counterexample.",
        "sigma": "1/4",
        "second_derivative_identity": True,
        "curvature_numerator_minimum": "1/8",
        "endpoint_value_and_derivative_zero": True,
        "density": str(exact_density),
        "density_strict_lower_bound": "3/140",
        "density_bound_dependencies": ["sqrt(3)<26/15 by squaring", "classical pi<22/7"],
        "positive_definiteness": "Paper proof: positive Catalan series and positive mixture of triangular kernels.",
        "sympy_version": sp.__version__,
        "compute_seconds": time.monotonic() - start,
    }
    output = Path(".research/experiments/cubic_two_scale_2026-10-23/profile_countermodel.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
