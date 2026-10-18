r"""E35 evaluation: actual R(A) for the best lambda-ruler candidates (A = differences of multiplicity exactly lambda).
Reads examples/lambda_ruler/e35_grid.txt; for each lambda and k keeps the best phi; computes R(A) by FFT + Newton
(UNCERTIFIED) and prints it with phi and the prediction 1/sqrt(2*lambda*phi)."""
import sys, os, math, re
sys.path.insert(0, 'src')
from chowla import min_estimate_fft
best = {}
for line in open('examples/lambda_ruler/e35_grid.txt'):
    m = re.match(r'lam=(\d+) k=(\d+) L=(\d+) phi=([\d.]+).* D=(.*)', line.strip())
    if not m: continue
    lam, k, L, phi = int(m[1]), int(m[2]), int(m[3]), float(m[4]); D = [int(v) for v in m[5].split(',')]
    if (lam, k) not in best or phi > best[lam, k][0]: best[lam, k] = (phi, L, D)
for (lam, k), (phi, L, D) in sorted(best.items()):
    r = {}
    for i in range(len(D)):
        for j in range(i):
            d = abs(D[i] - D[j]); r[d] = r.get(d, 0) + 1
    A = sorted(d for d, c in r.items() if c == lam)
    e = min_estimate_fft(A, oversample=32, polish=12)
    print(f"lam={lam} k={k} L={L} phi={phi:.3f} |A|={len(A)} R(A)={e.R:.4f}  1/sqrt(2*lam*phi)={1/math.sqrt(2*lam*phi):.3f}", flush=True)
