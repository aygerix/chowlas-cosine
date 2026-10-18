/* coretail.c -- complete branch-and-bound over the structured class
 *     C(X, N, Y, h) = { A subset [1,X] : |A| = N, |[1,Y] \ A| <= h }      (core [1,Y] with at most h holes, free tail)
 * minimising M(A) = -min_x sum_{a in A} cos(a x).   (agent "construct", 2026-10-18)
 *
 * Outer loop: every hole set H subset [hmin, Y], |H| <= h (lexicographic; pattern c handled iff c % npart == part).
 * Inner loop: DFS over tails T subset (Y, X], |T| = N - Y + |H|, elements in increasing order, with the valid prune
 *     exists j : g_S(x_j) + U_j(k, i) < -thr,   U_j(k, i) = sum of the k largest cos(a x_j) over tail positions >= i,
 * on the grid x_j = pi j / G (grid values are actual values of f, so a pruned node has no completion with M <= thr).
 * Leaves with grid M < thr are re-evaluated by Newton polishing from the lowest grid local minima ("true" M, float);
 * thr is lowered to the best true M found (branch and bound).  So the final best is the class optimum up to float
 * error of the Newton evaluation (NUMERICAL-EXACT, not interval-certified); certify the output set with arb separately.
 *
 * usage: coretail X N Y h thr0 G npart part [hmin]
 * output: "IMPROVE M R H=[..] A=[..]" lines, then "DONE ..." with node counts.
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static int X, N, Y, H, G, GP, m;             /* m = number of tail positions = X - Y */
static double *C;                            /* C[a*GP + j] = cos(pi a j / G) */
static double *U;                            /* U[(k*(m+1) + i)*GP + j] */
static double *lev;                          /* (kmax+2) * GP partial sums */
static double thr;
static int cur[512], ncur, holes[64], nholes, kmax;
static long long nodes = 0, leaves = 0, newton = 0;
static int hint[512];
static double t0;
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

static double true_min_of(const double *g, int *Aset, int na) {
    /* Newton from the lowest grid local minima within 0.3 of the grid minimum */
    double gmin = 1e300; for (int j = 0; j < GP; j++) if (g[j] < gmin) gmin = g[j];
    double best = gmin;
    for (int j = 0; j < GP; j++) {
        double l = j ? g[j - 1] : g[1], r = j < G ? g[j + 1] : g[G - 1];
        if (g[j] > l || g[j] > r || g[j] > gmin + 0.3) continue;
        double x = M_PI * j / G;
        for (int it = 0; it < 40; it++) {
            double d1 = 0, d2 = 0;
            for (int q = 0; q < na; q++) { double a = Aset[q]; d1 -= a * sin(a * x); d2 -= a * a * cos(a * x); }
            if (d2 <= 0) break;
            double st = d1 / d2; x -= st; if (fabs(st) < 1e-14) break;
        }
        double v = 0; for (int q = 0; q < na; q++) v += cos(Aset[q] * x);
        if (v < best) best = v;
    }
    newton++;
    return best;
}

static void leaf(const double *g) {
    leaves++;
    int Aset[1024], na = 0, hi = 0;
    for (int n = 1; n <= Y; n++) { if (hi < nholes && holes[hi] == n) { hi++; continue; } Aset[na++] = n; }
    for (int q = 0; q < ncur; q++) Aset[na++] = Y + 1 + cur[q];
    double tm = true_min_of(g, Aset, na);
    if (-tm < thr) {
        thr = -tm;
        printf("IMPROVE M=%.7f R=%.7f t=%.1f H=[", -tm, -tm / sqrt(N), now() - t0);
        for (int q = 0; q < nholes; q++) printf("%d%s", holes[q], q + 1 < nholes ? "," : "");
        printf("] A=[");
        for (int q = 0; q < na; q++) printf("%d%s", Aset[q], q + 1 < na ? "," : "");
        printf("]\n"); fflush(stdout);
    }
}

