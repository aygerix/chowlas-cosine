"""Round-16 bounded VM adversaries. All floating conclusions NUMERICAL."""
from pathlib import Path
from fractions import Fraction
import json, math, platform
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parent

def conv(a,b):return np.fft.ifft(np.fft.fft(a)*np.fft.fft(b)).real

def metric(b,name,boolean=True,mellin=True):
    q=len(b);lam=np.fft.fft(b).real;K=-float(min(lam[1:]));t=K-.5;L=float(max(lam[1:]))+K
    h=lam+K;h[0]=t;C=q*(t*t-.25);V=q*q/4+C
    D=h>=L/2;D[0]=False;s=int(D.sum());d=D.astype(float);r=conv(d,d)
    pp=h*d;u=h-pp;S=r>.5;S[0]=False
    hc=conv(h,h);pc=conv(pp,pp);pu=conv(pp,u);uc=conv(u,u)
    smooth=conv(d,h)
    actual=float(sum((smooth-s*t)**2));target=q*s*(q-s)/4
    out=dict(status='NUMERICAL',name=name,q=q,K=K,t=t,L=L,epsilon=t/math.sqrt(q),
             core_size=s,core_energy_fraction=float(sum(pp*pp)/V),sumset_offzero=int(S.sum()),
             core_sum_relative_error=float(max(abs(hc[S]-C))/C) if S.any() else 0.,
             global_relative_error=float(max(abs(hc[1:]-C))/C),
             core_core_fraction_mean=float(np.mean(pc[S]/C)) if S.any() else 0.,
             core_bulk_fraction_mean=float(np.mean(2*pu[S]/C)) if S.any() else 0.,
             bulk_bulk_fraction_mean=float(np.mean(uc[S]/C)) if S.any() else 0.,
             variance_relative_error=(actual-target)/max(1,target),
             boolean_square_residual=float(max(abs((b[1:]-.5)**2-.25))),
             mass_relative_error=float(sum(h)-q*t)/max(1,q*t),energy_relative_error=float(sum(h*h)-V)/V)
    if boolean:
        assert b[0]==0 and sum(b)==(q-1)//2 and np.array_equal(b,b[(-np.arange(q))%q])
        assert out['global_relative_error']<2e-8
        assert abs(out['variance_relative_error'])<2e-8
        # Exact identity and nonnegative decomposition; numerical finite check.
        assert max(abs((pc+2*pu+uc-hc)))/V<1e-9
        eadd=float(sum(r*r));assert (L*L/4)*(eadd-s*s)<=C*(s*s-s)+1e-7*q*q*max(1,s*s)
        # Energy-carrying threshold used in the strategic follow-up.
        A=h>=V/(2*q*t);A[0]=False
        out['energy_threshold_size']=int(sum(A));out['energy_threshold_fraction']=float(sum(h[A]**2)/V)
        assert out['energy_threshold_fraction']>=.5-1e-9
    if mellin:
        n=(q-1)//2;g=int(sp.primitive_root(q));powers=np.empty(n,dtype=np.int64);v=1
        for j in range(n):powers[j]=v;v=(v*g)%q
        F=b[powers]-.5;X=(lam[powers]+.5)/math.sqrt(q)
        fc=np.fft.fft(F)/n;xc=np.fft.fft(X)/n
        c=2*np.cos(2*np.pi*powers/q);thetabar=np.fft.fft(c)/math.sqrt(q)
        neg=(-np.arange(n))%n;theta=thetabar[neg]
        err=float(max(abs(xc[1:]-thetabar[1:]*fc[neg[1:]])))
        assert err<1e-8
        assert max(abs(fc[1:]))<=t/math.sqrt(q)+1e-8
        # Multiplicative Boolean identity in coefficient space.
        bc=np.fft.ifft(np.fft.fft(fc)**2);bc[0]-=.25
        log4=int(np.flatnonzero((powers==4)|(powers==q-4))[0])
        k=np.arange(1,n);k=k[(2*k)%n!=0]
        hd=theta[k]*theta[(k+n//2)%n]-np.exp(-2j*np.pi*k*log4/n)*theta[(2*k)%n]*theta[n//2]
        hd_err=float(max(abs(hd))) if len(k) else 0.
        assert hd_err<1e-8
        moment=[]
        for j in range(1,7):
            # Sup over all twists a in G, including principal character.
            vals=np.fft.ifft(theta**j)
            mx=float(max(abs(vals)));assert mx<=2*j/math.sqrt(q)+1e-8
            moment.append(mx)
        out.update(mellin_max_coefficient=float(max(abs(fc[1:]))),
                   mellin_energy=float(sum(abs(fc)**2)),mellin_effective_count=float(sum(abs(fc)**2)**2/sum(abs(fc)**4)),
                   mellin_required_count=q/(4*t*t),gauss_transform_error=err,hasse_davenport_error=hd_err,
                   boolean_mellin_quadratic_error=float(max(abs(bc))),gauss_moment_twist_suprema=moment)
        if boolean:assert out['boolean_mellin_quadratic_error']<1e-8
    return out

def array(q,pairs):
    b=np.zeros(q);b[pairs]=1;b[[-x%q for x in pairs]]=1;return b

records=[]
prior=json.loads(Path('examples/r15_certificates/stability_probe.json').read_text())['records']
for rec in prior:
    if rec['is_exact_halfset'] and rec.get('pairs') is not None:
        records.append(metric(array(rec['q'],rec['pairs']),rec['name']))
# Reproduce the prior repaired random-profile sets, with the exact prior RNG sequence.
rng=np.random.default_rng(151019)
def repair(b):
    q=len(b);m=(q-1)//4;pp=np.flatnonzero(b[1:(q+1)//2]>.5)+1
    if len(pp)>m:
        rem=rng.choice(pp,len(pp)-m,replace=False);b[rem]=0;b[q-rem]=0
    elif len(pp)<m:
        av=np.flatnonzero(b[1:(q+1)//2]<.5)+1;add=rng.choice(av,m-len(pp),replace=False);b[add]=1;b[q-add]=1
    return b
for q in (4093,65537):
    x=np.arange(1,(q+1)//2)
    pp=x[rng.random(len(x))<.5+.2*np.cos(2*np.pi*x/q)]
    records.append(metric(repair(array(q,pp.tolist())),'R13_PK_repaired'))
    a=1-1/math.sqrt(2);pp=x[rng.random(len(x))<a+.1*np.cos(2*np.pi*x/q)]
    b=array(q,pp.tolist());u=np.maximum(b,b[(3*np.arange(q))%q]);records.append(metric(repair(u),'R14_UNION_repaired'))
# Reconstruct R12-S in its old sign normalization, then convert to the current h.
q=1000033;u=q**(1/3);h0=u-1;T=q*(u-1);V=q*q+q*u*(u-2)
Tp=T-h0;Ep=V-h0*h0;m=4*math.ceil(Tp*Tp/(4*Ep));mu=Tp/m;var=Ep/m-mu*mu
raw=np.zeros(q);raw[0]=h0
for j in range(m//2):
    a=j+1;raw[a]=raw[q-a]=mu+(1 if j<m//4 else -1)*math.sqrt(var)
b=(np.fft.ifft(raw-u).real+1)/2
records.append(metric(b,'R12_S_weighted_fake',False,True))
# Round-15 B3 exact scalar counterexample, from stored rational formulas.
fake=json.loads(Path('examples/r15_certificates/support_counterexample.json').read_text())
q=fake['q'];K=float(fake['K']);t=K-.5;m=fake['core_modes'];w=fake['weak_positive_modes']
mu=float(Fraction(fake['core_h_mean']));var=float(Fraction(fake['core_h_variance']))
h=np.zeros(q);h[0]=t
for j in range(m//2):
    a=j+1;h[a]=h[q-a]=mu+(1 if j<m//4 else -1)*math.sqrt(var)
for j in range(m//2,m//2+w//2):h[j+1]=h[q-j-1]=K+1/q
b=np.fft.ifft(h).real+.5;b[0]-=K
records.append(metric(b,'R15_B3_scalar_fake',False,True))
for r in records:
    print(r['name'],r['q'],'D',r['core_size'],'core_energy',round(r['core_energy_fraction'],6),
          'Serr',r['core_sum_relative_error'],'MellinMax/eps',round(r['mellin_max_coefficient']/r['epsilon'],6),flush=True)
ROOT.joinpath('adversaries.json').write_text(json.dumps({'status':'NUMERICAL','python':platform.python_version(),
   'numpy':np.__version__,'sympy':sp.__version__,'seed':151019,'records':records},indent=2))
