"""Corrected round 17: optimize the maximum of four certificates, VM ONLY.

All quadratures/eigenvalues here are NUMERICAL. No asymptotic conclusion follows
from this finite family. Exact count checks are in fourway_verify.py.
"""
import argparse
import hashlib
import json
import math
import platform
import sys
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigvalsh
from scipy.sparse.linalg import LinearOperator, eigsh

sys.path.insert(0, 'src')
sys.path.insert(0, '.research/agents/tdense17_scratch')
from chowla import min_estimate_fft
from probe import spline_prob
from zoo import quadric
from bu import A_of_S
from singer import singer

ROOT = Path('.research/agents/tdense17_scratch')


def bottom(W, A, lookup):
    W = np.array(sorted(set(map(int, W))), dtype=np.int64)
    m = len(W)
    if m <= 2200:
        H = lookup[np.abs(W[:, None] - W[None, :])].astype(float)
        return float(eigvalsh(H, subset_by_index=[0, 0], check_finite=False)[0])
    # Linear convolution: the padding excludes every circular alias on W.
    X = int(max(A))
    L = 1 << (int(W.max()) + X + 1).bit_length()
    c = np.zeros(L)
    c[A] = 1
    c[(-A) % L] = 1
    fc = np.fft.rfft(c)

    def mv(v):
        z = np.zeros(L)
        z[W] = np.ravel(v)
        return np.fft.irfft(np.fft.rfft(z) * fc, L)[W]

    op = LinearOperator((m, m), matvec=mv, dtype=float)
    vals = eigsh(op, k=1, which='SA', tol=2e-8, ncv=32,
                 v0=np.random.default_rng(17).normal(size=m),
                 return_eigenvectors=False, maxiter=3000)
    return float(vals[0])


