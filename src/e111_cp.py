"""E111 side computation; run ONLY through src/dirun.sh on dirichlet.

Flat/nonnegative integer-level block LP, Gurobi MILP pricing, exact rational
primal repair, FFT comparison and reproducible add/remove/swap falsification.
All output is confined to examples/e111. No project research notes are changed.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import random
import socket
import sys
sys.dont_write_bytecode = True
import time

import gurobipy as gp
from gurobipy import GRB
import numpy as np
from scipy.optimize import minimize_scalar

OUT = Path("examples/e111")
TOL = 1e-8
ENV = None


def model(name):
    global ENV
    if ENV is None:
        ENV = gp.Env(empty=True)
        ENV.setParam("OutputFlag", 0)
        ENV.start()
    m = gp.Model(name, env=ENV)
    m.Params.OutputFlag = 0
    m.Params.Threads = min(2, int(os.environ.get("CHOWLA_WORKERS", "1")))
    m.Params.FeasibilityTol = 1e-9
    m.Params.OptimalityTol = 1e-9
    m.Params.IntFeasTol = 1e-9
    m.Params.MIPGap = 0
    m.Params.MIPGapAbs = 1e-9
    m.Params.Seed = 20261019
    return m


def normalized(B):
    B = sorted(B)
    return tuple(b - B[0] for b in B)


def differences(B):
    return {v-u for i, u in enumerate(B) for v in B[i+1:]}


def column(B, levels=None):
    if levels is None:
        levels = (1,) * len(B)
    counts = Counter()
    for i, b in enumerate(B):
        for j in range(i+1, len(B)):
            counts[B[j]-b] += levels[i] * levels[j]
    return counts, sum(a*a for a in levels)


def block_type(B):
    if len(B) <= 2 or len(set(B[i+1]-B[i] for i in range(len(B)-1))) == 1:
        return "AP"
    if len(differences(B)) == len(B)*(len(B)-1)//2:
        return "Sidon"
    return "other"


def fft_stats(A):
    L = 2**16
    f = np.zeros(L)
    f[A] = 0.5
    f[[-a for a in A]] = 0.5
    vals = np.fft.fft(f).real
    j = int(np.argmin(vals))
    # Independent direct cosine check of the selected FFT sample.
    aa = np.array(A)
    direct = float(np.cos(2*np.pi*aa*j/L).sum())
    assert abs(direct-vals[j]) < 1e-9
    # Refine every sampled local minimum, rather than only the winning cell.
    minima = np.where((vals <= np.roll(vals, 1)) & (vals <= np.roll(vals, -1)))[0]
    best, theta = float(vals[j]), j/L
    for k in minima:
        opt = minimize_scalar(lambda t: float(np.cos(2*np.pi*aa*t).sum()),
                              bounds=((k-1)/L, (k+1)/L), method="bounded",
                              options={"xatol": 1e-15})
        if opt.fun < best:
            best, theta = float(opt.fun), float(opt.x % 1)
    return {"grid_size": L, "R_grid": -float(vals[j])/math.sqrt(len(A)),
            "M_grid": -float(vals[j]), "grid_index": j,
            "R_refined_uncertified": -best/math.sqrt(len(A)),
            "theta_refined": theta, "FFT_direct_error": abs(direct-vals[j])}


class Pricing:
    """Anchored clique pricing: only vertices 0 and A can occur.

    Products z_ij are exact McCormick products of binary x_i,x_j; forbidden
    differences give x_i+x_j<=1. For levels 1,2, each location has two
    mutually exclusive binary choices, and products are linearized likewise.
    """
    def __init__(self, A, two_level=False):
        self.A = set(A)
        self.two_level = two_level
        self.m = model("e111_pricing")
        self.m.Params.PoolSolutions = 16
        self.choices = [(b, a) for b in [0]+A for a in ([1, 2] if two_level else [1])]
        self.x = self.m.addVars(self.choices, vtype=GRB.BINARY)
        self.m.addConstr(gp.quicksum(self.x[0,a] for a in ([1,2] if two_level else [1])) == 1)
        if two_level:
            for b in A:
                self.m.addConstr(self.x[b,1]+self.x[b,2] <= 1)
        self.edges = []
        levels = [1,2] if two_level else [1]
        for i, b in enumerate([0]+A):
            for c in ([0]+A)[i+1:]:
                if c-b not in self.A:
                    self.m.addConstr(gp.quicksum(self.x[b,a] for a in levels) +
                                     gp.quicksum(self.x[c,a] for a in levels) <= 1)
                else:
                    for a in levels:
                        for d in levels:
                            z = self.m.addVar(lb=0, ub=1)
                            self.m.addConstr(z <= self.x[b,a])
                            self.m.addConstr(z <= self.x[c,d])
                            self.m.addConstr(z >= self.x[b,a]+self.x[c,d]-1)
                            self.edges.append((c-b, a*d, z))
        self.m.update()

    def solve(self, y, seconds):
        self.m.Params.TimeLimit = max(0.01, seconds)
        self.m.setObjective(gp.quicksum(y[k]*ad*z for k, ad, z in self.edges) -
                            gp.quicksum(a*a*self.x[b,a] for b,a in self.choices), GRB.MAXIMIZE)
        self.m.optimize()
        blocks = []
        for sol in range(self.m.SolCount):
            self.m.Params.SolutionNumber = sol
            chosen = sorted((b,a) for b,a in self.choices if self.x[b,a].Xn > 0.5)
            B, levels = tuple(b for b,a in chosen), tuple(a for b,a in chosen)
            counts, cost = column(B, levels)
            val = sum(y[k]*v for k,v in counts.items())-cost
            if val > TOL:
                blocks.append((B,levels))
        return {"blocks": blocks, "bound": float(self.m.ObjBound),
                "value": float(self.m.ObjVal) if self.m.SolCount else None,
                "status": int(self.m.Status), "runtime": self.m.Runtime,
                "nodes": self.m.NodeCount}

    def clique_bound(self, seconds):
        self.m.Params.TimeLimit=max(0.01,seconds)
        self.m.setObjective(gp.quicksum(self.x[b,a] for b,a in self.choices),GRB.MAXIMIZE)
        self.m.optimize()
        return {"upper":float(self.m.ObjBound),"incumbent":float(self.m.ObjVal) if self.m.SolCount else None,
                "status":int(self.m.Status),"runtime":self.m.Runtime}


def greedy_blocks(A, y, rng, starts=20):
    aset = set(A)
    found = set()
    for _ in range(starts):
        B, cand = [0], list(A)
        while cand:
            gains = [(sum(y[abs(c-b)] for b in B)-1, c) for c in cand]
            gains.sort(reverse=True)
            # Perturb starting choices; thereafter favour positive reduced cost.
            pick = rng.randrange(min(4, len(gains))) if len(B) == 1 else 0
            gain, c = gains[pick]
            if len(B) > 1 and gain <= 0:
                break
            B.append(c)
            cand = [d for d in cand if d != c and abs(d-c) in aset]
            if len(B) >= 2:
                BB = tuple(sorted(B))
                counts, cost = column(BB)
                if sum(y[k]*v for k,v in counts.items())-cost > TOL:
                    found.add(BB)
    return found


def enumerated_heuristic(A, limit=200000, seed=20261019):
    """Bounded anchored-clique enumeration for a stronger pricing heuristic.

    If truncated this is only a heuristic, never a source of a global bound.
    The matrix stores exact integer multiplicities; MILP pricing is retained.
    """
    vertices = list(A)
    random.Random(seed).shuffle(vertices)
    aset, index = set(A), {a:i for i,a in enumerate(A)}
    adjacent = []
    for b in vertices:
        adjacent.append(sum(1<<j for j,c in enumerate(vertices) if abs(c-b) in aset))
    blocks, counts = [], []
    truncated = False

    def visit(B, candidates):
        nonlocal truncated
        while candidates:
            if len(blocks)>=limit:
                truncated=True
                return
            bit=candidates & -candidates
            candidates-=bit
            i=bit.bit_length()-1
            BB=B+[vertices[i]]
            block=tuple(sorted(BB))
            cc,_=column(block)
            row=np.zeros(len(A),dtype=np.uint8)
            for k,v in cc.items():
                row[index[k]]=v
            blocks.append(block); counts.append(row)
            visit(BB,candidates & adjacent[i])
            if truncated:
                return
    visit([0],(1<<len(vertices))-1)
    return blocks,np.asarray(counts,dtype=np.float64),not truncated


def rational_certificate(A, active):
    """Round to rationals, scale any overcoverage down, fill with pair blocks.

    This always produces an EXACT feasible rational certificate, independently
    of LP residuals or successful rational reconstruction of the optimal basis.
    """
    weights = {}
    for B, levels, w in active:
        q = Fraction(float(w)).limit_denominator(10**9)
        if q > 0:
            weights[B, levels] = weights.get((B, levels), Fraction(0))+q
    cov = {a: Fraction(0) for a in A}
    for (B, levels), w in weights.items():
        cc, _ = column(B, levels)
        for k,v in cc.items():
            assert k in cov
            cov[k] += w*v
    scale = max([Fraction(1)]+list(cov.values()))
    weights = {key: w/scale for key,w in weights.items()}
    for a in A:
        residual = 1-cov[a]/scale
        assert residual >= 0
        if residual:
            key = ((0,a),(1,1))
            weights[key] = weights.get(key, Fraction(0))+residual
    checked = {a: Fraction(0) for a in A}
    cost = Fraction(0)
    blocks = []
    for (B,levels), w in sorted(weights.items()):
        cc, c = column(B, levels)
        assert min(B) == 0 and all(v > 0 for v in levels) and w > 0
        for k,v in cc.items():
            assert k in checked
            checked[k] += w*v
        cost += c*w
        blocks.append({"B": list(B), "levels": list(levels), "weight": str(w),
                       "weight_float": float(w), "type": block_type(B)})
    assert all(v == 1 for v in checked.values())
    return {"blocks": blocks, "C_exact": str(cost), "C_exact_float": float(cost),
            "exact_identity_checked": True, "rounding_scale": str(scale),
            "rational_round_denominator_limit": 10**9}


def solve_flat(A, *, seconds=120, price_seconds=10, max_iter=1000,
               seed=20261019, warm=(), two_level=False, certify=True,
               enumerate_heuristic=False):
    A = sorted(set(A))
    assert A and min(A)>0
    start = time.monotonic()
    rng = random.Random(seed)
    aset = set(A)
    lp = model("e111_master")
    lp.Params.Method = 1
    constraints = {a: lp.addConstr(gp.LinExpr() == 1) for a in A}
    variables, keys = [], set()

    def add(B, levels=None):
        B = normalized(B)
        levels = tuple(levels) if levels is not None else (1,)*len(B)
        key = B, levels
        if key in keys or len(B)<2 or not differences(B) <= aset:
            return
        cc, cost = column(B, levels)
        var = lp.addVar(obj=cost, column=gp.Column(list(cc.values()), [constraints[k] for k in cc]))
        variables.append((B, levels, var))
        keys.add(key)

    for a in A:
        add((0,a))
    for b in warm:
        if isinstance(b, dict):
            add(b["B"], b.get("levels"))
        else:
            add(b)
    for B in greedy_blocks(A, {a:2.0 for a in A}, rng, 40):
        add(B)
    enum_blocks, enum_counts, enum_complete = [],None,False
    if enumerate_heuristic and not two_level:
        enum_blocks,enum_counts,enum_complete=enumerated_heuristic(A,seed=seed)
        print("ENUM",len(A),max(A),len(enum_blocks),"complete",enum_complete,flush=True)
    enum_costs=np.array([len(B) for B in enum_blocks])
    pricing = Pricing(A, two_level=two_level)
    history, lower = [], 0.0
    clique_bound=None
    if enumerate_heuristic and not two_level:
        clique_bound=pricing.clique_bound(min(5,max(0.01,seconds-(time.monotonic()-start))))
        if math.isfinite(clique_bound["upper"]) and clique_bound["upper"]>1:
            lower=2*len(A)/(clique_bound["upper"]-1)
    stop = "iteration_limit"
    last_y = None
    for it in range(max_iter):
        lp.optimize()
        assert lp.Status == GRB.OPTIMAL
        if lower >= lp.ObjVal-TOL:
            stop="clique_dual_matched_to_tolerance"
            break
        y = {a: constraints[a].Pi for a in A}
        last_y = y
        elapsed = time.monotonic()-start
        if elapsed >= seconds:
            stop = "total_time_limit"
            break
        previous = len(keys)
        if not two_level:
            for B in greedy_blocks(A, y, rng, 12):
                add(B)
        if enum_blocks:
            scores=enum_counts @ np.array([y[a] for a in A])-enum_costs
            for j in np.argsort(scores)[-32:]:
                if scores[j]>TOL:
                    add(enum_blocks[j])
        # Greedy columns accelerate the master, but a global pricing call is
        # still needed for a flat-class lower bound and termination decision.
        if len(keys) > previous:
            history.append({"iteration":it, "C":lp.ObjVal, "heuristic_added":len(keys)-previous})
            continue
        priced = pricing.solve(y, min(price_seconds, max(0.01, seconds-elapsed)))
        U = priced["bound"]
        # For every nontrivial column c>=2 and y.m <= c+U. Rescaling y by
        # alpha=1+max(U,0)/2 therefore gives a full-class feasible dual,
        # conditional on the floating point MILP bound and its tolerances.
        alpha = 1+max(0.0,U)/2
        candidate_lb = sum(y.values())/alpha if math.isfinite(alpha) else 0.0
        lower = max(lower, candidate_lb)
        history.append({"iteration":it, "C":lp.ObjVal, "pricing":{k:v for k,v in priced.items() if k!="blocks"},
                        "scaled_dual_lower":candidate_lb, "duals":y})
        for B, levels in priced["blocks"]:
            add(B, levels)
        if U <= TOL:
            stop = "pricing_proved_no_improvement_to_tolerance"
            break
        if len(keys) == previous:
            # Retain the bound, then spend the remaining total case budget on
            # further MILP pricing instead of stopping after one short call.
            price_seconds=min(max(price_seconds*2,1),max(0.01,seconds-(time.monotonic()-start)))
            stop = "pricing_time_limit_no_new_column"
    lp.optimize()
    active = [(B,levels,v.X) for B,levels,v in variables if v.X > 1e-10]
    residual = max(abs(sum(column(B,levels)[0].get(a,0)*w for B,levels,w in active)-1) for a in A)
    cert = rational_certificate(A, active) if certify else {}
    C = cert.get("C_exact_float", lp.ObjVal)
    result = {"A":A, "n":len(A), "X":max(A), "C_lp":lp.ObjVal,
              "C_flat_UB" if not two_level else "C_two_level_UB":C,
              "R_CP_flat_UB" if not two_level else "R_CP_two_level_UB":C/(2*math.sqrt(len(A))),
              "flat_class_LP_lower" if not two_level else "two_level_class_LP_lower":lower,
              "numerical_gap":lp.ObjVal-lower, "stop":stop, "iterations":len(history),
              "columns":len(keys), "active_blocks":len(active),
              "block_sizes":dict(sorted(Counter(len(B) for B,_,_ in active).items())),
              "block_types":dict(Counter(block_type(B) for B,_,_ in active)),
              "blocks_numerical":[{"B":list(B),"levels":list(levels),"weight":w,"type":block_type(B)} for B,levels,w in active],
              "max_primal_residual":residual, "seconds":time.monotonic()-start,
              "seed":seed, "history":history, "certificate":cert,
              "enumeration_heuristic":{"enabled":enumerate_heuristic,"blocks":len(enum_blocks),"complete":enum_complete},
              "clique_bound":clique_bound,
              "last_master_duals":last_y}
    pricing.m.dispose()
    lp.dispose()
    return result


def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True)+"\n")


def suite_cases():
    cases = []
    for filename in ["examples/construct/N50_certified.json", "examples/dense_certified.json"]:
        for name,row in json.loads(Path(filename).read_text()).items():
            if max(row["A"]) <= 120:
                cases.append((name, row["A"], {"source":filename}))
    from singer import singer, is_perfect_difference_set
    for q in [5,7,11]:
        B,v = singer(q)
        assert is_perfect_difference_set(B,v)
        A = sorted(differences(B))
        assert len(A) == len(B)*(len(B)-1)//2
        cases.append((f"Singer_q{q}",A,{"B":B,"cyclic_modulus":v,"warm":[B]}))
    for X in [20,40]:
        cases.append((f"interval_{X}",list(range(1,X+1)),{}))
    rng = random.Random(20261019)
    A = [a for a in range(1,61) if rng.random()<0.5]
    cases.append(("random60_half",A,{"generator":"random.Random(20261019), independent Bernoulli(1/2)"}))
    unions = [([0,1,4,10],[0,2,7,15]),
              ([0,1,4,10,18],[0,2,7,15,24]),
              ([0,1,4,10],[0,1,4,9,11]),
              ([0,1,4,10,18],[0,1,4,10,12])]
    for i,(B1,B2) in enumerate(unions):
        assert len(differences(B1))==len(B1)*(len(B1)-1)//2
        assert len(differences(B2))==len(B2)*(len(B2)-1)//2
        cases.append((f"Sidon_union_{i+1}",sorted(differences(B1)|differences(B2)),
                      {"B1":B1,"B2":B2,"warm":[B1,B2]}))
    return cases


def metadata(args):
    return {"command":sys.argv,"host":socket.gethostname(),"python":platform.python_version(),
            "numpy":np.__version__,"gurobi":gp.gurobi.version(),"unix_time":time.time(),
            "tolerances":{"FeasibilityTol":1e-9,"OptimalityTol":1e-9,"IntFeasTol":1e-9,
                          "MIPGap":0,"MIPGapAbs":1e-9,"column_reduced_cost":TOL},
            "args":vars(args), "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def run_suite(args):
    path = OUT/"suite.jsonl"
    done = {row["name"] for row in map(json.loads,path.read_text().splitlines())} if path.exists() and args.resume else set()
    with path.open("a" if args.resume else "w") as fh:
        for name,A,info in suite_cases():
            if name in done or (args.only and name not in args.only):
                continue
            print("START",name,"n",len(A),"X",max(A),flush=True)
            row = solve_flat(A,seconds=args.seconds,price_seconds=args.price_seconds,warm=info.get("warm",()))
            row.update(name=name, input_info=info, **fft_stats(A))
            write_json(OUT/f"{name}_certificate.json", row)
            fh.write(json.dumps({k:v for k,v in row.items() if k not in ["history","certificate","blocks_numerical","last_master_duals"]})+"\n")
            fh.flush()
            print("DONE",name,"C",row["C_flat_UB"],"LB",row["flat_class_LP_lower"],
                  "RCP",row["R_CP_flat_UB"],"stop",row["stop"],"secs",row["seconds"],flush=True)


def initial_search_set(X, rng, restart):
    if restart%3 == 0:
        # Greedy Golomb ruler up to X supplies a structural starting point.
        B = [0]
        for b in range(1,X+1):
            new = [b-a for a in B]
            if len(set(new)|differences(B)) == len(new)+len(differences(B)):
                B.append(b)
        A = differences(B)
    elif restart%3 == 1:
        A = {a for a in range(1,X+1) if rng.random()<0.65}
    else:
        A = set(range(1,X+1))
    A.add(X)
    while len(A)<10:
        A.add(rng.randrange(1,X+1))
    return sorted(A)


def run_search(args):
    summaries = []
    trace = (OUT/"search_trace.jsonl").open("w")
    for X in args.X:
        seed = 20261019+1009*X
        rng = random.Random(seed)
        start = time.monotonic()
        best, evaluated, accepted = None, 0, 0
        move_counts = Counter()
        cache = {}
        for restart in range(args.restarts):
            A = initial_search_set(X,rng,restart)
            current = None
            for move in range(args.moves+1):
                if time.monotonic()-start > args.search_seconds and best is not None:
                    break
                if current is None:
                    proposed, kind = A,"start"
                else:
                    S = set(A)
                    kind = rng.choice(["add","remove","swap"])
                    missing, removable = sorted(set(range(1,X+1))-S),sorted(S-{X})
                    if kind == "add" and missing:
                        S.add(rng.choice(missing))
                    elif kind == "remove" and len(S)>10 and removable:
                        S.remove(rng.choice(removable))
                    elif kind == "swap" and missing and removable:
                        S.remove(rng.choice(removable)); S.add(rng.choice(missing))
                    else:
                        continue
                    proposed = sorted(S)
                key = tuple(proposed)
                if key in cache:
                    candidate = cache[key]
                else:
                    warm = current["blocks_numerical"] if current else ()
                    candidate = solve_flat(proposed, seconds=args.eval_seconds,price_seconds=args.eval_price_seconds,
                                           warm=warm,seed=seed+evaluated,certify=False)
                    cache[key] = candidate
                    evaluated += 1
                value = candidate["R_CP_flat_UB"]
                temperature = 0.025*(1-move/max(1,args.moves))+0.001
                take = current is None or value <= current["R_CP_flat_UB"] or rng.random()<math.exp(
                    min(0,(current["R_CP_flat_UB"]-value)/temperature))
                move_counts[kind] += 1
                if take:
                    A,current = proposed,candidate
                    accepted += 1
                improved = best is None or value < best["R_CP_flat_UB"]-1e-10
                if improved:
                    best = candidate
                    print("SEARCH",X,"best",value,"n",len(proposed),"evaluated",evaluated,flush=True)
                trace.write(json.dumps({"X":X,"seed":seed,"restart":restart,"move":move,"kind":kind,
                                        "A":proposed,"R_CP_flat_UB":value,"accepted":take,"improved":improved,
                                        "C":candidate["C_lp"],"lower":candidate["flat_class_LP_lower"],
                                        "stop":candidate["stop"],"elapsed":time.monotonic()-start})+"\n")
                trace.flush()
            if time.monotonic()-start > args.search_seconds:
                break
        # Re-solve the best candidate at full accuracy, with exact rational repair.
        final = solve_flat(best["A"],seconds=args.seconds,price_seconds=args.price_seconds,
                           warm=best["blocks_numerical"],seed=seed)
        final.update(name=f"search_X{X}", **fft_stats(best["A"]),
                     search={"seed":seed,"evaluated_distinct":evaluated,"accepted":accepted,
                             "moves":dict(move_counts),"restarts_started":restart+1,
                             "moves_per_restart_limit":args.moves,"elapsed_seconds":time.monotonic()-start,
                             "search_time_limit":args.search_seconds,
                             "evaluation_seconds_limit":args.eval_seconds,
                             "evaluation_pricing_seconds_limit":args.eval_price_seconds,
                             "objective":"numerical C_flat upper bound / (2 sqrt(n)); full re-solve for winner",
                             "max_A_fixed_at_X":True})
        write_json(OUT/f"search_X{X}_certificate.json",final)
        summaries.append({k:v for k,v in final.items() if k not in ["history","certificate","blocks_numerical","last_master_duals"]})
        write_json(OUT/"search_summary.json",summaries)
        print("SEARCH_DONE",X,"RCP",final["R_CP_flat_UB"],"LB",final["flat_class_LP_lower"],flush=True)
    trace.close()


def run_levels(args):
    for name in args.only:
        source = json.loads((OUT/f"{name}_certificate.json").read_text())
        row = solve_flat(source["A"],seconds=args.seconds,price_seconds=args.price_seconds,
                         warm=source["blocks_numerical"],two_level=True)
        row.update(name=name,**fft_stats(source["A"]))
        write_json(OUT/f"{name}_two_level.json",row)
        print("TWO_LEVEL",name,"C",row["C_two_level_UB"],"LB",row["two_level_class_LP_lower"],
              "R",row["R_CP_two_level_UB"],"stop",row["stop"],flush=True)


def run_refine(args):
    rows=[json.loads(line) for line in (OUT/"suite.jsonl").read_text().splitlines()]
    for i,summary in enumerate(rows):
        name=summary["name"]
        if (args.only and name not in args.only) or (not args.only and summary["stop"]=="pricing_proved_no_improvement_to_tolerance"):
            continue
        original=json.loads((OUT/f"{name}_certificate.json").read_text())
        if not (OUT/f"{name}_initial.json").exists():
            write_json(OUT/f"{name}_initial.json",original)
        print("REFINE_START",name,flush=True)
        row=solve_flat(original["A"],seconds=args.seconds,price_seconds=args.price_seconds,
                       warm=original["blocks_numerical"],enumerate_heuristic=True)
        row.update(name=name,input_info=original["input_info"],**fft_stats(original["A"]))
        row["refinement"]={"case_seconds_limit":args.seconds,"pricing_seconds_limit_initial":args.price_seconds,
                           "initial_C":original["C_flat_UB"],"initial_lower":original["flat_class_LP_lower"],
                           "initial_seconds":original["seconds"],"initial_file":f"{name}_initial.json"}
        write_json(OUT/f"{name}_certificate.json",row)
        rows[i]={k:v for k,v in row.items() if k not in ["history","certificate","blocks_numerical","last_master_duals"]}
        (OUT/"suite.jsonl").write_text("".join(json.dumps(r)+"\n" for r in rows))
        print("REFINE_DONE",name,"C",row["C_flat_UB"],"LB",row["flat_class_LP_lower"],"RCP",row["R_CP_flat_UB"],"stop",row["stop"],flush=True)


def endpoint_sidon(X, rng, return_block=False):
    """Verified Sidon starts whose diameter is the requested X."""
    templates=[[0,1,4,9,11],[0,1,4,10,12,17],
               [0,1,4,10,18,23,25],[0,1,4,9,15,22,32,34]]
    best=[0,X]
    for template in templates:
        B=template[:-1]+[X]
        if B==sorted(set(B)) and len(differences(B))==len(B)*(len(B)-1)//2 and len(B)>len(best):
            best=B
    for _ in range(500):
        B,D=[0,X],{X}
        candidates=list(range(1,X)); rng.shuffle(candidates)
        for b in candidates:
            new=[abs(b-c) for c in B]
            if len(set(new))==len(new) and not (set(new)&D):
                B.append(b); D.update(new)
        if len(B)>len(best):
            best=sorted(B)
    assert len(differences(best))==len(best)*(len(best)-1)//2
    A=sorted(differences(best))
    return (A,best) if return_block else A


def run_polish(args):
    rows=json.loads((OUT/"search_summary.json").read_text())
    if not (OUT/"search_initial_summary.json").exists():
        write_json(OUT/"search_initial_summary.json",rows)
    trace=(OUT/"search_trace.jsonl").open("a")
    for i,summary in enumerate(rows):
        X=summary["X"]
        if X not in args.X:
            continue
        seed=20261019+1009*X+4096
        rng=random.Random(seed); start=time.monotonic()
        original=json.loads((OUT/f"search_X{X}_certificate.json").read_text())
        best=original; current=None; evaluated=accepted=0; counts=Counter(); cache={tuple(best["A"]):best}
        sidon_A,sidon_B=endpoint_sidon(X,rng,return_block=True)
        starts=[sidon_A,best["A"]]
        if len(starts[0])<10:
            starts[0]=best["A"]
        for restart,A in enumerate(starts):
            current=None
            for move in range(args.moves+1):
                if time.monotonic()-start>=args.search_seconds:
                    break
                proposed=list(A); kind="start"
                if current is not None:
                    S=set(A); missing=sorted(set(range(1,X+1))-S); removable=sorted(S-{X})
                    kind=rng.choice(["add","remove","swap"])
                    if kind=="add" and missing:
                        S.add(rng.choice(missing))
                    elif kind=="remove" and len(S)>10 and removable:
                        S.remove(rng.choice(removable))
                    elif kind=="swap" and missing and removable:
                        S.remove(rng.choice(removable)); S.add(rng.choice(missing))
                    else:
                        continue
                    proposed=sorted(S)
                key=tuple(proposed)
                if key not in cache:
                    warm=list(current["blocks_numerical"]) if current else []
                    warm.append(sidon_B)
                    cache[key]=solve_flat(proposed,seconds=args.eval_seconds,price_seconds=args.eval_price_seconds,
                                          warm=warm,seed=seed+evaluated,certify=False)
                    evaluated+=1
                candidate=cache[key]; value=candidate["R_CP_flat_UB"]
                temperature=0.015*(1-move/max(1,args.moves))+0.0005
                take=current is None or value<=current["R_CP_flat_UB"] or rng.random()<math.exp(
                    min(0,(current["R_CP_flat_UB"]-value)/temperature))
                counts[kind]+=1
                if take:
                    A,current=proposed,candidate; accepted+=1
                improved=value<best["R_CP_flat_UB"]-1e-10
                if improved:
                    best=candidate
                    print("POLISH",X,"RCP",value,"n",len(proposed),flush=True)
                trace.write(json.dumps({"stage":"polish","X":X,"seed":seed,"restart":restart,"move":move,
                                        "kind":kind,"A":proposed,"R_CP_flat_UB":value,"accepted":take,
                                        "improved":improved,"elapsed":time.monotonic()-start})+"\n"); trace.flush()
            if time.monotonic()-start>=args.search_seconds:
                break
        if best is original:
            final=original
        else:
            final=solve_flat(best["A"],seconds=args.seconds,price_seconds=args.price_seconds,warm=best["blocks_numerical"],seed=seed)
            final.update(name=f"search_X{X}",**fft_stats(best["A"]))
        s=dict(original["search"])
        s["moves"]=dict(Counter(s["moves"])+counts)
        s["evaluated_distinct"]+=evaluated; s["accepted"]+=accepted
        s["restarts_started"]+=restart+1
        s["elapsed_seconds"]+=time.monotonic()-start
        s["polish"]={"seed":seed,"time_limit":args.search_seconds,"moves_per_restart_limit":args.moves,
                       "distinct_evaluations":evaluated,"elapsed_seconds":time.monotonic()-start,
                       "endpoint_sidon_start":starts[0],"sidon_block":sidon_B,
                       "temperature":"0.015*(1-move/moves)+0.0005"}
        final["search"]=s
        write_json(OUT/f"search_X{X}_certificate.json",final)
        rows[i]={k:v for k,v in final.items() if k not in ["history","certificate","blocks_numerical","last_master_duals"]}
        write_json(OUT/"search_summary.json",rows)
        print("POLISH_DONE",X,"RCP",final["R_CP_flat_UB"],flush=True)
    trace.close()


def run_warm_controls(args):
    """Ensure every generated Sidon start uses its known one-block column."""
    rows=json.loads((OUT/"search_summary.json").read_text())
    trace=(OUT/"search_trace.jsonl").open("a")
    for i,summary in enumerate(rows):
        if "polish" not in summary["search"]:
            continue
        X=summary["X"]; p=summary["search"]["polish"]
        A,B=endpoint_sidon(X,random.Random(p["seed"]),return_block=True)
        original=json.loads((OUT/f"search_X{X}_certificate.json").read_text())
        assert A==p["endpoint_sidon_start"] or len(A)<10
        original["search"]["polish"]["sidon_block"]=B
        known_ratio=len(B)/(2*math.sqrt(len(A)))
        final=original
        if len(A)>=10 and known_ratio<original["R_CP_flat_UB"]-1e-9:
            start=time.monotonic()
            final=solve_flat(A,seconds=args.seconds,price_seconds=args.price_seconds,warm=[B],
                             seed=p["seed"],enumerate_heuristic=True)
            final.update(name=f"search_X{X}",**fft_stats(A))
            final["search"]=original["search"]
            final["search"]["evaluated_distinct"]+=1
            final["search"]["accepted"]+=1
            final["search"]["moves"]["start"]+=1
            final["search"]["elapsed_seconds"]+=time.monotonic()-start
            final["search"]["sidon_warm_control"]={"B":B,"seed":p["seed"],"seconds":time.monotonic()-start,
                                                       "case_limit":args.seconds,"pricing_limit":args.price_seconds}
            trace.write(json.dumps({"stage":"sidon_warm_control","X":X,"seed":p["seed"],"restart":0,"move":0,
                                    "kind":"start","A":A,"R_CP_flat_UB":final["R_CP_flat_UB"],"accepted":True,
                                    "improved":True,"elapsed":time.monotonic()-start})+"\n"); trace.flush()
            print("SIDON_WARM_CONTROL",X,"C",final["C_flat_UB"],"RCP",final["R_CP_flat_UB"],flush=True)
        write_json(OUT/f"search_X{X}_certificate.json",final)
        rows[i]={k:v for k,v in final.items() if k not in ["history","certificate","blocks_numerical","last_master_duals"]}
    trace.close()
    write_json(OUT/"search_summary.json",rows)


def audit_threshold(args):
    """Re-solve and save EVERY distinct search candidate below 0.68."""
    seen, records, proposals, all_sets, minimum = set(), [], 0, set(), math.inf
    path = OUT/"search_trace.jsonl"
    for raw in path.read_text().splitlines():
        trial = json.loads(raw)
        key = tuple(trial["A"])
        proposals+=1; all_sets.add(key); minimum=min(minimum,trial["R_CP_flat_UB"])
        if trial["R_CP_flat_UB"] >= 0.68 or key in seen:
            continue
        seen.add(key)
        row = solve_flat(list(key),seconds=args.seconds,price_seconds=args.price_seconds)
        row.update(name=f"sub068_{len(seen)}", **fft_stats(list(key)))
        write_json(OUT/f"sub068_{len(seen)}_certificate.json",row)
        records.append({"A":list(key),"reported_search_R":trial["R_CP_flat_UB"],
                        "R_CP_flat_UB":row["R_CP_flat_UB"],"file":f"sub068_{len(seen)}_certificate.json"})
    write_json(OUT/"sub068_audit.json",{"threshold":0.68,"proposals_scanned":proposals,
               "distinct_sets_scanned":len(all_sets),"minimum_recorded_flat_ratio":minimum,
               "distinct_search_candidates":records})
    print("SUB068_AUDIT",len(records),flush=True)


def verify_saved():
    checked = []
    for path in sorted(OUT.glob("*_certificate.json"))+sorted(OUT.glob("*_two_level.json"))+sorted(OUT.glob("*_initial.json")):
        row = json.loads(path.read_text())
        expected, actual = set(row["A"]),Counter()
        assert len(expected)==row["n"] and max(expected)==row["X"]
        C = Fraction(0)
        for block in row["certificate"]["blocks"]:
            B, levels, w = block["B"],block["levels"],Fraction(block["weight"])
            assert B == sorted(set(B)) and min(B)==0 and w>0
            assert len(levels)==len(B) and all(isinstance(a,int) and a in [1,2] for a in levels)
            for i,b in enumerate(B):
                C += w*levels[i]**2
                for j in range(i+1,len(B)):
                    actual[B[j]-b] += w*levels[i]*levels[j]
        assert set(actual)==expected and all(actual[k]==1 for k in expected)
        assert C==Fraction(row["certificate"]["C_exact"])
        checked.append({"file":str(path),"n":len(expected),"C_exact":str(C),"blocks":len(row["certificate"]["blocks"]),
                        "all_coefficients_exact":True,
                        "ratio_strictly_below_068_exact":C*C < 4*len(expected)*Fraction(17,25)**2})
    write_json(OUT/"verification.json",{"checked":checked,"count":len(checked),"host":socket.gethostname()})
    print("EXACT_VERIFIED",len(checked),flush=True)


def run_report(args):
    suite = [json.loads(line) for line in (OUT/"suite.jsonl").read_text().splitlines()]
    search = json.loads((OUT/"search_summary.json").read_text())
    audit = json.loads((OUT/"sub068_audit.json").read_text())
    verification = json.loads((OUT/"verification.json").read_text())
    environment = json.loads((OUT/"metadata_suite.json").read_text())
    full = [json.loads((OUT/f"{r['name']}_certificate.json").read_text()) for r in suite+search]
    levels=[json.loads(path.read_text()) for path in sorted(OUT.glob("*_two_level.json"))]
    best = min(full, key=lambda r:r["R_CP_flat_UB"])
    closed = lambda r:r["stop"] in ["pricing_proved_no_improvement_to_tolerance","clique_dual_matched_to_tolerance"]
    block_sizes = lambda r:", ".join(f"{k}:{v}" for k,v in sorted(r["block_sizes"].items(),key=lambda kv:int(kv[0])))
    lines = ["# E111: completely-positive flat-block certificate costs", "",
             "Generated "+time.strftime("%Y-%m-%d %H:%M:%S UTC",time.gmtime())+".", "",
             "Side computation for the lead; no core theorem is claimed. All optimization, FFTs, search, and rational verification ran on `dirichlet` through `src/dirun.sh`. No commit was made.", "",
             f"Completed **{len(suite)} prescribed benchmark cases** and local searches at **every integer X=10,...,40**. "
             f"The smallest flat upper-bound ratio among these saved cases is **{best['R_CP_flat_UB']:.10f}**, "
             f"for `{best['name']}` (n={best['n']}, X={best['X']}). "
             f"Pricing closed to the specified tolerances for {sum(closed(r) for r in suite)}/{len(suite)} benchmarks "
             f"and {sum(closed(r) for r in search)}/{len(search)} search winners. "
             "These are finite numerical flat-class optimization results; they establish no asymptotic CP lower bound.", "",
             "## Benchmark table", "",
             "Convention: `f_A(theta)=sum_{a in A} cos(2*pi*a*theta)`, `n=|A|`, `X=max(A)`. "
             "`R_grid = -min_grid f_A / sqrt(n)` uses exactly 2^16 points and is uncertified. "
             "`R_CP` denotes the flat certificate upper bound `C_flat/(2 sqrt(n))`, not the unknown optimum over every nonnegative sequence. "
             "The LP lower-bound column concerns only the flat class and is numerical. Decimal values are rounded for display; exact primal weights and exact rational costs are in the linked JSON files. "
             "Block entries are `size:number` for positive master-LP blocks before tiny rational repairs.", "",
             "| Set | n | X | R (grid) | R_CP (flat UB) | C_flat (UB) | Flat-class LP lower bound | Blocks used (size:number) | Pricing |",
             "|---|---:|---:|---:|---:|---:|---:|---|---|"]
    if levels:
        best_level=min(levels,key=lambda r:r["R_CP_two_level_UB"])
        position=lines.index("## Benchmark table")
        lines[position:position]=[
            f"**Optional non-flat finding:** `{best_level['name']}` has an exact rational two-level certificate with "
            f"C={best_level['C_two_level_UB']:.12f}, hence R_CP<={best_level['R_CP_two_level_UB']:.12f} "
            f"(n={best_level['n']}, X={best_level['X']}). Its grid R is {best_level['R_grid']:.9f}. "
            "The exact support, levels, weights and coefficient check are saved; the explicit set and strict rational threshold check appear below. "
            "This is a finite non-flat result, not a counterexample to the flat asymptotic target.", ""]
    for r in suite:
        lines.append(f"| [{r['name']}](../../examples/e111/{r['name']}_certificate.json) | {r['n']} | {r['X']} | {r['R_grid']:.8f} | {r['R_CP_flat_UB']:.8f} | {r['C_flat_UB']:.8f} | {r['flat_class_LP_lower']:.8f} | {block_sizes(r)} | {'closed' if closed(r) else r['stop']} |")
    lines += ["", "The `N50_x71` input label has actual max(A)=68; the table uses the set itself. "
              "The qualifying dense rows are selected by actual max(A)<=120. Singer A is the set of positive **integer** differences of the representatives returned by `src/singer.py`, rather than all nonzero cyclic residues. "
              "The random row uses Python `random.Random(20261019)` and includes each a=1,...,60 independently when `random()<1/2`; its explicit A is saved in its certificate JSON. "
              "Each Sidon-union input records both B1 and B2 in `input_info`; both were checked to have no repeated positive integer differences.", "",
              "## Numerical optimization and exact checks", "",
              "The restricted master starts with every pair {0,a}, plus greedy cliques and supplied generating blocks. "
              "Greedy pricing adds improving columns before MILP pricing. The MILP uses vertices {0} union A, fixes 0 in the clique, "
              "forbids x_b+x_c>1 when c-b is absent from A, and linearizes each allowed binary product with all three McCormick inequalities. "
              "Its objective is sum_{b<c} y_{c-b} x_b x_c - sum_b x_b. Singleton blocks cannot improve the master. "
              "Translation normalization loses no admissible block, since a clique of minimum 0 has all its other vertices in A.", "",
              "For a master dual y and a global MILP pricing upper bound U, the saved lower bound is "
              "sum(y)/(1+max(U,0)/2), maximized over pricing calls (and 0). "
              "Every nontrivial flat column has cost at least 2, so rescaling by this factor satisfies every flat dual inequality, "
              "conditional on the floating-point LP/MILP bounds. The master itself supplies C_lp. "
              "`closed` means a global pricing bound U<=1e-8; it is not an exact-rational proof of dual optimality. "
              "For time-limited cases the table deliberately retains the feasible certificate and the available scaled-dual lower bound, and reports the remaining gap.", "",
              f"Environment: host `{environment['host']}`, Python {environment['python']}, NumPy {environment['numpy']}, "
              f"Gurobi {'.'.join(map(str,environment['gurobi']))}. "
              "Gurobi settings: FeasibilityTol=OptimalityTol=IntFeasTol=1e-9; MIPGap=0; MIPGapAbs=1e-9; "
              "positive reduced-cost threshold 1e-8; master dual simplex; at most two solver threads per job. "
              "Benchmark case budget 120 seconds, each MILP pricing call at most 8 seconds. "
              "Final search-winner budget 60 seconds, each MILP call at most 6 seconds. "
              "All timing includes model construction, master iterations, and pricing; a final master solve and rational repair can slightly exceed a case budget. "
              "Full pricing incumbent values, global bounds, solver statuses, nodes, duals, and runtimes are in each JSON `history`. "
              "Status 2 is Gurobi OPTIMAL; status 9 is TIME_LIMIT. A time-limited pricing call can still produce a valid numerical global upper bound.", "",
              "Every flat case here with X<=30 closed its pricing gap to solver tolerances; all 31 final adversarial winners at X<=40 "
              "also closed. Larger benchmark cases used bounded MILP pricing plus the stated heuristics; the table identifies any unclosed cases. "
              "A globally solved Gurobi MILP is still floating-point optimization, distinct from the exact rational primal checks.", "",
              "Some nonclosed benchmark cases were then refined from their saved master blocks, with a 120-second total budget and "
              "an initial 10-second MILP call limit, increasing on stalled calls within the total budget. "
              "Refinement also enumerates at most 200,000 anchored cliques in a seeded order and uses their exact multiplicity vectors "
              "to propose up to 32 improving columns per iteration. Truncated enumeration is only a heuristic; "
              "all reported full-class bounds still come from global Gurobi pricing bounds. "
              "`enumeration_heuristic` records the count and whether enumeration completed; `refinement` records limits and initial results. "
              "Initial runs are retained in `*_initial.json`.", "",
              "Refinement also solves an anchored maximum-clique MILP for at most 5 seconds. "
              "A global upper bound W on clique size gives the constant flat dual y_a=2/(W-1), with value 2*n/(W-1). "
              "This is included when stronger than the quadratic-pricing dual bound. If it matches the feasible master value to 1e-8, "
              "the stop reason is `clique_dual_matched_to_tolerance`, also counted as closed. The value and status of the clique solve "
              "are saved in `clique_bound`; its bounds and matching statement remain numerical.", "",
              "For every saved certificate, positive numerical weights are rounded with Fraction.limit_denominator(10^9). "
              "If any frequency is overcovered, all rounded weights are divided by the largest rational coverage (or 1). "
              "Each residual is then filled by a rationally weighted pair {0,a}. This gives an actual exact feasible certificate, "
              "even when simple rounding of the LP basis would fail. The cost in C_flat_UB includes these repairs. "
              "A separate verifier rereads saved JSON and directly accumulates all pair products and diagonal costs using Python Fraction; "
              "it checks every positive coefficient is exactly 1 on A, all other positive coefficients vanish, all weights are positive, "
              "and the exact diagonal cost matches C_exact. Negative coefficients follow by symmetry. "
              f"The independent pass checked **{verification['count']} files**; see [verification.json](../../examples/e111/verification.json). "
              "Thus primal feasibility is exact; displayed optimality and dual lower bounds remain numerical.", "",
              "FFT values are independently checked by direct cosine summation at the winning grid point (error recorded). "
              "For the search winners, every sampled local minimum is also refined by bounded scalar minimization. "
              "The resulting `R_refined_uncertified` is an estimate of the actual R=M/sqrt(n), not a certified global minimum. "
              "Neither a grid result nor the scalar refinement is called a true or rigorous minimum here.", "",
              "## Adversarial search: best set per X", "",
              "The search fixes max(A)=X and |A|>=10, with X=10,...,40. At each X it attempts up to three restarts, "
              "80 add/remove/swap proposals per restart, with a 20-second search budget. Starting families alternate between "
              "greedy Sidon differences (filled to n>=10 and including X), a density-0.65 Bernoulli set, and an interval. "
              "Annealing accepts improvements and accepts uphill moves with exp(-delta/T), T=0.025*(1-move/80)+0.001. "
              "Repeated sets use a cache. Each new trial has a 1-second column-generation budget with 0.25-second MILP calls; "
              "the objective during search is therefore a feasible restricted-master upper bound, and is not guaranteed to be the flat optimum. "
              "Each winner is subsequently re-solved at the longer limits above and rationally verified. "
              "The move trace records every evaluated proposal, including cached proposals and acceptance decisions. "
              "This is a bounded heuristic falsification attempt, not enumeration of all A or proof of local/global optimality in A.", "",
              "An additional 10-second pass at each X=15,...,40 uses a verified Sidon difference set of diameter exactly X "
              "and the previous winner as starts (up to 60 moves per start). The Sidon start is selected from verified templates "
              "and 500 seeded greedy extensions of {0,X}; it is not claimed to be a largest Sidon set. "
              "This pass uses seed 20261019+1009*X+4096 and temperature 0.015*(1-move/60)+0.0005. "
              "The original summaries are retained in `search_initial_summary.json`, new trace entries have stage=polish, "
              "and each winner's `search.polish` records the added budget, seed, start, and runtime. "
              "The timing and move totals below sum both passes; expensive evaluations are counted within each pass, so the same set "
              "can be counted once in each pass.", "",
              "After the short pass, a Sidon control check reconstructs the generating block from the saved seed and inserts its "
              "known one-block column whenever its cost improves the current numerical incumbent. Such a check uses a 30-second "
              "case budget and a 5-second initial pricing limit, is recorded as `sidon_warm_control` in the trace, and contributes "
              "one start/evaluation to the totals. This corrects a short pricing run that can fail to rediscover its own generating block. "
              "The final source supplies that block as a warm start during polishing as well. All generating blocks are saved in `search.polish.sidon_block`.", "",
              "| X | n | R (grid) | R (refined, uncertified) | R_CP (flat UB) | Flat LP lower bound | Explicit best A |",
              "|---:|---:|---:|---:|---:|---:|---|"]
    for r in search:
        lines.append(f"| {r['X']} | {r['n']} | {r['R_grid']:.8f} | {r['R_refined_uncertified']:.8f} | {r['R_CP_flat_UB']:.8f} | {r['flat_class_LP_lower']:.8f} | {r['A']} |")
    lines += ["", "The seeds are deterministic: `20261019+1009*X`. The next table counts attempted moves that reached objective evaluation "
              "(including cache hits), distinct expensive evaluations, and accepted states (including restart starts). "
              "Runtime includes the final longer solve and FFT comparison. Per-trial timing and completed restart counts are also saved.", "",
              "| X | Seed | Starts/add/remove/swap | Distinct evaluations | Accepted | Restarts started | Runtime (s) | Final pricing |",
              "|---:|---:|---|---:|---:|---:|---:|---|"]
    for r in search:
        s=r["search"]; m=s["moves"]
        counts="/".join(str(m.get(k,0)) for k in ["start","add","remove","swap"])
        lines.append(f"| {r['X']} | {s['seed']} | {counts} | {s['evaluated_distinct']} | {s['accepted']} | {s['restarts_started']} | {s['elapsed_seconds']:.3f} | {'closed' if closed(r) else r['stop']} |")
    lines += ["", "## Search certificate block structure", "",
              "Each entry below is `size/type: weight, weight, ...`, giving every positive numerical master block weight "
              "(10 significant figures). AP means equally spaced support (including pairs), Sidon means all positive differences are distinct, "
              "and other means neither. AP takes precedence for classification. The linked JSON gives **all supports and exact rational weights**, "
              "including any tiny pair repairs; its `blocks_numerical` field records the unrounded master solution. "
              "When final pricing is closed, this is a numerically optimal flat certificate; otherwise it is a feasible certificate only.", "",
              "| X | Master blocks | Size/type and weights | Complete certificate |",
              "|---:|---:|---|---|"]
    for r in full[len(suite):]:
        groups={}
        for b in r["blocks_numerical"]:
            groups.setdefault((len(b["B"]),b["type"]),[]).append(b["weight"])
        description="; ".join(f"{size}/{kind}: "+", ".join(f"{w:.10g}" for w in sorted(weights))
                               for (size,kind),weights in sorted(groups.items()))
        lines.append(f"| {r['X']} | {r['active_blocks']} | {description} | [{r['name']}](../../examples/e111/{r['name']}_certificate.json) |")
    lines += ["", "## Threshold audit and scope", ""]
    sub=[r for r in full if r["R_CP_flat_UB"]<0.68]
    if not sub and not audit["distinct_search_candidates"]:
        lines.append("**No benchmark, saved search winner, or recorded search proposal had R_CP<0.68.** "
                     "Here R_CP refers to the flat upper bound. "
                     f"The full trace audit scanned {audit['proposals_scanned']} proposals and {audit['distinct_sets_scanned']} distinct sets; "
                     "[sub068_audit.json](../../examples/e111/sub068_audit.json) records the empty flat result. "
                     "This finite failure to falsify the flat target does not prove it.")
    else:
        for r in sub:
            lines.append(f"- `{r['name']}`: A={r['A']}, R_CP={r['R_CP_flat_UB']:.12g}; exact identity verified in its linked certificate.")
        for r in audit["distinct_search_candidates"]:
            lines.append(f"- Search proposal A={r['A']}, re-solved R_CP={r['R_CP_flat_UB']:.12g}; exact certificate `{r['file']}`.")
    low_levels=[r for r in levels if r["R_CP_two_level_UB"]<0.68]
    if low_levels:
        lines += ["", "The optional **non-flat two-level** class does produce the following sub-0.68 certificates. "
                  "These do not falsify the flat-class target. Every set is explicit, and the linked JSON contains supports, "
                  "levels and exact rational weights. The independent verifier also checks the strict threshold in rational arithmetic "
                  "as C^2 < 4*n*(17/25)^2:", ""]
        for r in low_levels:
            cost=r["certificate"]["C_exact"]
            lines.append(f"- **{r['name']}**: A={r['A']}; n={r['n']}; X={r['X']}; R_CP(two-level UB)={r['R_CP_two_level_UB']:.12f}; "
                         f"exact C={cost}; [exact certificate](../../examples/e111/{r['name']}_two_level.json). "
                         "All coefficients and nonnegativity checked in exact rational arithmetic after rounding and repair.")
    if levels:
        lines += ["", "## Optional two-level blocks", "",
                  "Values are in {0,1,2} times sqrt(w). Pricing includes mutually exclusive level choices at each location "
                  "and binary-product linearization; the nonzero value at location 0 may be 1 or 2. Flat columns are warm starts. "
                  "The same solver tolerances, rescaled-dual bound, and exact rational verification apply. "
                  "Each case had a 45-second total limit and an initial 5-second pricing limit; stalled pricing limits increase within the total budget.", "",
                  "| Set | Flat C | Two-level C (UB) | Two-level class LP lower | R_CP (two-level UB) | Pricing |",
                  "|---|---:|---:|---:|---:|---|"]
        for r in levels:
            flat=json.loads((OUT/f"{r['name']}_certificate.json").read_text())
            lines.append(f"| {r['name']} | {flat['C_flat_UB']:.8f} | {r['C_two_level_UB']:.8f} | {r['two_level_class_LP_lower']:.8f} | {r['R_CP_two_level_UB']:.8f} | {r['stop']} |")
    else:
        lines += ["", "The optional two-level task was not run: the required flat benchmarks and adversarial search took priority."]
    lines += ["", "## Reproduction and artifacts", "",
              "Source: [src/e111_cp.py](../../src/e111_cp.py). Data: [examples/e111](../../examples/e111/). "
              "All paths in this report are relative to `.research/agents/`. No files outside the permitted code, data, and report locations were intentionally edited by this task.", "",
              "```sh",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 3600 python src/e111_cp.py suite --seconds 120 --price-seconds 8",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 2400 python src/e111_cp.py search --seconds 60 --price-seconds 6 --search-seconds 20 --eval-seconds 1 --eval-price-seconds 0.25 --moves 80 --restarts 3",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 1800 python src/e111_cp.py refine --seconds 120 --price-seconds 10",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 1200 python src/e111_cp.py polish --X 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 --seconds 60 --price-seconds 6 --search-seconds 10 --moves 60 --eval-seconds 1 --eval-price-seconds 0.25",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 300 python src/e111_cp.py warm_controls --seconds 30 --price-seconds 5",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 600 python src/e111_cp.py levels --seconds 45 --price-seconds 5 --only search_X11 search_X12 X30_s0",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 600 python src/e111_cp.py levels --seconds 45 --price-seconds 5 --only X30_s1 search_X13 search_X14",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 600 python src/e111_cp.py audit",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 300 python src/e111_cp.py verify",
              "DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 300 python src/e111_cp.py report",
              "```", "",
              "The first two jobs ran concurrently with two-core quotas each; do not add their per-case wall times to infer elapsed session time. "
              "`suite.jsonl`, `search_summary.json`, `search_trace.jsonl`, `*_certificate.json`, and `verification.json` contain the results. "
              "`metadata_*.json` records commands, host, Python/NumPy/Gurobi versions, and tolerances; later metadata also includes the final source SHA-256. "
              "The initial suite/search processes loaded the initial source before the optional refinement, polish, and postprocessing code was added. "
              "The final source retains the algorithms and adds stronger bounded pricing retries for stalled cases; under time limits, "
              "reproduction need not yield identical search move counts or identical LP bases.", ""]
    # This is the only permitted write under .research.
    Path(".research/agents/e111_report.md").write_text("\n".join(lines))
    print("REPORT_WRITTEN",len(suite),len(search),"best",best["name"],best["R_CP_flat_UB"],flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode",choices=["suite","search","levels","verify","audit","report","refine","polish","warm_controls"])
    p.add_argument("--seconds",type=float,default=120)
    p.add_argument("--price-seconds",type=float,default=10)
    p.add_argument("--only",nargs="*",default=[])
    p.add_argument("--resume",action="store_true")
    p.add_argument("--X",nargs="*",type=int,default=list(range(10,41)))
    p.add_argument("--moves",type=int,default=60)
    p.add_argument("--restarts",type=int,default=3)
    p.add_argument("--search-seconds",type=float,default=30)
    p.add_argument("--eval-seconds",type=float,default=2)
    p.add_argument("--eval-price-seconds",type=float,default=0.5)
    args = p.parse_args()
    if "dirichlet" not in socket.gethostname():
        raise SystemExit("Heavy computation must run on dirichlet via src/dirun.sh")
    OUT.mkdir(exist_ok=True)
    write_json(OUT/f"metadata_{args.mode}.json",metadata(args))
    {"suite":run_suite,"search":run_search,"levels":run_levels,"verify":lambda _:verify_saved(),
     "audit":audit_threshold,"report":run_report,"refine":run_refine,"polish":run_polish,
     "warm_controls":run_warm_controls}[args.mode](args)


if __name__ == "__main__":
    main()
