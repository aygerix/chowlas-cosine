# Search Sidon D (|D|=k, D ⊂ [0,L]) maximising c = min_x |F_D(x)|^2 / k  (UNCERTIFIED, grid 16L + local min refine)
import numpy as np, math, sys
def minF2(D, L):
    G = 1 << math.ceil(math.log2(32 * (L+1)))
    c = np.zeros(G); c[D] = 1
    P = np.abs(np.fft.fft(c))**2
    return P.min()
def is_sidon_add(D, x, diffs):
    nd = [abs(x - d) for d in D]
    return len(set(nd)) == len(nd) and not any(d in diffs for d in nd)
def run(k, L, iters, seed):
    rng = np.random.default_rng(seed)
    # random greedy Sidon set
    while True:
        D = [0]; diffs = set()
        cand = rng.permutation(np.arange(1, L + 1))
        for x in cand:
            if len(D) == k: break
            if is_sidon_add(D, int(x), diffs):
                for d in D: diffs.add(abs(int(x) - d))
                D.append(int(x))
        if len(D) == k: break
    cur = minF2(D, L) / k; best = (cur, sorted(D))
    for it in range(iters):
        T = 0.05 * (0.002 / 0.05) ** (it / iters)
        i = int(rng.integers(len(D))); D2 = D[:i] + D[i+1:]
        diffs2 = {abs(a - b) for a in D2 for b in D2 if a != b}
        x = int(rng.integers(0, L + 1))
        if x in D2 or not is_sidon_add(D2, x, diffs2): continue
        D3 = D2 + [x]
        new = minF2(D3, L) / k
        if new >= cur or rng.random() < math.exp((new - cur) / T):
            D, cur = D3, new
            if cur > best[0]: best = (cur, sorted(D))
    return best
if __name__ == "__main__":
    for k in [5, 6, 8, 10, 12, 16]:
        res = [run(k, int(1.5 * k * k), 4000, s) for s in range(3)]
        b = max(res)
        R = (1 - b[0]) / math.sqrt(2) * math.sqrt(k / (k - 1))
        print(f"k={k} best c=min|F|^2/k={b[0]:.4f}  => R(D-D)={R:.4f}  D={b[1]}", flush=True)