def metrics(A, fine=False, include_M=True):
    A = np.asarray(sorted(set(map(int, A))), dtype=np.int64)
    n = len(A)
    assert n > 0 and A[0] > 0
    X = int(A[-1])
    rootn = math.sqrt(n)
    G = 1 << (int((8 if fine else 2) * (2*X+1))-1).bit_length()
    ds = (32, 16, 8, 4, 2, 1) if fine else (8, 4, 2, 1)
    Hs = sorted({max(1, X//d) for d in ds})
    p28 = []
    for H in Hs:
        sup = np.zeros(G)
        for m in range(H, X+H, max(1, H//(4 if fine else 2))):
            weights = np.maximum(1-np.abs(A-m)/H, 0)
            c = np.zeros(G)
            c[A] = weights
            sup = np.maximum(sup, np.abs(np.fft.fft(c)))
        p28.append([H, float(sup.mean()/2)])
    # P29(b), L=X+h. This is a finite quantitative Gibbs certificate.
    # It is a lower bound for M for every h, theta, before sampling theta.
    gibbs = []
    for h in Hs:
        c = np.zeros(G)
        c[A] = h/X - (1+h/X)*np.maximum(1-A/h, 0)
        vals = np.fft.fft(c).real
        j = int(vals.argmax())
        gibbs.append([h, max(0., float(vals[j])), j, G])
    lookup = np.zeros(2*X+1, dtype=bool)
    lookup[A] = True
    H = lookup[np.abs(A[:, None]-A[None, :])].astype(float)
    edges = int(H.sum())//2
    w = eigvalsh(H, check_finite=False)
    tau = rootn
    low = w[w <= tau]
    mu = float(low.mean())
    bd = float(low.var()/(tau+abs(mu))+abs(mu)) / 2
    t = 3*edges/n
    star = 4*n/(math.sqrt(t*t+8*n)+t)/2
    W2 = np.r_[X-A, X, X+A]
    w2 = bottom(W2, A, lookup)
    certs = dict(spread=max(v[1] for v in p28),
                 star_compression=star, graph_W2=-w2/2,
                 bulk_BD=bd, graph_A=-float(w[0])/2,
                 Gibbs_P29=max(v[1] for v in gibbs))
    # W2 contains A, so the full-graph component dominates graph_A and BD.
    objective = max(certs.values())/rootn
    out = dict(n=n, X=X, edges=edges, density=n/X,
               triple_over_n32=edges/n**1.5,
               certs={k:v/rootn for k,v in certs.items()}, objective=objective,
               p28=[[h,v/rootn] for h,v in p28],
               Gibbs=[[h,v/rootn,j,g] for h,v,j,g in gibbs],
               quadrature_G=G, fine=fine,
               beta1=float(np.sum(w[np.abs(w)<=tau]**2)/n**2),
               negative_energy=float(np.sum(w[w<0]**2)/n**2))
    if include_M:
        est = min_estimate_fft(A.tolist(), oversample=16, polish=8)
        out['R_est'] = -est.fmin/rootn
        out['xmin_est'] = est.xmin
    out['sha256_A'] = hashlib.sha256(A.astype('<i8').tobytes()).hexdigest()
    return out


def seeds():
    rng = np.random.default_rng(171701)
    for nt in (96, 256, 640):
        for factor in (0.3, 0.6, 1.2):
            alpha = factor*nt**(-1/3)
            X = round(nt/alpha)
            a = np.arange(1, X+1)
            p = 2*alpha*(1-a/(X+1))
            A = a[rng.random(X)<p]
            yield f'taper_random_{nt}_{factor}', A, dict(nt=nt, factor=factor)
    for rank in (2, 3, 4):
        for nt in (96, 256, 640):
            alpha = 0.6*nt**(-1/3)
            X = round(nt/alpha)
            a = np.arange(1, X+1)
            for variant in ('hard_window', 'smooth_round'):
                # Exact rational rotation parameters; floating comparison only
                # defines the saved finite sample, not an arithmetic theorem.
                q = 1000003
                steps = rng.integers(1, q, size=rank)
                phases = np.abs((a[:,None]*steps[None,:]+q//2)%q-q//2)/q
                if variant == 'hard_window':
                    radius = (2*alpha*(1-a/(X+1)))**(1/rank)/2
                    keep = np.all(phases<radius[:,None],axis=1)
                else:
                    radius = min(.49, (4*alpha)**(1/rank))
                    bohr = np.prod(np.maximum(1-phases/radius, 0),axis=1)
                    p = np.clip(2*alpha*(1-a/(X+1))*bohr/radius**rank,0,1)
                    keep = rng.random(X)<p
                if keep.sum() >= 10:
                    yield f'taper_Bohr_r{rank}_{nt}_{variant}', a[keep], dict(rank=rank, nt=nt, variant=variant, q=q, steps=steps.tolist())
    for L in (128, 512, 1024):
        a,p,Q = spline_prob(L)
        for power in (2/3, 5/6):
            k=round(L**power)
            keep=rng.random(len(a))<p
            keep[:k]=True
            yield f'prefix_{L}_{power:.3f}',a[keep],dict(L=L,power=power,k=k)
    for p in (3,5):
        for taper in (False, True):
            A,meta=quadric(p,1,taper,17)
            yield f'quadric_{p}_{taper}',A,meta
    for n in (96, 256):
        yield f'AP_{n}',np.arange(1,n+1),{}
        yield f'sumfree_{n}',np.arange(n+1,2*n+1),{}
        yield f'shifted_interval_{n}',np.arange(n//2+1,3*n//2+1),{}
    sm=json.load(open('examples/smallN_best.json'))
    for key in ('36','50','80','100'):
        if key in sm: yield 'smallN_'+key,sm[key]['A'],{}
    for q in (7,11,17,31):
        S,v=singer(q)
        yield 'singer_bu_'+str(q),A_of_S(sorted(S)),dict(q=q)


def run_seeds():
    records=[]
    for name,A,meta in seeds():
        begin=time.time()
        rec=metrics(A)
        rec.update(name=name,meta=meta,secs=time.time()-begin)
        np.savez_compressed(ROOT/(name+'.npz'),A=np.array(sorted(A),dtype=np.int64))
        records.append(rec)
        (ROOT/'fourway_seeds.json').write_text(json.dumps(records,indent=2)+'\n')
        print(json.dumps({k:rec[k] for k in ('name','n','objective','certs','R_est','secs')}),flush=True)


def run_search(steps):
    records=json.load(open(ROOT/'fourway_seeds.json'))
    # Search independent low-cardinality basins and one tapered Bohr basin.
    starts=sorted([r for r in records if r['n']<=330],key=lambda r:r['objective'])[:3]
    bohrs=[r for r in records if r['n']<=330 and 'Bohr' in r['name']]
    if bohrs: starts.append(min(bohrs,key=lambda r:r['objective']))
    for name in ('taper_random_96_0.6','taper_random_256_0.6',
                 'taper_Bohr_r2_96_hard_window','taper_Bohr_r3_96_hard_window',
                 'prefix_128_0.667','singer_bu_11'):
        rows=[r for r in records if r['name']==name]
        if rows and rows[0] not in starts: starts.append(rows[0])
    rng=np.random.default_rng(171702)
    output=[]
    for start in starts:
        A=np.load(ROOT/(start['name']+'.npz'))['A'].tolist()
        X=start['X']; n=len(A)
        current=metrics(A,include_M=False)
        best=current.copy(); bestA=A.copy(); history=[]
        for j in range(steps):
            aset=set(A)
            remove=int(rng.integers(n))
            add=int(rng.integers(1,X+1))
            while add in aset: add=int(rng.integers(1,X+1))
            candidate=A.copy(); candidate[remove]=add; candidate.sort()
            trial=metrics(candidate,include_M=False)
            temperature=.012*(1-j/steps)+.0005
            delta=trial['objective']-current['objective']
            accept=delta<=0 or rng.random()<math.exp(-delta/temperature)
            if accept: A=candidate; current=trial
            if trial['objective']<best['objective']:
                best=trial.copy(); bestA=candidate.copy()
                np.savez_compressed(ROOT/('search_'+start['name']+'.npz'),A=np.array(bestA,dtype=np.int64))
            if j%20==0 or j+1==steps:
                history.append(dict(step=j+1,current=current['objective'],best=best['objective']))
                print(json.dumps(dict(start=start['name'],**history[-1])),flush=True)
        fine=metrics(bestA,fine=True)
        output.append(dict(start=start['name'],seed=171702,steps=steps,
                           coarse=best,fine=fine,history=history))
        (ROOT/'fourway_search.json').write_text(json.dumps(output,indent=2)+'\n')


def audit():
    out=[]
    seedrecs=json.load(open(ROOT/'fourway_seeds.json'))
    selected=sorted(seedrecs,key=lambda r:r['objective'])[:5]
    for prefix in ('taper_random_', 'taper_Bohr_r2_', 'taper_Bohr_r3_', 'taper_Bohr_r4_', 'prefix_', 'quadric_'):
        rows=[r for r in seedrecs if r['name'].startswith(prefix)]
        if rows:
            rec=min(rows,key=lambda r:r['objective'])
            if rec not in selected: selected.append(rec)
    for rec in selected:
        A=np.load(ROOT/(rec['name']+'.npz'))['A']
        r=metrics(A,fine=True); r['name']=rec['name']; out.append(r)
        print(json.dumps(dict(name=r['name'],objective=r['objective'],certs=r['certs'],R_est=r['R_est'])),flush=True)
    (ROOT/'fourway_audit.json').write_text(json.dumps(dict(records=out,
        python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        seed=171701),indent=2)+'\n')
    lines=['### Corrected four-certificate audit','',
        'NUMERICAL only. Spread is sampled P28; W2 is full P9 on {0} union ±A; BD is the cutoff bound on A at sqrt(n); Gibbs is P29(b) restricted to L=X+h and the tested h. Every entry is divided by sqrt(n). The objective is their maximum (also including the redundant graph-A and compressed-star checks). Finer audits use h=floor(X/d), d=1,2,4,8,16,32; center step max(1,h//4); circle grid >=8(2X+1).','',
        '| seed | n | P28 | W2 | BD | Gibbs | maximum | R estimate |',
        '|---|---:|---:|---:|---:|---:|---:|---:|']
    for r in out:
        c=r['certs']
        lines.append(f"| {r['name']} | {r['n']} | {c['spread']:.6f} | {c['graph_W2']:.6f} | {c['bulk_BD']:.6f} | {c['Gibbs_P29']:.6f} | {r['objective']:.6f} | {r['R_est']:.6f} |")
    search=json.load(open(ROOT/'fourway_search.json'))
    lines+=['','NUMERICAL local search: seed 171702, 400 fixed-cardinality swap proposals per start, annealed acceptance. The optimization objective is the maximum of the certificates, not M. Every retained winner was re-evaluated with the finer parameters above.','',
        '| start | n | coarse initial | coarse winner | fine winner | fine P28 | fine W2 | fine Gibbs | R estimate |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in search:
        d=r['fine'];c=d['certs'];s=next(x for x in seedrecs if x['name']==r['start'])
        lines.append(f"| {r['start']} | {d['n']} | {s['objective']:.6f} | {r['coarse']['objective']:.6f} | {d['objective']:.6f} | {c['spread']:.6f} | {c['graph_W2']:.6f} | {c['Gibbs_P29']:.6f} | {d['R_est']:.6f} |")
        # A start that never improved is itself the winner.
        dest=ROOT/('search_'+r['start']+'.npz')
        if not dest.exists():
            A=np.load(ROOT/(r['start']+'.npz'))['A']
            assert hashlib.sha256(A.astype('<i8').tobytes()).hexdigest()==r['coarse']['sha256_A']
            np.savez_compressed(dest,A=A)
    (ROOT/'fourway_tables.md').write_text('\n'.join(lines)+'\n')


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('mode',choices=['seeds','search','audit'])
    ap.add_argument('--steps',type=int,default=160)
    args=ap.parse_args()
    if args.mode=='seeds':run_seeds()
    elif args.mode=='search':run_search(args.steps)
    else:audit()
