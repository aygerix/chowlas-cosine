r"""E116 SA driver: build P_L (JL lift or full box), run src/e116_sa.c, re-evaluate the best T by true_min.
E = R_1D upper bound = K'/√(2|T|). Usage: python src/e116_sa_driver.py p a j L iters seed [full] [init: box|bern|empty|all]
"""
import sys, os, json, subprocess, math, tempfile
import numpy as np
sys.path.insert(0, "src")
from e114_cp_group import jl_set
from e116_jl_taper import lift, true_min

p, a, j, L, iters, seed = (int(t) for t in sys.argv[1:7])
full = len(sys.argv) > 7 and sys.argv[7] == "full"
init = sys.argv[8] if len(sys.argv) > 8 else "bern"
D, n = jl_set(p, a, j)
pairs = lift(D, n, L, full=full)
lam = (1 - np.abs(pairs[:, 0]) / L).clip(0) * (1 - np.abs(pairs[:, 1]) / L).clip(0)
rng = np.random.default_rng(seed)
if init == "box":
    x0 = ((np.abs(pairs[:, 0]) <= n // 2) & (np.abs(pairs[:, 1]) <= n // 2)).astype(int)
elif init == "all":
    x0 = np.ones(len(pairs), dtype=int)
else:
    x0 = (rng.random(len(pairs)) < lam).astype(int)
G = 4 * (2 * L + 1)
binp = "src/.build/e116_sa"
os.makedirs("src/.build", exist_ok=True)
if not os.path.exists(binp) or os.path.getmtime(binp) < os.path.getmtime("src/e116_sa.c"):
    subprocess.check_call(["cc", "-O3", "-march=native", "-o", binp, "src/e116_sa.c", "-lm"])
tag = f"p{p}a{a}j{j}L{L}{'F' if full else ''}_{init}_s{seed}"
inf = f"examples/e116/sa_in_{tag}.txt"; outf = f"examples/e116/sa_out_{tag}.txt"
with open(inf, "w") as fh:
    fh.write(f"{len(pairs)} {G}\n")
    for (u, v), b in zip(pairs, x0):
        fh.write(f"{u} {v} {b}\n")
T0 = 0.02; T1 = 0.0005
log = subprocess.run([binp, inf, str(iters), str(T0), str(T1), str(seed), outf], capture_output=True, text=True).stdout
line2 = open(outf).read().split("\n")[1]
w = np.array([int(c) for c in line2], dtype=float)
fmin, xi, _, _ = true_min(pairs, w, L, G=1 << int(math.ceil(math.log2(32 * (2 * L + 1)))), nstart=24)
T = int(2 * w.sum())
os.remove(inf)
print(json.dumps({"p": p, "a": a, "j": j, "L": L, "full": full, "init": init, "seed": seed, "iters": iters,
                  "sa": log.strip(), "T": T, "K_true": -fmin, "ratio": T / fmin ** 2, "R1D_upper": -fmin / math.sqrt(2 * T),
                  "argmin": list(map(float, xi))}), flush=True)
