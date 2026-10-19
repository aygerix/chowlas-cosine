"""Independent normalization/finite-identity checks; VM only."""
import sys
sys.dont_write_bytecode=True
import json
import math
import importlib.util
from pathlib import Path
from fractions import Fraction as Q
import numpy as np

out=Path('.research/agents/p31_scratch')
rng=np.random.default_rng(310020)
checks=[]
for A in ([1], list(range(1,9)), [1,2,4,8,16], [1,3,4,17,31], [2,5,8,11]):
    A=np.asarray(A,dtype=int)
    for w in (1,5,32):
        X=int(A[-1]); L=X+w
        K=1 << (2*L+1).bit_length()
        grid=np.arange(K)*2*math.pi/K
        f=np.cos(A[:,None]*grid).sum(axis=0)
        kappa=np.maximum(0,1-A/(w+1))
        M=len(A) # safe nonnegativity for all real x, not a minimum estimate
        F0=np.ones(K)
        for j in range(1,w+1):
            F0 += 2*(1-j/(w+1))*np.cos(j*grid)
        W=2*(w+1)/3+1/(3*(w+1))
        S=kappa@kappa
        left=[]; right=[]; max_mean_err=0
        for j in range(K):
            F=np.roll(F0,j)
            h=F*(f+M)
            s=M+sum(float(k)*math.cos(int(a)*grid[j]) for a,k in zip(A,kappa))
            max_mean_err=max(max_mean_err,abs(h.mean()-s))
            left.append((h*h).mean())
            right.append(s*s)
        rec=dict(A=A.tolist(),w=w,K=K,
                 F2_error=abs((F0*F0).mean()-W),
                 h_mean_error=max_mean_err,
                 averaged_h2_error=abs(np.mean(left)-W*(len(A)/2+M*M)),
                 averaged_s2_error=abs(np.mean(right)-(M*M+S/2)))
        checks.append(rec)
assert Q(77,100)*Q(251,250)**3<Q(39,50)
# Complex sinc-interpolation L2 and convolution identities by Gauss integration.
from scipy.integrate import quad
u=rng.normal(size=8)+1j*rng.normal(size=8)
u/=np.linalg.norm(u)
E=float(np.vdot(np.convolve(u,u),np.convolve(u,u)).real)
theta=.317
def transform(x):
    return sum(u[j]*np.exp(1j*j*(theta-x)) for j in range(len(u)))
L2=quad(lambda x:abs(transform(x))**2,-math.pi,math.pi,epsabs=1e-11)[0]/(2*math.pi)
L4=quad(lambda x:abs(transform(x))**4,-math.pi,math.pi,epsabs=1e-11)[0]/(2*math.pi)
data=dict(seed=310020,normalization_checks=checks,sinc_fourier_check=dict(L2=L2,E=E,L4=L4,error=abs(E-L4)))
audit=json.loads((out/'audit_results.json').read_text())
data['audit_summary']=dict(cases=len(audit['cases']),windows=sum(len(c['windows']) for c in audit['cases']),
 max_fft_error=max(c['fft_direct_error'] for c in audit['cases']),max_bu_error=max(c['bu_identity_error'] for c in audit['cases']),
 max_rho_required=max(z['rho_required'] for c in audit['cases'] for z in c['windows']),
 violations_of_proved_bound=[c['name'] for c in audit['cases'] if c['max_proved_bound']>c['M_estimate']+1e-6])
(out/'verification_results.json').write_text(json.dumps(data,indent=2))
print(json.dumps(data['audit_summary'],indent=2))
print('max normalization error', max(z[k] for z in checks for k in z if k.endswith('_error')))
print('sinc Fourier check',data['sinc_fourier_check'])
print('PDF extraction availability', {m: bool(importlib.util.find_spec(m)) for m in ['pypdf','pdfplumber','fitz']})
print('| case | n | X | estimated M | proved-P31 bound | heuristic-rho bound |')
print('|---|---:|---:|---:|---:|---:|')
for c in audit['cases']:
    print('| %s | %d | %d | %.6f | %.6f | %.6f |' % (c['name'],c['n'],c['X'],c['M_estimate'],c['max_proved_bound'],c['max_heuristic_bound']))
