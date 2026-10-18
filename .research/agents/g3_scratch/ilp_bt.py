# Exact ILP: maximize |B_t| over symmetric A subset Gamma\{0} with F(chi) >= -K0 for all nontrivial chi.
# Gamma = Z_{n1} x ... x Z_{nr}; t given as a tuple.  Usage: python ilp_bt.py "3,3,3,3,3" "1,0,0,0,0" K0 timelimit
import sys, itertools, time, json
import numpy as np
import highspy

dims = tuple(int(v) for v in sys.argv[1].split(','))
t = tuple(int(v) for v in sys.argv[2].split(','))
K0 = float(sys.argv[3]); tl = float(sys.argv[4]) if len(sys.argv) > 4 else 600
extra = sys.argv[5] if len(sys.argv) > 5 else ""
els = list(itertools.product(*[range(n) for n in dims]))
idx = {e: i for i, e in enumerate(els)}
neg = lambda e: tuple((-x) % n for x, n in zip(e, dims))
addv = lambda e, f: tuple((x + y) % n for x, y, n in zip(e, f, dims))
subv = lambda e, f: tuple((x - y) % n for x, y, n in zip(e, f, dims))
zero = tuple(0 for _ in dims)
orbits = []; orb_of = {}
for e in els:
    if e == zero or e in orb_of: continue
    o = sorted({e, neg(e)}); k = len(orbits); orbits.append(o)
    for f in o: orb_of[f] = k
nx = len(orbits); G = len(els)
h = highspy.Highs(); h.setOptionValue("output_flag", False); h.setOptionValue("time_limit", tl)
h.setOptionValue("threads", 4)
inf = highspy.kHighsInf
# x vars 0..nx-1, z vars nx..nx+G-1
for k in range(nx): h.addVar(0, 1)
for m in range(G): h.addVar(0, 1)
h.changeColsIntegrality(nx, np.arange(nx, dtype=np.int32), np.array([highspy.HighsVarType.kInteger] * nx))
# objective: maximize sum z  -> minimize -sum z
h.changeColsCost(G, np.arange(nx, nx + G, dtype=np.int32), -np.ones(G))
X = lambda e: orb_of[e] if e != zero else None
# z_m <= x_m, z_m <= x_{m-t}, z_m <= 1 - x_{m+t}
for m in els:
    zm = nx + idx[m]
    for e, sgn in ((m, 1), (subv(m, t), 1), (addv(m, t), -1)):
        xe = X(e)
        if xe is None:          # e = 0: x_0 = 0
            if sgn == 1: h.addRow(-inf, 0, 1, np.array([zm], np.int32), np.array([1.0]))
            continue
        if sgn == 1:
            h.addRow(-inf, 0, 2, np.array([zm, xe], np.int32), np.array([1.0, -1.0]))
        else:
            h.addRow(-inf, 1, 2, np.array([zm, xe], np.int32), np.array([1.0, 1.0]))
# character constraints, one per {chi, chi-bar}
seen = set(); ncons = 0
E = np.array(els)
for chi in els:
    if chi == zero or chi in seen: continue
    seen.add(chi); seen.add(neg(chi))
    ph = sum((np.array([o[0][i] for o in orbits]) * chi[i]) / dims[i] for i in range(len(dims)))
    coef = np.array([len(o) * np.cos(2 * np.pi * pv) for o, pv in zip(orbits, ph)])
    # for orbits of size 2 the two terms are equal (cos even); len(o) handles size-1 orbits (elements of order 2)
    nz = np.nonzero(np.abs(coef) > 1e-12)[0]
    h.addRow(-K0, inf, len(nz), nz.astype(np.int32), coef[nz]); ncons += 1
t0 = time.time(); h.run(); dt = time.time() - t0
info = h.getInfo(); st = h.modelStatusToString(h.getModelStatus())
sol = np.array(h.getSolution().col_value)
xs = np.round(sol[:nx]).astype(int)
A = [e for k, o in enumerate(orbits) if xs[k] for e in o]
S = set(A)
B = sum(1 for m in els if m in S and subv(m, t) in S and addv(m, t) not in S)
# exact recheck of K by FFT
I = np.zeros(dims);
for e in A: I[e] = 1
F = np.fft.fftn(I).real; F[zero] = np.inf; K = -F.min()
print(json.dumps({"dims": dims, "t": t, "K0": K0, "status": st, "time": round(dt, 1), "obj": -info.objective_function_value,
                  "bound": -info.mip_dual_bound, "gap": info.mip_gap, "B_t": B, "K": round(K, 9), "|A|": len(A),
                  "ratio_B_K3": B / K ** 3 if K > 0 else None}))
if extra:
    with open(extra, "w") as fh: json.dump({"dims": dims, "t": t, "A": A}, fh)
