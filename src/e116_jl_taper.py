r"""E116: lifting a Jedwab–Li two-valued set from Z_n² to Z² (hence Z) with a JOINTLY optimised Boolean taper
(advisor's experiment, cont. 31). Lead.

Object. D = D_{a,j} ⊂ Z_n², n = p^a, an exact LS_r(n) PDS (r = p^{a−1}): D̂ ∈ {n − r, −r} off 0, ratio_G = |D|/r².
Lift. P_L = {z ∈ [−L, L]² : z mod n ∈ D} (symmetric, 0 ∉ P_L). A weight w on P_L gives the 2D cosine polynomial
    F_w(ξ) = Σ_{z ∈ P_L} w_z cos(2π z·ξ),   ξ ∈ T²,   K'(w) = −min_{T²} F_w.
A Boolean w = 1_T (T ⊂ P_L symmetric) maps to the integer set S = {z₁ + V z₂ : z ∈ T} (V > 4L), whose 1D cosine sum is
F_T restricted to the line ξ = (t, Vt); so K'_1D <= K'_2D and ratio_1D = |S|/K'_1D² >= |T|/K'_2D².
(Chowla on Z² is equivalent to Chowla on Z by this Freiman map.) R_1D = K'/√(2|T|) (ratio 2 ⟺ R = 1/2).
Measured quantities (advisor):
  (i)   ratio_G (exact on Z_n²);
  (ii)  fractional lift w = Λ(z₁/L)Λ(z₂/L) (PD taper, F_w >= −r exactly when L = n by Poisson): K'_frac, Σw², Σw²/K'²;
  (iii) Boolean: hard box (one representative per class), Bernoulli rounding of the taper, and a jointly optimised T
        (Gurobi MILP: max |T| s.t. F_T >= −Kthr at cut points; lazy cuts at incumbents' true minimisers).
All minima are NUMERICAL (FFT grid + local refinement), not interval-certified.
Usage:
  python src/e116_jl_taper.py measure p a j L [seeds]
  python src/e116_jl_taper.py milp p a j L Kthr timelimit [threads] [full]    (full: all of [−L,L]² as control)
"""
import sys, json, time, math
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, "src")
from e114_cp_group import jl_set


def lift(D, n, L, full=False):
    pts = []
    for z1 in range(-L, L + 1):
        for z2 in range(-L, L + 1):
            if (z1, z2) == (0, 0):
                continue
            if full or ((z1 % n, z2 % n) in D):
                pts.append((z1, z2))
    pairs = [z for z in pts if (z[0] > 0 or (z[0] == 0 and z[1] > 0))]  # one of each ±z
    return np.array(pairs, dtype=np.int64)


def grid_values(pairs, w, G):
    """F_w on the G×G grid, w per pair (each pair contributes 2w cos)."""
    A = np.zeros((G, G))
    np.add.at(A, (pairs[:, 0] % G, pairs[:, 1] % G), w)
    np.add.at(A, ((-pairs[:, 0]) % G, (-pairs[:, 1]) % G), w)
    return np.fft.fft2(A).real  # Σ w cos(2π z·(i,j)/G) summed over ±z


def Fval(pairs, w, xi):
    ph = 2 * np.pi * (pairs @ xi)
    return 2 * np.dot(w, np.cos(ph)), -2 * 2 * np.pi * (w * np.sin(ph)) @ pairs


def true_min(pairs, w, L, G=None, nstart=12):
    if G is None:
        G = 1 << int(math.ceil(math.log2(16 * (2 * L + 1))))
    V = grid_values(pairs, w, G)
    flat = np.argsort(V, axis=None)[: 4 * nstart]
    best = (V.flat[flat[0]], np.array(np.unravel_index(flat[0], V.shape)) / G)
    seen = []
    for idx in flat:
        x0 = np.array(np.unravel_index(idx, V.shape), dtype=float) / G
        if any(np.max(np.abs(((x0 - s + 0.5) % 1) - 0.5)) < 2.0 / G for s in seen):
            continue
        seen.append(x0)
        r = minimize(lambda x: Fval(pairs, w, x), x0, jac=True, method="BFGS", options={"gtol": 1e-10})
        if r.fun < best[0]:
            best = (r.fun, r.x % 1)
        if len(seen) >= nstart:
            break
    return float(best[0]), best[1], V, G


def finite_K(D, n):
    A = np.zeros((n, n))
    for (x, y) in D:
        A[x, y] = 1
    F = np.fft.fft2(A).real
    F[0, 0] = np.inf
    return float(-F.min())


