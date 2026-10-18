"""Mechanism test M-D: "dense real squares" (residual = square of a DENSE real cosine polynomial).

Ansatz:  f_A = W + (P^2 - ||p||^2/2) + D,  P(x) = sum_{s=1}^L p_s cos(s x)  (real, dense support),
         W(x) = sum_{n>=1} w_n cos(n x), w_n = w0 * arch(n / (2L))  (doubly positive profile, W >= -w0/2),
so that  min f_A >= -(w0 + ||p||^2)/2 - max(-D).  The coefficient of cos(nx) in P^2 is
         c_n = sum_s p_s p_{s+n} + (1/2) sum_{s+t=n} p_s p_t      (n >= 1),
and the 0/1 requirement is  c_n + w_n in {0,1}  (defect d_n = 1_A(n) - w_n - c_n, A = {n : c_n + w_n > 1/2}).
If the defect were 0 and P Gaussian-like, R ~ sqrt(1-rho)/2 ~ 0.26 (P^2 is chi^2_1: c_E = 1/sqrt2).  The system is
overdetermined 2:1 (2L lags, L reals): this tests whether dense "Bu-type" real squares with a p.d. offset exist.
Loss: sum_n (u_n (1-u_n))^2 (double well, u = c + w), annealed to sum_n min(u,1-u)^2; L-BFGS, analytic gradient.
Output per run: defect rms, predicted M, exact R(A) of the rounded set (FFT + Newton, UNCERTIFIED).
"""
import sys, json, math
import numpy as np
from scipy.optimize import minimize

def arch(t):
    K = 2000; tt = np.linspace(0, 1, K + 1); h = np.sin(np.pi * tt) ** 0.8
    W = np.correlate(h, h, 'full')[K:]; W /= W[0]
    return np.interp(np.clip(t, 0, 1), np.linspace(0, 1, K + 1), W)

def coeffs(p):
    L = len(p)
    ac = np.correlate(p, p, 'full')[L:]                 # lags 1..L-1: sum_s p_s p_{s+n}
    cv = np.convolve(p, p)                              # index i <-> s+t = i+2 (s,t >= 1): sums 2..2L
    c = np.zeros(2 * L + 1)                             # c[n], n = 0..2L
    c[1:L] += ac
    c[2:2 * L + 1] += 0.5 * cv
    return c

MU, LAM = 1.0, 0.01
def loss(p, w, mode):
    L = len(p); c = coeffs(p); u = c[1:] + w[1:]
    if mode == 0:
        g = u * (1 - u); val = (g ** 2).sum(); du = 2 * g * (1 - 2 * u)
    else:
        e = np.where(u > 0.5, u - 1, u); val = (e ** 2).sum(); du = 2 * e
    sc = c[1:].sum(); val += MU * sc * sc / (2 * L); du = du + MU * sc / L     # unbiased rounding: sum c_n ~ 0
    dc = np.concatenate([[0.0], du])                    # dL/dc_n
    # dc_n/dp: autocorr part: d/dp_k sum_s p_s p_{s+n} = p_{k+n} + p_{k-n}; conv part: d/dp_k (1/2) sum_{s+t=n} p_s p_t = p_{n-k}
    grad = np.zeros(L)
    G1 = dc[1:L]                                        # lags 1..L-1
    for_auto = np.correlate(np.concatenate([p, np.zeros(L)]), np.concatenate([[0.0], G1]), 'valid')[:L]   # sum_n G_n p_{k+n}
    back = np.convolve(p, np.concatenate([[0.0], G1]))[:L]                                                  # sum_n G_n p_{k-n}
    grad += for_auto + back
    # conv part: index k (0-based, frequency k+1); sum over n of dc_n * p_{n-(k+1)} (frequency), i.e. correlate
    dcc = dc[2:2 * L + 1]                               # n = 2..2L  <->  i = n-2
    grad += np.correlate(dcc, p, 'full')[L - 1: 2 * L - 1]
    val += LAM * (p ** 2).sum(); grad += 2 * LAM * p
    return val, grad

def true_min(A, over=64):
    A = np.asarray(A); X = A.max(); G = 1 << int(math.ceil(math.log2(over * X)))
    c = np.zeros(2 * G); c[A] = 1; v = np.fft.rfft(c).real[:G + 1]
    best = v.min(); Af = A.astype(float)
    for j in np.argsort(v)[:10]:
        x = math.pi * j / G
        for _ in range(30):
            d1 = -(Af * np.sin(Af * x)).sum(); d2 = -(Af * Af * np.cos(Af * x)).sum()
            if d2 <= 0: break
            x -= d1 / d2
        best = min(best, np.cos(Af * x).sum())
    return best

if __name__ == "__main__":
    Ls = [int(s) for s in sys.argv[1].split(',')] if len(sys.argv) > 1 else [40, 80, 160]
    ntr = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    rng = np.random.default_rng(7)
    # gradient check
    pt = rng.standard_normal(13) * 0.3; wt = 0.7 * arch(np.arange(27) / 26); wt[0] = 0
    for md in (0, 1):
        v0, g0 = loss(pt, wt, md); num = np.array([(loss(pt + 1e-6 * e, wt, md)[0] - loss(pt - 1e-6 * e, wt, md)[0]) / 2e-6 for e in np.eye(13)])
        print("gradcheck mode", md, float(np.abs(num - g0).max()), flush=True)
    for L in Ls:
        for w0 in (0.0, 0.6, 0.9):
            n = np.arange(2 * L + 1); w = w0 * arch(n / (2 * L)); w[0] = 0
            rho = (w[1:] ** 2).sum() / (w0 * w[1:].sum()) if w0 > 0 else 0.0
            best = None
            for tr in range(ntr):
                Nt = w[1:].sum() if w0 > 0 else 0.4 * L
                scale = (0.25 * np.sqrt((1 - rho) * Nt)) ** 0.5 / np.sqrt(L / 2)   # ||p||^2/2 ~ target M
                p = rng.standard_normal(L) * scale
                for mode in (0, 1):
                    res = minimize(loss, p, args=(w, mode), jac=True, method='L-BFGS-B', options=dict(maxiter=20000))
                    p = res.x
                c = coeffs(p); u = c[1:] + w[1:]
                A = (np.flatnonzero(u > 0.5) + 1).tolist()
                if len(A) < 4: continue
                d = np.where(u > 0.5, 1 - u, -u); drms = float(np.sqrt((d ** 2).mean()))
                N = len(A); fm = true_min(A); R = -fm / math.sqrt(N)
                Mpred = (w0 + (p ** 2).sum()) / 2
                rec = dict(L=L, w0=w0, rho=round(rho, 4), trial=tr, N=N, maxA=max(A), defect_rms=round(drms, 4),
                           frac_defect_gt_0p1=round(float((np.abs(d) > 0.1).mean()), 3),
                           M_pred=round(Mpred, 3), R_pred=round(Mpred / math.sqrt(N), 4), R_true=round(R, 4))
                print(json.dumps(rec), flush=True)
                if best is None or R < best[0]: best = (R, A)
            print(json.dumps(dict(L=L, w0=w0, best_R_true=round(best[0], 4), best_A=best[1])), flush=True)
