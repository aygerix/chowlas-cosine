"""Small NumPy/CuPy pilot for Chowla's mixed-certificate Fourier operator.

For q=sum v_k cos(kx), apply C with H=<D_A,q^2>=v^T C v.
Discovery arithmetic is float64. Exact controls and an optional saved
rational witness are checked separately; no optimized-cost claim is made.
Run research computations on the authorized VM, not the local workstation.
"""
import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path
import platform
import socket
import statistics
import time

import numpy as np


class FourierCost:
    def __init__(self, A, B, xp=np):
        self.A, self.B = tuple(A), tuple(B)
        assert self.A and self.B
        assert list(A) == sorted(set(A)) and min(A) > 0
        assert list(B) == sorted(set(B)) and min(B) > 0
        self.xp = xp
        # D*q^2 has degree at most max(A)+2*max(B). Strict padding avoids
        # cyclic alias in the cubic average as well as in the operator.
        degree = max(2 * max(A), max(A) + 2 * max(B))
        self.length = 1 << degree.bit_length()
        assert self.length > degree
        self.indices = xp.asarray(B, dtype=xp.int64)
        spectrum = xp.zeros(self.length // 2 + 1, dtype=xp.complex128)
        spectrum[xp.asarray(A, dtype=xp.int64)] = 1
        self.D = xp.fft.irfft(spectrum, n=self.length, norm="forward")

    def apply(self, vectors):
        xp = self.xp
        vectors = xp.atleast_2d(vectors)
        assert vectors.shape[1] == len(self.B)
        spectrum = xp.zeros((len(vectors), self.length // 2 + 1), dtype=xp.complex128)
        spectrum[:, self.indices] = vectors / 2
        values = xp.fft.irfft(spectrum, n=self.length, axis=1, norm="forward")
        values *= self.D
        product = xp.fft.rfft(values, axis=1, norm="forward")
        return product[:, self.indices].real


def exact_action(A, B, vectors):
    """Independent integer Toeplitz-plus-Hankel action; returns 2*C*v."""
    support = set(A)
    matrix = [[int(abs(j-k) in support) + int(j+k in support) for k in B] for j in B]
    return [[sum(c*int(v) for c, v in zip(row, vector)) for row in matrix]
            for vector in vectors]


def synchronize(xp):
    if xp is not np:
        xp.cuda.get_current_stream().synchronize()


def to_cpu(xp, value):
    return value if xp is np else xp.asnumpy(value)


def timed(xp, function, repeats):
    function()  # Warm plans and allocations; compilation/setup excluded.
    synchronize(xp)
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = function()
        synchronize(xp)
        samples.append(time.perf_counter() - start)
    return result, statistics.median(samples)


def controls(xp):
    rng = np.random.default_rng(20261021)
    records = []
    cases = [([1], [1], [[1]], F(0)), ([2], [1], [[1]], F(1, 2)),
             ([101], [1], [[1]], F(0)),
             ([1, 3, 8], list(range(1, 18)), rng.integers(-4, 5, (4, 17)).tolist(), None),
             ([1, 17, 1009], [1, 16, 17, 18, 992, 1009],
              rng.integers(-4, 5, (4, 6)).tolist(), None)]
    for A, B, integers, hand_H in cases:
        operator = FourierCost(A, B, xp)
        vectors = xp.asarray(integers, dtype=xp.float64)
        actual = to_cpu(xp, operator.apply(vectors))
        twice = np.array(exact_action(A, B, integers), dtype=np.float64)
        error = float(np.max(np.abs(actual-twice/2)))
        assert error < 2e-10
        if hand_H is not None:
            assert abs(float(np.sum(to_cpu(xp, vectors)*actual))-float(hand_H)) < 2e-12
        records.append(dict(A=A, B=B, fft_length=operator.length,
                            max_operator_error=error, hand_H=str(hand_H)))
    return records


def check_saved_witness(xp, path):
    data = json.loads(Path(path).read_text())
    A = data['actual']; n = len(A); row = data['polynomials'][-1]
    nums = row['positive_numerators']; den = row['denominator']
    coefficients = {s: int(c) for k, c in enumerate(nums, 1) for s in (-k, k) if c}
    a = F(sum(coefficients.get(s, 0) for t in A for s in (-t, t)), den)
    Q = F(sum(c*c for c in coefficients.values()), den*den)
    H = F(2*sum(c*coefficients.get(k+t, 0) for t in A
                for k, c in coefficients.items()), den*den)
    assert a == n and Q <= 25*n
    assert H == F(row['H'])
    K = 2*F(row['global_M_lower'])
    assert Q*K*K+H*K-n*n < 0
    operator = FourierCost(A, list(range(1, len(nums)+1)), xp)
    v = xp.asarray([2*c/den for c in nums], dtype=xp.float64)[None, :]
    numeric_H = float(to_cpu(xp, xp.sum(v*operator.apply(v))))
    assert abs(numeric_H-float(H)) < 1e-8*max(1, abs(float(H)))
    return dict(a=str(a), Q=str(Q), H=str(H), global_M_lower=row['global_M_lower'],
                numeric_H=numeric_H, numeric_error=abs(numeric_H-float(H)),
                status='Exact integer moments PASS; FFT agrees numerically')


def benchmarks(xp, batches, repeats):
    rng = np.random.default_rng(20261021)
    cases = [('small', sorted(rng.choice(np.arange(1, 73), 50, replace=False).tolist()),
              list(range(1, 145))),
             ('large_band', sorted(rng.choice(np.arange(1, 4097), 256, replace=False).tolist()),
              list(range(1, 8193))),
             ('wide_sparse', [1, 19, 317, 1009, 30011, 65537, 100003, 131071],
              [1, 18, 19, 20, 298, 317, 1009, 29002, 30011, 65537, 100003, 131071])]
    out = []
    for label, A, B in cases:
        start = time.perf_counter()
        operator = FourierCost(A, B, xp)
        synchronize(xp)
        setup = time.perf_counter()-start
        ell = float(to_cpu(xp, xp.mean(xp.abs(operator.D))))/math.sqrt(len(A))
        for batch in batches:
            host_vectors = rng.normal(size=(batch, len(B)))
            start = time.perf_counter()
            vectors = xp.asarray(host_vectors, dtype=xp.float64)
            synchronize(xp)
            transfer = time.perf_counter()-start
            result, seconds = timed(xp, lambda: operator.apply(vectors), repeats)
            assert bool(to_cpu(xp, xp.all(xp.isfinite(result))))
            direct_seconds = None
            if len(B) <= 144:
                support = set(A)
                matrix = np.array([[int(abs(j-k) in support)+int(j+k in support)
                                    for k in B] for j in B], dtype=np.float64)/2
                direct, direct_seconds = timed(np, lambda: host_vectors@matrix.T, repeats)
                assert np.max(np.abs(to_cpu(xp, result)-direct)) < 1e-8
            out.append(dict(label=label, n=len(A), max_A=max(A), witness_frequencies=len(B),
                            fft_length=operator.length, batch=batch, setup_seconds=setup,
                            input_transfer_seconds=transfer, kernel_median_seconds=seconds,
                            actions_per_second=batch/seconds, cpu_dense_median_seconds=direct_seconds,
                            diagnostic_L1_over_sqrt_n=ell,
                            L1_status='Uncertified grid diagnostic', optimized_cost_claim=False))
            print(json.dumps(out[-1]), flush=True)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--backend', choices=['numpy', 'cupy'], default='numpy')
    parser.add_argument('--fixture', default='.research/experiments/resolvent_2026-10-20/results.json')
    parser.add_argument('--output', required=True)
    parser.add_argument('--batches', default='1,8,32')
    parser.add_argument('--repeats', type=int, default=3)
    args = parser.parse_args()
    if platform.system() == 'Darwin':
        raise SystemExit('Run computations on the authorized research VM.')
    xp = np
    gpu = None
    if args.backend == 'cupy':
        import cupy as xp
        properties = xp.cuda.runtime.getDeviceProperties(0)
        gpu = {k: (v.decode() if isinstance(v, bytes) else v)
               for k, v in properties.items() if k in ['name', 'totalGlobalMem', 'major', 'minor']}
    output = dict(backend=args.backend, host=socket.gethostname(), gpu=gpu,
                  dtype='float64', seed=20261021, exact_controls=controls(xp),
                  saved_witness=check_saved_witness(xp, args.fixture),
                  benchmarks=benchmarks(xp, [int(t) for t in args.batches.split(',')], args.repeats),
                  numpy_version=np.__version__, backend_version=xp.__version__,
                  qualification='Operator pilot only; no new universal or optimized-cost bound.')
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', backend=args.backend, output=str(path))), flush=True)


if __name__ == '__main__':
    main()
