"""E108d: DOMINATION-OR-TWIN criterion for T-A2 (P75, lead 2026-10-19).
sigma = (mu + mu~)/2 (mu = stationary Parry measure on T). If Re mu^ >= 0 then phi = sigma * Lambda_r (triangle, half-width
r = b^{-k}) is a continuous PD function, maximal at 0. For u = m/b^p (k = p + N):
  I(x) := int Lambda_r(x - y) dmu(y);  phi(u) = (I(u) + I(-u))/2,  phi(0) = I(0).
  I(u) = lam^{-k} b^{-k} [ R(w 0^N) + L(w^- (b-1)^N) ],  R(v) = sum_t rho(v)_t r_t (1 - E_t),  L(v) = sum_t rho(v)_t r_t E_t,
  rho(v)_t = sum_{s: delta(s,v) = t} pi_s,  E_t = mean of the Parry measure nu_t on [0, 1].
G(u) := I(u) + I(-u) - 2 I(0) (common factor dropped). G > 0 contradicts PD directly; G = 0 gives u-periodicity; twins whose
reduced denominators have b | lcm force sigma = Lebesgue, contradiction. Either way Re mu^(j) < 0 for some j (T-A2 holds for that automaton).
Usage: python src/e108_dom.py rows.jsonl pmax out.jsonl
"""
import sys, json, os
from math import gcd
import numpy as np
from multiprocessing import Pool

NST = 40

def setup(delta, b):
    S = len(delta); Cd = np.zeros((b, S, S))
    for s in range(S):
        for d in range(b):
            t = delta[s][d]
            if t >= 0: Cd[d, s, t] = 1
    C = Cd.sum(0)
    w, V = np.linalg.eig(C); i = int(np.argmax(w.real)); lam = w[i].real; r = np.abs(V[:, i].real)
    wl, U = np.linalg.eig(C.T); il = int(np.argmax(wl.real)); pi = np.abs(U[:, il].real); pi = pi / (pi @ r)
    # E_t = sum_d (r_{delta(t,d)}/(lam r_t)) (d + E_{delta(t,d)}) / b   ->   (I - P/b) E = (P d) / b
    P = np.zeros((S, S)); pd = np.zeros(S)
    for t in range(S):
        for d in range(b):
            u = delta[t][d]
            if u >= 0:
                pr = r[u] / (lam * r[t]); P[t, u] += pr; pd[t] += pr * d
    E = np.linalg.solve(np.eye(S) - P / b, pd / b)
    return lam, r, pi, E

def tau(delta, word):
    m = list(range(len(delta)))
    for d in word:
        m = [(delta[x][d] if x >= 0 else -1) for x in m]
    return m

def rho(delta, pi, word):
    v = np.zeros(len(delta))
    for s, t in enumerate(tau(delta, word)):
        if t >= 0: v[t] += pi[s]
    return v

def digits(m, b, p):
    out = []
    for _ in range(p): out.append(m % b); m //= b
    return out[::-1]

def one(args):
    row, pmax = args
    b, delta = row["b"], row["delta"]
    try: lam, r, pi, E = setup(delta, b)
    except Exception: return dict(b=b, delta=delta, status="fail")
    z, top = [0] * NST, [b - 1] * NST
    R = lambda v: float(rho(delta, pi, v) @ (r * (1 - E)))
    Lf = lambda v: float(rho(delta, pi, v) @ (r * E))
    best = None; L = 1; twins = []
    for p in range(1, pmax + 1):
        I0 = R([0] * p + z) + Lf([b - 1] * p + top)
        for m in range(1, b ** p):
            Iu = lambda mm: R(digits(mm, b, p) + z) + Lf(digits(mm - 1, b, p) + top)
            G = (Iu(m) + Iu(b ** p - m) - 2 * I0) / max(I0, 1e-300)
            if best is None or G > best[0]: best = (G, p, m)
            if G > 1e-9:
                return dict(b=b, delta=delta, ok=True, kind="dom", G=G, p=p, m=m, lam=float(lam))
            if abs(G) < 1e-12:
                q = b ** p // gcd(m, b ** p); L = L * q // gcd(L, q); twins.append([m, p])
                if L % b == 0:
                    return dict(b=b, delta=delta, ok=True, kind="twin", twins=twins[-4:], lcm=L, lam=float(lam))
    return dict(b=b, delta=delta, ok=False, Gmax=best[0], p=best[1], m=best[2], lcm=L, lam=float(lam))

def main():
    fn, pmax, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    rows = [json.loads(l) for l in open(fn)]
    with Pool(int(os.environ.get("CHOWLA_WORKERS", "4"))) as P, open(out, "w") as o:
        for r in P.imap_unordered(one, ((r, pmax) for r in rows), chunksize=64):
            o.write(json.dumps(r) + "\n")

if __name__ == "__main__":
    main()
