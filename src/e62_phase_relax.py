"""E62: phase relaxation of the best 0/1 supports.  For a support A, maximise min_x T(x), T = sum_{a in A} cos(a x - theta_a),
over the phases theta (theta = 0 is the 0/1 set).  Does freeing the phases push R = -min T/sqrt|A| below 1/2 on Bu's
supports and on the dense N=50 record?  (P34: window methods are phase-blind; this asks whether C1/2 is a positivity
phenomenon or a support phenomenon.)  Soft-min on an FFT grid (x_g = 2 pi g/G), annealed beta, L-BFGS, gradient by FFT:
d softmin/d theta_a = sum_g p_g sin(a x_g - theta_a).  Final value: 32x-oversampled grid minimum (UNCERTIFIED diagnostic).
Usage: python src/e62_phase_relax.py > examples/e62/e62.jsonl
"""
import json, math, sys
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, "src")
from e51_transfer import sets

def grid_T(A, th, G):
    c = np.zeros(G, complex); c[A] = np.exp(-1j * th)
    return (np.fft.ifft(c) * G).real                     # sum cos(a x_g - th_a)

def final_R(A, th):
    X = int(A.max()); G = 32 << math.ceil(math.log2(X)); return -grid_T(A, th, min(G, 1 << 26)).min() / math.sqrt(len(A))

def optimise(A, th0, betas, iters):
    X = int(A.max()); G = 8 << math.ceil(math.log2(X)); th = th0.copy()
    for beta0 in betas:
        def obj(t):
            T = grid_T(A, t, G); m0 = T.min(); z = np.exp(-beta0 * (T - m0)); Z = z.sum(); p = z / Z
            m = m0 - math.log(Z) / beta0
            Pf = np.fft.fft(p)                            # Pf[a] = sum_g p_g e^{-i a x_g}
            g = (np.conj(Pf[A]) * np.exp(-1j * t)).imag    # sum_g p_g sin(a x_g - t_a)
            return -m, -g
        th = minimize(obj, th, jac=True, method="L-BFGS-B", options={"maxiter": iters}).x
    return th

if __name__ == "__main__":
    S = sets(); rng = np.random.default_rng(7)
    for name in ("dense_N50", "bu_101_20", "bu_199_40", "singer_diff_q31", "e49_p1_n299_6"):
        A = np.asarray(sorted(S[name])); n = len(A)
        R0 = final_R(A, np.zeros(n))
        for start in ("zero", "rand1", "rand2"):
            th0 = np.zeros(n) if start == "zero" else rng.uniform(0, 2 * np.pi, n)
            sc = math.sqrt(n)
            th = optimise(A, th0, betas=[2 / sc, 8 / sc, 32 / sc, 128 / sc], iters=300 if n < 2000 else 150)
            print(json.dumps(dict(set=name, n=n, X=int(A.max()), R_01=round(R0, 4), start=start, R_phase=round(final_R(A, th), 4))), flush=True)
