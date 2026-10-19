"""Round-2 finite audits. EXECUTE ONLY with src/dirun.sh -c 2.

Exact modular FLINT polynomial products, two-prime CRT, proved count bound.
The numerical cosine minima and eigenvector search are explicitly numerical;
the rounded rational moment witnesses are evaluated in exact arithmetic.
"""
import argparse
import hashlib
import json
import math
import platform
import sys
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from flint import fmpz_poly, nmod_poly
from scipy.linalg import eigh

sys.path.insert(0, "src")
from box_minlam import true_min

OUT = Path('.research/agents/tdense2_scratch')
PRIMES = (998244353, 1004535809)
P_ALPHA = 2147483647


def exact_counts(A, save=None):
    X, n = max(A), len(A)
    coeff = [0] * (2*X+1)
    for a in A:
        coeff[X-a] = coeff[X+a] = 1
    bound = (2*n)**2
    assert bound < PRIMES[0]*PRIMES[1]
    residues, pairs = [], []
    for p in PRIMES:
        f = nmod_poly(coeff, p)
        f2 = f*f
        f3 = f2*f
        residues.append(np.array([int(f3[3*X+k]) for k in range(3*X+1)], dtype=np.int64))
        # Pair counts <=2n, hence the first prime alone is sufficient here.
        if not pairs:
            pairs.append(np.array([int(f2[2*X+k]) for k in range(2*X+1)], dtype=np.int64))
    p, r = PRIMES
    c = residues[0] + p * (((residues[1]-residues[0])*pow(p, -1, r)) % r)
    assert int(c.max()) <= bound
    assert int(c[0]) % 6 == 0
    if save:
        np.savez_compressed(save, c=c, r=pairs[0])
    return c, pairs[0]


def best_filter(A, save=None, qmax=None):
    X, n = max(A), len(A)
    c, r = exact_counts(A, save)
    aa = np.zeros(X+1, dtype=np.int64)
    aa[A] = 1
    qmax = X if qmax is None else qmax
    if qmax>X:
        aa=np.pad(aa,(0,qmax-X))
        c=np.pad(c,(0,3*(qmax-X)))
        r=np.pad(r,(0,2*(qmax-X)))
    qs = np.arange(1, qmax+1)
    aq = aa[qs]
    v = 12*n - 8*r[qs] + 2*r[2*qs] - 4*aq
    delta = 10*c[0] - 15*c[qs] + 6*c[2*qs] - c[3*qs]
    w = delta + 3*aq*v + 4*aq
    admissible = np.flatnonzero(5*v >= 8*n)
    assert len(admissible)
    best = None
    # Compare signs and squares by Python integers: exact minimizer of W/V^(3/2).
    for i in admissible:
        vi, wi = int(v[i]), int(w[i])
        if best is None:
            best = int(i)
            continue
        vb, wb = int(v[best]), int(w[best])
        si, sb = (wi>0)-(wi<0), (wb>0)-(wb<0)
        if si < sb or (si == sb and si and
                si*(wi*wi*vb**3 - wb*wb*vi**3) < 0):
            best = int(i)
    q, vi, wi = best+1, int(v[best]), int(w[best])
    ratio = 2*wi/vi**1.5
    lbm = (math.sqrt(ratio*ratio+4)-ratio)/2 * math.sqrt(vi/16)
    result = dict(q=q, V=str(F(vi,16)), W=str(F(wi,32)),
        V_over_n=vi/(16*n), min_W_over_V_threehalves=ratio,
        admissible_count=len(admissible), all_q_checked=qmax,
        exact_argmin=True, cmax=int(c.max()), c0=int(c[0]),
        c_at_0_q_2q_3q=[int(c[k*q]) for k in range(4)],
        third_moment_M_lb_numerical=(lbm+int(aa[q])/2)/2,
        min_V_over_n=float(v.min())/(16*n))
    return result


