"""Small exact rational intervals for saved finite root certificates.

No outward floating rounding is needed: every endpoint operation uses
fractions.Fraction. This is ordinary exact computation, not Lean.
"""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction

    def __init__(self, lo=0, hi=None):
        object.__setattr__(self,'lo',Fraction(lo))
        object.__setattr__(self,'hi',Fraction(lo if hi is None else hi))
        assert self.lo<=self.hi

    @staticmethod
    def cast(value):
        return value if isinstance(value,I) else I(value)

    def __add__(self,other):
        other=I.cast(other)
        return I(self.lo+other.lo,self.hi+other.hi)

    __radd__=__add__

    def __neg__(self):
        return I(-self.hi,-self.lo)

    def __sub__(self,other):
        return self+-I.cast(other)

    def __rsub__(self,other):
        return I.cast(other)+-self

    def __mul__(self,other):
        other=I.cast(other)
        values=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(values),max(values))

    __rmul__=__mul__

    def __truediv__(self,other):
        other=I.cast(other)
        assert other.hi<0 or other.lo>0
        return self*I(1/other.hi,1/other.lo)

    def __rtruediv__(self,other):
        return I.cast(other)/self

    def __pow__(self,power):
        assert isinstance(power,int) and power>=0
        value=I(1)
        for _ in range(power):
            value=value*self
        return value

    def magnitude(self):
        return max(abs(self.lo),abs(self.hi))

    def serial(self):
        return [str(self.lo),str(self.hi)]
