/* E116-FD: best FUNDAMENTAL-DOMAIN lift. Each class pair {g, −g} of D (g ∈ Z_n²) gets exactly one representative
   z ∈ g + nZ² from a candidate list (and −z for −g). Minimise Kgrid = −min_{G×G grid} F(ξ), F = Σ_classes 2cos(2π z·ξ).
   |T| = |D| is fixed, so ratio = |D|/K². Lead, cont. 31.
   Input: "C G", then C lines "k z1_1 z2_1 ... z1_k z2_k init_index". Output: best K and chosen indices.
   Usage: e116_fd infile iters T0 T1 seed outfile */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
static unsigned long long rs;
static double rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (rs >> 11) * (1.0 / 9007199254740992.0); }
static int G, H; static double *cg, *F;
static void add(long z1, long z2, double s, double *mn) {
  long a0 = z1 % G; if (a0 < 0) a0 += G; long db = z2 % G; if (db < 0) db += G; double m = 1e300;
  for (int i = 0; i < H; i++) { double *row = F + (size_t)i * G; long a = (a0 * i) % G, b = 0;
    for (int j = 0; j < G; j++) { long u = a + b; if (u >= G) u -= G; row[j] += s * cg[u]; if (row[j] < m) m = row[j]; b += db; if (b >= G) b -= G; } }
  if (mn) *mn = m;
}
int main(int argc, char **argv) {
  FILE *f = fopen(argv[1], "r"); int C; if (fscanf(f, "%d %d", &C, &G) != 2) return 3;
  int *k = malloc(C * sizeof(int)), *cur = malloc(C * sizeof(int)), *best = malloc(C * sizeof(int)); long **Z = malloc(C * sizeof(long *));
  for (int c = 0; c < C; c++) { if (fscanf(f, "%d", &k[c]) != 1) return 3; Z[c] = malloc(2 * k[c] * sizeof(long));
    for (int t = 0; t < 2 * k[c]; t++) if (fscanf(f, "%ld", &Z[c][t]) != 1) return 3; if (fscanf(f, "%d", &cur[c]) != 1) return 3; }
  fclose(f);
  long iters = atol(argv[2]); double T0 = atof(argv[3]), T1 = atof(argv[4]); rs = 88172645463325252ULL ^ (unsigned long long)atol(argv[5]);
  cg = malloc(G * sizeof(double)); for (int q = 0; q < G; q++) cg[q] = 2.0 * cos(2 * M_PI * q / G);
  H = G / 2 + 1; F = calloc((size_t)H * G, sizeof(double));
  for (int c = 0; c < C; c++) add(Z[c][2 * cur[c]], Z[c][2 * cur[c] + 1], 1.0, NULL);
  double mn = 1e300; for (size_t q = 0; q < (size_t)H * G; q++) if (F[q] < mn) mn = F[q];
  double E = -mn, bE = E; memcpy(best, cur, C * sizeof(int));
  for (long it = 0; it < iters; it++) {
    double temp = T0 * pow(T1 / T0, (double)it / iters);
    int c = (int)(rnd() * C); if (k[c] < 2) continue; int nw = (int)(rnd() * (k[c] - 1)); if (nw >= cur[c]) nw++;
    double m2;
    add(Z[c][2 * cur[c]], Z[c][2 * cur[c] + 1], -1.0, NULL);
    add(Z[c][2 * nw], Z[c][2 * nw + 1], 1.0, &m2);
    double E2 = -m2;
    if (E2 <= E || rnd() < exp(-(E2 - E) / temp)) { cur[c] = nw; E = E2; if (E < bE) { bE = E; memcpy(best, cur, C * sizeof(int)); } }
    else { add(Z[c][2 * nw], Z[c][2 * nw + 1], -1.0, NULL); add(Z[c][2 * cur[c]], Z[c][2 * cur[c] + 1], 1.0, NULL); }
  }
  FILE *o = fopen(argv[6], "w"); fprintf(o, "%.10f\n", bE); for (int c = 0; c < C; c++) fprintf(o, "%d ", best[c]); fprintf(o, "\n"); fclose(o);
  printf("bestK %.6f\n", bE); return 0;
}
