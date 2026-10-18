"""Referee falsification tests for P16, lemma by lemma (independent code; imports nothing from src/ except the Singer
generator).  Usage: .venv/bin/python src/agents/p16_review_lemmas.py [maxlog2grid]

For every test set S (Bu sets + adversarial Sidon sets):
  (B2)   S is Sidon in the full sense (all s+t, s<=t, distinct), A(S) is a genuine set of k(k-1) positive integers.
  (S0)   identity f_A = P^2 - k/2 - C/2 at 400 random real x (direct cosine sum over A on the left).
  (S1)   #{(u1..u4) in (±T)^4 : sum = 0} by exact integer pair-sum counting, vs 6(2k^2-k); second evaluator: alias-free
         FFT-grid mean of C^4 (grid size > 4 max T, so the grid mean of C^4 is exactly the Fourier mean).
  (S2)   visit lemma: exact Sx(h) = sum_s sinc^2(|b_s| h/2) <= Sbar(h) on a log grid of h; smallest grid h with Sx(h) < delta
         (h_ex) vs the Sbar root (h_bar); longest run of |P| >= delta on a fine grid (cyclic, x-units) vs 2 h_ex.
  (S3/4) with h = h_bar, windows c_j = j(2h+2r): fraction of windows with NO visit y having C(y) > -eta k ("bad" windows,
         which the proof shows cannot be all windows when the P16 inequality holds); measure of {C <= -eta k/2} vs the
         Chebyshev bound; actual half-width of {C <= -eta k/2} around the deepest bad visit vs the Lipschitz radius r.
All grid statements are numerical evidence only (no interval certification).
"""
import sys, math, json
import numpy as np
sys.path.insert(0, 'src')
from singer import singer

MAXLOG = int(sys.argv[1]) if len(sys.argv) > 1 else 23
AL, BE, GA = math.sqrt(2 / 3), (2 / 3) ** 0.25, 1 + math.sqrt(4 / 3) + (4 / 3) ** 0.25


def is_B2(S):
    S = sorted(S); k = len(S)
    sums = [S[i] + S[j] for i in range(k) for j in range(i, k)]
    return len(set(sums)) == len(sums)


def A_of_S(S):
    k = len(S); out = []
    for i in range(k):
        for j in range(i + 1, k):
            out.append(3 * abs(S[i] - S[j])); out.append(abs(3 * (S[i] + S[j]) + 1))
    A = np.array(out, dtype=np.int64)
    ok = len(np.unique(A)) == k * (k - 1) and A.min() > 0
    return A, ok


def sbar(h):
    X = 2 / h
    return (8 / h ** 2) * (2 * AL / 3 * X ** -1.5 + 4 * BE / 7 * X ** -1.75 + GA / 2 * X ** -2)


def hbar(delta):
    if delta <= GA: return None
    lo, hi = -300.0, 50.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if sbar(math.exp(mid)) >= delta else (lo, mid)
    return math.exp(hi)


def Sx(b, h):
    u = np.abs(b) * h / 2
    return float(np.sum(np.where(u == 0, 1.0, (np.sin(u) / np.where(u == 0, 1, u)) ** 2)))


def quad_count(T):
    U = np.concatenate([T, -T]).astype(np.int64)
    ps = (U[:, None] + U[None, :]).ravel()
    _, cnt = np.unique(ps, return_counts=True)
    return int(np.sum(cnt.astype(np.int64) ** 2))     # U symmetric, so r(v) = r(-v)


def longest_run(mask):
    """longest cyclic run of True in mask (returns count); all-True -> len."""
    if mask.all(): return len(mask)
    m = np.concatenate([mask, mask])
    d = np.diff(np.concatenate([[0], m.astype(np.int8), [0]]))
    st, en = np.where(d == 1)[0], np.where(d == -1)[0]
    return int(min((en - st).max(), len(mask)))


