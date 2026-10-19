"""E92 — is the third-profile defect s = e(1 − 2p) of the P61 optimizer positive definite?
p = φ(w²), e = w²/4 = p − p², w = G⋆G̃ from the E82 N = 320 optimizer (largest D). If ŝ >= 0, PD gadgets (cost v/2) can
supply the third moment, so third-order weak-limit arguments give nothing even when M = o(X^{1/3}) (NOTEBOOK cont. 17.8).
Also tests the triangle generator G = 1. NUMERICAL (quadrature + FFT). Output: examples/e92/e92.json
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
    # F(ξ) = 2∫_0^1 f(t) cos(ξ t) dt by the trapezoid rule
    wts = np.full_like(t, t[1] - t[0]); wts[0] /= 2; wts[-1] /= 2
    return np.array([2 * np.sum(wts * f * np.cos(x * t)) for x in xis])

def analyse(name, t, w):
    p = phi(w * w); e = w * w / 4; s = e * (1 - 2 * p)
    xis = np.linspace(0, 400, 40001)
    out = {}
    for lab, f in (("p", p), ("e", e), ("s", s), ("p_cubed_plus_3pe", p ** 3 + 3 * p * e)):
        F = ft_even(f, t, xis)
        i = int(np.argmin(F))
        out[lab] = {"min_ft": float(F[i]), "at_xi": float(xis[i]), "ft0": float(F[0]), "rel_min": float(F[i] / F[0])}
    return out

def main():
    os.makedirs("examples/e92", exist_ok=True)
    rows = [json.loads(l) for l in open("examples/e82/e82.jsonl")]
    r = max((x for x in rows if x["N"] == 320), key=lambda x: x["D"])
    res = {}
    t, w = w_from_g(np.array(r["g"], float), 20000)
    res["E82_opt"] = analyse("E82", t, w)
    t2 = np.linspace(0, 1, 20001); res["triangle"] = analyse("tri", t2, 1 - t2)
    json.dump(res, open("examples/e92/e92.json", "w"), indent=1)
    print(json.dumps(res, indent=1))

if __name__ == "__main__":
    main()
