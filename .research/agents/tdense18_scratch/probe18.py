"""Round 18 adversaries. Execute only on dirichlet through src/dirun.sh.

P28/eigenvalues/minima are NUMERICAL unless explicitly Arb certified.
Boundary maximization is exhaustive, with exact rational enclosures of c0.
"""
import argparse
import bisect
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import flint
import numpy as np
import scipy
from scipy.linalg import eigvalsh

sys.path.insert(0, 'src')
sys.path.insert(0, '.research/agents/tdense17_scratch')
from chowla import min_estimate_fft
from fourway import bottom
from probe import spline_prob
from singer import singer
from bu import A_of_S

ROOT = Path('.research/agents/tdense18_scratch')
PI_LO = Fraction('3.14159265358979323846264338327950288419716939937510')
PI_HI = PI_LO + Fraction(1, 10**50)
C_LO = Fraction(2, 3) / PI_HI - Fraction(1, 8)
C_HI = Fraction(2, 3) / PI_LO - Fraction(1, 8)


def boundary(A):
    """All d,k: positive B requires k <= |A_d|/(1-c0).

    Every relevant d divides an a. For these d enumerate every such integer k.
    Exact rational c0 bounds enclose the maximum without floating comparisons.
    """
    groups = defaultdict(list)
    for a in map(int, A):
        for d in range(1, math.isqrt(a)+1):
            if a % d == 0:
                groups[d].append(a//d)
                if d*d != a:
                    groups[a//d].append(d)
    bestlo = Fraction(0)
    besthi = Fraction(0)
    witness = None
    tested = 0
    sharp_max_k = 0
    sharp_max_k_upper = 0
    for d, bs in groups.items():
        bs.sort()
        nd = len(bs)
        ps = [0]
        for b in bs:
            ps.append(ps[-1]+b)
        kmax = (nd * (1-C_HI).denominator) // (1-C_HI).numerator
        # A sharp witness also has k <= nd/(1-c0/2), within this range.
        for k in range(1, kmax+1):
            i = bisect.bisect_right(bs, k)
            j = bisect.bisect_left(bs, 4*k)
            numerator = 4*k*(k-i+j-i)-(ps[j]-ps[i])
            defect = Fraction(numerator, 4*k)
            lo = C_LO*k-defect
            hi = C_HI*k-defect
            if lo > bestlo:
                bestlo = lo
                witness = dict(d=d, k=k, defect=str(defect), nd=nd)
            besthi = max(besthi, hi)
            if defect <= C_LO*k/2:
                sharp_max_k = max(sharp_max_k, k)
            if defect <= C_HI*k/2:
                sharp_max_k_upper = max(sharp_max_k_upper, k)
            tested += 1
    return dict(lower_rational=str(bestlo), upper_rational=str(besthi),
                lower=float(bestlo), upper=float(besthi), witness=witness,
                d_count=len(groups), pairs=tested, sharp_max_k=sharp_max_k,
                sharp_max_k_upper=sharp_max_k_upper)


def p28(A, full=False):
    X = int(max(A))
    G = 1 << (max(2048, 16*X)-1).bit_length()
    hs = range(1, X+1) if full else sorted({1} | {max(1,X//d) for d in (1,2,4,8,16,32)})
    best = 0.
    rows = []
    for h in hs:
        if h == 1:
            # Every nonempty set has centerwise supremum identically one.
            rows.append([1,.5])
            best=max(best,.5)
            continue
        sup = np.zeros(G)
        step = 1 if full else max(1, h//4)
        centers = list(range(h, X+h, step))
        for m in centers:
            w = np.maximum(1-np.abs(A-m)/h, 0.)
            c = np.zeros(G)
            c[A] = w
            sup = np.maximum(sup, np.abs(np.fft.fft(c)))
        val = float(sup.mean()/2)
        rows.append([int(h), val])
        best = max(best, val)
    return dict(value=best, rows=rows, grid=G,
                all_integer_H_and_centers=full)


def metrics(A, full=False):
    A = np.array(sorted(set(map(int,A))), dtype=np.int64)
    assert len(A) and A[0] > 0
    n = len(A)
    X = int(A[-1])
    lookup = np.zeros(2*X+1, dtype=bool)
    lookup[A] = True
    H = lookup[np.abs(A[:,None]-A[None,:])].astype(float)
    e = int(H.sum())//2
    vals = eigvalsh(H, check_finite=False)
    low = vals[vals <= math.sqrt(n)]
    mu = float(low.mean())
    bd = float(low.var()/(math.sqrt(n)+abs(mu))+abs(mu))/2
    t = 3*e/n
    star = 2*n/(math.sqrt(t*t+8*n)+t)
    w2 = -bottom(np.r_[X-A, X, X+A], A, lookup)/2
    spread = p28(A, full=full)
    edge = boundary(A)
    est = min_estimate_fft(A.tolist(), oversample=32, polish=24)
    certs = dict(P28=spread['value'], W2=w2, star=star, bulk_BD=bd,
                 boundary=edge['upper'])
    return dict(n=n, X=X, gcd=int(np.gcd.reduce(A)), density=n/X,
                certs={k:v/math.sqrt(n) for k,v in certs.items()},
                maximum=max(certs.values())/math.sqrt(n),
                R_est=est.R, xmin=est.xmin, edges=e,
                triples_over_n32=e/n**1.5,
                beta1=float(np.sum(vals[np.abs(vals)<=math.sqrt(n)]**2)/n**2),
                p28=spread, boundary=edge,
                sha256=hashlib.sha256(A.astype('<i8').tobytes()).hexdigest())


def cumulative(n, X, phase=Fraction(37,100), power=1):
    # Exact cumulative mass for p_j proportional to (X-j)^power.
    out = []
    old = phase.numerator//phase.denominator
    den = sum((X-j)**power for j in range(1,X+1))
    running = 0
    for j in range(1,X+1):
        running += (X-j)**power
        new = (phase.numerator*den+n*running*phase.denominator)//(phase.denominator*den)
        assert new-old in (0,1)
        if new > old:
            out.append(j)
        old = new
    assert len(out) == n
    return np.array(out, dtype=np.int64)


def stratified(n, X, kind):
    # Inverse of the continuous triangle CDF, with reproducibly saved output.
    if kind == 'antithetic':
        phases = np.where(np.arange(n)%2 == 0, .25, .75)
    elif kind == 'thue_morse':
        phases = np.array([.25 if j.bit_count()%2 == 0 else .75 for j in range(n)])
    else:
        rng = np.random.default_rng(181801+n)
        u = .25+.5*rng.random((n+1)//2)
        phases = np.empty(n)
        phases[::2] = u
        phases[1::2] = 1-u[:n//2]
    t = (np.arange(n)+phases)/n
    A = np.floor(X*(1-np.sqrt(1-t))).astype(np.int64)+1
    assert len(np.unique(A)) == n
    return A


def seeds():
    for n in (96,256,768):
        X = round(n**(4/3)/.6)
        for power in (1,2):
            yield f'cum_p{power}_{n}', cumulative(n,X,power=power), dict(n=n,X=X,power=power)
        for kind in ('antithetic','thue_morse','pair_random'):
            yield f'{kind}_{n}', stratified(n,X,kind), dict(n=n,X=X,kind=kind)
        aa = np.arange(1,X+1,dtype=np.int64)
        q = 1000003
        for rank, steps in ((1,[618035]),(2,[618035,414215])):
            distances = np.abs((aa[:,None]*np.array(steps)+q//2)%q-q//2)
            alpha = n/X
            radii = q*(2*alpha*(1-aa/(X+1)))**(1/rank)/2
            keep = np.all(distances<radii[:,None],axis=1)
            yield f'nested_Bohr_r{rank}_{n}', aa[keep], dict(q=q,steps=steps,ntarget=n,X=X)
    for n in (96,256,768):
        parts = []
        for d in (7,11,17):
            parts.extend((d*cumulative(n//3,4*n//3)).tolist())
        yield f'dilation_union_{n}', parts, dict(dilations=[7,11,17],component_n=n//3)
    for q,k in ((31,9),(67,17),(127,28)):
        S,v = singer(q)
        S = np.array(sorted(S),dtype=np.int64)
        # Deterministic stratified selection of a tapered Singer subset.
        p = 1-np.abs(S-(v-1)/2)/((v+1)/2)
        cuts = np.cumsum(p)/sum(p)*k
        keep = np.floor(cuts+.37)>np.floor(np.r_[0.,cuts[:-1]]+.37)
        B = (S[keep]-(v-1)//2).tolist()
        yield f'singer_taper_q{q}_k{k}', A_of_S(B), dict(q=q,k=len(B),S=B,analytic_M_upper=len(B))
    rng = np.random.default_rng(181802)
    for n in (96,256,768):
        L = round(n**(4/3))
        a,p,Q = spline_prob(L)
        p = p*n/p.sum()
        keep = rng.random(len(a))<p
        k = round(n**.65)
        keep[:k] = True
        yield f'forced_thin_{n}', a[keep], dict(L=L,prefix=k,seed=181802)
    for name in ('search_smallN_36','search_taper_Bohr_r2_96_hard_window','search_singer_bu_11'):
        A = np.load(Path('.research/agents/tdense17_scratch')/(name+'.npz'))['A']
        yield 'r17_'+name, A, dict(source='round17',full_p28=bool(max(A)<=80))


def run():
    flint.ctx.prec = 200
    assert flint.arb.pi() > flint.arb(PI_LO.numerator)/PI_LO.denominator
    assert flint.arb.pi() < flint.arb(PI_HI.numerator)/PI_HI.denominator
    records = json.loads((ROOT/'adversaries.json').read_text()) if (ROOT/'adversaries.json').exists() else []
    completed = {r['name']:r for r in records}
    for name,A,meta in seeds():
        start = time.time()
        A = np.array(sorted(set(map(int,A))),dtype=np.int64)
        if name in completed:
            assert completed[name]['sha256']==hashlib.sha256(A.astype('<i8').tobytes()).hexdigest()
            continue
        np.savez_compressed(ROOT/(name+'.npz'), A=A)
        row = metrics(A,full=meta.get('full_p28',False))
        row.update(name=name,meta=meta,seconds=time.time()-start)
        records.append(row)
        (ROOT/'adversaries.json').write_text(json.dumps(records,indent=2)+'\n')
        print(json.dumps({k:row[k] for k in ('name','n','X','certs','maximum','R_est','seconds')}),flush=True)
    (ROOT/'environment.json').write_text(json.dumps(dict(python=platform.python_version(),
        numpy=np.__version__,scipy=scipy.__version__,flint=flint.__version__,
        c0_lower=str(C_LO),c0_upper=str(C_HI)),indent=2)+'\n')
    table(records)


def table(records):
    lines=['# Round 18 adversarial table','',
           'NUMERICAL P28, graph spectra, and R estimates. Boundary entries are exhaustive exact-rational upper enclosures over all d,k. All five certificate columns are divided by sqrt(n). P28 uses the stated sampled scales/centers unless marked full.','',
           '| family | n | X/n | P28 | W2 | star | bulk BD | boundary | max | R estimate |',
           '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for row in records:
        c=row['certs']
        lines.append(f"| {row['name']} | {row['n']} | {row['X']/row['n']:.3f} | {c['P28']:.6f} | {c['W2']:.6f} | {c['star']:.6f} | {c['bulk_BD']:.6f} | {c['boundary']:.6f} | {row['maximum']:.6f} | {row['R_est']:.6f} |")
    (ROOT/'adversarial_table.md').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    run()
