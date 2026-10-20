"""Targeted equality/inequality L4 probes and exact weighted sign control.

Run on Dirichlet. Finite convex solves and sampled dual integrals remain
numerical. The single-frequency coefficient ratios below are exact.
"""
import contextlib
from fractions import Fraction as F
import io
import json
from pathlib import Path
import socket

import numpy as np
from cstar_l4_completion import solve


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    alpha = F(1, 3)
    moment3 = (alpha + 2) / (alpha + 3)
    moment5 = moment3 * (alpha + 4) / (alpha + 5)
    ratio3 = 4 * moment3 - 3
    ratio5 = 16 * moment5 - 20 * moment3 + 5
    assert ratio3 == F(-1, 5) and ratio5 == F(1, 10)
    cases = [
        ('weighted_1_5', [1, 5], [1, .01], 100),
        ('hereditary_8', [1, 2, 3, 4, 5, 6, 7, 9], None, 36),
        ('threshold_miss_10', [1, 2, 3, 4, 5, 6, 7, 8, 9, 13], None, 52),
        ('interval_32', list(range(1, 33)), None, 64),
    ]
    rows = []
    for tag, A, values, B in cases:
        values = np.ones(len(A)) if values is None else np.array(values)
        for relaxed in [False, True]:
            with contextlib.redirect_stdout(io.StringIO()):
                row = solve(tag, np.array(A), values, B, 30,
                            lower_bounds_only=relaxed)
            rows.append(row)
            print(json.dumps({k: row.get(k) for k in [
                'tag', 'constraint_kind', 'status', 'L4_over_sqrt_N',
                'dual_L4_lower_over_sqrt_N_float',
                'selected_coefficient_max_slack',
                'negative_dual_support_coefficients']}), flush=True)
    out = dict(
        qualification='Numerical comparisons, not unrestricted optimality or a Boolean sign theorem.',
        exact_single_frequency_ratios=dict(alpha=str(alpha), third=str(ratio3),
                                          fifth=str(ratio5)),
        cases=rows)
    path = Path('.research/experiments/dual_deletion_2026-10-20/partial_majorant.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, separators=(',', ':')) + '\n')


if __name__ == '__main__':
    main()
