"""Exact finite checks for Boolean boundary and whole-space residual notes.

These checks verify algebraic identities and finite premises. The uniform
asymptotic notch obstruction is a paper proof, not a finite search claim.
Run only on Dirichlet through src/dirun.sh.
"""
from collections import Counter
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import random
import socket

import flint
from singer import singer, is_perfect_difference_set
from cstar_projected_verify import independent_square_moments


def root_checks():
    rng = random.Random(20261021)
    rows = []
    for k in (4, 5, 6, 8, 10, 12):
        base = k + 1
        B = [base**j for j in range(k)]
        S = {b-c for b in B for c in B if b != c}
        m = len(S)
        assert m == k*(k-1)
        overlap = Counter(a-b for a in S for b in S)
        maximum = max(v for h, v in overlap.items() if h)
        assert maximum == 2*(k-2)
        for t in range(m+1):
            assert sum(max(v-(m-t), 0) for v in overlap.values()) <= t*t
        fourth = sum(v*v for v in overlap.values())
        assert fourth <= 10*k**4
        L1_squared_lower = F(m**3, fourth)
        assert L1_squared_lower > F(k*k, 25)
        variance_lower = L1_squared_lower**2/(16*m)
        leakage_lower = (m-maximum)*variance_lower
        assert leakage_lower >= F(k**4, 20000)
        # Independently count the sine/root-space quadratic form, using
        # integer imaginary coefficients i*c_s, with c_-s=-c_s.
        T = [[0]*k for _ in range(k)]
        for i in range(k):
            for j in range(i):
                T[i][j] = rng.randrange(-3, 4)
                T[j][i] = -T[i][j]
        c = {B[i]-B[j]: T[i][j] for i in range(k)
             for j in range(k) if i != j and T[i][j]}
        Q = sum(v*v for v in c.values())
        H = -sum(v*u for s, v in c.items() for t, u in c.items()
                 if -s-t in S)
        row_norm = sum(sum(row)**2 for row in T)
        assert H == 2*row_norm-2*Q
        rows.append(dict(k=k, base=base, m=m, max_nonzero_overlap=maximum,
                         fourth_moment=fourth, L1_squared_lower=str(L1_squared_lower),
                         variance_lower=str(variance_lower),
                         leakage_lower=str(leakage_lower),
                         sine_Q=Q, sine_H=H, matrix_row_norm=row_norm,
                         all_popular_difference_thresholds_verified=True))
    return rows


def differences(B):
    A = {b-c for b in B for c in B if b > c}
    assert len(A) == len(B)*(len(B)-1)//2
    return A


