"""Exact constants + adversarial numerical audits of the finite Gaussian proof."""
import json, math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
OUT=Path('.research/agents/tdense8_scratch')

def run():
    K=10**6;J=10**6;delta=F(3,10**6);omega=2*delta+F(12,K)
    # beta=10^(-6000003), c=beta/100. Avoid instantiating enormous integers.
    beta_upper=F(1,10**12);c_upper=beta_upper/100
    exact=dict(beta_exponent=6000003,c_exponent=6000005,K=K,J=J,
        density_Nikolskii_margin=str(F(5,6)-(F(811,1000)*F(1004,1000)+F(811,1000)/100+F(71,300)/100)),
        increment_bound=str(F(2,J)+42*c_upper),delta=str(delta),
        density_lower_bound=str(F(8,15)-2*beta_upper),omega=str(omega),
        crossing_error=str(2*delta+3*beta_upper),
        required_energy_gap=str(F(3,100)**2-F(7,10**6)**2),
        available_error=str(8*omega+2*beta_upper))
    assert F(exact['density_Nikolskii_margin'])>0
    assert F(exact['increment_bound'])<delta
    assert F(exact['density_lower_bound'])>F(53,100)
    assert F(exact['crossing_error'])<F(7,10**6)
    assert F(exact['required_energy_gap'])>F(exact['available_error'])
    # Numeric audits are not used to certify the analytic kernel lemmas.
    kernel=[]
    for ss in (1.,2.,5.,10.,30.):
        R=math.ceil(14*ss);idx=np.arange(-R,R+1);kk=np.exp(-idx**2/(4*ss**2));Z=kk.sum();kk/=Z
        xx=np.linspace(-np.pi,np.pi,3001)
        L=np.cos(np.outer(xx,idx))@kk
        # Absolute floating errors dominate the exponentially small exact bound for s>=2.
        kernel.append(dict(s=ss,Z=float(Z),Z_lower=2*math.sqrt(math.pi)*ss,Z_upper=4*ss+1,
            first_abs_moment=float(np.dot(abs(idx),kk)),moment_upper=4*ss,
            min_L_float=float(L.min()),max_L_float=float(L.max()),
            gaussian_difference_float=float(np.max(abs(L-np.exp(-ss**2*xx**2))))))
    rng=np.random.default_rng(2026101908);finite=[]
    for X in (100,300,800):
        aa=np.zeros(2*X+1);bits=rng.random(X)<.35;bits[-1]=1
        aa[X+1:]=bits;aa[:X]=bits[::-1]
        for ss in (2.,10.,30.):
            R=math.ceil(14*ss);idx=np.arange(-R,R+1);ks=np.exp(-idx**2/(4*ss**2));ks/=ks.sum()
            q=np.convolve(aa,ks,'full');a=np.pad(aa,(R,R));r=a-q
            E=np.convolve(r*r,ks,'full');ee=np.pad(q*(1-q),(R,R))
            variation=max(float(np.max(abs(q-np.roll(q,j)))) for j in (1,2))
            finite.append(dict(X=X,s=ss,energy_approx_max_error=float(np.max(abs(E-ee))),
                               coefficient_variation=float(variation)))
    rec=dict(status='EXACT CONSTANTS; NUMERICAL KERNEL AUDIT',exact=exact,kernel_numeric=kernel,finite_numeric=finite)
    OUT.joinpath('effective_checks.json').write_text(json.dumps(rec,indent=2))
    print(json.dumps(rec,indent=2),flush=True)

if __name__=='__main__':run()
