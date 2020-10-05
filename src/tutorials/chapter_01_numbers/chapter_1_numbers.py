# #############################################################################
# Section 1. Integers
# #############################################################################
print(2020)

# arithmetic operations, +, -, *, /, **, ()
print(1 + 2 * 3)  # multiplication proceeds addition
print((1 + 2) / 3)  # result is a real number(float), not int anymore
print(4 // 2)  # this is int division
print(5 % 2)  # remainder

print(5 ** 2)  # exponential

# comparison
print(2 > 1)
print(2 < 1)
print(2 == 1)  # Since = is used for assignment, we use == for comparison

# assign values to variables: reuse same value, no duplicates.
# variable name: [_a-zA-Z]+[_0-9a-zA-Z]*
# _ and __ are a special variable prefix - scope
c = 3
a = 3
print(a == c)  # value comparison.

a = b = 1
print(a)
print(b)

a, b = 1, 2
print(a)
print(b)

# swap
a, b = b, a
print(a)
print(b)

# hard way - integer swap with temp variables
x, y = 3, 5
x = x + y  # so now x is sum(x, y)
y = x - y  # sum - old y = x, so y has x now
x = x - y  # sum - y = sum - old x = old y
print(x)
print(y)

# int is unbound, not restricted by hardware limit, 32-bit or 64 bit.

print(9223372036854775808)  # 2^63
# huge number, if you do this in a calculator, you get overflow.
print(10 ** 100)

# #############################################################################
# Section 2. Real (Float) and Complex Numbers
# #############################################################################
print(3.1415925)  # pi

print(1/3)  # keep only 16 significant digits
print(2/3)  # the last digit is 6, not 7, seems we truncate not round result.
print(5/3)  # this time we round not truncate!

print(8.0 / 4.0)
print(8.0 // 4.0)  # 19.0, ouch! not 20.0. Don't do // with float

print(0.1)  # 0.1
print(0.2)  # 0.2
print(0.1 + 0.2)  # 0.30000000000000004, error at 16th digit
print(1.2 - 1.0)  # 0.19999999999999996, seems that ulp = 0.00...004

# check equal
d = 10000.0 / 3.0
d = d * 3
print(d)  # 10000.0

print(2.2 + 3)  # upcasting/type conversion, convert int 3 to float 3 first.

print(0.1 + 0.2 == 0.3)  # False due to roundings

a = 3  # int
b = 2.5  # float
print(a + b)  # float 5.5

# overflow
print(10000000 + 0.00000001)  # fine, 10000000.00000001
print(100000000 + 0.000000001)  # not fine, 100000000.0

# downcasting is tricky
print(int(3.14))  # int = floor, toward 0
print(int(2.718))
print(int(-3.14))
print(int(-2.718))

# complex numbers
print(1.0 + 2.0j)  # Python uses j instead of i in complex numbers
# all arithmetic operations apply, to float <op> complex as well
print(2.71828 ** 3.14159j)  # Euler's identity, e ^ (i * pi) = -1

# complex is not ordered, so we can't compare 2 complex numbers.

# #############################################################################
# Section 3. Integer Representation
# #############################################################################
# for positive numbers, use all the bits except the most significant bit
# (MSB, left most bit).
# to represent a negative number, take the positive number, invert all bits
# (0 to 1 and 1 to 0) and then add 1.

# bit operations, &, |, ~, ^, >>, <<
print(3 & 5)  # 1, 101 & 011
print(3 | 5)  # 7
print(~3)     # -4
print(bin(~3))  # binary
print(3 ^ 5)  # 6 = b'110', 1 if exactly one operand is 1 else 0
print(5 >> 1)  # 2, 101 shifts to right -> 010, remove right most 1 from left
print(5 << 1)  # 10, 101 shifts to left -> 1010, append 0 from right

x, y = 3, 5
x = x ^ y  # XOR
y = y ^ x
x = x ^ y
print(x)
print(y)

# #############################################################################
# Section 4. Real Number(float) Representation
# #############################################################################
# Python, and many other languages use IEEE 754 standard to represent float
#    sign | exponent | mantissa
#    1 bit  11 bits    52 bits
# 1 <= mantissa < 10
# It's base-2 scientific notation.
# try out: http://evanw.github.io/float-toy/

# modules are reusable code. Every language has some built-in modules and
# 3rd party extended modules. The standard libraries, or built-in modules, are
# in here: https://docs.python.org/3/library/.
import math
print(math.frexp(123.456))  # (0.9645, 7) -> (m, e) such that x = m * 2 ** e
print(math.ldexp(0.9645, 7))  # back to 123.456

print(math.frexp(math.inf))  # (inf, 0), not the same as (1024, 0)
print(math.frexp(float('inf')))
print(math.frexp(float('nan')))
print(math.frexp(math.nan))

print(math.ldexp(1, 1023))
# print(math.ldexp(1, 1024))  # overflow

# hardware information, check 32 bit or 64 bit
import platform
print(platform.architecture())  # 64 bit

# to check float max/min/machine precision/epsilon
import sys
print(sys.float_info)

# Python 3.9 has a new function in math that can tell the gap of numbers.
# Note that the gap is getting larger as the number is larger.
# math.ulp(x) and math.nextafter(x, x+1)

# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex
import struct


def float2bins(f):
    [d] = struct.unpack(">Q", struct.pack(">d", f))
    return f'{d:064b}'


def bins2float(b):
    h = int(b, 2).to_bytes(8, byteorder="big")
    return struct.unpack('>d', h)[0]


print(float2bins(3.14))
print(bins2float('0100000000001001000111101011100001010001111010111000010100011111'))

# special values and ranges:
#  NaN: 0111111111111000000000000000000000000000000000000000000000000000
# -Inf: 1111111111110000000000000000000000000000000000000000000000000000
# +Inf: 0111111111110000000000000000000000000000000000000000000000000000
# -Max: 1111111111101111111111111111111111111111111111111111111111111111
# +Max: 0111111111101111111111111111111111111111111111111111111111111111

# https://www.ardanlabs.com/blog/2013/08/gustavos-ieee-754-brain-teaser.html

# arithmetic operation errors

# #############################################################################
# Section 5. Data Types
# #############################################################################
# In order to interpret a bit array, we need a hint - data type.
# Python basic number types: int, float, complex
print(type(7))  # <class 'int'>
print(isinstance(7, int))  # True

print(type(3.1415925))  # <class 'float'>
print(type(1.0 + 2.0j))  # <class 'complex'>

# We may define our own data types.
c = 3
print(a == c)  # value comparison
print(a is c)  # constant 3 is cached - identity comparison
print(a is 3)  # True too.

# #############################################################################
# Section 6. Other Number formats
# #############################################################################
# We have base 2, base 8, and base 16 integers
print(0b10)  # binary number
print("{0:010b}".format(0b011110))
print("{0:010f}".format(0b011110))
print(0o10)  # octal number
print(0xA)  # hex number
print(bin(314))  # convert it to binary

# To deal with arbitrary precision
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
print(math.pi)
print(math.sqrt(5))
print(math.sin(3.14))  # near zero
print(math.log10(11))
print(math.factorial(5))
print(math.ceil(3.14))  # 4
print(math.floor(2.718))  # 2

# cmath module is for complex numbers
