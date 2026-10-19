"""Lead's re-check of the round-17 CLIQUE-S certificate (VM only), by a method different from the agent's pure-Arb
script: the project's blocked Arb-DFT + Taylor certifier (src/chowla.py). Checks: A is a set of distinct positive
integers, [1, k] ⊂ A (so {0..k} is a clique of Cay(Z, ±A)), and a rigorous lower bound on min f_A, hence an upper bound
on M and a lower bound on clique/K. Output: examples/r17_certificates/lead_recheck.json."""
import json, math, sys, time
import numpy as np
sys.path.insert(0, 'src')
from chowla import certify_lower_bound_blocked
t0 = time.time()
A = sorted(int(a) for a in np.load('examples/r17_certificates/spline_L4096_s17_p5_6.npz')['A'])
assert len(A) == len(set(A)) and A[0] >= 1
k = 0
while k + 1 in set(A): k += 1
lb = certify_lower_bound_blocked(A, oversample=32, blocks=64).lower_bound
M_up = -lb
rec = dict(n=len(A), X=max(A), prefix_k=k, clique_global=k + 1, M_upper=M_up,
           clique_over_K_lower=(k + 1) / (2 * M_up), R_upper=M_up / math.sqrt(len(A)), secs=round(time.time() - t0, 1))
print(json.dumps(rec), flush=True)
json.dump(rec, open('examples/r17_certificates/lead_recheck.json', 'w'), indent=2)
