"""Falsify a proposed coefficient-threshold deletion heuristic on Dirichlet.

The L4 primal is numerical. Its rounded rational coefficients determine an
exact rational dual candidate by projecting its cube. Minima in the search
are numerical; any found miss is saved for separate exact verification.
"""
import contextlib
import io
import itertools
import json
import math
from pathlib import Path
import socket
import sys

import numpy as np

from cstar_l4_completion import solve
from box_minlam import true_min


def ratio(A):
    return -true_min(list(A), over=32)[0][0] / math.sqrt(len(A))


def rank_prefixes(row):
    cert = row['exact_primal']
    c = cert['positive_coefficients']
    B = len(c)
    z = np.array(c[::-1]+[0]+c, dtype=object)
    cube = np.convolve(np.convolve(z,z),z)
    A = row['support']
    weights = {a:int(cube[3*B+a]) for a in A}
    order = sorted(A,key=lambda a:(weights[a],a))
    subsets = set()
    for k in range(1,len(A)):
        subsets.add(tuple(sorted(order[:k])))
        subsets.add(tuple(sorted(order[-k:])))
    scored = sorted((ratio(B),list(B)) for B in subsets)
    return weights, scored


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run on dirichlet through src/dirun.sh')
    base = [1,2,3,4,5,6,7,9]
    base_R = 1/math.sqrt(2)
    candidates = [base+[a] for a in range(8,33) if a not in base]
    extras = [a for a in range(8,21) if a not in base]
    candidates += [base+list(pair) for pair in itertools.combinations(extras,2)]
    checked = []
    found = None
    for A in candidates:
        A=sorted(A)
        parent_R=ratio(A)
        if parent_R <= base_R+1e-5:
            continue
        with contextlib.redirect_stdout(io.StringIO()):
            row=solve('threshold_probe',np.array(A),np.ones(len(A)),2*max(A),15)
        if 'exact_primal' not in row:
            continue
        weights, scored=rank_prefixes(row)
        record=dict(A=A,parent_R_float=parent_R,known_subset_R=base_R,
                    best_threshold_R_float=scored[0][0],best_threshold=scored[0][1],
                    cost_float=row['L4_over_sqrt_N'])
        checked.append(record)
        if scored[0][0] > parent_R+1e-5:
            found=dict(**record,weights={str(a):str(v) for a,v in weights.items()},
                       thresholds=[dict(R_float=r,A=B) for r,B in scored],
                       parent_completion=row,known_improving_subset=base)
            print('FOUND',json.dumps(record),flush=True)
            break
    out=dict(status='numerical threshold-heuristic test, not a universal theorem',
             checked=checked,miss=found)
    path=Path('.research/experiments/dual_deletion_2026-10-20/probe.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(checked=len(checked),found=found is not None,
                         worst_margins=sorted(checked,key=lambda r:r['best_threshold_R_float']-r['parent_R_float'],reverse=True)[:5]),indent=2))


if __name__=='__main__':
    main()
