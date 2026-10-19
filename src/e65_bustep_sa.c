/* e65_bustep_sa.c — E65: one Bu step at larger k by annealing. D is FIXED (the dilate 3D is a fixed part of A); E is
 * a free m-subset of the candidates {1 <= e <= XE : 3 ∤ e}. Minimise the grid value of M(3D ∪ E) = −min f.
 * Question (NOTEBOOK, triangle geometry): at |E| = lambda·|D| with lambda > 1, can M(3D ∪ E) stay near Bu's M
 * (lambda = 1)? Moves swap an element of E with a non-element candidate. f is even: grid of G = 8·Xmax + 1 points on
 * [0, π], O(G) update per move. Start: E0 from the input file (e.g. Bu's E, padded/trimmed randomly to m) or random.
 * HEURISTIC: grid minimum only; refine/certify winners separately (src/chowla.py / box_minlam.true_min).
 * Input file (whitespace separated): nD  d_1..d_nD  nE0  e_1..e_nE0  XE
 * The best state seen during each run is kept (so a Bu start can only improve at lambda = 1).
 * Usage: e65_bustep_sa infile m iters restarts seed [T0 factor, default 0.01]   prints JSON: grid M, R, E.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static int G, nc;
static float *ctab;                 /* ctab[i*G + j] = cos(cand[i] x_j) */
static double *f, *g, *base;

static inline void addc(double *h, int i, double s) { const float *c = ctab + (size_t)i * G; for (int j = 0; j < G; j++) h[j] += s * c[j]; }
static inline double gridM(const double *h) { double m = 1e300; for (int j = 0; j < G; j++) if (h[j] < m) m = h[j]; return -m; }

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: e65_bustep_sa infile m iters restarts seed\n"); return 2; }
    FILE *fp = fopen(argv[1], "r"); if (!fp) { perror("infile"); return 2; }
    int m = atoi(argv[2]); long iters = atol(argv[3]); int restarts = atoi(argv[4]);
    rs = strtoull(argv[5], 0, 10) * 2654435761ULL + 88172645463325252ULL;
    double T0f = argc > 6 ? atof(argv[6]) : 0.01;
    int nD; if (fscanf(fp, "%d", &nD) != 1) return 2;
    int *D = malloc(sizeof(int) * nD); for (int i = 0; i < nD; i++) if (fscanf(fp, "%d", &D[i]) != 1) return 2;
    int nE0; if (fscanf(fp, "%d", &nE0) != 1) return 2;
    int *E0 = malloc(sizeof(int) * (nE0 + 1)); for (int i = 0; i < nE0; i++) if (fscanf(fp, "%d", &E0[i]) != 1) return 2;
    int XE; if (fscanf(fp, "%d", &XE) != 1) return 2; fclose(fp);
    int Xmax = XE; for (int i = 0; i < nD; i++) if (3 * D[i] > Xmax) Xmax = 3 * D[i];
    G = 8 * Xmax + 1;
    int *cand = malloc(sizeof(int) * XE), *pos = malloc(sizeof(int) * (XE + 1));
    nc = 0; for (int e = 1; e <= XE; e++) { pos[e] = -1; if (e % 3) { pos[e] = nc; cand[nc++] = e; } }
    if (m > nc) { fprintf(stderr, "m > candidates\n"); return 2; }
    ctab = malloc(sizeof(float) * (size_t)nc * G);
    for (int i = 0; i < nc; i++) for (int j = 0; j < G; j++) ctab[(size_t)i * G + j] = (float)cos(cand[i] * M_PI * j / (G - 1));
    base = calloc(G, sizeof(double)); f = malloc(sizeof(double) * G); g = malloc(sizeof(double) * G);
    for (int i = 0; i < nD; i++) for (int j = 0; j < G; j++) base[j] += cos(3.0 * D[i] * M_PI * j / (G - 1));
    int *in = malloc(sizeof(int) * nc), *bestin = malloc(sizeof(int) * nc), *el = malloc(sizeof(int) * m), *out = malloc(sizeof(int) * nc);
    double bestM = 1e300;
    for (int r = 0; r < restarts; r++) {
        memset(in, 0, sizeof(int) * nc); memcpy(f, base, sizeof(double) * G); int cntE = 0;
        for (int i = 0; i < nE0 && cntE < m; i++) { int e = E0[i]; if (e >= 1 && e <= XE && pos[e] >= 0 && !in[pos[e]]) { in[pos[e]] = 1; addc(f, pos[e], 1); cntE++; } }
        while (cntE < m) { int i = (int)(rnd() % nc); if (!in[i]) { in[i] = 1; addc(f, i, 1); cntE++; } }
        /* E0 longer than m: keep the first m; restarts > 0 randomise by a few random swaps */
        int ne = 0, no = 0; for (int i = 0; i < nc; i++) { if (in[i]) el[ne++] = i; else out[no++] = i; }
        double M = gridM(f), T0 = T0f * sqrt((double)(nD + m)), T;
        if (M < bestM) { bestM = M; memset(bestin, 0, sizeof(int) * nc); for (int i = 0; i < ne; i++) bestin[el[i]] = 1; }
        for (long it = 0; it < iters; it++) {
            T = T0 * pow(1e-3, (double)it / iters);
            int a = (int)(rnd() % ne), b = (int)(rnd() % no);
            memcpy(g, f, sizeof(double) * G); addc(g, el[a], -1); addc(g, out[b], 1);
            double M2 = gridM(g);
            if (M2 <= M || urand() < exp((M - M2) / T)) {
                double *tmp = f; f = g; g = tmp; int t = el[a]; el[a] = out[b]; out[b] = t; M = M2;
                if (M < bestM - 1e-12) { bestM = M; memset(bestin, 0, sizeof(int) * nc); for (int i = 0; i < ne; i++) bestin[el[i]] = 1; }
            }
        }
    }
    printf("{\"nD\": %d, \"m\": %d, \"XE\": %d, \"iters\": %ld, \"restarts\": %d, \"grid_M\": %.6f, \"grid_R\": %.6f, \"E\": [",
           nD, m, XE, iters, restarts, bestM, bestM / sqrt((double)(nD + m)));
    int first = 1; for (int i = 0; i < nc; i++) if (bestin[i]) { printf(first ? "%d" : ", %d", cand[i]); first = 0; }
    printf("]}\n");
    return 0;
}
