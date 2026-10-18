/* bb_lambda.c — exact branch-and-bound (independent of CP-SAT) for the minimum number of defect pairs
 *   def(D) = C(k,2) - lam * #{d >= 1 : r_D(d) = lam}
 * over D ⊂ [0, L] with 0, L ∈ D, |D| = k   (r_D(d) = #{(u,v) ∈ D^2 : u - v = d}).
 * Search: interior points chosen in increasing order (DFS), symmetry D <-> L - D broken by x_2 <= L - x_{k-1}
 * (checked at the leaf), lower bound = over-full weight + dead deficient classes + knapsack on remaining new pairs.
 * All bounds are valid lower bounds on the final def (proof in lambda_report.md, section "Exact optima").
 * Usage: bb_lambda lam k L UB [MD [MF [x2lo x2hi]]]   (MD/MF = remaining-point thresholds for the dead-class and
 *        full-hit tests; x2lo..x2hi restricts the first interior point, for splitting a run over processes)
 *            reports min def if min def <= UB (else "none <= UB"), one optimal D, node count.
 * Complete search: a printed optimum is exact for span exactly L.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int MD = 3, MF = 0, P0, X2LO = 1, X2HI = 1 << 30, STRICT = 0;   /* STRICT: forbid r > lam (B_2[lam] sets) */
static int lam, k, L, best, bestD[64], D[64], s;   /* D[0..s-1] current points ascending except D[1] = L */
static int r[4096];
static int over;          /* sum of r over classes with r > lam */
static long long nodes;
static int ndef[64];      /* ndef[j] = number of classes with r = j for 1 <= j < lam (deficient) */
static int defw;          /* sum of r over deficient classes */

static inline void addd(int d, int sg) {
    int o = r[d], n = o + sg;
    if (o > lam) over -= o; else if (o > 0 && o < lam) { ndef[o]--; defw -= o; }
    if (n > lam) over += n; else if (n > 0 && n < lam) { ndef[n]++; defw += n; }
    r[d] = n;
}
static void addpt(int x, int sg) { for (int i = 0; i < s; i++) addd(abs(x - D[i]), sg); }

static int curdef(void) { return over + defw; }   /* exact def of the current (complete) set */

/* lower bound on final def given m remaining points in (xc, L) */
static int lowerbound(int m, int xc) {
    if (STRICT && over > 0) return 1 << 29;
    long Q = (long)m * (m - 1) / 2 + (long)m * s;
    int lb = over;
    /* dead deficient classes (only computed when m small) */
    int dead = 0, deadw = 0;
    int nd2[64]; memcpy(nd2, ndef, sizeof(int) * lam);
    if (m <= MD) {
        for (int d = 1; d < L; d++) {
            int o = r[d];
            if (o <= 0 || o >= lam) continue;
            int capA = 0;
            for (int i = 0; i < s; i++) if (D[i] != L) { int y = D[i] + d; if (y > xc && y < L) capA++; }
            int capC = (d <= L - xc - 2) ? m - 1 : 0;
            int cap = capA + capC; if (cap > m) cap = m;
            if (d <= L - xc - 1) cap += 1;
            if (cap < lam - o) { dead++; deadw += o; nd2[o]--; }
        }
    }
    lb += deadw;
    /* full-hit bound: a future point y pays >= 1 for each old u with r_S(|y-u|) >= lam (that pair is a defect or
       destroys a good class); these pairs are distinct, so the m cheapest positions give a valid additive bound,
       and those pairs are unavailable to the knapsack (LB = s + KS(Q - s) is increasing in s). */
    long smin = 0;
    if (m <= MF) {
        int cnt[65]; memset(cnt, 0, sizeof cnt);
        for (int y = xc + 1; y < L; y++) {
            int c = 0;
            for (int i = 0; i < s; i++) { int d = abs(y - D[i]); if (r[d] >= lam) c++; }
            cnt[c]++;
        }
        int need = m;
        for (int c = 0; c <= 64 && need > 0; c++) { int t = cnt[c] < need ? cnt[c] : need; smin += (long)t * c; need -= t; }
        lb += (int)smin;
    }
    /* knapsack: alive deficient classes with r = j cost lam - j new pairs to fix, save j */
    int rest = defw - deadw;
    long budget = Q - smin; int save = 0;
    for (int j = lam - 1; j >= 1 && budget > 0; j--) {
        long cost = lam - j; long can = budget / cost; if (can > nd2[j]) can = nd2[j];
        save += (int)can * j; budget -= can * cost;
        if (can < nd2[j] && budget > 0) { /* fractional part */ save += (int)((budget * j) / cost); budget = 0; }
    }
    lb += rest - save;
    /* def = C(k,2) - lam*G is congruent to C(k,2) mod lam */
    while (((lb - P0) % lam + lam) % lam) lb++;
    return lb;
}

static void dfs(int xc) {
    nodes++;
    int m = k - s;
    if (m == 0) {
        int dd = curdef();
        if (STRICT && over > 0) return;
        /* symmetry: x_2 <= L - x_{k-1}: D sorted is D[0]=0, D[2..s-1] ascending, D[1]=L */
        if (k >= 4 && D[2] > L - D[s - 1]) return;
        if (dd < best) { best = dd; memcpy(bestD, D, sizeof(int) * k); }
        return;
    }
    if (lowerbound(m, xc) >= best) return;
    int xmax = L - m;
    if (k >= 4 && s >= 3 && L - D[2] < xmax) xmax = L - D[2];   /* symmetry: every interior point <= x_{k-1} <= L - x_2 */
    for (int x = xc + 1; x <= xmax; x++) {
        if (k >= 4 && s == 2 && x > L - x) { /* x_2 > L/2 impossible with symmetry x_2 <= L - x_{k-1} <= L - x_2 */ break; }
        if (s == 2 && (x < X2LO || x > X2HI)) continue;
        addpt(x, +1); D[s++] = x;
        dfs(x);
        s--; addpt(x, -1);
    }
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: lam k L UB\n"); return 2; }
    lam = atoi(argv[1]); k = atoi(argv[2]); L = atoi(argv[3]); int UB = atoi(argv[4]);
    if (L >= 4096 || k >= 64) return 2;
    best = UB + 1; P0 = k * (k - 1) / 2; if (argc > 5) MD = atoi(argv[5]); if (argc > 6) MF = atoi(argv[6]);
    if (argc > 8) { X2LO = atoi(argv[7]); X2HI = atoi(argv[8]); }
    if (getenv("BB_STRICT")) STRICT = 1;
    D[0] = 0; s = 1; addpt(L, +1); D[1] = L; s = 2;
    dfs(0);
    if (best <= UB) {
        int P = k * (k - 1) / 2;
        int srt[64]; memcpy(srt, bestD, sizeof(int) * k);
        for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (srt[j] < srt[i]) { int t = srt[i]; srt[i] = srt[j]; srt[j] = t; }
        printf("lam=%d k=%d L=%d mindef=%d G=%d phi=%.4f nodes=%lld D=", lam, k, L, best, (P - best) / lam,
               (double)(P - best) / P, nodes);
        for (int i = 0; i < k; i++) printf("%d%c", srt[i], i + 1 < k ? ',' : '\n');
    } else printf("lam=%d k=%d L=%d none<=%d nodes=%lld\n", lam, k, L, UB, nodes);
    return 0;
}
