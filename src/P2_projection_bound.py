"""Test one stronger finite-coefficient P2 criterion on a saved Boolean set.

No new support search or numerical minimum is used. Rigorous balls
certify finite Taylor recurrences; a separate exact polynomial residual
then encloses the complete inverse norm on the same support.
"""
from collections import Counter
from fractions import Fraction as Q
import json
from math import isqrt
from pathlib import Path
import socket


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    from cstar_zero_reciprocal import ball, bracket, one
    flint.ctx.prec = 384
    source = Path('.research/experiments/P2_alias_2026-10-23/results.json')
    data = json.loads(source.read_text())
    row = next(r for r in data['evaluated_cases'] if r['L'] == 36)
    A, n, D = row['A'], row['n'], row['X']
    DA = data['fixed_family']['U_differences']
    DB = [36*a for a in data['fixed_family']['V_differences']]
    for points, expected in [(data['fixed_family']['U'], DA),
                             (data['fixed_family']['V'], [a//36 for a in DB])]:
        raw = [b-a for i,a in enumerate(points) for b in points[i+1:]]
        assert len(raw) == len(set(raw)) and sorted(raw) == expected
    assert not set(DA) & set(DB)
    assert sorted(DA+DB) == A and len(A) == len(set(A)) == 76
    assert Q(17,2)**2 < n
    lam = 2*flint.arb(n).sqrt()
    p, p2 = [1/lam], [1/(lam*lam)]
    for j in range(1, 2*D+1):
        p.append(-sum((p[j-a] for a in A if a<=j), flint.arb(0))/lam)
        p2.append((p[j]-sum((p2[j-a] for a in A if a<=j), flint.arb(0)))/lam)
    C1 = sum((p[a] for a in A), flint.arb(0))
    T = sum((p2[a] for a in A), flint.arb(0))
    T_cross = sum((sum((p[j]*p[a-j] for j in range(a+1)), flint.arb(0))
                   for a in A), flint.arb(0))
    assert abs(T-T_cross) < flint.arb('1e-90')
    sums = Counter(a+b for a in A for b in A)
    t = sum(sums[a] for a in A)
    C2 = sum((count*p[j] for j,count in sums.items()), flint.arb(0))
    y = -lam*T
    G3 = (y*y+4*(C1+y)**2+2*y)/5
    criterion = 2*t*(-G3/lam-T/2)-C2*C2
    negative_coefficients = [lam*sum((p2[a-j] for a in A if a>=j), flint.arb(0))
                             for j in range(1,D+1)]
    negative_energy = sum((k*k for k in negative_coefficients), flint.arb(0))
    Gminus = (y*y+negative_energy+2*y)/5
    minus_criterion = 2*t*(-Gminus/lam-T/2)-C2*C2
    intervals = {name:bracket(value,value) for name,value in
        [('C1',C1),('C2',C2),('T',T),('y',y),('G3',G3),
         ('finite_projection_criterion',criterion),
         ('full_negative_block_energy',negative_energy),('Gminus',Gminus),
         ('full_negative_projection_criterion',minus_criterion)]}
    out = dict(status='PASS', host=socket.gethostname(), precision_bits=384,
        source=str(source), L=36, A=A, n=n, max_A=D, t_exact=t,
        actual_lowM_certificate='Two disjoint Sidon difference squares: M<=17/2<sqrt(76)',
        lambda_exact='2sqrt(76)', intervals=intervals,
        finite_projection_criterion_refuted=bool(criterion > 0),
        criterion_succeeds_on_this_support=bool(criterion < 0),
        full_negative_projection_criterion_refuted=bool(minus_criterion > 0),
        full_negative_projection_criterion_succeeds=bool(minus_criterion < 0),
        inverse_square_recurrence_check_ball=str(T-T_cross),
        qualification=('The tested condition uses the rigorous lower bound g>=G3 '
            'instead of the full inverse norm. It is stronger than P2. '
            'A positive result refutes that stronger condition only; it does '
            'not establish a positive Rayleigh determinant or refute P2.'))
    # On the SAME falsifier, check the complete inverse by an exact
    # polynomial residual. FFT only proposes the finite approximation.
    exact = one(A, Q(17,2), 'P2_projection_L36', band_multiple=32)
    S_P = Q(exact['S_P_exact'])
    S_error = Q(exact['S_error_upper'])
    # Reconstruct the residual by sparse Python-integer shifts,
    # independently of the producer's FLINT polynomial product.
    den = exact['finite_denominator']
    nums = exact['finite_sine_numerators']
    v2 = S_P*den*den
    assert v2.denominator == 1
    constant_squared = int(v2)-sum(v*v for v in nums)
    constant = isqrt(constant_squared)
    assert constant*constant == constant_squared
    nums = [constant]+nums
    residual_integer = [0]*(len(nums)+D)
    residual_integer[0] = -den
    for a in A:
        for j,v in enumerate(nums):
            residual_integer[a+j] += v
    u2 = sum(v*v for v in residual_integer)
    uv = sum(residual_integer[j]*v for j,v in enumerate(nums))
    residual2 = (flint.arb(u2+4*n*int(v2))+2*lam*uv)/(den*den)
    eps_verified = residual2.sqrt()/(lam-ball(Q(17,2)))
    assert eps_verified < ball(exact['L2_error_upper'])
    assert 2*ball(S_P).sqrt()*eps_verified+eps_verified**2 < ball(S_error)
    glo = lam*lam*ball(S_P-S_error)-1
    ghi = lam*lam*ball(S_P+S_error)-1
    Hlo, Hhi = map(Q,exact['H_bracket'])
    phi_lo = 2*t*ball(Hlo)-C2*C2
    phi_hi = 2*t*ball(Hhi)-C2*C2
    out['full_reciprocal_certificate'] = exact
    out['full_norm_comparison'] = dict(
        g_bracket=bracket(glo,ghi),
        g_minus_G3_bracket=bracket(glo-G3,ghi-G3),
        unprojected_phase_energy_bracket=bracket(5*(glo-G3),5*(ghi-G3)),
        strictly_positive_K_energy_bracket=bracket(5*(glo-Gminus),5*(ghi-Gminus)),
        original_P2_violation_bracket=bracket(phi_lo,phi_hi),
        original_P2_holds_for_this_support=bool(phi_hi < 0),
        original_S0_holds_for_this_support=exact['infinite_energy_negative'],
        independent_sparse_integer_residual_verified=True)
    dest=Path('.research/experiments/P2_projection_2026-10-23/results.json')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS', artifact=str(dest),
        criterion_ball=str(criterion),
        stronger_criterion_refuted=out['finite_projection_criterion_refuted'],
        full_P2_holds=out['full_norm_comparison']['original_P2_holds_for_this_support'],
        full_negative_criterion_ball=str(minus_criterion),
        g_midpoint_approx=float((glo+ghi)/2), G3_approx=float(G3),
        Gminus_approx=float(Gminus),
        unprojected_phase_energy_approx=float(5*((glo+ghi)/2-G3)))),flush=True)


if __name__ == '__main__':
    main()
