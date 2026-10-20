"""Sequential VM-only verification batch; maximum two threads inherited from dirun."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path('.research/agents/tdense9_scratch').resolve()))
from exact_witness import run as witness
from cp_obstruction import run as cp
witness(160,'full')
cp()
import runpy
runpy.run_path('.research/agents/tdense9_scratch/independent_verify.py',run_name='__main__')
