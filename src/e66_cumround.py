"""E66: cumulative (Sturmian) rounding of profiles p:[0,1]->[0,1]; M/sqrt(n) vs X. Tests P41 (curved profiles,
van der Corput + spike truncation) against flat-irrational / flat-rational pieces where P41's hypothesis fails.
A = {j<=X : floor(sigma+Phi(j)) > floor(sigma+Phi(j-1))}, Phi(j) = sum_{i<=j} p(i/X).
NUMERICAL (grid + Newton minimum via box_minlam.true_min; not certified).
Usage: python src/e66_cumround.py [--out examples/e66/e66.jsonl]"""
import argparse, json, math, os, sys
import numpy as np
sys.path.insert(0, "src")
from box_minlam import true_min
g = (math.sqrt(5) - 1) / 2
PROFILES = {
    "a_lin_irr": lambda t: g * (1 - t),
    "b_quad_irr": lambda t: g * (1 - t) ** 2,
    "c_quad_half": lambda t: 0.5 * (1 - t) ** 2,
    "d_flat_irr": lambda t: np.where(t <= 0.5, g, g * (1 - (2 * t - 1)) ** 2),
    "e_flat_half": lambda t: np.where(t <= 0.5, 0.5, 0.5 * (1 - (2 * t - 1)) ** 2),
    "f_osc": lambda t: 0.35 + 0.25 * np.cos(5 * np.pi * t),
    "g_lin_from1": lambda t: 1 - t,
}
def cumround(p, X, sigma):
    t = np.arange(1, X + 1) / X
    Phi = np.cumsum(p(t))
    U = np.floor(sigma + Phi); U0 = np.concatenate([[math.floor(sigma)], U[:-1]])
    return (np.nonzero(U - U0 > 0)[0] + 1).tolist()
ap = argparse.ArgumentParser(); ap.add_argument("--out", default="examples/e66/e66.jsonl")
ap.add_argument("--logX", default="10,11,12,13,14,15,16"); a = ap.parse_args()
os.makedirs(os.path.dirname(a.out), exist_ok=True)
for name, p in PROFILES.items():
    for lx in map(int, a.logX.split(",")):
        X = 1 << lx
        for sigma in (0.0, 0.37, 0.71):
            A = cumround(p, X, sigma)
            (fm, xm), _, _ = true_min(A, over=16)
            rec = dict(profile=name, X=X, sigma=sigma, n=len(A), maxA=max(A), M=-fm, R=-fm / math.sqrt(len(A)), xmin=xm)
            print(json.dumps(rec), flush=True)
            with open(a.out, "a") as fh: fh.write(json.dumps(rec) + "\n")
