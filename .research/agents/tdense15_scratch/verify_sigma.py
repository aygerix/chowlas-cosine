"""VM-only independent reconstruction of the sigma certificate and all inputs."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent
source=Path('examples/r11_certificates/independent_verify.py').read_text()
changes={
    "OUT=Path('.research/agents/tdense11_scratch')": "OUT=Path("+repr(str(ROOT))+")",
    "OUT.joinpath('certificate_td.json')": "OUT.joinpath('certificate_sigma.json')",
    "OUT/'certificate_td.json'": "OUT/'certificate_sigma.json'",
    "support=json.load(open(OUT/'support_lines.json'))": "support=json.load(open('examples/r11_certificates/support_lines.json'))",
    "P=sp.Poly(u*u*(2-u*u)/4,u,domain=sp.QQ)-A*A": "P=sp.Poly((1-sp.Rational(2,3)*(1-u*u)**2)/4,u,domain=sp.QQ)-A*A",
    "assert D==R(259,2000) and 1/D>R(77,10)": "assert c['sigma']=='2/3' and D==R(73,1000) and 1/D>R(1369,100)",
    "OUT.joinpath('independent_verification.json')": "OUT.joinpath('sigma_independent.json')",
}
for old,new in changes.items():
    assert source.count(old)==1,old
    source=source.replace(old,new)
ns={'__name__':'sigma_independent','__file__':__file__}
exec(compile(source,'round11_independent_sigma_port','exec'),ns)
ns['verify']()
