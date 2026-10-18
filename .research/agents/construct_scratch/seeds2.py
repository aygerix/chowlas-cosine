"""Profile seeds: Tukey (flat top + raised-cosine taper) profile w(t) = 1 (t <= a), cos^2(pi (t-a) / (2 (1-a))) (a < t < 1),
t = n / Xp with Xp chosen so that sum_n w(n/Xp) = N; randomized rounding fixed up to exactly N elements of [1, X].
usage: seeds2.py N X a seed  (X = box for the search; requires Xp <= X)"""
import sys, math, random
N, X = int(sys.argv[1]), int(sys.argv[2]); a = float(sys.argv[3]); random.seed(int(sys.argv[4]))
def w(t):
    if t <= a: return 1.0
    if t >= 1: return 0.0
    return math.cos(math.pi * (t - a) / (2 * (1 - a))) ** 2
Xp = N / (a + (1 - a) / 2)
Xp = min(Xp, X)
A = set(n for n in range(1, X + 1) if random.random() < w(n / Xp))
while len(A) > N: A.discard(random.choice(sorted(A)))
while len(A) < N:
    n = random.randint(1, int(Xp))
    A.add(n)
print(" ".join(map(str, sorted(A))))
