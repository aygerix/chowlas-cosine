"""SA over the Bu class: S ⊂ [-L, L] Sidon, |S| = k, A(S) = {3|s_i-s_j|} ∪ {|3(s_i+s_j)+1|} (a genuine set iff S Sidon).
Objective: M(A(S)) estimated by FFT grid (UNCERTIFIED). Reports excess (M - k/2)/sqrt(k) and R = M/sqrt(k(k-1)).
Usage: python src/bu_class_sa.py k L iters seed
"""
import sys, math, json, time
import numpy as np


def A_of(S):
    k = len(S)
    return [3 * abs(S[i] - S[j]) for i in range(k) for j in range(i + 1, k)] + \
           [abs(3 * (S[i] + S[j]) + 1) for i in range(k) for j in range(i + 1, k)]


def sidon(S):
    d = [S[i] - S[j] for i in range(len(S)) for j in range(len(S)) if i != j]
    return len(set(d)) == len(d)


def Mest(A, G):
    c = np.zeros(2 * G); c[A] = 1
    return -np.fft.rfft(c).real.min()


def run(k, L, iters, seed):
    rng = np.random.default_rng(seed)
    G = 1 << math.ceil(math.log2(16 * (6 * L + 2)))
    while True:                                   # greedy random Sidon set (rejection of whole sets is hopeless for k >~ 15)
        S = []
        for x in rng.permutation(np.arange(-L, L + 1)).tolist():
            if len(S) == k: break
            if sidon(S + [x]): S.append(x)
        if len(S) == k: S = sorted(S); break
    cur = Mest(A_of(S), G); best = (cur, S)
    for it in range(iters):
        T = 0.3 * (0.003 / 0.3) ** (it / iters)
        i = int(rng.integers(k)); S2 = list(S)
        S2[i] = int(S2[i] + rng.integers(-3, 4)) if rng.random() < 0.5 else int(rng.integers(-L, L + 1))
        if S2[i] in S or abs(S2[i]) > L or not sidon(S2): continue
        new = Mest(A_of(S2), G)
        if new <= cur or rng.random() < math.exp(-(new - cur) / T):
            S, cur = S2, new
            if cur < best[0]: best = (cur, sorted(S))
    return best


if __name__ == "__main__":
    k, L, iters, seed = map(int, sys.argv[1:5])
    t = time.time(); M, S = run(k, L, iters, seed)
    print(json.dumps(dict(k=k, L=L, seed=seed, M=round(M, 5), excess=round((M - k / 2) / math.sqrt(k), 4),
                          R=round(M / math.sqrt(k * (k - 1)), 5), S=S, secs=round(time.time() - t))), flush=True)
