r"""E125 (lead, cont. 31): near-floor geometry, Boolean sets vs fractional P61(b) packets (follow-up to E124's lesson).
For f = Σ c_a cos(2πax) with M = −min f: N(t) = |{x : f(x) <= −M(1 − t)}|, wells(t) = number of connected components of that
set on the circular grid, γ = log-slope of N(t) between t = 0.01 and 0.1 (isolated quadratic wells give γ = 1/2).
PRE-REGISTERED (CSTAR, before the run): a separating statistic exists at computable X iff N(t) (t ∈ [0.01, 0.1]) or γ differs
between the packets and the Singer–Bu sets by a factor >= 3 (resp. >= 0.2 in γ), consistently over X; otherwise record
that no local statistic tested separates them at computable X. NUMERICAL (grid L >= 64·max A; M = grid minimum).
"""
import sys, json, math
import numpy as np
sys.path.insert(0, "src")

def floor_stats(name, idx, val, boolean):
    a = np.asarray(idx, dtype=np.int64); c = np.asarray(val, dtype=float)
    L = 1 << int(math.ceil(math.log2(64 * a.max() + 64)))
    spec = np.zeros(L); np.add.at(spec, a, c)
    f = np.fft.fft(spec).real; M = -f.min()
    out = {"family": name, "boolean": boolean, "n_eff": float((c * c).sum()), "X": int(a.max()), "R": float(M / math.sqrt((c * c).sum()))}
    Ns = {}
    for t in (0.01, 0.02, 0.05, 0.1, 0.2, 0.5):
        m = f <= -M * (1 - t)
        Ns[t] = m.mean()
        wells = int(np.count_nonzero(m & ~np.roll(m, 1))) or int(m.any())
        out[f"N{t}"] = float(m.mean()); out[f"wells{t}"] = wells
        out[f"Nw{t}"] = float(m.mean() / wells) if wells else 0.0   # mean well width
    out["gamma"] = float(math.log(Ns[0.1] / Ns[0.01]) / math.log(10))
    out["wells0.1_per_X"] = out["wells0.1"] / out["X"]
    print(json.dumps(out), flush=True)

from bu import A_of_S
d = json.load(open("examples/singer_bu/certified.json"))
for q in ("61", "101", "199"):
    A = A_of_S(d[q]["S"]); floor_stats(f"singer_bu q={q}", A, np.ones(len(A)), True)
dd = json.load(open("examples/dense_certified.json"))
for k in ("X120_s0", "X260_s0"):
    A = dd[k]["A"]; floor_stats(f"dense {k}", A, np.ones(len(A)), True)
rng = np.random.default_rng(7)
A = np.nonzero(rng.random(4096) < 0.5)[0] + 1; floor_stats("random X=4096 d=0.5", A, np.ones(len(A)), True)
from e83_escape_binarise import escape, wstar
w = wstar()
for X in (1024, 4096, 16384):
    p_, r_, coef, J, Mesc = escape(X, 0.9, np.random.default_rng(X), w)
    k = np.arange(1, X + 1)
    floor_stats(f"packet fractional X={X}", k, coef, False)
    b = (np.random.default_rng(X + 1).random(X) < np.clip(coef, 0, 1)).astype(float)
    floor_stats(f"packet Bernoulli X={X}", k[b > 0], np.ones(int(b.sum())), True)
