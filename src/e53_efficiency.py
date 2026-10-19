"""E53: realised efficiency of the P31 window–Nikolskii step, for f and along the low-pass recursion.
P31: W (n/2 + M^2) <= rho_L (L+1) (M^2 + s_A/2), rho_L <= 0.7698 (Beckner), numerical sup 0.687 (E48).
Realised efficiency   eff_f(w) = W (n/2 + M^2) / ((X+w+1) (M^2 + s_A/2))                (<= rho_L always).
Low-pass recursion (NOTEBOOK 2026-10-19): G = g_w (coefficients kappa_w(a) on A), next window w' = theta*w:
                      eff_g(w,theta) = W' (s_w/2 + M^2) / ((w+w'+1) (M^2 + s_ww'/2)),  s_ww' = sum kappa_w^2 kappa_w'^2.
The recursion forces the weighted front density to GROW (=> dense Chowla, M >= delta^C sqrt n) iff the relevant
efficiency is < (2/3)/(1+theta) uniformly; Nikolskii only gives rho ≈ 0.687 > 2/3. This measures the slack.
M: grid minimum on 16x oversampled FFT (UNCERTIFIED, fine for a ratio diagnostic).
Usage: python src/e53_efficiency.py > examples/e53/e53.jsonl
"""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from e51_transfer import sets

def kap(w, X):
    return np.clip(1 - np.arange(X + 1) / (w + 1), 0, None)

def Wof(w):
    k = kap(w, w); return 1 + 2 * float((k[1:] ** 2).sum())

def run(name, A, out):
    A = np.asarray(sorted(set(int(a) for a in A))); X = int(A.max()); n = len(A)
    G = 16 << math.ceil(math.log2(X)); c = np.zeros(G); c[A] = 1
    M = -np.fft.fft(c).real.min(); M2 = M * M
    rec = dict(set=name, n=n, X=X, R=round(M / math.sqrt(n), 4), eff_f={}, eff_g={})
    for wf in (1 / 16, 1 / 8, 1 / 4, 1 / 2, 1):
        w = max(1, int(round(wf * X))); kw = kap(w, X); s = float((kw[A] ** 2).sum())
        rec["eff_f"][f"{wf:g}"] = round(Wof(w) * (n / 2 + M2) / ((X + w + 1) * (M2 + s / 2)), 4)
        for th in (0.1, 0.25, 0.5):
            w2 = max(1, int(round(th * w))); k2 = kap(w2, X); s2 = float(((kw * k2)[A] ** 2).sum())
            rec["eff_g"][f"{wf:g}/{th:g}"] = round(Wof(w2) * (s / 2 + M2) / ((w + w2 + 1) * (M2 + s2 / 2)), 4)
    print(json.dumps(rec), file=out, flush=True)

if __name__ == "__main__":
    for name, A in sets().items():
        if name.startswith("random"): continue
        run(name, A, sys.stdout)
