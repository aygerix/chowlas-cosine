"""Certify candidate sets: rigorous lower bound for min f_A by arb ball arithmetic (src/chowla.certify_lower_bound,
4th-order Taylor cells on a grid of L = 2^ceil(log2(over*maxA)) points) + float estimate (FFT + Newton).
Input: a file with lines containing 'A=[a,b,...]' or 'A=a b c' (IMPROVE/FINAL lines) or JSON {"A": [...]}; label = line tag.
Output: JSON lines {label, N, max, est_min, cert_lower, R_est, R_cert, L} (R_cert = -cert_lower/sqrt(N) is a CERTIFIED upper
bound for R(A))."""
import sys, re, json, math
sys.path.insert(0, 'src')
from chowla import certify_lower_bound, min_estimate_fft, validate

def parse(line):
    m = re.search(r'A=\[([0-9,\s]+)\]', line)
    if m: return [int(t) for t in re.split(r'[,\s]+', m.group(1).strip()) if t]
    m = re.search(r'A=([0-9\s]+)$', line.strip())
    if m: return [int(t) for t in m.group(1).split()]
    try: return json.loads(line)['A']
    except Exception: return None

over = int(sys.argv[2]) if len(sys.argv) > 2 else 64
for i, line in enumerate(open(sys.argv[1])):
    A = parse(line)
    if not A: continue
    A = validate(A)
    est = min_estimate_fft(A, oversample=64, polish=16)
    cert = certify_lower_bound(A, oversample=over)
    N = len(A)
    out = dict(label=line.split()[0][:40], line=i, N=N, max=max(A), est_min=est.fmin, x_est=est.xmin,
               cert_lower=cert.lower_bound, R_est=est.R, R_cert=-cert.lower_bound / math.sqrt(N), L=cert.L,
               gap=est.fmin - cert.lower_bound, A=A)
    print(json.dumps(out), flush=True)
