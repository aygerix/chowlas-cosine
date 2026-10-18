/* signed_tabu.c — tabu search (HEURISTIC) over signed sets (D, eps): minimise the rigorous naive bound
 *   Rn = (k + W_s) / (2 lam sqrt|A|),  A = {g>0: c(g) = lam},  W_s = sum_{c(g) ∉ {0,lam}} 2|c(g)|,
 * c(g) = sum_{u-v=g} eps_u eps_v.  D ⊂ [0,L], 0 and L fixed in D (their signs may flip, eps(0) = +1 fixed).
 * Moves: move point i (i >= 2) to a free y with sign ±1, or flip the sign of point i >= 1.  Best non-tabu move.
 * Optional: unsigned mode (all signs +, no flips) for comparison: pass mode=0.
 * Usage: signed_tabu lam k L iters seed mode(1 signed, 0 unsigned) [tenure] [stall]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static int lam, k, L, *D, *Es, *inD, *c, *tabu, G, Wd;
static inline int cost(int x) { return (x == 0 || x == lam) ? 0 : 2 * abs(x); }
static inline void upd(int g, int dv) { int o = c[g], n = o + dv; if (o == lam) G--; if (n == lam) G++; Wd += cost(n) - cost(o); c[g] = n; }
static void pt(int i, int x, int e, int sg) { for (int j = 0; j < k; j++) if (j != i) upd(abs(D[j] - x), sg * e * Es[j]); }
static double obj(int g, int w) { return g > 0 ? (double)(k + w) * (k + w) / g : 1e18; }

int main(int argc, char **argv) {
    lam = atoi(argv[1]); k = atoi(argv[2]); L = atoi(argv[3]); long iters = atol(argv[4]);
    rs = 0x9E3779B97F4A7C15ULL ^ ((uint64_t)atol(argv[5]) * 0x2545F4914F6CDD1DULL); int mode = atoi(argv[6]);
    int tenure = argc > 7 ? atoi(argv[7]) : 7, stall = argc > 8 ? atoi(argv[8]) : 2000;
    D = malloc(sizeof(int) * k); Es = malloc(sizeof(int) * k); inD = calloc(L + 1, sizeof(int));
    c = calloc(L + 1, sizeof(int)); tabu = calloc(2 * (L + 1), sizeof(int));
    int *bD = malloc(sizeof(int) * k), *bE = malloc(sizeof(int) * k);
    D[0] = 0; D[1] = L; inD[0] = inD[L] = 1;
    for (int i = 2; i < k; i++) { int x; do x = 1 + (int)(rnd() % (L - 1)); while (inD[x]); D[i] = x; inD[x] = 1; }
    for (int i = 0; i < k; i++) Es[i] = (mode && i > 0 && (rnd() % 5 == 0)) ? -1 : 1;
    for (int i = 0; i < k; i++) for (int j = 0; j < i; j++) upd(abs(D[i] - D[j]), Es[i] * Es[j]);
    double cur = obj(G, Wd), best = cur; int bG = G, bW = Wd; memcpy(bD, D, sizeof(int) * k); memcpy(bE, Es, sizeof(int) * k);
    long lastimp = 0;
    for (long it = 1; it <= iters; it++) {
        int bi = -1, by = -1, be = 0, nb = 0; double bo = 1e300;
        for (int i = 1; i < k; i++) {
            /* sign flip of point i */
            if (mode) {
                int o = D[i], e = Es[i];
                pt(i, o, e, -1); pt(i, o, -e, +1);
                double v = obj(G, Wd);
                pt(i, o, -e, -1); pt(i, o, e, +1);
                int ok = tabu[2 * o + (-e < 0 ? 0 : 1)] < it || v < best - 1e-12;
                if (ok && (v < bo - 1e-12 || (fabs(v - bo) < 1e-12 && rnd() % (++nb) == 0))) { if (v < bo - 1e-12) nb = 1; bo = v; bi = i; by = o; be = -e; }
            }
            if (i < 2) continue;
            for (int y = 1; y < L; y++) {
                if (inD[y]) continue;
                for (int e = -1; e <= 1; e += 2) {
                    if (!mode && e < 0) continue;
                    int o = D[i], eo = Es[i];
                    pt(i, o, eo, -1); D[i] = y; Es[i] = e; pt(i, y, e, +1);
                    double v = obj(G, Wd);
                    pt(i, y, e, -1); D[i] = o; Es[i] = eo; pt(i, o, eo, +1);
                    int ok = tabu[2 * y + (e < 0 ? 0 : 1)] < it || v < best - 1e-12;
                    if (ok && (v < bo - 1e-12 || (fabs(v - bo) < 1e-12 && rnd() % (++nb) == 0))) { if (v < bo - 1e-12) nb = 1; bo = v; bi = i; by = y; be = e; }
                }
            }
        }
        if (bi < 0) continue;
        int o = D[bi], eo = Es[bi];
        pt(bi, o, eo, -1); inD[o] = 0; D[bi] = by; Es[bi] = be; inD[by] = 1; pt(bi, by, be, +1);
        tabu[2 * o + (eo < 0 ? 0 : 1)] = it + tenure + (int)(rnd() % 3);
        cur = obj(G, Wd);
        if (cur < best - 1e-12) { best = cur; bG = G; bW = Wd; memcpy(bD, D, sizeof(int) * k); memcpy(bE, Es, sizeof(int) * k); lastimp = it; }
        if (it - lastimp > stall) {
            for (int t = 0; t < 2; t++) {
                int i = 2 + (int)(rnd() % (k - 2)), y; do y = 1 + (int)(rnd() % (L - 1)); while (inD[y]);
                int oo = D[i], ee = Es[i]; pt(i, oo, ee, -1); inD[oo] = 0; D[i] = y; inD[y] = 1;
                if (mode && rnd() % 4 == 0) Es[i] = -ee;
                pt(i, y, Es[i], +1);
            }
            cur = obj(G, Wd); lastimp = it;
        }
    }
    int neg = 0; for (int i = 0; i < k; i++) neg += bE[i] < 0;
    printf("lam=%d k=%d L=%d mode=%s Rn=%.4f |A|=%d W_s=%d W_s/k=%.3f neg=%d D=", lam, k, L, mode ? "signed" : "unsigned",
           sqrt(best) / (2.0 * lam), bG, bW, (double)bW / k, neg);
    int idx[256]; for (int i = 0; i < k; i++) idx[i] = i;
    for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (bD[idx[j]] < bD[idx[i]]) { int t = idx[i]; idx[i] = idx[j]; idx[j] = t; }
    for (int i = 0; i < k; i++) printf("%s%d%c", bE[idx[i]] < 0 ? "-" : "", bD[idx[i]], i + 1 < k ? ',' : '\n');
    return 0;
}
