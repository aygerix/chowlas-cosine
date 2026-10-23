"""One exact weighted falsifier of both reciprocal parity planes.

This is not a Boolean support and does not refute P2 or Chowla.
The finite polynomial has coefficients (99/101)^(a-1), 1<=a<=1024.
Both its energy calibration and its all-circle comparison are exact.
Research computation runs on Dirichlet, without grids or solvers.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import platform
import socket


def saved(q):
    return dict(exact=str(q), decimal=float(q))


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    u, r, N = Q(1, 10), Q(99, 101), 1024
    lam = Q(101, 10)
    alpha = 1+4*u-u*u
    beta = (1+2*u)*(2-u)
    g = u/beta
    C1 = -u/alpha
    c = -u*(1-u-u*u)/(alpha*alpha)
    tau = (1-u*u)/(16*u)
    h = u*u*(1-3*u)*(3+u)/(2*alpha*alpha*beta)
    he = -2*(g+C1)-h
    odd = [[tau/2, c/2], [c/2, h]]
    even = [[3*tau/2, c/2-C1-Q(1, 4)],
            [c/2-C1-Q(1, 4), he]]

    # Independent direct closed forms, before the u-simplification.
    delta = 1/lam
    s = r-delta
    assert g == delta*delta/(1-s*s)
    assert C1 == -delta*delta/(1-r*s)
    assert tau == delta**3*r/(1-r*r)**2
    assert c == -delta**3*s/(1-r*s)**2
    assert h == -g+delta*delta/(1-r*s)-delta**3*r/(2*(1-r*s)**2)
    assert lam*lam == 4/(1-r*r)

    # F_N differs from z/(1-rz) by at most r^N/(1-r) everywhere.
    # lambda_N=lambda*sqrt(1-r^(2N)); 1-sqrt(1-x)<=x.
    eps_F, eps_lam = Q(1, 10**6), Q(1, 10**12)
    assert r**N/(1-r) < eps_F
    assert lam*r**(2*N) < eps_lam
    assert lam*lam*(1-r**(2*N)) > 100
    M_upper = 1/(1+r)+eps_F
    assert M_upper < 1
    # Both finite and infinite Re(lambda+F)>9, lambda_N>10,
    # |F/lambda|<=6, |lambda/(lambda+F)-1|<=1.
    assert lam-eps_lam-M_upper > 9
    assert Q(1, 1)/(1-r)/10 < 6

    e1 = eps_F/10+eps_lam/2
    e2 = eps_lam/9+lam*(eps_F+eps_lam)/81
    errors = [[216*e1, 24*e1+72*e2],
              [24*e1+72*e2, 2*e1+24*e2]]

    certified = {}
    for name, matrix in [('odd', odd), ('even', even)]:
        A, B, D = matrix[0][0], matrix[0][1], matrix[1][1]
        a_lo, d_lo = A-errors[0][0], D-errors[1][1]
        det_lo = a_lo*d_lo-(abs(B)+errors[0][1])**2
        assert a_lo > 0 and d_lo > 0 and det_lo > 0
        certified[name] = dict(
            infinite_energy_matrix=[[saved(x) for x in row] for row in matrix],
            finite_first_diagonal_lower=saved(a_lo),
            finite_second_diagonal_lower=saved(d_lo),
            finite_determinant_lower=saved(det_lo),
            finite_entire_plane_positive_definite=True)

    out = dict(status='PASS', host=socket.gethostname(),
        python=platform.python_version(),
        polynomial=dict(N=N, r=str(r), coefficient_a='(99/101)^(a-1)',
            a_inclusive=[1,N], coefficients_in_0_1=True, Boolean=False,
            lambda_exact='(101/10)*sqrt(1-(99/101)^2048)',
            coefficient_energy_exact='(10201/400)*(1-(99/101)^2048)'),
        all_circle_M_upper=saved(M_upper),
        calibration='lambda=2*sqrt(sum of squared coefficients), not occupied count',
        infinite_invariants={name:saved(value) for name,value in
            [('g',g),('C1',C1),('C2_over_lambda',c),
             ('t_over_lambda_cubed',tau),('lambda_Hodd',h),('lambda_Heven',he)]},
        tail_certificate=dict(
            function_sup_error_upper=str(eps_F),
            lambda_error_upper=str(eps_lam),
            checks='r^1024/(1-r)<1e-6; (101/10)*r^2048<1e-12; lambda_N>10',
            inverse_real_margin_lower='9',
            normalized_first_basis_error=str(e1),
            normalized_second_basis_error=str(e2),
            energy_entry_errors=[[saved(x) for x in row] for row in errors]),
        normalized_basis=dict(odd=['Im(F)/lambda','lambda*Im(p)'],
            even=['Re(F)/lambda','lambda*Re(p)-1'],
            weight='2*Re(F)/lambda',p='1/(lambda+F)'),
        certificates=certified,
        qualification=('Exact rational tail inequalities and positive determinants prove '
            'the full finite weighted reciprocal parity planes are positive definite. '
            'No quadrature, minimum grid or unchecked solver is used. '
            'The coefficients are not Boolean; P2 and Chowla are not refuted.'))
    dest=Path('.research/experiments/P2_geometric_2026-10-23/results.json')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS', artifact=str(dest),
        all_circle_M_upper=float(M_upper),
        odd_determinant_lower=float(Q(certified['odd']['finite_determinant_lower']['exact'])),
        even_determinant_lower=float(Q(certified['even']['finite_determinant_lower']['exact'])),
        Boolean=False)),flush=True)


if __name__ == '__main__':
    main()
