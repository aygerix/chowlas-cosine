"""E101: numerical check of the window-variance bound VB (NOTEBOOK cont. 21.3), derived by the lead from P28's pointwise
domination |V_m(x)| <= 2(M + W_0(x)) (m >= H):
    4M^2 >= [avg_{m in Mset} E_m - 2 E_0] + E_x Var_{m in Mset} |V_m(x)|,
V_m(x) = sum_a psi_H(a-m) e^{iax}, psi_H(j) = (1-|j|/H)+, E_m = sum_a psi_H(a-m)^2, E_0 = sum_a psi_H(a)^2,
W_0(x) = sum_a psi_H(a) cos(ax). Also checks the pointwise domination on the grid. NUMERICAL (FFT grid)."""
import json, math, sys
import numpy as np
sys.path.insert(0, 'src')
from chowla import min_estimate_fft
from bu import A_of_S

def check(name, A, H, nm=64):
    A = np.array(sorted(A)); X = int(A.max()); n = len(A)
    M = -min_estimate_fft(A.tolist(), oversample=16, polish=8).fmin
    G = 1 << math.ceil(math.log2(8 * (X + H)))
    psi = lambda j: np.clip(1 - np.abs(j) / H, 0, None)
    w0 = np.zeros(G); w0[A] = psi(A)
    W0 = np.real(np.fft.fft(w0))            # sum_a psi(a) e^{-iax}; real part = W_0 at grid x (cos is even)
    E0 = float((psi(A) ** 2).sum())
    ms = np.unique(np.linspace(H, X + H, nm).astype(int))
    mods = []; Ems = []; viol = 0.0
    for m in ms:
        v = np.zeros(G); v[A] = psi(A - m)
        Vm = np.abs(np.fft.fft(v)); mods.append(Vm); Ems.append(float((psi(A - m) ** 2).sum()))
        viol = max(viol, float((Vm - 2 * (M + W0)).max()))
    mods = np.array(mods)
    var = float(mods.var(axis=0).mean()); gap = float(np.mean(Ems) - 2 * E0)
    rec = dict(family=name, n=n, X=X, H=H, M=M, R=M / math.sqrt(n), lhs_4M2=4 * M * M, front_gap=gap, Evar=var,
               rhs=gap + var, holds=4 * M * M >= gap + var - 1e-6 * n, max_pointwise_violation=viol,
               var_over_4M2=var / (4 * M * M), avgEm=float(np.mean(Ems)), twoE0=2 * E0)
    print(json.dumps(rec), flush=True)
    with open('examples/e101/e101.jsonl', 'a') as fh: fh.write(json.dumps(rec) + '\n')

if __name__ == '__main__':
    import os; os.makedirs('examples/e101', exist_ok=True)
    rng = np.random.default_rng(20261023)
    sm = json.load(open('examples/smallN_best.json'))
    sb = json.load(open('examples/singer_bu/certified.json'))
    sets = [('smallN100', sm['100']['A']), ('singer_bu61', A_of_S(sb['61']['S'])), ('singer_bu101', A_of_S(sb['101']['S']))]
    X = 8000; sets.append(('random_half', (rng.choice(X, X // 2, replace=False) + 1).tolist()))
    a = np.arange(1, X + 1); sets.append(('tapered_tri', a[rng.random(X) < 0.5 * (1 - a / X)].tolist()))
    for name, A in sets:
        Xa = max(A)
        for frac in (8, 4):
            check(name, A, max(2, Xa // frac))
