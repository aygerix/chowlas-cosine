r"""Driver for src/exh2.c (complete box enumeration, load-balanced pthreads).  Same contract as
smallN_search.py exhaustive: threshold = certified upper bound on M of the best heuristic set in [1,L] (SA C kernel),
complete enumeration of all N-subsets of [1,L] with M_grid <= thr, accurate re-evaluation of survivors, certificate
(arb ball arithmetic) for the best.  Usage: python src/exh2_driver.py N L [threads] [P]
"""
import sys, os, json, time, subprocess
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(__file__))
import smallN_search as sn
N, L = int(sys.argv[1]), int(sys.argv[2])
th = sys.argv[3] if len(sys.argv) > 3 else os.environ.get('CHOWLA_WORKERS', '4')
P = sys.argv[4] if len(sys.argv) > 4 else '12'
here = os.path.dirname(os.path.abspath(__file__)); exe = os.path.join(here, '.build', 'exh2')
if not os.path.exists(exe) or os.path.getmtime(exe) < os.path.getmtime(os.path.join(here, 'exh2.c')):
    subprocess.check_call(['cc', '-O3', '-march=native', '-o', exe, os.path.join(here, 'exh2.c'), '-lm', '-lpthread'])
t0 = time.time()
known = [r['opt_A'] for r in sn._load_exh().values() if r.get('N') == N and 'opt_A' in r]
with Pool(int(th)) as pool:
    ub, A0 = sn.box_upper_bound(N, L, pool, extra=[sn.primitive(a) for a in known])
t1 = time.time()
out = subprocess.run([exe, str(N), str(L), repr(ub + 1e-9), str(4 * L), str(32 * L), str(th), '0', P],
                     capture_output=True, text=True, check=True).stdout.splitlines()
t2 = time.time()
surv = [list(map(int, l.split()[2:])) for l in out if l.startswith('S ')]
stats = next(l for l in out if l.startswith('STATS'))
ev = sorted((sn.accurate_M(S)[0], S) for S in surv)
rec = dict(N=N, L=L, thr_certified_ub=ub, seed_set=A0, n_survivors=len(surv), stats=stats,
           t_sa=round(t1 - t0, 1), t_enum=round(t2 - t1, 1), engine='exh2.c')
if ev:
    Mb, Sb = ev[0]; cub = sn.certify(Sb)
    rec.update(opt_A=Sb, opt_M_est=Mb, opt_M_cert_ub=cub, opt_R_est=Mb / N ** 0.5, opt_R_cert=cub / N ** 0.5,
               second_M=ev[1][0] if len(ev) > 1 else None)
print(json.dumps(rec), flush=True)
with open(os.path.join(sn.RUN_DIR, 'exh2.log'), 'a') as fh: fh.write(json.dumps(rec) + '\n')
