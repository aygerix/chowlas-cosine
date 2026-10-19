"""E67 zoo: bulk fraction beta_K(A) = int_{f<=K sqrt n} f^2 / int f^2 (Conjecture SB, NOTEBOOK 2026-10-19 late) for the
project's set families. Grid: FFT on 2^ceil(log2(64 X)) points of [0, 2pi). NUMERICAL. Then the SA driver.
Usage: python src/e67_zoo.py [--sa]"""
import json, math, os, subprocess, sys
import numpy as np
sys.path.insert(0, "src")
from singer import singer
OUT = "examples/e67/e67_zoo.jsonl"

def bulk(A, Ks=(1, 2, 3)):
    X = max(A); G = 1 << math.ceil(math.log2(64 * X))
    c = np.zeros(G); c[A] = 1
    f = np.fft.rfft(c).real                      # f(2 pi j/G), j = 0..G/2 (f even)
    w = np.ones(len(f)); w[0] = w[-1] = 0.5
    den = (w * f * f).sum(); n = len(A)
    return {f"beta{K}": float((w * f * f * (f <= K * math.sqrt(n))).sum() / den) for K in Ks} | \
           {"M_grid": float(-f.min()), "R_grid": float(-f.min() / math.sqrt(n)), "n": n, "X": X}

def bu(q):
    S0, v = singer(q); best = None
    for c in range(-max(S0) // 2 - 20, -max(S0) // 2 + 21):
        S = [s + c for s in S0]
        D = sorted({b - a for a in S for b in S if b > a}); E = sorted({abs(3 * (a + b) + 1) for i, a in enumerate(S) for b in S[i + 1:]})
        A = sorted(set(3 * d for d in D) | set(E)); r = bulk(A)
        if best is None or r["M_grid"] < best[1]["M_grid"]: best = (A, r)
    return best

def cumround(p, X, sigma=0.37):
    t = np.arange(1, X + 1) / X; Phi = np.cumsum(p(t)); U = np.floor(sigma + Phi)
    U0 = np.concatenate([[0.0], U[:-1]]); return (np.nonzero(U - U0 > 0)[0] + 1).tolist()

def rec(name, A, **kw):
    r = bulk(A) | {"family": name} | kw
    print(json.dumps(r), flush=True)
    with open(OUT, "a") as fh: fh.write(json.dumps(r) + "\n")

if __name__ == "__main__":
    os.makedirs("examples/e67", exist_ok=True)
    rng = np.random.default_rng(20261019)
    for n in (256, 1024, 4096):
        rec("interval", list(range(1, n + 1)))
        rec("random_dense_1/3", sorted(rng.choice(np.arange(1, 3 * n + 1), n, replace=False).tolist()))
        rec("random_sparse_1/50", sorted(rng.choice(np.arange(1, 50 * n + 1), n, replace=False).tolist()))
        X = 6 * n; rec("cumround_half(1-t)^2", cumround(lambda t: 0.5 * (1 - t) ** 2, X))
        X = 2 * n; rec("cumround_(1-t)", cumround(lambda t: 1 - t, X))
        L = n // 8; rec("multidilate_primes", sorted({p * j for p in (11, 13, 17, 19, 23, 29, 31, 37) for j in range(1, L + 1)}))
    for q in (7, 11, 13, 17, 23, 31):
        A, r = bu(q); rec("Bu_Singer", A, q=q)
    for fn in ("examples/construct/N50_certified.json",):
        if os.path.exists(fn):
            d = json.load(open(fn)); A = d.get("A") or d.get("set") or d
            if isinstance(A, list): rec("N50_certified", sorted(A))
    if os.path.exists("examples/smallN_best.json"):
        d = json.load(open("examples/smallN_best.json"))
        items = d.items() if isinstance(d, dict) else enumerate(d)
        for k, v in items:
            A = v.get("A") if isinstance(v, dict) else v
            if isinstance(A, list) and len(A) >= 20: rec("smallN_best", sorted(A), key=str(k))
    if "--sa" in sys.argv:
        subprocess.run(["cc", "-O3", "-march=native", "-o", "src/.build/e67_bulk_sa", "src/e67_bulk_sa.c", "-lm"], check=True)
        for (X, n) in ((256, 64), (512, 64), (1024, 128), (4096, 64)):
            for K in (1.0, 2.0):
                r = subprocess.run(["src/.build/e67_bulk_sa", str(X), str(n), str(K), "4000000", "3", str(X + n)],
                                   capture_output=True, text=True, check=True)
                for line in r.stdout.splitlines():
                    d = json.loads(line); d["family"] = "SA_min_beta"
                    print(json.dumps({k: v for k, v in d.items() if k != "A"}), flush=True)
                    with open("examples/e67/e67_sa.jsonl", "a") as fh: fh.write(json.dumps(d) + "\n")
