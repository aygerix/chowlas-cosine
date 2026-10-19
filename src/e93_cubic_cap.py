"""E93 — cubic front cap (NOTEBOOK cont. 17.9). Under M = o(X^{1/3}) the cubic profile s = g(p) = p(1−p)(1−2p) must be
PD, which forces a = p(0) <= u* = (3 − √3)/6, so σ = 4a(1 − a) <= 2/3 and d <= D_{2/3} (E88: 0.066166 ⇒ C < 15.11).
Question: at the D_{2/3} optimiser (E82 lam mode, λ = 2/3), is s itself PD? If not, the true cubic reach is larger.
Checks FT(p), FT(e), FT(s) on a dense frequency grid. NUMERICAL. Output: examples/e93/e93.json
"""
import json, os
import numpy as np

def phi(x):
    return (1 - np.sqrt(np.clip(1 - x, 0, None))) / 2

def w_from_g(g, M):
    N = len(g)
    c = np.correlate(g, g, "full")[N - 1:] / (g @ g)
    c = np.append(c, 0.0)
    t = np.linspace(0, 1, M + 1)
    return t, np.interp(t, np.arange(N + 1) / N, c)

def ft_even(f, t, xis):
    wts = np.full_like(t, t[1] - t[0]); wts[0] /= 2; wts[-1] /= 2
    C = np.cos(np.outer(xis, t))
    return 2 * C @ (wts * f)

def main():
    os.makedirs("examples/e93", exist_ok=True)
    out = {}
    xis = np.linspace(0, 300, 6001)
    for lam, fn in ((2 / 3, "examples/e82/e82_lam0.6666666667.jsonl"), (1.0, "examples/e82/e82.jsonl")):
        rows = [json.loads(l) for l in open(fn)]
        Nmax = max(r["N"] for r in rows)
        r = max((x for x in rows if x["N"] == Nmax), key=lambda x: x["D"])
        t, w = w_from_g(np.array(r["g"], float), 8000)
        p = phi(lam * w * w); e = p * (1 - p); s = e * (1 - 2 * p)
        res = {"N": Nmax, "D": r["D"], "a": float(p[0]), "int_p": float(np.trapezoid(p, t))}
        for lab, f in (("p", p), ("e", e), ("s", s)):
            F = ft_even(f, t, xis); i = int(np.argmin(F))
            res[lab] = {"min_ft": float(F[i]), "at": float(xis[i]), "ft0": float(F[0])}
        out[f"lam={lam:.4f}"] = res
    json.dump(out, open("examples/e93/e93.json", "w"), indent=1)
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
