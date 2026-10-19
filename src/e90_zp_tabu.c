/* e90_zp_tabu.c — E90: large-q heuristic search for symmetric half-sets of Z_q with small negative spectrum.
 * Same objective as zp_half.c / zp_sa.c (E41): P = k pairs {a,−a} ⊂ Z_q^*, k = (q−1)/4 (q ≡ 1 mod 4) or (q+1)/4,
 * K(P) = max_{γ=1..h} −λ(γ),  λ(γ) = 2 Σ_{a∈P} cos(2π aγ/q),  h = (q−1)/2.
 * Differences from zp_sa.c: a SMOOTH surrogate objective (soft-max of −λ at inverse temperature beta/√q), sampled
 * best-of-C swap moves, a tabu list on recently moved pairs, and periodic hard-max polishing. Also records
 * Λ = max_{γ} λ(γ) of the best set (the peak / negative-floor trade-off of NOTEBOOK cont. 17).
 * Seeds: 0 random, 1 interval [1,k], 2 quadratic residues (q ≡ 1 mod 4), 3 profiled interval: pairs a <= L forced in,
 * the rest random (L = argv[7], default k/3).
 * HEURISTIC: an upper bound on min K only.
 * Usage: e90_zp_tabu q steps restarts seedmode rngseed [beta] [L]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static double softobj(const double *F, int h, double b, double shift) {
    double s = 0; for (int g = 0; g < h; g++) s += exp(b * (-F[g] - shift)); return shift + log(s) / b;
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: e90_zp_tabu q steps restarts seedmode rngseed [beta] [L]\n"); return 2; }
    int q = atoi(argv[1]); long steps = atol(argv[2]); int restarts = atoi(argv[3]), mode = atoi(argv[4]);
    rs = 0x9E3779B97F4A7C15ULL ^ (uint64_t)atol(argv[5]);
    double beta = (argc > 6) ? atof(argv[6]) : 6.0;
    int h = (q - 1) / 2, k = (q % 4 == 1) ? (q - 1) / 4 : (q + 1) / 4;
    int Lc = (argc > 7) ? atoi(argv[7]) : k / 3;
    double b = beta / sqrt((double)q);
    double *V = malloc(sizeof(double) * (size_t)(h + 1) * h);
    for (int a = 1; a <= h; a++) for (int g = 0; g < h; g++) V[(size_t)a * h + g] = 2.0 * cos(2.0 * M_PI * (double)((long)a * (g + 1) % q) / q);
    int *in = malloc(sizeof(int) * (h + 1)), *IN = malloc(sizeof(int) * k), *OUT = malloc(sizeof(int) * (h - k));
    int *best = malloc(sizeof(int) * (h + 1)); long *tabu = calloc(h + 1, sizeof(long));
    double *F = malloc(sizeof(double) * h), *G = malloc(sizeof(double) * h), bestK = 1e300, bestLam = 0;
    const int C = 48; const long tenure = 2 + k / 8;
    for (int rep = 0; rep < restarts; rep++) {
        memset(in, 0, sizeof(int) * (h + 1)); memset(tabu, 0, sizeof(long) * (h + 1));
        if (mode == 1) for (int a = 1; a <= k; a++) in[a] = 1;
        else if (mode == 2 && q % 4 == 1) for (long x = 1; x <= h; x++) { long r = (x * x) % q; in[r <= h ? r : q - r] = 1; }
        else {
            int c = 0;
            if (mode == 3) for (int a = 1; a <= Lc && c < k; a++) { in[a] = 1; c++; }
            while (c < k) { int a = 1 + (int)(rnd() % h); if (!in[a]) { in[a] = 1; c++; } }
        }
        int ni = 0, no = 0;
        for (int a = 1; a <= h; a++) { if (in[a]) IN[ni++] = a; else OUT[no++] = a; }
        for (int g = 0; g < h; g++) { double s = 0; for (int i = 0; i < k; i++) s += V[(size_t)IN[i] * h + g]; F[g] = s; }
        double curK = -1e300; for (int g = 0; g < h; g++) if (-F[g] > curK) curK = -F[g];
        double cur = softobj(F, h, b, curK);
        if (curK < bestK - 1e-12) { /* record the seed itself (matters for the Paley seed, mode 2) */
            bestK = curK; memcpy(best, in, sizeof(int) * (h + 1));
            double L = -1e300; for (int g = 0; g < h; g++) if (F[g] > L) L = F[g]; bestLam = L;
        }
        for (long it = 1; it <= steps; it++) {
            double bestc = 1e300; int bi = -1, bj = -1;
            for (int c = 0; c < C; c++) {
                int i = (int)(rnd() % k), j = (int)(rnd() % (h - k)); int a = IN[i], bb = OUT[j];
                if (tabu[a] > it || tabu[bb] > it) continue;
                const double *va = V + (size_t)a * h, *vb = V + (size_t)bb * h; double mx = -1e300;
                for (int g = 0; g < h; g++) { double y = -(F[g] - va[g] + vb[g]); if (y > mx) mx = y; }
                double s = 0; for (int g = 0; g < h; g++) s += exp(b * (-(F[g] - va[g] + vb[g]) - mx));
                double o = mx + log(s) / b;
                if (o < bestc) { bestc = o; bi = i; bj = j; }
            }
            if (bi < 0) continue;
            /* accept the best sampled move (tabu search: also uphill), but with a mild annealing gate */
            if (bestc <= cur || urand() < exp((cur - bestc) * b * 4.0)) {
                int a = IN[bi], bb = OUT[bj]; const double *va = V + (size_t)a * h, *vb = V + (size_t)bb * h;
                double mK = -1e300;
                for (int g = 0; g < h; g++) { F[g] += vb[g] - va[g]; if (-F[g] > mK) mK = -F[g]; }
                IN[bi] = bb; OUT[bj] = a; in[a] = 0; in[bb] = 1; tabu[a] = it + tenure; tabu[bb] = it + tenure;
                cur = bestc; curK = mK;
                if (curK < bestK - 1e-12) {
                    bestK = curK; memcpy(best, in, sizeof(int) * (h + 1));
                    double L = -1e300; for (int g = 0; g < h; g++) if (F[g] > L) L = F[g]; bestLam = L;
                }
            }
        }
    }
    printf("q=%d k=%d mode=%d beta=%.2f bestK=%.6f K/sqrtq=%.5f Lambda=%.3f Lambda/q=%.4f LambdaK/q=%.4f paley/sqrtq=%.5f P=",
           q, k, mode, beta, bestK, bestK / sqrt(q), bestLam, bestLam / q, bestLam * bestK / q, (1 + sqrt(q)) / 2 / sqrt(q));
    for (int a = 1; a <= h; a++) if (best[a]) printf("%d ", a);
    printf("\n");
    return 0;
}
