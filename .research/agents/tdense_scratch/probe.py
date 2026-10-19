"""Targeted, uncertified diagnostics. Run ONLY through src/dirun.sh -c 2.

Exact membership checks use integers. Floating minima are heuristic evidence.
No solver or search is used. Output records all generated sets and parameters.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

sys.path.insert(0, "src")
from box_minlam import true_min
from bu import A_of_S

OUT = Path(".research/agents/tdense_scratch")


def coeff_min(b):
    X = len(b) - 1
    G = 1 << math.ceil(math.log2(64 * X))
    cf = np.zeros(2 * G)
    cf[:len(b)] = b
    v = np.fft.rfft(cf).real
    j = int(v.argmin())
    x0 = math.pi * j / G
    js = np.flatnonzero(b)
    def val(x):
        return float(np.dot(b[js], np.cos(js * x)))
    opt = minimize_scalar(val, bounds=(max(0, x0-math.pi/G),
                                      min(math.pi, x0+math.pi/G)),
                          method="bounded", options={"xatol": 1e-14})
    return min(float(v[j]), float(opt.fun)), float(opt.x), val(float(opt.x))


def p31(b):
    X = len(b) - 1
    E = float(np.dot(b[1:], b[1:]))
    prefix = [np.cumsum((b[1:] ** 2) * np.arange(1, X+1) ** k)
              for k in range(3)]
    ws = np.arange(1, X+1)
    S = prefix[0] - 2*prefix[1]/(ws+1) + prefix[2]/(ws+1)**2
    W = 2*(ws+1)/3 + 1/(3*(ws+1))
    C = .811*(X+ws+1) + 71/300
    lbs = (W*E-C*S)/(2*(C-W))
    w = int(lbs.argmax())
    return {"E": E, "lb": math.sqrt(max(0, float(lbs[w]))),
            "w": w+1, "lb2_max": float(lbs[w])}


def cumulative_exact_quadratic(X, shift=0):
    den = 2*X*X
    acc = shift
    old = acc//den
    a = np.zeros(X+1)
    for j in range(1, X+1):
        acc += (X-j)**2
        new = acc//den
        a[j] = new-old
        old = new
    return a


def run(name, a, p=None):
    A = np.flatnonzero(a).astype(int).tolist()
    assert A and min(A)>0 and len(A)==len(set(A))
    X = max(A)
    a = a[:X+1]
    (fm, xm), _, _ = true_min(A)
    direct = float(np.cos(np.array(A)*xm).sum())
    out = {"name": name, "n": len(A), "X": X, "R": -fm/math.sqrt(len(A)),
           "xmin": float(xm), "M": -float(fm), "direct_error": direct-float(fm),
           "longest_run": 0, "A": A, "original": p31(a), "filters": {}}
    streak = 0
    for v in a[1:]:
        streak = streak+1 if v else 0
        out["longest_run"] = max(streak, out["longest_run"])
    for q in [1, 2, 4, 8, 16]:
        b = np.zeros(X+q+1)
        def av(j):
            return a[abs(j)] if abs(j)<=X else 0
        for j in range(1, X+q+1):
            b[j] = av(j)-(av(j-q)+av(j+q))/2
        z = p31(b)
        z["implied_M"] = (z["lb"]+av(q)/2)/2
        out["filters"][str(q)] = z
        test_x = .732123
        lhs = (1-math.cos(q*test_x))*float(np.cos(np.array(A)*test_x).sum())+av(q)/2
        rhs = float(np.dot(b[1:], np.cos(np.arange(1, len(b))*test_x)))
        assert abs(lhs-rhs)<1e-8*(1+len(A)), (name,q,lhs,rhs)
    if p is not None:
        # Keep full ambient support: beta contains -p even beyond max A.
        aa = np.zeros_like(p)
        aa[A] = 1
        beta = aa-p
        mb, xb, dv = coeff_min(beta)
        smooth = float(np.dot(p[1:], np.cos(np.arange(1,len(p))*xb)))
        out["fluctuation"] = {**p31(beta), "min": mb, "xmin": xb,
                              "smooth_at_min": smooth,
                              "prefix_discrepancy": float(np.max(np.abs(np.cumsum(beta)))),
                              "fft_direct_error": dv-mb}
    print(json.dumps({k:v for k,v in out.items() if k!="A"}), flush=True)
    return out


def main():
    rng = np.random.default_rng(20261019)
    records = []
    for X in [384, 1536, 6144]:
        p = np.r_[0, .5*(1-np.arange(1,X+1)/X)**2]
        records.append(run(f"quadratic_exact_beatty_X{X}", cumulative_exact_quadratic(X), p))
    X = 1536
    t = np.arange(1,X+1)/X
    profiles = {"quadratic": .5*(1-t)**2,
                "quartic": .5*(1-t)**4,
                "twolvl": np.where(t<=.2,.45,.035)}
    for alpha in [.5, .75]:
        profiles[f"powerlaw_alpha{alpha}"] = np.minimum(.5, .09*t**(alpha-1))
    for name, pp in profiles.items():
        p = np.r_[0,pp]
        rounded = np.r_[0,np.diff(np.r_[0,np.floor(np.cumsum(pp))])]
        random = np.r_[0,(rng.random(X)<pp).astype(float)]
        records.append(run(name+"_beatty",rounded,p))
        records.append(run(name+"_random_seed20261019",random,p))
    for path in ["examples/construct/N50_certified.json", "examples/smallN_best.json"]:
        data = json.load(open(path))
        selected = list(data) if "N50" in path else [k for k in ["4","10","20","30","50"] if k in data]
        for key in selected:
            A = data[key]["A"]
            a = np.zeros(max(A)+1)
            a[A] = 1
            records.append(run(path+":"+key,a))
    data = json.load(open("examples/singer_bu/certified.json"))
    A = A_of_S(data["61"]["S"])
    a = np.zeros(max(A)+1)
    a[A] = 1
    records.append(run("Singer_Bu_q61",a))
    (OUT/"probe.json").write_text(json.dumps({"seed":20261019,
        "status":"NUMERICAL, floating minima uncertified", "records":records},indent=2))


if __name__ == "__main__":
    main()
