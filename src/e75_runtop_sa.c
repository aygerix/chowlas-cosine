/* e75_runtop_sa.c — E75: adversarial search against the per-t run-top conjecture RT2 (|B_t| <~ K^2 in Z,
 * NOTEBOOK/EXPERIMENTS E74). Anneal A ⊂ [1, X], |A| = n, MAXIMISING  Q(A) = max_t |B_t(A')| / K_grid^2,
 * A' = A ∪ (−A), B_t = {a ∈ A' : a − t ∈ A', a + t ∉ A'} (t >= 1), K = 2·lambda_grid, lambda_grid = −min f_A on a
 * grid of 8X+1 points of [0, pi]. If mode = 1 the objective is mean_{1<=t<=2X} |B_t| / K^2 instead.
 * Swap moves; f on the grid updated incrementally; |B_t| recomputed in O(X^2/64)-ish per move (direct, X small).
 * HEURISTIC search; grid lambda is UNCERTIFIED (best sets must be re-evaluated). Prints JSON per restart.
 * Usage: e75_runtop_sa X n mode iters restarts seed
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
static int cmpi(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }

static int X, n, G, mode;
static float *ctab; static double *f, *g;
static unsigned char *ind; /* ind[off + v] for v in [-X-2X.., ...] */
static int off, L;

static double objective(const double *fv, int *targ, double *lam) {
    double m = 1e300; for (int j = 0; j < G; j++) if (fv[j] < m) m = fv[j];
    double K = 2 * (-m); *lam = -m; if (K < 1e-9) K = 1e-9;
    long best = 0, sum = 0; int bt = 1;
    for (int t = 1; t <= 2 * X; t++) {
        long c = 0;
        for (int v = -X; v <= X; v++) {
            if (!ind[off + v]) continue;
            if (ind[off + v - t] && !ind[off + v + t]) c++;
        }
        sum += c; if (c > best) { best = c; bt = t; }
    }
    *targ = bt;
    return mode == 0 ? best / (K * K) : (sum / (2.0 * X)) / (K * K);
}

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: e75_runtop_sa X n mode iters restarts seed\n"); return 2; }
    X = atoi(argv[1]); n = atoi(argv[2]); mode = atoi(argv[3]); long iters = atol(argv[4]); int restarts = atoi(argv[5]);
    rs = strtoull(argv[6], 0, 10) * 2654435761ULL + 88172645463325252ULL;
    G = 8 * X + 1; ctab = malloc(sizeof(float) * (size_t)X * G); f = malloc(sizeof(double) * G); g = malloc(sizeof(double) * G);
    for (int m = 1; m <= X; m++) for (int j = 0; j < G; j++) ctab[(size_t)(m - 1) * G + j] = (float)cos(m * M_PI * j / (G - 1));
    off = 4 * X + 2; L = 2 * off + 1; ind = calloc(L, 1);
    int *el = malloc(sizeof(int) * n), *out = malloc(sizeof(int) * X), *bestA = malloc(sizeof(int) * n);
    for (int rr = 0; rr < restarts; rr++) {
        memset(ind, 0, L); memset(f, 0, sizeof(double) * G);
        int c = 0; while (c < n) { int m = 1 + (int)(rnd() % X); if (!ind[off + m]) { ind[off + m] = ind[off - m] = 1; el[c++] = m;
            const float *tb = ctab + (size_t)(m - 1) * G; for (int j = 0; j < G; j++) f[j] += tb[j]; } }
        int no = 0; for (int m = 1; m <= X; m++) if (!ind[off + m]) out[no++] = m;
        int bt; double lam, Q = objective(f, &bt, &lam), bestQ = Q; memcpy(bestA, el, sizeof(int) * n);
        double T0 = 0.05 * (Q > 0 ? Q : 1);
        for (long it = 0; it < iters; it++) {
            double T = T0 * pow(1e-3, (double)it / iters);
            int i = (int)(rnd() % n), o = (int)(rnd() % no); int u = el[i], v = out[o];
            ind[off + u] = ind[off - u] = 0; ind[off + v] = ind[off - v] = 1;
            const float *ta = ctab + (size_t)(u - 1) * G, *tb = ctab + (size_t)(v - 1) * G;
            for (int j = 0; j < G; j++) g[j] = f[j] - ta[j] + tb[j];
            double lam2; int bt2; double Q2 = objective(g, &bt2, &lam2);
            if (Q2 >= Q || urand() < exp((Q2 - Q) / T)) {
                double *tmp = f; f = g; g = tmp; el[i] = v; out[o] = u; Q = Q2;
                if (Q > bestQ) { bestQ = Q; memcpy(bestA, el, sizeof(int) * n); }
            } else { ind[off + v] = ind[off - v] = 0; ind[off + u] = ind[off - u] = 1; }
        }
        /* re-evaluate best */
        memset(ind, 0, L); memset(f, 0, sizeof(double) * G);
        for (int k = 0; k < n; k++) { int m = bestA[k]; ind[off + m] = ind[off - m] = 1; const float *tb = ctab + (size_t)(m - 1) * G; for (int j = 0; j < G; j++) f[j] += tb[j]; }
        Q = objective(f, &bt, &lam);
        qsort(bestA, n, sizeof(int), cmpi);
        printf("{\"X\": %d, \"n\": %d, \"mode\": %d, \"iters\": %ld, \"restart\": %d, \"Q\": %.6f, \"t_star\": %d, \"lambda_grid\": %.6f, \"R_grid\": %.6f, \"A\": [",
               X, n, mode, iters, rr, Q, bt, lam, lam / sqrt((double)n));
        for (int k = 0; k < n; k++) printf(k ? ", %d" : "%d", bestA[k]);
        printf("]}\n"); fflush(stdout);
    }
    return 0;
}
