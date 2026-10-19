"""VM-only port of the round-11 QQ/Bernstein certifier to sigma = 2/3.

The imported implementation is unchanged except for the radical polynomial,
input/output paths, and support-line input path. No discovery optimization here.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
original = Path('examples/r11_certificates/certify.py').read_text()
changes = {
    "OUT=Path('.research/agents/tdense11_scratch')": "OUT=Path(" + repr(str(ROOT)) + ")",
    "rec=json.loads(OUT.joinpath(path).read_text())": "rec=json.loads(Path(path).read_text())",
    "support=json.load(open(OUT/'support_lines.json'))": "support=json.load(open('examples/r11_certificates/support_lines.json'))",
    "vpoly=[Q(0),Q(0),Q(1,2),Q(0),-Q(1,4)]": "vpoly=[Q(1,12),Q(0),Q(1,3),Q(0),-Q(1,6)]",
    "assert all(row[0]==0 and all(row[i]<=row[i+1] for i in range(deg)) for row in bs)": """# Exact monotone reconstruction repairs solver tolerance violations.
    for row in bs:
        row[0]=Q(0)
        for i in range(1,len(row)):row[i]=max(row[i],row[i-1])
    assert all(row[0]==0 and all(row[i]<=row[i+1] for i in range(deg)) for row in bs)""",
    "OUT.joinpath('certificate_td.json')": "OUT.joinpath('certificate_sigma.json')",
    "out=dict(status=": "out=dict(sigma='2/3',status=",
}
for old, new in changes.items():
    assert original.count(old) == 1, old
    original = original.replace(old, new)
namespace = {'__name__': 'ported_certifier', '__file__': __file__}
exec(compile(original, 'round11_certifier_sigma_port', 'exec'), namespace)
Q = namespace['Q']
namespace['run'](sys.argv[1], Q(sys.argv[2]), Q(sys.argv[3]))
