"""Small-N mechanism probe for Chowla's cosine problem.

Goal: estimate K(N) = min_{|A|=N} M(A),  M(A) = -min_x sum_{a in A} cos(a x),
for N = 4..100, and study the structure of near-optimal sets.

Convention: f_A(x) = sum_{a in A} cos(a x).  Grids are x_j = 2 pi j / G
(SA, j = 0..G/2) or x_j = pi j / H (exhaustive, j = 0..H); since f_A is even
and 2 pi-periodic, [0, pi] suffices.

Two engines, both in a small C kernel compiled on first use (cc -O3):

  (1) sa_run  : simulated annealing over N-subsets of [1, cap].  Objective is
      the GRID value M_grid(A) = -min_j f_A(x_j) with G >= 16*cap.  A swap is
      O(G) via a cos table; most proposals are rejected early by checking a
      watch list of the current deepest local minima first, then the full grid
      with early exit against the Metropolis threshold.  UNCERTIFIED.

  (2) exh_run : provably complete enumeration of all N-subsets of [1, L].
      Since every grid value f_A(x_j) >= min f_A, M_grid(A) <= M(A): a grid
      lower-bounds M.  Given a threshold thr >= K_box (a certified upper bound
      from an explicit set), every A with M(A) <= thr satisfies M_grid(A) <= thr.
      DFS over increasing elements with partial grid sums g_S and the valid
      prune  exists j: g_S(x_j) + U_j(last, k) < -thr,  U_j(last,k) = sum of the
      k largest cos(a x_j), a in (last, L]  (k = elements still to choose).
      Leaves surviving the coarse grid are re-checked on a finer grid; all
      survivors are returned for accurate evaluation.  Completeness holds up
      to floating-point rounding of the grid sums (~1e-13 << margins).

All reported numbers are re-evaluated with chowla.min_estimate_fft (uncertified)
and the final best per N with chowla.certify_lower_bound (rigorous lower bound
for min f_A, hence rigorous UPPER bound for M(A) and R(A)).

CLI:
  python src/smallN_search.py exhaustive  # complete box searches
  python src/smallN_search.py sa          # heuristic search N=4..100
  python src/smallN_search.py analyze     # structure + trend fit
"""
from __future__ import annotations

import ctypes
import json
import math
import os
import subprocess
import sys
import time
from itertools import combinations
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from chowla import certify_lower_bound, min_estimate_fft  # noqa: E402
from families import erdos_turan_sidon, is_prime, is_sidon  # noqa: E402

OUT_JSON = os.path.join(ROOT, "examples", "smallN_best.json")
RUN_DIR = os.path.join(ROOT, "examples", "smallN_runs")

# ---------------------------------------------------------------------------
# C kernel
# ---------------------------------------------------------------------------

