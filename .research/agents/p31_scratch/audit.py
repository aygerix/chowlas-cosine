"""Numerical P31 falsification tests; run only through src/dirun.sh.

No optimizer output here is a rigorous all-circle minimum certificate.
All generated files stay inside p31_scratch.
"""
import sys
sys.dont_write_bytecode = True
import ctypes
import json
import math
import platform
from pathlib import Path
import subprocess
from fractions import Fraction as Q

import numpy as np
from scipy.optimize import minimize_scalar, minimize

ROOT = Path.cwd()
OUT = ROOT / '.research/agents/p31_scratch'
subprocess.run(['cc', '-O3', '-shared', '-fPIC', str(OUT/'eval.c'), '-lm', '-o', str(OUT/'eval.so')], check=True)
lib = ctypes.CDLL(str(OUT/'eval.so'))
ptr = np.ctypeslib.ndpointer(dtype=np.int64, ndim=1, flags='C_CONTIGUOUS')
for name in ('cosine_value', 'bu_value'):
    f = getattr(lib, name)
    f.argtypes = [ptr, ctypes.c_size_t, ctypes.c_double]
    f.restype = ctypes.c_double
sys.path.insert(0, str(ROOT/'src'))
from bu import A_of_S
from singer import singer

seed = 310019
rng = np.random.default_rng(seed)
cases = []
def add(name, a, s=None, certificate=None):
    a = np.array(sorted(set(map(int, a))), dtype=np.int64)
    assert len(a) and a[0] > 0
    cases.append((name, a, None if s is None else np.array(s, dtype=np.int64), certificate))

add('singleton_1', [1])
add('singleton_12_P29_error', [12])
for x in (32, 128, 512):
    add(f'interval_{x}', range(1,x+1))
for density in (.1, .35, .7):
    a = np.flatnonzero(rng.random(512) < density)+1
    add(f'random_X512_d{density}', a)
for p in (1, 2, 4, 8):
    a = np.flatnonzero(rng.random(2048) < (1-np.arange(1,2049)/2048)**p)+1
    add(f'taper_p{p}_X2048', a)
add('lacunary_powers2', [2**j for j in range(13)])
add('lacunary_powers3', [3**j for j in range(9)])
for tails in (4, 32):
    a = list(range(1,129))+list(rng.choice(np.arange(4096,65536), tails, replace=False))
    add(f'core128_tail{tails}', a)
for name, record in json.loads((ROOT/'examples/construct/N50_certified.json').read_text()).items():
    add(name, record['A'], certificate={'upper_M': -record['cert_lower'], 'source': 'examples/construct/N50_certified.json'})
for q in (7, 31):
    d, _ = singer(q)
    a = sorted({abs(x-y) for j,x in enumerate(d) for y in d[j+1:]})
    assert len(a) == len(d)*(len(d)-1)//2
    add(f'Singer_difference_q{q}', a)
for q in ('61', '101', '401'):
    record = json.loads((ROOT/'examples/singer_bu/certified.json').read_text())[q]
    add(f'Bu_q{q}', A_of_S(record['S']), s=record['S'], certificate={'upper_M': -record['cert_lower'], 'source': 'examples/singer_bu/certified.json'})

