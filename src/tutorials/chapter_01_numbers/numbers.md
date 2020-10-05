### Numbers

In high school, we use this for number crunching:

![TI-84 Plus](it-84_plus.jpg)

It has a 10-digit panel(base-10) with operators and functions. Internally 
it uses base-2 numbers.

#### Bit World
Modern computers use base-2 representation with 2 states 0 and 1. 
Historic computers use base-10. 
- https://web.csulb.edu/~cwallis/labs/computability/index.html
- https://www.thoughtco.com/history-of-calculators-1991652
- https://en.wikipedia.org/wiki/Mechanical_calculator
- https://en.wikipedia.org/wiki/Abacus

We call single base-2 digit "bit", for short. Bits have a long history:
- https://en.wikipedia.org/wiki/Binary_number

With only 2 states to manage, we map these 2 states to electronic
waves and carry arithmetic and other operations much faster than before.
(Mapping 10 states is much harder, if possible)
- https://en.wikipedia.org/wiki/Digital_signal
- https://www.electronics-tutorials.ws/binary/bin_1.html

Quantum computing has a new way to represent bits, qubits. Ignoring its
complexity, it's another way to represent bits. The new way can carry
operations on these bits much fast than the current electronic way.

So computers live in the bit world, however bits are implemented.


#### Integers in the Bit World
We choose 2's complement representation over 1's complement and signed number
representation for several reasons:
- It's easier to implement addition, subtraction, and multiplication. 
- Hardware implementation is simpler too, using fewer components/gates.
- ...

How to do arithmetic operations in 2's compliment:
- https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html
- https://en.wikipedia.org/wiki/Two%27s_complement

Computers nowadays have 64 bits. So the range of numbers 2's compliment
can represent is limited, 2^63 - 1 to - 2^63. However, Python extends 
integers to arbitrary precision (bounded by hardware memory)

- https://rushter.com/blog/python-integer-implementation/
- https://stackoverflow.com/questions/61493053/how-come-python-3-has-no-size-limit-on-numbers-when-all-other-languages-do
- https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic
- https://en.wikipedia.org/wiki/List_of_C%2B%2B_multiple_precision_arithmetic_libraries

The extra work for arbitrary precision poses a bit slowdown in performance.
 
In contrast, C, Java and other languages don't have this extra, and they are
bounded to hardware architecture/OS. So they are a bit faster. They use 
separate classes to deal with this limit, with slower performance,
such as BigInteger/etc.

The main reason we care about the number limits is to prevent errors,
overflow and underflow, when performing arithmetic operations. Since int is
unbound, we don't have these issues. On the other hand, float is bounded and
has overflow and underflow that we have to deal with. So int is a perfect
world, with the price of a bit slowdown.

#### Real Numbers in the Bit World
Python, and many other languages use IEEE 754 standard to represent real
numbers for 64-bit computers (2-based scientific notation)

| sign  | exponent | mantissa |  
|-------|----------|----------|
| 1 bit | 11 bits  | 52 bits  |

(mantissa is also called significand) This is equivalent to 16 digits in 
base-10. 

- https://en.wikipedia.org/wiki/IEEE_754
- https://www.doc.ic.ac.uk/~eedwards/compsys/float/
- https://docs.python.org/3.0/tutorial/floatingpoint.html
- https://en.wikipedia.org/wiki/Floating-point_arithmetic

The period floats because of the exponent since we want to keep mantissa 
within 1 <= m < 10, such as 3.14, 31.4 = 3.14 X 10 = 3.925 X 8. This is
why we call this representation as floating-point. 

https://chortle.ccsu.edu/AssemblyTutorial/Chapter-30/ass30_2.html

So I guess we should restore the name back to "real", since float-point is just
a way to represent real numbers. We use int above and complex below, so float
in the middle is kind of odd.

We use fixed point in abacus.

If 1 <= m < 10, we call it normalized. If it's < 1, we call it subnormal
(Before IEEE-754-2008, this is called denormalized). This indicates we have
an underflow. https://en.wikipedia.org/wiki/Denormal_number

Due to hardware restriction, we have only finite numbers of bits. So
binary representation is discrete. However, real number is continuous.
So there are "gaps" in the binary representation. Some real numbers
can't be represented by binaries exactly, and they are approximated by
nearby binaries. The difference is called rounding error.

https://stackoverflow.com/questions/38588815/rounding-errors-in-python-floor-division

An observation is when exponent is 0, the mantissa's gaps are the smallest.
When the exponent gets larger, the gaps are getting larger too. The numbers
in a gap will be rounded to the boundary as representation. 

display value != machine true value != true value

When we carry arithmetic operations (+, -, *, /) on the representations of
numbers, we need to make sure the representation errors stay bounded with
representation error of the real result. IEEE 754 standard requires this and
more.

- https://matthew-brett.github.io/teaching/floating_error.html
- https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
- https://www.unioviedo.es/compnum/labs/PYTHON/Finite_arithmetic.html
- https://www.juliensobczak.com/inspect/2019/03/10/floating-point-numbers-demystified.html
- https://www.soa.org/news-and-publications/newsletters/compact/2014/may/com-2014-iss51/losing-my-precision-tips-for-handling-tricky-floating-point-arithmetic/

We have to be careful about the error propagation when performing arithmetic 
operations. Subtracting or dividing 2 close numbers could lose precision.
In these cases, we either transform the calculations or increase precision.

This is why a lot of special functions used in practice need to be carefully
crafted. One of the best site is:

- https://keisan.casio.com/menu/system/000000000760
