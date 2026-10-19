import json, glob, math, sys, os
import numpy as np
sys.path.insert(0, 'src')
import e107_sector as E
def nuhat(delta, b, SMAX=400.0, DS=0.01):
    Cd = E.mats(delta, b); C = Cd.sum(0); S = C.shape[0]
    w, V = np.linalg.eig(C); i = int(np.argmax(abs(w))); lam = float(w[i].real); r = np.abs(V[:, i].real)
    s = np.arange(0.0, SMAX, DS); m = int(math.ceil(math.log(SMAX * 1e6) / math.log(b)))
    vec = np.tile(r.astype(complex), (s.size, 1))
    for i_ in range(m, 0, -1):
        vec = np.einsum('pst,pt->ps', E.Mof(Cd, s / b ** i_), vec) / lam
    return s, vec[:, 0] / r[0], lam
for f in sorted(glob.glob('examples/e107/sa_*.jsonl')):
    L = [json.loads(l) for l in open(f) if l.strip()]
    r = [x for x in L if x.get('final')]
    if not r: continue
    r = r[0]; b = r['b']; delta = r['delta']
    s, nu, lam = nuhat(delta, b)
    re = nu.real
    bands = [(0, 3), (3, 30), (30, 400)]
    out = []
    for lo, hi in bands:
        sel = (s >= lo) & (s < hi); j = np.argmin(re[sel]); out.append(f"[{lo},{hi}): min {re[sel][j]:+.4f} at s={s[sel][j]:.2f}")
    print(f.split('/')[-1], f"lam={lam:.3f} alpha={math.log(lam)/math.log(b):.3f}", " | ".join(out))
