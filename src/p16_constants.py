"""P16 explicit constants (improved visit lemma via the Sidon counting bound).  Closed forms, float with 1e-9 margin.
Sidon counting (Lindström): a Sidon set in m consecutive integers has <= m^{1/2} + m^{1/4} + 1 elements, so with
m <= 2t/3 + 4/3:  N(t) = #{s : |3s+1/2| <= t} <= α t^{1/2} + β t^{1/4} + γ,  α = (2/3)^{1/2}, β = (2/3)^{1/4},
γ = 1 + (4/3)^{1/2} + (4/3)^{1/4}   (√(a+b) <= √a+√b, (a+b)^{1/4} <= a^{1/4}+b^{1/4}).
Visit bound: |P| >= δ on [c-h, c+h] ⇒ δ <= Σ_s sinc^2(|b_s|h/2) <= ∫_{X}^∞ N(t) 8/(h^2 t^3) dt (X = 2/h)
   = (8/h^2)[ (2α/3) X^{-3/2} + (4β/7) X^{-7/4} + (γ/2) X^{-2} ] =: Σbar(h)."""
import math
al, be, ga = math.sqrt(2 / 3), (2 / 3) ** 0.25, 1 + math.sqrt(4 / 3) + (4 / 3) ** 0.25
def sigbar(h):
    X = 2 / h
    return (8 / h ** 2) * (2 * al / 3 * X ** -1.5 + 4 * be / 7 * X ** -1.75 + ga / 2 * X ** -2) * (1 + 1e-9)
def hstar(delta):
    lo, hi = 1e-300, 1e6
    if sigbar(hi) >= delta: return None
    for _ in range(400):
        mid = math.sqrt(lo * hi)
        lo, hi = (mid, hi) if sigbar(mid) >= delta else (lo, mid)
    return hi
def holds(k, L, eta):
    delta = math.sqrt(eta * k / 2); h = hstar(delta)
    if h is None: return False
    r = eta / (2 * (6 * L + 1)); n = math.floor(2 * math.pi / (2 * h + 2 * r))
    return 2 * r * n > 24 * math.pi / (eta ** 4 * k ** 2) * (1 + 1e-9)
for h in (1e-1, 1e-2, 1e-4, 1e-6, 1e-8):
    print(f"h={h:g}: Σbar(h)={sigbar(h):.4f}  Σbar·√h={sigbar(h)*math.sqrt(h):.4f}", flush=True)
for k in (10**4, 10**5, 10**6, 10**7, 10**8, 10**10, 10**12):
    for Lname, L in (("k^2/2", k * k // 2), ("k^2.5", int(k ** 2.5))):
        if not holds(k, L, 0.5): print(f"k={k:.0e} L={Lname}: no eta <= 1/2", flush=True); continue
        lo, hi = 1e-12, 0.5
        for _ in range(200):
            mid = (lo + hi) / 2
            lo, hi = (lo, mid) if holds(k, L, mid) else (mid, hi)
        print(f"k={k:.0e} L={Lname}: M(A(S)) >= (1/2 - {hi:.4f}) k   [R >= {0.5-hi:.4f}]", flush=True)
