r"""Averaged Bedert boundary bound: numerical probes (agent bedert_avg).

Convention (Bedert/Shankar symmetric): A = S u (-S), S a set of positive integers, n = |A|,
F(x) = 1^_A(x) = sum_{a in A} e(a x) = 2 f_S(2 pi x), K = -min F = 2 M(S).
A_t = A n (A+t),  B_t = A_t \ (-A_t) = {m in A : m-t in A, m+t not in A}.

For each t (t > 0 suffices: B_{-t} = -B_t) we compute on an FFT grid of size N (UNCERTIFIED floats):
  |A_t|, |B_t|, ||1^_{A_t}||_1, ||1^_{B_t}||_1,
  Bedert v3 Lemma 7.1 decomposition 1^_{B_t} = Q1 + Q2 reproduced literally
     (T1 = max(F,0), T2 = min(F,0); truncations at F+K resp. 2(F+K)), then symmetrised,
     ell_t = ||Q1||_1, q_t = ||Q2||_2^2, ||Q2||_inf,
  the exact pointwise K-functional  Phi_t = min_s [K^2 (int (|h|-s)_+)^2 + int min(|h|,s)^2],  h = 1^_{B_t},
     (soft thresholding is the exact minimiser of K^2||Q1||_1^2 + ||h-Q1||_2^2 over all Q1),
and the local energies E_A(x) = sum_{t in A} |1^_{A_t}(x)|^2, E_B(x) = sum_{t in A}|1^_{B_t}(x)|^2.
"""
from __future__ import annotations

import json
import math
import sys
import time

import numpy as np


def sym(S):
    S = sorted(set(int(s) for s in S))
    assert S[0] > 0
    return S


def setup(S, over=16):
    S = sym(S)
    M = max(S)
    N = 1 << int(math.ceil(math.log2(over * 2 * M + 1)))
    a = np.zeros(N)
    a[np.array(S) % N] = 1.0
    a[(-np.array(S)) % N] = 1.0
    F = np.real(np.fft.ifft(a)) * N
    K = -F.min()
    return dict(S=S, N=N, a=a, F=F, K=K, n=2 * len(S))


def coef(g, N):
    return np.fft.fft(g) / N


def grid(c, N):
    return np.fft.ifft(c) * N


def trunc(g, b):
    ag = np.abs(g)
    fac = np.where(ag > b, b / np.maximum(ag, 1e-300), 1.0)
    return g * fac


def soft_K(h, K):
    """min_s K^2 (mean (|h|-s)_+)^2 + mean min(|h|,s)^2 ; exact over grid values of s."""
    v = np.sort(np.abs(h))[::-1]  # descending
    N = len(v)
    cs = np.cumsum(v)  # sum of top j values (j=1..N)
    cs2_tail = np.cumsum((v ** 2)[::-1])[::-1]  # sum_{i>=j} v_i^2
    best = cs2_tail[0] / N  # s = inf  -> Q1 = 0
    # s = v[j] (j = 1..N-1): top j values exceed s
    j = np.arange(1, N)
    s = v[1:]
    L1 = (cs[:-1] - j * s) / N
    L2 = (cs2_tail[1:] + j * s ** 2) / N
    val = K * K * L1 ** 2 + L2
    k = int(np.argmin(val))
    if val[k] < best:
        return float(val[k]), float(s[k])
    return float(best), float("inf")


