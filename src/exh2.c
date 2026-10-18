/* exh2.c — complete enumeration of N-subsets A of [1,L] with M_grid(A) <= thr (lead, 2026-10-18).
 *
 * Same contract as exh_run in src/smallN_search.py (grid x_j = pi j / H, j = 0..H; every A with M(A) <= thr survives,
 * since M_grid <= M), plus a stronger valid prune: for any probability vector w on grid points,
 *     min_j f_A(x_j) <= sum_j w_j f_A(x_j),
 * so a node (partial set S, last element, k elements still to choose from (last, L]) can be pruned when
 *     sum_j w_j g_S(x_j) + topk_{b in (last,L]} ( sum_j w_j cos(b x_j) ) < -thr.
 * w = delta_j is the old single-point test; we add w = (delta_j + delta_{j+d})/2 for d in a small offset list.
 * Because topk of an average <= average of topks, pair tests prune nodes no single point prunes.
 * Completeness up to floating-point rounding of the sums (~1e-13, far below margins). Survivors are re-checked on a
 * fine grid H2 and printed for accurate evaluation.
 * Threads: every thread walks the same top tree down to depth P (cheap, replicated); the i-th node at depth P (in DFS
 * order) is expanded by whichever thread claimed index i from a shared atomic counter, so load is balanced.
 * Build: cc -O3 -march=native -o src/.build/exh2 src/exh2.c -lm -lpthread
 * Usage: exh2 N L thr H H2 threads d1,d2,... [P [W]]   (offsets "0" = single-point only; P = split depth,
 *        default 12; W = window half-width around the tightest grid point for pair tests, default 0)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#include <pthread.h>
#include <stdatomic.h>

static int N, L, H, H2, Hp, ND, D[16];
static double thr;
static double *C;    /* C[a*Hp + j] */
static double *U;    /* U[(k*(L+1)+last)*Hp + j]: sum of k largest C[b][j], b in (last, L] */
static double *U2;   /* U2[((dd*(N+1)+k)*(L+1)+last)*Hp + j]: topk of (C[b][j]+C[b][j+D[dd]])/2 */
static int P = 12, W = 0, SEP = 4, KMAX = 0, NLAM = 3;
static double LAM[8] = {0.5, 0.3, 0.7};   /* W: extra window around the tightest point for pair tests */
static atomic_llong claim_ctr = 0;
static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
static int64_t tot_nodes = 0, tot_leaves = 0, tot_surv = 0;

typedef struct { int cur[64]; double *lev; int hint[64]; int64_t nodes, leaves; long long idx, my; } th_t;

static double fine_min(const int *cur) {
    double mn = 1e300;
    for (int j = 0; j <= H2; j++) {
        double x = M_PI * (double)j / (double)H2, s = 0;
        for (int i = 0; i < N; i++) s += cos((double)cur[i] * x);
        if (s < mn) mn = s;
    }
    return mn;
}

static void report(const int *cur, double fm) {
    pthread_mutex_lock(&mtx);
    tot_surv++;
    printf("S %.12f", -fm);
    for (int i = 0; i < N; i++) printf(" %d", cur[i]);
    printf("\n"); fflush(stdout);
    pthread_mutex_unlock(&mtx);
}

static void topk_table(double *dst, const double *val /* val[b*Hp+j], b=1..L */, int jmax) {
    /* dst[(k*(L+1)+last)*Hp + j] for k = 0..N, last = 0..L, j = 0..jmax-1 */
    double *v = malloc(sizeof(double) * (L + 1));
    for (int j = 0; j < jmax; j++) {
        int cnt = 0;
        for (int last = L; last >= 0; last--) {
            double s = 0;
            for (int k = 0; k <= N; k++) {
                if (k > 0) s = (k <= cnt) ? s + v[k - 1] : 1e300;
                dst[((size_t)k * (L + 1) + last) * Hp + j] = s;
            }
            if (last >= 1) {
                double x = val[(size_t)last * Hp + j];
                int p = cnt; while (p > 0 && v[p - 1] < x) { v[p] = v[p - 1]; p--; }
                v[p] = x; cnt++;
            }
        }
    }
    free(v);
}

