"""Exact endpoint-energy test on the existing certified triangular pilot.

No search or fresh random draw. Add its missing endpoint Q. Transfer the
previous all-circle M upper by M(A union {Q}) <= M(A)+1. Independently
compute the new signed boundary energy by integer pair counts and by
the complete polynomial's exact autocorrelation. Run on Dirichlet.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import socket
import time


def digest(values):
    return hashlib.sha256(','.join(map(str, values)).encode()).hexdigest()


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    import numpy as np
    started = time.monotonic()
    source = Path('.research/experiments/modulated_triangle_2026-10-23')
    pilot = json.loads((source / 'pilot.json').read_text())
    verified = json.loads((source / 'verification.json').read_text())
    assert pilot['status'] == verified['status'] == 'PASS'
    Q = pilot['Q']
    old_A = pilot['A']
    assert old_A == sorted(set(old_A)) and min(old_A) > 0
    assert max(old_A) < Q and Q == verified['Q'] == 65536
    A = sorted(old_A + [Q])
    S = set(A) | {-a for a in A}
    B = sorted(s for s in S if s-Q in S and s+Q not in S)
    assert B and all(0 < s < Q for s in B)
    assert B == sorted(set(A) & {Q-a for a in A})
    assert set(B) == {Q-s for s in B}
    assert 2*sum(B) == Q*len(B)
    assert not (set(B) & {s+Q for s in B})

    # Method1: ordered boundary-pair formula; int64 operations are exact.
    # The worst possible absolute total is <=2*Q^2, far below 2^63.
    assert 2*Q*Q < 2**63
    occupied = np.zeros(Q+1, dtype=np.int64)
    occupied[A] = 1
    b_array = np.array(B, dtype=np.int64)
    H_pairs = 0
    for s in B:
        distance = np.abs(b_array-s)
        kernel = 2*occupied[distance] - occupied[Q-distance]
        kernel[distance == 0] = -2
        H_pairs += int(kernel.sum())

    # Method2: full q=(1-z^Q)F_B, with exact FLINT integer multiplication.
    # Coefficient degree+d of q(z)z^degree*q(z^-1) is its correlation r(d).
    degree = max(B)+Q
    coefficients = [0]*(degree+1)
    for s in B:
        coefficients[s] = 1
        coefficients[s+Q] = -1
    q = flint.fmpz_poly(coefficients)
    correlations = q * flint.fmpz_poly(coefficients[::-1])
    norm = int(correlations[degree])
    coupling = sum(coefficients[s] for s in A)
    H_full = 2*sum(int(correlations[degree+a]) for a in A)
    assert norm == 2*len(B) and coupling == len(B)
    assert H_full == H_pairs and H_full > 0

    old_M_upper = Fraction(verified['second_all_circle_certificate']['M_upper_rational'])
    assert old_M_upper == Fraction(75623, 180)
    M_upper = old_M_upper+1
    K_upper = 2*M_upper
    ratio_lower = Fraction(H_full, len(B))/K_upper
    assert ratio_lower > 15
    result = dict(
        status='PASS', host=socket.gethostname(), elapsed_seconds=time.monotonic()-started,
        Q=Q, t=Q, n=len(A), maxA=max(A), added_frequency=Q,
        source_pilot=str(source/'pilot.json'), source_verification=str(source/'verification.json'),
        source_pilot_sha256=hashlib.sha256((source/'pilot.json').read_bytes()).hexdigest(),
        source_verification_sha256=hashlib.sha256((source/'verification.json').read_bytes()).hexdigest(),
        A_sha256=digest(A), B_size=len(B), B_sha256=digest(B),
        endpoint_first_moment=sum(B), coupling=coupling, squared_norm=norm,
        H_exact_integer=H_full, exact_pair_energy=H_pairs,
        H_methods=['integer boundary-pair kernel', 'full polynomial exact autocorrelation'],
        inherited_all_circle_M_upper=str(old_M_upper),
        all_circle_M_upper=str(M_upper), all_circle_K_upper=str(K_upper),
        all_circle_bound_method='Previously certified M plus1 for adding cos(Q*x)',
        H_over_actual_K_B_lower_bound=str(ratio_lower),
        asymptotic_selection_implemented=False,
        qualification='A deterministic modification of the saved pilot, not a new search. '
        'The all-circle bound is inherited from its previously checked certificate. '
        'Exact energies refute constant15 in H<=C*K*|B|. This is not a Chowla counterexample.'
    )
    destination = Path('.research/experiments/ordered_boundary_2026-10-23')
    destination.mkdir(parents=True, exist_ok=True)
    (destination/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
