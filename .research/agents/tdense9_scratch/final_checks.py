"""Final sequential VM checks and reproducibility manifest."""
import runpy,json,hashlib,platform,sys
from pathlib import Path
OUT=Path('.research/agents/tdense9_scratch')
runpy.run_path(str(OUT/'long_verify.py'),run_name='__main__')
runpy.run_path(str(OUT/'packet_probe.py'),run_name='__main__')
import numpy,sympy,flint,gurobipy
records=[]
for p in sorted(OUT.iterdir()):
    if not p.is_file() or p.name=='manifest.json':continue
    if p.suffix=='.py':compile(p.read_text(),str(p),'exec')
    records.append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
rec=dict(status='source compiled, exact checks and numerical probe completed',python=platform.python_version(),numpy=numpy.__version__,sympy=sympy.__version__,flint=flint.__version__,gurobi=gurobipy.gurobi.version(),VM='34.148.157.169',max_cores=2,seed=2026101909,files=records)
(OUT/'manifest.json').write_text(json.dumps(rec,indent=2));print('MANIFEST',len(records),'files',flush=True)
