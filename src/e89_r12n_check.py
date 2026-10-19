"""E89 — lead's independent falsification test of round-12 R12-N:
  if A ∩ NZ = {N, 2N, ..., l0·N} (initial progression, possibly empty) and r = #{a mod N}, then
      M(A) >= n/((3π+2) r),   and >= 2n/((3π+2) r) when the residue counts are symmetric (l_c = l_{-c}).
Sampled grid minima only UNDER-estimate M, so a grid value above the bound is consistent; a grid value below the bound
is refined by local golden-section search before being reported as a violation. NUMERICAL (falsification only).
Families: random residue subsets with random progression lengths per class (nested and nonnested), adversarial
l0 = 3π/(3π+2)·n/(2r) (the balance point of the proof), symmetric-count variants, and small exhaustive N.
Output: examples/e89/e89.json.  Usage: src/dirun.sh -c 4 python src/e89_r12n_check.py
"""
import json
import math
import os

import numpy as np

rng = np.random.default_rng(2026101989)
C1 = 3 * math.pi + 2


def grid_min(A, oversample=16):
    X = int(max(A))
    L = 1 << int(math.ceil(math.log2(oversample * (X + 1))))
    c = np.zeros(L)
    c[np.asarray(A, int)] = 1.0
    v = np.fft.rfft(c).real  # Σ cos(2π k a / L)
    i = int(np.argmin(v))
    x0 = 2 * math.pi * i / L
    A = np.asarray(A, float)
    f = lambda x: float(np.cos(A * x).sum())
    lo, hi = x0 - 2 * math.pi / L, x0 + 2 * math.pi / L
    g = (math.sqrt(5) - 1) / 2
    for _ in range(60):
        m1, m2 = hi - g * (hi - lo), lo + g * (hi - lo)
        if f(m1) < f(m2):
            hi = m2
        else:
            lo = m1
    return min(float(v[i]), f((lo + hi) / 2))


def build(N, counts, start_offsets=None):
    """A = ∪_c {c + N j : j in J_c}; class 0 is the initial progression {N, ..., l0 N}."""
    A = []
    for c in range(N):
        l = counts[c]
        if l == 0:
            continue
        if c == 0:
            A += [N * j for j in range(1, l + 1)]
        else:
            s = 0 if start_offsets is None else start_offsets[c]
            A += [c + N * (s + j) for j in range(l)]
    return sorted(A)


def check(A, N, tag):
    A = sorted({int(a) for a in A})
    n = len(A)
    res = {a % N for a in A}
    r = len(res)
    cnt = np.bincount(np.array(A) % N, minlength=N)
    sym = all(cnt[c] == cnt[(-c) % N] for c in range(N))
    bound = (2 if sym else 1) * n / (C1 * r)
    M = -grid_min(A)
    return {"tag": tag, "N": int(N), "n": n, "r": r, "l0": int(cnt[0]), "sym": bool(sym), "X": int(max(A)), "M_grid": M,
            "bound": bound, "ratio": M / bound}


def main():
    os.makedirs("examples/e89", exist_ok=True)
    out = []
    # 1. random nested / nonnested residue schedules
    for N in (3, 5, 8, 13, 29, 64, 101):
        for trial in range(40):
            r_target = int(rng.integers(1, N + 1))
            occ = rng.choice(N, size=r_target, replace=False)
            counts = np.zeros(N, int)
            for c in occ:
                counts[c] = int(rng.integers(1, 200))
            offs = rng.integers(0, 50, size=N) if trial % 2 else None
            A = build(N, counts, offs)
            if A:
                out.append(check(A, N, "random" + ("_offset" if trial % 2 else "_nested")))
    # 2. adversarial balance point: equal counts l on r classes, l0 at the proof's balance point
    for N in (7, 16, 31, 64, 127):
        for r in sorted({1, 2, 3, N // 4, N // 2, N}):
            if r < 1:
                continue
            for l in (20, 60, 200):
                n_est = r * l
                l0 = max(0, int(round(3 * math.pi / C1 * n_est / (2 * r))))
                occ = list(range(1, r)) if r > 1 else []
                counts = np.zeros(N, int)
                counts[0] = l0
                for c in occ:
                    counts[c] = l
                A = build(N, counts)
                if A:
                    out.append(check(A, N, "balance"))
                # symmetric occupied classes
                counts = np.zeros(N, int)
                counts[0] = l0
                half = [c for c in range(1, N) if c <= N - c][: max(0, (r - 1) // 2)]
                for c in half:
                    counts[c] = l
                    counts[(-c) % N] = l
                A = build(N, counts)
                if A:
                    out.append(check(A, N, "balance_sym"))
    # 3. scan l0 at fixed other classes (worst case over l0)
    for N in (5, 12, 33):
        counts0 = np.zeros(N, int)
        occ = rng.choice(np.arange(1, N), size=max(1, N // 3), replace=False)
        for c in occ:
            counts0[c] = 100
        for l0 in range(0, 120, 4):
            counts = counts0.copy()
            counts[0] = l0
            A = build(N, counts)
            out.append(check(A, N, "l0scan"))
    worst = min(out, key=lambda d: d["ratio"])
    viol = [d for d in out if d["ratio"] < 1 - 1e-9]
    summary = {"cases": len(out), "violations": len(viol), "worst": worst,
               "worst_by_tag": {t: min((d for d in out if d["tag"] == t), key=lambda d: d["ratio"])
                                for t in sorted({d["tag"] for d in out})}}
    json.dump({"summary": summary, "cases": out}, open("examples/e89/e89.json", "w"), indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
