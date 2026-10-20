"""E114c: clique number of the Jedwab–Li PDS Cayley graph (exact, networkx max_weight_clique branch and bound on the
neighbourhood of 0; vertex-transitive so omega = 1 + clique number of G[D]) and the CP lower bound
C_CP >= |D|/(omega − 1) (P76(b) in group form), against K = p^{a−1} (lead, cont. 30).
Usage: python src/e114c_omega.py p a j
"""
import sys, json, time
import networkx as nx
sys.path.insert(0, "src")
from e114_cp_group import jl_set

def main():
    p, a, j = (int(t) for t in sys.argv[1:4])
    D, m = jl_set(p, a, j); r = p ** (a - 1); V = sorted(D)
    sub = lambda u, v: ((u[0] - v[0]) % m, (u[1] - v[1]) % m)
    G = nx.Graph(); G.add_nodes_from(range(len(V)))
    for s in range(len(V)):
        for t in range(s + 1, len(V)):
            if sub(V[t], V[s]) in D: G.add_edge(s, t)
    t0 = time.time(); c, w = nx.max_weight_clique(G, weight=None)
    omega = len(c) + 1
    out = dict(p=p, a=a, j=j, size=len(D), K=r, ratio=len(D) / r ** 2, delsarte=1 + len(D) // r, omega=omega,
               CP_lower=len(D) / (omega - 1), CP_lower_over_K=len(D) / (omega - 1) / r, seconds=round(time.time() - t0, 1),
               clique=[V[i] for i in c])
    print(json.dumps(out), flush=True)
    json.dump(out, open(f"examples/e114/jl_omega_p{p}a{a}j{j}.json", "w"))

if __name__ == "__main__":
    main()
