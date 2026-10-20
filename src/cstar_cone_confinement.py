"""Exact full cone-concentration spectrum and Boolean taper probes.

All research computation runs on Dirichlet. The proof uses only finite
Fourier orthogonality and the two rulings of det=0 in Mat_2(F_p).
No conclusion for integer Chowla supports is inferred from this model.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import socket
import time

import numpy as np


def projective(p):
    return [(1, t) for t in range(p)] + [(0, 1)]


def coordinates(p):
    lines = projective(p)
    points = [(0, 0, 0, 0)]
    cells = []
    for u in lines:
        for v in lines:
            cell = []
            for z in range(1, p):
                cell.append(len(points))
                points.append(tuple(z * a * b % p for a in u for b in v))
            cells.append(cell)
    assert len(set(points)) == len(points) == p**3 + p*p - p
    return np.array(points, dtype=np.int64), cells


def probe(p, points, cells, B, name, selected):
    m, l = p + 1, p - 1
    d = len(points) - 1
    assert 0 not in selected and selected
    bits = np.zeros(len(points), dtype=np.int64)
    bits[list(selected)] = 1
    count = len(selected)
    s = F(count, d)
    t = [[F(sum(int(bits[i]) for i in cells[u*m+v]), l)
          for v in range(m)] for u in range(m)]
    rows = [sum(row, F(0))/m for row in t]
    cols = [sum((t[u][v] for u in range(m)), F(0))/m for v in range(m)]
    within = l*sum((x*(1-x) for row in t for x in row), F(0))
    interaction = l*sum(((t[u][v]-rows[u]-cols[v]+s)**2
                         for u in range(m) for v in range(m)), F(0))
    ruling = l*m*(sum(((r-s)**2 for r in rows), F(0))
                  +sum(((c-s)**2 for c in cols), F(0)))
    energy = d*s*(1-s)
    assert energy == within+interaction+ruling
    # Integer numerator E=d*(eta-s), with E(0)=0.
    E = d*bits-count
    E[0] = 0
    inside = F(int(E @ B @ E), p**3*d*d)
    leakage = energy-inside
    predicted = (1-F(1,p))*within+(1-F(1,p*p))*interaction
    assert leakage == predicted
    assert inside == ruling+within/p+interaction/(p*p)
    # Independent full ambient FFT check, only corroboration of exact values.
    ambient = np.zeros((p,)*4)
    for point, value in zip(points, E):
        ambient[tuple(point)] = int(value)/d
    spectrum = np.fft.fftn(ambient, norm='ortho')
    fft_inside = sum(abs(spectrum[tuple(q)])**2 for q in points)
    assert abs(float(inside)-float(fft_inside)) < 1e-8*max(1,float(energy))
    # Exact distance to every single-ruling Boolean selector; independent
    # choices of rows/columns make the closest one a majority decision.
    row_errors = sum(min(sum(int(bits[i]) for v in range(m) for i in cells[u*m+v]),
                         l*m-sum(int(bits[i]) for v in range(m) for i in cells[u*m+v]))
                     for u in range(m))
    col_errors = sum(min(sum(int(bits[i]) for u in range(m) for i in cells[u*m+v]),
                         l*m-sum(int(bits[i]) for u in range(m) for i in cells[u*m+v]))
                     for v in range(m))
    threshold = {i for u in range(m) for v in range(m) if rows[u]+cols[v]-s >= F(1,2)
                 for i in cells[u*m+v]}
    threshold_error = len(selected.symmetric_difference(threshold))
    assert threshold_error <= 4*(within+interaction) <= F(4*p,p-1)*leakage
    even = all(bits[i] == bits[1+(i-1)//l*l+(p-2-(i-1)%l)] for i in range(1,len(bits)))
    record = dict(name=name, count=count, density=str(s), even=bool(even),
                  error_energy=str(energy), inside_energy=str(inside),
                  outside_energy=str(leakage), within_line_energy=str(within),
                  grid_interaction_energy=str(interaction), ruling_energy=str(ruling),
                  leakage_fraction=str(leakage/energy) if energy else None,
                  closest_single_ruling_hamming=min(row_errors,col_errors),
                  two_ruling_threshold_hamming=threshold_error,
                  mask_hex=hex(sum(1 << int(i-1) for i in selected)),
                  verified=True)
    return record


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    started = time.monotonic()
    out = dict(qualification='Exact finite full concentration operators and identities; '
               'FFT values are corroboration. No universal integer-support claim.',
               seed=20261022, numpy=np.__version__, cases=[])
    rng = np.random.default_rng(out['seed'])
    for p in (3,5,7):
        points,cells = coordinates(p)
        qsize = len(points)
        difference = (points[:,None,:]-points[None,:,:]) % p
        same_cone = ((difference[:,:,0]*difference[:,:,3]
                      -difference[:,:,1]*difference[:,:,2]) % p == 0)
        B = p*p*np.eye(qsize,dtype=np.int64)+p*same_cone.astype(np.int64)-1
        # B=p^3*T. Verify the complete minimal-polynomial identity over Z.
        B2 = B @ B
        B3 = B2 @ B
        roots = (p**3,p*p,p)
        poly = B3-sum(roots)*B2+sum(a*b for a,b in itertools.combinations(roots,2))*B
        poly -= np.prod(roots)*np.eye(qsize,dtype=np.int64)
        assert not np.any(poly)
        multiplicities = [2*p+1,(p+1)**2*(p-2),p*p+1]
        assert sum(multiplicities) == qsize
        assert int(np.trace(B)) == sum(a*b for a,b in zip(roots,multiplicities))
        assert int(np.trace(B2)) == sum(a*a*b for a,b in zip(roots,multiplicities))
        # Independently verify the finite-field Fourier kernel using exact
        # residue counts, not floating roots of unity or the rook formula.
        all_points = np.array(list(itertools.product(range(p),repeat=4)),dtype=np.int64)
        dot = (all_points @ points.T) % p
        for point, residues in zip(all_points,dot):
            counts = np.bincount(residues,minlength=p)
            if not np.any(point):
                assert counts[0] == qsize and not np.any(counts[1:])
            else:
                on_cone = (point[0]*point[3]-point[1]*point[2])%p == 0
                expected = p*p-p if on_cone else -p
                assert np.all(counts[1:] == counts[1])
                assert int(counts[0]-counts[1]) == expected
        m,l = p+1,p-1
        def cell_union(predicate):
            return {i for u in range(m) for v in range(m) if predicate(u,v)
                    for i in cells[u*m+v]}
        probes = [
            ('one_ruling',cell_union(lambda u,v:u<m//2)),
            ('balanced_permutation',cell_union(lambda u,v:u==v)),
            ('mixed_two_planes',cell_union(lambda u,v:u==0 or v==0)),
            ('scalar_even', {cell[j] for cell in cells for j in {0,l-1}}),
        ]
        random_even=set()
        for cell in cells:
            for j in range(l//2):
                if rng.random()<1/3:
                    random_even.update([cell[j],cell[l-1-j]])
        probes.append(('seeded_even',random_even))
        records=[probe(p,points,cells,B,name,selected) for name,selected in probes]
        assert records[0]['outside_energy']=='0'
        assert records[1]['ruling_energy']=='0'
        assert F(records[1]['leakage_fraction'])==1-F(1,p*p)
        mixed=records[2]
        assert F(mixed['leakage_fraction'])==F(p*p-1,p*p*(2*p+1))
        # This tends to zero, although distance to every single ruling stays
        # a positive fraction of the selected set. Record the countercontrol.
        row=dict(p=p,cone_size=qsize,nonzero_cone_size=qsize-1,
                 points_sha256=hashlib.sha256(points.tobytes()).hexdigest(),
                 spectrum=[dict(eigenvalue=str(F(r,p**3)),multiplicity=k)
                           for r,k in zip(roots,multiplicities)],
                 exact_cubic_identity=True,exact_fourier_residue_counts=True,
                 probes=records)
        out['cases'].append(row)
        print(json.dumps({k:v for k,v in row.items() if k!='probes'}),flush=True)
    out['seconds']=time.monotonic()-started
    root=Path('.research/experiments/cone_confinement_2026-10-20')
    root.mkdir(parents=True,exist_ok=True)
    (root/'results.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':
    main()
