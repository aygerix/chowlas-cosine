"""E41 shape analysis: for each exact optimal half-set P ⊂ Z_p (pairs), find the multiplier c that makes ±cP most
interval-like (minimal mean |centered representative|), print the dilated pair set, its density profile, and the
Fourier spectrum 1̂_A(γ)/√p sorted (to see which γ attain the minimum and whether the spectrum is flat or spiky)."""
import sys, re, numpy as np
rows = []
for fn in sys.argv[1:]:
    for line in open(fn):
        m = re.search(r"p=(\d+) k=(\d+).*minM=([\d.]+).*P=([\d ]+)", line)
        if m: rows.append((int(m.group(1)), int(m.group(2)), float(m.group(3)), [int(x) for x in m.group(4).split()]))
for p, k, M, P in sorted(rows):
    h = (p - 1) // 2
    best = None
    for c in range(1, h + 1):
        Q = sorted(min(c * a % p, p - c * a % p) for a in P)
        s = sum(Q)
        if best is None or s < best[0]: best = (s, c, Q)
    _, c, Q = best
    g = np.arange(1, h + 1); vals = np.array([2 * np.cos(2 * np.pi * np.outer(g, P) / p).sum(1)])[0]
    srt = np.sort(vals)
    nmin = int(np.sum(vals < -M + 1e-6))
    mask = ''.join('#' if a in set(Q) else '.' for a in range(1, h + 1))
    print(f"p={p:3d} M/sqrtp={M/np.sqrt(p):.4f} c={c:3d} maxQ={max(Q):3d}/{h} | {mask}")
    print(f"      spectrum/sqrtp: min {srt[0]/np.sqrt(p):+.3f} (#at min {nmin}), 2nd {srt[1]/np.sqrt(p):+.3f}, "
          f"#neg {int(np.sum(vals<0))}/{h}, top3 {np.round(srt[-3:]/np.sqrt(p),2)}, max/p {srt[-1]/p:.3f}")
