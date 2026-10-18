# Lead's independent spot-check of P19 Theorem A (random relaxed sets saturate Bedert's (37)).
import numpy as np, math
rng = np.random.default_rng(7)
for N in (2000, 8000, 32000):
    for t in (1, 3):
        j = np.arange(1, N); W = 0.5 * np.clip(1 - j / N, 0, None); p = (np.sqrt(1 + 2 * W) - 1) / 2
        xi = rng.random(N - 1) < p
        off = N + 2 * t; a = np.zeros(2 * off + 1)          # index m -> m + off
        a[off + j[xi]] = 1; a[off - j[xi]] = 1
        m = np.arange(-off + 2 * t, off - 2 * t + 1)
        c = (2 * a[off + m] - 1j * a[off + m - t] + 1j * a[off + m + t]) ** 2
        G = 1 << math.ceil(math.log2(16 * len(m))); buf = np.zeros(G, complex); buf[(m % G)] = c
        phi = np.real(np.fft.ifft(buf) * G)                   # Σ c_m e(m x_k)
        Ks2 = -phi.min() / 16
        inA = lambda v: a[off + v] == 1
        B = sum(1 for mm in range(-N, N + 1) if inA(mm) and abs(mm - t) <= N and inA(mm - t) and not (abs(mm + t) <= N and inA(mm + t)))
        print(f"N={N} t={t} |A|={int(a.sum())} min f_t*f_t/sqrt(N log N)={phi.min()/math.sqrt(N*math.log(N)):.2f} "
              f"|B_t|/N={B/N:.4f} |B_t|/K*^4={B/Ks2**2:.3f}", flush=True)
