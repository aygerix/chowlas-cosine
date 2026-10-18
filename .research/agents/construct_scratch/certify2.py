"""Second, independent certificate for min f_A (direct summation + second-order Taylor cells; no DFT, no arb).

Grid x_j = j*h on [0, pi], h = pi/K.  For x in the cell [x_j - h/2, x_j + h/2]:
    f(x) >= f(x_j) - |f'(x_j)| h/2 - (h/2)^2/2 * S2,     S2 = sum a^2 >= |f''|,
since f is even and 2pi-periodic, [0, pi] suffices (cells at the ends extend symmetrically).
f(x_j), f'(x_j) are computed by direct float64 summation of cos(a x_j), a sin(a x_j) with a = integer, x_j = j*pi/K
computed as (pi*j)/K in float64.  Error budget (explicit, padded): each term's argument error <= a*x_j*2^-52*2 + ulp,
cos/sin error <= 1 ulp (glibc), summation error <= N * 2^-52 * sum|terms|; we pad the cell bound by
    pad = N*(2.3e-16*(X*pi*2 + 4)) + 1e-12 + |f'|-part analogue,
which is far below the reported margins.  This is a RIGOROUS-UP-TO-LIBM-ACCURACY certificate (it trusts glibc's cos/sin
to be within 1 ulp), meant as an independent cross-check of the arb certificate, not a replacement.
usage: certify2.py file_with_A_lines [K]
"""
import sys, json, math, re
import numpy as np

def parse(line):
    try: return json.loads(line)['A']
    except Exception: pass
    m = re.search(r'A=\[([0-9,\s]+)\]', line)
    if m: return [int(t) for t in re.split(r'[,\s]+', m.group(1).strip()) if t]
    return None

def cert2(A, K=None):
    A = np.array(sorted(set(A)), dtype=np.int64); N = len(A); X = int(A.max())
    if K is None: K = 1 << int(math.ceil(math.log2(256 * X)))
    h = math.pi / K
    S2 = float((A.astype(float) ** 2).sum()); S1 = float(A.sum())
    best = math.inf; jbest = -1
    Af = A.astype(float)
    for j0 in range(0, K + 1, 4096):
        j = np.arange(j0, min(K + 1, j0 + 4096))
        x = (math.pi * j) / K
        ax = np.outer(x, Af)
        f = np.cos(ax).sum(1); fp = -(np.sin(ax) * Af).sum(1)
        err_f = N * (2.3e-16 * (X * math.pi * 2 + 4)) + 1e-12
        err_fp = S1 * (2.3e-16 * (X * math.pi * 2 + 4)) + 1e-12
        lower = f - err_f - (np.abs(fp) + err_fp) * h / 2 - (h / 2) ** 2 / 2 * S2
        i = int(np.argmin(lower))
        if lower[i] < best: best = float(lower[i]); jbest = int(j[i])
    return best, K, jbest

if __name__ == "__main__":
    K = int(sys.argv[2]) if len(sys.argv) > 2 else None
    for line in open(sys.argv[1]):
        A = parse(line)
        if not A: continue
        lb, KK, jb = cert2(A, K)
        print(json.dumps(dict(N=len(A), max=max(A), cert2_lower=lb, R_cert2=-lb / math.sqrt(len(A)), K=KK, x_cell=jb * math.pi / KK)), flush=True)
