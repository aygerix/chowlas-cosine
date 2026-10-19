"""E84 — lead's independent re-check of the round-10 certificate D <= 1333/10000 (PROOFS P62), by a method different from
the agent's (the agent: u = sqrt(1-x) substitution, squared form, exact Bernstein; here: Arb ball arithmetic directly in
x, mean-value enclosures, adaptive bisection, max over branches; Schur cubics re-derived by my own exact integration).

Claim to check, for every half-cell jj in [0, 128) (t in [jj/128, (jj+1)/128)), main cell j = jj // 2, child cell jj
(if jj < 64, else no child potential), every x in [0, cap_jj]:
    F(x) = a_j x + beta_child(L(x)) - beta_j(x)/2 - phi(x^2) >= 0,   phi(y) = (1 - sqrt(1 - y))/2,
with L(x) any valid lower branch for y = w(2t) lying in [0,1]: 0, 2x^2 - 1, x - sqrt(1 - x); beta_* increasing on [0,1],
beta(0) = 0. cap_jj = cos(pi/(k+2)), k = ceil(128/jj) - 1 (Egervary-Szasz), cap_0 = 1 — computed here in Arb.
Then the Schur test: (T_a U)(x) <= (1333/5000) U(x) on [0,1], U = 1 + (4/5)x(1-x), kernel a(|x-y|) piecewise constant.
Output: examples/e84/e84_verify.json. Usage: python src/e84_r10_verify.py
"""
import json
import os
import sys
from fractions import Fraction as F
from math import comb

from flint import arb, ctx

ctx.prec = 200
S = ".research/agents/tdense10_scratch/"
cert = json.load(open(S + "certificate_td.json"))
K = cert["K"]
A = [F(x) for x in cert["a"]]
BB = [[F(x) for x in row] for row in cert["beta_bernstein"]]


def bern_to_power(bs):
    m = len(bs) - 1
    p = [F(0)] * (m + 1)
    for k, v in enumerate(bs):
        for j in range(m - k + 1):
            p[k + j] += v * comb(m, k) * comb(m - k, j) * (-1) ** j
    return p


BP = [bern_to_power(r) for r in BB]


def arbF(q):
    return arb(q.numerator) / arb(q.denominator)


BPa = [[arbF(c) for c in p] for p in BP]
DBPa = [[arbF(k * p[k]) for k in range(1, len(p))] for p in BP]
# beta(x)/x as a polynomial (beta(0) = 0)
BXa = [[arbF(c) for c in p[1:]] for p in BP]
DBXa = [[arbF(k * p[k + 1]) for k in range(1, len(p) - 1)] for p in BP]


def horner(c, x):
    v = arb(0)
    for a in reversed(c):
        v = v * x + a
    return v


def ssqrt(z):
    """sqrt of a ball that may dip below 0 only through rounding (we never evaluate at genuinely negative arguments)."""
    if z.lower() < 0:
        u = float(z.upper())
        u = max(u, 0.0) * (1 + 1e-12) + 1e-300
        z = arb(u / 2, u / 2)
    return z.sqrt()


def ball(lo, hi):
    return arb((lo + hi) / 2, (hi - lo) / 2)


def F_branch(i, j, ch, x, a):
    """Value and derivative enclosures of F_i on ball x (branch i must lie in [0,1] on x)."""
    s = ssqrt(1 - x * x)
    phi = (1 - s) / 2
    dphi = x / (2 * s) if s > 0 else None
    val = a * x - horner(BPa[j], x) / 2 - phi
    der = None if dphi is None else a - horner(DBPa[j], x) / 2 - dphi
    if i == 0 or ch is None:
        return val, der
    if i == 1:
        L, dL = 2 * x * x - 1, 4 * x
    else:
        r = ssqrt(1 - x)
        L = x - r
        dL = 1 + 1 / (2 * r) if r > 0 else None
    val = val + horner(BPa[ch], L)
    if der is not None and dL is not None:
        der = der + horner(DBPa[ch], L) * dL
    else:
        der = None
    return val, der, L


def branch_ok(i, j, ch, lo, hi, a):
    x = ball(lo, hi)
    if i == 0 or ch is None:
        val, der = F_branch(0, j, ch, x, a)
        L = None
    else:
        out = F_branch(i, j, ch, x, a)
        val, der, L = out
        if not (L.lower() >= 0 and L.upper() <= 1):
            return False
    if val.lower() > 0:
        return True
    if der is not None:  # mean-value form around the midpoint
        m = arb((lo + hi) / 2)
        if i == 0 or ch is None:
            vm, _ = F_branch(0, j, ch, m, a)
        else:
            vm = F_branch(i, j, ch, m, a)[0]
        enc = vm + der * arb(0, (hi - lo) / 2)
        if enc.lower() > 0:
            return True
    return False


