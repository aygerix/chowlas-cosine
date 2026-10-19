"""E110: are near-extremal sets certified by NONNEGATIVE Gram matrices? (DNN vs PSD square certificates; lead 2026-10-19)
For A ⊂ [1, X]:  f_A(θ) + λ = v(θ)* Q v(θ),  v = (e(iθ))_{i=0..X},  Q real symmetric PSD,
  Σ_i Q_{i,i+k} = ½·1_A(k)  (k = 1..X),   λ = tr Q.
  M_PSD = min tr Q over Q ⪰ 0            (= M(A) by Fejér–Riesz + SDP duality, up to solver tolerance)
  M_DNN = min tr Q over Q ⪰ 0, Q >= 0    (nonnegative Gram: no phase cancellation; diagonals k ∉ A vanish entrywise)
Every DNN Q is a valid certificate, so M <= M_DNN. Both known C*-type objects (Sidon squares / Bu; F_p^r quadrics
with subgroup blocks) are DNN-certified. Question: is M_DNN/M bounded on near-extremal sets, or do they need
cancellation? NUMERICAL SDP (solver tolerance), not a certificate.
Usage: python src/e110_dnn.py out.jsonl [names...]
"""
import sys, json, math
import numpy as np, cvxpy as cp
sys.path.insert(0, "src")

def grid_M(A, L=1 << 16):
    c = np.zeros(L); c[list(A)] = 1.0
    return float(-np.min(np.fft.rfft(c).real))

def cert(A, dnn, solver):
    X = max(A); N = X + 1; S = set(A)
    Q = cp.Variable((N, N), symmetric=True)
    cons = [Q >> 0]
    for k in range(1, N):
        cons.append(sum(Q[i, i + k] for i in range(N - k)) == (0.5 if k in S else 0.0))
    if dnn:
        cons.append(Q >= 0)
    pr = cp.Problem(cp.Minimize(cp.trace(Q)), cons)
    if solver == "CLARABEL":
        pr.solve(solver=cp.CLARABEL)
    else:
        pr.solve(solver=cp.SCS, eps=1e-7, max_iters=200000)
    Qv = Q.value
    ev = np.linalg.eigvalsh(Qv) if Qv is not None else None
    rank = int(np.sum(ev > 1e-4 * ev.max())) if ev is not None else None
    return float(pr.value), pr.status, rank

def sets():
    out = {}
    d = json.load(open("examples/construct/N50_certified.json"))
    for k, v in d.items(): out[k] = v["A"]
    d = json.load(open("examples/dense_certified.json"))
    for k, v in d.items():
        if v["maxA"] <= 200: out["dense_" + k] = v["A"]
    from singer import singer
    for q in (5, 7, 11, 13):
        D, v = singer(q); D = sorted(D)
        out[f"sidon_diff_q{q}"] = sorted({b - a for a in D for b in D if b > a})
    rng = np.random.default_rng(20261019)
    for X, p in ((80, 0.5), (120, 0.3), (160, 0.15)):
        out[f"rand_X{X}_p{p}"] = sorted(int(a) for a in np.nonzero(rng.random(X) < p)[0] + 1)
    for X in (30, 60):
        out[f"interval_{X}"] = list(range(1, X + 1))
    return out

def main():
    fn = sys.argv[1]; names = sys.argv[2:]
    S = sets()
    with open(fn, "a") as o:
        for name, A in S.items():
            if names and name not in names: continue
            A = sorted(set(A)); X = max(A); n = len(A)
            solver = "CLARABEL" if X <= 130 else "SCS"
            Mg = grid_M(A)
            mp, sp, rp = cert(A, False, solver)
            md, sd, rd = cert(A, True, solver)
            row = dict(name=name, n=n, X=X, M_grid=Mg, M_psd=mp, M_dnn=md, ratio=md / mp, R=Mg / math.sqrt(n),
                       R_dnn=md / math.sqrt(n), st=[sp, sd], rank=[rp, rd], solver=solver)
            print(json.dumps(row), flush=True); o.write(json.dumps(row) + "\n"); o.flush()

if __name__ == "__main__":
    main()
