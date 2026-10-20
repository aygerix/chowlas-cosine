"""Independent standard-library verification of cone-noise identities.

Enumerates det=0 lexicographically, reconstructs Fourier kernels by residue
counts, and checks a complete explicit eigenbasis. Imports no producer code
and uses no floating arithmetic. Run on Dirichlet.
"""
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import socket
import time


def direction(x,p):
    pivot=next(a for a in x if a)
    inverse=pow(pivot,-1,p)
    return tuple(a*inverse%p for a in x)


def verify(source):
    p=source['p'];m=p+1;l=p-1
    V=list(itertools.product(range(p),repeat=4))
    Q=[x for x in V if (x[0]*x[3]-x[1]*x[2])%p==0]
    size=len(Q);d=size-1
    assert Q[0]==(0,0,0,0) and size==source['cone_size']
    kernel={}
    for x in V:
        counts=[0]*p
        for y in Q:
            counts[sum(a*b for a,b in zip(x,y))%p]+=1
        assert len(set(counts[1:]))==1
        transform=counts[0]-counts[1]
        assert transform%p==0
        kernel[x]=transform//p
    B=[[kernel[tuple((a-b)%p for a,b in zip(x,y))] for y in Q] for x in Q]
    lines=[(1,t) for t in range(p)]+[(0,1)]
    labels=[];cells=[[[] for _ in range(m)] for _ in range(m)]
    for i,x in enumerate(Q):
        if i==0:
            labels.append(None);continue
        a,b,c,e=x
        u=direction((a,c) if a or c else (b,e),p)
        v=direction((a,b) if a or b else (c,e),p)
        ui,vi=lines.index(u),lines.index(v)
        up=0 if u[0] else 1;vp=0 if v[0] else 1
        scalar=x[2*up+vp]
        assert scalar and x==tuple(scalar*z*w%p for z in u for w in v)
        labels.append((ui,vi,scalar))
        cells[ui][vi].append(i)
    assert all(len(cell)==l for row in cells for cell in row)
    def eig(sparse,eigenvalue):
        assert all(sum(B[i][j]*a for j,a in sparse.items())==eigenvalue*sparse.get(i,0)
                   for i in range(size))
    # Each of the two full plane families is a 1-eigenvector of T.
    for u in range(m):
        eig({i:1 for i in [0]+[j for cell in cells[u] for j in cell]},p**3)
    for v in range(m):
        eig({i:1 for i in [0]+[j for u in range(m) for j in cells[u][v]]},p**3)
    # Scalar differences: independent basis of every within-cell zero-sum space.
    for row in cells:
        for cell in row:
            for i in cell[1:]:eig({cell[0]:-1,i:1},p*p)
    # Rectangular interactions: a basis for zero row/column cell sums.
    for u in range(p):
        for v in range(p):
            sparse={i:sign for a,b,sign in [(u,v,1),(u,p,-1),(p,v,-1),(p,p,1)]
                    for i in cells[a][b]}
            eig(sparse,p)
    eig({i: (-(p*p-1) if i==0 else 1) for i in range(size)},p)
    # Linear independence of the listed subspaces follows from disjoint
    # cell sums/zero-sum conditions. Plane vectors have just one relation;
    # check their exact Gram rank, rather than assuming independence.
    planes=[]
    for u in range(m):planes.append({0}|{j for cell in cells[u] for j in cell})
    for v in range(m):planes.append({0}|{j for u in range(m) for j in cells[u][v]})
    gram=[[F(len(a&b)) for b in planes] for a in planes]
    rank=0
    for col in range(len(gram)):
        pivot=next((i for i in range(rank,len(gram)) if gram[i][col]),None)
        if pivot is None:continue
        gram[rank],gram[pivot]=gram[pivot],gram[rank]
        z=gram[rank][col];gram[rank]=[a/z for a in gram[rank]]
        for i in range(rank+1,len(gram)):
            z=gram[i][col]
            if z:gram[i]=[a-z*b for a,b in zip(gram[i],gram[rank])]
        rank+=1
    assert rank==2*p+1
    checked=[]
    for row in source['probes']:
        mask=int(row['mask_hex'],16)
        eta=[0]*size
        for i,label in enumerate(labels[1:],1):
            u,v,z=label
            eta[i]=(mask >> ((u*m+v)*l+z-1))&1
        count=sum(eta);s=F(count,d)
        assert count==row['count']
        E=[d*bit-count for bit in eta];E[0]=0
        inside=F(sum(E[i]*sum(b*e for b,e in zip(B[i],E)) for i in range(size)),p**3*d*d)
        total=F(sum(e*e for e in E),d*d)
        leakage=total-inside
        assert total==F(row['error_energy']) and inside==F(row['inside_energy'])
        assert leakage==F(row['outside_energy'])
        means=[[F(sum(eta[i] for i in cell),l) for cell in line] for line in cells]
        r=[sum(line)/m for line in means]
        c=[sum(means[u][v] for u in range(m))/m for v in range(m)]
        within=l*sum((a*(1-a) for line in means for a in line),F(0))
        interaction=l*sum(((means[u][v]-r[u]-c[v]+s)**2 for u in range(m) for v in range(m)),F(0))
        assert within==F(row['within_line_energy'])
        assert interaction==F(row['grid_interaction_energy'])
        assert leakage==(1-F(1,p))*within+(1-F(1,p*p))*interaction
        mistakes=sum(int(eta[i] != (r[u]+c[v]-s>=F(1,2)))
                     for i,label in enumerate(labels) if label is not None
                     for u,v,z in [label])
        assert mistakes==row['two_ruling_threshold_hamming']
        assert mistakes<=F(4*p,p-1)*leakage
        if row['name']=='mixed_two_planes':
            assert count==(p-1)*(2*p+1)
            assert leakage==F((p-1)**2,p+1)
            assert F(row['leakage_fraction'])==F(p*p-1,p*p*(2*p+1))
            assert row['closest_single_ruling_hamming']==p*(p-1)
        checked.append(dict(name=row['name'],verified=True,threshold_hamming=mistakes))
    return dict(p=p,full_eigenbasis_checked=True,plane_span_rank=rank,
                exact_fourier_residue_counts=len(V),probes=checked,verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    started=time.monotonic()
    root=Path('.research/experiments/cone_confinement_2026-10-20')
    results=json.loads((root/'results.json').read_text())
    out=dict(qualification='Independent exact standard-library finite-field and eigenbasis checks; '
             'not an external-agent or Lean audit of the all-prime proof.',cases=[])
    for row in results['cases']:
        result=verify(row);out['cases'].append(result);print(json.dumps(result),flush=True)
    out['seconds']=time.monotonic()-started
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
