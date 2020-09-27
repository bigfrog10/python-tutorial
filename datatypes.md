# basic data types

## integer (int)
integers are positive or negative whole numbers with no decimal point and have no size limit. 

the most basic operators are addition, subtraction, multiplication and the use
of parentheses:  
```x + 2``` for addition  
```x + 2``` for subtraction  
```x + 2``` for multiplication  
```x + 2``` for parentheses  

division is different, as with integers. playing '/' division could result in 
non-integer solutions. as a result, '%' is used to find the remainder of a 
variable and '//' is used for floor division. for exponentiation, '**' is used 
instead of '^'. unary operator like '+' or '-' works on single numbers for 
example, ```--3 = 3```. 
```
x % 2
x // 2
x ** 2
```

attaching an equal sign behind the previous operators, for example,  
```x += 3``` is a more convenient way to write ```x = x + 3```.
these are called python assignment operators. 

to compare two values, comparison operators are used. 
```
x == y
x != y
x > y, x < y
x >= y, x <= y
```

python's logical operators are used to combine conditional statements.  
```and```: returns True if both surrounding statements are True  
```or```: returns True if one of the statements is true  
```not```: returns the opposite of the statement, returns True if False  

identity operators compare whether two objects are the same object, not just 
equal.  
```is```: returns True if both unknowns are the same object, and ```is not``` 
returns True if they are not the same object. 

the int() cast function converts the value inside to a normal integer. 

references:  
[math module example](src/beginning_python/chapter3.py)  
[24 sum problem](src/problems/24game.py)  
[integer factors with comprehension](src/problems/integer_factors.py)  
[fibonacci sequence](src/puzzles/fibonacci.py)  


## float
floats represent real numbers that are written with a decimal point to divide
the integer and fractional parts. 

the float() cast function converts the value inside into a number with type 'float'. 
the value inside can be an integer or a string. 

the '/' operator works as a division operator that will return a float number. 

the smallest positive float number can be achieved through importing numpy and
using the nextafter() function:
``` 
import numpy as np

np.nextafter(0, 1)
4.9406564584124654e-324
```
this is also the machine epsilon

IEEE  754 64 bit numbers are split into 3 components, the sign of mantissa, the biased 
exponent, and the normalised mantissa. 
![double precision](double_precision_float.jpg) 

source:
https://stackoverflow.com/questions/38477908/smallest-positive-float64-number

for the four basic operators, it is guaranteed the rounding error is on the last
digit. for other function computation, there is not always a guarantee. 

keisan casio online calculator:
https://keisan.casio.com/menu/system/000000000760
this online calculator always guarantees the rounding error on the last digit
but is slower than other routines. 

significant figures:
1. all non-zero digits are significant
2. zeros that appear between two significant digits are significant 
3. zeros to the left of significant digits are not significant
4. zeros to the right of significant figures are only significant if they are to
 the right of the decimal point. this is because they are only necessary to 
 indicate precision. 
 
significant figure rounding:
1. identify the significant figures prior to rounding
2. if the digit to the immediate right of the last significant figure is at
least a five, add 1 to the last significant figure. 
3. if the digit to the immediate right of the last significant figure is a 5
not followed by another digit, or only followed by 0: round half away from zero
or round to nearest even number
4. replace non significant figures in front of the decimal point by zeros
5. drop all the digits after the decimal point to the right of the significant
figures. 

## string
strings are python arrays that represent unicode characters. they can be 
represented by using either single quotes or triple quotes. by using triple
quotes, you can create a multiline string. to access certain elements of a 
string, you can use square brackets:
```
x = 'hello, world!'
print(a[1])
```

you can return a certain range of characters by using slicing and dicing. 
```
x = 'hello, world!'
print(a[2:7])
```

if the length of the string is too long, you can count from the end of the
string, using a negative index:
```
x = 'hello, world!'
print(a[-2])
```

the len() function returns the length of a string:
```
x = 'hello, world!'
print(len(a))
```

the lower() and upper() methods returns the string in all lower/upper case
respectively:
```
x = 'hello, world!'
print(a.lower())
print(a.upper())
```

the split() method splits the string into substrings given the separator:
```
a = "hello, world!"
print(a.split(","))
```

the replace() method replaces a string with another string:
``` 
a = "hello, world!"
print(a.replace("h", "j"))
```

you can use the keywords "in" or "not in" to check whether a certain phrase or
character is in a string

to combine two strings you can use the '+' or '*' operator  
``` 
print('hello, ' + 'world')
print('hello ' * 80)
```

the str() cast method converts the target into a string.

python 3 by default uses unicode instead of ascii. 
``` 
你好 = 1
print(你好)  # prints 1

print(ascii("π"))  # prints '\u03c0'
``` 

the recommended string format way:
```
s1 = 'hello'
s2 = 'man'
print(f's1 = {s1}, s2 = {s2}')
```
the benefit to this format is not needing to pass in variables like in string's
format() 

references:  
[matching words ratio/percentage](src/problems/matching.py)  
[matching words string](src/problems/logic.py)  
[numerals english name](src/puzzles/numerals_english.py) 

## boolean
the boolean datatype is either True or False. True and False are keywords, so 
they are to be written with uppercase first letters.

the most common boolean operators are the following:
``` 
or
and
not
==
!=
```
you can combine ```and```, ```or```, and ```not``` with parentheses to make
compound expressions. 

the bool() function evaluates the value inside, returning either True or False.

most values are true with few exceptions. any string is True, except for empty
strings. any number is True, except for 0. any list, tuple, set, and dictionary
are True, except for empty ones. 

references:  
[logic](src/problems/logic.py)  
[logic gates](src/problems/logic_gates.py)  
[nor gates](src/problems/nor_gate_origin.py) 
