"""Exact variable-coupling certificates for the saved forced-plateau sets.

Run on Dirichlet. q=D_A-D_p, hence qhat(a)=1-p_a on selected frequencies.
The rational two-by-two determinant certifies an all-circle lower bound
for M(A), independently of the finite-witness upper-bound algorithm.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
from flint import fmpz_poly
from cstar_forced_plateau import correlation


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    r=[1,0,-5,5,0,-1]
    square=[0]*11
    for j,a in enumerate(r):
        for k,b in enumerate(r):square[j+k]+=a*b
    mean=sum(F(a,j+1) for j,a in enumerate(r))
    variance=mean-sum(F(a,j+1) for j,a in enumerate(square))
    assert mean==F(5,12) and variance>0
    root=Path('.research/experiments/forced_plateau_2026-10-20')
    source=json.loads((root/'results.json').read_text())
    out=dict(qualification='Exact all-circle variable-coupling certificates; no uniform interpolation assertion.',
             continuous_profile_coefficients=r,asymptotic_density=str(mean),
             asymptotic_variance_density=str(variance),cases=[])
    for row in source['cases']:
        L,b,A=row['L'],row['b'],row['A'];X=L-2;N=2*len(A)
        energy=(L**5-L)//30;selected=set(A)
        pnum=[energy if a<=b else correlation(L,a) for a in range(1,X+1)]
        positive=[(energy if a in selected else 0)-pnum[a-1]
                  for a in range(1,X+1)]
        assert all(positive[a-1]==0 for a in range(1,b+1))
        coeff=positive[::-1]+[0]+positive
        Qnum=sum(z*z for z in coeff)
        convolution=list(fmpz_poly(coeff)**2)
        Hnum=2*sum(int(convolution[2*X+a]) for a in A)
        fourth_num=sum(int(z)**2 for z in convolution)
        coupling=F(2*sum(positive[a-1] for a in A),energy)
        Q=F(Qnum,energy**2);H=F(Hnum,energy**2)
        fourth=F(fourth_num,energy**4)
        af,qf,hf=map(float,[coupling,Q,H])
        disc=math.hypot(hf,2*math.sqrt(qf)*af)
        lower_float=(2*af*af/(disc+hf) if hf>=0
                     else (disc-hf)/(2*qf))
        lower=F(max(1,math.floor(lower_float*10**6)),10**6)
        determinant=lower*lower*Q+lower*H-coupling*coupling
        assert determinant<0
        current_variance=sum(F(z*(energy-z),energy**2) for z in pnum)
        outrow=dict(t=row['t'],L=L,b=b,n=len(A),N=N,
                    coupling=str(coupling),coupling_over_N_float=af/N,
                    profile_variance=str(current_variance),
                    weighted_rounding_residual=str(sum(F(pnum[a-1],energy) for a in A)
                                                  -sum(F(z*z,energy**2) for z in pnum)),
                    norm_squared=str(Q),energy=str(H),fourth_power=str(fourth),
                    norm_squared_over_N_float=float(Q)/N,
                    fourth_power_over_N2_float=float(fourth)/N**2,
                    K_lower_rational=str(lower),
                    negative_determinant=str(determinant),
                    R_lower_float=float(lower)/math.sqrt(2*N),verified=True)
        out['cases'].append(outrow)
        print(json.dumps({k:outrow[k] for k in ['t','n','coupling_over_N_float',
              'norm_squared_over_N_float','fourth_power_over_N2_float','R_lower_float']}),flush=True)
    (root/'noise.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(asymptotic_density=str(mean),variance_density=str(variance))))


if __name__=='__main__':main()
