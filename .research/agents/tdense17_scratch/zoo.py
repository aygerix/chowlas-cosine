"""Adversarial spectra and clique lower bounds; VM only, four cores maximum."""
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
import scipy
from scipy.linalg import eigvalsh

sys.path.insert(0, 'src')
from chowla import min_estimate_fft
from bu import A_of_S

ROOT = Path('.research/agents/tdense17_scratch')


def metrics(name, A, **meta):
    A = np.array(sorted(set(map(int, A))), dtype=np.int64)
    assert len(A) and A.min() > 0
    n = len(A)
    D = np.abs(A[:, None] - A[None, :])
    mask = np.zeros(int(A.max()) + 1, dtype=bool)
    mask[A] = True
    H = mask[D].astype(np.float64)
    w = eigvalsh(H, check_finite=False, driver='evr')
    d = H.sum(axis=0)
    H2 = H @ H
    t2 = int(np.sum(d))
    t3 = int(np.sum(H2 * H))
    t4 = int(np.sum(H2 * H2))
    # Two independent exact integer expressions for moments (matrix sizes modest).
    assert t2 == int(np.sum(H*H))
    assert abs(np.sum(w*w) - t2) < 1e-5 * max(1, t2)
    assert abs(np.sum(w**3) - t3) < 1e-7 * max(1, t3)
    assert abs(np.sum(w**4) - t4) < 1e-7 * max(1, t4)
    tau = math.sqrt(n)
    low = w[w <= tau]
    mu = float(low.mean())
    var = float(low.var())
    bd = var/(tau+abs(mu)) + abs(mu)
    neg2 = float(np.sum(w[w < 0]**2))
    pos = w[w > 1e-9]
    r_eff = float(pos.sum()**2 / np.sum(pos*pos)) if len(pos) else 0.
    M = -min_estimate_fft(A.tolist(), oversample=16, polish=16).fmin
    # Star extension, including sum-free adversaries.
    H0 = np.zeros((n+1, n+1))
    H0[1:, 1:] = H
    H0[0, 1:] = 1
    H0[1:, 0] = 1
    w0 = eigvalsh(H0, check_finite=False, driver='evr')
    rec = dict(name=name, n=n, X=int(A.max()), R_est=M/math.sqrt(n), K_est=2*M,
               alpha=t2/n**2, tr2=t2, tr3=t3, tr4=t4,
               tr3_n3=t3/n**3, tr4_n4=t4/n**4,
               cgw_defect=(t4-float(w[-1])**4)/n**4,
               residual4_n3=(t4-float(w[-1])**4)/n**3,
               min_over_sqrtn=float(-w[0]/tau), star_min_over_sqrtn=float(-w0[0]/tau),
               beta1=float(np.sum(w[np.abs(w)<=tau]**2)/n**2),
               beta2=float(np.sum(w[np.abs(w)<=2*tau]**2)/n**2),
               psd_distance=float(math.sqrt(neg2)/n), r_eff=r_eff,
               mu_cut=mu, variance_cut=var, bd_over_sqrtn=bd/tau,
               traceP_n32=float(pos.sum()/n**1.5),
               neg_energy_over_nK2=neg2/(n*(2*M)**2), **meta)
    print(json.dumps(rec), flush=True)
    return rec


def quadric(p, repeats, taper, seed):
    d = next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    # Balanced rank-4 GAP, base >2*coordinate radius prevents additive carry.
    h = repeats*p//2
    B = 4*h+3
    coords = np.indices((2*h+1,)*4).reshape(4,-1).T-h
    q = (coords[:,0]*coords[:,1]+coords[:,2]**2-d*coords[:,3]**2)%p
    keep = q != 0
    if taper:
        # Product triangular taper; independent symmetric-pair rounding in Z.
        probs = np.prod(1-np.abs(coords)/(h+1),axis=1)
    v = coords @ np.array([1,B,B*B,B**3],dtype=np.int64)
    keep &= v > 0
    if taper:
        keep &= np.random.default_rng(seed).random(len(v)) < probs
    A = v[keep].tolist()
    return A, dict(p=p, repeats=repeats, taper=taper, seed=seed, base=B, coord_radius=h)


