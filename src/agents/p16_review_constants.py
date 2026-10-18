"""Independent referee recomputation of the P16 constants (written from scratch; does not import p16_constants.py).

Everything in mpmath at 50 digits.  Conventions as in PROOFS.md P16:
  delta = sqrt(theta*eta*k)            (P16 itself: theta = 1/2, i.e. delta^2 = eta*k/2)
  Sbar(h) = int_{2/h}^inf (a t^{1/2} + b t^{1/4} + g) * 8/(h^2 t^3) dt   (checked against quadrature below)
  h       = smallest h (up to 1e-30 relative) with Sbar(h) < delta  (we take h = h0*(1+1e-30), Sbar(h0) = delta)
P16 original (Lipschitz) test   : 2 r n > 2pi*E4/tau^4, r = (1-theta)eta/(6L+1), n = floor(2pi/(2h+2r)),
                                  tau = (1-theta) eta k   [theta = 1/2 gives r = eta/(2(6L+1)), tau = eta k/2, RHS <= 24pi/(eta^4 k^2)]
Referee variant (large sieve)   : m (2(1-theta) eta k)^4 >= (4D + pi/h) E4,  m = floor(pi/(2h)), D = 6L+1.
E4 = 3k^2/4 - 3k/8 (exact); the author's test uses the cruder 3k^2/4.
"""
import mpmath as mp

mp.mp.dps = 50
A_ = mp.sqrt(mp.mpf(2) / 3)
B_ = (mp.mpf(2) / 3) ** mp.mpf('0.25')
G_ = 1 + mp.sqrt(mp.mpf(4) / 3) + (mp.mpf(4) / 3) ** mp.mpf('0.25')
G1 = mp.mpf(3)            # gamma if one uses the sharper count m <= 2t/3 + 1 (referee remark)


def sbar(h, g=G_):
    X = 2 / h
    return (8 / h ** 2) * (2 * A_ / 3 * X ** mp.mpf(-1.5) + 4 * B_ / 7 * X ** mp.mpf(-1.75) + g / 2 * X ** -2)


def sbar_quad(h, g=G_):
    return mp.quad(lambda t: (A_ * mp.sqrt(t) + B_ * t ** mp.mpf(0.25) + g) * 8 / (h ** 2 * t ** 3), [2 / h, 20 / h, mp.inf])


def hstar(delta, g=G_):
    if delta <= g:                      # Sbar(h) -> g as h -> inf, and Sbar is decreasing
        return None
    f = lambda lh: sbar(mp.e ** lh, g) - delta
    lo, hi = mp.mpf(-200), mp.mpf(50)
    for _ in range(400):
        mid = (lo + hi) / 2
        if f(mid) >= 0: lo = mid
        else: hi = mid
    return mp.e ** hi * (1 + mp.mpf(10) ** -30)


def E4(k):
    return mp.mpf(3) * k * k / 4 - mp.mpf(3) * k / 8


def holds_lip(k, L, eta, theta=mp.mpf(1) / 2, exactE4=False, g=G_):
    k, L, eta = mp.mpf(k), mp.mpf(L), mp.mpf(eta)
    delta = mp.sqrt(theta * eta * k)
    h = hstar(delta, g)
    if h is None: return False
    r = (1 - theta) * eta / (6 * L + 1)
    n = mp.floor(2 * mp.pi / (2 * h + 2 * r))
    tau = (1 - theta) * eta * k
    e4 = E4(k) if exactE4 else mp.mpf(3) * k * k / 4
    return 2 * r * n > 2 * mp.pi * e4 / tau ** 4


def holds_ls(k, L, eta, theta=mp.mpf(1) / 5, g=G_):
    k, L, eta = mp.mpf(k), mp.mpf(L), mp.mpf(eta)
    delta = mp.sqrt(theta * eta * k)
    h = hstar(delta, g)
    if h is None: return False
    m = mp.floor(mp.pi / (2 * h))
    if m < 1: return False
    D = 6 * L + 1
    return m * (2 * (1 - theta) * eta * k) ** 4 >= (4 * D + mp.pi / h) * E4(k)


def min_eta(test, k, L, **kw):
    if not test(k, L, mp.mpf(1) / 2, **kw): return None
    lo, hi = mp.mpf(0), mp.mpf(1) / 2
    for _ in range(60):
        mid = (lo + hi) / 2
        if test(k, L, mid, **kw): hi = mid
        else: lo = mid
    return hi


