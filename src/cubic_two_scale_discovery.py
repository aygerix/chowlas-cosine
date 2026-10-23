"""One fixed coupled-cubic discovery LP after a certified generator probe.

K64, degree10, and the existing support-cap envelope are retained.
rho optimizes one dyadic triangular shape. Its parent/child weights
are affine on each halfcell, so both endpoints are constrained.
No optimizer output is itself a certificate.
"""
import json
from pathlib import Path
import socket


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    root = Path('.research/experiments/cubic_two_scale_2026-10-23')
    probe = json.loads((root/'probe.json').read_text())
    assert probe['status'] == 'PASS' and probe['shape_area'] == '1/32'
    source = Path('src/e95_discover_sigma.py').read_text()
    substitutions = {
        "OUT=Path('examples/e95'); OUT.mkdir(exist_ok=True)":
            "OUT=Path('.research/experiments/cubic_two_scale_2026-10-23'); OUT.mkdir(parents=True,exist_ok=True)",
        'model.Params.Threads=4': 'model.Params.Threads=2; model.Params.TimeLimit=100',
        'D=model.addVar(lb=0)':
            '''D=model.addVar(lb=0)
    rho=model.addVar(lb=0,ub=1/24)
    cu=962250449/10**10
    gamma_shape=lambda t:max(0.,1-32*abs(t-7/32))''',
        'cap=np.cos(np.pi/(k+2)) if jj else 1.':
            '''cap=np.cos(np.pi/(k+2)) if jj else 1.
        lower_b,upper_b=0.,2/3
        for _ in range(64):
            middle_b=(lower_b+upper_b)/2
            if middle_b*middle_b*(1-middle_b)<4*cap*cap/27:lower_b=middle_b
            else:upper_b=middle_b
        cubic_cap=upper_b if jj else 2/3
        endpoint_shapes=sorted(set((gamma_shape(tt),gamma_shape(tt/2))
            for tt in (tlo,(jj+1)/(splits*K))))''',
        'val=sigma*x/(2*(1+math.sqrt(max(0,1-sigma*x*x))))':
            '''val=sigma*x/(2*(1+math.sqrt(max(0,1-sigma*x*x))))
            v=sigma*x*x
            if v>cubic_cap:
                phi_b=cubic_cap/(2*(1+math.sqrt(1-cubic_cap)))
                val=(phi_b+(v-cubic_cap)/(4*math.sqrt(1-cubic_cap)))/x''',
        'model.addConstr(expr>=0)':
            '''for parent_shape,child_shape in endpoint_shapes:
                vv=min(v,cubic_cap)
                gv=vv*math.sqrt(1-vv)/4
                correction=.5*child_shape*gv-2*parent_shape*gv*gv/cu
                if v>cubic_cap:
                    gp1=(2-3*vv)/(8*math.sqrt(1-vv))
                    g2p=vv*(2-3*vv)/16
                    correction+=(.5*child_shape*gp1-2*parent_shape*g2p/cu)*(v-vv)
                model.addConstr(expr-rho*correction/x>=0)''',
        'model.setObjective(D,gp.GRB.MINIMIZE)':
            'model.setObjective(D+cu*rho/32,gp.GRB.MINIMIZE)',
        'rec=dict(K=K,degree=deg,shape=shape,triple=triple,sigma=sigma,D=D.X,C=1/D.X':
            "rec=dict(coupled_cubic_dual=True,certified=False,rho=rho.X,c_upper='962250449/10000000000',D_kernel=D.X,offset=cu*rho.X/32,K=K,degree=deg,shape=shape,triple=triple,sigma=sigma,D=D.X+cu*rho.X/32,C=1/(D.X+cu*rho.X/32)",
        "if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]))":
            "if __name__=='__main__':run(64,10,.1,0,2/3)",
    }
    for old, new in substitutions.items():
        assert source.count(old) == 1, old
        source = source.replace(old, new)
    exec(compile(source, 'coupled_cubic_discovery_port', 'exec'), {'__name__': '__main__'})


if __name__ == '__main__':
    main()