def bohr(X, seed, profile='quadratic', factor=8):
    J = math.ceil(factor*math.log(X)/math.log(math.log(X)))
    # epsilon=1/(8J) exactly. C0=2 in the brief's epsilon=1/(4 C0 J).
    rng = np.random.default_rng(seed)
    mm = np.arange(1, X+1, dtype=np.int64)
    chosen = None
    for trial in range(100):
        numerators = rng.choice(P_ALPHA-1, size=J, replace=False)+1
        union = np.zeros(X, dtype=bool)
        active = np.zeros(X, dtype=np.int16)
        for a in numerators:
            rr = (mm*a) % P_ALPHA
            dd = np.minimum(rr, P_ALPHA-rr)
            union |= (dd*(8*J) < P_ALPHA)
            yes = np.zeros(X, dtype=bool)
            for k in (1,2,3):
                rk = (rr*k) % P_ALPHA
                dk = np.minimum(rk, P_ALPHA-rk)
                yes |= (dk*(8*J) < 3*P_ALPHA)
            active += yes
        if int(active.max()) <= J//2:
            chosen = (numerators, union, active, trial)
            break
    if chosen is None:
        raise RuntimeError('No alpha sample passed the stated finite activity condition')
    numerators, union, active, trial = chosen
    # Rational thinning probabilities, exact integer Bernoulli realization.
    den = 5*(X+1)**2
    if profile == 'quadratic':
        threshold = 4*(X+1-mm)**2
    elif profile == 'flat':
        threshold = np.full(X, 4*(X+1)**2, dtype=np.int64)
    else:
        raise ValueError(profile)
    keep = rng.integers(0, den, size=X, dtype=np.int64) < threshold
    A = mm[union & keep].astype(int).tolist()
    return A, dict(kind='Bohr union', X_ambient=X, seed=seed, J=J,
        epsilon=f'1/{8*J}', C0=2, alpha_denominator=P_ALPHA,
        alpha_numerators=numerators.astype(int).tolist(), alpha_trials=trial+1,
        maximum_active=int(active.max()), activity_limit=J//2,
        union_size=int(union.sum()), thinning=f'(4/5)*(1-m/{X+1})^2' if profile=='quadratic' else '4/5',
        exact_membership_and_thinning=True)


def fejer(X, seed, jfactor=2):
    rng = np.random.default_rng(seed)
    J = math.ceil(jfactor*math.log(X))
    nums = rng.choice(P_ALPHA-1, size=J, replace=False)+1
    mm = np.arange(1, X+1, dtype=np.int64)
    modulation = np.zeros(X)
    negative_count = np.zeros(X, dtype=np.int16)
    for a in nums:
        theta = 2*math.pi*((mm*a)%P_ALPHA)/P_ALPHA
        cc = np.cos(theta)
        modulation += cc
        negative_count += cc <= 0
    prob = .5*(1-mm/(X+1))*(1+.5/J*modulation)
    A = mm[rng.random(X) < prob].astype(int).tolist()
    return A, dict(kind='positive Fejer mixture Bernoulli', X_ambient=X,
        seed=seed, J=J, delta=.5, modulation_amplitude=.5,
        alpha_denominator=P_ALPHA, alpha_numerators=nums.astype(int).tolist(),
        minimum_negative_cos_count=int(negative_count.min()),
        probability_evaluation='floating point (saved realization is an exact integer set)')


def moments(A, q, order=7):
    X=max(A)
    D=X+q
    a=set(A)
    g=[]
    for j in range(-D,D+1):
        if j==0:
            g.append(0)
        else:
            av=lambda k: int(abs(k) in a)
            g.append(2*av(j)-av(j-q)-av(j+q) if q else 2*av(j))
    poly=fmpz_poly(g)
    cur=fmpz_poly([1])
    out=[F(1)]
    for k in range(1,order+1):
        cur=cur*poly
        out.append(F(int(cur[k*D]),4**k))
    return out


