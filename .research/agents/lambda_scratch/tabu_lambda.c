/* tabu_lambda.c — tabu search (HEURISTIC) minimising the defect-pair count
 *   def(D) = sum_{d >= 1, r(d) not in {0, lam}} r(d)          (W = 2 def, phi = 1 - def / C(k,2))
 * over D ⊂ [0, L] with 0, L ∈ D, |D| = k.  Full neighbourhood: move any interior point to any free position
 * (delta evaluated in O(k) per move via the incremental class counts), best non-tabu move (aspiration on new best),
 * random perturbation after `stall` non-improving iterations.  Prints the best D found.
 * Usage: tabu_lambda lam k L iters seed [tenure] [stall] [seedset a,b,c,...]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static int lam, k, L, *D, *inD, *r, *tabu;
static int cost(int x) { return (x == 0 || x == lam) ? 0 : x; }
static int total(void) { int t = 0; for (int d = 1; d <= L; d++) t += cost(r[d]); return t; }
static void place(int i, int x, int s) { for (int j = 0; j < k; j++) if (j != i) r[abs(D[j] - x)] += s; }

/* delta of moving point i from D[i] to y (y free) */
static int *tmpd;
static int delta(int i, int y) {
    int old = D[i], dl = 0, n = 0;
    /* removal of old pairs then addition of new pairs; classes may coincide, so do it exactly with a scratch list */
    for (int j = 0; j < k; j++) if (j != i) { int d = abs(D[j] - old); dl -= cost(r[d]); r[d]--; dl += cost(r[d]); tmpd[n++] = d; }
    for (int j = 0; j < k; j++) if (j != i) { int d = abs(D[j] - y); dl -= cost(r[d]); r[d]++; dl += cost(r[d]); }
    for (int j = 0; j < k; j++) if (j != i) { int d = abs(D[j] - y); r[d]--; }
    for (int t = 0; t < n; t++) r[tmpd[t]]++;
    return dl;
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: lam k L iters seed [tenure] [stall]\n"); return 2; }
    lam = atoi(argv[1]); k = atoi(argv[2]); L = atoi(argv[3]); long iters = atol(argv[4]);
    rs = 0x9E3779B97F4A7C15ULL ^ ((uint64_t)atol(argv[5]) * 0x2545F4914F6CDD1DULL); if (!rs) rs = 1;
    int tenure = argc > 6 ? atoi(argv[6]) : 7, stall = argc > 7 ? atoi(argv[7]) : 2000;
    D = malloc(sizeof(int) * k); inD = calloc(L + 1, sizeof(int)); r = calloc(L + 1, sizeof(int));
    tabu = calloc(L + 1, sizeof(int)); tmpd = malloc(sizeof(int) * k);
    int *bestD = malloc(sizeof(int) * k);
    D[0] = 0; D[1] = L; inD[0] = inD[L] = 1;
    if (argc > 8) {   /* seed set: comma-separated, must contain 0 and L and have k elements */
        int n = 2; char *p = argv[8];
        while (*p) { int x = (int)strtol(p, &p, 10); if (x > 0 && x < L && !inD[x] && n < k) { D[n++] = x; inD[x] = 1; } if (*p == ',') p++; }
        for (; n < k; n++) { int x; do x = 1 + (int)(rnd() % (L - 1)); while (inD[x]); D[n] = x; inD[x] = 1; }
    } else
    for (int i = 2; i < k; i++) { int x; do x = 1 + (int)(rnd() % (L - 1)); while (inD[x]); D[i] = x; inD[x] = 1; }
    for (int i = 0; i < k; i++) for (int j = 0; j < i; j++) r[abs(D[i] - D[j])]++;
    int cur = total(), best = cur; memcpy(bestD, D, sizeof(int) * k);
    long lastimp = 0;
    for (long it = 1; it <= iters; it++) {
        int bi = -1, by = -1, bd = 1 << 30, nb = 0;
        for (int i = 2; i < k; i++) for (int y = 1; y < L; y++) {
            if (inD[y]) continue;
            int dl = delta(i, y);
            int ok = (tabu[y] < it) || (cur + dl < best);
            if (!ok) continue;
            if (dl < bd) { bd = dl; bi = i; by = y; nb = 1; }
            else if (dl == bd && (rnd() % (++nb)) == 0) { bi = i; by = y; }
        }
        if (bi < 0) continue;
        int old = D[bi];
        place(bi, old, -1); inD[old] = 0; D[bi] = by; inD[by] = 1; place(bi, by, +1);
        tabu[old] = it + tenure + (int)(rnd() % 3);
        cur += bd;
        if (cur < best) { best = cur; memcpy(bestD, D, sizeof(int) * k); lastimp = it; }
        if (it - lastimp > stall) {   /* perturb: relocate 2 random interior points */
            for (int t = 0; t < 2; t++) {
                int i = 2 + (int)(rnd() % (k - 2)), y; do y = 1 + (int)(rnd() % (L - 1)); while (inD[y]);
                int o = D[i]; place(i, o, -1); inD[o] = 0; D[i] = y; inD[y] = 1; place(i, y, +1);
            }
            cur = total(); lastimp = it;
        }
    }
    int P = k * (k - 1) / 2;
    for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (bestD[j] < bestD[i]) { int t = bestD[i]; bestD[i] = bestD[j]; bestD[j] = t; }
    printf("lam=%d k=%d L=%d def=%d W/k=%.3f phi=%.4f D=", lam, k, L, best, 2.0 * best / k, 1.0 - (double)best / P);
    for (int i = 0; i < k; i++) printf("%d%c", bestD[i], i + 1 < k ? ',' : '\n');
    return 0;
}