def best_theta(test, k, L, grid):
    best = None
    for th in grid:
        e = min_eta(test, k, L, theta=th)
        if e is not None and (best is None or e < best[0]): best = (e, th)
    return best


if __name__ == '__main__':
    print("1. Sbar closed form vs quadrature, and Sbar*sqrt(h):")
    for h in ('1e-1', '1e-2', '1e-4', '1e-6', '1e-8'):
        h = mp.mpf(h)
        print(f"   h={mp.nstr(h,3):>6}  closed={mp.nstr(sbar(h),12)}  quad={mp.nstr(sbar_quad(h),12)}  Sbar*sqrt(h)={mp.nstr(sbar(h)*mp.sqrt(h),6)}")
    print(f"   leading coefficient 16*alpha/(3*2^1.5) = {mp.nstr(16*A_/(3*2**mp.mpf(1.5)),8)}; gamma = {mp.nstr(G_,8)}")
    print("2. P16 as stated (theta=1/2, E4 <= 3k^2/4): minimal eta, R >= 1/2 - eta")
    for k in (10**4, 10**5, 10**6, 10**7, 10**8, 10**10, 10**12):
        row = []
        for name, c in (("k^2/2", mp.mpf(1) / 2), ("12.5k^2", mp.mpf(25) / 2), ("32k^2", mp.mpf(32))):
            e = min_eta(holds_lip, k, c * k * k)
            row.append(f"L={name}: " + ("none" if e is None else f"R>={mp.nstr(mp.mpf(1)/2-e,4)}"))
        print(f"   k=1e{len(str(k))-1}: " + " | ".join(row))
    # smallest k for which P16 is nontrivial with L = k^2/2
    def kmin(test, c, **kw):
        lo, hi = 10, 10 ** 9
        while hi / lo > 1.01:
            mid = int(mp.sqrt(lo * hi))
            if min_eta(test, mid, c * mid * mid, **kw) is not None: hi = mid
            else: lo = mid
        return hi
    print(f"   smallest k with some eta<=1/2 (L=k^2/2): ~{kmin(holds_lip, mp.mpf(1)/2)};  (L=12.5k^2): ~{kmin(holds_lip, mp.mpf(25)/2)}")
    print("3. Asymptotic constant: k^3 > c L eta^-6 ; fitted c from eta_min at k=1e12, L=k^2/2")
    k = mp.mpf(10) ** 12; L = k * k / 2; e = min_eta(holds_lip, k, L)
    print(f"   eta_min={mp.nstr(e,6)}  c = k^3 eta^6 / L = {mp.nstr(k**3*e**6/L,6)}  (author: ~690)")
    print("4. REFEREE IMPROVEMENTS (not part of P16 as stated):")
    print("   (a) Lipschitz proof with optimised theta (delta^2 = theta*eta*k):")
    for k in (10**5, 10**6, 10**8, 10**10, 10**12):
        b = best_theta(holds_lip, k, k * k // 2, [mp.mpf(i) / 24 for i in range(1, 20)])
        print(f"       k=1e{len(str(k))-1}, L=k^2/2: " + ("none" if b is None else f"R >= {mp.nstr(mp.mpf(1)/2-b[0],4)} (theta={mp.nstr(b[1],3)})"))
    print("   (b) large-sieve proof (no Lipschitz bound), best theta:")
    for k in (10**3, 10**4, 10**5, 10**6, 10**8, 10**10, 10**12):
        row = []
        for name, c in (("k^2/2", mp.mpf(1) / 2), ("12.5k^2", mp.mpf(25) / 2), ("32k^2", mp.mpf(32))):
            b = best_theta(holds_ls, k, c * k * k, [mp.mpf(i) / 40 for i in range(2, 21)])
            row.append(f"L={name}: " + ("none" if b is None else f"R>={mp.nstr(mp.mpf(1)/2-b[0],4)} (th={mp.nstr(b[1],2)})"))
        print(f"       k=1e{len(str(k))-1}: " + " | ".join(row))
    print(f"       smallest k with some eta<=1/2 (L=k^2/2, theta=1/5): ~{kmin(holds_ls, mp.mpf(1)/2)}")
    k = mp.mpf(10) ** 12; L = k * k / 2; e = min_eta(holds_ls, k, L)
    print(f"       asymptotic: eta_min={mp.nstr(e,6)} at k=1e12; c5 = k^3 eta^5 / L = {mp.nstr(k**3*e**5/L,6)} (heuristic ~20.7)")
