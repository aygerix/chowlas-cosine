/* dsearch.c -- iterated tabu search for dense Chowla sets (agent "construct", 2026-10-18).
 *
 * Problem: A subset of [1,X], |A| = N fixed; minimise M(A) = -min_x sum_{a in A} cos(a x).
 * Objective on the grid x_j = pi j / G, j = 0..G (f even, 2pi-periodic, so [0,pi] suffices).
 * Grid M is an UNDER-estimate of the true M (every grid value >= min f); final sets are re-evaluated with Newton
 * polishing and certified separately with arb ball arithmetic (src/chowla.py).  Nothing printed here is certified.
 *
 * Search: tabu search over swaps (a in A) <-> (b not in A).  Guidance objective = soft-max
 *     Phi = U + (1/beta) log sum_j exp(beta (u_j - U)),   u_j = -f(x_j),  U = max_j u_j  (= grid M),
 * candidate moves from the first-order change dPhi ~ g_a - g_b, g_n = sum_j p_j cos(n x_j) (p = soft-max weights),
 * plus shift moves a -> a +- 1, +-2 and random swaps; every candidate is evaluated exactly on the grid.
 * Iterated: on stagnation restart from an elite solution with a random perturbation.
 *
 * usage: dsearch X N G iters seed beta mode [initfile|corefrac] [time_limit_s]
 *   mode 0 random | 1 core+tail (corefrac = fraction of [1,X] used as core, default 0.62) | 2 arch profile | 3 file
 * output (stdout): one line per new global best ("BEST U R t A=...") and a final line "FINAL ...".
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct { uint64_t s[4]; } rng_t;
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t rnext(rng_t *r) {
    uint64_t *s = r->s; const uint64_t res = rotl(s[1] * 5, 7) * 9; const uint64_t t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3]; s[2] ^= t; s[3] = rotl(s[3], 45); return res;
}
static void rseed(rng_t *r, uint64_t seed) {
    for (int i = 0; i < 4; i++) { seed += 0x9E3779B97F4A7C15ULL; uint64_t z = seed;
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; r->s[i] = z ^ (z >> 31); }
}
static inline double runif(rng_t *r) { return (rnext(r) >> 11) * 0x1.0p-53; }
static inline int rint_(rng_t *r, int n) { return (int)(runif(r) * (double)n); }

static int X, N, G, GP;            /* GP = G+1 grid points */
static float *T;                   /* T[n*GP + j] = cos(n pi j / G), n = 0..X */
static float *f, *tmp;
static double beta;
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

/* exact grid evaluation of the swap a -> b (a = 0 or b = 0 means no removal / no addition): returns Phi, sets *U */
static double eval_swap(int a, int b, double *Uout) {
    const float *Ta = T + (size_t)a * GP, *Tb = T + (size_t)b * GP;
    float mn = 1e30f;
    if (a && b) { for (int j = 0; j < GP; j++) { float v = f[j] - Ta[j] + Tb[j]; tmp[j] = v; mn = v < mn ? v : mn; } }
    else if (a) { for (int j = 0; j < GP; j++) { float v = f[j] - Ta[j]; tmp[j] = v; mn = v < mn ? v : mn; } }
    else { for (int j = 0; j < GP; j++) { float v = f[j] + Tb[j]; tmp[j] = v; mn = v < mn ? v : mn; } }
    double U = -mn, s = 0; float cut = mn + (float)(8.0 / beta);
    for (int j = 0; j < GP; j++) if (tmp[j] < cut) s += exp(beta * (mn - tmp[j]));
    *Uout = U; return U + log(s) / beta;
}

static void recompute(const char *inA) {
    for (int j = 0; j < GP; j++) f[j] = 0;
    double *acc = calloc(GP, sizeof(double));
    for (int n = 1; n <= X; n++) if (inA[n]) for (int j = 0; j < GP; j++) acc[j] += cos(M_PI * (double)n * j / G);
    for (int j = 0; j < GP; j++) f[j] = (float)acc[j];
    free(acc);
}

static double cur_phi(double *Uout) {
    float mn = 1e30f; for (int j = 0; j < GP; j++) mn = f[j] < mn ? f[j] : mn;
    double s = 0; float cut = mn + (float)(8.0 / beta);
    for (int j = 0; j < GP; j++) if (f[j] < cut) s += exp(beta * (mn - f[j]));
    *Uout = -mn; return -mn + log(s) / beta;
}

/* arch profile w(t) = (h*h~)(t)/(h*h~)(0), h(t) = sin(pi t)^0.8 on [0,1] */
static double arch_w(double t) {
    static double *W = NULL; static int K = 4000;
    if (!W) { W = malloc(sizeof(double) * (K + 1)); double *h = malloc(sizeof(double) * (K + 1));
        for (int i = 0; i <= K; i++) h[i] = pow(sin(M_PI * i / K), 0.8);
        for (int s = 0; s <= K; s++) { double acc = 0; for (int i = s; i <= K; i++) acc += h[i] * h[i - s]; W[s] = acc; }
        for (int s = K; s >= 0; s--) W[s] /= W[0]; free(h); }
    if (t >= 1) return 0; double u = t * K; int i = (int)u; double fr = u - i; return W[i] * (1 - fr) + (i < K ? W[i + 1] : 0) * fr;
}

