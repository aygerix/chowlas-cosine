r"""E30: finite-group probe for the run-top question of P19 (is |B_t| << K^{2+o(1)} in every finite abelian group?).

Γ = Z_{m_1} × ... × Z_{m_d} (all m_i odd, so a ≠ −a for a ≠ 0), t = e_1 (order m_1 >= 3). A = −A ⊂ Γ \ {0} is a union of
pairs {a, −a}; F(χ) = Σ_{a∈A} χ(a) (real), K = −min_χ F(χ) (exact enumeration of all |Γ| characters, float),
B_t = {x ∈ A : x − t ∈ A, x + t ∉ A}.  Simulated annealing on pair toggles maximises |B_t| subject to K <= K0
(penalty), for a sweep of K0; reports the frontier max|B_t|(K0) and the ratio |B_t|/K0^2.  Bedert's Prop 7.3 holds in
every finite abelian group (|B_t| << K^4); the agent's evidence suggests |B_t| <~ K^2 in groups.  UNCERTIFIED (float K,
heuristic search: lower bounds on the frontier only).
Usage: python src/group_runtop_sa.py m1,m2,...,md iters seed K0list      e.g.  3,3,3,3,3,3 200000 1 2,3,4,6,8
"""
import sys, math, itertools, json
import numpy as np

ms = [int(v) for v in sys.argv[1].split(',')]
iters, seed = int(sys.argv[2]), int(sys.argv[3])
K0s = [float(v) for v in sys.argv[4].split(',')]
rng = np.random.default_rng(seed)
G = list(itertools.product(*[range(m) for m in ms])); n = len(G)
idx = {g: i for i, g in enumerate(G)}
neg = np.array([idx[tuple((-c) % m for c, m in zip(g, ms))] for g in G])
t = tuple([1] + [0] * (len(ms) - 1))
plus_t = np.array([idx[tuple((c + s) % m for c, s, m in zip(g, t, ms))] for g in G])
minus_t = np.array([idx[tuple((c - s) % m for c, s, m in zip(g, t, ms))] for g in G])
reps = [i for i in range(1, n) if i < neg[i]]                       # one representative per pair {a, −a}
Gm = np.array(G, dtype=float); Ms = np.array(ms, dtype=float)
phase = 2 * np.pi * ((Gm[reps][:, None, :] * Gm[None, :, :]) / Ms).sum(-1)   # (pairs, characters)
C = 2 * np.cos(phase)                                               # contribution of pair to F(χ)


def runtops(ind):
    return int((ind & ind[minus_t] & ~ind[plus_t]).sum())


def run(K0, init=None):
    x = np.zeros(len(reps), bool) if init is None else init.copy()
    F = C[x].sum(0) if x.any() else np.zeros(n)
    ind = np.zeros(n, bool); ind[np.array(reps)[x]] = True; ind[neg[np.array(reps)[x]]] = True
    def score(F, ind):
        K = max(0.0, -F.min()); b = runtops(ind)
        return b - 50.0 * max(0.0, K - K0), b, K
    cur, b, K = score(F, ind); best = (b if K <= K0 + 1e-9 else -1, K, x.copy())
    T0 = 2.0
    for it in range(iters):
        T = T0 * (1 - it / iters) + 0.02
        p = int(rng.integers(len(reps))); a = reps[p]; s = -1.0 if x[p] else 1.0
        F2 = F + s * C[p]; ind[a] = ind[neg[a]] = not x[p]
        new, b2, K2 = score(F2, ind)
        if new >= cur or rng.random() < math.exp((new - cur) / T):
            x[p] = not x[p]; F = F2; cur = new
            if K2 <= K0 + 1e-9 and b2 > best[0]:
                best = (b2, K2, x.copy())
        else:
            ind[a] = ind[neg[a]] = bool(x[p])
    return best


out = []
for K0 in K0s:
    b, K, x = run(K0)
    A = [G[i] for i in np.array(reps)[x]]
    out.append(dict(K0=K0, B=b, K=K, sizeA=2 * int(x.sum()), ratio=b / max(K0, 1) ** 2))
    print(f"group Z{'xZ'.join(map(str, ms))} (|Γ|={n}) K0={K0:g}: max|B_t|={b} at K={K:.3f}, |A|={2 * int(x.sum())}, "
          f"|B_t|/K0^2={b / max(K0, 1) ** 2:.3f}", flush=True)
json.dump(dict(ms=ms, iters=iters, seed=seed, frontier=out),
          open(f"examples/group_runtop/Z{'x'.join(map(str, ms))}_s{seed}.json", 'w'))
