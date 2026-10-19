"""E62b: phase relaxation on larger structured supports and random controls (E62 extension; phase-C1/2 test).
Supports: Singer differences q31/q61, Bu q199/q401, dense N50, E49 triangle; controls: random A subset [1, 2n], n = 50, 200.
4 random starts each; reports the best R_phase (32x grid; UNCERTIFIED).  Usage: python src/e62b_phase_relax_wide.py > examples/e62/e62b.jsonl"""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from e51_transfer import sets
from e62_phase_relax import optimise, final_R

if __name__ == "__main__":
    S = sets(); rng = np.random.default_rng(23)
    sup = {k: S[k] for k in ("dense_N50", "singer_diff_q31", "singer_diff_q61", "e49_p1_n299_6", "bu_199_40", "bu_401_80")}
    for n in (50, 200):
        sup[f"random_n{n}_X{2*n}"] = sorted(rng.choice(np.arange(1, 2 * n + 1), n, replace=False).tolist())
    for name, A in sup.items():
        A = np.asarray(sorted(A)); n = len(A); best = 9.0
        for s in range(4):
            th0 = rng.uniform(0, 2 * np.pi, n); sc = math.sqrt(n)
            th = optimise(A, th0, betas=[2 / sc, 8 / sc, 32 / sc, 128 / sc], iters=300 if n < 2000 else 120)
            best = min(best, final_R(A, th))
        print(json.dumps(dict(set=name, n=n, X=int(A.max()), R_01=round(final_R(A, np.zeros(n)), 4), R_phase_best=round(best, 4))), flush=True)
