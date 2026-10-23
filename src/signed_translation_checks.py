#!/usr/bin/env python3
"""Exact constants for signed translations and the two-scale obstruction.

The infinite-family theorem has a paper proof and independent advisor
audit. This script checks the exact algebra and rational endpoint bounds;
it does not enumerate exponentially large frequencies or sample minima.
Run through src/dirun.sh.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import socket
import time


def main():
    if "dirichlet" not in socket.gethostname():
        raise SystemExit("Use src/dirun.sh")
    import sympy as sp

    start = time.monotonic()
    delta = F(1, 64)
    margin = F(3, 64) - 2*delta*(1+delta)
    assert margin == F(31, 2048)
    root_constant_squared = margin/F(9, 4)
    assert root_constant_squared == F(31, 4608)
    m = sp.symbols("m", positive=True)
    n0 = 2*m*m-m
    n1 = (m*m-m)/2
    n = n0+n1
    floor = 3*m/2
    assert sp.expand(n - floor**2 - m*(m-6)/4) == 0
    assert sp.expand(n+floor) == 5*m*m/2
    alpha0 = sp.cancel(n0/(n+floor))
    alpha1 = sp.cancel(n1/(n+floor))
    assert sp.simplify(alpha0 - (sp.Rational(4, 5)-sp.Rational(2, 5)/m)) == 0
    assert sp.simplify(alpha1 - (sp.Rational(1, 5)-sp.Rational(1, 5)/m)) == 0
    threshold = 2000
    low0 = F(4, 5)-F(2, 5*threshold)-delta*delta
    low1 = F(1, 5)-F(1, 5*threshold)-delta*delta
    assert low0 > F(3, 4)
    assert low1 > F(3, 16)
    assert (1+delta)**4 < F(9, 8)
    product_lower = F(3, 4)*F(3, 16)/F(9, 8)
    assert product_lower == F(1, 8)
    four_missing_upper = F(12, 5*threshold)+F(8, 65)
    assert four_missing_upper < product_lower
    # Three-color upgrade: n0 >= 85*lambda, N/S <= 1/8.
    three_delta = F(1, 8)
    block_mass_lower = F(85, 256)
    color_lower = (block_mass_lower-three_delta**2)/(1+three_delta)**2
    assert color_lower == F(1, 4)
    edge_lower = F(7, 9)-F(1, 256)
    assert edge_lower > F(3, 4)
    e = sp.symbols("e", real=True)
    assert sp.expand((2*e-1)**2-(e-sp.Rational(1, 2))
                     -(4*e-3)*(e-sp.Rational(1, 2))) == 0
    three_gap = (4*edge_lower-3)*(edge_lower-F(1, 2))
    assert three_gap > 0
    bu_upper = F(11, 20)
    assert 3*bu_upper**2 == F(363, 400) < 1
    bu_base_threshold = 20000
    assert F(bu_base_threshold) > (85*3*bu_upper)**2
    result = {
        "status": "EXACT_CONSTANTS_PASS",
        "scope": "Paper theorem constants; no sampled minimum or huge-set enumeration.",
        "signed_mass_threshold": str(delta),
        "signed_gram_margin": str(margin),
        "root_constant_squared": str(root_constant_squared),
        "even_m_threshold": threshold,
        "n": str(n),
        "actual_M": str(floor),
        "n_minus_M_squared": str(sp.factor(n-floor**2)),
        "S_squared": str(sp.expand(n+floor)),
        "low_edge_numerator_lower": str(low0),
        "high_edge_numerator_lower": str(low1),
        "edge_probability_product_strict_lower": str(product_lower),
        "four_missing_probability_upper": str(four_missing_upper),
        "strict_contradiction_gap": str(product_lower-four_missing_upper),
        "three_color_upgrade": {
            "signed_mass_threshold": str(three_delta),
            "finite_premise": "Each of three equal blocks has n0>=85*lambda; no mixed-color triangle.",
            "block_mass_lower": str(block_mass_lower),
            "each_color_probability_lower": str(color_lower),
            "edge_probability_lower": str(edge_lower),
            "edge_lower_minus_three_quarters": str(edge_lower-F(3, 4)),
            "triangle_contradiction_gap_at_edge_lower": str(three_gap),
            "cited_Bu_base_ratio_upper_eventually": str(bu_upper),
            "three_block_ratio_upper_squared": str(3*bu_upper**2),
            "base_cardinality_additional_threshold": bu_base_threshold,
            "scope": "Cited Bu asymptotic upper bound also required; its threshold is not computed here.",
        },
        "independent_paper_dependencies": [
            "weighted graph degree inequality from row-difference Jensen",
            "no mixed triangles for separated small and L-divisible lags",
            "signed autocorrelation matching and ordered missing-lag mass bound",
            "parity-balanced Sidon square identity at pi",
        ],
        "sympy_version": sp.__version__,
        "compute_seconds": time.monotonic()-start,
    }
    output = Path(".research/experiments/signed_translation_2026-10-23/constants.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
