/* e83_sa.c — E83: block-preserving simulated annealing on M(A) = −min_x Σ_{a∈A} cos(a x) from a GIVEN initial set.
 * Blocks of length b partition [1, X]; a move swaps an element with a non-element of the same block, so the density
 * profile of the initial set is preserved exactly. f is even: grid of G = 8X + 1 points on [0, π], O(G) update per move.
 * HEURISTIC: grid minimum only.
 * Usage: e83_sa X b iters restarts seed T0 < initset   (initset: whitespace-separated elements)
 * Prints one JSON line: init grid M, best grid M, n, and the best set.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
static int X, G, b, nb;
static double *ctab;
static inline void addfreq(double *h, int a, double s) { const double *c = ctab + (size_t)(a - 1) * G; for (int j = 0; j < G; j++) h[j] += s * c[j]; }
static inline double gridM(const double *h) { double m = 1e300; for (int j = 0; j < G; j++) if (h[j] < m) m = h[j]; return -m; }

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: e83_sa X b iters restarts seed T0 < initset\n"); return 2; }
    X = atoi(argv[1]); b = atoi(argv[2]); long iters = atol(argv[3]); int restarts = atoi(argv[4]);
    rs = strtoull(argv[5], 0, 10) * 2654435761ULL + 88172645463325252ULL; double T0 = atof(argv[6]);
    G = 8 * X + 1; nb = (X + b - 1) / b;
    ctab = malloc(sizeof(double) * (size_t)X * G);
    for (int a = 1; a <= X; a++) for (int j = 0; j < G; j++) ctab[(size_t)(a - 1) * G + j] = cos((double)a * M_PI * j / (G - 1));
    int *in0 = calloc(X + 1, sizeof(int)), *in = calloc(X + 1, sizeof(int)), *best = calloc(X + 1, sizeof(int));
    int v, n = 0;
    while (scanf("%d", &v) == 1) if (v >= 1 && v <= X && !in0[v]) { in0[v] = 1; n++; }
    double *f = malloc(sizeof(double) * G), *g = malloc(sizeof(double) * G);
    for (int j = 0; j < G; j++) f[j] = 0;
    for (int a = 1; a <= X; a++) if (in0[a]) addfreq(f, a, 1.0);
    double Minit = gridM(f), Mbest = Minit;
    for (int a = 1; a <= X; a++) best[a] = in0[a];
    for (int r = 0; r < restarts; r++) {
        for (int a = 1; a <= X; a++) in[a] = best[a];       /* each restart starts from the best so far */
        for (int j = 0; j < G; j++) f[j] = 0;
        for (int a = 1; a <= X; a++) if (in[a]) addfreq(f, a, 1.0);
        double Mcur = gridM(f);
        for (long it = 0; it < iters; it++) {
            double T = T0 * (1.0 - (double)it / iters) + 1e-9;
            int blk = rnd() % nb, lo = blk * b + 1, hi = lo + b - 1; if (hi > X) hi = X;
            int len = hi - lo + 1; if (len < 2) continue;
            int u = lo + rnd() % len, w = lo + rnd() % len;
            if (in[u] == in[w]) continue;
            if (!in[u]) { int t = u; u = w; w = t; }             /* u in A, w not */
            const double *cu = ctab + (size_t)(u - 1) * G, *cw = ctab + (size_t)(w - 1) * G;
            double m = 1e300;
            for (int j = 0; j < G; j++) { double h = f[j] - cu[j] + cw[j]; g[j] = h; if (h < m) m = h; }
            double Mnew = -m;
            if (Mnew <= Mcur || urand() < exp((Mcur - Mnew) / T)) {
                double *t = f; f = g; g = t; in[u] = 0; in[w] = 1; Mcur = Mnew;
                if (Mcur < Mbest) { Mbest = Mcur; for (int a = 1; a <= X; a++) best[a] = in[a]; }
            }
        }
    }
    printf("{\"X\": %d, \"n\": %d, \"b\": %d, \"M_init\": %.6f, \"M_best\": %.6f, \"R_init\": %.6f, \"R_best\": %.6f, \"A\": [",
           X, n, b, Minit, Mbest, Minit / sqrt(n), Mbest / sqrt(n));
    int first = 1; for (int a = 1; a <= X; a++) if (best[a]) { printf(first ? "%d" : ", %d", a); first = 0; }
    printf("]}\n");
    return 0;
}