C_SRC = r"""
#include <math.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef struct { uint64_t s[4]; } rng_t;
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t rnext(rng_t *r) {
    uint64_t *s = r->s;
    const uint64_t result = rotl(s[1] * 5, 7) * 9;
    const uint64_t t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3]; s[2] ^= t; s[3] = rotl(s[3], 45);
    return result;
}
static void rseed(rng_t *r, uint64_t seed) {
    for (int i = 0; i < 4; i++) {
        seed += 0x9E3779B97F4A7C15ULL;
        uint64_t z = seed;
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
        z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
        r->s[i] = z ^ (z >> 31);
    }
}
static inline double runif(rng_t *r) { return (rnext(r) >> 11) * 0x1.0p-53; }
static inline int64_t rint_(rng_t *r, int64_t n) { return (int64_t)(runif(r) * (double)n); }

/* watch list: K lowest local minima of g[0..H] (g even, symmetric ends) */
static int build_watch(const double *g, int H, int K, int *W) {
    double wv[256]; int cnt = 0;
    if (K > 256) K = 256;
    for (int j = 0; j <= H; j++) {
        double l = (j == 0) ? g[1] : g[j - 1];
        double r = (j == H) ? g[H - 1] : g[j + 1];
        double v = g[j];
        if (v <= l && v <= r) {
            if (cnt < K) { wv[cnt] = v; W[cnt] = j; cnt++; }
            else {
                int mi = 0; for (int t = 1; t < K; t++) if (wv[t] > wv[mi]) mi = t;
                if (v < wv[mi]) { wv[mi] = v; W[mi] = j; }
            }
        }
    }
    /* sort ascending by value so the deepest is tested first */
    for (int a = 1; a < cnt; a++) {
        double v = wv[a]; int jj = W[a]; int b = a - 1;
        while (b >= 0 && wv[b] > v) { wv[b + 1] = wv[b]; W[b + 1] = W[b]; b--; }
        wv[b + 1] = v; W[b + 1] = jj;
    }
    return cnt;
}

/* Simulated annealing.  Returns best grid M; best set in best_out.
   stats[0]=proposals, [1]=watch rejections, [2]=full passes, [3]=accepts */
double sa_run(int N, int L, int G, const int *init, int64_t iters, double T0, double T1,
              uint64_t seed, double pglobal, int D, int K, int *best_out, int *cur_out,
              int64_t *stats) {
    int H = G / 2;
    rng_t rng; rseed(&rng, seed);
    double *tab = (double *)malloc(sizeof(double) * G);
    for (int k = 0; k < G; k++) tab[k] = cos(2.0 * M_PI * (double)k / (double)G);
    double *g = (double *)calloc(H + 1, sizeof(double));
    double *tmp = (double *)malloc(sizeof(double) * (H + 1));
    char *inA = (char *)calloc(L + 2, 1);
    int *A = (int *)malloc(sizeof(int) * N);
    int W[256];
    for (int i = 0; i < N; i++) {
        A[i] = init[i]; inA[A[i]] = 1;
        int64_t idx = 0;
        for (int j = 0; j <= H; j++) { g[j] += tab[idx]; idx += A[i]; if (idx >= G) idx -= G; }
    }
    double mn = 1e300;
    for (int j = 0; j <= H; j++) if (g[j] < mn) mn = g[j];
    double cur = -mn, best = cur;
    memcpy(best_out, A, sizeof(int) * N);
    int nw = build_watch(g, H, K, W);
    double T = T0, fac = (iters > 1) ? pow(T1 / T0, 1.0 / (double)iters) : 1.0;
    int64_t nprop = 0, nwrej = 0, nfull = 0, nacc = 0;
    for (int64_t it = 0; it < iters; it++, T *= fac) {
        int i = (int)rint_(&rng, N);
        int aold = A[i], anew;
        if (runif(&rng) < pglobal) anew = 1 + (int)rint_(&rng, L);
        else {
            int d = 1 + (int)rint_(&rng, 2 * D);
            if (d > D) d = D - d;            /* d in [-D,-1] U [1,D] */
            anew = aold + d;
        }
        if (anew < 1 || anew > L || inA[anew]) continue;
        nprop++;
        double u = runif(&rng);
        double thr = cur - T * log(u > 1e-300 ? u : 1e-300);   /* accept iff newM <= thr */
        int bad = 0;
        for (int w = 0; w < nw; w++) {
            int j = W[w];
            double v = g[j] - tab[((int64_t)aold * j) % G] + tab[((int64_t)anew * j) % G];
            if (v < -thr) { bad = 1; break; }
        }
        if (bad) { nwrej++; continue; }
        nfull++;
        int64_t io = 0, in = 0; double m2 = 1e300;
        for (int j = 0; j <= H; j++) {
            double v = g[j] - tab[io] + tab[in];
            tmp[j] = v;
            if (v < m2) { m2 = v; if (v < -thr) { bad = 1; break; } }
            io += aold; if (io >= G) io -= G;
            in += anew; if (in >= G) in -= G;
        }
        if (bad) continue;
        nacc++;
        double *sw = g; g = tmp; tmp = sw;
        cur = -m2; A[i] = anew; inA[aold] = 0; inA[anew] = 1;
        nw = build_watch(g, H, K, W);
        if (cur < best - 1e-12) { best = cur; memcpy(best_out, A, sizeof(int) * N); }
    }
    memcpy(cur_out, A, sizeof(int) * N);
    stats[0] = nprop; stats[1] = nwrej; stats[2] = nfull; stats[3] = nacc;
    free(tab); free(g); free(tmp); free(inA); free(A);
    return best;
}

/* ---------------- exhaustive enumeration ---------------- */
typedef struct {
    int N, L, H, H2;
    double thr;
    const double *C;      /* C[a*(H+1)+j] = cos(pi a j / H) */
    const double *U;      /* U[(k*(L+1)+last)*(H+1)+j] */
    double *lev;          /* (N+1)*(H+1) */
    int cur[64];
    int *out; double *outM; int64_t cap, nout;
    int64_t nodes, leaves, survivors_coarse;
    int hint[64];
} ex_t;

static double fine_min(ex_t *e) {
    double mn = 1e300;
    for (int j = 0; j <= e->H2; j++) {
        double x = M_PI * (double)j / (double)e->H2, s = 0;
        for (int i = 0; i < e->N; i++) s += cos((double)e->cur[i] * x);
        if (s < mn) mn = s;
    }
    return mn;
}

static void dfs(ex_t *e, int depth, int last) {
    int N = e->N, L = e->L, H = e->H, Hp = H + 1;
    int k = N - depth;                 /* elements still to choose, >= 1 */
    const double *gS = e->lev + (size_t)depth * Hp;
    double *ng = e->lev + (size_t)(depth + 1) * Hp;
    double nthr = -e->thr;
    for (int a = last + 1; a <= L - k + 1; a++) {
        const double *Ca = e->C + (size_t)a * Hp;
        const double *Ua = e->U + ((size_t)(k - 1) * (L + 1) + a) * Hp;
        e->nodes++;
        int pruned = 0;
        int h = e->hint[depth];
        /* first test the hint index, then full fused pass */
        if (gS[h] + Ca[h] + Ua[h] < nthr) pruned = 1;
        else {
            for (int j = 0; j < Hp; j++) {
                double v = gS[j] + Ca[j];
                ng[j] = v;
                if (v + Ua[j] < nthr) { pruned = 1; e->hint[depth] = j; break; }
            }
        }
        if (pruned) continue;
        e->cur[depth] = a;
        if (k == 1) {
            e->leaves++; e->survivors_coarse++;
            double fm = fine_min(e);
            if (fm >= nthr) {
                if (e->nout < e->cap) {
                    memcpy(e->out + e->nout * N, e->cur, sizeof(int) * N);
                    e->outM[e->nout] = -fm;
                }
                e->nout++;
            }
        } else {
            dfs(e, depth + 1, a);
        }
    }
}

/* Enumerate all N-subsets of [1,L] whose first npre elements equal pre[].
   Returns number of survivors (may exceed cap; then only cap stored). */
int64_t exh_run(int N, int L, int H, int H2, double thr, int npre, const int *pre,
                int *out, double *outM, int64_t cap, int64_t *stats) {
    int Hp = H + 1;
    double *C = (double *)malloc(sizeof(double) * (size_t)(L + 1) * Hp);
    for (int a = 0; a <= L; a++)
        for (int j = 0; j < Hp; j++) C[(size_t)a * Hp + j] = cos(M_PI * (double)a * (double)j / (double)H);
    /* U[k][last][j] = sum of k largest C[a][j] over a in (last, L]; k=0..N */
    double *U = (double *)malloc(sizeof(double) * (size_t)(N + 1) * (L + 1) * Hp);
    double *vals = (double *)malloc(sizeof(double) * (L + 1));
    for (int j = 0; j < Hp; j++) {
        int cnt = 0;   /* vals sorted descending, for a in (last, L] */
        for (int last = L; last >= 0; last--) {
            for (int k = 0; k <= N; k++) {
                double s = 0;
                if (k <= cnt) { for (int t = 0; t < k; t++) s += vals[t]; }
                else s = 1e300;                       /* unreachable */
                U[((size_t)k * (L + 1) + last) * Hp + j] = s;
            }
            if (last >= 1) {   /* insert value of a = last for the next (smaller) last */
                double v = C[(size_t)last * Hp + j];
                int p = cnt; while (p > 0 && vals[p - 1] < v) { vals[p] = vals[p - 1]; p--; }
                vals[p] = v; cnt++;
            }
        }
    }
    ex_t e; memset(&e, 0, sizeof(e));
    e.N = N; e.L = L; e.H = H; e.H2 = H2; e.thr = thr; e.C = C; e.U = U;
    e.lev = (double *)calloc((size_t)(N + 1) * Hp, sizeof(double));
    e.out = out; e.outM = outM; e.cap = cap;
    for (int i = 0; i < 64; i++) e.hint[i] = Hp - 1;
    /* prefix */
    int ok = 1, last = 0;
    for (int d = 0; d < npre; d++) {
        int a = pre[d];
        if (a <= last || a > L - (N - d) + 1) { ok = 0; break; }
        double *gS = e.lev + (size_t)d * Hp, *ng = e.lev + (size_t)(d + 1) * Hp;
        const double *Ua = U + ((size_t)(N - d - 1) * (L + 1) + a) * Hp;
        for (int j = 0; j < Hp; j++) {
            ng[j] = gS[j] + C[(size_t)a * Hp + j];
            if (ng[j] + Ua[j] < -thr) ok = 0;
        }
        e.cur[d] = a; last = a;
        if (!ok) break;
    }
    if (ok) {
        if (npre == N) {
            e.leaves = 1;
            double fm = fine_min(&e);
            if (fm >= -thr) { memcpy(out, e.cur, sizeof(int) * N); outM[0] = -fm; e.nout = 1; }
        } else dfs(&e, npre, last);
    }
    stats[0] = e.nodes; stats[1] = e.leaves; stats[2] = e.survivors_coarse;
    free(C); free(U); free(vals); free(e.lev);
    return e.nout;
}
"""

_LIB = None
_BUILD_DIR = os.path.join(HERE, ".build")


