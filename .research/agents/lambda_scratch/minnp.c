/* minnp.c — exhaustive minimum over D ⊂ [0,L], 0,L ∈ D, |D| = k of
 *   n_p(D) = #{d != 0 : r_D(d) != 0 mod p}  (two-sided count)   and   W_p(D) = sum_{d>0, p ∤ r(d)} 2 r(d).
 * W >= W_p >= n_p for every lambda divisible by p (defects include every d with p ∤ r(d)).
 * Usage: minnp p k Lmax     prints for each L <= Lmax the min n_p, min W_p and argmin D (exhaustive DFS).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int p, k, L, D[64], s, r[1024];
static int bestn, bestw, bD[64], bDw[64];
static void addpt(int x, int sg) { for (int i = 0; i < s; i++) r[abs(x - D[i])] += sg; }
static void leaf(void) {
    int n = 0, w = 0;
    for (int d = 1; d <= L; d++) if (r[d] % p) { n += 2; w += 2 * r[d]; }
    if (n < bestn) { bestn = n; memcpy(bD, D, sizeof(int) * k); }
    if (w < bestw) { bestw = w; memcpy(bDw, D, sizeof(int) * k); }
}
static void dfs(int xc) {
    int m = k - s;
    if (m == 0) { leaf(); return; }
    for (int x = xc + 1; x <= L - m; x++) { addpt(x, 1); D[s++] = x; dfs(x); s--; addpt(x, -1); }
}
static void pr(int *A) {
    int t[64]; memcpy(t, A, sizeof(int) * k);
    for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (t[j] < t[i]) { int u = t[i]; t[i] = t[j]; t[j] = u; }
    for (int i = 0; i < k; i++) printf("%d%c", t[i], i + 1 < k ? ',' : ' ');
}
int main(int argc, char **argv) {
    p = atoi(argv[1]); k = atoi(argv[2]); int Lmax = atoi(argv[3]);
    int gn = 1 << 30, gw = 1 << 30;
    for (L = k - 1; L <= Lmax; L++) {
        memset(r, 0, sizeof r); bestn = bestw = 1 << 30;
        D[0] = 0; s = 1; addpt(L, 1); D[1] = L; s = 2;
        if (k == 2) { leaf(); } else dfs(0);
        if (bestn < gn) gn = bestn;
        if (bestw < gw) gw = bestw;
        printf("p=%d k=%d L=%d min_np=%d min_Wp=%d  (running: %d %d)  argmin_np=", p, k, L, bestn, bestw, gn, gw);
        pr(bD); printf(" argmin_Wp="); pr(bDw); printf("\n"); fflush(stdout);
    }
    return 0;
}
