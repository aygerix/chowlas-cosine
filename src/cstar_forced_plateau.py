"""Boolean forced plateaus: probe an obstruction to global L4 completion.

All computation runs on Dirichlet. The asymptotic existence proof uses
Spencer rounding; this script supplies finite witnesses, exact profile
checks, and separate all-circle ball-arithmetic upper bounds for M.
Finite random/MIP witnesses do not implement the asymptotic rounding proof.
"""
from fractions import Fraction as F
import json
import math
import os
from pathlib import Path
import socket
import time

import flint
import gurobipy as gp
from gurobipy import GRB
import numpy as np


def correlation(L, a):
    n = L - 1 - a
    if n <= 0:
        return 0
    s1 = n * (n + 1) // 2
    s2 = n * (n + 1) * (2*n + 1) // 6
    s3 = s1 * s1
    s4 = n * (n + 1) * (2*n + 1) * (3*n*n + 3*n - 1) // 30
    return (s4 - 2*(L-a)*s3 + (L*L-3*L*a+a*a)*s2
            + L*a*(L-a)*s1)


def exact_checks():
    count = 0
    for L in range(2, 33):
        v = [j*(L-j) for j in range(L+1)]
        energy = (L**5-L)//30
        assert sum(x*x for x in v) == energy
        assert sum((v[j]-v[j-1])**2 for j in range(1,L+1)) == L*(L*L-1)//3
        total = 0
        for a in range(L):
            value = sum(v[j]*v[j+a] for j in range(L+1-a))
            assert correlation(L,a) == value
            assert 0 <= value <= energy
            assert (energy-value)*(L*L+1) <= 5*a*a*energy
            if a:
                total += value
            count += 1
        assert F(total,energy) == F(5*L*(L*L-1),12*(L*L+1))-F(1,2)
    return dict(lengths=[2,32],correlations_checked=count,verified=True)


def sample_candidate(p, b, target, rng):
    eta = (rng.random(len(p)) < p).astype(int)
    eta[:b] = 1
    while eta.sum() > target:
        choices = np.flatnonzero((eta == 1) & (np.arange(len(p)) >= b))
        eta[int(rng.choice(choices))] = 0
    while eta.sum() < target:
        choices = np.flatnonzero(eta == 0)
        eta[int(rng.choice(choices))] = 1
    return eta


def mip_improve(eta, L, b, tl):
    grid = 16*L
    angles = 2*np.pi*np.arange(grid//2+1)/grid
    tail = np.arange(b+1,L-1)
    C = np.cos(np.outer(angles,tail))
    prefix = np.cos(np.outer(angles,np.arange(1,b+1))).sum(axis=1)
    model = gp.Model('forced_plateau')
    model.Params.OutputFlag = 0
    model.Params.Threads = int(os.environ.get('CHOWLA_WORKERS','2'))
    model.Params.TimeLimit = tl
    model.Params.MIPFocus = 1
    x = model.addMVar(len(tail),vtype=GRB.BINARY,name='tail')
    M = model.addVar(lb=0,name='M_grid')
    model.addConstr(x.sum() == int(eta.sum())-b)
    model.addConstr(C@x + M >= -prefix)
    x.Start = eta[b:]
    coeff = np.zeros(grid);coeff[1:L-1] = eta
    M.Start = float(-np.fft.fft(coeff).real.min())+1e-8
    model.setObjective(M,GRB.MINIMIZE)
    model.optimize()
    out = dict(status=int(model.Status),solutions=int(model.SolCount),
               gurobi=list(gp.gurobi.version()),time_limit=tl)
    if model.SolCount:
        eta[b:] = np.rint(x.X).astype(int)
        out['grid_objective_float'] = float(M.X)
    model.dispose()
    return eta,out


def certify(A, L):
    # Nearest grid point to an actual global minimizer has value at most
    # min f + (pi/Q)^2 sum a^2/2, since f'(x_min)=0.
    Q = 1 << math.ceil(math.log2(8*L**1.25))
    flint.ctx.prec = 96
    v = [flint.acb(0)]*Q
    for a in A:
        v[a] = flint.acb(1)
    values = flint.acb.dft(v)
    hint = math.ceil(max(-float(z.real.mid()) for z in values))+1
    assert all(z.real+hint > 0 for z in values)
    del v,values
    # pi<22/7 gives a purely rational remainder after the ball grid check.
    remainder = F(242*sum(a*a for a in A),49*Q*Q)
    bound = hint+remainder
    return dict(method='96-bit Arb DFT grid enclosure plus global-minimum second derivative bound',
                grid=Q,grid_M_upper_integer=hint,remainder=str(remainder),
                M_upper_rational=str(bound),R_upper_float=float(bound)/math.sqrt(len(A)),
                flint_version=flint.__version__,verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    start=time.time()
    path=Path('.research/experiments/forced_plateau_2026-10-20/results.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    out=dict(qualification='Finite Boolean witnesses, not Chowla counterexamples or exact extremizers.',
             exact_checks=exact_checks(),cases=[])
    for t in [2,3,4,5]:
        L,b=t**6,t**5
        energy=(L**5-L)//30
        numerators=[correlation(L,a) for a in range(1,L-1)]
        deficit=F(sum(energy-z for z in numerators[:b]),energy)
        for a,z in enumerate(numerators,start=1):
            assert 0<=z<=energy
            assert (energy-z)*(L*L+1)<=5*a*a*energy
        pnum=[energy if a<=b else z for a,z in enumerate(numerators,start=1)]
        mass=F(sum(pnum),energy)
        p=np.array([z/energy for z in pnum])
        target=(2*mass.numerator+mass.denominator)//(2*mass.denominator)
        rng=np.random.default_rng(20261020+t)
        grid=16*L;best=None
        for _ in range(32):
            eta=sample_candidate(p,b,target,rng)
            z=np.zeros(grid);z[1:L-1]=eta
            score=float(-np.fft.fft(z).real.min())
            if best is None or score<best[0]:best=(score,eta)
        eta=best[1]
        solver=None
        if t<=3:
            eta,solver=mip_improve(eta,L,b,30)
        A=(np.flatnonzero(eta)+1).tolist()
        assert A[:b]==list(range(1,b+1)) and len(A)==target
        certificate=certify(A,L)
        N=2*len(A)
        lower=F(b**4,(b+1)*N*N)
        row=dict(t=t,L=L,b=b,n=len(A),N=N,A=A,seed=20261020+t,
                 profile_mass=str(mass),forced_deficit=str(deficit),
                 mean_profile_M_upper=str(F(1,2)+deficit),
                 completion_fourth_over_N2_lower=str(lower),
                 completion_over_sqrt_N_lower_float=float(lower)**.25,
                 solver=solver,certificate=certificate,
                 seconds_since_start=time.time()-start)
        out['cases'].append(row)
        path.write_text(json.dumps(out,separators=(',',':'))+'\n')
        print(json.dumps({k:row[k] for k in ['t','L','b','n','completion_over_sqrt_N_lower_float','certificate','seconds_since_start']}),flush=True)


if __name__=='__main__':main()
