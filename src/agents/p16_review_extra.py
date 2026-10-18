"""Referee extra checks for P16 (independent code).
 (i)   Lindstrom F(m) < m^{1/2} + m^{1/4} + 1 vs exact maximal Sidon sizes (brute force m <= 45; OGR table A003022, m <= 586).
 (ii)  N(t) = #{s : |3s+1/2| <= t} <= alpha t^{1/2} + beta t^{1/4} + gamma, exactly, for the P16 test sets.
 (iii) large-sieve sanity: greedy 2h-separated points at the most negative values of C; sum C^4 vs (4D + pi/h) E[C^4].
 (iv)  Lipschitz slack: half-width of {C <= min C / 2} around the global min of C vs the Lipschitz radius |min C|/(2k(6L+1)).
 (v)   density version of the visit lemma (referee remark): best E with N(t) <= rho t + E for rho = 2k/(3L)*c, c in {1,2,4},
       and the resulting window h = 4 rho/(delta - E) vs the Sbar window h_bar, at eta = 1/2.
"""
import sys, math, json
import numpy as np
sys.path.insert(0, 'src'); sys.path.insert(0, 'src/agents')
from p16_review_lemmas import greedy_near_zero, mian_chowla, erdos_turan, centred, hbar
from singer import singer

AL, BE, GA = math.sqrt(2 / 3), (2 / 3) ** 0.25, 1 + math.sqrt(4 / 3) + (4 / 3) ** 0.25


def max_sidon(m):
    best = [0]
    def rec(S, diffs, nxt):
        if len(S) > best[0]: best[0] = len(S)
        if len(S) + (m - nxt) <= best[0]: return
        for x in range(nxt, m):
            nd = {x - s for s in S}
            if len(nd) == len(S) and not (nd & diffs):
                rec(S + [x], diffs | nd, x + 1)
    rec([0], set(), 1)
    return best[0]


OGR = [0, 1, 3, 6, 11, 17, 25, 34, 44, 55, 72, 85, 106, 127, 151, 177, 199, 216, 246, 283, 333, 356, 372, 425, 480, 492, 553, 585]

if __name__ == '__main__':
    print("(i) Lindstrom check")
    worst = 0
    for m in range(1, 46):
        F = max_sidon(m)
        Fo = max(n for n in range(1, 29) if OGR[n - 1] <= m - 1)
        assert F == Fo, (m, F, Fo)
        worst = max(worst, F / (m ** .5 + m ** .25 + 1))
    for m in range(46, 587):
        Fo = max(n for n in range(1, 29) if OGR[n - 1] <= m - 1)
        worst = max(worst, Fo / (m ** .5 + m ** .25 + 1))
    print(f"   brute force (m<=45) agrees with OGR table; max F(m)/(m^.5+m^.25+1) over m<=586 = {worst:.4f} (<1 required)")
    d = json.load(open('examples/bu_reproduction_certified.json'))
    tests = [('Bu_' + key, d[key]['S']) for key in d]
    tests += [('Singer307_centred_full', centred(singer(307)[0])), ('ErdosTuran211_centred', centred(erdos_turan(211))),
              ('greedy_near_zero_k150', greedy_near_zero(150)), ('MianChowla_k100_positive', mian_chowla(100)),
              ('Singer101_centred_full', centred(singer(101)[0]))]
    print("(ii) N(t) vs Lindstrom-type bound, (iv) Lipschitz slack, (v) density visit lemma")
    for name, S in tests:
        S = np.array(sorted(S)); k = len(S); L = int(np.abs(S).max())
        bs = np.sort(np.abs(3 * S + 0.5))
        N = np.arange(1, k + 1)                      # N(t) jumps to j at t = bs[j-1]
        U = AL * np.sqrt(bs) + BE * bs ** 0.25 + GA
        ratio = float((N / U).max())
        # (iv) global min of C on alias-free grid
        T = np.abs(6 * S + 1); G = 1 << min(23, math.ceil(math.log2(32 * T.max())))
        coef = np.zeros(G // 2 + 1); np.add.at(coef, T, 1.0)
        Cu = np.fft.irfft(coef, n=G) * (G / 2); du = 2 * math.pi / G
        i0 = int(np.argmin(Cu)); cmin = float(Cu[i0]); w = 0
        while w < G // 4 and Cu[(i0 + w + 1) % G] <= cmin / 2 and Cu[(i0 - w - 1) % G] <= cmin / 2: w += 1
        rlip = abs(cmin) / 2 / (k * (6 * L + 1))
        # (iii) large sieve sanity at h = h_bar(eta=1/2) and at h = 1/(6L)
        e4 = 0.75 * k * k - 0.375 * k; D = 6 * L + 1
        ls = []
        for h in (hbar(math.sqrt(k / 4)) or 1.0, 1.0 / (6 * L), 10.0 / (6 * L)):
            if h is None or h > 1: continue
            order = np.argsort(Cu); taken = []; sep = int(math.ceil(2 * h / du)); blocked = np.zeros(G, bool); tot = 0.0
            for i in order[:200000]:
                if Cu[i] >= 0: break
                if blocked[i]: continue
                tot += Cu[i] ** 4; taken.append(i)
                lo, hi = i - sep + 1, i + sep
                idx = np.arange(lo, hi) % G; blocked[idx] = True
            ls.append((h, len(taken), tot / ((4 * D + math.pi / h) * e4)))
        # (v) density version: rho = c * 2k/(3L)
        delta = math.sqrt(k / 4); hb = hbar(delta); dens = []
        for c in (1, 2, 4):
            rho = c * 2 * k / (3 * L)
            E = max(0.0, float((N - rho * bs).max()))   # smallest E >= 0 with N(t) <= rho t + E for all t (N(0) = 0)
            hv = 4 * rho / (delta - E) if delta > E else None
            dens.append((c, round(E, 2), hv))
        print(f"   {name}: k={k} L={L}  max N/U={ratio:.3f} | min C={cmin:.1f} ({cmin/k:.3f}k) halfwidth/r_lip={w*du/rlip:.1f} |"
              f" LS ratio (h, #pts, sumC^4/bound)={[(f'{a:.2e}', b, round(c_, 4)) for a, b, c_ in ls]} |"
              f" density visit lemma (c, E, h)={dens} vs h_bar={hb}", flush=True)
