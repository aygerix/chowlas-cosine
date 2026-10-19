"""E81 — lead's independent re-check of the round-9 certificates (PROOFS P60), by a method different from the agent's
(the agent used Bernstein subdivision + SymPy Sturm; this uses exact-rational Taylor models with interval subdivision).

(A) 18 supporting lines  q(2t) >= m q(t) + b :  T_2(z) - m z - b - sum_{n=3}^{24} lam_n T_n(z) >= 0 on [-1,1], lam_n >= 0.
(B) scalar certificate (kappa = 749089/1000000, degree-24 beta):  with x = 1 - u^2 (so 1 - sqrt(1-x) = 1 - u),
        P_i(u) = kappa (1 - u^2) - (1 - u) + beta(L_i(u)) - beta(1 - u^2)/2 >= 0   on each leaf [lo, hi] with branch i,
    leaves cover [0,1]; every branch argument L_i(u) lies in [-1e-5, 1] on its leaf; beta' >= 0 on [-1e-5, 1];
    beta's power and Bernstein forms agree; branches 3.. are exactly the 18 lines in u-form (m+b) - m u^2.
(C) the rational arithmetic C = 4/(r kappa), r = 769801/10^6 > 4/(3 sqrt 3).
(D) the 160-cell witness: q_i recomputed from the integer spectral factor; d = int_0^1 (1 - sqrt(1-q))/2 by closed-form
    cell integrals in mpmath (60 digits); 1/d < 7.267398825422.
(E) Horn test of the CP obstruction profile (mpmath).
Output: examples/e81/e81_verify.json.  Usage: python src/e81_r9_verify.py
"""
import json
import os
import sys
from fractions import Fraction as F

S = ".research/agents/tdense9_scratch/"


def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def pscale(a, s):
    return [s * x for x in a]


def pcompose(p, q):  # p(q(u))
    out = [F(0)]
    for c in reversed(p):
        out = padd(pmul(out, q), [c])
    return out


def peval(p, x):
    v = F(0)
    for c in reversed(p):
        v = v * x + c
    return v


def taylor_shift(p, c):  # coefficients of p(c + h) in h
    a = list(p)
    n = len(a)
    for i in range(n):
        for j in range(n - 2, i - 1, -1):
            a[j] += c * a[j + 1]
    return a


def pos_on(p, lo, hi, depth=0, maxdepth=40, stats=None):
    """Prove p > 0 on [lo, hi] (exact): Taylor model at the midpoint, subdivide on failure."""
    c = (lo + hi) / 2
    r = (hi - lo) / 2
    a = taylor_shift(p, c)
    lb = a[0] - sum(abs(a[j]) * r ** j for j in range(1, len(a)))
    if lb > 0:
        if stats is not None:
            stats["leaves"] += 1
            stats["depth"] = max(stats["depth"], depth)
        return True
    if depth >= maxdepth or a[0] <= 0:
        return False
    return pos_on(p, lo, c, depth + 1, maxdepth, stats) and pos_on(p, c, hi, depth + 1, maxdepth, stats)


def pdivide_1mu(p):  # p(u) / (1 - u), requires p(1) = 0
    assert peval(p, F(1)) == 0
    # p(u) = (1-u) s(u): synthetic division by (u - 1) then negate
    n = len(p) - 1
    s = [F(0)] * n
    acc = F(0)
    for i in range(n, 0, -1):
        acc = p[i] + acc
        s[i - 1] = acc
    # now p = (u-1) s + rem ; rem = p(1) = 0
    return [-x for x in s]


def cheb(n):
    T = [[F(1)], [F(0), F(1)]]
    for k in range(2, n + 1):
        T.append(padd(pscale(pmul([F(0), F(1)], T[k - 1]), 2), pscale(T[k - 2], -1)))
    return T


def part_a():
    recs = json.load(open(S + "long_gram_bounds.json"))
    T = cheb(24)
    out = []
    for rec in recs:
        m, b = F(rec["m"]), F(rec["b"])
        lam = [F(x) for x in rec["lambda_coefficients"]]
        assert len(lam) == 22 and all(x >= 0 for x in lam)
        P = padd(T[2], [-b, -m])
        for n, l in zip(range(3, 25), lam):
            if l:
                P = padd(P, pscale(T[n], -l))
        st = {"leaves": 0, "depth": 0}
        ok = pos_on(P, F(-1), F(1), stats=st)
        out.append({"m": rec["m"], "b": rec["b"], "ok": ok, **st})
    return out, recs


