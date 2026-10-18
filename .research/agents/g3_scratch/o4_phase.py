# Check of the explicit phase formula in Lemma S / Theorem O4 (GR(4,a), a odd):
#   every unit y = tau(ybar) * (1 + 2 tau(beta)),  S(y) = i^{-Q(beta)} S(1),  Q(z) = Tr(tau(z)),
#   S(1) = eps_a (1+i)^a with eps_a = +-1,  k(y) = Q(beta(y)) - (a+1)/2 + 2[eps_a = -1]  (mod 4).
# S(y) is computed directly as sum_{x in T} i^{Tr(xy)} (ring multiplication, no FFT).   Usage: python o4_phase.py a
import sys, itertools
import numpy as np
a = int(sys.argv[1]); n2 = 2 ** a
def pmm(u, v, h, mod=4):
    r = np.convolve(u, v) % mod
    for k in range(len(r) - 1, a - 1, -1):
        c = r[k]
        if c: r[k - a:k + 1] = (r[k - a:k + 1] - c * h) % mod
    out = np.zeros(a, int); out[:min(a, len(r))] = r[:a]; return out
def prim2(cf):
    f = np.array(list(cf) + [1]); cur = np.zeros(a, int); cur[0] = 1
    for k in range(1, n2):
        cur = pmm(cur, np.array([0, 1]), f, 2)
        if cur[0] == 1 and not cur[1:].any(): return k == n2 - 1
    return False
cf = next(c for c in itertools.product(range(2), repeat=a) if c[0] and prim2(c))
f = np.array(list(cf) + [1]); e = f.copy(); e[1::2] = 0; o = f.copy(); o[0::2] = 0
g = (np.convolve(e, e) - np.convolve(o, o)) * (-1) ** a % 4; h = g[0::2] % 4
X = np.array([0, 1]); pw = [np.eye(1, a, 0, dtype=int)[0]]
for k in range(1, n2 - 1): pw.append(pmm(pw[-1], X, h))
assert (pmm(pw[-1], X, h) == pw[0]).all()
key = lambda v: tuple(int(c) for c in v)
T = [np.zeros(a, int)] + pw
lift = {key(v % 2): v for v in T}                     # residue (mod 2 coords) -> Teichmueller element
logT = {key(v): j for j, v in enumerate(pw)}
def tr(z):                                            # Tr z = sum_k sigma^k z; sigma acts on coordinates via xi -> xi^2
    s = np.zeros(a, int); cur = z.copy()
    for _ in range(a):
        s = (s + cur) % 4
        # sigma(sum c_j xi^j) = sum c_j xi^{2j}  (c_j in Z_4 are fixed by sigma? no: sigma fixes Z_4, yes)
        nxt = np.zeros(a, int)
        for j, c in enumerate(cur):
            if c: nxt = (nxt + c * pw[(2 * j) % (n2 - 1)]) % 4
        cur = nxt
    assert not s[1:].any(); return int(s[0])
TRT = [tr(x) for x in T]                              # Q-values: Tr of Teichmueller elements
def S(y):
    return sum(1j ** tr(pmm(x, y, h)) for x in T)
one = pw[0]; S1 = S(one); eps = S1 / (1 + 1j) ** a
assert abs(abs(eps) - 1) < 1e-9 and abs(eps.imag) < 1e-9
eps = int(round(eps.real)); bad = 0; cnt = 0
for y in itertools.product(range(4), repeat=a):
    y = np.array(y)
    if not (y % 2).any(): continue
    t0 = lift[key(y % 2)]; j0 = logT[key(t0)]
    r = pmm(y, pw[(-j0) % (n2 - 1)], h)               # y * tau(ybar)^{-1} = 1 + 2 tau(beta)
    d = (r - one) % 4; assert not (d % 2).any()
    tb = lift[key((d // 2) % 2)]                      # tau(beta)
    Q = tr(tb) if (d // 2 % 2).any() else 0
    k_pred = (Q - (a + 1) // 2 + (2 if eps == -1 else 0)) % 4
    val = np.conj(S(y)) / 2 ** ((a - 1) / 2)
    k_true = [k for k in range(4) if abs(val - (1 + 1j) * 1j ** k) < 1e-8]
    cnt += 1; bad += (k_true != [k_pred])
print(f"a={a}: S(1) = {eps:+d}*(1+i)^{a};  units checked={cnt}, phase-formula mismatches={bad}")
