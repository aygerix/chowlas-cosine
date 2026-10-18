/* wlns.c -- large-neighbourhood search with EXACT window branch-and-bound (agent "construct", 2026-10-18).
 * A subset [1,X], |A| = N fixed, minimise M(A) = -min_x f_A(x).  Each step frees a window W subset [1,X] (|W| = w),
 * keeps A \ W, and enumerates ALL ways to put k = |A cap W| elements into W by DFS with the valid grid prune
 *     exists j: g(x_j) + U_j(k_left, i) < -thr   (U = sum of the k_left largest cos(a x_j) over remaining window positions),
 * threshold = current true M minus 1e-9 (strict improvement), lowered as better completions are found (window optimum).
 * Leaves are evaluated by Newton polishing (float, UNCERTIFIED; certify final sets separately with arb).
 * Window types: 0 random positions, 1 contiguous block, 2 upper part (>= 0.5X) + random core positions,
 *               3 dip-responsible positions (members with cos < 0 / non-members with cos > 0 at the deepest dips).
 * ILS: after `pat` windows without improvement, restart from the best set with r random swaps.
 * usage: wlns X N G seed tlimit initfile w [nodelimit] [pat]
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct { uint64_t s[4]; } rng_t;
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t rnext(rng_t *r) { uint64_t *s = r->s; const uint64_t res = rotl(s[1] * 5, 7) * 9; const uint64_t t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3]; s[2] ^= t; s[3] = rotl(s[3], 45); return res; }
static void rseed(rng_t *r, uint64_t seed) { for (int i = 0; i < 4; i++) { seed += 0x9E3779B97F4A7C15ULL; uint64_t z = seed;
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; r->s[i] = z ^ (z >> 31); } }
static inline double runif(rng_t *r) { return (rnext(r) >> 11) * 0x1.0p-53; }
static inline int rint_(rng_t *r, int n) { return (int)(runif(r) * (double)n); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

static int X, N, G, GP, w;
static double *C;                 /* C[a*GP+j] = cos(pi a j/G) */
static double *Ub, *lev;          /* U[(k*(w+1)+i)*GP + j] for window positions */
static int Wp[256];               /* window positions sorted */
static int fixedA[4096], nfixed, curW[256], ncurW, bestW[256], nbestW;
static double thr;
static long long nodes, nodelimit;
static int hint[256];

static double true_min_set(const int *A, int na, const double *g) {
    double gmin = 1e300; for (int j = 0; j < GP; j++) if (g[j] < gmin) gmin = g[j];
    double best = gmin;
    for (int j = 0; j < GP; j++) {
        double l = j ? g[j - 1] : g[1], r = j < G ? g[j + 1] : g[G - 1];
        if (g[j] > l || g[j] > r || g[j] > gmin + 0.3) continue;
        double x = M_PI * j / G;
        for (int it = 0; it < 40; it++) { double d1 = 0, d2 = 0;
            for (int q = 0; q < na; q++) { double a = A[q]; d1 -= a * sin(a * x); d2 -= a * a * cos(a * x); }
            if (d2 <= 0) break; double st = d1 / d2; x -= st; if (fabs(st) < 1e-14) break; }
        double v = 0; for (int q = 0; q < na; q++) v += cos(A[q] * x);
        if (v < best) best = v;
    }
    return best;
}

static void leaf(const double *g) {
    int A[4096], na = 0;
    for (int q = 0; q < nfixed; q++) A[na++] = fixedA[q];
    for (int q = 0; q < ncurW; q++) A[na++] = Wp[curW[q]];
    double tm = true_min_set(A, na, g);
    if (-tm < thr) { thr = -tm; nbestW = ncurW; memcpy(bestW, curW, sizeof(int) * ncurW); }
}

