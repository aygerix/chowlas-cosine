"""Revalidate a saved weighted primal and rebuild its correctly supported dual.

A candidate computed with extra zero-data constraints remains a feasible
upper-bound candidate when those constraints are removed. Its old dual need
not remain valid. This script discards the zero-data multipliers and evaluates
the resulting actual-support dual. All integrals here remain floating diagnostics.
"""
import argparse
import json
from pathlib import Path
import socket
import numpy as np
from scipy.fft import next_fast_len


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run on dirichlet through src/dirun.sh')
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    rows = []
    for old in json.loads(args.source.read_text())['cases']:
        if 'coefficients' not in old:
            continue
        indices, values = np.array(old['support']), np.array(old['values'])
        mask = values != 0
        removed = indices[~mask].tolist()
        indices, values = indices[mask], values[mask]
        c = np.array(old['coefficients'])
        c[indices - 1] = values
        B = len(c)
        L = next_fast_len(max(64 * B, 256))
        spectrum = np.zeros(L)
        spectrum[1:B+1], spectrum[-B:] = c, c[::-1]
        q = np.fft.ifft(spectrum).real * L
        fourth = float(np.mean(q ** 4))
        cube = np.fft.fft(q ** 3).real / L
        uspec = np.zeros(L)
        uspec[0] = cube[0]
        uspec[indices], uspec[-indices] = cube[indices], cube[indices]
        u = np.fft.ifft(uspec).real * L
        norm = float(np.mean(np.abs(u) ** (4/3)) ** (3/4))
        dual = float(2 * values @ cube[indices] / norm)
        N = float(2 * values @ values)
        row = dict(tag=old['tag'], source=str(args.source), removed_zero_constraints=removed,
                   optimization_status='no optimization; revalidated saved polynomial',
                   B=B, N=N, fourth_power=fourth, fourth_power_over_N2=fourth/N**2,
                   L4_over_sqrt_N=fourth**.25/N**.5,
                   dual_L4_lower_over_sqrt_N_float=dual/N**.5,
                   dual_primal_ratio_float=dual/fourth**.25,
                   support=indices.tolist(), values=values.tolist(), coefficients=c.tolist(),
                   qualification='actual-support primal/dual floating diagnostics; not certified optimality')
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ['support','values','coefficients']}))
    args.output.write_text(json.dumps(dict(cases=rows), separators=(',', ':'))+'\n')


if __name__ == '__main__':
    main()