def _lib():
    global _LIB
    if _LIB is not None:
        return _LIB
    os.makedirs(_BUILD_DIR, exist_ok=True)
    import hashlib
    h = hashlib.sha1(C_SRC.encode()).hexdigest()[:12]
    so = os.path.join(_BUILD_DIR, f"smallN_{h}.so")
    if not os.path.exists(so):
        src = os.path.join(_BUILD_DIR, f"smallN_{h}.c")
        with open(src, "w") as fh:
            fh.write(C_SRC)
        tmp = so + f".{os.getpid()}.tmp"
        subprocess.check_call(["cc", "-O3", "-march=native", "-shared", "-fPIC", "-o", tmp, src, "-lm"])
        os.replace(tmp, so)
    lib = ctypes.CDLL(so)
    I32P = ctypes.POINTER(ctypes.c_int)
    I64P = ctypes.POINTER(ctypes.c_int64)
    F64P = ctypes.POINTER(ctypes.c_double)
    lib.sa_run.restype = ctypes.c_double
    lib.sa_run.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, I32P, ctypes.c_int64,
                           ctypes.c_double, ctypes.c_double, ctypes.c_uint64, ctypes.c_double,
                           ctypes.c_int, ctypes.c_int, I32P, I32P, I64P]
    lib.exh_run.restype = ctypes.c_int64
    lib.exh_run.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double,
                            ctypes.c_int, I32P, I32P, F64P, ctypes.c_int64, I64P]
    _LIB = lib
    return lib


def _iarr(x):
    a = np.ascontiguousarray(np.asarray(x, dtype=np.int32))
    return a, a.ctypes.data_as(ctypes.POINTER(ctypes.c_int))


def sa(N, cap, init, iters, T0=0.3, T1=0.004, seed=0, pglobal=0.4, D=3, K=24, oversample=16):
    lib = _lib()
    init = sorted(int(a) for a in init)
    assert len(init) == N and len(set(init)) == N and min(init) >= 1 and max(init) <= cap
    G = 1 << math.ceil(math.log2(oversample * cap + 1))
    ia, ip = _iarr(init)
    bo, bp = _iarr(np.zeros(N))
    co, cp = _iarr(np.zeros(N))
    st = np.zeros(4, dtype=np.int64)
    best = lib.sa_run(N, cap, G, ip, int(iters), T0, T1, ctypes.c_uint64(seed & (2**64 - 1)), pglobal,
                      D, K, bp, cp, st.ctypes.data_as(ctypes.POINTER(ctypes.c_int64)))
    return best, sorted(int(a) for a in bo), sorted(int(a) for a in co), st.tolist()


def exh(N, L, thr, prefix, H=None, H2=None, cap=200000):
    lib = _lib()
    H = H or 4 * L
    H2 = H2 or 32 * L
    pa, pp = _iarr(prefix if len(prefix) else [0])
    out = np.zeros(cap * N, dtype=np.int32)
    outM = np.zeros(cap)
    st = np.zeros(3, dtype=np.int64)
    n = lib.exh_run(N, L, H, H2, thr, len(prefix), pp, out.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
                    outM.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), cap,
                    st.ctypes.data_as(ctypes.POINTER(ctypes.c_int64)))
    k = min(n, cap)
    sets = [sorted(out[i * N:(i + 1) * N].tolist()) for i in range(k)]
    return n, sets, outM[:k].tolist(), st.tolist()


# ---------------------------------------------------------------------------
# Structured seeds
# ---------------------------------------------------------------------------

GOLOMB = {  # optimal Golomb rulers (verified Sidon at import)
    2: [0, 1], 3: [0, 1, 3], 4: [0, 1, 4, 6], 5: [0, 1, 4, 9, 11], 6: [0, 1, 4, 10, 12, 17],
    7: [0, 1, 4, 10, 18, 23, 25], 8: [0, 1, 4, 9, 15, 22, 32, 34],
    9: [0, 1, 5, 12, 25, 27, 35, 41, 44], 10: [0, 1, 6, 10, 23, 26, 34, 41, 53, 55],
    11: [0, 1, 4, 13, 28, 33, 47, 54, 64, 70, 72],
    12: [0, 2, 6, 24, 29, 40, 43, 55, 68, 75, 76, 85],
    13: [0, 2, 5, 25, 37, 43, 59, 70, 85, 89, 98, 99, 106],
    14: [0, 4, 6, 20, 35, 52, 59, 77, 78, 86, 89, 99, 122, 127],
}
GOLOMB = {m: B for m, B in GOLOMB.items() if is_sidon(B)}


def mian_chowla(m):
    B = [1]
    sums = {2}
    x = 1
    while len(B) < m:
        x += 1
        ns = {x + b for b in B} | {2 * x}
        if not (ns & sums):
            B.append(x)
            sums |= ns
    return B


def sidon_sources(m, rng):
    """A few Sidon sets of size m (as lists)."""
    out = []
    if m in GOLOMB:
        out.append(GOLOMB[m])
    out.append(mian_chowla(m))
    for p in range(3, 200):
        if is_prime(p) and p >= m:
            B = erdos_turan_sidon(p)
            idx = sorted(rng.choice(p, size=m, replace=False)) if p > m else range(p)
            out.append([B[i] for i in idx])
            if p == m or len(out) >= 4:
                break
    return out


def diff_set(B):
    return sorted({abs(u - v) for u, v in combinations(B, 2)})


def bu_set(S, shift=0):
    S = [s + shift for s in S]
    A = {3 * abs(u - v) for u, v in combinations(S, 2)} | {abs(3 * (u + v) + 1) for u, v in combinations(S, 2)}
    return sorted(A)


def fit_to(A, N, cap, rng):
    """Trim/pad a structured set to exactly N elements within [1, cap]."""
    A = [a for a in sorted(set(A)) if 1 <= a <= cap]
    if len(A) > N:
        A = sorted(rng.choice(A, size=N, replace=False).tolist())
    pool = [a for a in range(1, cap + 1) if a not in set(A)]
    if len(A) < N:
        A = sorted(A + rng.choice(pool, size=N - len(A), replace=False).tolist())
    return [int(a) for a in A]


