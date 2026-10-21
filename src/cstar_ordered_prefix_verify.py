"""Independent scalar verification of prefix witnesses and interval algebra.

No producer import. Build prefix autocorrelations directly, reconstruct
the saved integer polynomial, then count scalar shifts independently of
the producer's sparse moment matrices and numerical Gram reduction.
"""
from collections import Counter
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket


def auto(P):
    r=Counter(a-b for a in P for b in P)
    del r[0]
    return r


def exact(A,poly,nums=None):
    nums=[1]*len(A) if nums is None else nums
    Q=sum(c*c for c in poly.values())
    H=2*sum(c*sum(v*poly.get(w+a,0) for w,v in poly.items()) for a,c in zip(A,nums))
    return Q,H


def verify(row):
    A=row['actual'];nums=row['coefficient_numerators'];den=row['coefficient_denominator']
    assert A==sorted(set(A)) and len(A)==row['n'] and min(A)>0 and max(A)==row['max_A']
    rows=[Counter({0:1})]
    if row.get('include_D_basis_row',True):rows.append(Counter({s:c for a,c in zip(A,nums) for s in [-a,a]}))
    for j in range(1,len(A)+1):
        now=auto([0]+A[:j]);old=auto([0]+A[:j-1]);r=Counter(now)
        for w,c in old.items():r[w]-=c
        rows.append({w:c for w,c in r.items() if c})
    if row['suffix']:
        for j in range(len(A)):
            now=auto([0]+A[j:]);old=auto([0]+A[j+1:]);r=Counter(now)
            for w,c in old.items():r[w]-=c
            rows.append({w:c for w,c in r.items() if c})
    assert len(rows)==len(row['integer_weights'])==row['basis_count']
    poly=Counter()
    for c,r in zip(row['integer_weights'],rows):
        for w,v in r.items():poly[w]+=c*v
    poly={w:c for w,c in poly.items() if c}
    assert poly==dict(row['test_polynomial'])
    assert all(poly.get(-w)==c for w,c in poly.items())
    Q,H=exact(A,poly,nums);assert (Q,H)==(row['norm_numerator'],row['Dnum_energy_numerator'])
    assert H<0 and F(-H,2*Q*den)==F(row['global_M_lower'])
    if 'global_M_upper' in row:assert F(row['global_M_lower'])<=F(row['global_M_upper'])
    dc=poly.get(0,0);Q0=Q-dc*dc
    coupling_num=2*sum(c*poly.get(a,0) for a,c in zip(A,nums))
    H0=H-2*dc*coupling_num
    assert Q0>0
    return dict(label=row['label'],suffix=row['suffix'],integer_scalar_form=True,
                global_M_lower=row['global_M_lower'],Boolean=row['Boolean'],
                mean_zero_Q=Q0,mean_zero_a=str(F(coupling_num,den)),mean_zero_H=str(F(H0,den)),
                coupling_at_Q_equals_n_over_n=abs(coupling_num)/(den*math.sqrt(len(A)*Q0)),
                H_at_Q_equals_n_over_n32=H0/(den*Q0*math.sqrt(len(A))),
                norm_budget_at_a_equals_n_over_n=str(F(Q0*len(A)*den*den,coupling_num**2)) if coupling_num else None)


def interval_identity():
    out=[]
    for m in [1,2,3,4,8,16,32,64]:
        A=list(range(1,2*m+1));poly={s:(-3 if abs(s)<=m else 4) for s in range(-2*m,2*m+1) if s}
        Q,H=exact(A,poly);coupling=2*sum(poly[a] for a in A)
        assert (Q,H,coupling)==(50*m,-4*m*m-26*m,2*m)
        assert F(-H,Q)==F(2*m+13,25)
        for j in range(1,2*m+1):
            r={s:1 for s in range(-j,j+1) if s};q,h=exact(A,r);a=2*j
            assert q==2*j and h>=2*j*(j-1)
            assert 4*q+2*h-a*a>0  # No single {1,D_j} root reaches K=2.
        out.append(dict(n=2*m,Q=Q,H=H,coupling=coupling,K_lower=str(F(-H,Q))))
    return out


def periodic_control(row):
    X=row['n'];den=row['coefficient_denominator'];T=den//(2*(X+1));assert den==2*(X+1)*T
    for k,c in enumerate(row['coefficient_numerators'],1):
        rnum=(X+1-k)*(4 if k%5==0 else -1)*4096;v=c-rnum
        # v=floor(den*phi(w^2)) proved by exact rational inequalities,
        # with no use of the producer's integer-square-root calculation.
        w=F(X+1-k,X+1);lo=F(v,den);hi=F(v+1,den)
        assert 0<=lo<hi<=F(1,2)
        assert (1-2*lo)**2>=1-w*w and (1-2*hi)**2<1-w*w
    upper=F(3,4)+F(X,den);assert upper==F(row['global_M_upper'])
    # The period-five packet r/w takes values 1,-1/4,-1/4,-1/4,-1/4.
    rr=[F(1)]+[F(-1,4)]*4
    assert sum(rr)==0 and sum(t*t for t in rr)/5==F(1,4)
    nearest=[k for k,c in enumerate(row['coefficient_numerators'],1) if 2*c>=den]
    m=len(nearest);assert nearest==list(range(5,5*m+1,5)) and m>0
    return dict(X=X,coefficient_rounding=True,packet_mean='0',packet_variance='1/4',global_M_upper=str(upper),
                nearest_binary_actual=nearest,nearest_binary_n=m,nearest_binary_max_A=5*m,
                nearest_binary_M_lower=str(F(7*m,33)),nearest_binary_M_upper=str(m),
                nearest_binary_status='Analytic negative point x=3pi/[5(2m+1)] and trivial all-circle upper M<=m; '
                                      'M>7m/33 uses sin(t)<=t and pi<22/7. No sampled minimum.')


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/ordered_prefix_2026-10-20');checks=[];periodic=[]
    for name in ['results.json','extra.json']:
        data=json.loads((root/name).read_text())
        for row in data['cases']:
            checks.append(verify(row))
            if row['label'].startswith('weighted_P61') and not row['suffix']:periodic.append(periodic_control(row))
    result=dict(status='PASS',host=socket.gethostname(),witnesses=checks,
                interval_algebra=interval_identity(),periodic_controls=periodic,
                qualification='Achieved Rayleigh bounds verified exactly, not numerical eigenvalue optimality. '
                              'The all-circle packet upper bound also uses the paper Fejer/PD identity.')
    (root/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',integer_witnesses=len(checks),interval_cases=len(result['interval_algebra']),
                         periodic_controls=len(periodic))))


if __name__=='__main__':main()
