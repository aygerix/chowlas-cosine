"""Pure-Arb, independent all-circle certificate; VM ONLY.

For a global minimum x*, choose its nearest grid point x_j, |x_j-x*|<=h.
Taylor at x* and |f'''|<=S3 imply
  f(x*) >= f(x_j) - (abs(f''(x_j)) + S3*h)*h^2/2.
Check every right-hand side in directed Arb arithmetic, with no float critical
points or minimization. The earlier padded-cubic certificate is separate.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import time

import flint
import numpy as np

ROOT=Path('.research/agents/tdense17_scratch')


def main():
    begin=time.time()
    A=np.load(ROOT/'spline_L4096_s17_p5_6.npz')['A'].tolist()
    flint.ctx.prec=120
    G=1<<21
    h=flint.arb.pi()/G
    S3=sum(a**3 for a in A)
    B=Fraction(384437,5000)
    c=[flint.acb(0)]*G
    for a in A:c[a]=flint.acb(1)
    f=flint.acb.dft(c)
    del c
    print('Arb value DFT completed',flush=True)
    c=[flint.acb(0)]*G
    for a in A:c[a]=flint.acb(a*a)
    f2=flint.acb.dft(c)
    del c
    print('Arb second-derivative DFT completed',flush=True)
    b=flint.arb(B.numerator)/B.denominator
    h2=h*h/2
    error=flint.arb(S3)*h
    smallest=None
    for j,(z,z2) in enumerate(zip(f,f2)):
        margin=z.real+b-(abs(z2.real)+error)*h2
        assert margin>0,(j,str(margin))
        lower=margin.lower()
        if smallest is None or lower<smallest:smallest=lower
    rec=dict(passed=True,n=len(A),X=max(A),grid=G,precision_bits=120,
        B_rational=str(B),B_decimal=str(b),S3=S3,
        smallest_margin_lower=str(smallest),
        global_clique=1025,in_S_clique=1024,
        global_ratio_rational=str(Fraction(1025,2)/B),
        global_ratio_decimal=float(Fraction(1025,2)/B),
        in_S_ratio_rational=str(Fraction(1024,2)/B),
        in_S_ratio_decimal=float(Fraction(1024,2)/B),
        seconds=time.time()-begin,flint_version=flint.__version__)
    dest=ROOT/'fourway_independent_certificate.json'
    dest.write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec),flush=True)
    manifest=json.load(open(ROOT/'continuation_manifest.json'))
    cmd='DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -m 10 -t 600 python .research/agents/tdense17_scratch/fourway_independent_cert.py'
    if cmd not in manifest['commands']:manifest['commands'].append(cmd)
    for p in (Path(__file__),dest):manifest['sha256'][str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
    (ROOT/'continuation_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


if __name__=='__main__':main()
