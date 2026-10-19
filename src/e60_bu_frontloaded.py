"""E60: does the P31 escape class (front-loaded profiles) contain near-1/2 sets?  Bu's identity
f_A = rho^2 - k/2 - g/2 holds for EVERY Sidon S (src/bu.py).  Take Bu's own S (examples/bu_reproduction_certified.json)
and add a few far OUTLIERS s = +-T*m (keeping S Sidon): the core differences/sums stay near 0 while max A grows by T/L,
so A becomes front-loaded at every scale, but Bu's bound M <= k/2 + max g/2 is unchanged up to k_out.
Report: true R (grid), front ratio fr(w) = s_A(w)*3X/(n(w+1)) (1 = uniform, 2 = triangle), best P31 lower bound (E55).
M: FFT grid minimum (16x oversampled, capped at 2^28 points) (UNCERTIFIED diagnostic).  Usage: python src/e60_bu_frontloaded.py > examples/e60/e60.jsonl
"""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from bu import A_of_S

def p31_lb(A, n, X):
    out = {}
    for rho, lab in ((0.7698, "beckner"), (None, "elem"), (0.687, "num")):
        b = (0.0, 0.0)
        for w in sorted(set(max(1, int(X * t)) for t in np.geomspace(1e-4, 1, 600))):
            s = float((np.clip(1 - A / (w + 1), 0, None) ** 2).sum())
            W = 2 * (w + 1) / 3 + 1 / (3 * (w + 1))
            C = (0.811 * (X + w + 1) + 0.2367) if rho is None else rho * (X + w + 1)
            lb2 = (W * n - C * s) / (2 * (C - W))
            if lb2 > b[0]: b = (lb2, w / X)
        out[lab] = [round(math.sqrt(b[0] / n), 4), round(b[1], 5)]
    return out

if __name__ == "__main__":
    bu = json.load(open("examples/bu_reproduction_certified.json"))
    for key in ("199_40", "401_80"):
        S0 = list(bu[key]["S"]); L = max(abs(s) for s in S0)
        for T, kout in ((0, 0), (8, 2), (32, 2), (32, 4), (96, 4)):
            S = list(S0); m = 1
            while len(S) < len(S0) + kout:          # add +-T*L*(1 + small odd offset) keeping Sidon
                cand = (T * L + 7 * m) * (1 if (len(S) - len(S0)) % 2 == 0 else -1); m += 1
                try: A_of_S(sorted(S + [cand])); S.append(cand)
                except ValueError: pass
            S = sorted(S); A = np.asarray(A_of_S(S)); n = len(A); X = int(A.max()); k = len(S)
            G = min(16 << math.ceil(math.log2(X)), 1 << 28); cf = np.zeros(G); cf[A] = 1
            M = -np.fft.rfft(cf).real.min(); del cf
            fr = {f"{t:g}": round(float((np.clip(1 - A / (int(t * X) + 1), 0, None) ** 2).sum()) * 3 * X / (n * (int(t * X) + 1)), 3)
                  for t in (0.001, 0.01, 0.1, 1.0)}
            print(json.dumps(dict(base=key, T=T, k_out=kout, k=k, n=n, X=X, R=round(M / math.sqrt(n), 4), M_over_k=round(M / k, 4),
                                  front_ratio=fr, P31_LB_R=p31_lb(A, n, X))), flush=True)
