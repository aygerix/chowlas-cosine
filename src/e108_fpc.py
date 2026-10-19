"""E108: FINITE-PREFIX CERTIFICATE (advisor, 2026-10-19) for automatic sets, in ball arithmetic (python-flint arb/acb).

Primitive deterministic digit automaton (base b, transitions delta, start s0 = 0), Perron root lam, right eigenvector r
(r_{s0} = 1). Parry measure nu from s0: cylinder [w], |w| = h, has mass q_w = lam^{-h} r_{s(w)}; left endpoint u_w.
    |nu^(t) - sum_w q_w e(t u_w)| <= 2 pi |t| / b^h,
    sum_w q_w e(t u_w) = lam^{-h} e_{s0}^T M(t/b) M(t/b^2) ... M(t/b^h) r,   M(y)_{st} = sum_{d: delta(s,d)=t} e(d y).
If Re(sum) + 2 pi |t| / b^h < 0 then Re nu^(t) < 0, so M(A_L) >= (|Re nu^(t)| - o(1)) |A_L| (A_L/b^L -> nu weakly,
C primitive). Everything below is rigorous (arb balls) except the float search that proposes t.
Usage:
  python src/e108_fpc.py one '<delta json>' b t_num t_den h
  python src/e108_fpc.py batch file.jsonl out.jsonl      (rows with keys b, delta; proposes t by a float scan)
"""
import sys, json, math, os
import numpy as np
from flint import fmpz_mat, arb, acb, arb_mat, acb_mat, fmpq, ctx
from multiprocessing import Pool
ctx.prec = 128

def perron(delta, b):
    S = len(delta)
    C = [[0] * S for _ in range(S)]
    for s in range(S):
        for d in range(b):
            t = delta[s][d]
            if t >= 0: C[s][t] += 1
    roots = [z for z, m in fmpz_mat(C).charpoly().complex_roots()]
    roots.sort(key=lambda z: float(z.real.mid()), reverse=True)
    lam = roots[0].real
    if len(roots) > 1 and not (lam.lower() > roots[1].real.upper()):
        return None   # Perron root not isolated by real part (imprimitive or unresolved)
    # r: (C - lam I) r = 0 with r_0 = 1; drop row 0, unknowns r_1..r_{S-1}
    if S == 1:
        return lam, [arb(1)], C
    N = [[arb(C[i][j]) - (lam if i == j else arb(0)) for j in range(1, S)] for i in range(1, S)]
    rhs = [[-arb(C[i][0])] for i in range(1, S)]
    try:
        sol = arb_mat(N).solve(arb_mat(rhs))
    except Exception:
        return None
    r = [arb(1)] + [sol[i, 0] for i in range(S - 1)]
    return lam, r, C

def certify(delta, b, tq, h):
    pr = perron(delta, b)
    if pr is None: return None
    lam, r, C = pr
    S = len(delta)
    v = [acb(1) if s == 0 else acb(0) for s in range(S)]
    for i in range(1, h + 1):
        y = tq / fmpq(b ** i)
        nv = [acb(0)] * S
        for s in range(S):
            if v[s] == 0: continue
            for d in range(b):
                t = delta[s][d]
                if t >= 0:
                    nv[t] += v[s] * acb(arb(2 * d * y)).exp_pi_i()
        v = nv
    val = sum((v[s] * r[s] for s in range(S)), acb(0)) / lam ** h
    err = 2 * arb.pi() * arb(abs(tq)) / arb(b) ** h
    ub = val.real + err
    return dict(sum_re=[float(val.real.lower()), float(val.real.upper())], err=float(err.upper()),
                bound_upper=float(ub.upper()), certified=bool(ub.upper() < 0), lam=float(lam.mid()))

def nu_float(delta, b, s):
    S = len(delta); Cd = np.zeros((b, S, S))
    for a in range(S):
        for d in range(b):
            t = delta[a][d]
            if t >= 0: Cd[d, a, t] = 1
    C = Cd.sum(0); w, V = np.linalg.eig(C); i = int(np.argmax(w.real)); lam = w[i].real; r = np.abs(V[:, i].real)
    m = int(math.ceil(math.log(max(s.max(), 1) * 1e7) / math.log(b)))
    vec = np.tile(r.astype(complex), (s.size, 1))
    for k in range(m, 0, -1):
        ph = np.exp(2j * np.pi * np.outer(s / b ** k, np.arange(b)))
        vec = np.einsum('pd,dst,pt->ps', ph, Cd, vec) / lam
    return vec[:, 0] / r[0]

def batch_one(row):
    b, delta = row["b"], row["delta"]
    s = np.arange(0.02, 20.0, 0.02)
    try: nu = nu_float(delta, b, s)
    except Exception: return dict(b=b, delta=delta, status="float_fail")
    j = int(np.argmin(nu.real)); val = float(nu.real[j])
    if val >= 0: return dict(b=b, delta=delta, status="no_negative_found", min_re=val)
    tq = fmpq(int(round(s[j] * 50)), 50)
    tf = float(tq.p) / float(tq.q)
    h = max(4, int(math.ceil(math.log(2 * math.pi * tf / (0.25 * abs(val))) / math.log(b))))
    res = certify(delta, b, tq, h)
    if res is None: return dict(b=b, delta=delta, status="perron_fail")
    res.update(b=b, delta=delta, t=f"{tq.p}/{tq.q}", h=h, float_re=val, status="ok")
    return res

def main():
    if sys.argv[1] == "one":
        delta = json.loads(sys.argv[2]); b = int(sys.argv[3]); tq = fmpq(int(sys.argv[4]), int(sys.argv[5])); h = int(sys.argv[6])
        print(json.dumps(certify(delta, b, tq, h)))
    else:
        rows = [json.loads(l) for l in open(sys.argv[2])]
        W = int(os.environ.get("CHOWLA_WORKERS", "4"))
        with Pool(W) as P, open(sys.argv[3], "w") as out:
            for r in P.imap_unordered(batch_one, rows, chunksize=16):
                out.write(json.dumps(r) + "\n"); out.flush()

if __name__ == "__main__":
    main()
