"""Final exact local-variation and benchmark checks. VM only, dirun.sh -c 2."""
import json
from fractions import Fraction as F
from pathlib import Path

OUT=Path('.research/agents/tdense2_scratch')


def main():
    rows=json.load(open(OUT/'benchmarks_summary.json'))
    for row in rows:
        v=F(row['filter']['V'])
        w=F(row['filter']['W'])
        assert v>=F(row['n'],10)
        assert w<=0 or w*w<=4*v**3
    tested=0
    # Exhaustive check of the new unweighted front-energy inequality, with the
    # even extension and its origin boundary. No profile assumptions needed.
    for X in range(1,11):
        for mask in range(1<<X):
            a={j+1 for j in range(X) if (mask>>j)&1}
            av=lambda j:int(abs(j) in a)
            for q in range(1,min(X,3)+1):
                for r in range(1,q+1):
                    d=[sum(av(i) for i in range(j+1,j+q+1)) for j in range(X-q+1)]
                    for w in range(X-q+1):
                        lhs=sum(F(2*av(j)-av(j-q)-av(j+q),2)**2 for j in range(1,w+1))
                        rhs=q+2*sum(abs(r-v) for v in d[:w+1])
                        assert lhs<=rhs
                        tested+=1
    result=dict(status='EXACT final checks PASS',benchmark_LM_eta='1/10',
        benchmark_LM_B=2,benchmark_sets_checked=len(rows),
        exhaustive_local_front_checks=tested,local_max_X=10,local_max_q=3,
        reason='Does not prove the asymptotic theorems; checks the finite claims and an algebraic normalization.')
    (OUT/'final_checks.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
