"""Cross-check e72's incremental B against a from-scratch numpy computation on the same (h, theta) grid."""
import json, math, sys
import numpy as np
HL = [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64]; TL = [0.1, 0.2, 0.3, 0.45, 0.6, 0.8, 1.0]
for l in sys.stdin:
    d = json.loads(l); A = np.array(d["A"]); X = d["X"]; n = len(A); best = 0
    for h in [h for h in HL if h <= X // 2]:
        N = 1 << int(math.ceil(math.log2(2 * (X + h) + 8))); a = np.zeros(N); a[A] = 1; a[(-A) % N] = 1
        if h: k = np.arange(-h, h + 1); ker = np.zeros(N); ker[k % N] = (1 - np.abs(k) / (h + 1)) / (h + 1); r = a - np.real(np.fft.ifft(np.fft.fft(a) * np.fft.fft(ker)))
        else: r = a
        rp = r[1:X + h + 1]; E = float(np.sum(rp ** 2))
        for th in TL:
            w = max(1, int(round(th * X))); kw = 1 - np.arange(1, w + 1) / (w + 1); S = float(np.sum(kw ** 2 * rp[:w] ** 2)); W = 1 + 2 * float(np.sum(kw ** 2)); L = X + h + w
            num = W * E - 0.687 * (L + 1) * S; den = 2 * (0.687 * (L + 1) - W); best = max(best, (math.sqrt(num / den) if num > 0 else 0) + abs(r[0]) / 2)
    print("C:", d["B_over_sqrtn"], " numpy:", round(best / math.sqrt(n), 6), " R:", d["grid_R"])
