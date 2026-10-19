/* e68_pareto_sa.c — E68 (from e67_bulk_sa.c): Pareto search, objective beta_K + mu*R (R = grid M/sqrt n).
 * Question: can a DENSE set be simultaneously spike-dominated (small beta_K) and small in R? (NOTEBOOK SB.)
 * Original E67 header follows.
 * E67: adversarial search against Conjecture SB (NOTEBOOK 2026-10-19 late; PROOFS P40).
 * Bulk fraction at level K: beta_K(A) = int_{f_A <= K sqrt(n)} f_A^2 / int f_A^2   (normalized Haar measure).
 * A Chowla counterexample with M = eps sqrt(n) has beta_K <= 2(K + 2 eps) eps (P40), so SB (beta_K >= c > 0 for all A)
 * implies Chowla. Here: anneal A ⊂ [1, X], |A| = n fixed, minimising beta_K (swap moves). f is even, so use the grid
 * x_j = pi j/(G-1), j = 0..G-1, G = 8X+1, with trapezoid weights. Also report the grid minimum M of the best set.
 * HEURISTIC: grid integrals; this is a falsification search for SB, not a certificate.
 * Usage: e67_bulk_sa X n K iters restarts seed      prints JSON lines (one per restart) with beta, M, R and A.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
static int G;
static float *ctab;   /* ctab[(a-1)*G + j] = cos(a x_j) */
static double *wt;

static int cmp(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }

static double beta(const double *f, double thr, double *Mout) {
    double num = 0, den = 0, mn = 1e300;
    for (int j = 0; j < G; j++) {
        double v = f[j], w = wt[j] * v * v; den += w; if (v <= thr) num += w; if (v < mn) mn = v;
    }
    if (Mout) *Mout = -mn;
    return num / den;
}

int main(int argc, char **argv) {
    if (argc < 8) { fprintf(stderr, "usage: e68_pareto_sa X n K mu iters restarts seed\n"); return 2; }
    int X = atoi(argv[1]), n = atoi(argv[2]); double K = atof(argv[3]);
    double mu = atof(argv[4]); long iters = atol(argv[5]); int restarts = atoi(argv[6]);
    rs = strtoull(argv[7], 0, 10) * 2654435761ULL + 88172645463325252ULL;
    G = 8 * X + 1;
    ctab = malloc(sizeof(float) * (size_t)X * G); wt = malloc(sizeof(double) * G);
    for (int a = 1; a <= X; a++) for (int j = 0; j < G; j++) ctab[(size_t)(a - 1) * G + j] = (float)cos(a * M_PI * j / (G - 1));
    for (int j = 0; j < G; j++) wt[j] = (j == 0 || j == G - 1) ? 0.5 : 1.0;
    double thr = K * sqrt((double)n);
    double *f = malloc(sizeof(double) * G), *g = malloc(sizeof(double) * G);
    int *in = malloc(sizeof(int) * (X + 1)), *el = malloc(sizeof(int) * n), *out = malloc(sizeof(int) * X);
    for (int r = 0; r < restarts; r++) {
        memset(in, 0, sizeof(int) * (X + 1)); memset(f, 0, sizeof(double) * G);
        int c = 0; while (c < n) { int a = 1 + (int)(rnd() % X); if (!in[a]) { in[a] = 1; el[c++] = a; const float *t = ctab + (size_t)(a - 1) * G; for (int j = 0; j < G; j++) f[j] += t[j]; } }
        int no = 0; for (int a = 1; a <= X; a++) if (!in[a]) out[no++] = a;
        double Mc; double b = beta(f, thr, &Mc) + mu * Mc / sqrt((double)n), best = b; int *bestA = malloc(sizeof(int) * n); memcpy(bestA, el, sizeof(int) * n);
        double T0 = 0.02;
        for (long it = 0; it < iters; it++) {
            double T = T0 * pow(1e-3, (double)it / iters);
            int i = (int)(rnd() % n), o = (int)(rnd() % no);
            const float *ta = ctab + (size_t)(el[i] - 1) * G, *tb = ctab + (size_t)(out[o] - 1) * G;
            for (int j = 0; j < G; j++) g[j] = f[j] - ta[j] + tb[j];
            double M2; double b2 = beta(g, thr, &M2) + mu * M2 / sqrt((double)n);
            if (b2 <= b || urand() < exp((b - b2) / T)) {
                double *tmp = f; f = g; g = tmp; int t = el[i]; el[i] = out[o]; out[o] = t; b = b2;
                if (b < best) { best = b; memcpy(bestA, el, sizeof(int) * n); }
            }
        }
        memset(f, 0, sizeof(double) * G);
        for (int i = 0; i < n; i++) { const float *t = ctab + (size_t)(bestA[i] - 1) * G; for (int j = 0; j < G; j++) f[j] += t[j]; }
        double M; double bb = beta(f, thr, &M);
        qsort(bestA, n, sizeof(int), cmp);
        printf("{\"X\": %d, \"n\": %d, \"K\": %g, \"mu\": %g, \"iters\": %ld, \"restart\": %d, \"beta\": %.6f, \"grid_M\": %.6f, \"grid_R\": %.6f, \"A\": [",
               X, n, K, mu, iters, r, bb, M, M / sqrt((double)n));
        for (int i = 0; i < n; i++) printf(i ? ", %d" : "%d", bestA[i]);
        printf("]}\n"); fflush(stdout); free(bestA);
    }
    return 0;
}
