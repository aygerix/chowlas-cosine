"""Exhaust exact monic reciprocal rational squares with Boolean outer coefficients.

The central coefficient of h*h is free. This searches a growing-degree
construction mechanism, not numerical minima. All math runs on Dirichlet.
"""
import argparse
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import platform
import socket
import time


def multiply(h):
    out = [F(0) for _ in range(2*len(h)-1)]
    for i, a in enumerate(h):
        for j, b in enumerate(h):
            out[i+j] += a*b
    return out


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-degree', type=int, default=24)
    args = parser.parse_args()
    assert 2 <= args.max_degree <= 30 and args.max_degree % 2 == 0
    import sympy as sp
    started = time.monotonic()
    rows, witnesses = [], []
    T = sp.Symbol('T')
    for degree in range(2, args.max_degree+1, 2):
        half = degree//2
        survivors = []
        tested = 0
        for bits in itertools.product((0, 1), repeat=half):
            tested += 1
            h = [F(1)]
            for k, bit in enumerate(bits, 1):
                correction = sum((h[j]*h[k-j] for j in range(1, k)), F(0))
                h.append((F(bit)-correction)/2)
            h += h[-2::-1]
            assert len(h) == degree+1 and h == h[::-1]
            tail = []
            for k in range(half+1, degree):
                coefficient = sum((h[j]*h[k-j] for j in range(k+1)), F(0))
                if coefficient not in (0, 1):
                    break
                tail.append(coefficient)
            else:
                square = multiply(h)
                assert all(a in (0, 1) for k, a in enumerate(square) if k != degree)
                A = [a for a in range(1, degree+1) if square[degree+a]]
                lam = square[degree]/2
                # Independent off-zero autocorrelation computation, not h*h.
                autocorr = [sum((h[j]*h[j+a] for j in range(len(h)-a)), F(0))
                            for a in range(degree+1)]
                assert autocorr[0]/2 == lam
                assert all(autocorr[a] == int(a in A) for a in range(1, degree+1))
                # Exact Chebyshev/Sturm existence of a unit-circle root of h.
                cheb = sp.Poly(sp.Rational(h[half].numerator, h[half].denominator)
                      + sum(2*sp.Rational(h[half-j].numerator, h[half-j].denominator)
                            *sp.chebyshevt(j, T) for j in range(1, half+1)), T)
                unit_zero = bool(cheb.eval(-1) == 0 or cheb.eval(1) == 0
                                 or cheb.count_roots(-1, 1) > 0)
                n = len(A)
                row = dict(degree=degree, h=[str(a) for a in h], A=A, n=n,
                    max_A=max(A), lambda_upper_exact=str(lam),
                    upper_R_squared_exact=str(lam*lam/n),
                    unit_circle_zero_exact=unit_zero,
                    actual_M_exact=str(lam) if unit_zero else None,
                    certification=('exact full-circle square identity; actual optimum also certified'
                                   if unit_zero else 'exact full-circle upper bound only'),
                    proposed_one_or_two_frequency_form=(
                        h == [F(1)]+[F(0)]*(degree-1)+[F(1)]
                        or h == [F(1)]+[F(0)]*(half-1)+[F(1,2)]
                                +[F(0)]*(half-1)+[F(1)]))
                survivors.append(row)
                if not row['proposed_one_or_two_frequency_form']:
                    witnesses.append(row)
        rows.append(dict(degree=degree, bit_vectors=tested,
                         complete_first_half_enumeration=True, survivors=survivors))
        print(json.dumps(dict(degree=degree, tested=tested,
                              survivors=len(survivors), new_patterns=len(witnesses))), flush=True)
    out = dict(status='PASS', host=socket.gethostname(), python=platform.python_version(),
               sympy=sp.__version__, elapsed_seconds=time.monotonic()-started,
               scope=dict(even_degrees=[2, args.max_degree], signed_coefficients_allowed=True,
                          rational_coefficients=True, monic_reciprocal=True,
                          all_outer_coefficients_exactly_zero_or_one=True,
                          central_coefficient_unrestricted=True,
                          optimality_not_assumed=True),
               degree_results=rows, counterexamples_to_proposed_classification=witnesses,
               qualification=('Finite complete enumeration of this rational-square class only; '
                              'not an unrestricted Chowla theorem. Odd-degree proof is separate.'))
    dest = Path('.research/experiments/boolean_square_2026-10-23/enumeration.json')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', total_patterns=sum(len(r['survivors']) for r in rows),
                          counterexamples=len(witnesses), artifact=str(dest))), flush=True)


if __name__ == '__main__':
    main()
