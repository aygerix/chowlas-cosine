r"""E124 (lead, cont. 31; advisor's commissioned experiment): local centroid / anti-concentration test.
P82 (proved, any real C² 1-periodic f, any measurable B ⊂ {f <= −r'}):  M := −min f >= r' + ∫_B f'² / (2√2·|B|^{1/2}·‖f''‖₂).
It is weight-agnostic, so Booleanity can only enter through BAC (conjecture): for Boolean A ⊂ [1, X], X <= C|A|,
    share₀ := ∫_{f<=0} f'² / ∫ f'²  >= c(C) > 0,   which with P82 at r' = 0 gives M >= G₀ >= c'√|A| (T-dense for all C).
PRE-REGISTERED (CSTAR, before this run): (P1) P82 <= M for every set; (P2) Boolean dense families (Singer–Bu near-½ sets,
dense optima, JL/quadric lift images, random, Paley, interval) have share₀ >= 0.2 and G₀/√n >= 0.05; (P3) fractional
P61(b) packets have share₀ → 0 as X grows. BAC is refuted if (P2) fails for a Boolean family.
f = Σ_a c_a cos(2πax) (one-sided; n_eff = Σc_a²). Grid L >= 32·max(A) (power of 2); M_grid <= M (grid min), so (P1) is
checked against M_grid (stronger). Integrals are grid Riemann sums (NUMERICAL).
"""
import sys, json, math, itertools
import numpy as np
sys.path.insert(0, "src")

def metrics(name, coef_idx, coef_val, boolean, extra=None):
    a = np.asarray(coef_idx, dtype=np.int64); c = np.asarray(coef_val, dtype=float)
    X = int(a.max()); L = 1 << int(math.ceil(math.log2(32 * X + 64)))
    spec = np.zeros(L); np.add.at(spec, a, c)
    F = np.fft.fft(spec); f = F.real
    spec1 = np.zeros(L); np.add.at(spec1, a, a * c)
    fp = 2 * np.pi * np.fft.fft(spec1).imag            # f'(j/L) = −2π Σ a c_a sin = 2π·Im(fft(a c))
    f2n = 4 * np.pi ** 2 * math.sqrt((c ** 2 * a.astype(float) ** 4).sum() / 2)
    tot = (fp ** 2).mean()
    M = -f.min(); n_eff = float((c ** 2).sum())
    out = {"family": name, "boolean": boolean, "n_eff": n_eff, "X": X, "M_grid": float(M), "R": float(M / math.sqrt(n_eff))}
    best = 0.0; rows = []
    for frac in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]:
        rp = frac * M
        Bm = f <= -rp
        beta = Bm.mean()
        if beta == 0: continue
        num = (fp[Bm] ** 2).sum() / L
        g = num / (2 * math.sqrt(2) * math.sqrt(beta) * f2n)
        best = max(best, rp + g)
        if frac == 0.0:
            out.update({"share0": float(num / tot), "beta0": float(beta), "G0": float(g), "G0_over_sqrt_n": float(g / math.sqrt(n_eff))})
    out.update({"P82_opt": float(best), "P82_over_M": float(best / M), "P1_ok": bool(best <= M + 1e-9)})
    if extra: out.update(extra)
    print(json.dumps(out), flush=True)

rng = np.random.default_rng(20261020)
fam = sys.argv[1] if len(sys.argv) > 1 else "all"
if fam in ("all", "bu"):
    from bu import A_of_S
    d = json.load(open("examples/singer_bu/certified.json"))
    for q in ("61", "101", "199", "307"):
        A = A_of_S(d[q]["S"]); metrics(f"singer_bu q={q}", A, np.ones(len(A)), True, {"R_cert": d[q]["R_cert"]})
if fam in ("all", "dense"):
    d = json.load(open("examples/dense_certified.json"))
    for k in ("X30_s0", "X120_s0", "X260_s0"):
        A = d[k]["A"]; metrics(f"dense {k}", A, np.ones(len(A)), True)
if fam in ("all", "lift"):
    rows = [json.loads(l) for l in open("examples/e116/scan.jsonl") if '"reps"' in l]
    seen = set()
    for r in rows:
        key = (r["p"], r["a"])
        if key in seen: continue
        seen.add(key)
        Z = np.array(r["reps"]); L = int(np.abs(Z).max()); V = 4 * L + 3
        s = np.abs(Z[:, 0] + V * Z[:, 1]); A = sorted(set(int(t) for t in s))
        metrics(f"JL lift p={r['p']} a={r['a']} (SA one-rep)", A, np.ones(len(A)), True)
    for p in (5, 7):
        Q = lambda x: (x[0] * x[1] + x[2] * x[3]) % p
        cone = [x for x in itertools.product(range(p), repeat=4) if any(x) and Q(x) == 0]
        neg = lambda x: tuple((-np.array(x)) % p)
        half = [x for x in cone if x < neg(x)]
        Z = [tuple(((t + p // 2) % p) - p // 2 for t in x) for x in half]
        V = 2 * p + 1
        A = sorted(set(abs(sum(z[k] * V ** k for k in range(4))) for z in Z))
        metrics(f"quadric centred lift p={p}", A, np.ones(len(A)), True)
if fam in ("all", "control"):
    for X, dens in ((4096, 0.5), (16384, 0.1)):
        A = np.nonzero(rng.random(X) < dens)[0] + 1; metrics(f"random X={X} d={dens}", A, np.ones(len(A)), True)
    A = np.arange(1, 2001); metrics("interval [1,2000]", A, np.ones(len(A)), True)
    P = 4093; A = sorted({(x * x) % P for x in range(1, P)}); metrics("Paley QR mod 4093", A, np.ones(len(A)), True)
if fam in ("all", "packet"):
    from e83_escape_binarise import escape, wstar
    w = wstar()
    for X in (1024, 4096, 16384, 65536):
        p_, r_, coef, J, Mesc = escape(X, 0.9, np.random.default_rng(X), w)
        k = np.arange(1, X + 1)
        metrics(f"packet fractional X={X}", k, coef, False, {"J": J})
        b = (np.random.default_rng(X + 1).random(X) < np.clip(coef, 0, 1)).astype(float)
        metrics(f"packet Bernoulli-rounded X={X}", k[b > 0], np.ones(int(b.sum())), True)
