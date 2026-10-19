"""E104: do the best known sets drift into the spiky (C*) regime as n grows?
For every stored near-extremizer compute R = M/sqrt(n), the bulk fractions beta_K = int_{f<=K sqrt n} f^2 / int f^2
(K = 1, 2, 3; Conjecture SB says beta_K >= c > 0), the bimodality lambda_half = |{f <= -M/2}| and the effective
support eta = (int|f|)^2 / int f^2. NUMERICAL (FFT grid 2^ceil(log2(64 X)), Newton-polished minimum). Writes
examples/e104/e104.jsonl. Question: does beta_2 (or eta) of the optima decrease with n (spiky extremizers), or stay flat?
"""
import json, math, sys
import numpy as np
sys.path.insert(0, 'src')
from singer import singer

def stats(A):
    A = np.array(sorted(set(A))); n = len(A); X = int(A.max())
    G = 1 << math.ceil(math.log2(64 * X))
    c = np.zeros(G); c[A] = 1.0
    f = np.real(np.fft.fft(c))
    i = int(np.argmin(f)); x = 2 * math.pi * i / G; Af = A.astype(float)
    for _ in range(40):
        d1 = -(Af * np.sin(Af * x)).sum(); d2 = -(Af * Af * np.cos(Af * x)).sum()
        if d2 <= 0: break
        st = d1 / d2; x -= st
        if abs(st) < 1e-15: break
    M = -min(float(np.cos(Af * x).sum()), float(f.min()))
    f2 = f * f; tot = f2.sum(); sq = math.sqrt(n)
    out = dict(n=n, X=X, R=M / sq, M=M)
    for K in (1, 2, 3):
        out[f'beta{K}'] = float(f2[f <= K * sq].sum() / tot)
    out['lambda_half'] = float((f <= -M / 2).mean())
    out['eta'] = float(np.abs(f).mean() ** 2 / f2.mean())
    out['spike_share_top1pct'] = float(np.sort(f2)[-max(1, G // 100):].sum() / tot)
    return out

rows = []
d = json.load(open('examples/smallN_best.json'))
for k in sorted(d, key=int):
    r = stats(d[k]['A']); r['family'] = 'smallN_best'; rows.append(r)
d = json.load(open('examples/dense_certified.json'))
for k in sorted(d):
    r = stats(d[k]['A']); r['family'] = 'dense_certified:' + k; rows.append(r)
for q in (7, 11, 13, 19, 23, 31, 43, 61):
    D, v = singer(q); D = sorted(D)
    r = stats(sorted({abs(a - b) for a in D for b in D if a != b})); r['family'] = f'singer_diff_q{q}'; rows.append(r)
try:
    from bu import bu_set_S, A_of_S
    for q in (61, 83, 101):
        D, v = singer(q); c = (v - 1) // 2; L = c + 1; rr = math.ceil(3 * math.sqrt(q))
        Ds = sorted(x % v for x in D); odd = sorted([x for x in Ds if (x - c) % 2], key=lambda x: abs(x - c))
        rest = [x for x in Ds if x not in set(odd[:rr])]; Mw = sum(1 - abs(x - c) / L for x in rest)
        S, _ = bu_set_S(q, int(0.8 * Mw), seed=1, D=D, v=v)
        r = stats(A_of_S(S)); r['family'] = f'bu_q{q}'; rows.append(r)
except Exception as e:
    print('bu skipped:', e)
with open('examples/e104/e104.jsonl', 'w') as fo:
    for r in rows:
        fo.write(json.dumps(r) + '\n')
        print(f"{r['family']:28s} n={r['n']:5d} X={r['X']:6d} R={r['R']:.4f} b1={r['beta1']:.3f} b2={r['beta2']:.3f} "
              f"b3={r['beta3']:.3f} lam={r['lambda_half']:.3f} eta={r['eta']:.3f} top1={r['spike_share_top1pct']:.3f}", flush=True)
