"""Read a completed Lean AxiomCheck transcript; this does not check proofs."""
from pathlib import Path
import collections,json,re,sys
root=Path(__file__).resolve().parents[3]
logpath=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('final_axioms.log')
s=logpath.read_text()
expected=len(re.findall(r'^#print axioms\s+', (root/'lean/AxiomCheck.lean').read_text(), re.M))
rows=re.findall(r"^'([^\n]+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",s,re.M)
allowed={'propext','Classical.choice','Quot.sound'}
bad=[]
for name,raw in rows:
 axioms={a.strip() for a in raw.split(',') if a.strip()}
 if axioms-allowed:bad.append({'name':name,'unexpected':sorted(axioms-allowed)})
summary={'expected_axiom_commands':expected,'printed_axiom_entries':len(rows),'unexpected_axioms':bad,'sorryAx_present':'sorryAx' in s,'lean_error_present':bool(re.search(r'(^|\n).*error:',s))}
print(json.dumps(summary,indent=2))
logpath.with_suffix('.summary.json').write_text(json.dumps(summary,indent=2)+'\n')
if len(rows)!=expected or bad or summary['sorryAx_present'] or summary['lean_error_present']:sys.exit(1)
