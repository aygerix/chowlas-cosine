/* profile_sa.c — E49: does steep front-loading help? P31 proves M >> √n unless A is front-loaded beyond ~2.5–2.9δ
 * (density near 0 vs average). Simulated annealing on M(A) = −min_x Σ_{a∈A} cos(a x) over sets whose density profile
 * is PRESCRIBED: [1, X] is cut into blocks of length b, and block k holds exactly round(Σ_{a∈block} c(1 − a/X)^p)
 * elements (total n). Moves swap an element with a non-element of the same block, so the profile is exact.
 * mode 1 (free) instead swaps any element with any non-element in [1, X] (calibration).
 * f is even, so it is evaluated on a grid of G = 8X + 1 points in [0, π], with an O(G) incremental update per move.
 * HEURISTIC: grid minimum only; refine/certify winners separately (src/chowla.py).
 * Usage: profile_sa mode X p c b iters restarts seed      prints JSON: best grid R, M, n, A.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static int X, G, n, b, nb, mode;
static double *ctab, *f, *g;
static int *in, *blk_lo, *blk_hi, *cnt;

static inline void addfreq(double *h, int a, double s) { const double *c = ctab + (size_t)(a - 1) * G; for (int j = 0; j < G; j++) h[j] += s * c[j]; }
static inline double gridM(const double *h) { double m = 1e300; for (int j = 0; j < G; j++) if (h[j] < m) m = h[j]; return -m; }

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: profile_sa mode X p c b iters restarts seed\n"); return 2; }
    mode = atoi(argv[1]); X = atoi(argv[2]); double p = atof(argv[3]), c = atof(argv[4]); b = atoi(argv[5]);
    long iters = atol(argv[6]); int restarts = atoi(argv[7]); rs = strtoull(argv[8], 0, 10) * 2654435761ULL + 88172645463325252ULL;
    G = 8 * X + 1;
    ctab = malloc(sizeof(double) * (size_t)X * G); f = malloc(sizeof(double) * G); g = malloc(sizeof(double) * G);
    for (int a = 1; a <= X; a++) for (int j = 0; j < G; j++) ctab[(size_t)(a - 1) * G + j] = cos(a * M_PI * j / (G - 1));
    nb = (X + b - 1) / b; blk_lo = malloc(sizeof(int) * nb); blk_hi = malloc(sizeof(int) * nb); cnt = malloc(sizeof(int) * nb);
    n = 0; double carry = 0;
    for (int k = 0; k < nb; k++) {
        blk_lo[k] = 1 + k * b; blk_hi[k] = (k + 1) * b < X ? (k + 1) * b : X;
        double want = carry; for (int a = blk_lo[k]; a <= blk_hi[k]; a++) want += c * pow(1.0 - (double)a / X, p);
        int ck = (int)floor(want + 0.5); int len = blk_hi[k] - blk_lo[k] + 1; if (ck > len) ck = len; if (ck < 0) ck = 0;
        carry = want - ck; cnt[k] = ck; n += ck;
    }
    in = calloc(X + 1, sizeof(int));
    int *bestA = malloc(sizeof(int) * (X + 1)); double bestR = 1e300, bestMv = 0;
    for (int r = 0; r < restarts; r++) {
        memset(in, 0, sizeof(int) * (X + 1)); memset(f, 0, sizeof(double) * G);
        for (int k = 0; k < nb; k++) {          /* random initial set with the block counts */
            int len = blk_hi[k] - blk_lo[k] + 1, placed = 0;
            while (placed < cnt[k]) { int a = blk_lo[k] + (int)(rnd() % len); if (!in[a]) { in[a] = 1; addfreq(f, a, 1); placed++; } }
        }
        double M = gridM(f), T0 = 0.05 * sqrt((double)n), T;
        for (long it = 0; it < iters; it++) {
            T = T0 * pow(1e-3, (double)it / iters);
            int a, a2;
            if (mode == 0) { int k = (int)(rnd() % nb); int len = blk_hi[k] - blk_lo[k] + 1; if (cnt[k] == 0 || cnt[k] == len) continue;
                do a = blk_lo[k] + (int)(rnd() % len); while (!in[a]); do a2 = blk_lo[k] + (int)(rnd() % len); while (in[a2]); }
            else { do a = 1 + (int)(rnd() % X); while (!in[a]); do a2 = 1 + (int)(rnd() % X); while (in[a2]); }
            memcpy(g, f, sizeof(double) * G); addfreq(g, a, -1); addfreq(g, a2, 1);
            double M2 = gridM(g);
            if (M2 <= M || urand() < exp((M - M2) / T)) { double *tmp = f; f = g; g = tmp; in[a] = 0; in[a2] = 1; M = M2; }
        }
        double R = M / sqrt((double)n);
        if (R < bestR) { bestR = R; bestMv = M; memcpy(bestA, in, sizeof(int) * (X + 1)); }
    }
    printf("{\"mode\": %d, \"X\": %d, \"p\": %g, \"c\": %g, \"b\": %d, \"n\": %d, \"iters\": %ld, \"restarts\": %d, \"grid_R\": %.6f, \"grid_M\": %.6f, \"A\": [",
           mode, X, p, c, b, n, iters, restarts, bestR, bestMv);
    int first = 1; for (int a = 1; a <= X; a++) if (bestA[a]) { printf(first ? "%d" : ", %d", a); first = 0; }
    printf("]}\n");
    return 0;
}