def small_ok(j, lo, hi, a):
    """On [lo, hi] subset [0, 0.6]: L = 0 is the only valid branch needed; check g(x) = F_0(x)/x > 0."""
    def g(x):
        s = ssqrt(1 - x * x)
        return a - horner(BXa[j], x) / 2 - x / (2 * (1 + s))
    def dg(x):
        s = ssqrt(1 - x * x)
        # d/dx [x/(2(1+s))] = 1/(2(1+s)) + x^2/(2 s (1+s)^2)
        return -horner(DBXa[j], x) / 2 - 1 / (2 * (1 + s)) - x * x / (2 * s * (1 + s) ** 2)
    x = ball(lo, hi)
    if g(x).lower() > 0:
        return True
    m = arb((lo + hi) / 2)
    return (g(m) + dg(x) * arb(0, (hi - lo) / 2)).lower() > 0


def check_cell(jj, stats):
    j = jj // 2
    ch = jj if jj < K else None
    a = arbF(A[j])
    if jj == 0:
        cap = arb(1)
    else:
        k = -(-2 * K // jj) - 1
        cap = (arb.pi() / (k + 2)).cos()
    caphi = float(cap.upper()) + 1e-15
    caphi = min(caphi, 1.0)
    todo = [(0.0, min(0.6, caphi))]
    if caphi > 0.6:
        todo.append((0.6, caphi))
    worst_depth = 0
    while todo:
        lo, hi = todo.pop()
        depth = 0
        ok = False
        if hi <= 0.6:
            ok = small_ok(j, lo, hi, a)
        else:
            for i in ((0, 1, 2) if ch is not None else (0,)):
                if branch_ok(i, j, ch, lo, hi, a):
                    ok = True
                    break
        if ok:
            stats["leaves"] += 1
            continue
        if hi - lo < 1e-13:
            stats["failed"].append((jj, lo, hi))
            continue
        mid = (lo + hi) / 2
        todo += [(lo, mid), (mid, hi)]
    return


def schur():
    lam = F(1333, 5000)
    sh = F(1, 5)
    U = [F(1), 4 * sh, -4 * sh]                 # U(y) = 1 + (4/5) y - (4/5) y^2
    V = [F(0), F(1), 2 * sh, -F(4, 3) * sh]     # antiderivative
    sys.path.insert(0, "src")
    from e81_r9_verify import pos_on, padd, pcompose, pscale
    res = []
    for i in range(K):
        lo, hi = F(i, K), F(i + 1, K)
        mid = (lo + hi) / 2
        T = [F(0)]
        for jdx, aj in enumerate(A):
            for (s0, s1, sign) in ((-F(jdx, K), -F(jdx + 1, K), +1), (F(jdx + 1, K), F(jdx, K), +1)):
                # piece: V(clip(x + s0)) - V(clip(x + s1))  (for the left piece s0 = -j/K, s1 = -(j+1)/K)
                part = [F(0)]
                for sh_, sg in ((s0, 1), (s1, -1)):
                    v = mid + sh_
                    if v <= 0:
                        term = [F(0)]
                    elif v >= 1:
                        term = [sum(V)]
                    else:
                        term = pcompose(V, [sh_, F(1)])
                    part = padd(part, pscale(term, F(sg)))
                T = padd(T, pscale(part, aj))
        P = padd(pscale(U, lam), pscale(T, F(-1)))
        st = {"leaves": 0, "depth": 0}
        ok = pos_on(P, lo, hi, stats=st)
        res.append({"cell": i, "ok": ok, **st})
    return res


def main():
    os.makedirs("examples/e84", exist_ok=True)
    mono = all(r[0] == 0 and all(r[i] <= r[i + 1] for i in range(len(r) - 1)) for r in BB)
    nonneg_a = all(x >= 0 for x in A)
    agree = all(bern_to_power(BB[i]) == [F(x) for x in cert["beta_power"][i]] + [F(0)] * (len(BB[i]) - len(cert["beta_power"][i]))
                for i in range(len(BB)))
    print("monotone betas, beta(0)=0:", mono, " a_j >= 0:", nonneg_a, " power form agrees:", agree, flush=True)
    stats = {"leaves": 0, "failed": []}
    for jj in range(2 * K):
        check_cell(jj, stats)
    print("pointwise: leaves", stats["leaves"], "failed", len(stats["failed"]), stats["failed"][:5], flush=True)
    sc = schur()
    print("schur all ok:", all(r["ok"] for r in sc), "max leaves", max(r["leaves"] for r in sc), flush=True)
    out = {"betas_monotone_beta0_zero": mono, "a_nonneg": nonneg_a, "power_form_agrees": agree,
           "pointwise_leaves": stats["leaves"], "pointwise_failed": stats["failed"],
           "schur_cells_ok": all(r["ok"] for r in sc), "schur": sc,
           "D1": "1333/10000", "C10": str(F(10000, 1333)), "C10_float": 10000 / 1333}
    json.dump(out, open("examples/e84/e84_verify.json", "w"), indent=1)


if __name__ == "__main__":
    main()