def notch_checks():
    rows = []
    for prime in (5, 7, 11):
        B, Q0 = singer(prime)
        assert is_perfect_difference_set(B, Q0)
        k = len(B)
        h = max(t for t in range(1, k)
                if (k+t)**2 <= 2*(k*(k-1)+t*(t-1)))
        subset = sorted(B)[:h]
        X = Q0-1
        L = 6*X+1
        A1, A2 = differences(B), differences(subset)
        A = A1 | {L*a for a in A2}
        assert len(A) == len(A1)+len(A2)
        S = A | {-a for a in A}
        m = len(S)
        assert (k+h)**2 <= 2*m
        max_a = max(A)
        d = [0]*(2*max_a+1)
        for a in S:
            d[max_a+a] = 1
        cube = flint.fmpz_poly(d)**3
        def cubic(j):
            return int(cube[3*max_a+j]) if abs(j) <= 3*max_a else 0
        s1 = A1 | {-a for a in A1}
        s2 = A2 | {-a for a in A2}
        square1 = Counter(a+b for a in s1 for b in s1)
        square2 = Counter(a+b for a in s2 for b in s2)
        def small_cube(Si, square, j):
            return sum(square[j-a] for a in Si)
        T1, T2 = small_cube(s1, square1, 0), small_cube(s2, square2, 0)
        assert cubic(0) == T1+T2
        for ki, Ti in ((k, T1), (h, T2)):
            assert Ti >= F(ki**6, 3*Q0)-4*ki**3+3*ki**2
        # Exhaust every potentially nonconstant cubic coefficient. All
        # larger shifts have T_z=T_2z=1_A(z)=r_S(z)=0 exactly.
        minimum_H = None
        minimizer = None
        for z in range(1, 3*max_a+1):
            Tz = cubic(z)
            if z <= 3*X:
                assert Tz == small_cube(s1, square1, z)+3*len(s2)*int(z in s1)
            elif z % L == 0:
                b = z//L
                assert Tz == small_cube(s2, square2, b)+3*len(s1)*int(b in s2)
            else:
                assert Tz <= 3*m
            r = sum(int(a-z in S) for a in S) if z <= 2*max_a else 0
            a = m-r
            H = F(3*cubic(0), 2)-2*Tz+F(cubic(2*z), 2)+2*int(z in A)*a
            if minimum_H is None or H < minimum_H:
                minimum_H, minimizer = H, z
        paper_lower = F(3*min(T1, T2), 2)-(4*k+6)*m
        assert minimum_H >= paper_lower
        selected = {1, X, 3*X, 3*X+1, L, L+1, 2*L, minimizer, 3*max_a+1}
        direct = []
        for z in sorted(selected):
            g = Counter({s: 2 for s in S})
            for s in S:
                g[s+z] -= 1
                g[s-z] -= 1
            g[0] += 2*int(z in A)
            g = {s: v for s, v in g.items() if v}
            assert g.get(0, 0) == 0
            a = F(sum(v for s, v in g.items() if -s in S), 2)
            q = F(sum(v*v for v in g.values()), 4)
            H = F(sum(v*u for s, v in g.items() for t, u in g.items()
                      if -s-t in S), 4)
            r = sum(int(s-z in S) for s in S)
            r2 = sum(int(s-2*z in S) for s in S)
            assert a == m-r
            assert q == 2*a-F(m-r2, 2)-int(z in A)
            assert H == F(3*cubic(0), 2)-2*cubic(z)+F(cubic(2*z), 2)+2*int(z in A)*a
            assert q <= 2*a
            direct.append(dict(shift=z, a=str(a), Q=str(q), H=str(H)))
        rows.append(dict(prime=prime, full_B=B, subset_B=subset, k=k, h=h,
                         modulus=Q0, dilation=L, n=len(A), A=sorted(A),
                         K_upper=k+h, lowK_exact=True, cubic_0=[T1, T2],
                         all_shifts_through=3*max_a,
                         minimum_single_notch_H=str(minimum_H), minimizer=minimizer,
                         paper_H_lower=str(paper_lower), direct_checks=direct,
                         qualification='Finite all-shift algebra/control; asymptotic positive cost is proved separately.'))
    return rows


def analytic_inverse_controls():
    flint.ctx.prec = 160
    I = 1/(2*flint.arb(3).sqrt())
    d = [F(1), F(4)]
    for j in range(2, 26):
        d.append(4*d[-1]-d[-2])
    rows = []
    for B in (1, 2, 4, 8, 12):
        IB = d[B]*d[B]/d[2*B+1]
        Ib = flint.arb(IB.numerator)/IB.denominator
        assert I-Ib >= 0 and I-Ib <= flint.arb(1)/(B+1)
        N = B+1
        trace = sum(d[j]*d[N-1-j]/d[N] for j in range(N))
        tr = flint.arb(trace.numerator)/trace.denominator
        assert N*I-tr >= 0 and N*I-tr <= 1
        assert trace <= N*IB
        rows.append(dict(B=B, I_B=str(IB), trace_inverse=str(trace),
                         rank_boundary_rate_verified=True))
    # Exact finite optimizer at B2. Interior residual is zero; the
    # exterior one alone separates finite and full-space leverage.
    v = [F(8, 15), F(-2, 15)]
    finite = F(8, 15)
    full = 4-2*flint.arb(3).sqrt()
    physical_r_squared = F(2, 225)
    upper = finite+physical_r_squared/2
    assert flint.arb(finite.numerator)/finite.denominator < full
    assert full < flint.arb(upper.numerator)/upper.denominator
    assert upper == F(121, 225)
    return dict(singleton_exact_optimizer=list(map(str, v)),
                finite_J=str(finite), full_J='4-2*sqrt(3)',
                physical_residual_squared=str(physical_r_squared),
                full_upper=str(upper), boundary_rate_controls=rows)


