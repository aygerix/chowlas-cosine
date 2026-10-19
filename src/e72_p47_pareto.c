/* e72_p47_pareto.c — E72: can a dense set escape the whole P47 high-pass window family AND have small R?
 * Anneal A ⊂ [1, X], |A| = n, minimising  J = B(A)/sqrt(n) + mu * R_grid(A), where
 *   B(A) = max over h in HL, theta in TL of  sqrt(max(0, W E_h - rho(L+1) S_{h,w}) / (2(rho(L+1) - W))) + |r_0^h|/2,
 *   r^h = a^ev - kt_h * a^ev (even extension, a_0 = 0), E_h = sum_{j>=1} (r^h_j)^2, S_{h,w} = sum_{j<=w} kappa_w(j)^2 (r^h_j)^2,
 *   L = X + h + w, rho = 0.687 (numerical), h = 0 means r = a (P31).
 * B(A) is a (numerical-rho) lower bound for M(A) (P47 reformulated, NOTEBOOK 2026-10-19 night). R_grid uses a grid of 8X+1
 * points on [0, pi]. Swap moves; r^h, E_h, S_{h,w}, r_0^h and the grid values are updated incrementally.
 * HEURISTIC search; prints JSON per restart.
 * Usage: e72_p47_pareto X n mu iters restarts seed
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
static int cmpi(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }

#define NH 13
#define NT 7
static const int HL[NH] = {0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64};
static const double TL[NT] = {0.1, 0.2, 0.3, 0.45, 0.6, 0.8, 1.0};
static int X, n, G, nh;
static double rho = 0.687;
static double *kt[NH];          /* kt[i][k], k = 0..h : (1 - k/(h+1))/(h+1) */
static double *r[NH];           /* r[i][j], j = 0..X+h */
static double E[NH], S[NH][NT], WW[NT]; static int w_[NT];
static double *kw2[NT];         /* kappa_w(j)^2, j = 1..w */
static float *ctab; static double *f, *g;
static int *a;

static double kern(int i, int k) { int h = HL[i]; k = k < 0 ? -k : k; return k > h ? 0.0 : kt[i][k]; }

/* change a[u] by d (u >= 1): update r[i][j] for affected j >= 0 (even extension: a_{-u} also changes) */
static void upd(int u, int d) {
    for (int i = 0; i < nh; i++) {
        int h = HL[i];
        int lo = u - h, hi = u + h;
        for (int j = (lo < 0 ? 0 : lo); j <= hi; j++) {
            double dr = (j == u ? d : 0) - d * (kern(i, j - u) + kern(i, j + u));
            if (j == 0) { r[i][0] += dr; continue; }
            double o = r[i][j], nw = o + dr; r[i][j] = nw; double dd = nw * nw - o * o; E[i] += dd;
            for (int t = 0; t < NT; t++) if (j <= w_[t]) S[i][t] += kw2[t][j] * dd;
        }
        /* reflected contribution j in [-u-h, -u+h] ∩ [0, ∞): j <= h - u */
        for (int j = 0; j <= h - u; j++) {
            if (j >= lo && j <= hi) continue; /* already handled (both terms included above) */
            double dr = -d * kern(i, j + u);
            if (j == 0) { r[i][0] += dr; continue; }
            double o = r[i][j], nw = o + dr; r[i][j] = nw; double dd = nw * nw - o * o; E[i] += dd;
            for (int t = 0; t < NT; t++) if (j <= w_[t]) S[i][t] += kw2[t][j] * dd;
        }
    }
}

