# Same ILP as framework_cap.py, but the Theorem-2 constraints are imposed only for subspaces W of dimension
# k-2, k-1, k (duals of subspaces of dimension 2, 1, 0) -- a relaxation, so the optimum is still an upper bound.
# For q = 3^{m/2} these are the only potentially binding ones when 3^{k-3} - 1 + q >= 4 * #lines(dim k-3), e.g. k=6,q=27.
# Usage: python framework_cap_hi.py k q
import sys, itertools
import numpy as np
import highspy
k, q = int(sys.argv[1]), int(sys.argv[2])
def normalize(v):
    for c in v:
        if c: return tuple((x * (1 if c == 1 else 2)) % 3 for x in v)
lines = sorted({normalize(v) for v in itertools.product(range(3), repeat=k) if any(v)})
L = np.array(lines); nL = len(lines)
orth = ((L @ L.T) % 3 == 0)                      # orth[i,j]: line j lies in the hyperplane lines[i]^perp
h = highspy.Highs(); h.setOptionValue("output_flag", False); h.setOptionValue("time_limit", 1500.0)
h.setOptionValue("threads", 4)
inf = highspy.kHighsInf
for _ in range(nL): h.addVar(0, 1)
h.changeColsIntegrality(nL, np.arange(nL, dtype=np.int32), np.array([highspy.HighsVarType.kInteger] * nL))
h.changeColsCost(nL, np.arange(nL, dtype=np.int32), -np.ones(nL))
allidx = np.arange(nL, dtype=np.int32)
ncons = 0
for i in range(nL):                               # c-constraint at beta = lines[i]
    h.addRow(-2, inf, nL, allidx, 3.0 * orth[i] - 1); ncons += 1
def t2(idx, dimW):                                # 4*sum_{L in W} x_L <= |W| - 1 + q
    global ncons
    h.addRow(-inf, (3 ** dimW - 1 + q) / 4.0, len(idx), np.array(idx, np.int32), np.ones(len(idx))); ncons += 1
t2(allidx, k)
for i in range(nL): t2(np.nonzero(orth[i])[0], k - 1)
seen = set()
for i in range(nL):
    for j in range(i + 1, nL):
        # 2-dim subspace spanned by lines i, j; its perp = lines orthogonal to both
        P = frozenset(normalize(tuple((a * L[i] + b * L[j]) % 3)) for a in range(3) for b in range(3) if (a, b) != (0, 0))
        if P in seen: continue
        seen.add(P)
        t2(np.nonzero(orth[i] & orth[j])[0], k - 2)
h.run()
sol = np.round(np.array(h.getSolution().col_value)).astype(int)
N = 2 * int(sol.sum())
print(f"k={k} q={q}: #lines={nL} #constraints={ncons} status={h.modelStatusToString(h.getModelStatus())} "
      f"max|N|={N} bound={-2 * h.getInfo().mip_dual_bound:.1f}  |N|/q={N / q:.3f}")
