# Power-map RDS construction for ord t = 3 and optimal full-coset repair.
#   Gamma = Z_3 x F_{3^m} x F_{3^m},  t = (1,0,0);  beta(x) = x^e  (e = 2: Dembowski-Ostrom; e = (3^k+1)/2: Coulter-Matthews)
#   U(a,b) = 3^{-m/2} conj( sum_x w^{Tr(a x + b beta(x))} ),  b != 0.  Requires U in +-mu_3 (checked).
#   Fibres: U = w^s -> {s};  U = -w^tau -> Z_3\{tau};  over (a,0): full (a in F) or empty.
#   F (symmetric subset of F_{3^m}\{0}) is chosen by an exact ILP minimising K.
# Usage: python planar2.py m e
import sys, itertools, json
import numpy as np
import highspy

m, e = int(sys.argv[1]), int(sys.argv[2]); p = 3; Q = p ** m
def mulmod(x, y, mp):
    r = [0] * (2 * m)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y): r[i + j] = (r[i + j] + xi * yj) % p
    for k in range(2 * m - 1, m - 1, -1):
        c = r[k]
        if c:
            for j in range(m + 1): r[k - m + j] = (r[k - m + j] - c * mp[j]) % p
    return r[:m]
one = [1] + [0] * (m - 1); X = [0, 1] + [0] * (m - 2)
for cf in itertools.product(range(p), repeat=m):
    mp = list(cf) + [1]; cur, k = X, 1
    while cur != one and k < Q: cur, k = mulmod(cur, X, mp), k + 1
    if cf[0] and k == Q - 1: break
