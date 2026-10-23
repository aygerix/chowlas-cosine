"""One predeclared adversary to the full-negative P2 strengthening.

Use an already saved n56 Boolean support. No support optimization,
new grid or full-space approximation is involved. All signs are balls;
the original all-circle low-M premise is rechecked by exact Sturm.
"""
from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path
import socket


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import flint
    from cstar_zero_reciprocal import ball, bracket
    from cstar_resolvent_verify import check_upper
    flint.ctx.prec = 384
    source=Path('.research/experiments/boolean_projection_2026-10-21/results.json')
    data=json.loads(source.read_text())
    row=next(r for r in data['cases'] if r['n']==56)
    A=row['A']
    n,D=len(A),max(A)
    assert A==sorted(set(A)) and min(A)>0 and n==56 and D==87
    M_upper=Q(row['candidate_certificate']['M_upper'])
    assert M_upper*M_upper<n
    sturm_chain_length=check_upper(A,M_upper)
    lam=2*flint.arb(n).sqrt()
    p=[1/lam]
    q=[1/(lam*lam)]
    for j in range(1,2*D+1):
        p.append(-sum((p[j-a] for a in A if a<=j),flint.arb(0))/lam)
        q.append((p[j]-sum((q[j-a] for a in A if a<=j),flint.arb(0)))/lam)
    T=sum((q[a] for a in A),flint.arb(0))
    T2=sum((sum((p[j]*p[a-j] for j in range(a+1)),flint.arb(0))
            for a in A),flint.arb(0))
    assert abs(T-T2)<flint.arb('1e-90')
    C1=sum((p[a] for a in A),flint.arb(0))
    sums=Counter(a+b for a in A for b in A)
    t=sum(sums[a] for a in A)
    C2=sum((count*p[j] for j,count in sums.items()),flint.arb(0))
    y=-lam*T
    k=[lam*sum((q[a-j] for a in A if a>=j),flint.arb(0))
       for j in range(1,D+1)]
    # Independent reversal/product implementation includes every row.
    reverse=flint.arb_poly([int(D-r in A) for r in range(D)])
    product=reverse*flint.arb_poly(q[:D])
    assert all(abs(k[j-1]-lam*product[D-j])<flint.arb('1e-90')
               for j in range(1,D+1))
    Nminus=sum((v*v for v in k),flint.arb(0))
    Gminus=(y*y+Nminus+2*y)/5
    criterion=2*t*(-Gminus/lam-T/2)-C2*C2
    v=(1+y)/lam+lam*p[D]
    allpass_floor=(v*v+p[D]*p[D])/(1-1/(lam*lam))
    corrected_criterion=criterion-2*t*allpass_floor/(5*lam)
    equivalent_margin=Nminus+5*lam*C2*C2/(2*t)-y/2+y*y
    assert abs(criterion+2*t*equivalent_margin/(5*lam))<flint.arb('1e-90')
    prior_path=Path('.research/experiments/zero_reciprocal_2026-10-21/results.json')
    prior=next(c for c in json.loads(prior_path.read_text())['cases'] if c['n']==n)
    assert prior['A']==A and prior['lambda_exact']=='2sqrt(n)'
    Hlo,Hhi=map(Q,prior['H_bracket'])
    assert Hhi<0
    phi_lo,phi_hi=2*t*ball(Hlo)-C2*C2,2*t*ball(Hhi)-C2*C2
    assert phi_hi<0
    out=dict(status='PASS',host=socket.gethostname(),precision_bits=384,
        source=str(source),A=A,n=n,D=D,t_exact=t,M_upper_exact=str(M_upper),
        all_circle_Sturm_chain_length=sturm_chain_length,
        actual_lowM_exact=True,
        intervals={name:bracket(value,value) for name,value in
            [('C1',C1),('C2',C2),('T',T),('y',y),('Nminus',Nminus),
             ('Gminus',Gminus),('Psi_minus',criterion),
             ('allpass_v',v),('p_D',p[D]),('allpass_positive_phase_floor',allpass_floor),
             ('allpass_corrected_Psi',corrected_criterion),
             ('equivalent_finite_inequality_margin',equivalent_margin)]},
        full_negative_strengthening_refuted=bool(criterion>0),
        full_negative_strengthening_holds_on_this_support=bool(criterion<0),
        allpass_corrected_strengthening_refuted=bool(corrected_criterion>0),
        allpass_corrected_strengthening_holds=bool(corrected_criterion<0),
        independent_inverse_square_and_negative_block_checks=True,
        prior_full_inverse_certificate=str(prior_path),
        prior_full_inverse_support_matches=True,
        original_P2_violation_bracket=bracket(phi_lo,phi_hi),
        original_P2_holds=True,
        qualification=('One existing actual-lowM Boolean support. A positive '
            'Psi_minus refutes the stronger finite-projection closure only; '
            'it does not refute original P2 or Chowla.'))
    dest=Path('.research/experiments/P2_aggregation_2026-10-23/n56.json')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',artifact=str(dest),
        Psi_minus_ball=str(criterion),
        strengthening_refuted=out['full_negative_strengthening_refuted'],
        allpass_corrected_Psi_ball=str(corrected_criterion),
        allpass_corrected_refuted=out['allpass_corrected_strengthening_refuted'],
        Nminus_ball=str(Nminus),y_ball=str(y))),flush=True)


if __name__=='__main__':
    main()
