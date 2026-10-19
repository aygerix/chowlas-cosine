"""Write D-files (examples/e64/D_bu_k*.json) holding Bu's set at the best shift, for second-level E64 runs."""
import json, sys
sys.path.insert(0, "src")
GOLOMB = {6: [0, 1, 4, 10, 12, 17], 7: [0, 1, 4, 10, 18, 23, 25], 8: [0, 1, 4, 9, 15, 22, 32, 34]}
from box_minlam import true_min


def bu(S):
    D = sorted({b - a for a in S for b in S if b > a})
    E = sorted({abs(3 * (a + b) + 1) for i, a in enumerate(S) for b in S[i + 1:]})
    return sorted(set(3 * d for d in D) | set(E))


for k in map(int, sys.argv[1:]):
    G = GOLOMB[k]; best = None
    for c in range(-max(G) - 1, 1):
        A = bu([g + c for g in G]); (fm, _), _, _ = true_min(A)
        if best is None or -fm < best[0]:
            best = (-fm, c, A)
    json.dump(dict(A=best[2], M=best[0], shift=best[1], k=k), open(f"examples/e64/D_bu_k{k}.json", "w"))
    print(k, best[0], len(best[2]), max(best[2]))
