/* pair_sa.c — E38: is the Z-analogue of Theorem O4 (every t-run a 2-run: A = S ∪ (S+t)) better or worse than
 * unrestricted sets?  Simulated annealing on M(A) = −min_x Σ_{a∈A} cos(a x), evaluated on a grid of G points in [0, π]
 * (f is even and 2π-periodic), with an O(G) incremental update per move.  HEURISTIC (search lower bounds on the best R;
 * grid minimum only, refine/certify the winners separately).
 *   mode 0 (pair):  A = S ∪ (S + t), |S| = n, S ⊂ [1, L], no two elements of S differ by t (so |A| = 2n).
 *   mode 1 (free):  A ⊂ [1, L + t] arbitrary with |A| = 2n (calibration: same span, same size, same search effort).
 * Usage: pair_sa mode n t L iters restarts seed        prints best grid R, M, and A.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

#define G 4096
static int mode, n, t, L, span;
static double *ctab;            /* ctab[a*G + j] = cos(a * x_j), x_j = π j / (G-1) */
static double f[G];
static int *S, *inS, nS;        /* mode 0: S (n elements); mode 1: A (2n elements) */

static inline void addfreq(int a, double s) { const double *c = ctab + (size_t)a * G; for (int j = 0; j < G; j++) f[j] += s * c[j]; }
static inline double curM(void) { double m = 1e300; for (int j = 0; j < G; j++) if (f[j] < m) m = f[j]; return -m; }
static inline void place(int x, double s) { addfreq(x, s); if (mode == 0) addfreq(x + t, s); }
static int ok(int x) {           /* can x be inserted? */
    if (x < 1 || x > (mode == 0 ? L : span) || inS[x]) return 0;
    if (mode == 0) { if (x + t <= L && inS[x + t]) return 0; if (x - t >= 1 && inS[x - t]) return 0; }
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 8) { fprintf(stderr, "usage: mode n t L iters restarts seed\n"); return 2; }
    mode = atoi(argv[1]); n = atoi(argv[2]); t = atoi(argv[3]); L = atoi(argv[4]);
    long iters = atol(argv[5]); int restarts = atoi(argv[6]); rs = 0x9E3779B97F4A7C15ULL ^ (uint64_t)atol(argv[7]);
    span = L + t; nS = (mode == 0) ? n : 2 * n;
    ctab = malloc(sizeof(double) * (size_t)(span + 1) * G);
    for (int a = 0; a <= span; a++) for (int j = 0; j < G; j++) ctab[(size_t)a * G + j] = cos(a * M_PI * j / (G - 1));
    S = malloc(sizeof(int) * nS); inS = calloc(span + 2, sizeof(int));
    int *best = malloc(sizeof(int) * nS); double bestM = 1e300;
    for (int rep = 0; rep < restarts; rep++) {
        memset(inS, 0, sizeof(int) * (span + 2)); memset(f, 0, sizeof f);
        for (int i = 0; i < nS; i++) { int x, tries = 0; do { x = 1 + (int)(rnd() % (mode == 0 ? L : span)); } while (!ok(x) && ++tries < 100000);
            S[i] = x; inS[x] = 1; place(x, 1.0); }
        double cur = curM(), T0 = 0.3, T1 = 0.003;
        for (long it = 0; it < iters; it++) {
            double T = T0 * pow(T1 / T0, (double)it / iters);
            int i = (int)(rnd() % nS), old = S[i], x;
            /* local move (±1..3) half the time, global otherwise */
            if (rnd() & 1) x = old + (int)(rnd() % 7) - 3; else x = 1 + (int)(rnd() % (mode == 0 ? L : span));
            inS[old] = 0;
            if (x == old || !ok(x)) { inS[old] = 1; continue; }
            place(old, -1.0); place(x, 1.0);
            double nw = curM();
            if (nw <= cur || urand() < exp((cur - nw) / T)) { S[i] = x; inS[x] = 1; cur = nw;
                if (cur < bestM) { bestM = cur; memcpy(best, S, sizeof(int) * nS); } }
            else { place(x, -1.0); place(old, 1.0); inS[old] = 1; }
        }
    }
    int NA = 2 * n; int *A = malloc(sizeof(int) * NA), k = 0;
    for (int i = 0; i < nS; i++) { A[k++] = best[i]; if (mode == 0) A[k++] = best[i] + t; }
    for (int i = 0; i < NA; i++) for (int j = i + 1; j < NA; j++) if (A[j] < A[i]) { int z = A[i]; A[i] = A[j]; A[j] = z; }
    printf("mode=%d n=%d t=%d L=%d N=%d gridM=%.6f R=%.5f max=%d A=", mode, n, t, L, NA, bestM, bestM / sqrt(NA), A[NA - 1]);
    for (int i = 0; i < NA; i++) printf("%d%c", A[i], i + 1 < NA ? ',' : '\n');
    return 0;
}