def clique_search(A, seed, known=None, starts=24):
    A = np.array(sorted(set(map(int,A))),dtype=np.int64)
    S = np.r_[-A[::-1], A]
    n = len(S)
    lookup = np.zeros(2*int(A.max())+1,dtype=bool)
    lookup[A] = True
    cache = {}
    def row(v):
        v = int(v)
        if v not in cache:
            x = lookup[np.abs(S-S[v])]
            cache[v] = int.from_bytes(np.packbits(x, bitorder='little').tobytes(),'little')
        return cache[v]
    rng = np.random.default_rng(seed)
    best = []
    full = (1 << n)-1
    initial = [[]]
    if known:
        index = {int(x):i for i,x in enumerate(S)}
        for c in known:
            cc = [index[int(x)] for x in c if x and int(x) in index]
            if cc: initial.append(cc)
    for trial in range(starts + len(initial)):
        C = list(initial[trial]) if trial < len(initial) else [int(rng.integers(n))]
        candidates = full
        for v in C: candidates &= row(v)
        while candidates:
            count = candidates.bit_count()
            # Uniformly choose one candidate by its rank. Python integer operations avoid dense graphs.
            rank = int(rng.integers(count))
            bits = candidates
            for _ in range(rank): bits &= bits-1
            bit = bits & -bits
            v = bit.bit_length()-1
            C.append(v)
            candidates &= row(v)
        if len(C) > len(best): best = C
    C = [int(S[i]) for i in best]
    aset = set(A.tolist())
    assert all(abs(a-b) in aset for i,a in enumerate(C) for b in C[i+1:])
    # Add 0, which is adjacent to every vertex of Cay[S]. Report both conventions.
    return dict(clique_in_S=C, omega_S_lower=len(C), omega_global_lower=len(C)+1,
                includes_zero_extension=True, cached_rows=len(cache))


def main():
    records = []
    sm = json.load(open('examples/smallN_best.json'))
    for n in ('36','50','64','80','100'):
        if n in sm: records.append(metrics('smallN_'+n, sm[n]['A']))
    sb = json.load(open('examples/singer_bu/certified.json'))
    records.append(metrics('singer_bu_61', A_of_S(sb['61']['S'])))
    for n in (128,512):
        records.append(metrics('AP_'+str(n), range(1,n+1)))
        records.append(metrics('shifted_interval_'+str(n), range(n//2+1,3*n//2+1)))
        records.append(metrics('sumfree_odd_'+str(n), range(1,2*n,2)))
    for rank in (2,3):
        aa = np.arange(1,4097)
        theta = np.sqrt(np.array([2,3,5])[:rank])
        phases = (aa[:,None]*theta[None,:]+0.5)%1-0.5
        A = aa[np.all(np.abs(phases)<0.28,axis=1)]
        records.append(metrics('bohr_rank'+str(rank), A, rank=rank, width=0.28, cap=4096))
    for pieces in (8,32):
        # Widely separated short APs: differences between high blocks do not lie in high blocks.
        A = [10000*j+a for j in range(1,pieces+1) for a in range(1,17)]
        records.append(metrics('many_AP_'+str(pieces), A, pieces=pieces, length=16))
        A = [10000*j+a for j in range(1,pieces+1) for a in range(1,33)
             if abs((a*math.sqrt(2)+0.5)%1-0.5)<0.28
             and abs((a*math.sqrt(3)+0.5)%1-0.5)<0.28]
        records.append(metrics('many_Bohr_'+str(pieces), A, pieces=pieces))
    for p,reps,taper in ((3,1,False),(3,3,False),(3,3,True),(5,1,False),(5,1,True)):
        A,meta=quadric(p,reps,taper,seed=17)
        records.append(metrics('quadric_'+str(p)+'_'+str(reps)+'_'+str(taper), A, **meta))
    rng=np.random.default_rng(20261019)
    for alpha in (0.05,0.25,0.5):
        A=np.flatnonzero(rng.random(2048)<alpha)+1
        records.append(metrics('random_'+str(alpha), A, seed=20261019, input_density=alpha))
    A=np.load(ROOT/'spline_L512_s17.npz')['A']
    records.append(metrics('forced_spline_512',A,L=512,seed=17))
    (ROOT/'zoo.json').write_text(json.dumps(dict(numpy=np.__version__, scipy=scipy.__version__, records=records),indent=2)+'\n')
    cliques=[]
    for key in ('36','50','64','80','100'):
        if key not in sm: continue
        A=sm[key]['A']; est=min_estimate_fft(A)
        c=clique_search(A,17,starts=80)
        c.update(name='smallN_'+key, K_est=-2*est.fmin,
                 omega_global_over_K_est=c['omega_global_lower']/(-2*est.fmin))
        cliques.append(c); print(json.dumps(c),flush=True)
    for key in ('61','101','151','199'):
        D=sb[key]['S']; A=A_of_S(D); est=min_estimate_fft(A)
        known=[[3*(x-b) for x in D] for b in (D[0],D[len(D)//2],D[-1])]
        c=clique_search(A,17,known=known,starts=16)
        c.update(name='singer_bu_'+key, K_est=-2*est.fmin,
                 omega_global_over_K_est=c['omega_global_lower']/(-2*est.fmin))
        cliques.append(c); print(json.dumps({k:v for k,v in c.items() if k!='clique_in_S'}),flush=True)
    (ROOT/'cliques.json').write_text(json.dumps(cliques,indent=2)+'\n')


if __name__=='__main__': main()
