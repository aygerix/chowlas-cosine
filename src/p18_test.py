"""E28: test the P18 dense min-max lemma on record sets.  For A ⊂ [1,X], W = w0·(Fejér K_Y or Jackson-type tent
autocorrelation), Y <= X+1, p.d. with W_0 = w0 (any w0 > 0; β = π w0, correction w0/2), e = 1_A − W, G = f_A − Ŵ, Λ = max|G| (FFT 64X, uncertified):
    P18 bound  B = Σ n^2 e_n^2 / (2 X^2 Λ) − w0/2   (rigorous given exact Λ; here Λ is a grid estimate).
Reports the best B over a (w0, Y) grid, M (from the record's certificate), B/M, Λ/sqrt(X), and where |G| peaks.
Usage: python src/p18_test.py
"""
import sys, json, math
import numpy as np


def grid_vals(coef, G):
    c = np.zeros(G); c[:len(coef)] = coef
    return np.real(np.fft.fft(c))              # Σ coef_n cos(n x_k), x_k = 2πk/G


def p18(A, M):
    X = max(A); n = np.arange(X + 1); ind = np.zeros(X + 1); ind[A] = 1.0
    G = 1 << math.ceil(math.log2(64 * X)); xs = 2 * np.pi * np.arange(G) / G
    best = None
    for fam in ('fejer', 'jackson'):
      for w0 in np.linspace(0.3, 2.5, 23):
        for Y in range(max(2, X // 4), X + 2, max(1, X // 60)):
            if fam == 'fejer':
                W = w0 * np.clip(1 - n / Y, 0, None)          # w0 * Fejér K_Y: p.d., support |n| < Y <= X+1
            else:
                h = Y // 2; t = np.clip(1 - np.arange(-h, h + 1) / (h + 1), 0, None)
                ac = np.correlate(t, t, 'full')[2 * h:]; ac = ac / ac[0]   # autocorrelation of a tent: p.d.
                W = np.zeros(X + 1); m = min(len(ac), X + 1); W[:m] = w0 * ac[:m]
                if len(ac) > X + 1: continue
            W = W.copy(); W[0] = 0.0
            e = ind - W; g = grid_vals(e, G); Lam = np.abs(g).max()
            B = (n * n * e * e).sum() / (2 * X * X * Lam) - w0 / 2
            if best is None or B > best[0]:
                k = int(np.abs(g).argmax())
                best = (B, w0, Y, Lam, xs[k] if xs[k] <= np.pi else xs[k] - 2 * np.pi, g[k], (e * e).sum())
    B, w0, Y, Lam, xpk, gpk, e2 = best
    return dict(N=len(A), X=X, M=M, R=M / math.sqrt(len(A)), B=B, B_over_M=B / M, w0=w0, Y=Y,
                Lam_over_sqrtX=Lam / math.sqrt(X), x_peak=xpk, G_peak=gpk, e2_over_N=e2 / len(A))


if __name__ == "__main__":
    recs = json.load(open('examples/smallN_best.json'))
    rows = []
    for key in ['20', '24', '27', '30', '34', '35', '36', '40', '45', '50', '55']:
        if key in recs:
            r = recs[key]; rows.append((f"box{key}", r['A'], -r['cert_lower']))
    m45 = json.load(open('examples/milp/N45_best.json')); rows.append(("milp45", m45['A'], -m45['cert_lower']))
    sb = json.load(open('examples/singer_bu/certified.json'))
    sys.path.insert(0, 'src'); from bu import A_of_S
    for q in ['61', '101']:
        rows.append((f"SB{q}", sorted(A_of_S(sb[q]['S'])), -sb[q]['cert_lower']))
    for name, A, M in rows:
        d = p18(sorted(A), M)
        print(f"{name:8s} N={d['N']:6d} X={d['X']:6d} R={d['R']:.4f} M={M:8.3f} B={d['B']:8.3f} B/M={d['B_over_M']:.3f} "
              f"w0={d['w0']:.2f} Y/X={d['Y']/d['X']:.2f} Λ/√X={d['Lam_over_sqrtX']:.3f} peak x={d['x_peak']:+.3f} "
              f"G={d['G_peak']:+.2f} Σe²/N={d['e2_over_N']:.3f}", flush=True)
