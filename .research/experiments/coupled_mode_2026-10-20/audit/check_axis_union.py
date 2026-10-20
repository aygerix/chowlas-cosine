#!/usr/bin/env python3
"""Finite exact combinatorial checks of the axis-union reduction.
Eigenvalues are only floating-point sanity checks; set/matrix identities are exact.
"""
from itertools import combinations, product
import json
import math
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def add(u,v): return tuple(a+b for a,b in zip(u,v))
def sub(u,v): return tuple(a-b for a,b in zip(u,v))
def axis(a,i,m): return tuple(a if j==i else 0 for j in range(m))
def mat(vertices,S):
    return np.array([[int(sub(u,v) in S) for v in vertices] for u in vertices], dtype=np.int64)
def scalar_mat(vertices,T):
    return np.array([[int(u-v in T) for v in vertices] for u in vertices], dtype=np.int64)
def K(A):
    return -float(np.linalg.eigvalsh(A)[0]) if len(A) else 0.0

cases = 0
max_spec_error = 0.
records = []
for mask in range(1,16):
    A = {d for d in range(1,5) if mask & (1 << (d-1))}
    T = A | {-a for a in A}
    Ts = sorted(T)
    I0 = T | {0}
    E0 = sorted({a+b for a in I0 for b in I0} - I0)
    C = scalar_mat(Ts,T)
    B0 = scalar_mat(E0,T)
    for m in [2,3]:
        S = {axis(a,i,m) for a in T for i in range(m)}
        zero = (0,)*m
        I = S | {zero}
        W = {add(u,v) for u in I for v in I}
        E = W-I
        blocks = [[axis(a,i,m) for a in E0] for i in range(m)]
        for i,j in combinations(range(m),2):
            blocks.append([add(axis(a,i,m),axis(b,j,m)) for a in Ts for b in Ts])
        ordered = [v for block in blocks for v in block]
        assert len(ordered)==len(set(ordered)) and set(ordered)==E
        B = mat(ordered,S)
        expected = np.zeros_like(B)
        start = 0
        for k,block in enumerate(blocks):
            want = B0 if k<m else np.kron(C,np.eye(len(T),dtype=np.int64))+np.kron(np.eye(len(T),dtype=np.int64),C)
            expected[start:start+len(block),start:start+len(block)] = want
            start += len(block)
        assert np.array_equal(B,expected)
        # Full W2 vertex injection and all adjacency relations, at safe Q=5X+1.
        X = max(A)
        Q = 5*X+1
        enc = lambda v: sum(c*Q**i for i,c in enumerate(v))
        encoded_S = {enc(v) for v in S}
        encoded_W = {enc(v) for v in W}
        assert len(encoded_W)==len(W)
        integer_I = encoded_S | {0}
        assert {a+b for a in integer_I for b in integer_I} == encoded_W
        for u in W:
            for v in W:
                assert ((sub(u,v) in S)==(enc(u)-enc(v) in encoded_S))
        if mask in [1,5,13,15]:
            measured, predicted = K(B), max(K(B0),2*K(C))
            err = abs(measured-predicted)
            max_spec_error=max(max_spec_error,err)
            records.append({'A':sorted(A),'m':m,'N':len(S),'exterior_size':len(E),'K_exterior':measured,'K_predicted':predicted,'K_W1':K(mat(sorted(I),S))})
        cases += 1

# Exhaustively check 27 E_color Z^c = Z_good for X=4, scaled by 8.
X=4
V=list(range(-X,0))+list(range(1,X+1))
noise_cases = 0
for eta_bits in product([0,1],repeat=X):
    eta = {i+1:b for i,b in enumerate(eta_bits)}
    Zg = np.zeros((2*X,2*X),dtype=np.int64)
    total = np.zeros_like(Zg)
    for i,u in enumerate(V):
        for j,v in enumerate(V):
            d=abs(u-v)
            if u!=v and d<=X and len({abs(u),abs(v),d})==3:
                Zg[i,j] = eta[abs(u)]*eta[abs(v)]*(8*eta[d]-(X-d))
    for colors in product([1,2,3],repeat=X):
        for i,u in enumerate(V):
            for j,v in enumerate(V):
                d=abs(u-v)
                if u!=v and d<=X and colors[abs(u)-1]==1 and colors[abs(v)-1]==2 and colors[d-1]==3:
                    total[i,j] += eta[abs(u)]*eta[abs(v)]*(8*eta[d]-(X-d))
    assert np.array_equal(27*total,3**X*Zg)
    noise_cases += 1

out={'axis_union_exact_cases_passed':cases,'base_sets':'Every nonempty A subset of {1,2,3,4}; T=±A; m=2,3', 'integer_encoding':'Q=5*max(A)+1; all full-W2 vertex pairs checked', 'exact_decoupling_eta_patterns':noise_cases,'exact_decoupling_colorings_per_pattern':3**X,'maximum_exterior_spectral_error':max_spec_error,'spectral_sanity_checks':records}
(ROOT/'check_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
