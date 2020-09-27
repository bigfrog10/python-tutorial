template = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(template % values)

from string import Template
tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(what="Dusty", who="Mars"))

print("{}, {} and {}".format("first", "second", "third"))
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))

from math import pi
print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))

from math import e
print(f"Euler's constant is roughly {e}.")
# "Euler's constant is roughly {e}.".format(e=e)

import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))

# the three flags(s, r, and a) result in conversion using str, repr, and ascii, respectively
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))
print(eval(repr(pi)))
print(str(pi))
print(ascii(pi))
print(ascii("π"))

# string formatting
header_fmt = '{{:{}}}{{:>{}}}'.format(15, 20)
print(header_fmt)