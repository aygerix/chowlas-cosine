"""Probe: are the exhaustive optima threshold sets A = {n <= X : sum_i mu_i cos(n x_i) > theta} of a measure mu
on their own near-minimal dips?  LP: max margin m s.t. phi(n) >= theta + m (n in A), phi(n) <= theta - m (n notin A, n<=X),
mu >= 0, sum mu = 1.  Also: dips of f_A (all local minima within delta of the min), for anatomy."""
import sys, json, math
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, 'src')
d = json.load(open('examples/smallN_best.json'))

def dips(A, G=1 << 15, delta=1.5):
    A = np.array(A, float)
    x = np.pi * np.arange(G + 1) / G
    f = np.zeros(G + 1)
    for a in A: f += np.cos(a * x)
    loc = [j for j in range(1, G) if f[j] <= f[j-1] and f[j] <= f[j+1]]
    out = []
    for j in loc:
        xx = x[j]
        for _ in range(30):
            d1 = -(A * np.sin(A * xx)).sum(); d2 = -(A * A * np.cos(A * xx)).sum()
            if d2 <= 0: break
            xx -= d1 / d2
        out.append((np.cos(A * xx).sum(), xx))
    out.sort()
    m = out[0][0]
    return [(v, xx) for v, xx in out if v <= m + delta], m

for key in sys.argv[1:]:
    A = d[key]['A']; X = max(A); S = set(A)
    dl, m = dips(A)
    print(f"N={key} X={X} min={m:.5f} R={-m/math.sqrt(len(A)):.5f}; dips (value, x, x*X/pi):")
    print("   " + "  ".join(f"({v:.3f},{xx:.4f},{xx*X/math.pi:.2f})" for v, xx in dl[:14]))
    for delta in (0.3, 0.6, 1.0, 1.5):
        pts = [xx for v, xx in dl if v <= m + delta]
        r = len(pts); n = np.arange(1, X + 1)
        C = np.cos(np.outer(n, pts))            # X x r
        # variables: mu (r), theta, marg ; maximize marg
        c = np.zeros(r + 2); c[-1] = -1
        Aub = []; bub = []
        for i, nn in enumerate(n):
            row = np.zeros(r + 2)
            if nn in S: row[:r] = -C[i]; row[r] = 1; row[r+1] = 1      # -phi + theta + m <= 0
            else: row[:r] = C[i]; row[r] = -1; row[r+1] = 1            # phi - theta + m <= 0
            Aub.append(row); bub.append(0)
        Aeq = [np.r_[np.ones(r), 0, 0]]; beq = [1]
        bounds = [(0, None)] * r + [(None, None), (None, 1)]
        res = linprog(c, A_ub=np.array(Aub), b_ub=bub, A_eq=np.array(Aeq), b_eq=beq, bounds=bounds, method='highs')
        mu = res.x[:r]; th = res.x[r]; mg = res.x[r+1]
        phi = C @ mu
        wrong = [int(nn) for i, nn in enumerate(n) if (nn in S) != (phi[i] > th)]
        print(f"   delta={delta}: r={r} dips, max margin={mg:.4f}  misclassified at margin-0 threshold: {len(wrong)} {wrong[:12]}")
