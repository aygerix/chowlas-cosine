"""E22: complete-multipartite generalisation of Bu's square identity (one positive eigenvalue, Smith's theorem).

For S Sidon (Bu frequencies b_s = 3s + 1/2) and a partition of S into blocks B_1..B_m, let
    A = {3|s-t|} ∪ {|3(s+t)+1|}  over pairs s, t in DIFFERENT blocks.
Then f_A = c^T (J - blockdiag J) c = P^2 - Σ_i P_i^2,  c_s = cos(b_s x),  P_i = Σ_{s in B_i} c_s,  |A| = k^2 - Σ|B_i|^2.
Heuristic (NOTEBOOK 2026-10-18): M ≈ E[Σ P_i^2 | P = 0] ≈ k/2, so R ≈ (k/2)/sqrt(k^2 - Σ|B_i|^2) >= 1/2, with large blocks
adding fluctuation.  Minima are FFT-grid estimates (uncertified), grid >= 16 max(A).
Usage: python src/multipartite_bu.py
"""
import sys, json, math
import numpy as np
sys.path.insert(0, 'src')

d = json.load(open('examples/bu_reproduction_certified.json'))
rng = np.random.default_rng(7)
print("key k b mode N M/k R R_pred=(k/2)/sqrt(N)")
for key in ('199_40', '311_60', '401_80'):
    S = np.array(sorted(d[key]['S'])); k = len(S)
    for b in (1, 2, 4, 8, k // 4, k // 2):
        for mode in (('sorted', 'random') if b > 1 else ('sorted',)):
            idx = np.arange(k) if mode == 'sorted' else rng.permutation(k)
            blk = np.empty(k, int); blk[idx] = np.arange(k) // b
            fr = []
            for i in range(k):
                for j in range(i + 1, k):
                    if blk[i] != blk[j]:
                        fr += [3 * abs(S[i] - S[j]), abs(3 * (S[i] + S[j]) + 1)]
            fr = np.array(fr)
            assert len(set(fr.tolist())) == len(fr) and fr.min() > 0
            G = 1 << math.ceil(math.log2(16 * fr.max() + 16))
            c = np.zeros(G); np.add.at(c, fr, 1.0)
            M = -np.real(np.fft.fft(c)).min(); N = len(fr)
            print(key, k, b, mode, N, round(M / k, 4), round(M / math.sqrt(N), 4), round(0.5 * k / math.sqrt(N), 4), flush=True)
