"""E108b: is the STATIONARY Parry measure mu of a sparse primitive digit automaton ever positive definite?  (T-A2)
mu^(t) = pi^T prod_{i>=1} (M(t/b^i)/lam) r   (pi^T r = 1),  M(y) = sum_d C_d e(d y).
Along t = b^m j, nu^(t) -> mu^(j) (nu = Parry measure from s0), so Re mu^(j) < 0 for some integer j forces an FPC failure
at large t. Here: m_J := min_{1 <= j <= J} Re mu^(j) (float), and the minimiser.
Usage: python src/e108_mu.py rows.jsonl J out.jsonl
"""
import sys, json, math, os
import numpy as np
from multiprocessing import Pool

J = 1

def mu_hat(delta, b, js):
    S = len(delta); Cd = np.zeros((b, S, S))
    for a in range(S):
        for d in range(b):
            t = delta[a][d]
            if t >= 0: Cd[d, a, t] = 1
    C = Cd.sum(0)
    w, V = np.linalg.eig(C); i = int(np.argmax(w.real)); lam = w[i].real; r = np.abs(V[:, i].real)
    wl, U = np.linalg.eig(C.T); il = int(np.argmax(wl.real)); pi = np.abs(U[:, il].real); pi = pi / (pi @ r)
    m = int(math.ceil(math.log(max(js.max(), 1) * 1e8) / math.log(b)))
    vec = np.tile(r.astype(complex), (js.size, 1))
    for k in range(m, 0, -1):
        ph = np.exp(2j * np.pi * np.outer(js / b ** k, np.arange(b)))
        vec = np.einsum('pd,dst,pt->ps', ph, Cd, vec) / lam
    return vec @ pi, lam

def one(row):
    b, delta = row["b"], row["delta"]
    js = np.arange(1, J + 1, dtype=float)
    try: mu, lam = mu_hat(delta, b, js)
    except Exception: return dict(b=b, delta=delta, status="fail")
    k = int(np.argmin(mu.real))
    return dict(b=b, delta=delta, lam=float(lam), minRe=float(mu.real[k]), jmin=int(js[k]), mu1=[float(mu[0].real), float(mu[0].imag)])

def main():
    global J
    fn, J, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    rows = [json.loads(l) for l in open(fn)]
    with Pool(int(os.environ.get("CHOWLA_WORKERS", "4"))) as P, open(out, "w") as o:
        for r in P.imap_unordered(one, rows, chunksize=32):
            o.write(json.dumps(r) + "\n")

if __name__ == "__main__":
    main()
