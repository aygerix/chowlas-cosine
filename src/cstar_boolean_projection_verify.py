"""Independent exact polynomial certificate for the small projection output.

The producer's all-circle certificate is an Arb DFT plus Taylor bound.
Here a rational Chebyshev/Sturm chain independently checks the first
new upper, and direct high-precision points check every saved lower.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket

import flint
from cstar_resolvent_verify import check_upper


def ball(value):
    return flint.arb(value.numerator)/value.denominator


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    root = Path('.research/experiments/boolean_projection_2026-10-21')
    data = json.loads((root/'results.json').read_text())
    out = dict(status='PASS', host=socket.gethostname(), cases=[])
    flint.ctx.prec = 256
    for row in data['cases']:
        A, seed, n = row['A'], row['seed_A'], row['n']
        assert A == sorted(set(A)) and len(A) == n and min(A) > 0
        assert len(seed) == n and max(A) <= row['X']
        assert math.gcd(*A) == 1
        cert = row['candidate_certificate']
        lower, upper = F(cert['M_lower']), F(cert['M_upper'])
        grid, j = cert['grid'], cert['independent_point_index']
        angle = 2*flint.arb.pi()*j/grid
        point = sum(((angle*a).cos() for a in reversed(A)), flint.arb(0))
        assert point+ball(lower) < 0
        remainder = F(242*sum(a*a for a in A), 49*grid*grid)
        assert remainder == F(cert['Taylor_remainder']) <= F(1, 100)
        assert upper == F(cert['grid_M_upper'])+remainder
        assert lower*lower > F(n, 4)
        assert lower*lower > F(81*n, 400)
        assert upper < F(row['seed_certificate']['M_lower'])
        sturm = check_upper(A, upper) if n == 56 else None
        normalized_lower = ball(lower)/flint.arb(n).sqrt()
        normalized_upper = ball(upper)/flint.arb(n).sqrt()
        out['cases'].append(dict(n=n, X_actual=max(A),
            frequencies_removed=len(set(seed)-set(A)),
            frequencies_added=len(set(A)-set(seed)),
            candidate_mod3_counts=[sum(a % 3 == r for a in A) for r in range(3)],
            seed_mod3_counts=[sum(a % 3 == r for a in seed) for r in range(3)],
            actual_lowM_verified=(upper*upper < n),
            R_lower_ball=str(normalized_lower), R_upper_ball=str(normalized_upper),
            point_lower_independently_checked=True,
            all_circle_Sturm_upper_verified=(sturm is not None),
            Sturm_chain_length=sturm,
            all_circle_Arb_upper_from_producer=True,
            strict_seed_improvement_verified=True,
            below_half_constant=False,
            qualification='Improves the specified seed; no global or repository record claim.'))
        print(json.dumps(out['cases'][-1]), flush=True)
    out['GPU_deployment_justified'] = False
    (root/'verification.json').write_text(json.dumps(out, indent=2)+'\n')


if __name__ == '__main__':
    main()