static void dfs(th_t *t, int depth, int last) {
    int k = N - depth;
    const double *gS = t->lev + (size_t)depth * Hp;
    double *ng = t->lev + (size_t)(depth + 1) * Hp;
    double nthr = -thr;
    for (int a = last + 1; a <= L - k + 1; a++) {
        const double *Ca = C + (size_t)a * Hp;
        const double *Ua = U + ((size_t)(k - 1) * (L + 1) + a) * Hp;
        t->nodes++;
        int h = t->hint[depth];
        if (gS[h] + Ca[h] + Ua[h] < nthr) continue;
        int pruned = 0, jm = 0, jm2 = -1; double sm = 1e300, sm2 = 1e300;
        if (KMAX == 0) {                            /* fast path: blocks of 8, one branch per block (vectorizes) */
            int j = 0;
            for (; j + 8 <= Hp; j += 8) {
                double mn = 1e300;
                for (int q = 0; q < 8; q++) { double v = gS[j + q] + Ca[j + q]; ng[j + q] = v; double sl = v + Ua[j + q]; mn = sl < mn ? sl : mn; }
                if (mn < nthr) { pruned = 1; for (int q = 0; q < 8; q++) if (ng[j + q] + Ua[j + q] < nthr) { t->hint[depth] = j + q; break; } break; }
            }
            if (!pruned) for (; j < Hp; j++) { double v = gS[j] + Ca[j]; ng[j] = v; if (v + Ua[j] < nthr) { pruned = 1; t->hint[depth] = j; break; } }
        } else
        for (int j = 0; j < Hp; j++) {
            double v = gS[j] + Ca[j];
            ng[j] = v;
            double sl = v + Ua[j];
            if (sl < nthr) { pruned = 1; t->hint[depth] = j; break; }
            if (sl < sm) { if (j - jm >= SEP || jm - j >= SEP) { sm2 = sm; jm2 = jm; } sm = sl; jm = j; }
            else if (sl < sm2 && (j - jm >= SEP || jm - j >= SEP)) { sm2 = sl; jm2 = j; }
        }
        if (pruned) continue;
        if (k > 1 && k - 1 <= KMAX && jm2 >= 0) {   /* coupled test at the two tightest separated grid points */
            int kk = k - 1;
            const double *c1 = C + jm, *c2 = C + jm2;
            for (int li = 0; li < NLAM && !pruned; li++) {
                double lam = LAM[li], top[64]; int cnt = 0;
                for (int b = a + 1; b <= L; b++) {
                    double v = lam * c1[(size_t)b * Hp] + (1 - lam) * c2[(size_t)b * Hp];
                    if (cnt < kk) { int q = cnt++; while (q > 0 && top[q - 1] < v) { top[q] = top[q - 1]; q--; } top[q] = v; }
                    else if (v > top[kk - 1]) { int q = kk - 1; while (q > 0 && top[q - 1] < v) { top[q] = top[q - 1]; q--; } top[q] = v; }
                }
                double sum = lam * ng[jm] + (1 - lam) * ng[jm2];
                for (int q = 0; q < kk; q++) sum += top[q];
                if (sum < nthr) pruned = 1;
            }
            if (pruned) continue;
        }
        if (k > 1 && ND) {                          /* pair tests around the tightest single point (and a window) */
            for (int dd = 0; dd < ND && !pruned; dd++) {
                int d = D[dd];
                const double *U2a = U2 + (((size_t)dd * (N + 1) + (k - 1)) * (L + 1) + a) * Hp;
                int j0 = jm - d - W, j1 = jm + W;
                if (j0 < 0) j0 = 0;
                if (j1 + d >= Hp) j1 = Hp - 1 - d;
                for (int j = j0; j <= j1; j++)
                    if (0.5 * (ng[j] + ng[j + d]) + U2a[j] < nthr) { pruned = 1; break; }
            }
            if (pruned) continue;
        }
        t->cur[depth] = a;
        if (depth + 1 == P && k > 1) {              /* node at split depth: expand only if claimed */
            long long i = t->idx++;
            if (i != t->my) continue;
            t->my = atomic_fetch_add(&claim_ctr, 1);
        }
        if (k == 1) {
            t->leaves++;
            double fm = fine_min(t->cur);
            if (fm >= nthr) report(t->cur, fm);
        } else dfs(t, depth + 1, a);
    }
}

static void *worker(void *arg) {
    (void)arg;
    th_t *t = calloc(1, sizeof(th_t));
    t->lev = calloc((size_t)(N + 1) * Hp, sizeof(double));
    for (int i = 0; i < 64; i++) t->hint[i] = Hp - 1;
    t->idx = 0; t->my = atomic_fetch_add(&claim_ctr, 1);
    dfs(t, 0, 0);
    pthread_mutex_lock(&mtx); tot_nodes += t->nodes; tot_leaves += t->leaves; pthread_mutex_unlock(&mtx);
    free(t->lev); free(t);
    return NULL;
}

int main(int argc, char **argv) {
    if (argc < 8) { fprintf(stderr, "usage: exh2 N L thr H H2 threads d1,d2,..\n"); return 2; }
    N = atoi(argv[1]); L = atoi(argv[2]); thr = atof(argv[3]); H = atoi(argv[4]); H2 = atoi(argv[5]);
    int nth = atoi(argv[6]); Hp = H + 1;
    ND = 0; for (char *s = strtok(argv[7], ","); s; s = strtok(NULL, ",")) { int d = atoi(s); if (d > 0) D[ND++] = d; }
    C = malloc(sizeof(double) * (size_t)(L + 1) * Hp);
    for (int a = 0; a <= L; a++) for (int j = 0; j < Hp; j++) C[(size_t)a * Hp + j] = cos(M_PI * (double)a * j / H);
    U = malloc(sizeof(double) * (size_t)(N + 1) * (L + 1) * Hp);
    topk_table(U, C, Hp);
    U2 = malloc(sizeof(double) * (size_t)(ND ? ND : 1) * (N + 1) * (L + 1) * Hp);
    double *val = malloc(sizeof(double) * (size_t)(L + 1) * Hp);
    for (int dd = 0; dd < ND; dd++) {
        int d = D[dd];
        for (int b = 0; b <= L; b++) for (int j = 0; j < Hp; j++)
            val[(size_t)b * Hp + j] = (j + d < Hp) ? 0.5 * (C[(size_t)b * Hp + j] + C[(size_t)b * Hp + j + d]) : 0;
        topk_table(U2 + (size_t)dd * (N + 1) * (L + 1) * Hp, val, Hp - d);
    }
    free(val);
    if (argc > 8) P = atoi(argv[8]);
    if (argc > 9) W = atoi(argv[9]);
    if (argc > 10) KMAX = atoi(argv[10]);
    if (argc > 11) SEP = atoi(argv[11]);
    if (P >= N) P = N - 1;
    if (P < 1) P = 1;
    pthread_t th[64];
    for (int i = 0; i < nth; i++) pthread_create(&th[i], NULL, worker, NULL);
    for (int i = 0; i < nth; i++) pthread_join(th[i], NULL);
    printf("STATS nodes=%lld leaves=%lld survivors=%lld\n", (long long)tot_nodes, (long long)tot_leaves, (long long)tot_surv);
    return 0;
}