int main(int argc, char **argv) {
    if (argc < 8) { fprintf(stderr, "usage: dsearch X N G iters seed beta mode [initfile|corefrac] [time_limit]\n"); return 2; }
    X = atoi(argv[1]); N = atoi(argv[2]); G = atoi(argv[3]); long iters = atol(argv[4]);
    uint64_t seed = strtoull(argv[5], 0, 10); beta = atof(argv[6]); int mode = atoi(argv[7]);
    double tlim = argc > 9 ? atof(argv[9]) : 1e18;
    if (G <= 0) G = 12 * X; GP = G + 1;
    rng_t rng; rseed(&rng, seed);
    T = malloc(sizeof(float) * (size_t)(X + 1) * GP);
    for (int n = 0; n <= X; n++) for (int j = 0; j < GP; j++) T[(size_t)n * GP + j] = (float)cos(M_PI * (double)((long)n * j % (2L * G)) / G);
    f = malloc(sizeof(float) * GP); tmp = malloc(sizeof(float) * GP);
    char *inA = calloc(X + 2, 1); int *A = malloc(sizeof(int) * N), *notA = malloc(sizeof(int) * X);
    /* ---- initialisation ---- */
    int cnt = 0;
    if (mode == 3) {
        FILE *fp = fopen(argv[8], "r"); int v;
        while (fp && fscanf(fp, "%d", &v) == 1) if (v >= 1 && v <= X && !inA[v] && cnt < N) { inA[v] = 1; cnt++; }
        if (fp) fclose(fp);
    } else if (mode == 1) {
        double cf = argc > 8 ? atof(argv[8]) : 0.62; int Y = (int)lround(cf * X); int Nc = (int)lround(0.8 * N); if (Nc > Y) Nc = Y;
        while (cnt < Nc) { int v = 1 + rint_(&rng, Y); if (!inA[v]) { inA[v] = 1; cnt++; } }
    } else if (mode == 2) {
        /* scale so that sum_n w(n/Xw) = N with Xw <= X */
        double lo = 1, hi = X; for (int it = 0; it < 60; it++) { double mid = 0.5 * (lo + hi), s = 0;
            for (int n = 1; n <= X; n++) s += arch_w(n / mid); if (s < N) lo = mid; else hi = mid; }
        for (int n = 1; n <= X && cnt < N; n++) if (runif(&rng) < arch_w(n / hi)) { inA[n] = 1; cnt++; }
    }
    while (cnt < N) { int v = 1 + rint_(&rng, X); if (!inA[v]) { inA[v] = 1; cnt++; } }
    recompute(inA);
    /* ---- tabu state ---- */
    long *tab_add = calloc(X + 2, sizeof(long)), *tab_rem = calloc(X + 2, sizeof(long));
    double U, phi = cur_phi(&U), bestU = U, t0 = now();
    char *bestA = malloc(X + 2); memcpy(bestA, inA, X + 2);
    enum { NE = 8 }; char *elite[NE]; double eliteU[NE]; int ne = 0;
    for (int e = 0; e < NE; e++) { elite[e] = malloc(X + 2); eliteU[e] = 1e30; }
    double *g = malloc(sizeof(double) * (X + 2)); int *J = malloc(sizeof(int) * GP); double *pj = malloc(sizeof(double) * GP);
    int KR = 8, KA = 8, NRND = 8; long last_imp = 0, stag = 4000 + 40L * N; int tenure = 7 + N / 12;
    int *candR = malloc(sizeof(int) * (KR + 8)), *candA = malloc(sizeof(int) * (KA + 8));
    long it; double runU = U; char *runA = malloc(X + 2); memcpy(runA, inA, X + 2); long nrestart = 0;
    for (it = 1; it <= iters; it++) {
        if ((it & 1023) == 0) { recompute(inA); phi = cur_phi(&U); if (now() - t0 > tlim) break; }
        /* soft-max weights and gradient */
        float mn = 1e30f; for (int j = 0; j < GP; j++) mn = f[j] < mn ? f[j] : mn;
        int nj = 0; double ps = 0; float cut = mn + (float)(6.0 / beta);
        for (int j = 0; j < GP; j++) if (f[j] < cut) { J[nj] = j; pj[nj] = exp(beta * (mn - f[j])); ps += pj[nj]; nj++; }
        int na = 0, nn = 0;
        for (int n = 1; n <= X; n++) { double s = 0; const float *Tn = T + (size_t)n * GP;
            for (int q = 0; q < nj; q++) s += pj[q] * Tn[J[q]]; g[n] = s / ps;
            if (inA[n]) A[na++] = n; else notA[nn++] = n; }
        /* top-KR removals (smallest g) and top-KA additions (largest g) by partial selection */
        int nr = 0, nadd = 0;
        for (int i = 0; i < na; i++) { int n = A[i]; if (nr < KR) { candR[nr++] = n; } else { int w = 0;
            for (int q = 1; q < KR; q++) if (g[candR[q]] > g[candR[w]]) w = q; if (g[n] < g[candR[w]]) candR[w] = n; } }
        for (int i = 0; i < nn; i++) { int n = notA[i]; if (nadd < KA) { candA[nadd++] = n; } else { int w = 0;
            for (int q = 1; q < KA; q++) if (g[candA[q]] < g[candA[w]]) w = q; if (g[n] > g[candA[w]]) candA[w] = n; } }
        /* evaluate candidate swaps */
        double bphi = 1e30, bU = 0; int ba = 0, bb = 0;
        #define TRY(aa, bb_) do { int _a = (aa), _b = (bb_); if (_a >= 1 && _a <= X && _b >= 1 && _b <= X && inA[_a] && !inA[_b]) { \
            double _U, _p = eval_swap(_a, _b, &_U); int tabu = (tab_add[_b] > it) || (tab_rem[_a] > it); \
            if ((!tabu || _U < bestU - 1e-9) && _p < bphi) { bphi = _p; bU = _U; ba = _a; bb = _b; } } } while (0)
        for (int r = 0; r < nr; r++) for (int s = 0; s < nadd; s++) TRY(candR[r], candA[s]);
        for (int r = 0; r < nr; r++) { int a = candR[r]; TRY(a, a + 1); TRY(a, a - 1); TRY(a, a + 2); TRY(a, a - 2); }
        for (int s = 0; s < nadd; s++) { int b = candA[s]; TRY(b + 1, b); TRY(b - 1, b); }
        for (int q = 0; q < NRND; q++) TRY(A[rint_(&rng, na)], notA[rint_(&rng, nn)]);
        if (!ba) continue;
        /* apply */
        const float *Ta = T + (size_t)ba * GP, *Tb = T + (size_t)bb * GP;
        for (int j = 0; j < GP; j++) f[j] += Tb[j] - Ta[j];
        inA[ba] = 0; inA[bb] = 1; phi = bphi; U = bU;
        tab_add[ba] = it + tenure + rint_(&rng, tenure); tab_rem[bb] = it + tenure + rint_(&rng, tenure);
        if (U < runU - 1e-9) { runU = U; memcpy(runA, inA, X + 2); last_imp = it; }
        if (U < bestU - 1e-9) {
            bestU = U; memcpy(bestA, inA, X + 2);
            printf("BEST U=%.6f R=%.6f it=%ld t=%.1f A=", U, U / sqrt(N), it, now() - t0);
            for (int n = 1; n <= X; n++) if (inA[n]) printf("%d ", n); printf("\n"); fflush(stdout);
        }
        if (it - last_imp > stag) {
            /* insert this run's best into the elite pool (if distinct), restart from an elite member, perturbed */
            int dup = 0; for (int e = 0; e < ne; e++) if (!memcmp(elite[e], runA, X + 2)) dup = 1;
            if (!dup) { int w; if (ne < NE) w = ne++; else { w = 0; for (int e = 1; e < NE; e++) if (eliteU[e] > eliteU[w]) w = e; }
                if (eliteU[w] > runU) { memcpy(elite[w], runA, X + 2); eliteU[w] = runU; } }
            int e = rint_(&rng, ne); if (runif(&rng) < 0.5) { e = 0; for (int q = 1; q < ne; q++) if (eliteU[q] < eliteU[e]) e = q; }
            memcpy(inA, elite[e], X + 2);
            int kp = 2 + rint_(&rng, 2 + N / 10);
            for (int q = 0; q < kp; q++) { int a, b; do a = 1 + rint_(&rng, X); while (!inA[a]); do b = 1 + rint_(&rng, X); while (inA[b]);
                inA[a] = 0; inA[b] = 1; }
            recompute(inA); phi = cur_phi(&U); memset(tab_add, 0, sizeof(long) * (X + 2)); memset(tab_rem, 0, sizeof(long) * (X + 2));
            last_imp = it; runU = 1e30; nrestart++;
        }
    }
    printf("FINAL U=%.6f R=%.6f it=%ld restarts=%ld t=%.1f X=%d N=%d G=%d seed=%llu mode=%d A=", bestU, bestU / sqrt(N), it, nrestart, now() - t0, X, N, G,
           (unsigned long long)seed, mode);
    for (int n = 1; n <= X; n++) if (bestA[n]) printf("%d ", n); printf("\n");
    return 0;
}
