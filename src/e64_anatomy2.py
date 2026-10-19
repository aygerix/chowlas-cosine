"""E64 anatomy 2: WHERE is the locked energy? Split Z's L² outside the incircle by y = 3x mod 2π into the central
spike |y| < c·2π/span(W) and the bulk. Also the L² of Z inside/outside the incircle relative to ∫P² (phase-blind cap).
Usage: python src/e64_anatomy2.py file.jsonl [...]"""
import json, math, os, sys
import numpy as np
for fn in sys.argv[1:]:
    if not os.path.exists(fn):
        continue
    for line in open(fn):
        d = json.loads(line)
        if d.get("event") != "final" or not d["E"]:
            continue
        D = sorted(set(a // 3 for a in d["A"] if a % 3 == 0)); E = d["E"]; Mt = d["Mt"]
        G = 1 << 17; x = 2 * np.pi * np.arange(G) / G
        P = np.cos(np.outer(3 * np.asarray(D), x)).sum(0) + Mt
        Z = np.zeros(G, complex)
        for e in E:
            Z += np.exp(1j * e * x) if e % 3 == 1 else np.exp(-1j * e * x)
        ms = [(e - 1) // 3 if e % 3 == 1 else -(e + 1) // 3 for e in E]       # W-frequencies
        span = max(ms) - min(ms) + 1
        y = (3 * x + np.pi) % (2 * np.pi) - np.pi
        out = np.abs(Z) > P; Z2 = np.abs(Z) ** 2; tot = Z2.sum()
        rec = dict(k=d.get("k"), nD=len(D), nE=len(E), span_W=span, PB_cap=round(float((P ** 2).mean()), 2),
                   EnergyZ=round(float(Z2.mean()), 2))
        for c in (1, 2, 4):
            cen = np.abs(y) < c * 2 * np.pi / span
            rec[f"out_central_c{c}"] = round(float(Z2[out & cen].sum() / tot), 3)
            rec[f"out_bulk_c{c}"] = round(float(Z2[out & ~cen].sum() / tot), 3)
        print(json.dumps(rec))
