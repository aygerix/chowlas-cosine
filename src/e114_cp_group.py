"""E114: flat completely-positive certificate cost for symmetric D in G = Z_m^2 (lead, cont. 30).
Is the Jedwab–Li non-subgroup LS PDS (CSTAR A9) CP-efficient? Flat CP: cliques B ∋ 0 of Cay(G, D) (B ⊂ D ∪ {0},
B − B ⊂ D ∪ {0}), weights w >= 0, Σ_B w_B m_B(h) = 1_D(h) (h ≠ 0, unordered ±pairs), cost C = Σ_B w_B |B|.
Then Σ w_B |F_B(χ)|² = C + D̂(χ), so K <= C. Column generation: Gurobi LP master + exact Gurobi MILP pricing
(max Σ_{pairs} y − |B| over cliques containing 0). Output: K, ratio |D|/K², clique number, C_flat (UB; LB = LP dual
when the final pricing is optimal), and the block structure. Numerical LP (Gurobi tolerances).
Usage: python src/e114_cp_group.py p a j [tlim]
"""
import sys, json, cmath, math, itertools
import gurobipy as gp

def jl_set(p, a, j):
    m = p ** a; D = set()
    for x in range(m):
        for y in range(1, m):
            k = 0; yy = y
            while yy % p == 0: yy //= p; k += 1
            b = a - k; mb = p ** b; z = (y // p ** k) % mb
            v = ((x % mb) * pow(z, -1, mb)) % mb
            if j * p ** (b - 1) <= v < (j + 1) * p ** (b - 1): D.add((x, y))
    return D, m

def main():
    p, a, j = (int(t) for t in sys.argv[1:4]); tlim = float(sys.argv[4]) if len(sys.argv) > 4 else 600
    D, m = jl_set(p, a, j)
    assert all(((-x) % m, (-y) % m) in D for x, y in D) and (0, 0) not in D
    sub = lambda u, v: ((u[0] - v[0]) % m, (u[1] - v[1]) % m)
    key = lambda h: min(h, ((-h[0]) % m, (-h[1]) % m))
    vals = []
    for u in range(m):
        for v in range(m):
            if (u, v) == (0, 0): continue
            vals.append(sum(math.cos(2 * math.pi * (u * x + v * y) / m) for x, y in D))
    K = -min(vals); lags = sorted({key(h) for h in D}); V = sorted(D)
    # pricing graph on V (0 is forced into B)
    adj = {(s, t) for s in range(len(V)) for t in range(s + 1, len(V)) if sub(V[t], V[s]) in D}
    def m_of(B):
        cnt = {}
        for s in range(len(B)):
            for t in range(s + 1, len(B)):
                h = key(sub(B[t], B[s])); cnt[h] = cnt.get(h, 0) + 1
        return cnt
    cols = [[(0, 0), h] for h in lags]
    pr = gp.Model(); pr.Params.OutputFlag = 0; pr.Params.TimeLimit = tlim
    x = pr.addVars(len(V), vtype=gp.GRB.BINARY)
    z = {}
    for s in range(len(V)):
        for t in range(s + 1, len(V)):
            if (s, t) in adj:
                z[s, t] = pr.addVar(lb=0, ub=1); pr.addConstr(z[s, t] <= x[s]); pr.addConstr(z[s, t] <= x[t])
                pr.addConstr(z[s, t] >= x[s] + x[t] - 1)
            else:
                pr.addConstr(x[s] + x[t] <= 1)
    pr.update()
    # clique number (cliques containing 0): maximise Σ x
    pr.setObjective(gp.quicksum(x[s] for s in range(len(V))), gp.GRB.MAXIMIZE); pr.optimize()
    omega = int(round(pr.ObjVal)) + 1; omega_status = pr.Status
    it = 0
    while True:
        it += 1
        mst = gp.Model(); mst.Params.OutputFlag = 0
        w = [mst.addVar(lb=0) for _ in cols]; mc = [m_of(B) for B in cols]
        cons = {h: mst.addConstr(gp.quicksum(w[i] * mc[i].get(h, 0) for i in range(len(cols))) == 1) for h in lags}
        mst.setObjective(gp.quicksum(w[i] * len(B) for i, B in enumerate(cols)), gp.GRB.MINIMIZE); mst.optimize()
        C = mst.ObjVal; y = {h: cons[h].Pi for h in lags}
        obj = gp.quicksum(y[key(V[s])] * x[s] for s in range(len(V))) - gp.quicksum(x[s] for s in range(len(V)))
        obj += gp.quicksum(y[key(sub(V[t], V[s]))] * z[s, t] for (s, t) in z)
        pr.setObjective(obj, gp.GRB.MAXIMIZE); pr.optimize()
        red = pr.ObjVal - 1   # the element 0 itself costs 1
        status = "opt" if pr.Status == 2 else "timelimit"
        print(json.dumps(dict(it=it, C=C, reduced=red, status=status, ncols=len(cols))), flush=True)
        if red <= 1e-7: break
        B = [(0, 0)] + [V[s] for s in range(len(V)) if x[s].X > 0.5]
        if B in cols: status = "stalled"; break
        cols.append(B)
    used = [(w[i].X, len(B)) for i, B in enumerate(cols) if w[i].X > 1e-9]
    sizes = {}
    for wt, sz in used: sizes[sz] = sizes.get(sz, 0) + wt
    out = dict(p=p, a=a, j=j, m=m, size=len(D), K=K, ratio=len(D) / K ** 2, omega=omega, omega_status=omega_status,
               delsarte=1 + len(D) / K, C_flat=C, eff=C / K, final_pricing=status, weight_by_block_size=sizes)
    print(json.dumps(out), flush=True)
    json.dump(out, open(f"examples/e114/jl_p{p}a{a}j{j}.json", "w"))

if __name__ == "__main__":
    main()
