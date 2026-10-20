"""Validate the non-isoclinic box resonance and its limiting integral.

The integral is enclosed using entire sinc power series with a rational
uniform tail bound; no singular numerical quadrature is used.
Run on Dirichlet.
"""
from collections import Counter
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import flint
from cstar_integer_cone_box import box_set


def sinc_polynomial(a,b,K):
    coefficients=[flint.arb(0) for _ in range(2*K+1)]
    pi=flint.arb.pi()
    for k in range(K+1):
        factor=(-1)**k*pi**(2*k)/math.factorial(2*k+1)
        for j in range(2*k+1):
            coefficients[j]+=factor*math.comb(2*k,j)*a**(2*k-j)*b**j
    return coefficients


def integral_certificate():
    K=40
    first=sinc_polynomial(2,1,K);second=sinc_polynomial(1,2,K)
    product=[flint.arb(0) for _ in range(4*K+1)]
    for j,a in enumerate(first):
        for k,b in enumerate(second):product[j+k]+=a*b
    # Half of the integral over [-1,1]: odd powers vanish.
    center=sum((z/(j+1) for j,z in enumerate(product) if j%2==0),flint.arb(0))
    T=F(66,7)  # |pi*(a+b*t)| <= 3*pi < 66/7.
    tail=T**(2*K+2)/math.factorial(2*K+3)
    ratio=T*T/F((2*K+4)*(2*K+5))
    epsilon=tail/(1-ratio)
    error=2*epsilon+epsilon*epsilon
    radius=flint.arb(error.numerator)/error.denominator
    assert center+radius < -flint.arb(1)/25
    return dict(sinc_degree=2*K,precision=flint.ctx.prec,
                uniform_single_factor_error=str(epsilon),
                product_integral_error=str(error),
                integral_midpoint_float=float(center.mid()),
                rigorous_integral_upper='-1/25',verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=256
    root=Path('.research/experiments/integer_cone_2026-10-20')
    root.mkdir(parents=True,exist_ok=True)
    out=dict(limit=integral_certificate(),cases=[])
    for X in [8,16,32,64]:
        B=2*X+1;A=box_set(X);n=len(A);q=B*B+3*B+1;j=2*B+5
        counts=Counter(min(j*a%q,q-(j*a%q)) for a in A)
        point=sum((count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,q))
                   for r,count in counts.items()),flint.arb(0))
        upper=F(math.ceil(float(point.mid())/n*10**6)+1,10**6)
        assert point<flint.arb(upper.numerator)*n/upper.denominator
        out['cases'].append(dict(X=X,B=B,n=n,
                                 root_of_unity=dict(numerator=j,denominator=q),
                                 f_over_n_upper_rational=str(upper),
                                 M_lower_rational=str(-n*upper),verified=True))
    (root/'box_limit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
