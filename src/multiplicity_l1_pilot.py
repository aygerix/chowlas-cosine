"""One exact-combinatorial l1 multiplicity construction pilot.

Archived failed-mechanism pilot: the subsequent centroid theorem in
.research/notes/multiplicity_centroid_2026-10-23.md proves the half
gate impossible for this objective. Do not enlarge/redeploy it.
This keeps every nonzero difference class. Its certified all-circle
upper bound uses the square identity and an l1 coefficient remainder.
It neither samples minima nor establishes a parametric construction.
Run mathematical computation on Dirichlet via dirun.sh.
"""
from fractions import Fraction
import json
import math
from pathlib import Path
import socket
import time

from flint import fmpz_poly
import numpy as np


def pair_counts(B, X):
    values = np.array(sorted(B),dtype=np.int64)
    differences = values[:,None]-values[None,:]
    return np.bincount(differences[differences>0],minlength=X+1)


def cost(values, r):
    return np.where(values>0,np.abs(values-r),0)


def certify(B,r,X):
    B = sorted(map(int,B))
    counts = pair_counts(B,X)
    flags = [0]*(max(B)+1)
    for b in B:
        flags[b]=1
    # A separate exact polynomial multiplication checks all pair counts.
    autocorr = fmpz_poly(flags)*fmpz_poly(flags[::-1])
    for d in range(1,X+1):
        assert int(counts[d]) == int(autocorr[len(flags)-1+d])
    assert int(autocorr[len(flags)-1]) == len(B)
    A = np.flatnonzero(counts).tolist()
    E = int(cost(counts,r).sum())
    N,k = len(A),len(B)
    assert sum(int(v) for v in counts) == k*(k-1)//2
    assert abs(r*N-k*(k-1)//2)<=E
    upper = Fraction(k+2*E,2*r)
    bound_squared = upper*upper/N
    return dict(B=B,A=A,k=k,r=r,N=N,max_A=max(A),
        E=E,multiplicity_histogram={str(i):int(np.sum(counts==i))
             for i in np.unique(counts) if i>0},
        M_upper_exact=str(upper),R_upper_squared_exact=str(bound_squared),
        R_upper_display=math.sqrt(float(bound_squared)),
        defect_ratio_display=E/(k*math.sqrt(r)),
        defect_target_passed=64*E*E < k*k*r,
        half_constant_upper_passed=4*upper*upper < N,
        independent_exact_autocorrelation_match=True,
        certificate='Exact square identity plus l1 coefficient remainder; all real x')


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    k,r,X,steps,seed = 128,8,2048,15000,2026102308
    rng = np.random.default_rng(seed)
    B = {0,*map(int,rng.choice(np.arange(1,X+1),k-1,replace=False))}
    counts = pair_counts(B,X)
    E = int(cost(counts,r).sum())
    initial = E
    bestE,bestB,beststep = E,sorted(B),-1
    accepted = 0
    history = []
    start = time.monotonic()
    for step in range(steps):
        size = int(rng.choice([1,2,4],p=[.8,.15,.05]))
        removed = set(map(int,rng.choice(sorted(B-{0}),size,replace=False)))
        kept = B-removed
        added = set()
        while len(added)<size:
            if rng.random()<.5:
                base = int(rng.choice(sorted(removed)))
                new = base+int(rng.integers(-32,33))
            else:
                new = int(rng.integers(1,X+1))
            if 0<new<=X and new not in B:
                added.add(new)
        kept_array = np.array(sorted(kept),dtype=np.int64)
        delta = np.zeros(X+1,dtype=np.int64)
        for sign,changed in ((-1,removed),(1,added)):
            changed_array = np.array(sorted(changed),dtype=np.int64)
            distances = np.abs(changed_array[:,None]-kept_array[None,:]).ravel()
            delta += sign*np.bincount(distances,minlength=X+1)
            delta += sign*pair_counts(changed,X)
        affected = np.flatnonzero(delta)
        proposed = counts[affected]+delta[affected]
        assert np.all(proposed>=0)
        change = int((cost(proposed,r)-cost(counts[affected],r)).sum())
        temperature = 8*(.2/8)**(step/max(1,steps-1))
        if change<=0 or math.log(float(rng.random())) < -change/temperature:
            B = kept|added
            counts[affected] = proposed
            E += change
            accepted += 1
            if E<bestE:
                bestE,bestB,beststep = E,sorted(B),step
                current_N = int(np.count_nonzero(counts))
                if 64*E*E < k*k*r or (k+2*E)**2 < r*r*current_N:
                    break
        if step%500==499:
            assert np.array_equal(counts,pair_counts(B,X))
            assert E == int(cost(counts,r).sum())
        if step%3000==0:
            history.append(dict(step=step,best_E=bestE,current_E=E))
            print(json.dumps(history[-1]),flush=True)
    certified = certify(bestB,r,X)
    assert certified['E'] == bestE
    out = dict(host=socket.gethostname(),seed=seed,k=k,r=r,ambient=[0,X],
               steps=step+1,step_cap=steps,chains=1,swap_sizes=[1,2,4],initial_E=initial,
               best_step=beststep,accepted=accepted,history=history,
               seconds=time.monotonic()-start,result=certified,
               interpretation='One incomplete heuristic box; no general multiplicity obstruction or asymptotic family',
               GPU_deployment_justified=False,status='PASS')
    path = Path('.research/experiments/multiplicity_l1_2026-10-23/results.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',output=str(path),E=bestE,
        N=certified['N'],R_upper=certified['R_upper_display'],
        defect_ratio=certified['defect_ratio_display'],
        defect_target_passed=certified['defect_target_passed'],
        half_constant_upper_passed=certified['half_constant_upper_passed'])),flush=True)


if __name__=='__main__':
    main()