enc = lambda v: sum(c * p ** i for i, c in enumerate(v))
dig = np.array([[(z // p ** i) % p for i in range(m)] for z in range(Q)])
EXP = [enc(one)]; cur = one
for k in range(Q - 2): cur = mulmod(cur, X, mp); EXP.append(enc(cur))
EXP = np.array(EXP); LOG = np.full(Q, -1); LOG[EXP] = np.arange(Q - 1)
def mul(u, v): return 0 if u == 0 or v == 0 else int(EXP[(LOG[u] + LOG[v]) % (Q - 1)])
def pw(u, k): return 0 if u == 0 else int(EXP[(LOG[u] * k) % (Q - 1)])
def add(u, v): return enc(list((dig[u] + dig[v]) % p))
def tr(z):
    s, y = 0, z
    for _ in range(m): s, y = add(s, y), pw(y, 3)
    return dig[s][0]
TR = np.array([tr(z) for z in range(Q)])
MUL = np.array([[mul(u, v) for v in range(Q)] for u in range(Q)])
BE = np.array([pw(x, e) for x in range(Q)])
T_ax = TR[MUL]                      # Tr(a x)
w = np.exp(2j * np.pi / 3)
U = np.zeros((Q, Q), complex)
for b in range(1, Q):
    T_b = TR[MUL[b][BE]]            # Tr(b x^e) as function of x
    S = (w ** ((T_ax + T_b[None, :]) % 3)).sum(axis=1)
    U[:, b] = np.conj(S) / 3 ** (m / 2)
I = np.zeros((3, Q, Q), bool); typ = np.zeros((Q, Q), int)  # 1 = E, 2 = D
for a in range(Q):
    for b in range(1, Q):
        u = U[a, b]
        ks = [s for s in range(3) if abs(u - w ** s) < 1e-7]; kd = [s for s in range(3) if abs(u + w ** s) < 1e-7]
        if ks: I[ks[0], a, b] = True; typ[a, b] = 1
        elif kd:
            for s in range(3):
                if s != kd[0]: I[s, a, b] = True
            typ[a, b] = 2
        else: raise SystemExit(f"U not in +-mu3 at {(a, b)}: {u}  (x^{e} not bent-of-real-type here)")
nD = int((typ == 2).sum()); nE = int((typ == 1).sum())
dens = (typ == 2).sum(axis=0)[1:] / Q        # D-density in each b-coset
print(f"m={m} e={e}: |D|={nD} |E|={nE}; D-density per b-coset takes values {sorted(set(np.round(dens, 4).tolist()))}")
# spectrum of the U-part / c-part without full cosets
n = 1 + 2 * m
def realise(I3, full):
    J = np.zeros((3,) * n, bool)
    for s in range(3):
        for a in range(Q):
            for b in range(Q):
                if I3[s, a, b] or (b == 0 and full[a]): J[(s,) + tuple(dig[a]) + tuple(dig[b])] = True
    return J
J0 = realise(I, np.zeros(Q, bool))
F0 = np.fft.fftn(J0.astype(float)).real
# full coset over (a,0) adds 3*[j=0]*w^{alpha.a} : build per-a contribution only on j=0 characters with beta''=anything
# variables: symmetric pairs {a,-a}, a != 0
pairs = []; seen = set()
for a in range(1, Q):
    if a in seen: continue
    na = enc(list((-dig[a]) % 3)); seen |= {a, na}; pairs.append((a, na))
# characters (j, alpha, beta''): index arrays over digit coords; contribution of pair at char = 3*[j=0]*2cos(2pi alpha.a/3)
chars = np.array(list(itertools.product(range(3), repeat=n)))
jj = chars[:, 0]; al = chars[:, 1:1 + m]
coef = np.zeros((len(chars), len(pairs)))
for k, (a, na) in enumerate(pairs):
    ph = (al @ dig[a]) % 3
    coef[:, k] = np.where(jj == 0, 3 * 2 * np.cos(2 * np.pi * ph / 3), 0.0)
base = F0.reshape(-1)  # C-order matches itertools.product ordering
nontriv = np.any(chars != 0, axis=1)
h = highspy.Highs(); h.setOptionValue("output_flag", False); h.setOptionValue("time_limit", 600.0)
inf = highspy.kHighsInf
for k in range(len(pairs)): h.addVar(0, 1)
h.addVar(0, inf)                    # K
nv = len(pairs)
h.changeColsIntegrality(nv, np.arange(nv, dtype=np.int32), np.array([highspy.HighsVarType.kInteger] * nv))
h.changeColsCost(1, np.array([nv], np.int32), np.array([1.0]))
rows = np.nonzero(nontriv)[0]
# dedupe identical rows
key = {}
for r in rows:
    kk = (round(base[r], 6),) + tuple(np.round(coef[r], 6))
    key.setdefault(kk, r)
for kk, r in key.items():
    idx = np.nonzero(np.abs(coef[r]) > 1e-12)[0]
    h.addRow(-base[r], inf, len(idx) + 1, np.append(idx, nv).astype(np.int32), np.append(coef[r, idx], 1.0))
h.run()
sol = np.array(h.getSolution().col_value); xs = np.round(sol[:nv]).astype(int)
full = np.zeros(Q, bool)
for k, (a, na) in enumerate(pairs):
    if xs[k]: full[a] = full[na] = True
J = realise(I, full)
neg = J
for ax in range(n): neg = np.take(neg, [(-i) % 3 for i in range(3)], axis=ax)
assert (neg == J).all() and not J[(0,) * n]
F = np.fft.fftn(J.astype(float)).real; F[(0,) * n] = np.inf; K = -F.min()
B = int((J & np.roll(J, 1, 0) & ~np.roll(J, -1, 0)).sum())
print(f"  optimal repair: |F|={int(full.sum())} K={K:.6f} |B_t|={B} |B_t|/K^3={B / K ** 3:.4f}  (status {h.modelStatusToString(h.getModelStatus())})")
vals, cnt = np.unique(np.round(F[np.isfinite(F)], 4), return_counts=True)
print("  spectrum:", dict(zip(vals.tolist(), cnt.tolist())))