static double bound(int *bi, int *bt) {
    double best = 0; *bi = *bt = 0;
    for (int i = 0; i < nh; i++) for (int t = 0; t < NT; t++) {
        double L = X + HL[i] + w_[t], num = WW[t] * E[i] - rho * (L + 1) * S[i][t], den = 2 * (rho * (L + 1) - WW[t]);
        double b = (num > 0 ? sqrt(num / den) : 0.0) + fabs(r[i][0]) / 2;
        if (b > best) { best = b; *bi = i; *bt = t; }
    }
    return best;
}
static double gridmin(const double *v) { double m = 1e300; for (int j = 0; j < G; j++) if (v[j] < m) m = v[j]; return -m; }

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: e72_p47_pareto X n mu iters restarts seed\n"); return 2; }
    X = atoi(argv[1]); n = atoi(argv[2]); double mu = atof(argv[3]); long iters = atol(argv[4]); int restarts = atoi(argv[5]);
    rs = strtoull(argv[6], 0, 10) * 2654435761ULL + 88172645463325252ULL;
    nh = 0; while (nh < NH && HL[nh] <= X / 2) nh++;
    for (int i = 0; i < nh; i++) { int h = HL[i]; kt[i] = malloc(sizeof(double) * (h + 1));
        for (int k = 0; k <= h; k++) kt[i][k] = (h == 0) ? 0.0 : (1.0 - (double)k / (h + 1)) / (h + 1);
        r[i] = malloc(sizeof(double) * (X + h + 2)); }
    for (int t = 0; t < NT; t++) { int w = (int)lround(TL[t] * X); if (w < 1) w = 1; w_[t] = w; kw2[t] = malloc(sizeof(double) * (w + 1));
        double s = 0; for (int j = 1; j <= w; j++) { double k = 1.0 - (double)j / (w + 1); kw2[t][j] = k * k; s += k * k; } WW[t] = 1 + 2 * s; }
    G = 8 * X + 1; ctab = malloc(sizeof(float) * (size_t)X * G); f = malloc(sizeof(double) * G); g = malloc(sizeof(double) * G);
    for (int m = 1; m <= X; m++) for (int j = 0; j < G; j++) ctab[(size_t)(m - 1) * G + j] = (float)cos(m * M_PI * j / (G - 1));
    a = malloc(sizeof(int) * (X + 1)); int *el = malloc(sizeof(int) * n), *out = malloc(sizeof(int) * X), *bestA = malloc(sizeof(int) * n);
    double sn = sqrt((double)n);
    for (int rr = 0; rr < restarts; rr++) {
        memset(a, 0, sizeof(int) * (X + 1)); memset(f, 0, sizeof(double) * G);
        for (int i = 0; i < nh; i++) { memset(r[i], 0, sizeof(double) * (X + HL[i] + 2)); E[i] = 0; for (int t = 0; t < NT; t++) S[i][t] = 0; }
        int c = 0; while (c < n) { int m = 1 + (int)(rnd() % X); if (!a[m]) { a[m] = 1; el[c++] = m; upd(m, 1);
            const float *tb = ctab + (size_t)(m - 1) * G; for (int j = 0; j < G; j++) f[j] += tb[j]; } }
        int no = 0; for (int m = 1; m <= X; m++) if (!a[m]) out[no++] = m;
        int bi, bt; double B = bound(&bi, &bt), M = gridmin(f), J = B / sn + mu * M / sn, bestJ = J;
        memcpy(bestA, el, sizeof(int) * n);
        double T0 = 0.05;
        for (long it = 0; it < iters; it++) {
            double T = T0 * pow(1e-3, (double)it / iters);
            int i = (int)(rnd() % n), o = (int)(rnd() % no); int u = el[i], v = out[o];
            a[u] = 0; upd(u, -1); a[v] = 1; upd(v, 1);
            const float *ta = ctab + (size_t)(u - 1) * G, *tb = ctab + (size_t)(v - 1) * G;
            for (int j = 0; j < G; j++) g[j] = f[j] - ta[j] + tb[j];
            double B2 = bound(&bi, &bt), M2 = gridmin(g), J2 = B2 / sn + mu * M2 / sn;
            if (J2 <= J || urand() < exp((J - J2) / T)) {
                double *tmp = f; f = g; g = tmp; el[i] = v; out[o] = u; J = J2;
                if (J < bestJ) { bestJ = J; memcpy(bestA, el, sizeof(int) * n); }
            } else { a[v] = 0; upd(v, -1); a[u] = 1; upd(u, 1); }
        }
        /* recompute for the best set from scratch */
        for (int m = 1; m <= X; m++) if (a[m]) { a[m] = 0; upd(m, -1); }
        memset(f, 0, sizeof(double) * G);
        for (int k = 0; k < n; k++) { int m = bestA[k]; a[m] = 1; upd(m, 1); const float *tb = ctab + (size_t)(m - 1) * G; for (int j = 0; j < G; j++) f[j] += tb[j]; }
        B = bound(&bi, &bt); M = gridmin(f);
        qsort(bestA, n, sizeof(int), cmpi);
        printf("{\"X\": %d, \"n\": %d, \"mu\": %g, \"iters\": %ld, \"restart\": %d, \"B_over_sqrtn\": %.6f, \"best_h\": %d, \"best_theta\": %g, \"grid_R\": %.6f, \"J\": %.6f, \"A\": [",
               X, n, mu, iters, rr, B / sn, HL[bi], TL[bt], M / sn, B / sn + mu * M / sn);
        for (int k = 0; k < n; k++) printf(k ? ", %d" : "%d", bestA[k]);
        printf("]}\n"); fflush(stdout);
        for (int m = 1; m <= X; m++) if (a[m]) { a[m] = 0; upd(m, -1); }
    }
    return 0;
}
