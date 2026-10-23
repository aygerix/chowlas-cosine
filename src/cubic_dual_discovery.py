"""One fixed P66 convex-dual discovery LP, not a mathematical certificate.

Port the existing E95 LP without changing its legacy source. Add the
valid dual objective phi(v)+eta*cos(9.1*t)*v*sqrt(1-v)/4 before
Gabor-Jensen. eta is optimized in[0,1/2]. Fixed K64,degree10.
No parameter sweep, no GPU, shared Dirichlet only.
"""
from pathlib import Path
import socket


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    source = Path('src/e95_discover_sigma.py').read_text()
    substitutions = {
        "OUT=Path('examples/e95'); OUT.mkdir(exist_ok=True)":
            "OUT=Path('.research/experiments/cubic_dual_2026-10-23'); OUT.mkdir(parents=True,exist_ok=True)",
        'model.Params.Threads=4':
            'model.Params.Threads=2; model.Params.TimeLimit=100',
        'D=model.addVar(lb=0)':
            'D=model.addVar(lb=0); eta=model.addVar(lb=0,ub=.5)',
        'j=jj//splits; tlo=jj/(splits*K)':
            '''j=jj//splits; tlo=jj/(splits*K)
        thi=(jj+1)/(splits*K)
        omega=9.1
        # Discovery-only floating envelope. A later exact certificate is mandatory.
        anglelo,anglehi=omega*tlo,omega*thi
        coshi=max(math.cos(anglelo),math.cos(anglehi))
        if math.ceil(anglelo/(2*math.pi))<=math.floor(anglehi/(2*math.pi)):coshi=1.
        coshi=math.nextafter(coshi,math.inf)''',
        'expr=aa[j]-val-gp.quicksum':
            'expr=aa[j]-val-eta*(coshi*sigma*x*math.sqrt(max(0,1-sigma*x*x))/4)-gp.quicksum',
        'rec=dict(K=K,degree=deg,shape=shape,triple=triple,sigma=sigma,D=D.X':
            'rec=dict(eta=eta.X,omega=9.1,certified=False,K=K,degree=deg,shape=shape,triple=triple,sigma=sigma,D=D.X',
        "if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]))":
            "if __name__=='__main__':run(64,10,.1,0,2/3)",
    }
    for old, new in substitutions.items():
        assert source.count(old) == 1, old
        source = source.replace(old, new)
    exec(compile(source, 'e95_convex_cubic_dual_port', 'exec'), {'__name__': '__main__'})


if __name__ == '__main__':
    main()
