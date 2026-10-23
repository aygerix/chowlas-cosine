"""Exact rational certificate for the cubic-PD support-cap envelope.

Legacy rational polynomial and Schur helpers are reused read-only.
Every pointwise sign is certified by rational Bernstein coefficients;
the tangent branch is squared with its positive denominator retained.
Discovery is only an input proposal. Run on shared Dirichlet.
"""
import json
import math
from pathlib import Path
import socket
import time


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    source = Path('examples/r11_certificates/certify.py').read_text()
    helpers = source.split('def run(', 1)[0]
    ns = {'__name__': 'legacy_rational_helpers'}
    exec(compile(helpers, 'legacy_rational_helpers', 'exec'), ns)
    Q = ns['Q']
    add, mul, compose, peval = [ns[name] for name in ('add', 'mul', 'compose', 'peval')]
    bern, bpower, cosupper, sqrt_floor, schur_poly, divide_endpoint = [
        ns[name] for name in ('bern', 'bpower', 'cosupper', 'sqrt_floor', 'schur_poly', 'divide_endpoint')]
    root = Path('.research/experiments/cubic_cap_2026-10-23')
    input_path = root/'discovery_sigma0.6667_K64_d10_s0.1_t0.json'
    rec = json.loads(input_path.read_text())
    assert rec['cubic_cap_envelope'] and not rec['certified']
    K, degree, shape = rec['K'], rec['degree'], Q(str(rec['shape']))
    D = Q(29, 400)
    slack = Q(1, 10000)
    aa = [Q(math.ceil(x*10**9), 10**9)+slack for x in rec['a']]
    bs = [[Q(round(x*10**10), 10**10) for x in row] for row in rec['beta']]
    for row in bs:
        row[0] = Q(0)
        for j in range(1, len(row)):
            row[j] = max(row[j], row[j-1])
    assert min(aa) >= 0
    assert all(len(row) == degree+1 and row[0] == 0 and all(row[i] <= row[i+1] for i in range(degree)) for row in bs)
    beta = [bpower(row) for row in bs]
    xpoly = [Q(1), Q(0), -Q(1)]
    vpoly = [Q(2, 3), Q(0), -Q(4, 3), Q(0), Q(2, 3)]
    radical = [Q(1, 12), Q(0), Q(1, 3), Q(0), -Q(1, 6)]
    gram = json.loads(Path('.research/agents/tdense9_scratch/long_gram_bounds.json').read_text())
    support = json.loads(Path('examples/r11_certificates/support_lines.json').read_text())
    common = [[Q(0)], [Q(1), Q(0), -Q(4), Q(0), Q(2)], [Q(1), -Q(1), -Q(1)]]
    common += [[Q(row['m'])+Q(row['b']), Q(0), -Q(row['m'])] for row in gram]

    def cap_upper(cos_cap):
        # Grid denominator includes3, so2/3 is represented exactly.
        denominator = 3*10**9
        low, high = 0, 2*10**9
        target = Q(4, 27)*cos_cap*cos_cap
        while low < high:
            middle = (low+high)//2
            value = Q(middle, denominator)
            if value*value*(1-value) >= target:
                high = middle
            else:
                low = middle+1
        value = Q(high, denominator)
        assert 0 < value <= Q(2, 3) and value*value*(1-value) >= target
        return value

    started = time.monotonic()
    cells, failed = [], []
    tangent_count = 0
    for jj in range(2*K):
        j = jj//2
        k = (2*K+jj-1)//jj-1 if jj else None
        cap = min(Q(1), cosupper(k)) if jj else Q(1)
        bcap = cap_upper(cap)
        ulo = sqrt_floor(1-cap)
        branches = common+[[Q(row['m'])+Q(row['b']), Q(0), -Q(row['m'])]
                           for row in support.get(str(k), [])]
        base = add([aa[j]-Q(1, 2), Q(0), -aa[j]], [-v/2 for v in compose(beta[j], xpoly)])
        numerator = add([2-bcap], [-v for v in vpoly])
        expressions = {}
        def build(index):
            A = add(base, compose(beta[jj], branches[index])) if jj < K else base
            square_A = mul(A, A)
            lowP, lowfactor = divide_endpoint(add(radical, [-v for v in square_A]))
            highP, highfactor = divide_endpoint(add(mul(numerator, numerator), [-16*(1-bcap)*v for v in square_A]))
            expressions[index] = (A, lowP, lowfactor, highP, highfactor)
        pending = [(ulo, Q(1), 0)]
        leaves = []
        while pending:
            lo, hi, depth = pending.pop()
            middle = (lo+hi)/2
            candidates = sorted(range(len(branches)), key=lambda b: peval(branches[b], middle), reverse=True)[:3]
            valid = []
            for branch in candidates+[0]:
                values = bern(branches[branch], lo, hi)
                if min(values) >= 0 and max(values) <= 1:
                    valid.append(branch)
            valid.sort(key=lambda b: peval(branches[b], middle), reverse=True)
            complete = False
            for branch in valid:
                if branch not in expressions:
                    build(branch)
                A, lowP, lowfactor, highP, highfactor = expressions[branch]
                avals = bern(A, lo, hi)
                if min(avals) >= 0:
                    leaves.append(dict(lo=str(lo), hi=str(hi), branch=branch, mode='A', min=str(min(avals))))
                    complete = True
                    break
                tangent = peval(vpoly, hi) >= bcap
                P, factor = (highP, highfactor) if tangent else (lowP, lowfactor)
                pvals = bern(P, lo, hi)
                if min(pvals) >= 0:
                    mode = 'tangent' if tangent else 'radical'
                    leaves.append(dict(lo=str(lo), hi=str(hi), branch=branch, mode=mode,
                                       endpoint_factor=factor, min=str(min(pvals))))
                    tangent_count += int(tangent)
                    complete = True
                    break
            if complete:
                continue
            if depth >= 30:
                failed.append(dict(jj=jj, lo=str(lo), hi=str(hi)))
                break
            pending.extend([(lo, middle, depth+1), (middle, hi, depth+1)])
        cells.append(dict(jj=jj, support_k=k, cap=str(cap), cubic_cap=str(bcap), u_lower=str(ulo),
                          branches=[[str(v) for v in br] for br in branches], leaves=leaves))
        if failed:
            break
        if jj % 16 == 0:
            print('CAP_POINTWISE', jj, 'leaves', len(leaves), 'seconds', round(time.monotonic()-started, 2), flush=True)
    schur = []
    Utest = [Q(1), 4*shape, -4*shape]
    for cell in range(K):
        row = schur_poly(aa, shape, K, cell)
        difference = add([2*D*v for v in Utest], [-v for v in row])
        margin = min(bern(difference, Q(cell, K), Q(cell+1, K)))
        schur.append(dict(cell=cell, min_bernstein=str(margin), polynomial=list(map(str, difference))))
    good = not failed and len(cells) == 2*K and all(Q(row['min_bernstein']) >= 0 for row in schur)
    out = dict(status='PROVED' if good else 'UNRESOLVED', source=str(input_path), sigma='2/3',
               envelope='cubic_profile_support_cap_with_convex_tangent_extension',
               K=K, degree=degree, shape=str(shape), D1=str(D), dense_C=str(1/D),
               a=list(map(str, aa)), beta_bernstein=[[str(v) for v in row] for row in bs],
               beta_power=[[str(v) for v in row] for row in beta], pointwise=cells, failed=failed,
               schur=schur, min_schur=str(min(Q(row['min_bernstein']) for row in schur)),
               tangent_leaves=tangent_count, seconds=time.monotonic()-started)
    (root/'certificate.json').write_text(json.dumps(out, indent=2)+'\n')
    print('CAP_CERTIFICATE', json.dumps({k: v for k, v in out.items()
          if k not in ('a', 'beta_bernstein', 'beta_power', 'pointwise', 'schur')}, indent=2), flush=True)
    if not good:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
