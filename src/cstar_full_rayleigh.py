"""Full real Fourier action and exact finite-to-global Rayleigh controls.

The existing mixed-cost kernel omits constant and sine directions. This
operator includes both parity sectors in orthonormal coordinates. NumPy or
CuPy proposes actions; rational Toeplitz PSD checks certify the small cases.
No universal negative-eigenvalue estimate or GPU speedup is claimed.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import socket

import numpy as np
from cstar_gpu_kernel import FourierCost, to_cpu


class FullRayleigh:
    def __init__(self, A, band, xp=np):
        assert band >= 1
        self.base = FourierCost(A, list(range(1, band+1)), xp)
        self.xp, self.band = xp, band

    def apply(self, vectors, parity):
        xp, op = self.xp, self.base
        v = xp.atleast_2d(vectors)
        assert parity in ('even', 'odd')
        assert v.shape[1] == self.band+(parity == 'even')
        spectrum = xp.zeros((len(v), op.length//2+1), dtype=xp.complex128)
        root2 = xp.sqrt(2.)
        if parity == 'even':
            spectrum[:, 0] = v[:, 0]
            spectrum[:, op.indices] = v[:, 1:]/root2
        else:
            spectrum[:, op.indices] = -1j*v/root2
        q = xp.fft.irfft(spectrum, n=op.length, axis=1, norm='forward')
        product = xp.fft.rfft(q*op.D, axis=1, norm='forward')
        if parity == 'even':
            return xp.concatenate((product[:, :1].real,
                                   root2*product[:, op.indices].real), axis=1)
        return -root2*product[:, op.indices].imag


def exact_moments(A, coefficients, parity):
    # Twice the Laurent coefficients; imaginary numerators in the odd case.
    if parity == 'even':
        z = {0: 2*int(coefficients[0])}
        z.update({j: int(c) for j, c in enumerate(coefficients[1:], 1)})
        z.update({-j: int(c) for j, c in enumerate(coefficients[1:], 1)})
        sign = 1
    else:
        z = {j: -int(c) for j, c in enumerate(coefficients, 1)}
        z.update({-j: int(c) for j, c in enumerate(coefficients, 1)})
        sign = -1
    Q = F(sum(t*t for t in z.values()), 4)
    S = set(A) | {-a for a in A}
    H = F(sign*sum(t*u for j, t in z.items() for k, u in z.items()
                   if -j-k in S), 4)
    return Q, H


def pd(A, band, shift):
    support = set(A)
    size = 2*band+1
    mat = [[F(int(abs(j-k) in support))+(shift if j == k else 0)
            for k in range(size)] for j in range(size)]
    # Exact symmetric Schur elimination: all positive pivots iff PD.
    for j in range(size):
        pivot = mat[j][j]
        if pivot <= 0:
            return False
        for k in range(j+1, size):
            for ell in range(k, size):
                mat[ell][k] -= mat[ell][j]*mat[k][j]/pivot
                mat[k][ell] = mat[ell][k]
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--backend', choices=('numpy', 'cupy'), default='numpy')
    args = parser.parse_args()
    if args.backend == 'numpy' and 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    xp = np
    if args.backend == 'cupy':
        import cupy as xp
    rng = np.random.default_rng(20261021)
    actions = []
    for A, B in (([1], 1), ([2], 1), ([1, 2], 8), ([1, 3, 8], 17), ([101], 2)):
        op = FullRayleigh(A, B, xp)
        for parity in ('even', 'odd'):
            size = B+(parity == 'even')
            integers = rng.integers(-4, 5, (4, size))
            vectors = integers.astype(float)
            vectors[:, (1 if parity == 'even' else 0):] /= np.sqrt(2.)
            actual = to_cpu(xp, op.apply(xp.asarray(vectors), parity))
            errors = []
            for c, v, out in zip(integers, vectors, actual):
                Q, H = exact_moments(A, c, parity)
                assert abs(float(v@v)-float(Q)) < 1e-10
                errors.append(abs(float(v@out)-float(H)))
            assert max(errors) < 1e-9
            # Independent Toeplitz +/- Hankel action, including center.
            support = set(A)
            indices = list(range(0 if parity == 'even' else 1, B+1))
            matrix = np.zeros((size, size))
            for j, a in enumerate(indices):
                for k, b in enumerate(indices):
                    if a == b == 0:
                        value = 0
                    elif a == 0 or b == 0:
                        value = np.sqrt(2.)*int(max(a, b) in support)
                    else:
                        value = int(abs(a-b) in support)+(1 if parity == 'even' else -1)*int(a+b in support)
                    matrix[j, k] = value
            action_error = float(np.max(np.abs(actual-vectors@matrix.T)))
            assert action_error < 1e-10
            actions.append(dict(A=A, band=B, parity=parity,
                max_exact_energy_error=max(errors), max_action_error=action_error))
    kernels = []
    for N in (1, 2, 4, 8):
        c = {j: F(N-abs(j), N) for j in range(1-N, N)}
        A0 = sum(t*t for t in c.values())
        assert A0 == F(2*N*N+1, 3*N)
        for a in range(2*N+3):
            kappa = sum(t*c.get(j-a, 0) for j, t in c.items())/A0
            assert 0 <= kappa <= 1
            assert 1-kappa <= F(3*a*a, 2*N*N+1)
        kernels.append(dict(N=N, exact_shift_bounds_verified=True))
    caps = []
    # Global K is analytic here, not inferred from a grid.
    for A, K in (([1], F(2)), ([1, 2], F(9, 4)), ([101], F(2))):
        for B in (1, 2, 4, 8):
            lo, hi = F(0), F(2*len(A)+1)
            assert pd(A, B, hi)
            for _ in range(28):
                mid = (lo+hi)/2
                if pd(A, B, mid):
                    hi = mid
                else:
                    lo = mid
            error = F(6*sum(a*a for a in A), 2*(B+1)**2+1)
            assert lo <= K <= hi+error
            caps.append(dict(A=A, band=B, K_global_exact=str(K),
                K_band_bracket=[str(lo), str(hi)], global_error_upper=str(error),
                certified_global_upper=str(hi+error), exact_PSD_bisection=True))
    result = dict(status='PASS', backend=args.backend, host=socket.gethostname(),
        seed=20261021, numpy_version=np.__version__, backend_version=xp.__version__,
        actions=actions, kernels=kernels, global_caps=caps,
        qualification='Finite action/certification controls for a general approximation theorem; no new universal Chowla bound or GPU performance claim.')
    path = Path(f'.research/experiments/sqrt_boolean_2026-10-21/rayleigh_{args.backend}.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', actions=len(actions), exact_global_caps=len(caps),
        output=str(path))), flush=True)


if __name__ == '__main__':
    main()
