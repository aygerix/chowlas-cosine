#!/usr/bin/env python
"""Driver for bb_lambda: per-L exact optima (span exactly L) with a pool of workers.
Usage: driver.py lam k Lmin Lmax UBmode [workers]
UBmode: 'full' (UB = C(k,2): exact per-L optimum) or an integer slack s (UB = best_so_far + s, tasks in L order,
        best_so_far updated as results arrive; a line 'none<=UB' means opt(L) > UB).
"""
import sys, subprocess, os
from concurrent.futures import ThreadPoolExecutor
lam, k, Lmin, Lmax = map(int, sys.argv[1:5])
mode = sys.argv[5]
W = int(sys.argv[6]) if len(sys.argv) > 6 else int(os.environ.get("CHOWLA_WORKERS", 4))
P = k * (k - 1) // 2
BIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin", os.environ.get("BB_BIN", "bb_lambda"))
best = [P]
def run(L):
    UB = P if mode == "full" else min(P, best[0] + int(mode))
    out = subprocess.run([BIN, str(lam), str(k), str(L), str(UB)], capture_output=True, text=True).stdout.strip()
    if "mindef=" in out:
        d = int(out.split("mindef=")[1].split()[0])
        if d < best[0]: best[0] = d
    print(out, flush=True)
with ThreadPoolExecutor(W) as ex:
    list(ex.map(run, range(Lmin, Lmax + 1)))
print(f"# lam={lam} k={k} L in [{Lmin},{Lmax}] best_def={best[0]} best_phi={(P-best[0])/P:.4f}", flush=True)
