#!/usr/bin/env python3
"""Summaries of tabu / signed outputs (text processing only).
Usage: summarize.py tabu FILE      best def per (lam, k), with W/k, phi, naive R bound
       summarize.py signed FILE    best Rn per (lam, k, mode) from signed_tabu output
"""
import sys, re, math
mode, fn = sys.argv[1], sys.argv[2]
best = {}
for line in open(fn):
    if mode == "tabu":
        m = re.search(r"lam=(\d+) k=(\d+) L=(\d+) def=(\d+) W/k=([\d.]+) phi=([\d.]+) D=(\S+)", line)
        if not m: continue
        lam, k, L, d = map(int, m.groups()[:4]); key = (lam, k)
        if key not in best or d < best[key][0]: best[key] = (d, L, m.group(7))
    else:
        m = re.search(r"lam=(\d+) k=(\d+) L=(\d+) mode=(\w+) Rn=([\d.]+) \|A\|=(\d+) W_s=(\d+) W_s/k=([\d.]+) neg=(\d+) D=(\S+)", line)
        if not m: continue
        lam, k, L = map(int, m.groups()[:3]); md = m.group(4); Rn = float(m.group(5)); key = (lam, k, md)
        if key not in best or Rn < best[key][0]: best[key] = (Rn, L, int(m.group(6)), int(m.group(7)), int(m.group(9)), m.group(10))
for key in sorted(best):
    if mode == "tabu":
        lam, k = key; d, L, D = best[key]; P = k * (k - 1) // 2; G = (P - d) // lam; W = 2 * d
        Rn = (k + W) / (2 * lam * math.sqrt(G)) if G else float('inf')
        print(f"lam={lam} k={k} L={L} def={d} W/k={W/k:.2f} phi={1-d/P:.3f} naiveR={Rn:.3f} D={D}")
    else:
        lam, k, md = key; Rn, L, G, W, neg, D = best[key]
        print(f"lam={lam} k={k} {md:8s} L={L} Rn={Rn:.3f} |A|={G} W_s={W} W_s/k={W/k:.2f} neg={neg} D={D}")