results = []
for name, a, s, cert in cases:
    n, x = len(a), int(a[-1])
    k = 1 << (16*x).bit_length()
    coeff = np.zeros(k//2+1, dtype=np.complex128)
    coeff[a] = k/2
    values = np.fft.irfft(coeff, n=k)
    if s is None:
        fun = lambda theta: lib.cosine_value(a, len(a), theta)
    else:
        fun = lambda theta: lib.bu_value(s, len(s), theta)
    # Refine the 48 lowest sampled local minima. The grid is numerical evidence.
    left, mid, right = values[:k//2-1], values[1:k//2], values[2:k//2+1]
    indices = np.flatnonzero((mid<=left)&(mid<=right))+1
    indices = indices[np.argsort(values[indices])[:48]]
    dx = 2*math.pi/k
    estimates = [(fun(0), 0), (fun(math.pi), math.pi)]
    for j in indices:
        opt = minimize_scalar(fun, bounds=((j-1)*dx,(j+1)*dx), method='bounded', options={'xatol': 2e-14})
        estimates.append((opt.fun, opt.x))
    fmin, theta = min(estimates)
    m = -fmin
    # Independent FFT/C direct checks, including actual A even for Bu.
    fft_error = 0
    bu_error = 0
    for j in rng.integers(0,k,size=5):
        val = lib.cosine_value(a, len(a), int(j)*dx)
        fft_error = max(fft_error, abs(val-values[j]))
        if s is not None:
            bu_error = max(bu_error, abs(val-fun(int(j)*dx)))
    windows = []
    for eps in (.01,.05,.1,.25,.5,1.,2.):
        w = max(1,int(eps*x))
        N = x+w+1
        W = 2*(w+1)/3+1/(3*(w+1))
        S = float(np.maximum(0,1-a.astype(float)/(w+1))@np.maximum(0,1-a.astype(float)/(w+1)))
        entry = dict(epsilon=eps,w=w,L=N-1,W=W,S=S,d=2*S/W)
        entry['rho_required'] = W*(n/2+m*m)/(N*(m*m+S/2))
        bounds = {}
        for label,rho in [('proved',min(.95,4/(3*math.sqrt(3))*(1+2/math.sqrt(N))**3)),('heuristic_rho_0.687',.687)]:
            C = rho*N
            bounds[label] = math.sqrt(max(0,(W*n-C*S)/(2*(C-W)))) if C>W else None
        entry['M_lower_bounds'] = bounds
        windows.append(entry)
    rec = dict(name=name,n=n,X=x,density=n/x,M_estimate=m,R_estimate=m/math.sqrt(n),theta=theta,fft_size=k,
               fft_direct_error=fft_error,bu_identity_error=bu_error,existing_certificate=cert,windows=windows,
               max_proved_bound=max(z['M_lower_bounds']['proved'] or 0 for z in windows),
               max_heuristic_bound=max(z['M_lower_bounds']['heuristic_rho_0.687'] or 0 for z in windows))
    results.append(rec)
    print(name, 'n',n,'X',x,'M',round(m,8),'P31',round(rec['max_proved_bound'],8),'rho_needed',round(max(z['rho_required'] for z in windows),8), flush=True)
    (OUT/'audit_results.json').write_text(json.dumps(dict(seed=seed,python=platform.python_version(),numpy=np.__version__,cases=results),indent=2))

# Exact independent checks of the quartic proof's polynomial identities.
for N in range(2,65):
    c = [Q(N*(N+1),2)+j*(N-1-j) for j in range(N)]
    av = sum(c)/N
    var = sum((z-av)**2 for z in c)/N
    assert var == Q((N*N-1)*(N*N-4),180)
    assert Q(2*N*N+1,3*N*N) <= Q(3,4)
    assert sum(Q(k*(N-k),N) for k in range(1,N)) == Q(N*N-1,6)
print('Exact uniform-proof identities checked for N=2..64',flush=True)

# Numerical maximizers are LOWER bounds for rho, never certificates of upper bounds.
rho_results = []
for N in (2,3,5,10,20,50,120):
    def objective(z):
        v = z*z
        c = np.convolve(v,v)
        return -(c@c)/(N*(v@v)**2)
    best = 0
    for trial in range(4):
        z = np.ones(N) if trial==0 else rng.uniform(.4,1.2,N)
        opt = minimize(objective,z,method='L-BFGS-B',options={'maxiter':1500})
        best=max(best,-float(opt.fun))
    rho_results.append({'N':N,'numerical_lower_bound_rho':best})
print('rho numerical lower bounds',rho_results,flush=True)
(OUT/'rho_lower_bounds.json').write_text(json.dumps(rho_results,indent=2))
print('Explicit beta bound N=250000:',4/(3*math.sqrt(3))*(1+2/500)**3,flush=True)
