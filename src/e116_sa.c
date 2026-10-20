/* E116 SA: minimise E(T) = Kgrid(T)/sqrt(|T|) over symmetric T ⊂ P (a list of pairs ±z, z ∈ Z²), where
   Kgrid = −min over the G×G grid of F_T(ξ) = Σ_{z∈T} 2cos(2π z·ξ). Lead, cont. 31.
   Input file: first line "P G", then P lines "z1 z2 init" (init ∈ {0,1}). Output: best E, |T|, Kgrid and the 0/1 vector.
   Usage: e116_sa infile iters T0 T1 seed outfile
   Grid minima are NUMERICAL; the driver re-evaluates the best set by true_min (FFT + BFGS). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

static unsigned long long rs;
static double rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (rs >> 11) * (1.0 / 9007199254740992.0); }

int main(int argc, char **argv) {
  if (argc < 7) { fprintf(stderr, "usage\n"); return 2; }
  FILE *f = fopen(argv[1], "r"); int P, G; if (fscanf(f, "%d %d", &P, &G) != 2) return 3;
  int *z1 = malloc(P * sizeof(int)), *z2 = malloc(P * sizeof(int)), *x = malloc(P * sizeof(int)), *bx = malloc(P * sizeof(int));
  for (int t = 0; t < P; t++) if (fscanf(f, "%d %d %d", &z1[t], &z2[t], &x[t]) != 3) return 3;
  fclose(f);
  long iters = atol(argv[2]); double T0 = atof(argv[3]), T1 = atof(argv[4]); rs = 88172645463325252ULL ^ (unsigned long long)atol(argv[5]);
  double *cg = malloc(G * sizeof(double)); for (int k = 0; k < G; k++) cg[k] = 2.0 * cos(2 * M_PI * k / G);
  int H = G / 2 + 1; /* rows i = 0..G/2 suffice by symmetry ξ -> −ξ */
  double *F = calloc((size_t)H * G, sizeof(double));
  int n = 0;
  for (int t = 0; t < P; t++) if (x[t]) { n++;
    for (int i = 0; i < H; i++) for (int j = 0; j < G; j++) {
      long u = ((long)z1[t] * i + (long)z2[t] * j) % G; if (u < 0) u += G; F[(size_t)i * G + j] += cg[u]; } }
  double mn = 1e300; for (size_t q = 0; q < (size_t)H * G; q++) if (F[q] < mn) mn = F[q];
  double E = (n > 0) ? (-mn) / sqrt((double)n * 4) : 1e9, bE = E; memcpy(bx, x, P * sizeof(int)); int bn = n; double bK = -mn;
  for (long it = 0; it < iters; it++) {
    double temp = T0 * pow(T1 / T0, (double)it / iters);
    int t = (int)(rnd() * P); double s = x[t] ? -1.0 : 1.0; int nn = n + (x[t] ? -1 : 1);
    if (nn < 1) continue;
    double m2 = 1e300;
    for (int i = 0; i < H; i++) { double *row = F + (size_t)i * G; long a = ((long)z1[t] * i) % G; if (a < 0) a += G;
      long b = 0, db = z2[t] % G; if (db < 0) db += G;
      for (int j = 0; j < G; j++) { long u = a + b; if (u >= G) u -= G; row[j] += s * cg[u]; if (row[j] < m2) m2 = row[j]; b += db; if (b >= G) b -= G; } }
    double E2 = (-m2) / sqrt((double)nn * 4);
    if (E2 <= E || rnd() < exp(-(E2 - E) / temp)) { x[t] ^= 1; n = nn; E = E2;
      if (E < bE) { bE = E; memcpy(bx, x, P * sizeof(int)); bn = n; bK = -m2; } }
    else { for (int i = 0; i < H; i++) { double *row = F + (size_t)i * G; long a = ((long)z1[t] * i) % G; if (a < 0) a += G;
        long b = 0, db = z2[t] % G; if (db < 0) db += G;
        for (int j = 0; j < G; j++) { long u = a + b; if (u >= G) u -= G; row[j] -= s * cg[u]; b += db; if (b >= G) b -= G; } } }
  }
  FILE *o = fopen(argv[6], "w"); fprintf(o, "%.10f %d %.10f\n", bE, 2 * bn, bK);
  for (int t = 0; t < P; t++) fprintf(o, "%d", bx[t]); fprintf(o, "\n"); fclose(o);
  printf("bestE %.6f |T| %d Kgrid %.6f ratio %.4f\n", bE, 2 * bn, bK, 2.0 * bn / (bK * bK));
  return 0;
}
