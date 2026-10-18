"""Run bedert_avg.analyse on test families; writes examples-free JSON to src/agents/bedert_avg_results.json."""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from families import erdos_turan_sidon, difference_set  # noqa: E402
from singer import singer  # noqa: E402
from bu import A_of_S  # noqa: E402
from bedert_avg import analyse, summarize  # noqa: E402

ROOT = os.path.join(HERE, "..", "..")


def fam():
    out = []
    for p in (11, 23, 37):
        out.append((f"ET-Sidon-diff p={p}", difference_set(erdos_turan_sidon(p))))
    for q in (13, 23, 31):
        D, v = singer(q)
        out.append((f"Singer-diff q={q}", difference_set(D)))
    bu = json.load(open(os.path.join(ROOT, "examples", "bu_reproduction_certified.json")))
    for key in ("61_12", "101_20"):
        out.append((f"Bu {key}", A_of_S(bu[key]["S"])))
    for f in ("X120_s0", "X180_s1", "X260_s0"):
        d = json.load(open(os.path.join(ROOT, "examples", "dense_runs", f + ".json")))
        out.append((f"dense {f}", sorted(d["A"])))
    for L in (100, 400):
        out.append((f"interval [1,{L}]", list(range(1, L + 1))))
    rng = np.random.default_rng(1)
    D, v = singer(31)
    base = difference_set(D)
    for p in (0.5, 0.25):
        sub = sorted(x for x in base if rng.random() < p)
        out.append((f"Singer31-diff random p={p}", sub))
    sub = sorted(x for x in range(1, 301) if rng.random() < 0.5)
    out.append(("random dens 1/2 in [1,300]", sub))
    return out


if __name__ == "__main__":
    which = sys.argv[1:] if len(sys.argv) > 1 else None
    res = []
    for name, S in fam():
        if which and not any(w in name for w in which):
            continue
        t0 = time.time()
        M = max(S)
        over = 16 if M < 3000 else 8
        o = analyse(S, over=over, max_t=240, seed=0)
        d = summarize(name, o)
        d["secs"] = round(time.time() - t0, 1)
        d["over"] = over
        print(json.dumps(d), flush=True)
        res.append(d)
    fn = os.path.join(HERE, "bedert_avg_results.json")
    old = json.load(open(fn)) if os.path.exists(fn) else []
    names = {r["name"] for r in res}
    old = [r for r in old if r["name"] not in names]
    json.dump(old + res, open(fn, "w"), indent=1)
