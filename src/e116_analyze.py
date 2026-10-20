r"""E116 analysis (advisor's second review, cont. 31). For a Boolean lift T ⊂ Z² of a JL set D ⊂ Z_n², report
  - energy Ɛ = Σ_{s≠0}|a_s|² (= |T| for a 0/1 set, Σw² for weights), K = −min, ρ = Ɛ/K², and the exact split
        ρ_int/ρ_G = (Ɛ_int/Ɛ_G)·(K_G/K_int)²;
  - a CERTIFIED enclosure of K for the 1D integer image A = {z₁ + V z₂ > 0} (V = 4L + 3):
        K_up = 2·(−certify_lower_bound(A))  [rigorous: M(A) <= K_up/2],
        K_low = 2·(−f_A(x*)) at the numerical minimiser x*, evaluated with mpmath at 60 digits [error < 1e−40];
    (the 2D minimum is only an upper bound for the 1D one; the 1D set is the actual Chowla object);
  - WHERE the rounding error lives: reference = fractional lift w_z = τ(z)·m(z mod n), τ = Λ(z₁/n)Λ(z₂/n), m = class
    multiplicities of T; e = F_T − F_w on a G×G grid; split ∫e² and min e over Σ+ = {F_w > 0} (spike region) and
    Σ− = {F_w <= 0} (background). Grid quantities are NUMERICAL.
Usage: python src/e116_analyze.py <jsonl file> <line index> [sa:<p,a,j,L,full,outfile>]
"""
import sys, json, math
import numpy as np
import mpmath as mp
sys.path.insert(0, "src")
from e114_cp_group import jl_set
from e116_jl_taper import lift, true_min, finite_K
import chowla


def analyze(p, a, j, T, label=""):
    D, n = jl_set(p, a, j)
    KG = finite_K(D, n); EG = len(D)
    m = {}
    for z in T:  # class multiplicities over the FULL symmetric set
        g = (int(z[0]) % n, int(z[1]) % n); m[g] = m.get(g, 0) + 1
    T = np.array([z for z in T if (z[0] > 0 or (z[0] == 0 and z[1] > 0))], dtype=np.int64)  # one per ±pair
    L = int(np.abs(T).max())
    w1 = np.ones(len(T))
    fmin2, xi, _, _ = true_min(T, w1, L, G=1 << int(math.ceil(math.log2(32 * (2 * L + 1)))), nstart=24)
    E = 2 * len(T)
    V = 4 * L + 3
    img = sorted({int(z[0] + V * z[1]) if z[0] + V * z[1] > 0 else int(-(z[0] + V * z[1])) for z in T})
    assert len(img) == len(T)
    A = img
    lb = chowla.certify_lower_bound_blocked(A).lower_bound   # g(t) = Σ cos(2π a t) >= lb for all t (rigorous)
    est = chowla.min_estimate_fft(A)                          # argmin in radians (numerical)
    mp.mp.dps = 60
    fx = mp.fsum(mp.cos(mp.mpf(a_) * mp.mpf(est.xmin)) for a_ in A)  # f_A at a definite point: an upper bound on min
    K_low = -2 * float(fx)
    K_up = -2 * float(lb)
    out = {"label": label, "p": p, "a": a, "j": j, "n": n, "Ɛ": E, "Ɛ_G": EG, "K_G": KG, "K_2D": -fmin2,
           "K_1D_low": K_low, "K_1D_up": K_up, "rho_cert": [E / K_up ** 2, E / K_low ** 2],
           "rho_G": EG / KG ** 2, "energy_factor": E / EG, "K_factor_sq": (KG / K_up) ** 2,
           "n1D": len(A), "maxA": max(A)}
    # where does the rounding error live?
    Lr = n
    ref = []
    wts = []
    for z1 in range(-Lr, Lr + 1):
        for z2 in range(-Lr, Lr + 1):
            if z1 > 0 or (z1 == 0 and z2 > 0):
                g = (z1 % n, z2 % n)
                if g in m:
                    t = (1 - abs(z1) / Lr) * (1 - abs(z2) / Lr)
                    if t > 0:
                        ref.append((z1, z2)); wts.append(t * m[g])
    ref = np.array(ref, dtype=np.int64); wts = np.array(wts)
    Gs = 1 << int(math.ceil(math.log2(8 * (2 * max(L, Lr) + 1))))
    def grid(P, w):
        Ar = np.zeros((Gs, Gs))
        np.add.at(Ar, (P[:, 0] % Gs, P[:, 1] % Gs), w)
        np.add.at(Ar, ((-P[:, 0]) % Gs, (-P[:, 1]) % Gs), w)
        return np.fft.fft2(Ar).real
    FT = grid(T, w1); FW = grid(ref, wts); e = FT - FW
    sp = FW > 0; bg = ~sp
    out.update({"Ɛ_ref": 2 * float((wts ** 2).sum()), "K_ref_grid": float(-FW.min()),
                "spike_measure": float(sp.mean()), "e2_total": float((e ** 2).mean()),
                "e2_spike_frac": float((e[sp] ** 2).sum() / (e ** 2).sum()),
                "min_e_bg": float(e[bg].min()), "min_e_spike": float(e[sp].min()),
                "min_FT_bg": float(FT[bg].min()), "min_FT_spike": float(FT[sp].min())})
    return out


if __name__ == "__main__":
    f, i = sys.argv[1], int(sys.argv[2])
    d = json.loads(open(f).read().splitlines()[i])
    if "reps" in d:
        T = d["reps"]; T = T + [[-u, -v] for u, v in T]
    elif "T_pairs" in d:
        T = d["T_pairs"]; T = T + [[-u, -v] for u, v in T]
    else:
        raise SystemExit("no set")
    print(json.dumps(analyze(d["p"], d["a"], d["j"], T, label=f"{f}:{i}")), flush=True)
