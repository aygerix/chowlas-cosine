# Weakly-regular RDS framework for ord t = 3: necessary conditions on the negative-sign set N (a union of lines of F_3^k):
#   (a) c-constraint:   N^(beta) >= -2 for every beta != 0        [N^(beta) = sum_L x_L (3[L in beta^perp] - 1)]
#   (b) Theorem 2 on each subgroup F_3^m x W:  |N cap W| - |W\0 \ N| <= q
# maximise |N|; the framework gives |B_t| = 3^m |N| and K = q, so |B_t|/K^3 = |N|/q.   Usage: python framework_cap.py k q
import sys, itertools
import numpy as np
import highspy
k, q = int(sys.argv[1]), int(sys.argv[2])
vecs = [v for v in itertools.product(range(3), repeat=k) if any(v)]
def normalize(v):
    for c in v:
        if c: return tuple((x * (1 if c == 1 else 2)) % 3 for x in v)
lines = sorted({normalize(v) for v in vecs}); li = {L: i for i, L in enumerate(lines)}
def span(gens):
    S = {tuple([0] * k)}
    for g in gens:
        S = {tuple((s[i] + c * g[i]) % 3 for i in range(k)) for s in S for c in range(3)}
    return frozenset(S)
subs = set(); frontier = [span([L]) for L in lines]
subs.update(frontier)
while frontier:
    nxt = []
    for S in frontier:
        for L in lines:
            if L in S: continue
            T2 = frozenset(tuple((s[i] + c * L[i]) % 3 for i in range(k)) for s in S for c in range(3))
            if T2 not in subs: subs.add(T2); nxt.append(T2)
    frontier = nxt
h = highspy.Highs(); h.setOptionValue("output_flag", False); h.setOptionValue("time_limit", 700.0)
inf = highspy.kHighsInf; nL = len(lines)
for _ in range(nL): h.addVar(0, 1)
h.changeColsIntegrality(nL, np.arange(nL, dtype=np.int32), np.array([highspy.HighsVarType.kInteger] * nL))
h.changeColsCost(nL, np.arange(nL, dtype=np.int32), -np.ones(nL))
for beta in lines:
    coef = np.array([3.0 * (sum(a * b for a, b in zip(L, beta)) % 3 == 0) - 1 for L in lines])
    h.addRow(-2, inf, nL, np.arange(nL, dtype=np.int32), coef)
for S in subs:
    idx = [li[normalize(v)] for v in S if any(v)]; idx = sorted(set(idx))
    # 2*sum - (|W|-1-2*sum) <= q  <=>  4*sum <= |W|-1+q
    h.addRow(-inf, (len(S) - 1 + q) / 4.0, len(idx), np.array(idx, np.int32), np.ones(len(idx)))
h.run()
sol = np.round(np.array(h.getSolution().col_value)).astype(int)
N = 2 * int(sol.sum())
print(f"k={k} q={q}: #lines={nL} #subspaces={len(subs)} status={h.modelStatusToString(h.getModelStatus())} "
      f"max|N|={N} bound={-2 * h.getInfo().mip_dual_bound:.1f}  |N|/q={N / q:.3f}")
print("  chosen lines:", [lines[i] for i in range(nL) if sol[i]])
