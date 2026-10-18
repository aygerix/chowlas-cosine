
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
