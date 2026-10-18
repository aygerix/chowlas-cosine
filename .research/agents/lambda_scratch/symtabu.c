/* symtabu.c — tabu search (HEURISTIC) over REFLECTION-SYMMETRIC sets D = H ∪ (c − H), H ⊂ [0, c/2), 0 ∈ H, |D| = k = 2|H|.
 * Even λ = 2μ.  r_D(d) = 2 r_H(d) + 2 #{h<h' ∈ H: h+h' = c−d} + [d ∈ c − 2H]; classes d = c − 2h ("fixed" classes,
 * r odd) are the Bu-type defects: when r(d) = 1 their contribution to E is E_fix(t) = P(2t) where F_D = e^{ict/2} P(t)
 * (harmless in Bu's mechanism).  Objective: W' = Σ 2 r(d) over defect classes (r ∉ {0, λ}) EXCLUDING fixed classes
 * with r = 1.  Also reports |A| = #{d: r(d) = λ}, total W and φ = λ|A|/C(k,2).
 * Usage: symtabu lam k c iters seed [tenure] [stall]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static int lam, k, h, c, *H, *inH, *r, *fx, *tabu, G, Wp, Wt, nD, *Dp;
static inline int costp(int d) { int x = r[d]; if (x == 0 || x == lam) return 0; if (x == 1 && fx[d]) return 0; return 2 * x; }
static inline int costt(int d) { int x = r[d]; return (x == 0 || x == lam) ? 0 : 2 * x; }
static inline void upd(int d, int dv) {
    Wp -= costp(d); Wt -= costt(d); if (r[d] == lam) G--;
    r[d] += dv;
    Wp += costp(d); Wt += costt(d); if (r[d] == lam) G++;
}
static inline void setfx(int d, int v) { Wp -= costp(d); fx[d] = v; Wp += costp(d); }
/* D stored as list Dp[0..nD) */
static void addpt(int x) { for (int i = 0; i < nD; i++) upd(abs(x - Dp[i]), +1); Dp[nD++] = x; }
static void rmpt(int x) {
    int j = -1; for (int i = 0; i < nD; i++) if (Dp[i] == x) { j = i; break; }
    Dp[j] = Dp[--nD]; for (int i = 0; i < nD; i++) upd(abs(x - Dp[i]), -1);
}
static void moveH(int i, int y) { /* H[i] -> y */
    int o = H[i];
    rmpt(o); rmpt(c - o); setfx(c - 2 * o, 0); inH[o] = 0;
    H[i] = y; inH[y] = 1; addpt(y); addpt(c - y); setfx(c - 2 * y, 1);
}
static double obj(void) { return G > 0 ? (double)(k + Wp) * (k + Wp) / G : 1e18; }

int main(int argc, char **argv) {
    lam = atoi(argv[1]); k = atoi(argv[2]); c = atoi(argv[3]); long iters = atol(argv[4]);
    rs = 0x9E3779B97F4A7C15ULL ^ ((uint64_t)atol(argv[5]) * 0x2545F4914F6CDD1DULL);
    int tenure = argc > 6 ? atoi(argv[6]) : 7, stall = argc > 7 ? atoi(argv[7]) : 2000;
    h = k / 2; int hm = (c - 1) / 2;           /* H ⊂ [0, hm], hm < c/2 */
    H = malloc(sizeof(int) * h); inH = calloc(c + 1, sizeof(int)); r = calloc(c + 1, sizeof(int));
    fx = calloc(c + 1, sizeof(int)); tabu = calloc(c + 1, sizeof(int)); Dp = malloc(sizeof(int) * (k + 4));
    int *bH = malloc(sizeof(int) * h);
    H[0] = 0; inH[0] = 1;
    for (int i = 1; i < h; i++) { int x; do x = 1 + (int)(rnd() % hm); while (inH[x]); H[i] = x; inH[x] = 1; }
    nD = 0; for (int i = 0; i < h; i++) { addpt(H[i]); addpt(c - H[i]); setfx(c - 2 * H[i], 1); }
    double best = obj(); int bG = G, bWp = Wp, bWt = Wt; memcpy(bH, H, sizeof(int) * h); long lastimp = 0;
    for (long it = 1; it <= iters; it++) {
        int bi = -1, by = -1, nb = 0; double bo = 1e300;
        for (int i = 1; i < h; i++) for (int y = 1; y <= hm; y++) {
            if (inH[y]) continue;
            int o = H[i]; moveH(i, y); double v = obj(); moveH(i, o);
            int ok = tabu[y] < it || v < best - 1e-12;
            if (ok && (v < bo - 1e-12 || (v < bo + 1e-12 && rnd() % (++nb) == 0))) { if (v < bo - 1e-12) nb = 1; bo = v; bi = i; by = y; }
        }
        if (bi < 0) continue;
        int o = H[bi]; moveH(bi, by); tabu[o] = it + tenure + (int)(rnd() % 3);
        double cur = obj();
        if (cur < best - 1e-12) { best = cur; bG = G; bWp = Wp; bWt = Wt; memcpy(bH, H, sizeof(int) * h); lastimp = it; }
        if (it - lastimp > stall) {
            for (int t = 0; t < 2; t++) { int i = 1 + (int)(rnd() % (h - 1)), y; do y = 1 + (int)(rnd() % hm); while (inH[y]); moveH(i, y); }
            lastimp = it;
        }
    }
    double P = k * (k - 1) / 2.0;
    printf("lam=%d k=%d c=%d |A|=%d Wp=%d Wp/k=%.3f Wtot=%d phi=%.4f Rn'=%.4f D=", lam, k, c, bG, bWp, (double)bWp / k, bWt,
           lam * bG / P, (k + bWp) / (2.0 * lam * __builtin_sqrt((double)bG)));
    int *Ds = malloc(sizeof(int) * k); for (int i = 0; i < h; i++) { Ds[i] = bH[i]; Ds[h + i] = c - bH[i]; }
    for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (Ds[j] < Ds[i]) { int t = Ds[i]; Ds[i] = Ds[j]; Ds[j] = t; }
    for (int i = 0; i < k; i++) printf("%d%c", Ds[i], i + 1 < k ? ',' : '\n');
    return 0;
}