def structured_seeds(N, cap, rng):
    seeds = []
    m = 2
    while m * (m - 1) // 2 < N:
        m += 1
    for mm in (m - 1, m, m + 1):
        if mm < 2:
            continue
        for B in sidon_sources(mm, rng):
            D = diff_set(B)
            if max(D) <= cap:
                seeds.append(("sidon_diff_m%d" % mm, fit_to(D, N, cap, rng)))
            else:  # dilation-free compression is impossible; rescale is not allowed -> skip
                pass
    k = 2
    while k * (k - 1) < N:
        k += 1
    for kk in (k - 1, k):
        if kk < 2:
            continue
        for S in sidon_sources(kk, rng)[:2]:
            span = max(S) - min(S)
            for shift in (-min(S), -min(S) - span // 2):
                A = bu_set(S, shift)
                if len(A) == kk * (kk - 1) and max(A) <= cap:
                    seeds.append(("bu_k%d_sh%d" % (kk, shift), fit_to(A, N, cap, rng)))
    return seeds


# ---------------------------------------------------------------------------
# Accurate re-evaluation
# ---------------------------------------------------------------------------

def accurate_M(A):
    e = min_estimate_fft(A, oversample=32, polish=12)
    return -e.fmin, e.xmin


def certify(A):
    c = certify_lower_bound(A)
    return -c.lower_bound  # rigorous upper bound on M(A)


# ---------------------------------------------------------------------------
# Exhaustive driver
# ---------------------------------------------------------------------------

def _exh_task(args):
    N, L, thr, prefix, H, H2 = args
    t = time.time()
    n, sets, Ms, st = exh(N, L, thr, prefix, H=H, H2=H2)
    return prefix, n, sets, Ms, st, time.time() - t


def box_upper_bound(N, L, pool, restarts=20, iters=200000, extra=()):
    """Heuristic best set in [1,L] (SA, plus any known sets in `extra` that fit in the box);
    returns (certified M upper bound, set)."""
    rng = np.random.default_rng(1000 * N + L)
    tasks = []
    for r in range(restarts):
        init = sorted(rng.choice(np.arange(1, L + 1), size=N, replace=False).tolist())
        tasks.append((N, L, init, iters, 0.3, 0.003, 7919 * r + N * 31 + L, 0.4, 3, 24, 32))
    res = pool.map(_sa_task, tasks)
    pool_sets = {tuple(r[1]) for r in res} | {tuple(sorted(A)) for A in extra if len(A) == N and max(A) <= L}
    cands = sorted(pool_sets, key=lambda A: accurate_M(A)[0])[:3]
    best = min(cands, key=certify)
    return certify(best), list(best)


def _load_exh():
    fp = os.path.join(RUN_DIR, "exhaustive.json")
    return json.load(open(fp)) if os.path.exists(fp) else {}


def run_exhaustive(plan, workers=6, log=print):
    results = {}
    with Pool(workers) as pool:
        for N, L in plan:
            t0 = time.time()
            known = []
            for fn in ("sa_best_raw.json",):
                fp = os.path.join(RUN_DIR, fn)
                if os.path.exists(fp):
                    kb = json.load(open(fp)).get(str(N))
                    if kb:
                        known.append(kb["A"])
            for k2, r2 in _load_exh().items():
                if r2.get("N") == N and "opt_A" in r2:
                    known.append(primitive(r2["opt_A"]))
            ub, A0 = box_upper_bound(N, L, pool, extra=known)
            thr = ub + 1e-9
            # prefixes (a1,a2) for load balance
            prefixes = [(a1, a2) for a1 in range(1, L - N + 2) for a2 in range(a1 + 1, L - N + 3)]
            tasks = [(N, L, thr, list(p), 4 * L, 32 * L) for p in prefixes]
            tot_nodes = tot_leaves = tot_surv = 0
            survivors = []
            overflow = False
            for prefix, n, sets, Ms, st, dt in pool.imap_unordered(_exh_task, tasks, chunksize=4):
                tot_nodes += st[0]; tot_leaves += st[1]; tot_surv += n
                if n > len(sets):
                    overflow = True
                survivors.extend(sets)
            # accurate evaluation of survivors
            evals = []
            for S in survivors:
                M, x = accurate_M(S)
                evals.append((M, x, S))
            evals.sort()
            best = evals[0] if evals else None
            rec = {"N": N, "L": L, "thr_certified_ub": ub, "seed_set": A0, "n_survivors": len(survivors),
                   "overflow": overflow, "nodes": tot_nodes, "leaves": tot_leaves,
                   "time_s": round(time.time() - t0, 1)}
            if best:
                Mb, xb, Sb = best
                cub = certify(Sb)
                # point evaluation gives rigorous-ish lower bound on M (float, error ~1e-14 N)
                ties = [list(S) for (M, x, S) in evals if M <= Mb + 1e-7]
                second = next(((M, S) for (M, x, S) in evals if M > Mb + 1e-7), None)
                rec.update({"opt_A": Sb, "opt_M_est": Mb, "opt_M_cert_ub": cub,
                            "opt_R_est": Mb / math.sqrt(N), "opt_R_cert": cub / math.sqrt(N),
                            "x_star": xb, "ties": ties[:20], "n_ties": len(ties),
                            "second_M": second[0] if second else None,
                            "second_A": second[1] if second else None})
            results[f"{N}_{L}"] = rec
            log(json.dumps({k: v for k, v in rec.items() if k not in ("ties",)}))
    return results


# ---------------------------------------------------------------------------
# SA driver
# ---------------------------------------------------------------------------

def _sa_task(args):
    (N, cap, init, iters, T0, T1, seed, pglobal, D, K, overs) = args[:11]
    t = time.time()
    best, A, cur, st = sa(N, cap, init, iters, T0=T0, T1=T1, seed=seed, pglobal=pglobal, D=D, K=K,
                          oversample=overs)
    return best, A, cur, st, time.time() - t, args


def caps_for(N):
    caps = sorted({2 * N, 3 * N, 5 * N, 8 * N, 16 * N, max(2 * N, N * N // 2), 4 * N * N})
    return [c for c in caps if c <= 8000 and c >= N + 2]


def load_best():
    if os.path.exists(OUT_JSON):
        with open(OUT_JSON) as fh:
            return json.load(fh)
    return {}


def save_best(best):
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    tmp = OUT_JSON + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(best, fh, indent=1, sort_keys=False)
    os.replace(tmp, OUT_JSON)


def perturb(A, cap, r, rng):
    A = list(A)
    s = set(A)
    for _ in range(r):
        i = int(rng.integers(len(A)))
        while True:
            b = int(rng.integers(1, cap + 1))
            if b not in s:
                break
        s.discard(A[i]); A[i] = b; s.add(b)
    return sorted(A)



def primitive(A):
    g = 0
    for a in A:
        g = math.gcd(g, int(a))
    return sorted(int(a) // g for a in A)


def _sa_eval_task(args):
    """SA run + accurate re-evaluation in the worker."""
    best, A, cur, st, dt, a = _sa_task(args)
    A = primitive(A)
    M, x = accurate_M(A)
    return {"N": a[0], "cap": a[1], "A": A, "M_grid": best, "M_est": M, "x": x, "iters": a[3],
            "T0": a[4], "T1": a[5], "seed": a[6], "time": round(dt, 2), "tag": a[11] if len(a) > 11 else ""}


def _mk(N, cap, init, iters, seed, tag, T0f=0.3, T1f=0.003, pg=0.4, D=3):
    s = math.sqrt(N)
    return (N, cap, init, int(iters), T0f * s, T1f * s, seed, pg, D, 24, 16, tag)


def sa_round1(Ns, it_per_N=3e5):
    """Broad round: random starts at several caps, structured starts (Sidon differences,
    Bu two-sided sets), and a few runs at the huge cap 4N^2 (N <= 40, multiples of 5)."""
    tasks = []
    for N in Ns:
        rng = np.random.default_rng(97 * N + 1)
        caps = sorted({math.ceil(1.25 * N) + 2, math.ceil(1.5 * N) + 1, 2 * N, 3 * N})
        iters = it_per_N * N
        for cap in caps:
            for r in range(2):
                init = sorted(rng.choice(np.arange(1, cap + 1), size=N, replace=False).tolist())
                tasks.append(_mk(N, cap, init, iters, 1000003 * N + 7919 * cap + r, f"random_cap{cap}"))
        for cap in (5 * N, 10 * N):
            ss = structured_seeds(N, cap, rng)
            # prefer one Sidon-difference and one Bu seed with the smallest R
            sd = sorted([t for t in ss if t[0].startswith("sidon")], key=lambda t: accurate_M(t[1])[0])[:1]
            bu = sorted([t for t in ss if t[0].startswith("bu")], key=lambda t: accurate_M(t[1])[0])[:1]
            for tag, A0 in sd + bu:
                tasks.append(_mk(N, cap, A0, iters, 31337 * N + cap + len(tasks), f"{tag}_cap{cap}",
                                 T0f=0.15, T1f=0.003))
        if N <= 40 and N % 5 == 0:
            cap = 4 * N * N
            ss = structured_seeds(N, cap, rng)
            sd = sorted([t for t in ss if t[0].startswith("sidon")], key=lambda t: accurate_M(t[1])[0])[:1]
            for tag, A0 in sd:
                tasks.append(_mk(N, cap, A0, iters // 2, 4243 * N, f"{tag}_cap{cap}", T0f=0.15, T1f=0.003))
            init = sorted(rng.choice(np.arange(1, cap + 1), size=N, replace=False).tolist())
            tasks.append(_mk(N, cap, init, iters // 2, 4242 * N, f"random_cap{cap}"))
    return tasks


def grow_shrink_seeds(best, N, rng):
    """Seeds for N from the best sets at N-1 (add the best single element) and N+1 (drop the
    element whose removal is best)."""
    out = []
    lo = best.get(str(N - 1))
    if lo:
        A = lo["A"]
        cand = [b for b in range(1, max(A) + max(4, N // 3)) if b not in set(A)]
        sc = sorted(((accurate_M(A + [b])[0], b) for b in cand))[:2]
        for M, b in sc:
            out.append(("grow_from_%d" % (N - 1), sorted(A + [b])))
    hi = best.get(str(N + 1))
    if hi:
        A = hi["A"]
        sc = sorted(((accurate_M([a for a in A if a != c])[0], c) for c in A))[:2]
        for M, c in sc:
            out.append(("shrink_from_%d" % (N + 1), sorted(a for a in A if a != c)))
    return out


def sa_round2(best, Ns, it_per_N=3e5, reps=6):
    tasks = []
    for N in Ns:
        rec = best.get(str(N))
        if not rec:
            continue
        A = rec["A"]
        rng = np.random.default_rng(55 * N + 3)
        cap = max(max(A) + max(3, N // 2), math.ceil(1.5 * N))
        for tag, A0 in grow_shrink_seeds(best, N, rng):
            c2 = max(cap, max(A0))
            tasks.append(_mk(N, c2, A0, it_per_N * N, 991 * N + len(tasks), f"{tag}_cap{c2}", T0f=0.1, T1f=0.002))
        for r in range(reps):
            k = int(rng.integers(2, max(3, N // 4) + 1))
            init = perturb(A, cap, k, rng)
            tasks.append(_mk(N, cap, init, it_per_N * N, 777 * N + r, f"ils_from_best_k{k}_cap{cap}",
                             T0f=0.1, T1f=0.002))
    return tasks


def run_sa_tasks(tasks, best, allres, log, workers=6, save_every=10):
    t0 = time.time()
    with Pool(workers) as pool:
        for i, r in enumerate(pool.imap_unordered(_sa_eval_task, tasks)):
            allres.append(r)
            N = str(r["N"])
            if N not in best or r["M_est"] < best[N]["est_M"] - 1e-9:
                best[N] = {"A": r["A"], "est_M": r["M_est"], "R_est": r["M_est"] / math.sqrt(r["N"]),
                           "max": max(r["A"]), "x_star": r["x"], "found_by": r["tag"], "cap": r["cap"],
                           "seed": r["seed"], "iters": r["iters"]}
                log(f"[{time.time()-t0:7.1f}s] N={N} new best R_est={best[N]['R_est']:.5f} max={best[N]['max']} "
                    f"by {r['tag']} (cap {r['cap']})")
            if i % save_every == 0:
                with open(os.path.join(RUN_DIR, "sa_best_raw.json"), "w") as fh:
                    json.dump(best, fh, indent=1)
                with open(os.path.join(RUN_DIR, "sa_all_runs.json"), "w") as fh:
                    json.dump(allres, fh)
    with open(os.path.join(RUN_DIR, "sa_best_raw.json"), "w") as fh:
        json.dump(best, fh, indent=1)
    with open(os.path.join(RUN_DIR, "sa_all_runs.json"), "w") as fh:
        json.dump(allres, fh)


def sa_round3(best, Ns, it_per_N=6e5, reps=4):
    """Deeper ILS for N >= 20: perturbations of best(N), plus best sets of neighbouring
    N (within the list) adapted greedily to size N."""
    tasks = []
    keys = sorted(int(k) for k in best)
    for N in Ns:
        if N < 20 or str(N) not in best:
            continue
        rng = np.random.default_rng(313 * N + 9)
        A = best[str(N)]["A"]
        cap = max(max(A) + max(3, N // 3), math.ceil(1.5 * N))
        for r in range(reps):
            k = int(rng.integers(2, max(3, N // 5) + 1))
            tasks.append(_mk(N, cap, perturb(A, cap, k, rng), it_per_N * N, 5557 * N + r,
                             f"r3_ils_k{k}_cap{cap}", T0f=0.12, T1f=0.002))
        nbrs = sorted((abs(M - N), M) for M in keys if M != N and abs(M - N) <= max(5, N // 8))[:2]
        for _, M in nbrs:
            A0 = adapt_size(best[str(M)]["A"], N)
            c2 = max(cap, max(A0) + 3)
            tasks.append(_mk(N, c2, A0, it_per_N * N, 6661 * N + M, f"r3_adapt_from_{M}_cap{c2}",
                             T0f=0.12, T1f=0.002))
    return tasks


def growth_chain(args):
    """Greedy growth chain: from a good set A0, repeatedly add the single element (in
    [1, max+slack]) minimizing accurate M, then polish with a cold SA run; record the best
    set at every size up to Nmax.  UNCERTIFIED heuristic."""
    A0, Nmax, seed, it_per_N, slack_f = args
    rng = np.random.default_rng(seed)
    A = sorted(A0)
    out = {}
    while len(A) < Nmax:
        N = len(A) + 1
        s = set(A)
        slack = max(4, int(slack_f * N))
        cand = [b for b in range(1, max(A) + slack) if b not in s]
        _, b = min((accurate_M(A + [b])[0], b) for b in cand)
        A = sorted(A + [b])
        cap = max(A) + max(3, N // 4)
        sq = math.sqrt(N)
        best, B, cur, st = sa(N, cap, A, int(it_per_N * N), T0=0.03 * sq, T1=0.001 * sq,
                              seed=int(rng.integers(1 << 62)), pglobal=0.3, D=3)
        B = primitive(B)
        MB, xB = accurate_M(B)
        MA, xA = accurate_M(A)
        if MB < MA:
            A = sorted(B) if len(set(B)) == N else A
            MA, xA = MB, xB
        out[N] = (MA, list(A), xA)
    return seed, out


def adapt_size(A, N, slack=None):
    """Greedily add/remove single elements (best accurate_M at each step) until |A| = N."""
    A = sorted(set(A))
    slack = slack if slack is not None else max(4, N // 3)
    while len(A) < N:
        s = set(A)
        cand = [b for b in range(1, max(A) + slack) if b not in s]
        _, b = min((accurate_M(A + [b])[0], b) for b in cand)
        A = sorted(A + [b])
    while len(A) > N:
        _, c = min((accurate_M([a for a in A if a != c])[0], c) for c in A)
        A = [a for a in A if a != c]
    return A


def lead_seeds(Ns, maxdiff=None):
    """Seeds from the lead's dense free-N runs (examples/dense_runs/X*_s*.json, key "A")."""
    import glob
    files = sorted(glob.glob(os.path.join(ROOT, "examples", "dense_runs", "X*_s*.json")))
    sets = []
    for f in files:
        try:
            sets.append((os.path.basename(f), sorted(json.load(open(f))["A"])))
        except Exception:
            pass
    out = []
    for N in Ns:
        for name, A in sets:
            if abs(len(A) - N) <= (maxdiff or max(8, N // 7)):
                out.append((N, "lead_" + name.replace(".json", "") + f"_adapt{len(A)}to{N}", adapt_size(A, N)))
    return out


def _task_key(a):
    return (int(a[0]), int(a[1]), int(a[6]), str(a[11]))


def main_sa(argv):
    os.makedirs(RUN_DIR, exist_ok=True)
    stage = argv[0] if argv else "r1"
    Ns = [int(t) for t in argv[1].split(",")] if len(argv) > 1 else list(range(4, 41)) + [45, 50, 55, 60, 70, 80, 90, 100]
    log = _log_to(os.path.join(RUN_DIR, "sa.log"))
    bp = os.path.join(RUN_DIR, "sa_best_raw.json")
    best = json.load(open(bp)) if os.path.exists(bp) else {}
    ap = os.path.join(RUN_DIR, "sa_all_runs.json")
    allres = json.load(open(ap)) if os.path.exists(ap) else []
    _lib()
    for k2, r2 in _load_exh().items():   # merge exhaustive box optima
        if "opt_A" in r2:
            A2 = primitive(r2["opt_A"])
            M2, x2 = accurate_M(A2)
            n2 = str(len(A2))
            if n2 not in best or M2 < best[n2]["est_M"] - 1e-9:
                best[n2] = {"A": A2, "est_M": M2, "R_est": M2 / math.sqrt(len(A2)), "max": max(A2), "x_star": x2,
                            "found_by": f"exhaustive box [1,{r2['L']}]", "cap": r2["L"], "seed": None, "iters": 0}
    if stage == "r1":
        tasks = sa_round1(Ns)
    elif stage == "r2":
        tasks = sa_round2(best, Ns, reps=3, it_per_N=1.5e5)
        for N, tag, A0 in lead_seeds(Ns):
            cap = max(max(A0) + max(3, N // 4), math.ceil(1.5 * N))
            tasks.append(_mk(N, cap, A0, 2e5 * N, 4447 * N + len(tasks), tag + f"_cap{cap}", T0f=0.1, T1f=0.002))
            A1 = sorted(A0)
            # also accurately record the adapted seed itself as a candidate
            M, x = accurate_M(A1)
            if str(N) not in best or M < best[str(N)]["est_M"] - 1e-9:
                best[str(N)] = {"A": A1, "est_M": M, "R_est": M / math.sqrt(N), "max": max(A1), "x_star": x,
                                "found_by": tag + " (seed itself)", "cap": max(A1), "seed": None, "iters": 0}
    elif stage == "chain":
        starts = []
        for n0 in (30, 32, 34, 35, 36):
            if str(n0) in best:
                starts.append(best[str(n0)]["A"])
        jobs = []
        for i, A0 in enumerate(starts):
            jobs.append((A0, 100, 8000 + i, 1e5, 0.3))
        jobs.append((best["36"]["A"], 100, 8100, 2e5, 0.5))
        with Pool(6) as pool:
            for seedv, res in pool.imap_unordered(growth_chain, jobs):
                for N, (M, A, x) in res.items():
                    allres.append({"N": N, "cap": max(A), "A": A, "M_grid": None, "M_est": M, "x": x,
                                   "iters": 0, "T0": None, "T1": None, "seed": seedv, "time": 0,
                                   "tag": f"growth_chain_seed{seedv}"})
                    if str(N) not in best or M < best[str(N)]["est_M"] - 1e-9:
                        best[str(N)] = {"A": A, "est_M": M, "R_est": M / math.sqrt(N), "max": max(A), "x_star": x,
                                        "found_by": f"growth_chain_seed{seedv} (greedy add + cold SA polish)",
                                        "cap": max(A), "seed": seedv, "iters": -1}
                        log(f"chain {seedv}: N={N} new best R_est={M/math.sqrt(N):.5f} max={max(A)}")
        with open(os.path.join(RUN_DIR, "sa_best_raw.json"), "w") as fh:
            json.dump(best, fh, indent=1)
        with open(os.path.join(RUN_DIR, "sa_all_runs.json"), "w") as fh:
            json.dump(allres, fh)
        return
    elif stage == "r3":
        tasks = sa_round3(best, Ns, it_per_N=3e5, reps=3)
    else:
        raise SystemExit("stage r1|r2|r3")
    done = {(r["N"], r["cap"], r["seed"], r["tag"]) for r in allres}
    n0 = len(tasks)
    tasks = [a for a in tasks if _task_key(a) not in done]
    log(f"skipping {n0 - len(tasks)} already-completed tasks")
    # big tasks first for load balance
    tasks.sort(key=lambda a: -a[3] * math.log2(16 * a[1]) * (1 + a[1] / 2000))
    log(f"stage {stage}: {len(tasks)} tasks for N in {Ns[0]}..{Ns[-1]}")
    run_sa_tasks(tasks, best, allres, log)



# ---------------------------------------------------------------------------
# Structural analysis
# ---------------------------------------------------------------------------

def additive_energy(A):
    """E(A) = #{(a,b,c,d) in A^4 : a+b = c+d} (ordered)."""
    v = np.zeros(max(A) + 1)
    v[list(A)] = 1
    r = np.convolve(v, v)
    return int(round(float((r * r).sum())))


def triples(A):
    """T3 = #{(a,b) in A^2 ordered, a=b allowed : a+b in A}."""
    s = set(A)
    return sum(1 for a in A for b in A if a + b in s)


def max_clique_diff(A):
    """Largest B containing 0 with all pairwise |u-v| in A (vertices {0} u A).
    Returns (omega, B, coverage = #distinct differences of B / |A|)."""
    s = set(A)
    V = [0] + sorted(A)
    nb = {u: {v for v in V if v != u and abs(u - v) in s} for u in V}
    best = [0]

    def bk(R, P, X):
        if not P and not X:
            if len(R) > len(best):
                best[:] = R
            return
        if len(R) + len(P) <= len(best):
            return
        u = max(P | X, key=lambda w: len(nb[w] & P))
        for v in list(P - nb[u]):
            bk(R + [v], P & nb[v], X & nb[v])
            P = P - {v}
            X = X | {v}

    bk([0], set(nb[0]), set())
    B = sorted(best)
    dif = {abs(u - v) for u, v in combinations(B, 2)}
    return len(B), B, len(dif) / len(A)


def sidon_clique(A, node_limit=100000):
    """Largest Sidon B (containing 0, WLOG min B = 0) with every positive difference of B in A.
    coverage = C(|B|,2)/|A| (= 1 iff A is exactly the Sidon difference set (B-B)^+).
    Returns (m, B, coverage, complete_flag)."""
    s = set(A)
    V = sorted(A)
    mmax = int((1 + math.isqrt(1 + 8 * len(A))) // 2)
    best = [[0]]
    nodes = [0]

    def rec(B, used, cand):
        nodes[0] += 1
        if len(B) > len(best[0]):
            best[0] = list(B)
        if len(best[0]) >= mmax or nodes[0] > node_limit:
            return
        if len(B) + len(cand) <= len(best[0]):
            return
        for i, v in enumerate(cand):
            if len(B) + len(cand) - i <= len(best[0]):
                return
            nd = [v - b for b in B]
            if all(d in s for d in nd) and not (set(nd) & used) and len(set(nd)) == len(nd):
                rec(B + [v], used | set(nd), cand[i + 1:])
                if len(best[0]) >= mmax or nodes[0] > node_limit:
                    return

    rec([0], set(), V)
    B = best[0]
    return len(B), B, (len(B) * (len(B) - 1) // 2) / len(A), nodes[0] <= node_limit


def diff_multiplicity(A):
    """Max multiplicity of a positive difference in A-A and fraction of distinct differences."""
    D = {}
    for u, v in combinations(sorted(A), 2):
        D[v - u] = D.get(v - u, 0) + 1
    n = len(A)
    return max(D.values()), len(D) / (n * (n - 1) / 2)


def local_minima(A, over=64, rel=0.01):
    """Local minima of f_A on [0, pi] (fine FFT grid + Newton), those within rel of global min."""
    from chowla import _newton_polish, grid_values_fft
    L = 1 << max(12, math.ceil(math.log2(over * max(A) + 1)))
    g = grid_values_fft(A, L)[: L // 2 + 1]
    idx = [j for j in range(1, L // 2) if g[j] <= g[j - 1] and g[j] <= g[j + 1]]
    if g[0] <= g[1]:
        idx.append(0)
    if g[L // 2] <= g[L // 2 - 1]:
        idx.append(L // 2)
    mins = []
    for j in idx:
        x, v = _newton_polish(A, 2 * math.pi * j / L)
        if g[j] < v:
            x, v = 2 * math.pi * j / L, g[j]
        x = x % (2 * math.pi)
        if x > math.pi:
            x = 2 * math.pi - x
        mins.append((v, x))
    mins.sort()
    gm = mins[0][0]
    close = [(v, x) for v, x in mins if v <= gm * (1 - rel)]
    return gm, mins, close


def small_rational(t, qmax=24, tol=2e-3):
    from fractions import Fraction
    fr = Fraction(t).limit_denominator(qmax)
    return f"{fr.numerator}/{fr.denominator}" if abs(float(fr) - t) < tol else None


def profile(A, bins=4):
    m = max(A)
    edges = np.linspace(0, m, bins + 1)
    out = []
    for i in range(bins):
        lo, hi = edges[i], edges[i + 1]
        cnt = sum(1 for a in A if lo < a <= hi)
        out.append(round(cnt / max(1e-9, hi - lo), 3))
    return out


def initial_run(A):
    s = set(A)
    k = 0
    while k + 1 in s:
        k += 1
    return k


def structure(A):
    A = sorted(A)
    N = len(A)
    gm, mins, close = local_minima(A)
    close5 = [m for m in mins if m[0] <= gm * 0.95]
    om, B, cov = max_clique_diff(A)
    sm, SB, scov, scomplete = sidon_clique(A)
    mm, frac = diff_multiplicity(A)
    xs = mins[0][1] / (2 * math.pi)
    return {
        "N": N, "max": A[-1], "max_over_N": round(A[-1] / N, 3), "E_over_N2": round(additive_energy(A) / N ** 2, 3),
        "E_over_N3": round(additive_energy(A) / N ** 3, 4), "T3": triples(A), "T3_over_N2": round(triples(A) / N ** 2, 3),
        "initial_run": initial_run(A), "density_profile": profile(A), "frac_odd": round(sum(a % 2 for a in A) / N, 3),
        "res_mod3": [sum(1 for a in A if a % 3 == r) for r in range(3)],
        "x_star_over_2pi": round(xs, 6), "x_star_rational": small_rational(xs),
        "n_minima_within_1pct": len(close), "n_minima_within_5pct": len(close5),
        "minima_within_1pct_x_over_2pi": [round(x / (2 * math.pi), 5) for v, x in close][:12],
        "clique_omega": om, "clique_B": B, "clique_coverage": round(cov, 3),
        "sidon_clique_m": sm, "sidon_clique_B": SB, "sidon_coverage": round(scov, 3), "sidon_search_complete": scomplete,
        "max_diff_mult": mm, "frac_distinct_diffs": round(frac, 3),
    }


def comparison_sets():
    out = []
    for m, B in sorted(GOLOMB.items()):
        if m >= 3:
            A = diff_set(B)
            out.append(("golomb_diff_m%d" % m, A))
    for p in (5, 7, 11, 13):
        A = diff_set(erdos_turan_sidon(p))
        out.append(("ET_diff_p%d" % p, A))
    for k in range(3, 11):
        S = GOLOMB[k]
        bestA, bestM = None, None
        span = max(S)
        for sh in range(-span - 1, 1):
            A = bu_set(S, sh)
            if len(A) != k * (k - 1):
                continue
            M = accurate_M(A)[0]
            if bestM is None or M < bestM:
                bestA, bestM = A, M
        out.append(("bu_golomb_k%d_bestshift" % k, bestA))
    return out


def _cert_task(A):
    c = certify_lower_bound(A)
    return c.lower_bound, c.L


def main_analyze(argv):
    bp = os.path.join(RUN_DIR, "sa_best_raw.json")
    sab = json.load(open(bp)) if os.path.exists(bp) else {}
    ep = os.path.join(RUN_DIR, "exhaustive.json")
    exr = json.load(open(ep)) if os.path.exists(ep) else {}
    allp = os.path.join(RUN_DIR, "sa_all_runs.json")
    allr = json.load(open(allp)) if os.path.exists(allp) else []
    # exhaustive summary per N (largest box)
    ex_by_N = {}
    for k, r in exr.items():
        N = r["N"]
        if "opt_A" in r and (N not in ex_by_N or r["L"] > ex_by_N[N]["L"]):
            ex_by_N[N] = r
    Ns = sorted({int(n) for n in sab} | set(ex_by_N))
    cands = {}
    for N in Ns:
        c = []
        if str(N) in sab:
            r = sab[str(N)]
            if str(r["found_by"]).startswith("exhaustive"):
                lab = f"{r['found_by']} (complete enumeration)"
            elif r.get("iters", 0) == -1:
                lab = f"{r['found_by']}"
            elif r.get("iters", 0) == 0:
                lab = f"seed set {r['found_by']}"
            else:
                lab = f"SA ({r['found_by']}, cap {r['cap']}, seed {r['seed']}, iters {r['iters']}, grid G>=16*cap)"
            c.append((r["est_M"], primitive(r["A"]), lab))
        if N in ex_by_N:
            r = ex_by_N[N]
            A = primitive(r["opt_A"])
            c.append((accurate_M(A)[0], A, f"exhaustive optimum over all N-subsets of [1,{r['L']}]"))
        c.sort(key=lambda t: t[0])
        cands[N] = c
    with Pool(6) as pool:
        certs = pool.map(_cert_task, [cands[N][0][1] for N in Ns])
    out = {}
    for N, (lb, Lg) in zip(Ns, certs):
        M, A, how = cands[N][0]
        # cap-wise best R (SA, uncertified) for the description
        bycap = {}
        for r in allr:
            if r["N"] == N:
                bycap[r["cap"]] = min(bycap.get(r["cap"], 9e9), r["M_est"] / math.sqrt(N))
        desc = how
        if N in ex_by_N:
            desc += f"; box [1,{ex_by_N[N]['L']}] exhaustive optimum R={ex_by_N[N]['opt_R_est']:.5f}"
        if bycap:
            desc += "; SA best R by cap: " + ", ".join(f"{c}:{v:.4f}" for c, v in sorted(bycap.items()))
        out[str(N)] = {"A": A, "est_min": -M, "cert_lower": lb, "R_est": M / math.sqrt(N),
                       "R_cert": -lb / math.sqrt(N), "max": max(A), "search": desc, "cert_grid_L": Lg}
        if max(A) <= 64:
            # exact PARI Sturm bracket: f_A >= -Bup on [0,2pi] proved; f_A >= -Blo fails (sign change)
            from chowla import sturm_certify
            Bup = math.ceil(M * 1e7) + 1
            Blo = math.floor(M * 1e7) - 1
            try:
                ok_up, _ = sturm_certify(A, Bup, 10 ** 7)
                ok_lo, n_lo = sturm_certify(A, Blo, 10 ** 7)
                if ok_up and not ok_lo:
                    out[str(N)]["sturm_M_bracket"] = [Blo / 1e7, Bup / 1e7]
            except Exception as ex:  # pragma: no cover
                out[str(N)]["sturm_error"] = str(ex)
    save_best(out)
    # structure
    rows = []
    for N in Ns:
        st = structure(out[str(N)]["A"])
        st["R_est"] = round(out[str(N)]["R_est"], 5)
        st["R_cert"] = round(out[str(N)]["R_cert"], 5)
        rows.append(st)
    comp = []
    for tag, A in comparison_sets():
        M, x = accurate_M(A)
        n = len(A)
        sm, SB, scov, _ = sidon_clique(A)
        comp.append({"tag": tag, "N": n, "max": max(A), "R_est": round(M / math.sqrt(n), 5), "sidon_coverage": round(scov, 3),
                     "E_over_N2": round(additive_energy(A) / n ** 2, 3), "T3_over_N2": round(triples(A) / n ** 2, 3),
                     "x_star_over_2pi": round(x / (2 * math.pi), 5)})
    # trend fits
    fits = {}
    for lo, hi in ((10, 36), (10, 100), (20, 36)):
        NN = np.array([r["N"] for r in rows if lo <= r["N"] <= hi], float)
        RR = np.array([r["R_cert"] for r in rows if lo <= r["N"] <= hi], float)
        if len(NN) < 4:
            continue
        X = np.vstack([np.ones_like(NN), 1 / np.sqrt(NN)]).T
        coef, *_ = np.linalg.lstsq(X, RR, rcond=None)
        X2 = np.vstack([np.ones_like(NN), np.log(NN)]).T
        c2, *_ = np.linalg.lstsq(X2, np.log(RR), rcond=None)
        c3, *_ = np.linalg.lstsq(X2, RR, rcond=None)
        fits[f"N{lo}-{hi}"] = {"R=a+b/sqrtN": [float(c) for c in coef],
                               "R=C*N^gamma": [float(math.exp(c2[0])), float(c2[1])],
                               "R=a+b*logN": [float(c) for c in c3]}
    fits["window_min_R_cert"] = {f"{lo}-{hi}": float(min((r["R_cert"] for r in rows if lo <= r["N"] <= hi), default=float('nan')))
                                 for lo, hi in ((4, 10), (11, 20), (21, 30), (31, 40), (41, 60), (61, 100))}
    with open(os.path.join(RUN_DIR, "analysis.json"), "w") as fh:
        json.dump({"rows": rows, "comparison": comp, "fits": fits}, fh, indent=1)
    keys = ["N", "R_est", "R_cert", "max", "max_over_N", "E_over_N2", "E_over_N3", "T3_over_N2", "initial_run",
            "density_profile", "x_star_over_2pi", "x_star_rational", "n_minima_within_1pct", "n_minima_within_5pct",
            "clique_omega", "clique_coverage", "sidon_clique_m", "sidon_coverage", "max_diff_mult", "frac_distinct_diffs", "frac_odd"]
    for r in rows:
        print(" ".join(f"{k}={r[k]}" for k in keys))
    for c in comp:
        print(c)
    print(json.dumps(fits, indent=1))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _log_to(path):
    def log(msg):
        print(msg, flush=True)
        with open(path, "a") as fh:
            fh.write(msg + "\n")
    return log


def main_exhaustive(argv):
    os.makedirs(RUN_DIR, exist_ok=True)
    plan = []
    for tok in argv:
        N, L = tok.split(":")
        plan.append((int(N), int(L)))
    if not plan:
        plan = [(4, 40), (5, 40), (6, 40), (7, 40), (8, 40)]
    log = _log_to(os.path.join(RUN_DIR, "exhaustive.log"))
    res = run_exhaustive(plan, workers=int(os.environ.get('CHOWLA_WORKERS', '6')), log=log)  # localrun.sh sets 4
    path = os.path.join(RUN_DIR, "exhaustive.json")
    old = {}
    if os.path.exists(path):
        with open(path) as fh:
            old = json.load(fh)
    old.update(res)
    with open(path, "w") as fh:
        json.dump(old, fh, indent=1)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "exhaustive":
        main_exhaustive(sys.argv[2:])
    elif cmd == "sa":
        main_sa(sys.argv[2:])
    elif cmd == "analyze":
        main_analyze(sys.argv[2:])
    else:
        print(__doc__)