def measure(p, a, j, L, seeds=5):
    D, n = jl_set(p, a, j)
    r = finite_K(D, n)
    out = {"p": p, "a": a, "j": j, "n": n, "L": L, "D": len(D), "K_G": r, "ratio_G": len(D) / r ** 2}
    pairs = lift(D, n, L)
    lam = (1 - np.abs(pairs[:, 0]) / L).clip(0) * (1 - np.abs(pairs[:, 1]) / L).clip(0)
    # (ii) fractional PD taper
    Kf = -true_min(pairs, lam, L)[0]
    s2 = 2 * float((lam ** 2).sum())
    out.update({"lift_points": 2 * len(pairs), "K_frac": Kf, "sumw2_frac": s2, "ratio_frac": s2 / Kf ** 2,
                "sumw_frac": 2 * float(lam.sum())})
    # (iii-a) hard box: centred representative of each class
    h = n // 2
    box = ((np.abs(pairs[:, 0]) <= h) & (np.abs(pairs[:, 1]) <= h)).astype(float)
    Kb = -true_min(pairs, box, L)[0]
    out.update({"box_size": 2 * int(box.sum()), "K_box": Kb, "ratio_box": 2 * box.sum() / Kb ** 2})
    # (iii-b) Bernoulli rounding of the taper
    rs = []
    for s in range(seeds):
        rng = np.random.default_rng(s)
        b = (rng.random(len(pairs)) < lam).astype(float)
        Kr = -true_min(pairs, b, L)[0]
        rs.append((2 * int(b.sum()), Kr, 2 * b.sum() / Kr ** 2))
    out["bernoulli"] = rs
    return out


def milp(p, a, j, L, Kthr, tl, threads=8, full=False):
    import gurobipy as gp
    from gurobipy import GRB
    D, n = jl_set(p, a, j)
    pairs = lift(D, n, L, full=full)
    P = len(pairs)
    m = gp.Model()
    m.Params.OutputFlag = 0
    m.Params.TimeLimit = tl
    m.Params.Threads = threads
    m.Params.LazyConstraints = 1
    m.Params.IntFeasTol = 1e-9
    m.Params.FeasibilityTol = 1e-8
    x = m.addVars(P, vtype=GRB.BINARY)
    # initial cuts: grid of spacing 1/(2L+1) on the half torus
    g = 2 * L + 1
    cuts = [(i / g, k / g) for i in range(g) for k in range(g) if (i, k) != (0, 0) and (i, k) <= ((-i) % g, (-k) % g)]
    def addcut(xi, lazy=None):
        c = 2 * np.cos(2 * np.pi * (pairs @ np.array(xi)))
        expr = gp.quicksum(float(c[t]) * x[t] for t in range(P))
        if lazy is None:
            m.addConstr(expr >= -Kthr)
        else:
            lazy.cbLazy(expr >= -Kthr)
    for xi in cuts:
        addcut(xi)
    m.setObjective(gp.quicksum(x[t] for t in range(P)), GRB.MAXIMIZE)
    stats = {"lazy": 0, "inc": []}
    t0 = time.time()

    def cb(model, where):
        if where == GRB.Callback.MIPSOL:
            v = np.array(model.cbGetSolution([x[t] for t in range(P)]))
            w = (v > 0.5).astype(float)
            fmin, xi, V, G = true_min(pairs, w, L, nstart=6)
            if fmin < -Kthr - 1e-7:
                addcut(tuple(xi), model)
                stats["lazy"] += 1
                # also the worst grid local minima
                flat = np.argsort(V, axis=None)[:5]
                for idx in flat:
                    if V.flat[idx] < -Kthr - 1e-7:
                        addcut(tuple(np.array(np.unravel_index(idx, V.shape)) / G), model)
                        stats["lazy"] += 1
            else:
                stats["inc"].append((round(time.time() - t0, 1), 2 * int(w.sum()), round(-fmin, 6)))

    m.optimize(cb)
    out = {"p": p, "a": a, "j": j, "n": n, "L": L, "full": full, "Kthr": Kthr, "pairs": P, "status": m.Status,
           "seconds": round(time.time() - t0, 1), "bound_T": 2 * m.ObjBound if m.SolCount or True else None,
           "lazy": stats["lazy"], "incumbents": stats["inc"][-5:]}
    if m.SolCount:
        w = np.array([x[t].X > 0.5 for t in range(P)], dtype=float)
        fmin, xi, _, _ = true_min(pairs, w, L, G=1 << int(math.ceil(math.log2(32 * (2 * L + 1)))), nstart=20)
        T = int(2 * w.sum())
        out.update({"T": T, "K_true": -fmin, "ratio": T / fmin ** 2, "R1D_upper": -fmin / math.sqrt(2 * T),
                    "ratio_bound_at_Kthr": out["bound_T"] / Kthr ** 2,
                    "T_pairs": pairs[w > 0.5].tolist()})
    return out


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "measure":
        p, a, j, L = (int(t) for t in sys.argv[2:6])
        seeds = int(sys.argv[6]) if len(sys.argv) > 6 else 5
        print(json.dumps(measure(p, a, j, L, seeds)), flush=True)
    elif cmd == "milp":
        p, a, j, L = (int(t) for t in sys.argv[2:6])
        Kthr, tl = float(sys.argv[6]), float(sys.argv[7])
        th = int(sys.argv[8]) if len(sys.argv) > 8 else 8
        full = len(sys.argv) > 9 and sys.argv[9] == "full"
        print(json.dumps(milp(p, a, j, L, Kthr, tl, th, full)), flush=True)
