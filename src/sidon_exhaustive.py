"""Exhaustive search over Sidon sets (Golomb rulers) D = {0 = d0 < ... < d_{k-1} <= L}: maximise c(D) = min_x |F_D(x)|^2 / k.
Grid min over 64L points (UNCERTIFIED, slight overestimate of the true min possible -> c may be overestimated).
Usage: python src/sidon_exhaustive.py k L
"""
import sys, math, numpy as np


def rulers(k, L):
    out = []
    def rec(D, diffs):
        if len(D) == k:
            out.append(list(D)); return
        lo = D[-1] + 1
        for x in range(lo, L + 1):
            nd = [x - d for d in D]
            if any(d in diffs for d in nd): continue
            # remaining marks need room
            if len(D) < k - 1 and x >= L: continue
            rec(D + [x], diffs | set(nd))
    rec([0], set())
    return out


if __name__ == "__main__":
    k, L = int(sys.argv[1]), int(sys.argv[2])
    R = rulers(k, L)
    G = 1 << math.ceil(math.log2(64 * L))
    best = []
    batch = 4096
    for i in range(0, len(R), batch):
        Rb = R[i:i + batch]
        C = np.zeros((len(Rb), G))
        for r, D in enumerate(Rb): C[r, D] = 1
        P = np.abs(np.fft.rfft(C, axis=1)) ** 2
        m = P.min(axis=1) / k
        for r in np.argsort(-m)[:3]: best.append((float(m[r]), Rb[r]))
    best.sort(reverse=True)
    print(f"k={k} L={L} rulers={len(R)} best c={best[0][0]:.4f} D={best[0][1]}  2nd {best[1][0]:.4f} {best[1][1]}"
          f"  => R(D-D) >= {(1-best[0][0])/math.sqrt(2)*math.sqrt(k/(k-1)):.4f}", flush=True)
