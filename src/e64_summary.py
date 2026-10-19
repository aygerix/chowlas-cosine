"""Summarize E64 run logs (examples/e64/run_*.log): final records and last incumbents."""
import glob, json
for f in sorted(glob.glob("examples/e64/run_*.log")):
    fin = None; inc = None; setup = None
    for l in open(f):
        try: d = json.loads(l)
        except Exception: continue
        if d.get("event") == "final": fin = d
        elif d.get("event") == "incumbent": inc = d
        elif d.get("event") == "setup": setup = d
    if fin:
        print(f.split("/")[-1], {k: (round(fin[k], 4) if isinstance(fin[k], float) else fin[k]) for k in
              ["nD", "M_D", "Mt", "nE", "bound", "optimal", "lam", "M_A", "R_A", "R_Bu", "pinch", "secs"] if k in fin})
    elif setup:
        print(f.split("/")[-1], "RUNNING", dict(nD=setup["nD"], Mt=round(setup["Mt"], 4)), inc)
