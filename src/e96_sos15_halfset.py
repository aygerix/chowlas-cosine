"""E96 — degree-3 'level 1.5' SOS/Sherali–Adams lower bound for cyclic half-set Chowla (prototype, NUMERICAL SDP).
Setting: q prime ≡ 1 (mod 4), h = (q−1)/2 pairs ±j (j ∈ G = Z_q^*/{±1}), x ∈ {0,1}^h, Σx = h/2,
λ_x(γ) = 2Σ_j x_j cos(2πjγ/q), K(x) = max_γ −λ_x(γ).  Relaxation SOS_{1.5}(q): pseudo-moments up to degree 3,
G-invariant (dilation averaging is legitimate: the feasible set and the objective are G-invariant and convex),
Boolean reduction, cardinality multiplied by every monomial of degree <= 2, Sherali–Adams nonnegativity of all
degree <= 3 products of x_i and (1 − x_i), moment matrix of degree <= 1 PSD, and ONE localizing matrix
L_{st} = Ẽ[(λ(1) + K) s t] (s, t ∈ {1, x_1, …, x_h}) PSD (the other γ follow by G-invariance).
K_{1.5}(q) := min K. Any genuine half-set has K >= K_{1.5}(q) (up to solver tolerance: NOT a certificate).
K multiplies pseudo-moments in L, so K is a PARAMETER: bisection over feasibility SDPs (Clarabel).
"""
import sys, json, math, itertools, numpy as np, cvxpy as cp
def red(r, q): r %= q; return min(r, q - r)
def feasible(q, Kval):
    h = (q - 1) // 2; G = list(range(1, h + 1)); inv = {j: pow(j, -1, q) for j in G}
    # degree-2 orbits: ratio class of {j,k}, j != k  -> r = red(k/j) with r ~ 1/r
    def o2(j, k):
        r = red(k * inv[j], q); return min(r, red(pow(r, -1, q), q))
    ids2 = sorted({o2(1, k) for k in G if k != 1}); I2 = {r: n for n, r in enumerate(ids2)}
    def o3(i, j, k):
        best = None
        for p, a, b in ((i, j, k), (j, i, k), (k, i, j)):
            t = tuple(sorted((red(a * inv[p], q), red(b * inv[p], q))))
            best = t if best is None or t < best else best
        return best
    ids3 = {}
    for j in G:
        for k in G:
            if 1 != j and 1 != k and j != k:
                ids3.setdefault(o3(1, j, k), len(ids3))
    psi = cp.Variable(len(ids2)); tau = cp.Variable(len(ids3)); K = Kval
    def E2(j, k): return 0.5 if j == k else psi[I2[o2(j, k)]]
    def E3(i, j, k):
        s = {i, j, k}
        if len(s) == 1: return 0.5
        if len(s) == 2: a, b = sorted(s); return E2(a, b)
        return tau[ids3[o3(i, j, k)]]
    cons = [psi >= 0, psi <= 0.5, tau >= 0]
    # cardinality: Σ_k E[x_j x_k] = h/4 ; Σ_k E[x_i x_j x_k] = (h/2) E[x_i x_j]  (use base point 1 by invariance)
    cons.append(sum(E2(1, k) for k in G) == h / 4)
    for r in ids2:
        cons.append(sum(E3(1, r, k) for k in G) == (h / 2) * E2(1, r))
    # Sherali–Adams on distinct triples (orbit representatives with base 1)
    rep3 = {}
    for j in G:
        for k in G:
            if 1 != j and 1 != k and j != k: rep3.setdefault(ids3[o3(1, j, k)], (1, j, k))
    for n, (i, j, k) in rep3.items():
        t = tau[n]; pij, pik, pjk = E2(i, j), E2(i, k), E2(j, k)
        cons += [pij - t >= 0, pik - t >= 0, pjk - t >= 0,
                 0.5 - pij - pik + t >= 0, 0.5 - pij - pjk + t >= 0, 0.5 - pik - pjk + t >= 0,
                 1 - 1.5 + pij + pik + pjk - t >= 0]
    for r in ids2:  # pairs: (1-x_i)(1-x_j) >= 0  <=>  psi >= 0 ; x_i(1-x_j) >= 0 <=> psi <= 1/2
        pass
    # moment matrix degree <= 1
    Mv = cp.Variable((h + 1, h + 1), symmetric=True)
    cons.append(Mv[0, 0] == 1)
    for a in range(h):
        cons.append(Mv[0, a + 1] == 0.5)
        for b in range(a, h): cons.append(Mv[a + 1, b + 1] == E2(G[a], G[b]))
    cons.append(Mv >> 0)
    c = {j: 2 * math.cos(2 * math.pi * j / q) for j in G}
    L00 = K + sum(c[j] * 0.5 for j in G)
    L0 = [K * 0.5 + sum(c[j] * E2(j, k) for j in G) for k in G]
    Lm = [[K * E2(j, k) + sum(c[i] * E3(i, j, k) for i in G) for k in G] for j in G]
    Lv = cp.Variable((h + 1, h + 1), symmetric=True)
    cons.append(Lv[0, 0] == L00)
    for a in range(h):
        cons.append(Lv[0, a + 1] == L0[a])
        for b in range(a, h): cons.append(Lv[a + 1, b + 1] == Lm[a][b])
    cons.append(Lv >> 0)
    prob = cp.Problem(cp.Minimize(0), cons)
    try: prob.solve(solver=cp.CLARABEL)
    except Exception as e: return False
    return prob.status in ('optimal', 'optimal_inaccurate')
def run(q, lo=0.5, hi=None, tol=1e-3):
    hi = hi or math.sqrt(q)
    assert feasible(q, hi), 'upper end infeasible'
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if feasible(q, mid): hi = mid
        else: lo = mid
    return dict(q=q, h=(q - 1) // 2, K15=hi)
if __name__ == '__main__':
    out = []
    for q in map(int, sys.argv[1:]):
        r = run(q); r['K15_over_sqrtq'] = r['K15'] / math.sqrt(q); out.append(r); print(json.dumps(r), flush=True)
