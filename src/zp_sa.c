/* zp_sa.c — E41b: heuristic upper bounds on min M_p over symmetric half-sets of Z_p (same objective as zp_half.c):
 * P = set of k pairs {a,−a} ⊂ Z_p^*, k = (p−1)/4 (p ≡ 1 mod 4) or (p+1)/4 (p ≡ 3 mod 4),
 * M_p(P) = max_{γ=1..h} −2 Σ_{a∈P} cos(2π a γ/p).  Simulated annealing with swap moves (one pair out, one pair in),
 * O(h) incremental update per move.  Seeds: 0 = random, 1 = interval [1,k], 2 = quadratic residues (p ≡ 1 mod 4).
 * HEURISTIC (an upper bound on the minimum; exact only where zp_half.c confirms).
 * Optional 6th argument L (core): pairs 1..L are forced into P and never moved (core-plus-tail family, E41c); the
 * remaining k−L pairs are annealed over L+1..h (seedmode 1 then means the tail starts as L+1..k).
 * Usage: zp_sa p iters restarts seedmode rngseed [L]   prints best M, M/sqrt p, Paley value, and P.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: zp_sa p iters restarts seedmode rngseed\n"); return 2; }
    int p = atoi(argv[1]); long iters = atol(argv[2]); int restarts = atoi(argv[3]), mode = atoi(argv[4]);
    rs = 0x9E3779B97F4A7C15ULL ^ (uint64_t)atol(argv[5]);
    int L = (argc > 6) ? atoi(argv[6]) : 0;
    int h = (p - 1) / 2, k = (p % 4 == 1) ? (p - 1) / 4 : (p + 1) / 4;
    double *V = malloc(sizeof(double) * (size_t)(h + 1) * h);
    for (int a = 1; a <= h; a++) for (int g = 0; g < h; g++) V[(size_t)a * h + g] = 2.0 * cos(2.0 * M_PI * (double)((long)a * (g + 1) % p) / p);
    int *in = malloc(sizeof(int) * (h + 1)), *IN = malloc(sizeof(int) * k), *OUT = malloc(sizeof(int) * (h - k)), *best = malloc(sizeof(int) * (h + 1));
    double *F = malloc(sizeof(double) * h), *G = malloc(sizeof(double) * h), bestM = 1e300;
    for (int rep = 0; rep < restarts; rep++) {
        memset(in, 0, sizeof(int) * (h + 1));
        if (mode == 1) for (int a = 1; a <= k; a++) in[a] = 1;
        else if (mode == 2 && p % 4 == 1) for (long x = 1; x <= h; x++) in[(x * x) % p <= h ? (x * x) % p : p - (x * x) % p] = 1;
        else { int c = 0; while (c < k) { int a = 1 + (int)(rnd() % h); if (!in[a]) { in[a] = 1; c++; } } }
        for (int a = 1; a <= L; a++) if (!in[a]) { /* force core: swap out a random non-core member */
            int b; do { b = L + 1 + (int)(rnd() % (h - L)); } while (!in[b]); in[b] = 0; in[a] = 1; }
        int ni = 0, no = 0; for (int a = 1; a <= L; a++) IN[ni++] = a;
        for (int a = L + 1; a <= h; a++) { if (in[a]) IN[ni++] = a; else OUT[no++] = a; }
        if (ni != k) { fprintf(stderr, "seed size %d != k %d\n", ni, k); return 1; }
        for (int g = 0; g < h; g++) { double s = 0; for (int i = 0; i < k; i++) s += V[(size_t)IN[i] * h + g]; F[g] = s; }
        double cur = -1e300; for (int g = 0; g < h; g++) if (-F[g] > cur) cur = -F[g];
        if (cur < bestM) { bestM = cur; memcpy(best, in, sizeof(int) * (h + 1)); }
        double T0 = (mode == 0 || rep > 0) ? 1.0 : 0.3, T1 = 0.002;
        for (long it = 0; it < iters; it++) {
            double T = T0 * pow(T1 / T0, (double)it / iters);
            if (k == L || h == k) break;
            int i = L + (int)(rnd() % (k - L)), j = (int)(rnd() % (h - k)); int a = IN[i], b = OUT[j];
            const double *va = V + (size_t)a * h, *vb = V + (size_t)b * h; double nw = -1e300;
            for (int g = 0; g < h; g++) { G[g] = F[g] - va[g] + vb[g]; if (-G[g] > nw) nw = -G[g]; }
            if (nw <= cur || urand() < exp((cur - nw) / T)) {
                memcpy(F, G, sizeof(double) * h); cur = nw; IN[i] = b; OUT[j] = a; in[a] = 0; in[b] = 1;
                if (cur < bestM - 1e-12) { bestM = cur; memcpy(best, in, sizeof(int) * (h + 1)); }
            }
        }
    }
    printf("p=%d k=%d L=%d mode=%d bestM=%.6f M/sqrtp=%.5f paley/sqrtp=%.5f P=", p, k, L, mode, bestM, bestM / sqrt(p), (1 + sqrt(p)) / 2 / sqrt(p));
    for (int a = 1; a <= h; a++) if (best[a]) printf("%d ", a);
    printf("\n");
    return 0;
}
