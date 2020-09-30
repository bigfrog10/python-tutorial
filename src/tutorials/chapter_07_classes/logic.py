# https://en.wikipedia.org/wiki/Truth_table
# https://www.cs.cmu.edu/~emc/15414-f12/lecture/propositional_logic.pdf
# p	q	p ∨ q   p ⇒→ q  p ↔ q   p ⊕ q
# T	T	  T       T       T       F
# T	F	  T       F       F       T
# F	T	  T       T       F       T
# F	F	  F       T       T       F


class Proposition:
    def __init__(self, value: bool):
        self.value = value

    def __add__(self, other: 'Proposition'):
        return self.value or other.value

    def __mul__(self, other: 'Proposition'):
        return self.value and other.value

    def __neg__(self):
        return not self.value

    def __gt__(self, other: 'Proposition'):
        if self.value:
            return other.value
        else:
            return not self.value
        # equivalent to not p or q

    def __xor__(self, other: 'Proposition'):
        if self.value:
            return not other.value
        else:
            return other.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return 'Proposition({})'.format(self.value)

    def __eq__(self, other: 'Proposition'):
        return self.value == other.value


PT = Proposition(True)
PF = Proposition(False)

print(PT)
print(str(repr(PT)))
print(eval(repr(PT)))
print(eval("1+2"))
print(PT is eval(repr(PT)))
print(PT == eval(repr(PT)))