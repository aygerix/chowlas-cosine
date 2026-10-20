"""Search for a failure of nonnegative true-dual Fourier coefficients.

Numerical search only. A strict gap between a signed-dual lower witness and a
lower-bound-interpolation primal upper witness can be certified separately.
"""
import argparse
import contextlib
import io
import json
from pathlib import Path
import socket
import numpy as np
from cstar_l4_completion import solve


def cube_weights(row):
    c=row['exact_primal']['positive_coefficients'];B=len(c)
    z=np.array(c[::-1]+[0]+c,dtype=object)
    cube=np.convolve(np.convolve(z,z),z)
    return {a:int(cube[3*B+a]) for a in row['support']},int(cube[3*B])


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through dirun.sh')
    parser=argparse.ArgumentParser();parser.add_argument('--box',type=int,default=10);args=parser.parse_args()
    out=dict(status='numerical search, no global sign claim until a separation is verified',box=args.box,checked=0,candidate=None)
    for mask in range(1,2**args.box):
        A=[j+1 for j in range(args.box) if mask>>j&1]
        if len(A)<3:continue
        with contextlib.redirect_stdout(io.StringIO()):
            row=solve('dual_sign_scan',np.array(A),np.ones(len(A)),2*max(A),10)
        if 'exact_primal' not in row:continue
        out['checked']+=1
        weights,c0=cube_weights(row)
        rel=min(weights.values())/max(abs(v) for v in weights.values())
        if rel < -.001:
            with contextlib.redirect_stdout(io.StringIO()):
                relaxed=solve('dual_sign_relaxed',np.array(A),np.ones(len(A)),4*max(A),30,lower_bounds_only=True)
            out['candidate']=dict(A=A,relative_minimum=rel,equality=row,relaxed=relaxed,
                                  weights={str(a):str(v) for a,v in weights.items()},constant=str(c0))
            print('CANDIDATE',json.dumps(dict(A=A,relative_minimum=rel,
                  equality_primal=row['L4_over_sqrt_N'],equality_dual=row['dual_L4_lower_over_sqrt_N_float'],
                  relaxed_primal=relaxed.get('L4_over_sqrt_N'))),flush=True)
            break
    path=Path('.research/experiments/dual_deletion_2026-10-20/dual_sign.json')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='candidate'},indent=2))


if __name__=='__main__':main()
