# Python basic number types: int, float, complex
print(7)
print(type(7))  # <class 'int'>
print(isinstance(7, int))  # True
print(3.1415925)  # pi
print(type(3.1415925))  # <class 'float'>
print(1.0 + 2.0j)  # Python uses j instead of i in complex numbers
print(type(1.0 + 2.0j))  # <class 'complex'>


# arithmetic operations, +, -, *, /, **, ()
print(1 + 2 * 3)  # multiplication proceeds addition
print((1 + 2) / 3)  # result is float, not int anymore
print(4 // 2)  # this is int division
print(5 % 2)  # remainder

print(1/3)  # keep only 16 significant digits

print(2/3)  # the last digit is 6, not 7, seems we truncate not round result.
print(5/3)  # this time we round not truncate!

print(8.0 // 0.4)  # 19.0, ouch! not 20.0. Don't // with float
# https://stackoverflow.com/questions/38588815/rounding-errors-in-python-floor-division

# display value != machine true value != true value
# https://docs.python.org/3.8/tutorial/floatingpoint.html
# https://matthew-brett.github.io/teaching/floating_error.html
# https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
# https://www.unioviedo.es/compnum/labs/PYTHON/Finite_arithmetic.html
# https://www.juliensobczak.com/inspect/2019/03/10/floating-point-numbers-demystified.html
# https://www.soa.org/news-and-publications/newsletters/compact/2014/may/com-2014-iss51/losing-my-precision-tips-for-handling-tricky-floating-point-arithmetic/
# file:///D:/3dev/deep_learning/FloatingPoint.Handout.pdf
print(0.1)  # 0.1
print(0.2)  # 0.2
print(0.1 + 0.2)  # 0.30000000000000004, error at 16th digit
print(1.2 - 1.0)  # 0.19999999999999996, seems that ulp = 0.00...004

# assign value to variable, name=[_a-zA-Z]+[_0-9a-zA-Z]*
# _ is a special variable
# check equal
d = 10000.0 / 3.0
d = d * 3
print(d)  # 10000.0
a = b = 1
print(a)
print(b)
a, b = 1, 2
print(a)
print(b)


print(2.71828 ** 3.14159j)  # Euler's identity, e ^ (i * pi) = -1

print(10 ** 100)  # huge number

print(2.2 + 3)  # upcasting/type conversion, convert int 3 to float 3 first.

# downcasting is tricky
print(int(3.14))  # int = floor, toward 0
print(int(2.718))
print(int(-3.14))
print(int(-2.718))

# assign values to variables: reuse same value, no duplicates.
a = 3  # int
b = 2.5  # float
print(a + b)  # float 5.5

# comparison, float is ordered(complex is not ordered)
print(2 > 1)  #
c = 3
print(a == c)  # value comparison
print(a is c)  # constant 3 is cached - identity comparison
print(a is 3)  # True too.
print(0.1 + 0.2 == 0.3)  # False due to roundings

# int is unbound, not restricted by hardware limit, 32-bit or 64 bit.
# In contrast, Java and other languages are bounded to hardware architecture.
# They use separate classes to deal with this limit with slower performance,
# such as BigInteger/etc. Python still is restricted by the available hardware
# memory size and become slower when dealing with very large numbers.
print(9223372036854775808)  # 2^63

# The main reason we care about the number limits is to prevent errors,
# overflow and underflow, when performing arithmetic operations. Since int is
# unbound, we don't have these issues. On the other hand, float is bounded.

# real number is continuous, but binary representation is discrete. So there
# are "gaps" where real number can't be represented by binaries exactly. The
# difference is called rounding error.
print(2 / 3)  # round at the end

# Python, and many other languages use IEEE 754 standard to represent float
#    sign | exponent | mantissa
#    1 bit  11 bits    52 bits
# This is the 64-bit design, there is a 32-bit version too. This corresponds
# to 16 digits in base 10.
# An observation is when exponent is 0, the mantissa's gaps are the smallest.
# When the exponent gets larger, the gaps are getting larger too. The numbers
# in a gap will be rounded to the boundary as representation. The difference is
# the representation error.
# https://docs.python.org/3.0/tutorial/floatingpoint.html

# modules are reusable code. Every language has some built-in modules and
# 3rd party extended modules.
# hardware information, check 32 bit or 64 bit
import platform
print(platform.architecture())  # 64 bit in my case

# to check float max/min/machine precision/epsilon
import sys
print(sys.float_info)

print(10000000  + 0.00000001)  # fine, 10000000.00000001
print(100000000 + 0.000000001)  # not fine, 100000000.0

# Python 3.9 has a new function in math that can tell the gap of numbers.
# Note that the gap is getting larger as the number is larger.
# math.ulp(x) and math.nextafter(x, x+1)

# When we carry arithmetic operations (+, -, *, /) on the representations of
# numbers, we need to make sure the representation errors stay bounded with
# representation error of the real result. IEEE 754 standard requires this and
# more.

print('{:,}'.format(1000000000000))  # add comma every 3 digit, in finance.

# more numbers
print(0b10)  # binary number
print("{0:010b}".format(0b011110))
print("{0:010f}".format(0b011110))
print(0o10)  # octal number
print(0xA)  # hex number

# https://docs.python.org/3/library/decimal.html
import decimal
print(1 / decimal.Decimal(7))  # default precision is 28 digit: 0.1428571428571428571428571429
decimal.getcontext().prec = 16  # set precision to 16
print(1 / decimal.Decimal(7))  # 0.1428571428571429

# Rational numbers
import fractions
print(fractions.Fraction(3.1415))
print(fractions.Fraction(355, 113))
print(fractions.Fraction(1, 2) + fractions.Fraction(1, 3))

# math functions
import math
print(math.pi)
print(math.sqrt(5))
print(math.sin(3.14))  # near zero
print(math.log10(11))
print(math.factorial(5))
print(math.ceil(3.14))  # 4
print(math.floor(2.718))  # 2


# bit representation for integers and 2's compliments:
# Among many ways to use bits(0 and 1) to represent integers, 1's and 2's
# compliments are common ones. 2's compliment is chosen for easier
# implementations of addition, subtraction, and multiplication:
# https://en.wikipedia.org/wiki/Two's_complement
# hardware implementation is simpler too, using less components

# for positive numbers, use all the bits except the most significant bit
# (MSB, left most bit).
# to represent a negative number, take the positive number, invert all bits
# (0 to 1 and 1 to 0) and then add 1.
