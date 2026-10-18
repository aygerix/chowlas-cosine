"""Certify the construction agent's N = 50 class records (2026-10-18) by two independent methods:
E2 (arb ball DFT + Taylor, chowla.certify_lower_bound) and E3 (exact PARI Sturm count, chowla.sturm_certify)."""
import json, math, sys
sys.path.insert(0, "src")
from chowla import certify_lower_bound, sturm_certify, min_estimate_fft, validate

SETS = {
    "N50_x72": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,
                39,40,43,44,47,49,50,52,54,60,68,69,72],
    "N50_x71": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,
                40,41,42,47,48,50,52,57,61,62,64,65,68],
}
out = {}
for name, A in SETS.items():
    A = validate(A); N = len(A)
    est = min_estimate_fft(A, oversample=64)
    cert = certify_lower_bound(A, oversample=64)
    lo = cert.lower_bound
    D = 10**7
    up = math.ceil(-lo * D)                     # B_up/D >= -lo: claim f + B_up/D > 0
    dn = math.floor(-est.fmin * D) - 2               # just below the estimated M
    ok_up, n_up = sturm_certify(A, up, D)
    ok_dn, n_dn = sturm_certify(A, dn, D)
    out[name] = dict(A=A, N=N, max=max(A), est=str(est), cert_lower=float(lo), sturm_up=[up, D, ok_up, n_up],
                     sturm_down=[dn, D, ok_dn, n_dn], R_upper=up / D / math.sqrt(N))
    print(name, N, max(A), "est", est, "E2 min f >=", lo, "E3 +%d/1e7: ok=%s roots=%d;  +%d/1e7: ok=%s roots=%d  R<=%.7f"
          % (up, ok_up, n_up, dn, ok_dn, n_dn, up / D / math.sqrt(N)), flush=True)
json.dump(out, open(".research/agents/construct_scratch/cert_n50.json", "w"), indent=1)
