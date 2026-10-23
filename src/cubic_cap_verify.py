"""Independent reconstruction of the new cubic-cap rational certificate.

Port the existing independent verifier read-only: own SymPy rational
reconstruction, finite-symbol/long-line checks, exact interval coverage,
and direct Schur integrals/interpolation. Reconstruct both objective
branches and validate every conservative cubic cap. No optimizer.
"""
from pathlib import Path
import socket


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    source = Path('examples/r11_certificates/independent_verify.py').read_text()
    substitutions = {
        "OUT=Path('.research/agents/tdense11_scratch')":
            "OUT=Path('.research/experiments/cubic_cap_2026-10-23')",
        "OUT.joinpath('certificate_td.json')": "OUT.joinpath('certificate.json')",
        "OUT/'certificate_td.json'": "OUT/'certificate.json'",
        "support=json.load(open(OUT/'support_lines.json'))":
            "support=json.load(open('examples/r11_certificates/support_lines.json'))",
        "k=(2*K+jj-1)//jj-1 if jj else None\n        assert cell['support_k']==k":
            """k=(2*K+jj-1)//jj-1 if jj else None
        assert cell['support_k']==k
        bcap=R(cell['cubic_cap'])
        assert 0<bcap<=R(2,3)
        assert bcap*bcap*(1-bcap)>=R(4,27)*cap*cap""",
        "P=sp.Poly(u*u*(2-u*u)/4,u,domain=sp.QQ)-A*A":
            """v=R(2,3)*x*x
                if leaf['mode']=='tangent':
                    assert sp.expand(v).subs(u,h)>=bcap
                    # Numerator2-b-v is at least2/3 on0<=u<=1.
                    assert bcap<=R(2,3) and 0<=l<h<=1
                    P=sp.Poly((2-bcap-v)**2,u,domain=sp.QQ)-16*(1-bcap)*A*A
                else:
                    assert leaf['mode']=='radical'
                    P=sp.Poly((1-v)/4,u,domain=sp.QQ)-A*A""",
        "assert D==R(259,2000) and 1/D>R(77,10)":
            "assert c['sigma']=='2/3' and c['envelope']=='cubic_profile_support_cap_with_convex_tangent_extension' and D==R(29,400) and 1/D>R(1000,73)",
        "independent_method='SymPy QQ + FLINT composition; direct exact Schur integrals/interpolation; Sturm long lines; rational finite-symbol evaluations'":
            "independent_method='SymPy QQ reconstruction of radical/tangent branches and cubic caps; exact leaf coverage; direct Schur integrals/interpolation; Sturm long lines; rational finite-symbol evaluations'",
        "files=sorted(OUT.glob('*.py'))+[OUT/'certificate.json']":
            "files=[Path('src/cubic_cap_certify.py'),Path('src/cubic_cap_verify.py'),Path('src/cubic_cap_discovery.py'),Path('examples/r11_certificates/certify.py'),Path('examples/r11_certificates/independent_verify.py'),OUT/'certificate.json']",
        "C11=str(1/D),C11_float=float(1/D)":
            "dense_C=str(1/D),dense_C_float=float(1/D)",
    }
    for old, new in substitutions.items():
        assert source.count(old) == 1, old
        source = source.replace(old, new)
    ns = {'__name__': 'cubic_cap_independent'}
    exec(compile(source, 'cubic_cap_independent', 'exec'), ns)
    ns['verify']()


if __name__ == '__main__':
    main()
