"""P16 checks.  With T = 6S+1 and C(u) = Σ_s cos((6s+1)u):  P(x) = C(x/2), and Bu's sum is
        f_{A(S)}(2u) = C(u)^2 - C(2u)/2 - k/2.
(1) identity on random points; (2) exact 4th moment of C equals 3k^2/4 - 3k/8 (S Sidon); (3) visit lemma: every interval
of half-length h = 5/(δ-2) in x (h/2 in u) contains |P| < δ — checked on a fine FFT grid; (4) explicit P16 threshold."""
import sys, json, math, numpy as np
sys.path.insert(0, 'src')
from bu import A_of_S
d = json.load(open('examples/bu_reproduction_certified.json'))
for key in d:
    S = np.array(d[key]['S']); k = len(S); A = np.array(A_of_S(list(d[key]['S'])))
    T = np.abs(6 * S + 1); G = 1 << math.ceil(math.log2(16 * T.max() + 16))
    c = np.zeros(G); np.add.at(c, T, 1.0)
    Cu = np.real(np.fft.fft(c))                                            # C(2π j/G), j = 0..G-1 (exact up to rounding)
    m4 = (Cu ** 4).mean()                                                  # exact mean since 4·maxT < G
    us = np.random.default_rng(1).uniform(0, 2 * np.pi, 2000)
    lhs = np.cos(np.outer(2 * us, A)).sum(1)
    rhs = np.cos(np.outer(us, T)).sum(1) ** 2 - np.cos(np.outer(2 * us, T)).sum(1) / 2 - k / 2
    rates = []
    for eta in (0.1, 0.3, 0.5):
        delta = math.sqrt(eta * k / 2)
        if delta <= 2: rates.append(None); continue
        hu = 5 / (delta - 2) / 2                                           # half-length in u
        w = min(G // 2 - 1, max(1, int(hu / (2 * np.pi / G))))             # grid points per half-window (<= half period)
        small = np.abs(Cu) < delta
        cs = np.concatenate([[0], np.cumsum(np.concatenate([small, small[:2 * w]]))])
        win = cs[2 * w + 1: 2 * w + 1 + G] - cs[:G]                        # count of small points in each window
        rates.append(float((win > 0).mean()))
    print(f"{key}: k={k} id.err={np.abs(lhs-rhs).max():.1e} E C^4={m4:.3f} (3k^2/4-3k/8={0.75*k*k-0.375*k:.3f}) "
          f"windows with a visit (eta=.1,.3,.5): {rates}", flush=True)
def holds(k, L, eta):
    delta = math.sqrt(eta * k / 2)
    if delta <= 2: return False
    h = 5 / (delta - 2); r = eta / (2 * (6 * L + 1))
    return 2 * r * math.floor(math.pi / (h + r)) > 24 * math.pi / (eta ** 4 * k ** 2)
for k in (10**3, 10**4, 10**5, 10**6, 10**8, 10**10, 10**14):
    L = k * k // 2
    if not holds(k, L, 0.5): print(f"k={k:.0e} L=k^2/2: no eta <= 1/2 works"); continue
    lo, hi = 1e-9, 0.5
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if holds(k, L, mid) else (mid, hi)
    print(f"k={k:.0e} L=k^2/2: P16 gives M(A(S)) >= (1/2 - {hi:.4f}) k")
