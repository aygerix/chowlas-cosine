"""E23: dense regime with a FIXED positive-definite profile — how good can the 0/1 rounding be?

Dense heuristic (E16): R = c_E sqrt((1-ρ)/2) with ρ = ∫w²/∫w; beating 1/2 needs c_E < 1/sqrt(2(1-ρ)).  Here the profile w
on [0,1] is fixed (p.d. after even extension), A ⊂ [1, X] starts as a sigma-delta rounding of w(n/X), and LNS moves with
CONTIGUOUS windows only (counts per window preserved, so the profile is kept at the window scale) minimise M(A).
Reports R and c_E := (M - main(x*)) / sigma_E with sigma_E^2 = Σ (1_A - w)^2 / 2 and main(x*) = Σ w_n cos(n x*)
(the smooth part at the minimiser).  Minima: FFT + Newton (box_minlam.true_min), UNCERTIFIED.
Usage: python src/profile_rounding.py X profile steps seed [win]      profile in {tri, gauss, fejer2}
"""
import sys, math, json, time
import numpy as np
sys.path.insert(0, 'src')
from box_minlam import true_min
from lns_milp import window_solve


def profile(name, t):
    if name == 'tri':                       # autocorrelation of a box: ŵ = sinc² >= 0, ρ = 2/3
        return np.clip(1 - t, 0, 1)
    if name == 'gauss':                     # Gaussian, truncated at t = 1 (w(1) ≈ 0.017): ρ ≈ 0.707
        return np.exp(-t ** 2 / (2 * 0.35 ** 2))
    if name == 'fejer2':                    # autocorrelation of a triangle (cubic B-spline shape), ρ ≈ 0.72
        s = 2 * t
        return np.where(s <= 1, 1 - 1.5 * s ** 2 + 0.75 * s ** 3, np.where(s <= 2, 0.25 * (2 - s) ** 3, 0.0))
    raise ValueError(name)


def sigma_delta(w):
    A, acc = [], 0.0
    for n, wn in enumerate(w, start=1):
        acc += wn
        if acc >= 0.5:
            A.append(n); acc -= 1.0
    return A


def report(A, w, X):
    (fm, xm), v, G = true_min(A)
    n = np.arange(1, X + 1); ind = np.zeros(X); ind[np.array(A) - 1] = 1
    main = float((w * np.cos(n * xm)).sum()); sig = math.sqrt(((ind - w) ** 2).sum() / 2)
    rho = float((w ** 2).sum() / w.sum())
    return dict(M=-fm, R=-fm / math.sqrt(len(A)), x=xm, main=main, cE=(-fm + main) / sig, rho=rho,
                need_cE=1 / math.sqrt(2 * (1 - rho)), N=len(A))


if __name__ == "__main__":
    X = int(sys.argv[1]); name = sys.argv[2]; steps = int(sys.argv[3]); seed = int(sys.argv[4])
    win = int(sys.argv[5]) if len(sys.argv) > 5 else 24
    w = profile(name, np.arange(1, X + 1) / X)
    A = sigma_delta(w)
    print("start", json.dumps(report(A, w, X)), flush=True)
    rng = np.random.default_rng(seed)
    cuts = set((np.pi * np.arange(4 * X + 1) / (4 * X)).tolist())
    (fm, xm), v, G = true_min(A); cur = -fm; t0 = time.time()
    for st in range(steps):
        s = int(rng.integers(1, max(2, X - win + 2))); W = list(range(s, min(X, s + win - 1) + 1))
        r = window_solve(A, W, X, cuts, tl=10.0)
        if r is not None and r[0] < cur - 1e-9:
            cur, A = r
            print(f"step {st}: M={cur:.4f} R={cur / math.sqrt(len(A)):.4f} t={time.time() - t0:.0f}s", flush=True)
    out = report(A, w, X); out.update(X=X, profile=name, seed=seed, A=A)
    print(json.dumps(out), flush=True)