def analyse(S, ts=None, over=16, max_t=None, seed=0, local_energy=True):
    st = setup(S, over)
    N, a, F, K, n = st["N"], st["a"], st["F"], st["K"], st["n"]
    Sset = set(st["S"])
    Aset = Sset | {-s for s in Sset}
    T1 = np.maximum(F, 0.0)
    T2 = np.minimum(F, 0.0)
    tau = coef(T1, N)
    FK = F + K
    if ts is None:
        ts = sorted(Sset)
    if max_t is not None and len(ts) > max_t:
        rng = np.random.default_rng(seed)
        ts = sorted(rng.choice(ts, size=max_t, replace=False).tolist())
    rows = []
    EA = np.zeros(N) if local_energy else None
    EB = np.zeros(N) if local_energy else None
    EQ = np.zeros(N) if local_energy else None
    viol = 0.0
    for t in ts:
        at = np.roll(a, t)       # a_{m-t}
        amt = np.roll(a, -t)     # a_{m+t}
        cAt = a * at
        cAmt = a * amt
        cTrip = a * at * amt
        cB = a * at * (1 - amt)
        hAt = grid(cAt, N)
        hB = grid(cB, N)
        # --- Lemma 7.1 decomposition (literal) ---
        G = grid(tau * np.roll(tau, t), N)
        U = trunc(G, FK)
        Gm = grid(tau * np.roll(tau, -t), N)
        Um = trunc(Gm, FK)
        w = grid(coef(U, N) * np.roll(tau, -t), N)
        u = trunc(w, FK)
        R1 = U + Um - 2 * u
        Smain = grid(tau * (np.roll(tau, t) - np.roll(tau, -t)), N)
        S1 = trunc(Smain, 2 * FK)
        Q1 = 0.5 * (R1 + S1)
        Q1 = 0.5 * (Q1 + np.conj(Q1[(-np.arange(N)) % N]))
        Q2 = hB - Q1
        viol = max(viol, float(np.max(np.abs(Q1) - 3 * FK)))
        absB = np.abs(hB)
        Bt = int(round(cB.sum()))
        Phi, s_opt = soft_K(hB, K)
        rows.append(dict(
            t=int(t), At=int(round(cAt.sum())), Bt=Bt,
            L1At=float(np.mean(np.abs(hAt))), L1B=float(np.mean(absB)),
            ell=float(np.mean(np.abs(Q1))), q2=float(np.mean(np.abs(Q2) ** 2)),
            q2inf=float(np.max(np.abs(Q2))), Phi=Phi,
            # pieces of Q2 that Bedert bounds in L^inf by K^2: bilinear cross terms (averageable) vs truncation remainders
            cross=float(np.mean(np.abs(hAt - G) ** 2)), Vrem=float(np.mean(np.abs(G - U) ** 2)),
        ))
        if local_energy:
            # factor 2: t and -t give the same |1^_{A_{-t}}(x)| = |1^_{A_t}(-x)|; use symmetrised energy
            EA += np.abs(hAt) ** 2 + np.abs(hAt[(-np.arange(N)) % N]) ** 2
            EB += absB ** 2 + absB[(-np.arange(N)) % N] ** 2
            aQ = np.abs(Q1)
            EQ += aQ ** 2 + aQ[(-np.arange(N)) % N] ** 2
    # exact combinatorics (all t in A, not only sampled)
    T = sum(1 for x in Aset for y in Aset if (x - y) in Aset)
    out = dict(n=n, K=float(K), maxA=max(st["S"]), N=N, nt=len(ts), T=T, Q1viol=viol)
    keys = ["At", "Bt", "L1At", "L1B", "ell", "q2", "q2inf", "Phi", "cross", "Vrem"]
    for k in keys:
        arr = np.array([r[k] for r in rows], float)
        out["avg_" + k] = float(arr.mean())
        out["max_" + k] = float(arr.max())
    out["avg_L1B2"] = float(np.mean([r["L1B"] ** 2 for r in rows]))
    out["avg_ell2"] = float(np.mean([r["ell"] ** 2 for r in rows]))
    out["avg_ratio_B_Phi"] = float(np.mean([r["Bt"] / r["Phi"] for r in rows if r["Bt"] > 0]))
    out["max_ratio_B_Phi"] = float(np.max([r["Bt"] / r["Phi"] for r in rows if r["Bt"] > 0]))
    if local_energy:
        scale = n / (2 * len(ts))  # extrapolate sampled positive t to all t in A
        EA *= scale
        EB *= scale
        EQ *= scale
        FKr = np.maximum(FK, 1e-9 * K)
        out["intEA"] = float(EA.mean())           # = sum_{t in A} |A_t| (check vs T)
        out["intEB"] = float(EB.mean())           # = sum_{t in A} |B_t|
        # Cauchy-Schwarz route for (a): sum_t ell_t^2 <= K * int (sum_t |Q1_t|^2)/(F+K)
        out["intEQ_over_FK_div_n"] = float(np.mean(EQ / FKr) / n)
        # where does the B-energy live?  fraction of int E_B on {F < K^j}
        out["EB_frac_F_lt_K"] = float(EB[F < K].sum() / EB.sum())
        out["EB_frac_F_lt_2K"] = float(EB[F < 2 * K].sum() / EB.sum())
        # pointwise: E_B(x) / (n (F(x)+K)), (F+K)-weighted average and 99th percentile
        r = EB / (n * FKr)
        out["EB_nFK_wavg"] = float(np.sum(r * FK) / np.sum(FK))
        out["EB_nFK_p99"] = float(np.quantile(r, 0.99))
    out["rows"] = rows
    return out


def summarize(name, o):
    K = o["K"]
    n = o["n"]
    d = dict(name=name, n=n, K=round(K, 3), maxA=o["maxA"], nt=o["nt"],
             logn_logK=round(math.log(n) / math.log(K), 3),
             T_over_n2K=round(o["T"] / (n * n / K), 3),
             avgB_K=round(o["avg_Bt"] / K, 3), avgB_K2=round(o["avg_Bt"] / K ** 2, 4),
             maxB_K2=round(o["max_Bt"] / K ** 2, 4),
             avgL1B2_K=round(o["avg_L1B2"] / K, 3),
             avgell=round(o["avg_ell"], 3), avgell_K=round(o["avg_ell"] / K, 3),
             avgell2_K=round(o["avg_ell2"] / K, 3),
             avgq2_K2=round(o["avg_q2"] / K ** 2, 3), maxq2inf_K2=round(o["max_q2inf"] / K ** 2, 3),
             avgcross_K2=round(o["avg_cross"] / K ** 2, 3), avgVrem_K2=round(o["avg_Vrem"] / K ** 2, 3),
             avgPhi_K=round(o["avg_Phi"] / K, 3), avgB_over_Phi=round(o["avg_ratio_B_Phi"], 3),
             maxB_over_Phi=round(o["max_ratio_B_Phi"], 3),
             Q1viol=o["Q1viol"])
    if "intEA" in o:
        d.update(intEA_over_T=round(o["intEA"] / o["T"], 3),
                 CS_a=round(o["intEQ_over_FK_div_n"], 3),
                 EBfrac_FltK=round(o["EB_frac_F_lt_K"], 3), EBfrac_Flt2K=round(o["EB_frac_F_lt_2K"], 3),
                 EB_nFK_wavg=round(o["EB_nFK_wavg"], 3), EB_nFK_p99=round(o["EB_nFK_p99"], 3))
    return d


if __name__ == "__main__":
    S = json.loads(sys.argv[1])
    t0 = time.time()
    o = analyse(S, max_t=int(sys.argv[2]) if len(sys.argv) > 2 else None)
    print(json.dumps(summarize("cli", o)), time.time() - t0)
