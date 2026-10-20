"""VM-only artifact manifest and source compilation, no mathematical search."""
import hashlib,json,platform,py_compile
from pathlib import Path
import gurobipy,numpy,sympy
OUT=Path('.research/agents/tdense8_scratch')
records=[]
for p in sorted(OUT.glob('*.py')):
    py_compile.compile(str(p),doraise=True)
for p in sorted(OUT.glob('*')):
    if p.is_file() and p.name!='manifest.json':
        records.append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
report=Path('.research/agents/tdense8_report.md')
records.append(dict(path=str(report),bytes=report.stat().st_size,sha256=hashlib.sha256(report.read_bytes()).hexdigest()))
rec=dict(python=platform.python_version(),gurobi=list(gurobipy.gurobi.version()),numpy=numpy.__version__,
         sympy=sympy.__version__,sources_compiled=True,files=records)
OUT.joinpath('manifest.json').write_text(json.dumps(rec,indent=2))
print(json.dumps({k:v for k,v in rec.items() if k!='files'}),flush=True)