static void dfs(int depth, int k, int i) {
    /* choose k more tail positions from index >= i; partial sums at lev[depth] */
    const double *gS = lev + (size_t)depth * GP; double *ng = lev + (size_t)(depth + 1) * GP;
    double nthr = -thr;
    for (int p = i; p <= m - k; p++) {
        const double *Ca = C + (size_t)(Y + 1 + p) * GP;
        const double *Up = U + ((size_t)(k - 1) * (m + 1) + (p + 1)) * GP;
        nodes++;
        int h = hint[depth], pr = 0;
        if (gS[h] + Ca[h] + Up[h] < nthr) pr = 1;
        else for (int j = 0; j < GP; j++) { double v = gS[j] + Ca[j]; ng[j] = v; if (v + Up[j] < nthr) { pr = 1; hint[depth] = j; break; } }
        if (pr) continue;
        cur[ncur++] = p;
        if (k == 1) leaf(ng); else dfs(depth + 1, k - 1, p + 1);
        ncur--;
        nthr = -thr;    /* thr may have dropped */
    }
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: coretail X N Y h thr0 G npart part [hmin]\n"); return 2; }
    X = atoi(argv[1]); N = atoi(argv[2]); Y = atoi(argv[3]); H = atoi(argv[4]); thr = atof(argv[5]); G = atoi(argv[6]);
    int npart = atoi(argv[7]), part = atoi(argv[8]); int hmin = argc > 9 ? atoi(argv[9]) : 1;
    if (G <= 0) G = 12 * X; GP = G + 1; m = X - Y; kmax = N - Y + H; if (kmax > m) kmax = m;
    t0 = now();
    C = malloc(sizeof(double) * (size_t)(X + 1) * GP);
    for (int a = 0; a <= X; a++) for (int j = 0; j < GP; j++) C[(size_t)a * GP + j] = cos(M_PI * (double)((long)a * j % (2L * G)) / G);
    U = calloc((size_t)(kmax + 1) * (m + 1) * GP, sizeof(double));
    double *vals = malloc(sizeof(double) * (m + 1));
    for (int j = 0; j < GP; j++) {
        for (int i = m; i >= 0; i--) {
            /* positions i..m-1 (tail index p <-> frequency Y+1+p); sorted descending insertion */
            int cnt = m - i;
            for (int q = 0; q < cnt; q++) vals[q] = C[(size_t)(Y + 1 + i + q) * GP + j];
            /* partial sort: simple insertion sort (m <= ~60) */
            for (int a = 1; a < cnt; a++) { double v = vals[a]; int b = a - 1; while (b >= 0 && vals[b] < v) { vals[b + 1] = vals[b]; b--; } vals[b + 1] = v; }
            double s = 0;
            for (int k = 0; k <= kmax; k++) { if (k > 0) { if (k <= cnt) s += vals[k - 1]; else s -= 1e9; }
                U[((size_t)k * (m + 1) + i) * GP + j] = s; }
        }
    }
    lev = malloc(sizeof(double) * (size_t)(kmax + 2) * GP);
    double *core = calloc(GP, sizeof(double));
    for (int n = 1; n <= Y; n++) for (int j = 0; j < GP; j++) core[j] += C[(size_t)n * GP + j];
    long long pat = 0, patdone = 0, patroot = 0;
    int idx[64];
    for (int hs = 0; hs <= H; hs++) {
        int t = N - Y + hs; if (t < 0 || t > m) continue;
        for (int q = 0; q < hs; q++) idx[q] = hmin + q;
        if (hs > 0 && idx[hs - 1] > Y) continue;
        while (1) {
            if (pat++ % npart == part) {
                patdone++;
                nholes = hs; for (int q = 0; q < hs; q++) holes[q] = idx[q];
                double *g0 = lev; memcpy(g0, core, sizeof(double) * GP);
                for (int q = 0; q < hs; q++) for (int j = 0; j < GP; j++) g0[j] -= C[(size_t)holes[q] * GP + j];
                int ok = 1; const double *Ut = U + ((size_t)t * (m + 1) + 0) * GP;
                for (int j = 0; j < GP; j++) if (g0[j] + Ut[j] < -thr) { ok = 0; break; }
                if (ok) { patroot++; ncur = 0; if (t == 0) leaf(g0); else dfs(0, t, 0); }
            }
            /* next combination of size hs from [hmin, Y] */
            if (hs == 0) break;
            int q = hs - 1; while (q >= 0 && idx[q] == Y - (hs - 1 - q)) q--;
            if (q < 0) break;
            idx[q]++; for (int r = q + 1; r < hs; r++) idx[r] = idx[r - 1] + 1;
        }
    }
    printf("DONE X=%d N=%d Y=%d h=%d G=%d part=%d/%d patterns=%lld rootpass=%lld nodes=%lld leaves=%lld best_M=%.7f R=%.7f t=%.1f\n",
           X, N, Y, H, G, part, npart, patdone, patroot, nodes, leaves, thr, thr / sqrt(N), now() - t0);
    return 0;
}
