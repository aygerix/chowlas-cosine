"""Exact falsification of the Boolean five-count phase-plane inequality.

This is a finite combinatorial test, not a minimum search. Existing
all-circle certificates supply the low-M premises. All research
computation runs on Dirichlet through dirun.sh.
"""
from fractions import Fraction
import itertools
import json
from pathlib import Path
import socket

from flint import fmpz_poly


def dot(p, q):
    return sum(int(p[j])*int(q[j]) for j in range(min(len(p), len(q))))


def counts(A):
    A = sorted(A)
    assert A and min(A) > 0 and len(A) == len(set(A))
    occupied = set(A)
    F = fmpz_poly([int(j in occupied) for j in range(max(A)+1)])
    F2 = F*F
    F3 = F2*F
    F4 = F2*F2
    t, E4, B, C = dot(F, F2), dot(F2, F2), dot(F3, F2), dot(F, F4)
    C5 = 2*B-C
    return dict(A=A,n=len(A),t=t,E4=E4,B=B,C=C,C5=C5,
                determinant_times_four=t*C5-E4*E4,
                ratio=str(Fraction(t*C5,E4*E4)))


def multiply(left, right):
    out = {}
    for a,c in left.items():
        for b,d in right.items():
            out[a+b] = out.get(a+b,0)+c*d
    return out


def independent_matrix(A):
    # Encode 2i*Im F and 2i*Im F² by signed Laurent integer arrays.
    F = {a:1 for a in A}
    F2 = multiply(F,F)
    vectors = [{**P,**{-a:-c for a,c in P.items()}} for P in (F,F2)]
    D = {**F,**{-a:c for a,c in F.items()}}
    Q, E = [], []
    for u in vectors:
        qrow, erow = [], []
        for v in vectors:
            uv = multiply(u,v)
            qrow.append(Fraction(-uv.get(0,0),4))
            erow.append(Fraction(-sum(c*uv.get(-a,0) for a,c in D.items()),4))
        Q.append(qrow)
        E.append(erow)
    return Q,E


def check_matrix(row):
    Q,E = independent_matrix(row['A'])
    assert Q == [[Fraction(row['n'],2),Fraction(row['t'],2)],
                 [Fraction(row['t'],2),Fraction(row['E4'],2)]]
    assert E == [[Fraction(row['t'],2),Fraction(row['E4'],2)],
                 [Fraction(row['E4'],2),Fraction(row['C5'],2)]]
    row['independent_Laurent_Q_and_energy_match'] = True


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    rows = []
    for filename in ('results','prefix'):
        source = Path(f'.research/experiments/zero_reciprocal_2026-10-21/{filename}.json')
        for saved in json.loads(source.read_text())['cases']:
            row = counts(saved['A'])
            M = Fraction(saved['M_upper'])
            assert M*M <= row['n']
            row.update(label=saved['label'],M_upper=str(M),premise_source=str(source))
            check_matrix(row)
            rows.append(row)
            print(json.dumps({k:row[k] for k in ('label','n','ratio','determinant_times_four')}),flush=True)
    # Stop after an actual-low-M falsifier; no unnecessary support sweep.
    lowM_falsifiers = [r for r in rows if r['determinant_times_four'] > 0]
    bounded = dict(executed=False,reason='Existing certified controls already falsify the sign'
                   if lowM_falsifiers else 'Pending bounded test')
    if not lowM_falsifiers:
        checked = 0
        first = None
        for n in range(2,17):
            for A in itertools.combinations(range(1,17),n):
                row = counts(A)
                checked += 1
                if row['determinant_times_four'] > 0:
                    check_matrix(row)
                    first = row
                    break
            if first is not None:
                break
        bounded = dict(executed=True,ambient=[1,16],order='cardinality then lexicographic',
                       checked=checked,first_falsifier=first,
                       qualification='No all-circle low-M premise for this bounded enumeration')
    out = dict(host=socket.gethostname(),cases=rows,bounded=bounded,
               lowM_sign_falsified=bool(lowM_falsifiers),
               qualification='Exact finite integer counts and independent Laurent matrices; no universal bound',
               status='PASS')
    path = Path('.research/experiments/phase_five_count_2026-10-23/results.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',output=str(path),
                         lowM_sign_falsified=bool(lowM_falsifiers),bounded=bounded)),flush=True)


if __name__ == '__main__':
    main()
