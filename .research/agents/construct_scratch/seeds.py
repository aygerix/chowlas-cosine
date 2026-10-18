"""Structured seeds for dense searches: core [1, Y] (Y = round(cf*N)) minus h random holes, tail = random elements of
(Y, X] filling up to N.  usage: seeds.py N X cf h seed > file"""
import sys, random
N, X = int(sys.argv[1]), int(sys.argv[2]); cf = float(sys.argv[3]); h = int(sys.argv[4]); random.seed(int(sys.argv[5]))
Y = min(round(cf * N), X)
core = set(range(1, Y + 1))
for a in random.sample(range(max(2, Y // 4), Y + 1), h): core.discard(a)
rest = N - len(core)
tail = random.sample(range(Y + 1, X + 1), rest)
print(" ".join(map(str, sorted(core | set(tail)))))
