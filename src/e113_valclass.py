"""E113: valuation-class sets in G = Z_{p^a}^2 (lead, cont. 30). D = {(x,y) != 0 : (val x, val y) in Omega}, val 0 = a.
Character sums depend only on (u, w) = (val alpha, val beta):  Ŝ(u, w) = Σ_{(i,j)∈Ω} φ(i,u)φ(j,w),
  φ(i,u) = Σ_{val x = i} e(αx/p^a):  (p−1)p^{a−i−1} if a−u <= i < a;  −p^u if i = a−u−1;  0 if i < a−u−1;  φ(a,u) = 1.
Exhaustive over Ω (a <= 3), SKIPPING Ω whose D ∪ {0} is a union of cyclic subgroups, and report the max ratio |D|/K² (K = −min over nontrivial characters), two-valuedness,
and whether D ∪ {0} is a subgroup union (checked separately). Exact integer arithmetic.
Usage: python src/e113_valclass.py p a
"""
import sys, itertools, json
def phi(i, u, p, a):
    if i == a: return 1
    if i >= a - u: return (p - 1) * p ** (a - i - 1)
    if i == a - u - 1: return -p ** u
    return 0
def size(i, p, a): return 1 if i == a else (p - 1) * p ** (a - i - 1)
def main():
    p, a = int(sys.argv[1]), int(sys.argv[2])
    cells = [(i, j) for i in range(a + 1) for j in range(a + 1) if (i, j) != (a, a)]
    chars = [(u, w) for u in range(a + 1) for w in range(a + 1) if (u, w) != (a, a)]
    # character (u,w): val alpha = u means alpha = p^u * unit; (a,a) is the trivial character
    T = [[phi(i, u, p, a) * phi(j, w, p, a) for (i, j) in cells] for (u, w) in chars]
    sz = [size(i, p, a) * size(j, p, a) for (i, j) in cells]
    best = []
    for mask in range(1, 1 << len(cells)):
        idx = [c for c in range(len(cells)) if mask >> c & 1]
        n = sum(sz[c] for c in idx)
        if 2 * n > (p ** a) ** 2: continue
        vals = [sum(T[q][c] for c in idx) for q in range(len(chars))]
        K = -min(vals)
        if K <= 0: continue
        Om = set(cells[c] for c in idx)
        closed = all((min(i + 1, a), min(j + 1, a)) in Om or (min(i + 1, a), min(j + 1, a)) == (a, a) for (i, j) in Om)
        if closed: continue          # D ∪ {0} is a union of cyclic subgroups: skip (spread-type)
        best.append((n / K ** 2, n, K, sorted(set(vals)), sorted(Om)))
    best.sort(key=lambda r: -r[0])
    for r in best[:12]:
        print(json.dumps(dict(ratio=round(r[0], 4), size=r[1], K=r[2], values=r[3], Omega=r[4])))
main()
