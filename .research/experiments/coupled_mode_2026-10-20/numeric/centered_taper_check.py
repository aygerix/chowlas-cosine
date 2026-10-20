"""FFT checks of the explicit two-space certificate, not asymptotic proofs."""
import json
from pathlib import Path
import numpy as np
from scipy.fft import next_fast_len, rfft, irfft

def run(t, seed=2102026):
    X = t**8
    alpha = t**-2
    rng = np.random.default_rng(seed + t)
    p = 2*alpha*(1-np.arange(1, X+1)/X)
    eta = rng.random(X) < p
    n = int(2*eta.sum())
    # Coefficients indexed -X,...,X.
    D = np.r_[eta[::-1], 0, eta].astype(float)
    Z = np.r_[(eta-p)[::-1], 0, eta-p]
    size = next_fast_len(4*X+1)
    z2 = irfft(rfft(Z, size)**2, size)[:4*X+1]
    numerator = float(D @ z2[X:3*X+1])
    V = float(Z @ Z)
    c0 = float(D @ Z)
    diagonal = numerator/V
    N = t*n
    b = np.sqrt(t)*c0/np.sqrt(V)
    certificate = (np.hypot(diagonal, 2*b)-diagonal)/2
    # Numerical support-membership diagnostic via rounded convolution;
    # this is not an interval-arithmetic or exact-integer certificate.
    d2 = irfft(rfft(D, size)**2, size)[:4*X+1]
    integer_error = float(np.max(np.abs(d2-np.rint(d2))))
    needed_counts = np.rint(d2[X:3*X+1])
    supported = bool(np.all((needed_counts>0) | (D>0) |
                            (np.arange(2*X+1)==X)))
    exterior = D == 0
    exterior[X] = False
    exterior_fraction = float(Z[exterior] @ Z[exterior]/V)
    return dict(t=t, X=X, alpha=alpha, n=n, N=N,
                interval_filled=supported, convolution_rounding_error=integer_error,
                V_over_n=V/n, c0_over_n=c0/n,
                diagonal=diagonal, coupling_over_sqrtN=b/np.sqrt(N),
                certificate_over_sqrtN=certificate/np.sqrt(N),
                exterior_fraction_of_noncentral_trial=exterior_fraction,
                note="Floating FFT diagnostics; not a certified eigenvalue enclosure.")

if __name__ == "__main__":
    results=[]
    for t in (2,3,4,5,6):
        result=run(t)
        results.append(result)
        print(json.dumps(result), flush=True)
    Path(__file__).with_suffix(".json").write_text(json.dumps(results, indent=2)+"\n")
