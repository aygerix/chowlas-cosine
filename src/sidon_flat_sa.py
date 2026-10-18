"""SA over Sidon sets D ⊂ [0, L], |D| = k, maximising c = min_x |F_D(x)|^2 / k (grid 32L; UNCERTIFIED).
Moves: shift one mark by ±1..3 or to a random position, keeping the Sidon property. Usage: k L iters seed"""
import sys, math, json, numpy as np
def sidon_ok(D):
    d = [a - b for a in D for b in D if a > b]
    return len(d) == len(set(d))
def cval(D, G):
    c = np.zeros(G); c[D] = 1
    return (np.abs(np.fft.rfft(c)) ** 2).min()
k, L, iters, seed = map(int, sys.argv[1:5])
rng = np.random.default_rng(seed); G = 1 << math.ceil(math.log2(32 * (L + 1)))
D = []
for x in rng.permutation(L + 1).tolist():
    if len(D) == k: break
    if sidon_ok(D + [x]): D.append(x)
cur = cval(D, G) / k; best = (cur, sorted(D))
for it in range(iters):
    T = 0.02 * (0.0005 / 0.02) ** (it / iters)
    i = int(rng.integers(k)); D2 = list(D)
    D2[i] = D2[i] + int(rng.integers(-3, 4)) if rng.random() < 0.6 else int(rng.integers(0, L + 1))
    if D2[i] < 0 or D2[i] > L or D2[i] in D or not sidon_ok(D2): continue
    new = cval(D2, G) / k
    if new >= cur or rng.random() < math.exp((new - cur) / T):
        D, cur = D2, new
        if cur > best[0]: best = (cur, sorted(D))
print(json.dumps(dict(k=k, L=L, seed=seed, c=round(best[0], 5), D=best[1])), flush=True)
