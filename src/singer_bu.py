"""E25: Bu et al.'s square identity on FULL Singer sets (no thinning, no parity block), best cyclic shift.

S = (D + shift mod v) − ⌊v/2⌋ for a Singer difference set D ⊂ Z_v (v = q^2+q+1, |D| = q+1), so S ⊂ [−v/2, v/2] is Sidon
with L ≈ v/2 ≈ k^2/2 (the densest Sidon sets).  A(S) = {3|s−t|} ∪ {|3(s+t)+1|}, |A| = k(k−1),
f_{A(S)} = P^2 − k/2 − C/2 (P15).  Shift chosen by FFT-grid minimum over `nshift` equally spaced shifts; the chosen set is
then certified with chowla.certify_lower_bound_blocked (arb ball-arithmetic DFT, decimated in 64 residue blocks, + Taylor
remainder: RIGOROUS lower bound on min f; identical to certify_lower_bound, validated on q = 61, 101).
P16 (kernel-checked) forces R(A(S)) > 1/2 − η once η^6 k^3 >= 7000 L, so this family converges to 1/2 from above.
Usage: python src/singer_bu.py q1,q2,... [nshift]      (appends to examples/singer_bu/certified.json)
"""
import sys, math, json, os, time
import numpy as np
sys.path.insert(0, 'src')
from singer import singer
from bu import A_of_S
from chowla import certify_lower_bound_blocked, min_estimate_fft

path = 'examples/singer_bu/certified.json'
out = json.load(open(path)) if os.path.exists(path) else {}
qs = [int(t) for t in sys.argv[1].split(',')]; nshift = int(sys.argv[2]) if len(sys.argv) > 2 else 60
for q in qs:
    t0 = time.time()
    D, v = singer(q); D = sorted(D); best = None
    cand = []
    for shift in range(0, v, max(1, v // nshift)):
        S = sorted(((d + shift) % v) - v // 2 for d in D)
        A = np.array(A_of_S(S))
        G = 1 << math.ceil(math.log2(8 * A.max() + 16)); c = np.zeros(G); np.add.at(c, A, 1.0)
        cand.append((-np.real(np.fft.fft(c)).min(), shift))
    for _, shift in sorted(cand)[:8]:          # 8x grids misrank shifts by ~0.004 in R: re-rank with 16x + Newton
        S = sorted(((d + shift) % v) - v // 2 for d in D)
        M = -min_estimate_fft(A_of_S(S), oversample=16, polish=16).fmin
        if best is None or M < best[0]: best = (M, shift)
    S = sorted(((d + best[1]) % v) - v // 2 for d in D); A = A_of_S(S); N = len(A)
    lb = certify_lower_bound_blocked(A, oversample=16, blocks=64).lower_bound   # same certificate, ~1/64 memory
    out[str(q)] = dict(q=q, shift=best[1], S=S, N=N, max=max(A), cert_lower=lb, R_cert=-lb / math.sqrt(N))
    json.dump(out, open(path, 'w'))
    print(f"q={q} k={q+1} N={N} max={max(A)} R_est={best[0]/math.sqrt(N):.5f} R_cert<={-lb/math.sqrt(N):.5f} "
          f"t={time.time()-t0:.0f}s", flush=True)
