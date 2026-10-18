"""Anatomy of candidate sets (float, UNCERTIFIED diagnostics).
For each set: N, X = max A, R (Newton), number of near-equal dips (local minima within 1% and 3% of M),
profile w = Gaussian smoothing of 1_A (bandwidth bw = 4, as in E21/E27), rho = sum w^2 / (max w * sum w),
residual E = f - sum_n w_n cos(nx): sigma_E (exact, Parseval), skew of E (bulk x > 8/X), c_E = -min_bulk E / sigma_E,
decomposition at x*: main(x*), E(x*).  Input: certify_sets.py JSON lines (with "A") or lines with A=[...].
"""
import sys, json, math, re
import numpy as np

def parse(line):
    try: return json.loads(line)['A']
    except Exception: pass
    m = re.search(r'A=\[([0-9,\s]+)\]', line)
    if m: return [int(t) for t in re.split(r'[,\s]+', m.group(1).strip()) if t]
    m = re.search(r'A=([0-9\s]+)$', line.strip())
    if m: return [int(t) for t in m.group(1).split()]
    return None

def analyse(A, bw=4.0):
    A = np.array(sorted(A)); N = len(A); X = A.max()
    G = 1 << int(math.ceil(math.log2(64 * X)))
    x = np.pi * np.arange(G + 1) / G
    c = np.zeros(2 * G); c[A] = 1
    f = np.fft.rfft(c).real[:G + 1]
    loc = [j for j in range(1, G) if f[j] <= f[j - 1] and f[j] <= f[j + 1]]
    Af = A.astype(float); vals = []
    for j in loc:
        xx = x[j]
        for _ in range(30):
            d1 = -(Af * np.sin(Af * xx)).sum(); d2 = -(Af * Af * np.cos(Af * xx)).sum()
            if d2 <= 0: break
            xx -= d1 / d2
        vals.append((np.cos(Af * xx).sum(), xx))
    vals.sort(); M = -vals[0][0]; xs = vals[0][1]
    n1 = sum(1 for v, _ in vals if v <= -0.99 * M); n3 = sum(1 for v, _ in vals if v <= -0.97 * M)
    # profile
    n = np.arange(0, X + 1 + int(6 * bw)); ind = np.zeros(len(n)); ind[A] = 1
    ext = np.concatenate([ind[::-1][:-1], ind])                       # even extension n = -..+
    k = np.arange(-int(6 * bw), int(6 * bw) + 1); ker = np.exp(-k ** 2 / (2 * bw * bw)); ker /= ker.sum()
    w = np.convolve(ext, ker, 'same')[len(ind) - 1:]                  # w_n for n >= 0
    w[0] = 0
    rho = (w ** 2).sum() / (w.max() * w.sum())
    e = ind - w; e[0] = 0
    sigE = math.sqrt((e[1:] ** 2).sum() / 2)
    cc = np.zeros(2 * G); cc[:len(w)] = w; main = np.fft.rfft(cc).real[:G + 1]
    E = f - main
    bulk = x > 8.0 / X
    Eb = E[bulk]; sk = float(((Eb - Eb.mean()) ** 3).mean() / Eb.std() ** 3)
    cE = -Eb.min() / sigE
    jx = int(round(xs / np.pi * G))
    return dict(N=N, X=int(X), M=round(M, 5), R=round(M / math.sqrt(N), 5), x_star=round(xs, 4), x_star_units=round(xs * X / math.pi, 2),
                dips_1pct=n1, dips_3pct=n3, rho=round(rho, 4), sigma_E_over_sqrtN=round(sigE / math.sqrt(N), 4), c_E=round(cE, 3),
                skew_E=round(sk, 3), main_at_x=round(float(main[jx]), 3), E_at_x=round(float(E[jx]), 3))

if __name__ == "__main__":
    for line in open(sys.argv[1]):
        A = parse(line)
        if A: print(json.dumps(analyse(A)), flush=True)
