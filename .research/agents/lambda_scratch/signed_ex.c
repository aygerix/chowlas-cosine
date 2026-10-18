/* signed_ex.c — EXHAUSTIVE search over signed sets (D, eps), D ⊂ [0, L] with 0, L ∈ D, |D| = k, eps ∈ {±1}^D,
 * eps(0) = +1 (global sign flip leaves c unchanged).  c(g) = sum_{u - v = g} eps_u eps_v.
 *   A = {g > 0 : c(g) = lam},  defect classes: c(g) ∉ {0, lam},  W_s = sum_defect 2|c(g)|.
 * Identity: 2 lam f_A = |q|^2 - k - E, hence M(A) <= (k + W_s)/(2 lam) and R(A) <= Rn := (k + W_s)/(2 lam sqrt|A|).
 * For each L reports: min Rn over all signed sets, min Rn over unsigned (all +) sets, min W_s subject to
 * |A| >= Gmin (Gmin = argument), and the optimal sets.  Usage: signed_ex lam k Lmin Lmax Gmin
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int lam, k, L, Gmin, D[64], E[64], s, c[4096], G, Wd;
static double bestR, bestRu; static int bestW, bestWG;
static int bD[64], bE[64], bDu[64], bDw[64], bEw[64];
static inline int cost(int x) { return (x == 0 || x == lam) ? 0 : 2 * abs(x); }
static inline void upd(int g, int dv) {
    int o = c[g], n = o + dv;
    if (o == lam) G--; if (n == lam) G++;
    Wd += cost(n) - cost(o); c[g] = n;
}
static void addpt(int x, int e, int sg) { for (int i = 0; i < s; i++) upd(abs(x - D[i]), sg * e * E[i]); }
static void leaf(void) {
    if (G <= 0) return;
    double Rn = (k + Wd) / (2.0 * lam * sqrt((double)G));
    int allplus = 1; for (int i = 0; i < k; i++) if (E[i] < 0) { allplus = 0; break; }
    if (Rn < bestR - 1e-12) { bestR = Rn; memcpy(bD, D, sizeof D); memcpy(bE, E, sizeof E); }
    if (allplus && Rn < bestRu - 1e-12) { bestRu = Rn; memcpy(bDu, D, sizeof D); }
    if (G >= Gmin && (Wd < bestW || (Wd == bestW && G > bestWG))) { bestW = Wd; bestWG = G; memcpy(bDw, D, sizeof D); memcpy(bEw, E, sizeof E); }
}
static void dfs(int xc) {
    int m = k - s;
    if (m == 0) { leaf(); return; }
    for (int x = xc + 1; x <= L - m; x++)
        for (int e = -1; e <= 1; e += 2) {
            addpt(x, e, +1); D[s] = x; E[s] = e; s++;
            dfs(x);
            s--; addpt(x, e, -1);
        }
}
static void pr(int *A, int *S) {
    int idx[64]; for (int i = 0; i < k; i++) idx[i] = i;
    for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (A[idx[j]] < A[idx[i]]) { int t = idx[i]; idx[i] = idx[j]; idx[j] = t; }
    for (int i = 0; i < k; i++) printf("%s%d%s", (S && S[idx[i]] < 0) ? "-" : "", A[idx[i]], i + 1 < k ? "," : "");
}
int main(int argc, char **argv) {
    lam = atoi(argv[1]); k = atoi(argv[2]); int Lmin = atoi(argv[3]), Lmax = atoi(argv[4]); Gmin = atoi(argv[5]);
    double gR = 1e9, gRu = 1e9;
    for (L = Lmin; L <= Lmax; L++) {
        memset(c, 0, sizeof c); G = 0; Wd = 0; bestR = bestRu = 1e9; bestW = 1 << 30; bestWG = 0;
        D[0] = 0; E[0] = 1; s = 1;
        for (int e = -1; e <= 1; e += 2) {        /* sign of the endpoint L */
            addpt(L, e, +1); D[1] = L; E[1] = e; s = 2;
            dfs(0);
            s = 1; addpt(L, e, -1);
        }
        if (bestR < gR) gR = bestR; if (bestRu < gRu) gRu = bestRu;
        printf("lam=%d k=%d L=%d minRn_signed=%.4f minRn_unsigned=%.4f (running %.4f %.4f) minW_s[|A|>=%d]=%d(|A|=%d) argRn=",
               lam, k, L, bestR, bestRu, gR, gRu, Gmin, bestW, bestWG);
        pr(bD, bE); printf(" argRn_u="); pr(bDu, NULL); printf(" argW="); pr(bDw, bEw); printf("\n"); fflush(stdout);
    }
    return 0;
}
