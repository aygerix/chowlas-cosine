"""E69b: numerical audit of P47 (bounded-discrepancy rounding + smoothing-defect filter H = 1 - K_h/K_h(0) + window).
For a 0/1 sequence a (j=1..X) and profile P_j = p(j/X):
  beta = a - P, D0 = max prefix |sum beta|;  G = H f_beta has coefficients gamma = beta_ev - kt*beta_ev (kt = Fejér/(h+1));
  E = sum_{j>=1} gamma_j^2, S = sum_{j<=w} kappa_w(j)^2 gamma_j^2, W = sum kappa_w^2, L = X + h + w;
  U = sup_x H f_p (FFT, numerical) and its P47 bound pi^2 * sum|D2 P| * h(h+2)/96;
  P47:  M >= sqrt( (W E - rho(L+1) S) / (2(rho(L+1) - W)) ) - U - gamma_0/2.
Prints the bound (rigorous rho and numerical rho=0.687) beside the true M (grid+Newton). NUMERICAL audit only."""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from box_minlam import true_min
rng = np.random.default_rng(7)

def walk(p, D0):
    a = np.zeros(len(p), int); D = 0.0
    for m, pm in enumerate(p):
        want = rng.random() < pm
        if want and D + 1 - pm > D0: want = False
        if (not want) and D - pm < -D0: want = True
        a[m] = want; D += a[m] - pm
    return a

def audit(a, P, h, theta):
    X = len(a); beta = a - P; D0 = np.abs(np.cumsum(beta)).max()
    N = 1 << int(math.ceil(math.log2(8 * (X + h + 2))))
    # even extensions on Z (index j -> j mod N), beta_0 = 0, P_0 := p(0) for Phi
    be = np.zeros(N); be[1:X + 1] = beta; be[N - X:] = beta[::-1]
    k = np.arange(-h, h + 1); kt = (1 - np.abs(k) / (h + 1)) / (h + 1)
    ker = np.zeros(N); ker[k % N] = kt
    conv = np.real(np.fft.ifft(np.fft.fft(be) * np.fft.fft(ker)))
    gam = be - conv
    E = float(np.sum(gam[1:X + h + 1] ** 2)); g0 = float(gam[0])
    w = int(theta * X); kw = 1 - np.arange(1, w + 1) / (w + 1)
    S = float(np.sum(kw ** 2 * gam[1:w + 1] ** 2)); W = 1 + 2 * float(np.sum(kw ** 2)); L = X + h + w
    # smooth part: f_p(x) = sum_j P_j cos jx; H f_p on fine grid
    cP = np.zeros(N); cP[1:X + 1] = P
    fp = np.real(np.fft.fft(cP))                         # sum_j P_j e^{-ij x_k}, real part = f_p(x_k), x_k = 2 pi k/N
    xs = 2 * np.pi * np.arange(N) / N
    Hx = 1 - (np.sin((h + 1) * xs / 2) ** 2 / np.maximum(np.sin(xs / 2) ** 2, 1e-300)) / (h + 1) ** 2; Hx[0] = 0.0
    U = float(np.max(Hx * fp))
    Pz = np.concatenate([P[::-1], [P[0] if False else 0.0], P])  # placeholder (not used)
    Pev = np.zeros(2 * X + 3); Pev[X + 1] = 2 * P[0] - P[1]  # extrapolated p(0)
    Pev[X + 2:2 * X + 2] = P; Pev[1:X + 1] = P[::-1]
    d2 = float(np.sum(np.abs(np.diff(Pev, 2))))
    Ub = math.pi ** 2 * d2 * h * (h + 2) / 96
    out = {}
    for name, rho in (("rig", 4 / (3 * math.sqrt(3)) * (1 + 2 / math.sqrt(L + 1)) ** 3), ("num", 0.687)):
        num = W * E - rho * (L + 1) * S; den = 2 * (rho * (L + 1) - W)
        mp = math.sqrt(num / den) if num > 0 else 0.0
        out[name] = mp - U - g0 / 2
    ener = float(np.sum(beta ** 2)); epr = float(np.sum(P * (1 - P)))
    return dict(D0=round(float(D0), 2), E=round(E, 1), S=round(S, 1), W=round(W, 1), U=round(U, 3), Ubound=round(Ub, 2),
                g0=round(g0, 4), bound_rig=round(out["rig"], 2), bound_num=round(out["num"], 2),
                beta2=round(ener, 1), sum_e=round(epr, 1))

PROF = {"half(1-t)^2": lambda t: 0.5 * (1 - t) ** 2, "(1-t)": lambda t: 1 - t, "0.9(1-t)^2": lambda t: 0.9 * (1 - t) ** 2,
        "flat0.3": lambda t: 0.3 + 0 * t}
for name, pf in PROF.items():
    for X in (4096, 16384):
        P = pf(np.arange(1, X + 1) / X)
        for D0 in (1, 4, 16):
            a = walk(P, D0); A = (np.nonzero(a)[0] + 1).tolist()
            (fm, xm), _, _ = true_min(A, over=16)
            for h in (2 * D0 + 2, 8 * D0):
                for theta in (0.1, 0.3, 0.6):
                    r = audit(a.astype(float), P, h, theta)
                    rec = dict(profile=name, X=X, D0target=D0, h=h, theta=theta, n=len(A), M=round(-fm, 2), **r)
                    print(json.dumps(rec), flush=True)
                    with open("examples/e69/e69_p47_audit.jsonl", "a") as fh: fh.write(json.dumps(rec) + "\n")