def moment_witness(A, q, order=7):
    mus=moments(A,q,order)
    scale=max(1, round(math.sqrt(len(A))))
    vals=[float(m/scale**k) for k,m in enumerate(mus)]
    out=[]
    for d in range(1,(order+1)//2):
        h0=np.array([[vals[i+j] for j in range(d+1)] for i in range(d+1)])
        h1=np.array([[vals[i+j+1] for j in range(d+1)] for i in range(d+1)])
        ev,evec=eigh(h1,h0)
        vec=evec[:,0]
        vec=vec/max(abs(vec))
        pp=[int(round(float(t)*10**9)) for t in vec]
        den=sum(F(pp[i]*pp[j],scale**(i+j))*mus[i+j]
                for i in range(d+1) for j in range(d+1))
        num=sum(F(pp[i]*pp[j],scale**(i+j))*mus[i+j+1]
                for i in range(d+1) for j in range(d+1))
        assert den>0
        lb=-num/den
        Mlb=(lb+F(int(q in A),2))/2 if q else lb
        out.append(dict(degree=d, highest_moment=2*d+1, scale=scale,
            integer_polynomial_coefficients=pp,
            exact_m_lower_bound=str(lb), exact_M_lower_bound=str(Mlb),
            M_lower_bound=float(Mlb), M_lb_over_sqrt_n=float(Mlb)/math.sqrt(len(A)),
            eigenvalue_numerical=float(ev[0])))
    return dict(q=q, moments=[str(m) for m in mus], witnesses=out)


def run_one(name,A,params=None,with_moments=False):
    A=sorted(set(map(int,A)))
    t=time.time()
    safe=name.replace('/','_').replace(':','_')
    row=dict(name=name,n=len(A),X=max(A),C=max(A)/len(A),A=A,parameters=params)
    row['filter']=best_filter(A,OUT/(safe+'_counts.npz'),
        qmax=params.get('X_ambient') if params else None)
    (fm,xm), _, G=true_min(A,over=64)
    direct=float(np.cos(np.array(A)*xm).sum())
    row['minimum_numerical']=dict(M=-float(fm),x=float(xm),R=-float(fm)/math.sqrt(len(A)),
        grid_half_count=G,fft_direct_disagreement=direct-float(fm),certified=False)
    if with_moments:
        row['higher_moments']=[moment_witness(A,q) for q in (0,row['filter']['q'])]
    row['seconds']=time.time()-t
    (OUT/(safe+'.json')).write_text(json.dumps(row,indent=2))
    summary={k:v for k,v in row.items() if k not in ('A','higher_moments','parameters')}
    if params:
        summary['parameters']={k:v for k,v in params.items() if k not in ('alpha_numerators',)}
    if with_moments:
        summary['moment_M_bounds']=[dict(q=m['q'],bounds=[w['M_lb_over_sqrt_n'] for w in m['witnesses']]) for m in row['higher_moments']]
    print(json.dumps(summary),flush=True)
    return summary


def selftest():
    from collections import Counter
    rng=np.random.default_rng(712)
    for X in range(1,22):
        for _ in range(3):
            A=[int(a) for a in range(1,X+1) if rng.random()<.6] or [X]
            c,r=exact_counts(A)
            S=A+[-a for a in A]
            rr=Counter(a+b for a in S for b in S)
            cc=Counter(a+b+c for a in S for b in S for c in S)
            assert all(int(v)==cc[k] for k,v in enumerate(c))
            assert all(int(v)==rr[k] for k,v in enumerate(r))
            for q in range(1,max(A)+1):
                mu=moments(A,q,3)
                aq=int(q in A)
                def rv(k): return int(r[k]) if k<len(r) else 0
                def cv(k): return int(c[k]) if k<len(c) else 0
                v=12*len(A)-8*rv(q)+2*rv(2*q)-4*aq
                w=10*cv(0)-15*cv(q)+6*cv(2*q)-cv(3*q)+3*aq*v+4*aq
                assert mu[1]==0 and mu[2]==F(v,16) and mu[3]==F(w,32)
    print(json.dumps(dict(selftest='PASS',exact_sets=63,python=platform.python_version())),flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['selftest','family','benchmarks','moments'],required=True)
    parser.add_argument('--sizes',type=int,nargs='*',default=[4096,16384,65536,200000])
    parser.add_argument('--kinds',nargs='*',default=['bohr','fejer'])
    parser.add_argument('--moments',action='store_true')
    args=parser.parse_args()
    OUT.mkdir(exist_ok=True)
    if args.mode=='selftest':
        return selftest()
    summaries=[]
    if args.mode=='family':
        for kind in args.kinds:
            for X in args.sizes:
                seed=2026101900+X
                A,params=(bohr(X,seed) if kind=='bohr' else fejer(X,seed))
                summaries.append(run_one(f'{kind}_X{X}',A,params,args.moments))
    elif args.mode=='benchmarks':
        rows=json.load(open('.research/agents/tdense_scratch/probe.json'))['records']
        for row in rows:
            summaries.append(run_one('benchmark_'+row['name'],row['A'],with_moments=args.moments))
        for name,A in [('interval_512',list(range(1,513))),
            ('dilated_intervals_512',sorted(set(list(range(2,1025,2))+list(range(3,1537,3)))) )]:
            summaries.append(run_one(name,A,with_moments=args.moments))
    elif args.mode=='moments':
        for kind in args.kinds:
            for X in args.sizes:
                path=OUT/f'{kind}_X{X}.json'
                row=json.load(open(path))
                row['higher_moments']=[moment_witness(row['A'],q) for q in (0,row['filter']['q'])]
                path.write_text(json.dumps(row,indent=2))
                print(json.dumps(dict(name=row['name'],bounds=[dict(q=m['q'],M_lb_over_sqrt_n=[w['M_lb_over_sqrt_n'] for w in m['witnesses']]) for m in row['higher_moments']])),flush=True)
        return
    (OUT/(args.mode+'_summary.json')).write_text(json.dumps(summaries,indent=2))


if __name__=='__main__':
    main()
