"""E85 — lead's independent re-check of the round-11 certificate D <= 259/2000 (PROOFS P63), by a method different from
the agent's (the agent: u = sqrt(1-x) substitution, SymPy/FLINT exact Bernstein leaves, its own branch list per cell).
Here: Arb ball arithmetic directly in x (as in E84), adaptive bisection, and a branch set that I DERIVE MYSELF instead of
reading the certificate's per-cell branch list:
  - y >= 0, y >= 2x^2 - 1 (Gram), y >= x - sqrt(1 - x) (P59.4), valid for every t;
  - the 18 round-9 long lines y >= m x + b (verified in E81), valid for every t;
  - support lines: from each stored LP record (k, nodes z_l, weights alpha_l >= 0) I recompute
        A_n = 2 sum_l alpha_l T_n(z_l),  c = sum_l alpha_l,  R = sum_{n=3}^k max(A_n, 0),
        y >= (-A_1 x - c - R)/A_2     (needs A_2 > 0),
    valid when w(nt) = 0 for n > k, i.e. on every half-cell whose own support length k_jj = ceil(1/t_lo) - 1 is <= k.
Here x = w(t), y = w(2t), w a normalized nonnegative PD function supported in [-1, 1] (P61's WLOG).
Claim checked, for every half-cell jj in [0, 2K) (t in [jj/(2K), (jj+1)/(2K))), main cell j = jj // 2, child cell jj
(if jj < K, else no child potential), and every x in [0, cap_jj] with cap_jj = cos(pi/(k_jj + 2)) (cap_0 = 1):
    F(x) = a_j x + beta_jj(L(x)) - beta_j(x)/2 - phi(x^2) >= 0,   phi(y) = (1 - sqrt(1 - y))/2,
for SOME valid lower branch L with L(x) in [0, 1] (beta_* increasing on [0, 1], beta(0) = 0).
Then the continuum Schur test (T_a U)(x) <= (2 D1) U(x) on [0, 1], U = 1 + 4 s x(1 - x), s = cert["shape"].
Output: examples/e85/e85_verify.json. Usage: src/dirun.sh -c 4 python src/e85_r11_verify.py
"""
import json
import os
import sys
from fractions import Fraction as F
from math import comb

from flint import arb, ctx

ctx.prec = 200
S = ".research/agents/tdense11_scratch/"
cert = json.load(open(S + "certificate_td.json"))
K = cert["K"]
A = [F(x) for x in cert["a"]]
BB = [[F(x) for x in row] for row in cert["beta_bernstein"]]
D1 = F(cert["D1"])
SHAPE = F(cert["shape"])


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
BXa = [[arbF(c) for c in p[1:]] for p in BP]
DBXa = [[arbF(k * p[k + 1]) for k in range(1, len(p) - 1)] for p in BP]


def horner(c, x):
    v = arb(0)
    for a in reversed(c):
        v = v * x + a
    return v


def hornerf(c, x):
    v = 0.0
    for a in reversed(c):
        v = v * x + float(a)
    return v


def ssqrt(z):
    """sqrt of a ball that may dip below 0 only through rounding (never evaluated at genuinely negative arguments)."""
    if z.lower() < 0:
        u = float(z.upper())
        u = max(u, 0.0) * (1 + 1e-12) + 1e-300
        z = arb(u / 2, u / 2)
    return z.sqrt()


def ball(lo, hi):
    return arb((lo + hi) / 2, (hi - lo) / 2)


# ---------------------------------------------------------------- valid branches (derived here, not read per cell)
def cheb(z, k):
    r = [F(1), z]
    for n in range(2, k + 1):
        r.append(2 * z * r[-1] - r[-2])
    return r


LONG = sorted({(F(r["m"]), F(r["b"])) for r in json.load(open("examples/r9_certificates/long_gram_bounds.json"))})
SUP = {}
sup_records = 0
sup_bad = []
for ks, rows in json.load(open(S + "support_lines.json")).items():
    for r in rows:
        k = int(r["k"])
        assert k == int(ks)
        nodes = [(F(z), F(al)) for z, al in r["nodes"]]
        if not all(-1 <= z <= 1 and al >= 0 for z, al in nodes):
            sup_bad.append((k, "node/weight out of range"))
            continue
        ch = [cheb(z, k) for z, _ in nodes]
        mom = [sum(2 * al * c[n] for (z, al), c in zip(nodes, ch)) for n in range(k + 1)]
        c0 = sum(al for _, al in nodes)
        R = sum((max(F(0), v) for v in mom[3:]), F(0))
        if mom[2] <= 0:
            sup_bad.append((k, "A_2 <= 0"))
            continue
        m, b = -mom[1] / mom[2], -(c0 + R) / mom[2]
        SUP.setdefault(k, set()).add((m, b))
        sup_records += 1
        # the agent's stored line must be implied by (<=) the line derived here on [0, 1]
        ms, bs = F(r["m"]), F(r["b"])
        if not (bs <= b and ms + bs <= m + b):
            sup_bad.append((k, "stored line not implied", str(ms), str(bs)))


