"""Check the P34-A brief constants with w = floor(n/2): elementary C gives M >= sqrt(n)/4 and trivial C gives >= sqrt(n)/6,
for all n <= 200000 (exact formula in floats with margin report)."""
import math
worst = {"elem": (9, 0), "triv": (9, 0)}
for n in range(1, 200001):
    w = n // 2; S = w * (2 * w + 1) / (6 * (w + 1)); W = 1 + 2 * S; L = n + w
    for kind, C, target in (("elem", 0.811 * (L + 1) + 71 / 300, 0.25), ("triv", L + 1.0, 1 / 6)):
        lb2 = max((W * n - C * S) / (2 * (C - W)), 0.5)          # w = 0 also gives M^2 >= 1/2
        r = math.sqrt(lb2 / n) / target
        if r < worst[kind][0]: worst[kind] = (r, n)
print({k: (round(v[0], 5), v[1]) for k, v in worst.items()}, "(ratio LB/target; must be >= 1)")
