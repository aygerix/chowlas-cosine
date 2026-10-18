"""Finite checks of the wider-residue dichotomy. Execute only on dirichlet.
Seed 20261019. This uses no optimization or ILP.
"""
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np

rng = np.random.default_rng(20261019)
records = []
for t in (1, 2, 3, 4):
    for ell in (0, 1, 3, 5):
        B = ell**2 + (ell+1)**2
        J = 2*ell+3
        # General fibers are independent sets in the graph with edges t,2t.
        for trial in range(5):
            fibers = {}
            for y in range(1, 13):
                chosen = []
                for r in rng.permutation(ell*t+1):
                    r = int(r)
                    if rng.random() < .6 and all(abs(r-s) not in (t, 2*t) for s in chosen):
                        chosen.append(r)
                if chosen:
                    fibers[y] = sorted(chosen)
            if not fibers:
                fibers[1] = [0]
            if ell >= 3 and trial == 0:
                fibers = {y: [0, 3*t] for y in range(1, 13)}
            residues = sorted({r for rs in fibers.values() for r in rs})
            counts = {r: sum(r in rs for rs in fibers.values()) for r in residues}
            n = sum(counts.values())
            k = len(residues)
            q = 16 * B * J * t * k

            # Exact integer statistic and the independent DFT/phase formula.
            beta = {(y, a): sum((-1)**((r-a)//t) for r in rs if r % t == a)
                    for y, rs in fibers.items() for a in range(t)}
            ctot = sum(b*b for b in beta.values())
            cs = []
            for j in range(t):
                u = (2*j+1)*math.pi/t
                cs.append(sum(abs(sum(np.exp(1j*r*u) for r in rs))**2
                              for rs in fibers.values()))
            assert abs(np.mean(cs)-ctot) < 1e-8
            nalt = sum((-1)**(r//t)*counts[r] for r in residues if r % t == 0)
            assert nalt*nalt <= n*ctot

            # Projection divided by (1+cos v); use its explicit polynomial,
            # never divide near pi. Verify mean, value at zero and grid sum.
            v = 2*math.pi*np.arange(J)/J
            Rvals = np.zeros(J)
            Nmult = 0
            for r, nr in counts.items():
                if r % t:
                    continue
                h = r//t
                Rvals += nr * (-1)**h * (1 + 2*sum((-1)**a*np.cos(a*v)
                                                    for a in range(1, h+1)))
                Nmult += nr
            assert abs(Rvals.mean()-nalt) < 1e-8
            assert abs(Rvals[0]-Nmult) < 1e-8
            reciprocal = float(np.sum(1/(1+np.cos(v))))
            assert abs(reciprocal-J*J/2) < 1e-8

            # Macro minimum upper enclosure from a grid and curvature bound.
            Ggrid = 32768
            u = 2*math.pi*np.arange(Ggrid)/Ggrid
            profile = sum(nr*(np.cos(r*u)+np.cos((r+t)*u)) for r, nr in counts.items())
            hcurv = sum(nr*(r*r+(r+t)**2) for r, nr in counts.items())
            m_upper = max(0., -float(profile.min())) + hcurv*math.pi**2/(2*Ggrid**2)
            macro_margin = 2*k*J*math.sqrt(n*ctot)+k*(J*J+1)*m_upper-n
            assert macro_margin >= -1e-7
            sharp_macro_margin = 2*k*J*J*(ctot+m_upper)-n
            assert sharp_macro_margin >= -1e-7
            # Independent, simpler finite identity sufficient for Theorem C.
            # N_alt^2 <= N_mult*Ctot is stronger than the earlier n*Ctot check.
            assert nalt*nalt <= Nmult*ctot

            # Actual lifted sample near the optimal Taylor displacement.
            theta = float(rng.uniform(0, 2*math.pi))
            z = {r: sum(np.exp(1j*y*theta) for y, rs in fibers.items() if r in rs)
                 for r in residues}
            curv = sum((r*r+(r+t)**2)*abs(z[r]) for r in residues)
            for j in range(t):
                u0 = (2*j+1)*math.pi/t
                d = t*sum(np.exp(1j*r*u0)*z[r] for r in residues).imag
                ideal = u0-d/curv if curv else u0
                idx = round((q*ideal-theta)/(2*math.pi))
                uu = (theta+2*math.pi*idx)/q
                hv = ((1+np.exp(1j*t*uu))*sum(np.exp(1j*r*uu)*z[r] for r in residues)).real
                mv = max(0., -float(hv))
                assert d*d <= 2*curv*mv+math.pi**2*curv*curv/q**2+1e-6

            records.append({"t": t, "L": ell, "trial": trial, "n": n, "k": k,
                            "q": q, "Ctot": ctot, "mean_Cj": float(np.mean(cs)),
                            "macro_m_upper": m_upper, "macro_inequality_margin": macro_margin,
                            "sharp_macro_margin": sharp_macro_margin,
                            "fibers": fibers})

# Exact cancellation pattern from the report: Ctot=0, macro dip at 5pi/6.
assert 1+(-1)**3 == 0
assert (math.sqrt(3)-1)/2-13*math.pi**2/24**2 > 1/8
out = {"seed": 20261019, "python": platform.python_version(),
       "numpy": np.__version__, "cases": records,
       "minimum_macro_margin": min(r["macro_inequality_margin"] for r in records),
       "minimum_sharp_macro_margin": min(r["sharp_macro_margin"] for r in records),
       "zero_energy_cases": sum(r["Ctot"] == 0 for r in records),
       "quarter_energy_cases": sum(r["Ctot"] < r["n"]/(16*r["k"]**2*(2*r["L"]+3)**2)
                                    for r in records)}
path = Path(__file__).with_name("wide_verification.json")
path.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({"cases": len(records), "minimum_macro_margin": out["minimum_macro_margin"],
                  "zero_energy_cases": out["zero_energy_cases"], "output": str(path)}, indent=2))
