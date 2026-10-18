#!/usr/bin/env python
"""Decision driver for bb_lambda: for each L, is there D (span exactly L, |D| = k) with def <= UB?  (fixed UB)
Usage: driver2.py lam k Lmin Lmax UB [workers]     (tasks dispatched largest-L-first for load balance)"""
import sys, subprocess, os
from concurrent.futures import ThreadPoolExecutor
lam, k, Lmin, Lmax, UB = map(int, sys.argv[1:6])
W = int(sys.argv[6]) if len(sys.argv) > 6 else 4
BIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin", "bb_lambda")
def run(L):
    out = subprocess.run([BIN, str(lam), str(k), str(L), str(UB)], capture_output=True, text=True).stdout.strip()
    print(out, flush=True)
with ThreadPoolExecutor(W) as ex:
    list(ex.map(run, range(Lmax, Lmin - 1, -1)))
print(f"# decision lam={lam} k={k} L in [{Lmin},{Lmax}] UB={UB} done", flush=True)
