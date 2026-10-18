/* lambda_ruler_sa.c — E35: how close can a set D ⊂ [0, L] of k integers come to a λ-fold ruler?
 * (NOTEBOOK 2026-10-18 evening.)  r(d) = #{(u,v) ∈ D², u − v = d}, d >= 1.  Exact fraction
 *     φ = Σ_{d : r(d) = λ} r(d) / (k(k−1)/2)   (share of pairs whose difference has multiplicity exactly λ).
 * With A = {d : r(d) = λ}: 2λ f_A = |F_D|² − k − E,  E = Σ_{d: r(d) ∉ {0,λ}} 2 r(d) cos(dx),  λ|A| = φ k(k−1)/2, so
 *     R(A) ≈ (1 + sup_{off main lobe} E / k) / sqrt(2λφ);  R < 1/2 at λ = 3 needs φ > 2/3 (and tame E).
 * Simulated annealing maximising φ by single-point relocations, O(k) incremental update of r. HEURISTIC search
 * (lower bounds on the best φ only).  Validation: λ = 2 has Bu-type sets with φ = 1 − 1/(k−1).
 * Usage: lambda_ruler_sa lambda k L iters restarts seed      prints best φ, defect pairs, and D.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static int lam, k, L;
static int *D, *inD, *r;
static long good;              /* Σ over d with r(d) = λ of r(d)  (= λ · #classes) */

static inline long contrib(int x) { return x == lam ? lam : 0; }
static inline void addpair(int d, int s) { int old = r[d]; good -= contrib(old); r[d] = old + s; good += contrib(old + s); }

static void place(int i, int x, int s) {   /* s = +1 add point x (index i), s = -1 remove */
    for (int j = 0; j < k; j++) if (j != i) { int d = abs(D[j] - x); addpair(d, s); }
}

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: lambda k L iters restarts seed\n"); return 2; }
    lam = atoi(argv[1]); k = atoi(argv[2]); L = atoi(argv[3]);
    long iters = atol(argv[4]); int restarts = atoi(argv[5]); rs = 0x9E3779B97F4A7C15ULL ^ (uint64_t)atol(argv[6]);
    D = malloc(sizeof(int) * k); inD = calloc(L + 1, sizeof(int)); r = calloc(L + 1, sizeof(int));
    int *bestD = malloc(sizeof(int) * k); long bestgood = -1;
    long pairs = (long)k * (k - 1) / 2;
    for (int rep = 0; rep < restarts; rep++) {
        memset(inD, 0, sizeof(int) * (L + 1)); memset(r, 0, sizeof(int) * (L + 1)); good = 0;
        for (int i = 0; i < k; i++) {                 /* random init, endpoints 0 and L included */
            int x; do x = (i == 0) ? 0 : (i == 1) ? L : (int)(rnd() % (L + 1)); while (inD[x]);
            D[i] = x; inD[x] = 1;
        }
        for (int i = 0; i < k; i++) for (int j = 0; j < i; j++) addpair(abs(D[i] - D[j]), +1);
        long cur = good, repbest = good;
        double T0 = 2.0, T1 = 0.02;
        for (long it = 0; it < iters; it++) {
            double T = T0 * pow(T1 / T0, (double)it / iters);
            int i = 2 + (int)(rnd() % (k - 2));          /* keep endpoints fixed (span exactly L) */
            int x; do x = 1 + (int)(rnd() % (L - 1)); while (inD[x]);
            int old = D[i];
            place(i, old, -1); D[i] = x; place(i, x, +1);
            long nw = good;
            if (nw >= cur || urand() < exp((nw - cur) / T)) {
                inD[old] = 0; inD[x] = 1; cur = nw;
                if (cur > repbest) repbest = cur;
                if (cur > bestgood) { bestgood = cur; memcpy(bestD, D, sizeof(int) * k); }
            } else { place(i, x, -1); D[i] = old; place(i, old, +1); }
        }
        (void)repbest;
    }
    /* report */
    memset(r, 0, sizeof(int) * (L + 1));
    for (int i = 0; i < k; i++) for (int j = 0; j < i; j++) r[abs(bestD[i] - bestD[j])]++;
    long defect_pairs = 0, nA = 0, W = 0;
    for (int d = 1; d <= L; d++) { if (r[d] == lam) nA++; else if (r[d]) { defect_pairs += r[d]; W += 2 * r[d]; } }
    printf("lam=%d k=%d L=%d phi=%.4f |A|=%ld defect_pairs=%ld W/k=%.3f D=", lam, k, L,
           (double)bestgood / pairs, nA, defect_pairs, (double)W / k);
    int *srt = malloc(sizeof(int) * k); memcpy(srt, bestD, sizeof(int) * k);
    for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (srt[j] < srt[i]) { int t = srt[i]; srt[i] = srt[j]; srt[j] = t; }
    for (int i = 0; i < k; i++) printf("%d%c", srt[i], i + 1 < k ? ',' : '\n');
    return 0;
}
