/* e39_lam_exact.c — lead's independent exact check of the agent's λ-ruler optima (E39).
 * Minimum defect def = Σ_{d>0: r(d) ∉ {0,λ}} r(d) over D ⊂ [0,L], |D| = k, 0 and L in D (span exactly L).
 * Plain DFS, interior points increasing, incremental r(d); only prune: Σ_{r(d) > λ} r(d) >= best (r never decreases).
 * Reflection D -> L - D broken by x[1] <= L - x[k-2]. Usage: e39_lam_exact lambda k Lmin Lmax  (prints min def per L) */
#include <stdio.h>
#include <stdlib.h>
static int lam, k, L, x[64], r[512], over, best;
static void add(int v, int s) {           /* add/remove point v against x[0..m-1] handled by caller */ (void)v; (void)s; }
static inline void bump(int d, int s) {
    int o = r[d];
    if (o > lam) over -= o;
    r[d] = o + s;
    if (o + s > lam) over += o + s;
}
static void dfs(int m) {                  /* m points placed: x[0..m-1]; x[m-1] < L except when m == k */
    if (over >= best) return;
    if (m == k - 1) {                     /* place L */
        for (int i = 0; i < m; i++) bump(L - x[i], 1);
        if (over < best && x[1] <= L - x[k - 2]) {
            int def = 0;
            for (int d = 1; d <= L; d++) if (r[d] && r[d] != lam) def += r[d];
            if (def < best) best = def;
        }
        for (int i = 0; i < m; i++) bump(L - x[i], -1);
        return;
    }
    int lo = x[m - 1] + 1, hi = L - (k - 1 - m);
    for (int v = lo; v <= hi; v++) {
        for (int i = 0; i < m; i++) bump(v - x[i], 1);
        x[m] = v; dfs(m + 1);
        for (int i = 0; i < m; i++) bump(v - x[i], -1);
    }
}
int main(int argc, char **argv) {
    lam = atoi(argv[1]); k = atoi(argv[2]); int Lmin = atoi(argv[3]), Lmax = atoi(argv[4]);
    int overall = 1 << 30, argL = -1;
    for (L = Lmin; L <= Lmax; L++) {
        for (int d = 0; d < 512; d++) r[d] = 0; over = 0; best = 1 << 30; x[0] = 0;
        dfs(1);
        printf("lam=%d k=%d L=%d mindef=%d\n", lam, k, L, best); fflush(stdout);
        if (best < overall) { overall = best; argL = L; }
    }
    printf("RESULT lam=%d k=%d L<=%d mindef=%d at L=%d\n", lam, k, Lmax, overall, argL);
    return 0;
}
