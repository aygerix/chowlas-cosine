"""Gurobi probe: change disk-center marginals while fixing expected size.

Single-fiber, D4-symmetric fractional profiles on a two-torus. This does
not output Boolean Chowla sets or certify an all-circle upper bound.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import flint
import gurobipy as gp
import numpy as np
from scipy.optimize import minimize


def orbit(a,b):
    return sorted(set((s*x,t*y) for x,y in [(a,b),(b,a)] for s in [-1,1] for t in [-1,1]))


def rationalize(values,counts,target):
    active=sorted(range(len(values)),key=lambda i:-values[i])
    j,k=next((j,k) for j in active for k in active if j!=k and counts[j]!=counts[k]
             and values[j]>1e-7 and values[k]>1e-7)
    p=[F(math.floor(max(0,x)*10**10),10**10) for x in values]
    rest=1-sum(p[i] for i in range(len(p)) if i not in (j,k))
    mass=target-sum(p[i]*counts[i] for i in range(len(p)) if i not in (j,k))
    p[j]=(mass-counts[k]*rest)/(counts[j]-counts[k]);p[k]=rest-p[j]
    assert min(p)>=0 and sum(p)==1 and sum(p[i]*counts[i] for i in range(len(p)))==target
    return p


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=160;out=dict(qualification='Two-dimensional fractional center-law probes only; '
                  'no all-phase upper bounds or Boolean outputs.',cases=[])
    root=Path('.research/experiments/wide_mean_2026-10-20')
    for R in [8,16,32]:
        disk=[(a,b) for a in range(-R,R+1) for b in range(-R,R+1) if a*a+b*b<=R*R]
        W=[w for w in disk if w!=(0,0)];arr=np.array(W);B=len(disk)
        centers=[(a,b) for a in range(R+1) for b in range(a+1) if a*a+b*b<=R*R]
        coeff=[];sizes=[];counts=[]
        for a,b in centers:
            T=orbit(a,b);s=len(T);sizes.append(s);v=np.zeros(len(W),dtype=np.int16)
            for t in T:
                plus=arr+np.array(t);minus=arr-np.array(t)
                v+=((plus*plus).sum(axis=1)<=R*R)&((minus*minus).sum(axis=1)<=R*R)
            coeff.append(v);counts.append(F(int(v.sum()),2*s))
        integer=np.array(coeff);C=integer/np.array(sizes)[:,None]
        uniform=[F(s,B) for s in sizes];target=sum(p*n for p,n in zip(uniform,counts))
        parity=C@np.array([[1-2*(a%2),1-2*((a+b)%2)] for a,b in W])
        # Stage one only asks whether changing the center law repairs parity.
        model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2
        p=model.addMVar(len(centers),lb=0,ub=1);delta=model.addVar(lb=-B)
        model.addConstr(p.sum()==1);model.addConstr(np.array(list(map(float,counts)))@p==float(target))
        model.addConstr(parity.T@p>=delta);model.setObjective(delta,gp.GRB.MAXIMIZE);model.optimize()
        assert model.Status==gp.GRB.OPTIMAL
        stage_delta=delta.X;floor=max(0,min(1e-4,stage_delta/2))
        # Optimize a grid with repaired parity. The grid is only a probe.
        grid=np.array([(math.pi*i/32,math.pi*j/32) for i in range(33) for j in range(i+1)])
        D=C@np.cos(arr@grid.T)
        model.remove(model.getConstrs()[-2:]);model.update()
        model.addConstr(parity.T@p>=floor)
        b=model.addVar(lb=0);model.addConstr(D.T@p>=-b)
        model.setObjective(b,gp.GRB.MINIMIZE);model.optimize()
        assert model.Status==gp.GRB.OPTIMAL
        probabilities=rationalize(p.X,counts,target)
        weighted=[sum(probabilities[i]*int(integer[i,j])/sizes[i] for i in range(len(centers)))
                  for j in range(len(W))]
        pv=[sum(c*(1-2*((a*v[0]+bb*v[1])%2)) for (a,bb),c in zip(W,weighted))
            for v in [(1,0),(0,1),(1,1)]]
        assert min(pv)>=0
        cf=np.array(list(map(float,weighted)))
        def objective(q):return float(cf@np.cos(arr@q))
        def gradient(q):return -(cf*np.sin(arr@q))@arr
        grid_values=D.T@np.array(list(map(float,probabilities)))
        seeds=grid[np.argsort(grid_values)[:32]]
        opt=[minimize(objective,q,jac=gradient,method='L-BFGS-B',bounds=[(0,math.pi)]*2) for q in seeds]
        best=min(opt,key=lambda a:a.fun);q=[F(float(z)) for z in best.x]
        value=flint.arb(0)
        for (a,bb),c in zip(W,weighted):
            angle=a*q[0]+bb*q[1]
            value+=(flint.arb(angle.numerator)/angle.denominator).cos()*c.numerator/c.denominator
        lower=F(max(0,math.floor(-float(value.mid())*10**8)-2),2*10**8)
        assert value+2*flint.arb(lower.numerator)/lower.denominator<0
        row=dict(R=R,disk_size=B,center_representatives=centers,orbit_sizes=sizes,
                 probabilities=list(map(str,probabilities)),expected_n=str(target),
                 repaired_parity_D=list(map(str,pv)),max_parity_floor_float=stage_delta,
                 optimized_grid_M_float=b.X/2,adversarial_phase_rationals=list(map(str,q)),
                 adversarial_D_ball=str(value),point_M_lower_rational=str(lower),
                 ratio_to_sqrt_expected_n_float=float(lower)/math.sqrt(float(target)),
                 status='exact mass and parity; Arb point lower bound; grid upper unproved')
        out['cases'].append(row);(root/'center_law.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:row[k] for k in ['R','expected_n','max_parity_floor_float',
                      'optimized_grid_M_float','point_M_lower_rational','ratio_to_sqrt_expected_n_float']}),flush=True)


if __name__=='__main__':main()
