"""E103: robustness of the square-root law to near-Boolean weights (Ruzsa's [0.99,1.01] question, cited by Bedert).

For a fixed support A and tau in [0,1), solve the LP
    minimize t   s.t.   sum_a w_a cos(a x) >= -t  for all x (cutting planes),   1 - tau <= w_a <= 1 + tau,
then report M_tau = t, the weighted ratio R_tau = M_tau / sqrt(sum w_a^2) and R_0 (tau = 0, i.e. the set itself).
Cutting planes: start from a coarse grid, then repeatedly add the FFT+Newton global minimiser of f_w until the LP
value and the true minimum agree to 1e-6 relative. NUMERICAL (FFT minimum, not interval-certified). Gurobi LP.
Question: does near-Booleanity (tau small) already allow M = o(sqrt n)? If R_tau/R_0 -> 0 for some family, any proof
of Chowla must use EXACT Booleanity; if R_tau >= (1 - O(tau)) R_0 uniformly, robust analytic proofs remain possible.
"""
import json, math, sys, time
import numpy as np
import gurobipy as gp
from gurobipy import GRB
sys.path.insert(0, 'src')
from bu import A_of_S


def fw_min(A, w, G):
    """Global min of sum w_a cos(a x): FFT grid of size G, then Newton polish of the 8 smallest grid points."""
    c = np.zeros(G); c[A] = w
    vals = np.real(np.fft.fft(c))
    idx = np.argpartition(vals, 8)[:8]
    best_x, best_v = None, np.inf
    Af = A.astype(float)
    for i in idx:
        x = 2 * math.pi * i / G
        for _ in range(30):
            s = np.sin(Af * x); co = np.cos(Af * x)
            d1 = -(w * Af * s).sum(); d2 = -(w * Af * Af * co).sum()
            if d2 <= 0: break
            step = d1 / d2; x -= step
            if abs(step) < 1e-15: break
        v = float((w * np.cos(Af * x)).sum())
        if v < best_v: best_v, best_x = v, x
    return best_v, best_x


def solve(A, tau, max_rounds=400, log=False):
    A = np.array(sorted(A)); n = len(A); X = int(A.max())
    G = 1 << math.ceil(math.log2(32 * X))
    m = gp.Model(); m.Params.OutputFlag = 0; m.Params.Method = 1
    w = m.addMVar(n, lb=1 - tau, ub=1 + tau); t = m.addVar(lb=-GRB.INFINITY)
    m.setObjective(t, GRB.MINIMIZE)
    xs = np.linspace(0, math.pi, 4 * n + 1)
    for x in xs:
        m.addConstr(np.cos(A * x) @ w + t >= 0)
    for r in range(max_rounds):
        m.optimize()
        wv = w.X; tv = t.X
        fmin, xmin = fw_min(A, wv, G)
        if -fmin <= tv * (1 + 1e-6) + 1e-9:
            break
        # cuts: the polished global minimiser plus the 24 lowest FFT-grid points below -t
        c = np.zeros(G); c[A] = wv
        vals = np.real(np.fft.fft(c))[: G // 2 + 1]
        idx = np.argpartition(vals, 24)[:24]
        pts = [xmin] + [2 * math.pi * i / G for i in idx if vals[i] < -tv]
        for x in pts:
            m.addConstr(np.cos(A * x) @ w + t >= 0)
    M = -fmin
    return dict(n=n, X=X, tau=tau, M=M, sumw2=float((wv ** 2).sum()), R=M / math.sqrt(float((wv ** 2).sum())),
                rounds=r + 1, wmin=float(wv.min()), wmax=float(wv.max()),
                frac_at_upper=float((wv > 1 + tau - 1e-9).mean()), frac_at_lower=float((wv < 1 - tau + 1e-9).mean()))


if __name__ == '__main__':
    import os; os.makedirs('examples/e103', exist_ok=True)
    rng = np.random.default_rng(20261019)
    from bu import bu_set_S
    fams = []
    from singer import singer
    for q in (13, 19, 23, 31, 43):
        D, v = singer(q); D = sorted(D)
        fams.append((f'singer_diff_q{q}', sorted({abs(a - b) for a in D for b in D if a != b})))
    for q in (61, 83):
        D, v = singer(q); c = (v - 1) // 2; L = c + 1; r = math.ceil(3 * math.sqrt(q))
        Ds = sorted(d % v for d in D); odd = sorted([d for d in Ds if (d - c) % 2], key=lambda d: abs(d - c))
        rest = [d for d in Ds if d not in set(odd[:r])]; Mw = sum(1 - abs(d - c) / L for d in rest)
        k = int(0.8 * Mw)
        S, _ = bu_set_S(q, k, seed=1, D=D, v=v); fams.append((f'bu_q{q}_k{k}', A_of_S(S)))
    for nn in (100, 200, 400, 800):
        fams.append((f'random_half_{nn}', (rng.choice(2 * nn, nn, replace=False) + 1).tolist()))
    fams.append(('interval200', list(range(1, 201))))
    taus = [0.0, 0.01, 0.1, 0.3]
    out = open('examples/e103/e103.jsonl', 'a')
    for name, A in fams:
        base = None
        for tau in taus:
            t0 = time.time()
            rec = solve(A, tau)
            if tau == 0.0: base = rec['R']
            rec.update(family=name, R_over_R0=rec['R'] / base, secs=round(time.time() - t0, 1))
            print(json.dumps(rec), flush=True); out.write(json.dumps(rec) + '\n'); out.flush()
