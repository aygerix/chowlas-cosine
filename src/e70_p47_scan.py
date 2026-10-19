"""E70: the full P47 high-pass window family on a zoo of sets (NUMERICAL; numerical rho = 0.687 unless --rig).
For each A and each h in {0,1,2,3,4,6,8,...} (h=0 is P31) and theta in a grid, with r = 1_A^ev - kt_h * 1_A^ev:
  bound(h,w) = sqrt( (W E - rho(L+1) S) / (2(rho(L+1) - W)) ) + |r_0|/2,   L = X + h + w,
which is a lower bound for M (P47 reformulated, NOTEBOOK 2026-10-19 night). Reports best bound / M and best / sqrt(n),
the minimizing (h, theta), and the true M (grid+Newton, numerical).
Usage: python src/e70_p47_scan.py [--rig] > examples/e70/e70_scan.jsonl"""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from box_minlam import true_min

def p47_family(A, rig=False):
    A = np.array(sorted(A)); X = int(A[-1]); n = len(A)
    hs = sorted(set([0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]) & set(range(0, X // 2 + 1)))
    best = (-1e9, None, None)
    out = []
    for h in hs:
        N = 1 << int(math.ceil(math.log2(2 * (X + h) + 8)))
        a = np.zeros(N); a[A] = 1; a[(-A) % N] = 1
        if h == 0: r = a
        else:
            k = np.arange(-h, h + 1); ker = np.zeros(N); ker[k % N] = (1 - np.abs(k) / (h + 1)) / (h + 1)
            r = a - np.real(np.fft.ifft(np.fft.fft(a) * np.fft.fft(ker)))
        r0 = r[0]; rp = r[1:X + h + 1]; E = float(np.sum(rp ** 2))
        for th in (0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.45, 0.6, 0.8, 1.0):
            w = max(1, int(round(th * X))); kw = 1 - np.arange(1, w + 1) / (w + 1)
            S = float(np.sum(kw ** 2 * rp[:w] ** 2)); W = 1 + 2 * float(np.sum(kw ** 2)); L = X + h + w
            rho = 4 / (3 * math.sqrt(3)) * (1 + 2 / math.sqrt(L + 1)) ** 3 if rig else 0.687
            num = W * E - rho * (L + 1) * S; den = 2 * (rho * (L + 1) - W)
            b = (math.sqrt(num / den) if num > 0 else 0.0) + abs(r0) / 2
            if b > best[0]: best = (b, h, th)
        out.append((h, E))
    return best, out

if __name__ == "__main__":
    rig = "--rig" in sys.argv
    zoo = json.load(open(".research/agents/tdense3_scratch/sets.json"))
    for fn in ("examples/e68/e68.jsonl", "examples/e68/e68b.jsonl"):
        for i, l in enumerate(open(fn)):
            d = json.loads(l); zoo[f"{fn.split('/')[-1]}_{i}"] = d["A"]
    for name, A in zoo.items():
        A = sorted(set(int(a) for a in A if a > 0)); n = len(A); X = A[-1]
        if X > 70000: continue
        (fm, xm), _, _ = true_min(A, over=16); M = -fm
        (b, h, th), _ = p47_family(A, rig)
        b0, _ = p47_family(A, rig) if False else (None, None)
        rec = dict(name=name, n=n, X=X, M=round(M, 4), R=round(M / math.sqrt(n), 4), best=round(b, 4), best_over_M=round(b / M, 4),
                   best_over_sqrtn=round(b / math.sqrt(n), 4), h=h, theta=th, rig=rig)
        print(json.dumps(rec), flush=True)
