"""Independent rational sign certificates and small brute cone checks.

Uses rational Bernstein coefficients instead of SymPy's Sturm algorithm.
The asymptotic counting/resonance argument remains a separate paper proof.
Run on Dirichlet.
"""
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path
import socket
from cstar_integer_cone import cone_pairs
from cstar_integer_cone_box import box_set


def bernstein(coeff,lo,hi):
    degree=len(coeff)-1;h=hi-lo
    power=[h**j*sum(coeff[k]*math.comb(k,j)*lo**(k-j)
                   for k in range(j,degree+1)) for j in range(degree+1)]
    return [sum(power[j]*F(math.comb(i,j),math.comb(degree,j))
                for j in range(i+1)) for i in range(degree+1)]


def disk_certificate(lo,hi,margin):
    coeff=[F((-1)**k,math.factorial(k)*math.factorial(k+1)) for k in range(21)]
    coeff[0]+=margin
    queue=[(lo,hi,0)];leaves=[]
    while queue:
        a,b,depth=queue.pop()
        weights=bernstein(coeff,a,b)
        if max(weights)<0:
            leaves.append(dict(lo=str(a),hi=str(b),max_bernstein=str(max(weights))))
        else:
            assert depth<16
            mid=(a+b)/2
            queue.extend([(a,mid,depth+1),(mid,b,depth+1)])
    leaves.sort(key=lambda r:F(r['lo']))
    assert F(leaves[0]['lo'])==lo and F(leaves[-1]['hi'])==hi
    assert all(a['hi']==b['lo'] for a,b in zip(leaves,leaves[1:]))
    assert hi<F(21*22)
    return dict(u_interval=[str(lo),str(hi)],margin=str(margin),
                leaves=leaves,verified=True)


def brute(X,box):
    out=set()
    for matrix in product(range(-X,X+1),repeat=4):
        if not any(matrix) or matrix<tuple(-z for z in matrix):continue
        a,b,c,d=matrix
        if a*d!=b*c:continue
        if not box and sum(z*z for z in matrix)>X*X:continue
        out.add(matrix)
    return out


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    root=Path('.research/experiments/integer_cone_2026-10-20')
    out=dict(qualification='Independent rational sign and finite parametrization checks; no external audit of the paper proof.',
             disk_certificates=[disk_certificate(F(4),F(484,49),F(1,50)),
                                disk_certificate(F(5929,1600),F(49,4),F(1,2000))],
             brute_checks=[])
    for X in [2,4,8]:
        actual=brute(X,False)
        generated={(u1*w1,u1*w2,u2*w1,u2*w2) for u1,u2,w1,w2 in cone_pairs(X)}
        assert actual==generated
        actual_box=brute(X,True);B=2*X+1
        encoded={abs(a+B*b+B*B*c+B**3*d) for a,b,c,d in actual_box}
        assert encoded==set(box_set(X))
        out['brute_checks'].append(dict(X=X,disk_n=len(actual),box_n=len(actual_box),verified=True))
    # Elementary bounds used in the independent analytic sign proof for
    # the box integral. They imply Si(2pi)>1 and log(3)<6/5.
    sine_lower=F(31,20)-F(22,7)**3/144-F(10,31)
    exponential_lower=sum(F(6,5)**k/math.factorial(k) for k in range(4))
    assert sine_lower>1 and exponential_lower>3
    assert F(22,7)**2<10
    out['box_analytic_bounds']=dict(Si_2pi_lower=str(sine_lower),
                                     exp_6_over_5_lower=str(exponential_lower),
                                     derived_box_integral_upper='-1/75',verified=True)
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(disk_partition_sizes=[len(z['leaves']) for z in out['disk_certificates']],
                         brute_checks=out['brute_checks'],box_analytic_bounds=out['box_analytic_bounds']),indent=2))


if __name__=='__main__':main()
