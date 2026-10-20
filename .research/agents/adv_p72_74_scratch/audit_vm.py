#!/usr/bin/env python3
"""Adversarial numerical checks. Run ONLY through src/dirun.sh on dirichlet.
Every cell mask denotes actual arcs of width 1/N centered at j/N, not point samples.
Numerical comparisons are evidence, not directed-rounding certificates.
"""
import itertools
import json
import math
import platform
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy
from scipy.optimize import linprog

OUT = Path('.research/agents/adv_p72_74_scratch')
SEED = 727374
rng = np.random.default_rng(SEED)
results = {'seed': SEED, 'platform': platform.platform(), 'python': platform.python_version(),
           'numpy': np.__version__, 'scipy': scipy.__version__, 'status': 'running'}
started = time.monotonic()

def save():
    results['elapsed_seconds'] = time.monotonic() - started
    (OUT / 'results_vm.json').write_text(json.dumps(results, indent=2))

def announce(name, data):
    results[name] = data
    save()
    print(name, json.dumps(data), flush=True)

def lp_pair(A, tau, N):
    A = np.array(A)
    C = np.cos(2*np.pi*np.outer(np.arange(N//2+1)/N, A))
    m, n = C.shape
    pr = linprog(np.r_[np.zeros(n), 1.], A_ub=np.c_[-C, -np.ones(m)],
                 b_ub=np.zeros(m), bounds=[(1-tau, 1+tau)]*n+[(None,None)], method='highs')
    # c=C^T p, t >= |c|. Minimize sum(c)+tau*sum(t), negate its value.
    du = linprog(np.r_[C.sum(axis=1), np.full(n,tau)],
                 A_ub=np.r_[np.c_[C.T,-np.eye(n)], np.c_[-C.T,-np.eye(n)]],
                 b_ub=np.zeros(2*n), A_eq=np.array([np.r_[np.ones(m),np.zeros(n)]]),
                 b_eq=[1.], bounds=[(0,None)]*(m+n), method='highs')
    if not pr.success or not du.success:
        raise RuntimeError((A.tolist(),tau,pr.message,du.message))
    c = C.T @ du.x[:m]
    actual_dual = float(np.sum(-c-tau*np.abs(c)))
    return {'A':A.tolist(),'tau':tau,'grid':N,'primal':float(pr.fun),'dual':float(-du.fun),
            'actual_dual':actual_dual,'gap':float(abs(pr.fun+du.fun)),
            'primal_residual':float(max(0,np.max(-C@pr.x[:n]-pr.x[n]))),
            'dual_mass_residual':float(abs(du.x[:m].sum()-1)),
            'dual_abs_residual':float(max(0,np.max(np.abs(c)-du.x[m:]))) }

# P72(a): all nonempty subsets of {1,...,6} of size <=4, and random sparse A.
sets = [a for n in range(1,5) for a in itertools.combinations(range(1,7),n)]
sets += [tuple(sorted(rng.choice(np.arange(1,25),size=int(rng.integers(2,7)),replace=False))) for _ in range(20)]
lps = [lp_pair(a,tau,2048) for a in sets for tau in (0.,.1,.5,.9)]
(OUT/'p72_lp_cases_vm.json').write_text(json.dumps(lps,indent=2))
coarse_fine = []
for case in sorted(lps,key=lambda c:c['gap'],reverse=True)[:8]:
    fine = lp_pair(case['A'],case['tau'],8192)
    fine['coarse_primal'] = case['primal']
    fine['grid_change'] = fine['primal']-case['primal']
    coarse_fine.append(fine)
announce('p72', {'cases':len(lps),'fine_cases':coarse_fine,
                 'max_lp_gap':max(c['gap'] for c in lps),
                 'max_actual_dual_gap':max(abs(c['primal']-c['actual_dual']) for c in lps),
                 'max_primal_residual':max(c['primal_residual'] for c in lps),
                 'max_dual_mass_residual':max(c['dual_mass_residual'] for c in lps),
                 'max_dual_abs_residual':max(c['dual_abs_residual'] for c in lps)})

# Fourier integration of a union of centered grid cells is exact in formula.
N = 2048
x = np.arange(N)/N
signedx = np.minimum(x,1-x)
kall = np.arange(N//2+1)
def coeff(mask):
    return np.fft.rfft(mask)/N*np.sinc(kall/N)

def independent_coeff(mask, ks):
    # Direct arc integration, independent of FFT. Endpoints may lie outside [0,1].
    centers = x[np.asarray(mask,dtype=bool)]
    ks = np.array(ks)
    return np.exp(-2j*np.pi*np.outer(ks,centers)).sum(axis=1)/N*np.sinc(ks/N)

def symmetric_mask(score, count):
    # Choose pairs j,-j only; omit singleton cells at 0 and 1/2.
    pairs = np.arange(1,N//2)
    count = min(N//4,max(1,count//2))
    chosen = pairs[np.argpartition(score[pairs],-count)[-count:]]
    mask = np.zeros(N)
    mask[chosen] = mask[-chosen] = 1.
    return mask

# P73(T): nonnegative Fourier coefficients give PD, including complex-valued g.
# Masks include independent random arcs, intervals, and adaptive near-best sets.
p73 = []
for rep in range(5000):
    degree = int(rng.integers(0,25))
    ks = np.arange(-degree,degree+1)
    weights = rng.exponential(size=len(ks))
    if rep%2 == 0:
        weights = (weights+weights[::-1])/2
    if rep%7 == 0:
        weights *= rng.random(len(ks)) < .3
    if weights.sum()==0:
        weights[len(ks)//2]=1
    gamma = float(rng.uniform(.01,1.332))
    weights *= gamma/weights.sum()
    delta = min(.499,(4-3*gamma)/5*.999)
    g = weights @ np.exp(2j*np.pi*np.outer(ks,x))
    mu_target = float(rng.uniform(.005,.5))
    count = max(1,min(N//2,int(N*mu_target)))
    if rep%4 == 0:
        mask = np.zeros(N); mask[rng.choice(N,count,replace=False)] = 1
    elif rep%4 == 1:
        center = rng.random(); distance = np.abs((x-center+.5)%1-.5)
        mask = np.zeros(N); mask[np.argpartition(distance,count-1)[:count]]=1
    else:
        # Adversarial set with largest Re g, with controlled measure <= 1/2.
        mask = np.zeros(N); mask[np.argpartition(g.real,-count)[-count:]]=1
    full = np.fft.fft(mask)/N*np.sinc(np.fft.fftfreq(N))
    a = full[ks%N]
    mu = float(mask.mean())
    E = float(np.dot(weights,weights)+mu-2*np.dot(weights,a.real))
    rhs = delta**2*mu/3
    p73.append({'rep':rep,'degree':degree,'gamma':gamma,'delta':delta,'mu':mu,'E':E,
                'rhs':rhs,'ratio':E/rhs,'margin':E-rhs})
    if rep == 0 or E/rhs <= min(c['ratio'] for c in p73[:-1]):
        np.savez(OUT/'p73_best_vm.npz',weights=weights,ks=ks,mask=mask)
# Boundary cases with known PD constants, arbitrary half-circle sets.
for gamma in (0.,.25,.5,1.,7/6):
    delta = min(.499,(4-3*gamma)/5*.999)
    mu=.5
    E=gamma**2+mu-2*gamma*mu
    p73.append({'kind':'constant','gamma':gamma,'delta':delta,'mu':mu,'E':E,
                'rhs':delta**2*mu/3,'ratio':E/(delta**2*mu/3),'margin':E-delta**2*mu/3})
announce('p73',{'cases':len(p73),'violations':sum(c['margin'] < -1e-10 for c in p73),
                 'min_ratio':min(p73,key=lambda c:c['ratio']),
                 'min_margin':min(p73,key=lambda c:c['margin'])})

# P74: exact continuous arc/lattice coefficients and random symmetric cell unions.
p74=[]; proposed={}; rejected={}; max_fft_direct_error=0.; best_ratio=float('inf')

def record74(L,mu,a,kind,metadata=None,mask=None):
    global best_ratio,max_fft_direct_error
    proposed[kind]=proposed.get(kind,0)+1
    if mu<=0 or mu>.5+1e-14 or min(a)<-2e-12:
        rejected[kind]=rejected.get(kind,0)+1
        return
    U=float(mu-a[0]**2-2*np.dot(a[1:],a[1:]))
    ratio=U/min(mu,1/L)
    row={'L':L,'mu':mu,'U':U,'gamma':float(a[0]+2*sum(a[1:])),
         'min_low_coefficient':float(min(a)),'ratio':ratio,'margin':U-2.5e-4*min(mu,1/L),
         'kind':kind,'metadata':metadata}
    p74.append(row)
    if ratio<best_ratio:
        best_ratio=ratio
        (OUT/'p74_best_vm.json').write_text(json.dumps(row,indent=2))
        if mask is not None:
            np.save(OUT/'p74_best_mask_vm.npy',mask)
    if mask is not None and len(p74)%100==0:
        direct=independent_coeff(mask,range(L+1))
        max_fft_direct_error=max(max_fft_direct_error,float(np.max(np.abs(direct-a))))

for L in (1,2,3,4,6,8,12,16,24,32,64):
    # Centered arc and preimages under x -> q*x (including exact coefficient zeros).
    for q in (1,2,3,5,8,17):
        for mu in np.geomspace(1e-5,min(.5,q/L),35):
            ks=np.arange(L+1)
            a=np.zeros(L+1)
            div=ks%q==0
            a[div]=mu*np.sinc((ks[div]/q)*mu)
            record74(L,float(mu),a,'arc_or_lattice',{'q':q})
    cosmat=np.cos(2*np.pi*np.outer(np.arange(1,L+1),x))
    D=1+2*cosmat.sum(axis=0)
    mask=(D>0).astype(float)
    # At large L, {D>0} can have measure > 1/2. Keep as rejected if so.
    record74(L,float(mask.mean()),coeff(mask)[:L+1].real,'dirichlet_sign',mask=mask)
    for rep in range(400):
        if rep%4==0:
            # Independent symmetric random unions, rejection-sampled for positivity.
            score=rng.random(N); score=(score+score[(-np.arange(N))%N])/2
            count=int(rng.integers(2,N//2+1))
            mask=symmetric_mask(score,count)
            kind='independent_random'
        elif rep%4==1:
            # Automatic positivity: all selected cells inside |x|<1/(4L).
            allowed=np.flatnonzero((signedx+1/(2*N))<1/(4*L))
            mask=np.zeros(N)
            pos=allowed[(allowed>0)&(allowed<N//2)]
            take=pos[rng.random(len(pos))<rng.uniform(.05,1.)]
            mask[take]=mask[-take]=1
            if rep%8==1: mask[0]=1
            kind='small_support_random'
        else:
            # Structured random Fourier scores with positive coefficients; filter.
            w=rng.exponential(size=L)
            if rep%5==0: w*=rng.random(L)<.25
            score=w@cosmat
            count=int(rng.integers(2,N//2+1))
            mask=symmetric_mask(score,count)
            kind='positive_score_random'
        a=coeff(mask)[:L+1]
        assert np.max(np.abs(a.imag))<1e-12
        record74(L,float(mask.mean()),a.real,kind,{'rep':rep},mask)
    if L in (4,16,64):
        print('p74_progress',L,'accepted',len(p74),flush=True)
announce('p74',{'accepted':len(p74),'proposed':proposed,'rejected':rejected,
                'violations':sum(c['margin'] < -1e-10 for c in p74),
                'min_ratio':min(p74,key=lambda c:c['ratio']),
                'min_margin':min(p74,key=lambda c:c['margin']),
                'max_fft_direct_error':max_fft_direct_error,
                'gamma_at_least_7_over_6':sum(c['gamma']>=7/6 for c in p74)})
(OUT/'p74_cases_vm.json').write_text(json.dumps(p74,indent=2))

# Constants and the literal P72(e) missing-upper-bound adversary.
mp.mp.dps=80
C=mp.sqrt(mp.mpf(3)/56)/(288*mp.pi)
constants={'p74_constant':mp.nstr(C,75),'claimed':str(mp.mpf('0.00025')),
           'ratio_to_claimed':mp.nstr(C/mp.mpf('0.00025'),60),
           'p74_h_at_L1':mp.nstr(mp.sqrt(mp.mpf(3)/56)/mp.pi,60),
           'branch_A':mp.nstr(mp.mpf(1)/300,60)}
# phi_B=c*1[-1,1]+B*(1-|x|)_+. Its transform >= -c^2/B exactly.
# Evaluate close to its negative excursions, without claiming global certification.
c=mp.mpf('.5'); rows=[]
for B in (1,10,100,1000,10000):
    z=mp.pi-c*mp.pi/B
    value=c*mp.sin(2*z)/z+B*(mp.sin(z)/z)**2
    rows.append({'tau':'.5','B':B,'frequency':mp.nstr(z/mp.pi,60),
                 'transform_value':mp.nstr(value,60),'rigorous_lower_formula':mp.nstr(-c*c/B,60)})
constants['p72e_example_evaluations']=rows
announce('constants',constants)
results['status']='complete'
save()
print('COMPLETE',flush=True)