static void dfs(int depth, int k, int i) {
    const double *gS = lev + (size_t)depth * GP; double *ng = lev + (size_t)(depth + 1) * GP;
    for (int p = i; p <= w - k; p++) {
        if (nodes > nodelimit) return;
        const double *Ca = C + (size_t)Wp[p] * GP, *Up = Ub + ((size_t)(k - 1) * (w + 1) + (p + 1)) * GP;
        double nthr = -thr; nodes++;
        int h = hint[depth], pr = 0;
        if (gS[h] + Ca[h] + Up[h] < nthr) pr = 1;
        else for (int j = 0; j < GP; j++) { double v = gS[j] + Ca[j]; ng[j] = v; if (v + Up[j] < nthr) { pr = 1; hint[depth] = j; break; } }
        if (pr) continue;
        curW[ncurW++] = p;
        if (k == 1) leaf(ng); else dfs(depth + 1, k - 1, p + 1);
        ncurW--;
    }
}

static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }

int main(int argc, char **argv) {
    if (argc < 8) { fprintf(stderr, "usage: wlns X N G seed tlimit initfile w [nodelimit] [pat]\n"); return 2; }
    X = atoi(argv[1]); N = atoi(argv[2]); G = atoi(argv[3]); uint64_t seed = strtoull(argv[4], 0, 10); double tl = atof(argv[5]);
    w = atoi(argv[7]); nodelimit = argc > 8 ? atoll(argv[8]) : 20000000LL; int pat = argc > 9 ? atoi(argv[9]) : 300;
    if (G <= 0) G = 8 * X; GP = G + 1;
    rng_t rng; rseed(&rng, seed);
    C = malloc(sizeof(double) * (size_t)(X + 1) * GP);
    for (int a = 0; a <= X; a++) for (int j = 0; j < GP; j++) C[(size_t)a * GP + j] = cos(M_PI * (double)((long)a * j % (2L * G)) / G);
    char *inA = calloc(X + 2, 1), *bestA = calloc(X + 2, 1); int cnt = 0;
    FILE *fp = fopen(argv[6], "r"); int v;
    while (fp && fscanf(fp, "%d", &v) == 1) if (v >= 1 && v <= X && !inA[v] && cnt < N) { inA[v] = 1; cnt++; }
    if (fp) fclose(fp);
    while (cnt < N) { int a = 1 + rint_(&rng, X); if (!inA[a]) { inA[a] = 1; cnt++; } }
    double *g = calloc(GP, sizeof(double));
    int Acur[4096];
    #define REBUILD() do { memset(g, 0, sizeof(double) * GP); int _n = 0; for (int a = 1; a <= X; a++) if (inA[a]) { Acur[_n++] = a; \
        const double *Ca = C + (size_t)a * GP; for (int j = 0; j < GP; j++) g[j] += Ca[j]; } } while (0)
    REBUILD();
    double curM = -true_min_set(Acur, N, g), bestM = curM; memcpy(bestA, inA, X + 2);
    printf("START M=%.7f R=%.7f\n", curM, curM / sqrt(N)); fflush(stdout);
    Ub = malloc(sizeof(double) * (size_t)(w + 2) * (w + 1) * GP); lev = malloc(sizeof(double) * (size_t)(w + 2) * GP);
    double *vals = malloc(sizeof(double) * (w + 1));
    double t0 = now(); long it = 0, lastimp = 0; long long totnodes = 0;
    while (now() - t0 < tl) {
        it++;
        /* --- choose window --- */
        int type = rint_(&rng, 4), nw = 0; char *inW = calloc(X + 2, 1);
        if (type == 1) { int s = 1 + rint_(&rng, X - w + 1); for (int a = s; a < s + w && a <= X; a++) { inW[a] = 1; nw++; } }
        else if (type == 2) { int lo = X / 2; int cap = X - lo; int take = w * 3 / 4 < cap ? w * 3 / 4 : cap;
            while (nw < take) { int a = lo + 1 + rint_(&rng, cap); if (!inW[a]) { inW[a] = 1; nw++; } } }
        else if (type == 3) {
            /* deepest grid local minima (up to 6), score s_a = sum_dips cos(a x) ; members with low s, non-members with high s */
            int dips[6], nd = 0; double dv[6];
            for (int j = 1; j < G; j++) if (g[j] <= g[j - 1] && g[j] <= g[j + 1]) {
                if (nd < 6) { dips[nd] = j; dv[nd] = g[j]; nd++; }
                else { int mx = 0; for (int q = 1; q < 6; q++) if (dv[q] > dv[mx]) mx = q; if (g[j] < dv[mx]) { dips[mx] = j; dv[mx] = g[j]; } } }
            double *sc = malloc(sizeof(double) * (X + 2));
            for (int a = 1; a <= X; a++) { double s = 0; for (int q = 0; q < nd; q++) s += C[(size_t)a * GP + dips[q]];
                sc[a] = (inA[a] ? -s : s) + 0.6 * runif(&rng); }
            for (int q = 0; q < w / 2; q++) { int bi = -1; for (int a = 1; a <= X; a++) if (!inW[a] && (bi < 0 || sc[a] > sc[bi])) bi = a; inW[bi] = 1; nw++; }
            free(sc);
        }
        while (nw < w) { int a = 1 + rint_(&rng, X); if (!inW[a]) { inW[a] = 1; nw++; } }
        int k = 0; nfixed = 0; int np = 0;
        for (int a = 1; a <= X; a++) { if (inW[a]) { Wp[np++] = a; if (inA[a]) k++; } else if (inA[a]) fixedA[nfixed++] = a; }
        free(inW);
        if (k == 0 || k == w) continue;
        /* --- base sums and U table --- */
        double *g0 = lev; memcpy(g0, g, sizeof(double) * GP);
        for (int q = 0; q < np; q++) if (inA[Wp[q]]) { const double *Ca = C + (size_t)Wp[q] * GP; for (int j = 0; j < GP; j++) g0[j] -= Ca[j]; }
        for (int j = 0; j < GP; j++) {
            int cntv = 0;
            for (int i = w; i >= 0; i--) {
                if (i < w) { double val = C[(size_t)Wp[i] * GP + j]; int b = cntv - 1; while (b >= 0 && vals[b] < val) { vals[b + 1] = vals[b]; b--; } vals[b + 1] = val; cntv++; }
                double s = 0;
                for (int kk = 0; kk <= k; kk++) { if (kk > 0) s += (kk <= cntv) ? vals[kk - 1] : -1e9; Ub[((size_t)kk * (w + 1) + i) * GP + j] = s; }
            }
        }
        thr = curM - 1e-9; nbestW = -1; nodes = 0; ncurW = 0;
        memset(hint, 0, sizeof(hint));
        dfs(0, k, 0);
        totnodes += nodes;
        if (nbestW >= 0) {
            for (int q = 0; q < np; q++) inA[Wp[q]] = 0;
            for (int q = 0; q < nbestW; q++) inA[Wp[bestW[q]]] = 1;
            REBUILD();
            curM = -true_min_set(Acur, N, g); lastimp = it;
            if (curM < bestM - 1e-9) {
                bestM = curM; memcpy(bestA, inA, X + 2);
                printf("BEST M=%.7f R=%.7f it=%ld type=%d t=%.1f A=", curM, curM / sqrt(N), it, type, now() - t0);
                for (int a = 1; a <= X; a++) if (inA[a]) printf("%d ", a); printf("\n"); fflush(stdout);
            }
        }
        if (it - lastimp > pat) {   /* ILS perturbation from the best */
            memcpy(inA, bestA, X + 2);
            int r = 2 + rint_(&rng, 2 + N / 15);
            for (int q = 0; q < r; q++) { int a, b; do a = 1 + rint_(&rng, X); while (!inA[a]); do b = 1 + rint_(&rng, X); while (inA[b]); inA[a] = 0; inA[b] = 1; }
            REBUILD(); curM = -true_min_set(Acur, N, g); lastimp = it;
        }
    }
    printf("FINAL M=%.7f R=%.7f it=%ld nodes=%lld t=%.1f X=%d N=%d w=%d seed=%llu A=", bestM, bestM / sqrt(N), it, totnodes, now() - t0, X, N, w,
           (unsigned long long)seed);
    for (int a = 1; a <= X; a++) if (bestA[a]) printf("%d ", a); printf("\n");
    return 0;
}
