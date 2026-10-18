/* zp_half.c — E41: exact minimum of M_p(A) = max_{γ≠0} (−1̂_A(γ)) over symmetric "half-sets" A ⊂ Z_p^*, i.e. A = ±P with
 * P a set of k pairs {a,−a}, k = (p−1)/4 (p ≡ 1 mod 4) or (p+1)/4 (p ≡ 3 mod 4).  1̂_A(γ) = 2 Σ_{a∈P} cos(2π a γ / p).
 * (Adding 0 to A shifts every 1̂_A(γ) by +1, so M(A ∪ {0}) = M(A) − 1; Sanders' Theorem 1.2 concerns |A| = (p+1)/2.)
 * Exhaustive depth-first branch and bound over pairs 1..(p−1)/2 with the multiplicative symmetry broken by forcing the
 * pair {1,−1} into P (A ↦ cA permutes the γ, so M is invariant and every orbit meets a set containing 1).
 * Pruning: at a node with chosen partial sums F[γ] and r pairs still to choose from the suffix i..h, the final value
 * satisfies F_final[γ] <= F[γ] + T[γ][i][r] (T = sum of the r largest suffix values), so
 * M_final >= max_γ −(F[γ] + T[γ][i][r]); prune when this is >= best − 1e−9 (keeps all optima with M < best).
 * Floating point (double) — NUMERICAL-EXACT up to rounding ~1e−12; values are reported to 1e−9.
 * Usage: zp_half p [best0]       prints p, k, min M, M/sqrt(p), #optimal P (with 1 ∈ P), one optimal P.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int p, h, k;
static double *V;          /* V[a*h + g] = 2 cos(2π a γ/p), a = 1..h, γ index g = 0..h−1 (γ = g+1) */
static double *T;          /* T[(g*(h+2) + i)*(h+2) + r] */
static double F[64], best;
static int chosen[64], bestset[64], nopt;
static long long nodes;

static inline double Tval(int g, int i, int r) { return T[((size_t)g * (h + 2) + i) * (h + 2) + r]; }

static void dfs(int i, int r) {       /* next candidate pair index i (1..h), r still to choose */
    nodes++;
    double lb = -1e300;
    for (int g = 0; g < h; g++) { double v = -(F[g] + Tval(g, i, r)); if (v > lb) lb = v; }
    if (lb >= best - 1e-9) return;
    if (r == 0) {                       /* leaf: lb is the exact M (T[..][..][0] = 0) */
        if (lb < best - 1e-9) { best = lb; nopt = 0; }
        nopt++; memcpy(bestset, chosen, sizeof chosen); return;
    }
    if (h - i + 1 < r) return;
    /* include pair i */
    chosen[i] = 1; for (int g = 0; g < h; g++) F[g] += V[(size_t)i * h + g];
    dfs(i + 1, r - 1);
    chosen[i] = 0; for (int g = 0; g < h; g++) F[g] -= V[(size_t)i * h + g];
    /* exclude pair i */
    dfs(i + 1, r);
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: zp_half p [best0]\n"); return 2; }
    p = atoi(argv[1]); h = (p - 1) / 2; k = (p % 4 == 1) ? (p - 1) / 4 : (p + 1) / 4;
    best = (argc > 2) ? atof(argv[2]) + 1e-7 : 1e300;
    V = malloc(sizeof(double) * (size_t)(h + 2) * h);
    for (int a = 1; a <= h; a++) for (int g = 0; g < h; g++) V[(size_t)a * h + g] = 2.0 * cos(2.0 * M_PI * (double)((long)a * (g + 1) % p) / p);
    T = calloc((size_t)h * (h + 2) * (h + 2), sizeof(double));
    double *buf = malloc(sizeof(double) * (h + 2));
    for (int g = 0; g < h; g++) for (int i = 1; i <= h + 1; i++) {
        int m = 0; for (int a = i; a <= h; a++) buf[m++] = V[(size_t)a * h + g];
        for (int x = 0; x < m; x++) for (int y = x + 1; y < m; y++) if (buf[y] > buf[x]) { double z = buf[x]; buf[x] = buf[y]; buf[y] = z; }
        double s = 0; T[((size_t)g * (h + 2) + i) * (h + 2) + 0] = 0;
        for (int r = 1; r <= h + 1; r++) { if (r <= m) s += buf[r - 1]; else s = 1e300; T[((size_t)g * (h + 2) + i) * (h + 2) + r] = s; }
    }
    memset(F, 0, sizeof F); memset(chosen, 0, sizeof chosen);
    chosen[1] = 1; for (int g = 0; g < h; g++) F[g] += V[(size_t)1 * h + g];
    dfs(2, k - 1);
    printf("p=%d k=%d |A|=%d minM=%.9f M/sqrtp=%.6f nopt=%d nodes=%lld P=", p, k, 2 * k, best, best / sqrt(p), nopt, nodes);
    for (int a = 1; a <= h; a++) if (bestset[a]) printf("%d ", a);
    printf("\n");
    return 0;
}