def inheritance_check():
    source_path = '.research/experiments/l25_2026-10-21/projected_cpu_verification.json'
    row = next(r for r in json.loads(Path(source_path).read_text())['cases']
               if r['label'].endswith('p31'))
    original = next(r for r in json.loads(Path(
        '.research/experiments/l25_2026-10-21/probe.json').read_text())['cases']
        if r['label'].endswith('p31'))
    Bset = sorted(original['metadata']['B'])
    Q0 = original['metadata']['modulus']
    k = len(Bset)
    assert is_perfect_difference_set(Bset, Q0)
    A0 = sorted(differences(Bset))
    assert A0 == row['A']
    h = max(t for t in range(1, k)
            if (k+t)**2 <= 2*(k*(k-1)+t*(t-1)))
    A2 = sorted(differences(Bset[:h]))
    L = 6*(Q0-1)+1
    tail = [L*a for a in A2]
    A = sorted(A0+tail)
    cert = row['certificate']
    nums, den = cert['positive_numerators'], cert['denominator']
    band = len(nums)
    assert min(tail) > 2*band and len(set(A)) == len(A)
    assert (k+h)**2 <= 4*len(A)
    # This independent signed Python product decodes every new A frequency;
    # all the far-block coefficients of q² are exactly zero.
    Q, H = independent_square_moments(A, nums)
    assert Q == cert['norm_numerator'] and H == cert['energy_numerator']
    a_raw = 2*sum(nums[a-1] for a in A if a <= band)
    assert a_raw == len(A0)*den
    K0 = 2*F(cert['global_M_lower'])
    assert Q*K0*K0+H*K0-a_raw*a_raw < 0
    assert H < 0
    n = len(A)
    # Test additive closure with a second, independently specified witness
    # q1=D_A2/2. This checks cross-term cancellation; it does not assert a
    # uniform mixed-cost theorem for that elementary second witness.
    qnums = {j: v for j, v in enumerate(nums, 1) if v}
    qnums.update({-j: v for j, v in enumerate(nums, 1) if v})
    assert den % 2 == 0
    for a in tail:
        assert a not in qnums and -a not in qnums
        qnums[a] = qnums[-a] = den//2
    total_S = set(A) | {-a for a in A}
    second_S = set(A2) | {-a for a in A2}
    closure_a = sum(v for s, v in qnums.items() if -s in total_S)
    closure_Q = sum(v*v for v in qnums.values())
    closure_H = 2*sum(sum(v*qnums.get(a-s, 0) for s, v in qnums.items()) for a in A)
    second_cubic = sum(int(-s-t in second_S) for s in second_S for t in second_S)
    assert closure_a == n*den
    assert closure_Q == Q+len(A2)*den*den//2
    assert closure_H == H+second_cubic*den*den//4
    return dict(host=socket.gethostname(), A=A, n=n, block_sizes=[k, h],
                low_block_n=len(A0), modulus=Q0, dilation=L,
                K_upper=k+h, lowK_exact=True, witness_band=band,
                minimum_tail_frequency=min(tail),
                source_certificate=source_path, source_label=row['label'],
                numerator_sha256=hashlib.sha256(json.dumps(nums).encode()).hexdigest(),
                denominator=den, inherited_a=str(F(a_raw, den)),
                inherited_Q=str(F(Q, den*den)), inherited_H=str(F(H, den*den)),
                normalized_Q_over_n=str(F(Q*n, a_raw*a_raw)),
                normalized_H=str(F(H*n*n, a_raw*a_raw)),
                global_M_lower=cert['global_M_lower'],
                additive_closure=dict(a=n, Q=str(F(closure_Q, den*den)),
                    H=str(F(closure_H, den*den)), second_cubic=second_cubic,
                    direct_signed_convolution_match=True,
                    qualification='Exact additive a,Q,H identity; no uniform bound on the elementary second witness is asserted.'),
                independent_Python_convolution_match=True,
                qualification='Same broader witness retains exact a,Q,H across a frequency gap; no single-notch success or universal theorem is inferred.')


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    parser = argparse.ArgumentParser()
    parser.add_argument('--inheritance-only', action='store_true')
    args = parser.parse_args()
    if args.inheritance_only:
        output = inheritance_check()
        path = Path('.research/experiments/boolean_boundary_2026-10-21/inheritance.json')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(output, indent=2)+'\n')
        print(json.dumps({k: output[k] for k in ('n', 'block_sizes', 'witness_band',
            'inherited_a', 'normalized_Q_over_n', 'global_M_lower')}), flush=True)
        print(json.dumps(dict(status='PASS', output=str(path))), flush=True)
        return
    output = dict(host=socket.gethostname(), analytic_inverse=analytic_inverse_controls(),
                  root_checks=root_checks(), notch_checks=notch_checks())
    path = Path('.research/experiments/boolean_boundary_2026-10-21/results.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', roots=len(output['root_checks']),
                         notch_cases=len(output['notch_checks']), output=str(path))), flush=True)


if __name__ == '__main__':
    main()
