"""E114b: is the Jedwab–Li PDS graph Cay(Z_{p^a}^2, D) GEOMETRIC (lines = Delsarte cliques of size n = p^a)?
(lead, cont. 30). If the maximum cliques through 0 have size 1 + |D|/K = n and partition D (each element of D lies in
exactly one of them), then the translates of these cliques give a flat CP certificate of cost exactly K = r (each
edge on one line), so C_CP = K (lower bound K from PSD). Exact combinatorics (networkx maximal cliques).
Usage: python src/e114b_cliques.py p a j
"""
import sys, json, math
import networkx as nx
sys.path.insert(0, "src")
from e114_cp_group import jl_set

def main():
    p, a, j = (int(t) for t in sys.argv[1:4])
    D, m = jl_set(p, a, j); n_ = p ** a; r = p ** (a - 1)
    V = sorted(D); idx = {v: i for i, v in enumerate(V)}
    sub = lambda u, v: ((u[0] - v[0]) % m, (u[1] - v[1]) % m)
    G = nx.Graph(); G.add_nodes_from(range(len(V)))
    for s in range(len(V)):
        for t in range(s + 1, len(V)):
            if sub(V[t], V[s]) in D: G.add_edge(s, t)
    deg = sorted(set(dict(G.degree()).values()))
    mx = 0; big = []
    for c in nx.find_cliques(G):
        if len(c) > mx: mx = len(c); big = []
        if len(c) == mx: big.append(frozenset(c))
    cover = {}
    for c in big:
        for v in c: cover[v] = cover.get(v, 0) + 1
    cov_counts = sorted(set(cover.get(v, 0) for v in range(len(V))))
    is_sub = [all(((V[x][0] + V[y][0]) % m, (V[x][1] + V[y][1]) % m) in D | {(0, 0)} for x in c for y in c) for c in big]
    out = dict(p=p, a=a, j=j, size=len(D), lambda_degrees=deg, omega=mx + 1, delsarte=1 + len(D) // r,
               n_max_cliques=len(big), cover_counts=cov_counts, subgroup_cliques=sum(is_sub),
               geometric=(mx + 1 == n_ and cov_counts == [1]))
    print(json.dumps(out), flush=True)
    json.dump(out, open(f"examples/e114/jl_cliques_p{p}a{a}j{j}.json", "w"))

if __name__ == "__main__":
    main()
