"""VM-only exact/Arb scalar counterexample to unthresholded support stability."""
from pathlib import Path
from fractions import Fraction as Q
from math import ceil
import json
import sympy as sp
from flint import arb,ctx
ctx.prec=220
ROOT=Path(__file__).resolve().parent
q=1000033
assert sp.isprime(q) and q%4==1
k=Q(32);t=k-Q(1,2);r=30000;eps=Q(1,q)
mass=(q-1)*t-r*(k+eps)
energy=(q-1)*(t*t+Q(q,4))-r*(k+eps)**2
s=4*ceil(mass*mass/(4*energy))
mean=mass/s;var=energy/s-mean*mean
assert 0<=var<mean*mean and s%4==r%4==0 and 2*(s+r)<q-1
def ball(x):return arb(x.numerator)/x.denominator
hi=ball(mean)+ball(var).sqrt();lo=ball(mean)-ball(var).sqrt()
assert (lo-ball(k+eps)).lower()>0
Lam=hi-ball(k)
E=(q-1)*(ball(t)*hi-ball(t*t+Q(q,4)))
C=ball(q*k*(k-1))
assert (C-hi*hi).lower()>0
assert (s*ball(mean)+r*ball(k+eps)-ball((q-1)*t)).contains(0)
assert (s*(ball(mean)**2+ball(var))+r*ball(k+eps)**2-ball((q-1)*(t*t+Q(q,4)))).contains(0)
out=dict(status='PROVED finite scalar counterexample, exact rational formulas and Arb enclosures',
         q=q,prime=True,K=str(k),weak_positive_modes=r,core_modes=s,total_positive_modes=r+s,
         epsilon=str(eps),core_h_mean=str(mean),core_h_variance=str(var),
         core_h_high=str(hi),core_h_low=str(lo),LambdaK_over_q_ball=str(Lam*ball(k)/q),
         E_over_q2_ball=str(E/(q*q)),
         omitted_frequency=(q-1)//2,convolution_at_omitted_frequency=0,
         required_convolution=str(q*k*(k-1)),
         assignment='core on +/-[1,s/2], high on first s/4 pairs; weak positive eigenvalues on next r/2 pairs; all other nonzero eigenvalues -K; h(0)=K-1/2')
ROOT.joinpath('support_counterexample.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