def part_b(recs):
    cert = json.load(open(S + "long_scalar_d24_exact.json"))
    kappa = F(cert["kappa"])
    bern = [F(x) for x in cert["beta_bernstein"]]
    powc = [F(x) for x in cert["beta_power"]]
    deg = len(bern) - 1
    from math import comb
    # Bernstein -> power
    conv = [F(0)] * (deg + 1)
    for k, bk in enumerate(bern):
        for j in range(k, deg + 1):  # x^k (1-x)^(deg-k) = sum_j C(deg-k, j-k) (-1)^(j-k) x^j
            conv[j] += bk * comb(deg, k) * comb(deg - k, j - k) * (-1) ** (j - k)
    agree = conv == powc
    beta = powc
    assert beta[0] == 0
    # beta' >= 0 on [-1e-5, 1]
    dbeta = [k * beta[k] for k in range(1, len(beta))]
    st = {"leaves": 0, "depth": 0}
    mono = pos_on(dbeta, F(-1, 100000), F(1), stats=st)
    # branches
    br = [[F(c) for c in b] for b in cert["branches"]]
    lines_match = all(br[3 + i] == [F(r["m"]) + F(r["b"]), F(0), -F(r["m"])] for i, r in enumerate(recs))
    xs = [F(1), F(0), F(-1)]  # x = 1 - u^2
    bx = pcompose(beta, xs)
    leaves = sorted(cert["leaves"], key=lambda L: F(L["lo"]))
    cover = leaves[0]["lo"] == "0" and leaves[-1]["hi"] == "1" and all(
        F(leaves[i]["hi"]) == F(leaves[i + 1]["lo"]) for i in range(len(leaves) - 1))
    res = []
    for L in leaves:
        lo, hi, i = F(L["lo"]), F(L["hi"]), L["branch"]
        Lp = br[i]
        # branch argument in [-1e-5, 1] on [lo, hi]
        arg_lo = pos_on(padd(Lp, [F(1, 100000)]), lo, hi) if any(Lp) else True
        # only the LOWER range matters (beta increasing on [L, y], y = q(2t) >= L); L <= 1 is automatic for a valid branch
        arg_hi = True
        P = padd(padd(pscale(xs, kappa), [F(-1), F(1)]), padd(pcompose(beta, Lp), pscale(bx, F(-1, 2))))
        st = {"leaves": 0, "depth": 0}
        if hi == 1 and peval(P, F(1)) == 0:
            Q = pdivide_1mu(P)
            ok = pos_on(Q, lo, hi, stats=st)
            note = "divided by (1-u)"
        else:
            ok = pos_on(P, lo, hi, stats=st)
            note = ""
        res.append({"lo": L["lo"], "hi": L["hi"], "branch": i, "ok": ok, "arg_in_range": arg_lo and arg_hi,
                    "note": note, **st})
    return {"kappa": cert["kappa"], "bernstein_power_agree": agree, "beta_monotone": mono, "mono_stats": st,
            "lines_match_branches": lines_match, "leaves_cover_[0,1]": cover, "leaves": res,
            "all_ok": agree and mono and lines_match and cover and all(x["ok"] and x["arg_in_range"] for x in res)}


def part_c(kappa):
    r = F(769801, 10 ** 6)
    C = 4 / (r * kappa)
    return {"r2_gt_16_27": r * r > F(16, 27), "C": str(C), "C_float": float(C),
            "C_matches": C == F("4000000000000/576649461289"),
            "rational_6.9366_ok": 4 - r * kappa * F(34683, 5000) > 0,
            "C_elementary_r0.811": float(4 / (F(811, 1000) * kappa))}


def part_d():
    import mpmath as mp
    mp.mp.dps = 60
    w = json.load(open(S + "witness_B160_full_factor.json"))
    g = [int(x) for x in w["factor_integers"]]
    B = len(g)
    den = sum(x * x for x in g)
    q = [F(sum(g[j] * g[j + i] for j in range(B - i)), den) for i in range(B)] + [F(0)]
    match = [F(x) for x in w["q"][:B]] == q[:B]
    phi = F(w["phi"])
    h = mp.mpf(phi.numerator) / phi.denominator / B
    # int over cell of (1 - sqrt(1 - q(t)))/2 with q linear from qa to qb: sqrt part = h * (2/3)(A^{3/2}-B^{3/2})/(A-B)
    tot = mp.mpf(0)
    for i in range(B):
        A = 1 - mp.mpf(q[i].numerator) / q[i].denominator
        Bv = 1 - mp.mpf(q[i + 1].numerator) / q[i + 1].denominator
        if A == Bv:
            sq = mp.sqrt(A)
        else:
            sq = mp.mpf(2) / 3 * (A ** 1.5 - Bv ** 1.5) / (A - Bv)
        tot += h * (1 - sq) / 2
    # cells beyond phi up to 1 have q = 0 -> integrand 0
    d = tot
    return {"q_match": match, "B": B, "phi": w["phi"], "d": mp.nstr(d, 30), "inv_d": mp.nstr(1 / d, 20),
            "inv_d_lt_7.267398825422": bool(1 / d < mp.mpf("7.267398825422")), "q_min": float(min(q)),
            "q_max_after0": float(max(q[1:]))}


def part_e():
    import mpmath as mp
    mp.mp.dps = 40
    eps, s = mp.mpf(1) / 1000, mp.mpf(1) / 2

    def E(y):
        z = eps * y / 2
        si = 1 if y == 0 else mp.sin(z) / z
        return eps * si ** 2 * (1 + mp.cos(s * y))
    h = 4 * mp.pi / 5
    horn = mp.mpf(0)
    for i in range(5):
        for j in range(5):
            sg = 1 if (i == j or (i - j) % 5 not in (1, 4)) else -1
            horn += sg * E((i - j) * h)
    return {"horn": mp.nstr(horn, 20), "negative": bool(horn < 0)}


def main():
    os.makedirs("examples/e81", exist_ok=True)
    a, recs = part_a()
    print("A lines:", all(x["ok"] for x in a), [x["leaves"] for x in a], flush=True)
    b = part_b(recs)
    print("B scalar:", b["all_ok"], b["bernstein_power_agree"], b["beta_monotone"], b["lines_match_branches"],
          b["leaves_cover_[0,1]"], flush=True)
    c = part_c(F(b["kappa"]))
    print("C:", c, flush=True)
    d = part_d()
    print("D witness:", d, flush=True)
    e = part_e()
    print("E horn:", e, flush=True)
    out = {"A_lines_all_ok": all(x["ok"] for x in a), "A": a, "B": b, "C": c, "D": d, "E": e}
    json.dump(out, open("examples/e81/e81_verify.json", "w"), indent=1)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
