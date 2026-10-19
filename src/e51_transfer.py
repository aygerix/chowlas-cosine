"""E51: R3 noise-transfer ratio and secondary-spike anatomy (PROOFS P32, NOTEBOOK 2026-10-19 "per-spike contraction").
For each test set A (f = f_A, M = -min f, n = |A|, X = max A) and window scale w, with g = f * F_w (coefficients
kappa_w(a) = (1 - a/(w+1))_+):
  S   = {x : f(x) > K*M, |x| >= C/w}                       (secondary spikes of f; central window removed)
  E   = S + [-c/w, c/w]                                     (P32's neighbourhood)
  m_f = (1/2pi) int_S (f+M)^2,  m_g = (1/2pi) int_E (M+g)^2,  tot_g = M^2 + s_A/2,  s_A = sum kappa_w(a)^2
  tau = m_g / tot_g          (fraction of g's L^2 mass sitting on E: the "noise-transfer ratio")
  P32 says m_f <= Lam * m_g with Lam = rho(X+w+1) / (W - tau_c);  we report the realised m_f/m_g and Lam.
  Contraction test (NOTEBOOK): m_f/(n/2) <= Lam*tau*tot_g/(n/2); the route needs Lam*tau*tot_g < (1-eps) n/2.
Also: top secondary spikes (height/sqrt n, x/2pi, best rational p/q with q <= 64).
FFT grid; UNCERTIFIED quadrature (diagnostic only). Usage: python src/e51_transfer.py > examples/e51/e51.jsonl
"""
import json, math, sys
from fractions import Fraction
import numpy as np
sys.path.insert(0, "src")
from bu import A_of_S
from singer import singer

RHO = 0.7698                      # Beckner-Hoelder constant (P31-N asymptotic); numerical sup is 0.687
K, CEX = 2.0, 4.0                 # spike threshold K*M; central exclusion |x| >= CEX/w

def grid_vals(coef, G):
    c = np.zeros(G); c[:len(coef)] = coef
    return np.fft.fft(c).real     # value at x_j = 2 pi j / G

def analyse(name, A, out):
    A = np.asarray(sorted(set(int(a) for a in A))); X = int(A.max()); n = len(A)
    G = 16 << math.ceil(math.log2(X))
    coef = np.zeros(X + 1); coef[A] = 1.0
    f = grid_vals(coef, G); M = -f.min(); R = M / math.sqrt(n)
    x = 2 * np.pi * np.arange(G) / G; x = np.where(x > np.pi, x - 2 * np.pi, x)
    rec = dict(set=name, n=n, X=X, M=round(M, 3), R=round(R, 4), scales=[])
    for wf in (0.25, 0.5, 1.0):
        w = max(1, int(round(wf * X)))
        kap = np.clip(1 - np.arange(X + 1) / (w + 1), 0, None)
        g = grid_vals(coef * kap, G)
        sA = float((kap[A] ** 2).sum()); tot_g = M * M + sA / 2
        Wn = 1 + 2 * float((kap[1:] ** 2).sum())
        S = (f > K * M) & (np.abs(x) >= CEX / w)
        m_f = float(((f + M) ** 2 * S).mean())
        row = dict(w=w, sA=round(sA, 2), tot_g=round(tot_g, 2), secshare_f=round(m_f / (n / 2 + M * M), 4))
        for c in (3.0, 4.0, 6.0):
            r = int(math.ceil(c / w * G / (2 * np.pi)))
            # dilate S by r grid points (circular) via cumulative sums
            cs = np.concatenate([[0], np.cumsum(np.concatenate([S[-r:], S, S[:r]]).astype(np.int64))])
            E = (cs[2 * r + 1:] - cs[:-2 * r - 1]) > 0
            m_g = float(((M + g) ** 2 * E).mean())
            tauc = math.pi ** 3 * w / (3 * c ** 3)
            Lam = RHO * (X + w + 1) / max(Wn - tauc, 1e-9)
            row[f"c{int(c)}"] = dict(Emeas=round(float(E.mean()), 4), tau=round(m_g / tot_g, 4),
                                    mf_over_mg=round(m_f / m_g, 3) if m_g > 0 else None, Lam=round(Lam, 2),
                                    bound_over_half_n=round(Lam * m_g / (n / 2), 3))
        rec["scales"].append(row)
    # spike anatomy at full resolution: local maxima of f above 2 sqrt n, excluding |x| < 4/X
    lm = (f > np.roll(f, 1)) & (f >= np.roll(f, -1)) & (f > 2 * math.sqrt(n)) & (np.abs(x) >= 4.0 / X) & (x > 0)
    idx = np.nonzero(lm)[0]; idx = idx[np.argsort(-f[idx])][:12]
    sp = []
    for j in idx:
        t = x[j] / (2 * np.pi); fr = Fraction(t).limit_denominator(64)
        sp.append(dict(h=round(float(f[j]) / math.sqrt(n), 2), t=round(float(t), 6), pq=f"{fr.numerator}/{fr.denominator}",
                       off_X=round(abs(t - float(fr)) * X, 2)))
    rec["top_spikes"] = sp
    rec["n_spikes_2sqrtn"] = int(lm.sum())
    print(json.dumps(rec), file=out, flush=True)

def sets():
    S = {}
    bu = json.load(open("examples/bu_reproduction_certified.json"))
    for k in ("101_20", "199_40", "401_80"):
        S["bu_" + k] = A_of_S(bu[k]["S"])
    d = json.load(open("examples/construct/N50_certified.json")); S["dense_N50"] = d["N50_x72"]["A"]
    for q in (31, 61):                         # Singer difference sets: positive integer differences of D in [0, v)
        D, v = singer(q)
        S[f"singer_diff_q{q}"] = sorted({(a - b) for a in D for b in D if a > b})
    for l in open("examples/profile_sa/e49.jsonl"):
        r = json.loads(l)
        if r["n"] >= 290 and r["mode"] == 0 and r["p"] in (1, 3): S[f"e49_p{int(r['p'])}_n{r['n']}_{len(S)}"] = r["A"]
    for l in open("examples/profile_sa/e50.jsonl"):
        r = json.loads(l)
        if r["n"] >= 290: S[f"e50_a{-r['p']}_n{r['n']}_{len(S)}"] = r["A"]
    rng = np.random.default_rng(20261019)
    S["taper_random_X4000"] = [a for a in range(1, 4001) if rng.random() < 1 - a / 4000]
    S["random_d0.5_X4000"] = [a for a in range(1, 4001) if rng.random() < 0.5]
    return S

if __name__ == "__main__":
    for name, A in sets().items():
        analyse(name, A, sys.stdout)