def analyse(name, S, etas=(0.1, 0.3, 0.5), rng=np.random.default_rng(7)):
    S = sorted(int(s) for s in S); k = len(S); L = max(abs(s) for s in S)
    rec = dict(name=name, k=k, L=L, L_over_k2=L / k ** 2)
    rec['B2'] = is_B2(S)
    A, ok = A_of_S(S); rec['A_genuine'] = bool(ok)
    Sa = np.array(S, dtype=np.float64); T = 6 * np.array(S, dtype=np.int64) + 1; b = 3 * Sa + 0.5
    # S0 identity
    xs = rng.uniform(-50, 50, 400)
    lhs = np.array([np.cos(A.astype(np.float64) * x).sum() for x in xs])
    Px = np.cos(np.outer(xs, b)).sum(1); Cx = np.cos(np.outer(xs, T.astype(np.float64))).sum(1)
    rec['S0_identity_maxerr'] = float(np.abs(lhs - (Px ** 2 - k / 2 - Cx / 2)).max())
    # S1 fourth moment, two evaluators
    cnt = quad_count(T); rec['S1_count'] = cnt; rec['S1_pred'] = 6 * (2 * k * k - k)
    Tmax = int(np.abs(T).max())
    G = 1 << max(12, min(MAXLOG, math.ceil(math.log2(32 * Tmax))))
    if G <= 4 * Tmax: raise ValueError("grid too small")
    coef = np.zeros(G // 2 + 1); np.add.at(coef, np.abs(T), 1.0)
    # irfft(c)[i] = (1/G)(c0 + 2 sum_{m>0} c_m cos(2 pi m i/G)) for m < G/2, so sum_m c_m cos = irfft*G/2
    Cu = np.fft.irfft(coef, n=G) * (G / 2)
    assert abs(Cu[0] - k) < 1e-6 * k
    rec['S1_fftmean_C4'] = float(np.mean(Cu ** 4)); rec['S1_pred_C4'] = 0.75 * k * k - 0.375 * k
    rec['grid'] = G; du = 2 * math.pi / G
    # P(y) = C(y/2): on the u-grid, y = 2u, so P at y_i = 2 u_i is Cu[i]; C(y_i) = Cu[2i mod G]; x-spacing dx = 2 du.
    dx = 2 * du
    Py = Cu                         # y in [0, 4 pi), step dx; |P| has period 2 pi in y (P(y+2pi) = -P(y))
    Cy = Cu[(2 * np.arange(G)) % G]
    # a grid point i is a (numerical) visit if |P_i| < delta, or if P changes sign between i and i+1 and |P_i| <= |P_{i+1}|
    # (IVT: a sign change forces a zero, hence |P| < delta, in between; narrow crossings are otherwise missed by the grid)
    sc = np.sign(Py) != np.sign(np.roll(Py, -1))
    sc_vis = (sc & (np.abs(Py) <= np.abs(np.roll(Py, -1)))) | np.roll(sc & (np.abs(Py) > np.abs(np.roll(Py, -1))), 1)
    hs = np.exp(np.linspace(math.log(1e-6), math.log(10.0), 3000))
    Sxh = np.array([Sx(b, h) for h in hs])
    rec['S2_max_Sx_over_Sbar'] = float(np.max(Sxh / np.array([sbar(h) for h in hs])))
    rec['etas'] = {}
    for eta in etas:
        delta = math.sqrt(eta * k / 2); e = {}
        idx = np.where(Sxh < delta)[0]
        h_ex = float(hs[idx[0]]) if len(idx) else None
        h_b = hbar(delta)
        half = G // 2                   # |P| period 2 pi in y = G/2 grid steps
        isvis = (np.abs(Py) < delta) | sc_vis
        run = longest_run(~isvis[:half]) + 1    # +1: conservative upper bound on run length in steps
        e.update(delta=delta, h_ex=h_ex, h_bar=h_b, run_len=run * dx)
        if h_ex: e['run_over_2h_ex'] = run * dx / (2 * h_ex)
        if h_b: e['run_over_2h_bar'] = run * dx / (2 * h_b)
        if h_b and 2 * h_b < 2 * math.pi:
            r = eta / (2 * (6 * L + 1)); n = int(math.floor(2 * math.pi / (2 * h_b + 2 * r)))
            bad = 0; worst = None
            for j in range(n):
                c = j * (2 * h_b + 2 * r)
                i0, i1 = int(math.ceil((c - h_b) / dx)), int(math.floor((c + h_b) / dx))
                ii = np.arange(i0, i1 + 1) % G
                vis = ii[isvis[ii]]
                if len(vis) == 0: e.setdefault('windows_without_grid_visit', 0); e['windows_without_grid_visit'] += 1; continue
                if Cy[vis].max() <= -eta * k:
                    bad += 1
                    y = vis[np.argmin(Cy[vis])]
                    if worst is None or Cy[y] < Cy[worst]: worst = y
            e.update(n_windows=n, bad_windows=bad, r=r)
            if worst is not None:
                # actual half-width of {C <= -eta k/2} around worst bad visit (in y units), via the Cy array
                thr = -eta * k / 2; w = 0
                while w < G // 4 and Cy[(worst + w + 1) % G] <= thr and Cy[(worst - w - 1) % G] <= thr: w += 1
                e['bad_visit_C_over_k'] = float(Cy[worst] / k); e['actual_halfwidth_over_r'] = (w * dx) / r
            tau = eta * k / 2
            meas = float(np.mean(Cu <= -tau)) * 2 * math.pi
            e['meas_C_le_-etak/2'] = meas; e['cheb_bound'] = 2 * math.pi * rec['S1_pred_C4'] / tau ** 4
            e['P16_condition_2rn'] = 2 * r * n; e['P16_condition_rhs'] = 24 * math.pi / (eta ** 4 * k * k)
        rec['etas'][str(eta)] = e
    return rec


def centred(S):
    S = sorted(S); c = (S[0] + S[-1]) // 2
    return [s - c for s in S]


def greedy_near_zero(k):
    S, sums = [], set()
    cand = 0
    seq = (x for m in range(10 ** 9) for x in ((m,) if m == 0 else (m, -m)))
    for x in seq:
        new = {x + s for s in S} | {2 * x}
        if len(new) == len(S) + 1 and not (new & sums):
            S.append(x); sums |= new
            if len(S) == k: return sorted(S)


def mian_chowla(k):
    S, sums = [], set(); x = 0
    while len(S) < k:
        x += 1
        new = {x + s for s in S} | {2 * x}
        if len(new) == len(S) + 1 and not (new & sums):
            S.append(x); sums |= new
    return S


def erdos_turan(p):
    return [2 * p * i + (i * i % p) for i in range(p)]


if __name__ == '__main__':
    tests = []
    d = json.load(open('examples/bu_reproduction_certified.json'))
    for key in d: tests.append(('Bu_' + key, d[key]['S']))
    D, v = singer(101); tests.append(('Singer101_centred_full', centred(D)))
    D, v = singer(307); tests.append(('Singer307_centred_full', centred(D)))
    tests.append(('Singer101_shifted_positive_far', [x + 10 ** 5 for x in singer(101)[0]]))
    tests.append(('ErdosTuran211_centred', centred(erdos_turan(211))))
    tests.append(('ErdosTuran101_dilated_x7_centred', [7 * s for s in centred(erdos_turan(101))]))
    tests.append(('greedy_near_zero_k80', greedy_near_zero(80)))
    tests.append(('greedy_near_zero_k150', greedy_near_zero(150)))
    tests.append(('MianChowla_k100_positive', mian_chowla(100)))
    tests.append(('lacunary_2^i_k16', [2 ** i for i in range(16)]))
    tests.append(('lacunary_-2^i_k16', [-(2 ** i) for i in range(16)]))
    out = []
    for name, S in tests:
        rec = analyse(name, S); out.append(rec)
        print(f"\n== {name}: k={rec['k']} L={rec['L']} (L/k^2={rec['L_over_k2']:.2f}) B2={rec['B2']} genuine={rec['A_genuine']} grid=2^{int(math.log2(rec['grid']))}")
        print(f"   S0 identity max err {rec['S0_identity_maxerr']:.1e} | S1 count {rec['S1_count']} vs 6(2k^2-k)={rec['S1_pred']}"
              f" | FFT mean C^4 {rec['S1_fftmean_C4']:.4f} vs {rec['S1_pred_C4']:.4f} | max Sx/Sbar {rec['S2_max_Sx_over_Sbar']:.3f}")
        for eta, e in rec['etas'].items():
            s = f"   eta={eta}: delta={e['delta']:.2f} h_ex={e['h_ex'] and round(e['h_ex'],5)} h_bar={e['h_bar'] and round(e['h_bar'],5)} run={e['run_len']:.5f}"
            if 'run_over_2h_ex' in e: s += f" run/2h_ex={e['run_over_2h_ex']:.3f}"
            if 'run_over_2h_bar' in e: s += f" run/2h_bar={e['run_over_2h_bar']:.3f}"
            if 'n_windows' in e:
                s += f" | windows={e['n_windows']} bad={e['bad_windows']}"
                if 'windows_without_grid_visit' in e: s += f" NO-VISIT={e['windows_without_grid_visit']}"
                if 'actual_halfwidth_over_r' in e: s += f" worstC/k={e['bad_visit_C_over_k']:.3f} halfwidth/r={e['actual_halfwidth_over_r']:.0f}"
                s += f" | meas(C<=-eta k/2)={e['meas_C_le_-etak/2']:.2e} <= cheb {e['cheb_bound']:.2e}"
                s += f" | 2rn={e['P16_condition_2rn']:.2e} vs {e['P16_condition_rhs']:.2e}"
            print(s, flush=True)
    json.dump(out, open('src/agents/p16_review_lemmas.json', 'w'), indent=1, default=str)