def lines_for(jj):
    """Valid linear lower bounds for y on half-cell jj: long lines always; support lines with k >= k_jj."""
    out = list(LONG)
    if jj >= 1:
        kjj = -(-2 * K // jj) - 1
        for k, ls in SUP.items():
            if k >= kjj:
                out += list(ls)
    # drop lines dominated on [0, 1] by another line (both endpoints)
    out = sorted(set(out), key=lambda mb: (-(mb[0] + mb[1]), -mb[1]))
    keep = []
    for m, b in out:
        if not any(b2 >= b and m2 + b2 >= m + b for m2, b2 in keep):
            keep.append((m, b))
    return keep


# ---------------------------------------------------------------- pointwise inequality
def F_eval(j, ch, x, a, br):
    """Value and derivative enclosures of F on ball x with branch br = ('zero'|'gram'|'sqrt'|('line', m, b)).
    Returns (val, der, L) with der None when unavailable; L None for the zero branch / no child."""
    s = ssqrt(1 - x * x)
    phi = (1 - s) / 2
    dphi = x / (2 * s) if s > 0 else None
    val = a * x - horner(BPa[j], x) / 2 - phi
    der = None if dphi is None else a - horner(DBPa[j], x) / 2 - dphi
    if ch is None or br == "zero":
        return val, der, None
    if br == "gram":
        L, dL = 2 * x * x - 1, 4 * x
    elif br == "sqrt":
        r = ssqrt(1 - x)
        L = x - r
        dL = 1 + 1 / (2 * r) if r > 0 else None
    else:
        _, m, b = br
        L, dL = arbF(m) * x + arbF(b), arbF(m)
    val = val + horner(BPa[ch], L)
    if der is not None and dL is not None:
        der = der + horner(DBPa[ch], L) * dL
    else:
        der = None
    return val, der, L


def branch_ok(j, ch, lo, hi, a, br):
    x = ball(lo, hi)
    val, der, L = F_eval(j, ch, x, a, br)
    if L is not None and not (L.lower() >= 0 and L.upper() <= 1):
        return False
    if val.lower() > 0:
        return True
    if der is not None:
        mid = arb((lo + hi) / 2)
        vm, _, Lm = F_eval(j, ch, mid, a, br)
        if Lm is not None and not (Lm.lower() >= 0 and Lm.upper() <= 1):
            return False
        if (vm + der * arb(0, (hi - lo) / 2)).lower() > 0:
            return True
    return False


def small_ok(j, lo, hi, a):
    """On [lo, hi] subset [0, 0.6], zero branch: check g(x) = F(x)/x > 0 (F(0) = 0)."""
    def g(x):
        s = ssqrt(1 - x * x)
        return a - horner(BXa[j], x) / 2 - x / (2 * (1 + s))

    def dg(x):
        s = ssqrt(1 - x * x)
        return -horner(DBXa[j], x) / 2 - 1 / (2 * (1 + s)) - x * x / (2 * s * (1 + s) ** 2)
    x = ball(lo, hi)
    if g(x).lower() > 0:
        return True
    m = arb((lo + hi) / 2)
    return (g(m) + dg(x) * arb(0, (hi - lo) / 2)).lower() > 0


def float_L(br, x):
    if br == "zero":
        return 0.0
    if br == "gram":
        return 2 * x * x - 1
    if br == "sqrt":
        return x - (1 - x) ** 0.5
    return float(br[1]) * x + float(br[2])


def check_cell(jj, stats):
    j = jj // 2
    ch = jj if jj < K else None
    a = arbF(A[j])
    if jj == 0:
        cap = arb(1)
        kjj = None
    else:
        kjj = -(-2 * K // jj) - 1
        cap = (arb.pi() / (kjj + 2)).cos()
    caphi = min(float(cap.upper()) + 1e-15, 1.0)
    brs = ["zero", "gram", "sqrt"] + [("line", m, b) for m, b in lines_for(jj)]
    todo = [(0.0, min(0.6, caphi))]
    if caphi > 0.6:
        todo.append((0.6, caphi))
    used = {}
    while todo:
        lo, hi = todo.pop()
        ok = False
        if hi <= 0.6:
            ok = small_ok(j, lo, hi, a)
            if ok:
                used["zero/x"] = used.get("zero/x", 0) + 1
        if not ok and lo > 0:
            if ch is None:
                cands = ["zero"]
            else:
                mid = (lo + hi) / 2
                cands = sorted((br for br in brs if 0 <= float_L(br, mid) <= 1 or br == "zero"),
                               key=lambda br: -float_L(br, mid))[:6]
            for br in cands:
                if branch_ok(j, ch, lo, hi, a, br):
                    ok = True
                    key = br if isinstance(br, str) else "line"
                    used[key] = used.get(key, 0) + 1
                    break
        if ok:
            stats["leaves"] += 1
            continue
        if hi - lo < 1e-13:
            stats["failed"].append((jj, lo, hi))
            continue
        mid = (lo + hi) / 2
        todo += [(lo, mid), (mid, hi)]
    for k2, v in used.items():
        stats["branch_use"][k2] = stats["branch_use"].get(k2, 0) + v
    stats["cert_support_k_match"] &= (cert["pointwise"][jj]["support_k"] in (None, kjj) or jj == 0)


def schur():
    lam = 2 * D1
    sh = SHAPE
    U = [F(1), 4 * sh, -4 * sh]                 # U(y) = 1 + 4 s y - 4 s y^2
    V = [F(0), F(1), 2 * sh, -F(4, 3) * sh]     # antiderivative
    sys.path.insert(0, "src")
    from e81_r9_verify import pos_on, padd, pcompose, pscale
    res = []
    for i in range(K):
        lo, hi = F(i, K), F(i + 1, K)
        mid = (lo + hi) / 2
        T = [F(0)]
        for jdx, aj in enumerate(A):
            for (s0, s1) in ((-F(jdx, K), -F(jdx + 1, K)), (F(jdx + 1, K), F(jdx, K))):
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
    os.makedirs("examples/e85", exist_ok=True)
    mono = all(r[0] == 0 and all(r[i] <= r[i + 1] for i in range(len(r) - 1)) for r in BB)
    nonneg_a = all(x >= 0 for x in A)
    agree = all(bern_to_power(BB[i]) == [F(x) for x in cert["beta_power"][i]] + [F(0)] * (len(BB[i]) - len(cert["beta_power"][i]))
                for i in range(len(BB)))
    print("K", K, "D1", D1, "shape", SHAPE, "| monotone betas, beta(0)=0:", mono, " a_j >= 0:", nonneg_a,
          " power form agrees:", agree, flush=True)
    print("support records", sup_records, "distinct lines per k", {k: len(v) for k, v in sorted(SUP.items())},
          "bad", sup_bad[:5], "| long lines", len(LONG), flush=True)
    stats = {"leaves": 0, "failed": [], "branch_use": {}, "cert_support_k_match": True}
    for jj in range(2 * K):
        check_cell(jj, stats)
        if jj % 48 == 47:
            print("  half-cells done", jj + 1, "leaves", stats["leaves"], "failed", len(stats["failed"]), flush=True)
    print("pointwise: leaves", stats["leaves"], "failed", len(stats["failed"]), stats["failed"][:5],
          "branch use", stats["branch_use"], "support_k matches cert", stats["cert_support_k_match"], flush=True)
    sc = schur()
    print("schur all ok:", all(r["ok"] for r in sc), "max leaves", max(r["leaves"] for r in sc), flush=True)
    out = {"betas_monotone_beta0_zero": mono, "a_nonneg": nonneg_a, "power_form_agrees": agree,
           "support_records": sup_records, "support_bad": sup_bad, "long_lines": len(LONG),
           "pointwise_leaves": stats["leaves"], "pointwise_failed": stats["failed"], "branch_use": stats["branch_use"],
           "cert_support_k_match": stats["cert_support_k_match"],
           "schur_cells_ok": all(r["ok"] for r in sc), "schur": sc,
           "D1": str(D1), "C11": str(1 / D1), "C11_float": float(1 / D1)}
    json.dump(out, open("examples/e85/e85_verify.json", "w"), indent=1)


if __name__ == "__main__":
    main()
