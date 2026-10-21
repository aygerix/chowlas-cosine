"""Exact finite analytic square-root witnesses, not a new flatness proof.

Only a few analytic/control inputs are used. Fractions verify every formal
coefficient; FLINT and separate sparse products verify the achieved witness.
All mathematical computation runs on Dirichlet through src/dirun.sh.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket

import flint
from singer import singer, is_perfect_difference_set


def enclosure(value, scale=10**9):
    low = value.numerator*scale//value.denominator
    return [str(F(low, scale)), str(F(low+1, scale))]


def differences(B):
    A = {b-c for b in B for c in B if b > c}
    assert len(A) == len(B)*(len(B)-1)//2
    return A


def interlaced_control(prime):
    B1, modulus = singer(prime)
    assert is_perfect_difference_set(B1, modulus)
    k = len(B1)
    h = max(t for t in range(1, k)
            if (k+t)**2 <= 2*(k*(k-1)+t*(t-1)))
    A1 = differences(B1)
    B2 = [0]
    used = set()
    for b in range(1, 2*modulus):
        new = {b-c for c in B2}
        if len(new) == len(B2) and not new.intersection(A1 | used):
            B2.append(b)
            used.update(new)
            if len(B2) == h:
                break
    assert len(B2) == h
    A2 = differences(B2)
    assert A1.isdisjoint(A2)
    A = sorted(A1 | A2)
    assert F((k+h)**2, 4) <= len(A)
    # The two supports are in overlapping frequency ranges and have actual
    # mixed additive relations; the separated closure lemma is unavailable.
    assert min(A2) < max(A1)
    S1, S2 = A1 | {-a for a in A1}, A2 | {-a for a in A2}
    cross = sum(int(-a-b in S2) for a in S1 for b in S1)
    cross += sum(int(-a-b in S1) for a in S2 for b in S2)
    assert cross > 0
    return dict(label=f'interlaced_two_squares_p{prime}', A=A,
                M_upper=F(k+h, 2),
                metadata=dict(B1=B1, B2=B2, modulus=modulus,
                              mixed_triangle_count=cross,
                              exact_disjoint_differences=True,
                              upper_proof='Two exact difference squares, with disjoint supports.'))


def certificate(A, M_upper, label, metadata=None):
    n, X = len(A), max(A)
    assert M_upper*M_upper <= n
    lam = 2*math.isqrt(n)
    if lam*lam < 4*n:
        lam += 2
    assert lam >= 2*M_upper and lam*lam >= 4*n
    B = 2*X-1
    support = set(A)
    # h=2sqrt(lambda)(sqrt(lambda+F_A)-sqrt(lambda)) obeys
    # h+h²/(4lambda)=F_A. These exact Taylor coefficients determine q.
    h = [F(0)]*(B+1)
    for j in range(1, B+1):
        h[j] = F(int(j in support))-sum((h[u]*h[j-u] for u in range(1, j)), F(0))/(4*lam)
    for j in range(1, B+1):
        assert h[j]+sum((h[u]*h[j-u] for u in range(1, j)), F(0))/(4*lam) == int(j in support)
    v = [h[j]*(1 if j <= X else F(2*X-j, X)) for j in range(1, B+1)]
    a = sum(v[j-1] for j in A)
    assert a == sum(h[j] for j in A)
    den = math.lcm(*(t.denominator for t in v))
    nums = [int(t*den) for t in v]
    z = nums[::-1]+[0]+nums
    square = flint.fmpz_poly(z)**2
    Qraw = sum(t*t for t in z)
    Hraw = 2*sum(int(square[2*B+j]) for j in A)
    assert int(square[2*B]) == Qraw
    sparse = {j: t for j, t in enumerate(nums, 1) if t}
    sparse.update({-j: t for j, t in enumerate(nums, 1) if t})
    S = support | {-j for j in A}
    independently_counted_H = sum(t*u for j, t in sparse.items()
                                  for k, u in sparse.items() if -j-k in S)
    assert independently_counted_H == Hraw
    Q, H = F(Qraw, 4*den*den), F(Hraw, 4*den*den)
    assert Q <= 2*n
    assert H*H <= 2592*lam*lam*n*n
    assert a > 0
    # Independent exact achieved all-circle lower certificate. The global
    # upper bound supplies the right endpoint; no sampled minimum enters.
    left, right = F(0), 2*M_upper
    def phi(K):
        return Q*K*K+H*K-a*a
    assert phi(left) < 0 and phi(right) >= 0
    for _ in range(40):
        mid = (left+right)/2
        if phi(mid) < 0:
            left = mid
        else:
            right = mid
    normalized_Q = Q*n*n/(a*a)
    normalized_H = H*n*n/(a*a)
    return dict(label=label, A=A, n=n, X=X, band=B, lambda_exact=lam,
                M_upper=str(M_upper), lowM_certified=True, metadata=metadata,
                cosine_numerators=nums, cosine_denominator=den,
                a_exact=str(a), a_over_n=enclosure(a/n),
                Q_exact=str(Q), H_exact=str(H),
                normalized_Q_over_n=enclosure(normalized_Q/n),
                normalized_H_exact=str(normalized_H),
                achieved_M_lower=str(left/2),
                achieved_M_bracket=list(map(str, (left/2, right/2))),
                proposed_half_coupling_holds=(2*a >= n),
                recurrence_verified=True, independent_sparse_H_match=True,
                uniform_norm_cost_bounds_verified=True,
                qualification='Exact finite achieved VP square-root witness; half-coupling is tested only on these inputs, not proved universally.')


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    old = json.loads(Path('.research/experiments/resolvent_2026-10-20/results.json').read_text())
    inputs = [dict(label='singleton', A=[1], M_upper=F(1))]
    inputs += [interlaced_control(p) for p in (5, 7)]
    inputs.append(dict(label='saved_n50', A=old['actual'], M_upper=F(old['global_M_upper']),
                       metadata=dict(upper_source='resolvent_2026-10-20/results.json; previously checked Sturm certificate, not rerun.')))
    output = dict(host=socket.gethostname(), cases=[])
    path = Path('.research/experiments/analytic_sqrt_2026-10-21/results.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    for inp in inputs:
        row = certificate(**inp)
        output['cases'].append(row)
        path.write_text(json.dumps(output, indent=2)+'\n')
        print(json.dumps({key: row[key] for key in ('label', 'n', 'X', 'a_over_n',
            'normalized_Q_over_n', 'achieved_M_lower', 'proposed_half_coupling_holds')}), flush=True)
    print(json.dumps(dict(status='PASS', output=str(path))), flush=True)


if __name__ == '__main__':
    main()
