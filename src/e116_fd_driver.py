r"""E116-FD driver: best fundamental-domain lift of a JL set (one representative per class, from [−Rn, Rn]²).
ratio = |D|/K'² with K' re-evaluated by true_min. Usage: python src/e116_fd_driver.py p a j R iters seed [init: box|rand|taper]
"""
import sys, os, json, subprocess, math
import numpy as np
sys.path.insert(0, "src")
from e114_cp_group import jl_set
from e116_jl_taper import true_min

p, a, j, R, iters, seed = (int(t) for t in sys.argv[1:7])
init = sys.argv[7] if len(sys.argv) > 7 else "box"
D, n = jl_set(p, a, j)
reps = []
for g in sorted(D):
    ng = ((-g[0]) % n, (-g[1]) % n)
    if ng < g:
        continue  # one class per ±pair (g = −g impossible for odd n)
    c = [(g[0] + n * u, g[1] + n * v) for u in range(-R - 1, R + 1) for v in range(-R - 1, R + 1)]
    c = [z for z in c if abs(z[0]) <= R * n and abs(z[1]) <= R * n]
    reps.append(c)
rng = np.random.default_rng(seed)
cur = []
for c in reps:
    if init == "box":
        cur.append(int(np.argmin([max(abs(z[0]), abs(z[1])) for z in c])))
    elif init == "taper":  # P(z) = Λ(z₁/n)Λ(z₂/n): the expectation is the fractional PD lift (K = r by Poisson)
        wt = np.array([max(0.0, 1 - abs(z[0]) / n) * max(0.0, 1 - abs(z[1]) / n) for z in c])
        cur.append(int(rng.choice(len(c), p=wt / wt.sum())))
    else:
        cur.append(int(rng.integers(len(c))))
L = R * n
G = 4 * (2 * L + 1)
binp = "src/.build/e116_fd"
os.makedirs("src/.build", exist_ok=True)
if not os.path.exists(binp) or os.path.getmtime(binp) < os.path.getmtime("src/e116_fd.c"):
    subprocess.check_call(["cc", "-O3", "-march=native", "-o", binp, "src/e116_fd.c", "-lm"])
tag = f"p{p}a{a}j{j}R{R}_{init}_s{seed}"
inf = f"examples/e116/fd_in_{tag}.txt"; outf = f"examples/e116/fd_out_{tag}.txt"
with open(inf, "w") as fh:
    fh.write(f"{len(reps)} {G}\n")
    for c, i0 in zip(reps, cur):
        fh.write(f"{len(c)} " + " ".join(f"{z[0]} {z[1]}" for z in c) + f" {i0}\n")
log = subprocess.run([binp, inf, str(iters), "0.3", "0.003", str(seed), outf], capture_output=True, text=True).stdout
idx = [int(t) for t in open(outf).read().split("\n")[1].split()]
pairs = np.array([reps[c][i] for c, i in enumerate(idx)], dtype=np.int64)
fmin, xi, _, _ = true_min(pairs, np.ones(len(pairs)), L, G=1 << int(math.ceil(math.log2(32 * (2 * L + 1)))), nstart=24)
os.remove(inf)
print(json.dumps({"p": p, "a": a, "j": j, "R": R, "init": init, "seed": seed, "iters": iters, "sa": log.strip(),
                  "D": len(D), "K_true": -fmin, "ratio": len(D) / fmin ** 2, "R1D_upper": -fmin / math.sqrt(2 * len(D)),
                  "reps": pairs.tolist()}), flush=True)
