"""One fixed discovery LP for a valid cubic-support convex envelope.

For actual v=4e, cubic-profile PD gives v(t)<=b_k, where
b_k^2(1-b_k)=(4/27)cos(pi/(k+2))^2. Replace phi above b_k by
its tangent continuation before Gabor-Jensen. This changes the
objective, not the legacy E95 source. All output remains uncertified.
"""
from pathlib import Path
import socket


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    source = Path('src/e95_discover_sigma.py').read_text()
    substitutions = {
        "OUT=Path('examples/e95'); OUT.mkdir(exist_ok=True)":
            "OUT=Path('.research/experiments/cubic_cap_2026-10-23'); OUT.mkdir(parents=True,exist_ok=True)",
        'model.Params.Threads=4': 'model.Params.Threads=2; model.Params.TimeLimit=100',
        'cap=np.cos(np.pi/(k+2)) if jj else 1.':
            '''cap=np.cos(np.pi/(k+2)) if jj else 1.
        lower_b,upper_b=0.,2/3
        for _ in range(64):
            middle_b=(lower_b+upper_b)/2
            if middle_b*middle_b*(1-middle_b)<4*cap*cap/27:lower_b=middle_b
            else:upper_b=middle_b
        cubic_cap=upper_b if jj else 2/3''',
        'val=sigma*x/(2*(1+math.sqrt(max(0,1-sigma*x*x))))':
            '''val=sigma*x/(2*(1+math.sqrt(max(0,1-sigma*x*x))))
            v=sigma*x*x
            if v>cubic_cap:
                phi_b=cubic_cap/(2*(1+math.sqrt(1-cubic_cap)))
                val=(phi_b+(v-cubic_cap)/(4*math.sqrt(1-cubic_cap)))/x''',
        'rec=dict(K=K,degree=deg,shape=shape,triple=triple,sigma=sigma,D=D.X':
            'rec=dict(cubic_cap_envelope=True,certified=False,K=K,degree=deg,shape=shape,triple=triple,sigma=sigma,D=D.X',
        "if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]))":
            "if __name__=='__main__':run(64,10,.1,0,2/3)",
    }
    for old, new in substitutions.items():
        assert source.count(old) == 1, old
        source = source.replace(old, new)
    exec(compile(source, 'e95_convex_cubic_cap_port', 'exec'), {'__name__': '__main__'})


if __name__ == '__main__':
    main()
