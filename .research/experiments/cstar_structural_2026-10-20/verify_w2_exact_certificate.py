"""Independent exact check of saved W2 support and rational positivity bound.

Reconstructs from the saved support, not a position in another results file.
Uses reversed row order, independently checking all Bareiss divisions/pivots.
"""
from pathlib import Path
from fractions import Fraction
import json
import time
HERE = Path(__file__).resolve().parent
record = json.loads((HERE / 'w2_exact_certificate.json').read_text())
A = record['A']
assert len(A) == len(set(A)) == 50 and min(A) > 0 and max(A) == 68
S = set(A) | {-a for a in A}
W = sorted({0} | S | {s+t for s in S for t in S}, reverse=True)
assert len(W) == record['W_size'] == 267
assert set(W) == set(range(-136,137)) - {-135,-134,-131,131,134,135}
p, q = record['p'], record['q']
assert (p,q) == (353,50) and Fraction(p*p,q*q) < 50
matrix = [[p*int(x==y)+q*int(x-y in S) for y in W] for x in W]
previous = 1
start = time.time()
for k in range(len(W)):
    pivot = matrix[k][k]
    assert pivot > 0, (k,pivot)
    for i in range(k+1,len(W)):
        for j in range(i,len(W)):
            numerator = pivot*matrix[i][j] - matrix[i][k]*matrix[k][j]
            value, remainder = divmod(numerator, previous)
            assert remainder == 0, (k,i,j)
            matrix[i][j] = matrix[j][i] = value
    previous = pivot
assert previous == int(record['determinant'])
assert Fraction(len(S)*q*q,p*p) == Fraction(250000,124609) > 2
print('PASS: exact support, all 267 positive leading minors in reversed row order, exact divisions, and saved determinant match.')
print('50 H + 353 I is positive definite; K_W2 < 353/50 < sqrt(50).')
print('This refutes the sharp constant only, not an unspecified universal positive constant.')
print('Elapsed seconds:',time.time()-start)
