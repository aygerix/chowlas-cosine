"""Sequential VM batch; failures are reported and independent checks continue."""
import sys,runpy,traceback
from pathlib import Path
sys.path.insert(0,str(Path('.research/agents/tdense9_scratch').resolve()))
from cp_obstruction import run as cp
from exact_witness import run as witness
for name,fun in [('CP',cp),('independent',lambda:runpy.run_path('.research/agents/tdense9_scratch/independent_verify.py',run_name='__main__')),('factor_witness',lambda:witness(160,'full','factor')),('long_gram',lambda:runpy.run_path('.research/agents/tdense9_scratch/long_gram.py',run_name='__main__'))]:
    print('START',name,flush=True)
    try:fun()
    except Exception:traceback.print_exc()
    print('END',name,flush=True)
