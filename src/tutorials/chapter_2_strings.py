# string is immutable, unicode
print('hello, world')
print("hello, world")
print('''hello
world
''')  # 3 lines as it is
print("""hello
world
""")
print("你好，世界")

# unicode variable name
你好 = 1024
print(你好)

Σ = 1.618
print(Σ)

# https://pythonforundergradengineers.com/unicode-characters-in-python.html
print('\u03B1 \u03B4 \u03B5')  # greek letters: α δ ε

# unicode represents characters. it can be encoded into charset.
print('\u03B5')  # this is unicode
print(len('\u03B5'))  # 1, just one unicode character
print('\u03B5'.encode('utf-8'))  # b'\xce\xb5', encode unicode to byte string, 2 bytes
print(len(b'\xce\xb5'))  # 2 bytes
print(b'\xce\xb5'.decode('utf-8'))  # ε, decode byte array to unicode

# utf-8 is a variable length charset
print(len('a'.encode('utf-8')))  # 1 byte, for English
print(len('ε'.encode('utf-8')))  # 2 bytes, for Europe
print(len('好'.encode('utf-8')))  # use 3 bytes to store the char in utf-8, Chinese

print(type(b'abc'))  # <class 'bytes'>
print(type(u'abc'))  # <class 'str'>

# another encoding: don't use latin-1 since it can't fit in
print('\u03B5'.encode('cp936'))  # b'\xa6\xc5'

import sys, locale
print(sys.getdefaultencoding())  # utf-8
print(locale.getpreferredencoding())  # cp936
print(sys.stdout.encoding)  # utf-8

print(help(locale.getpreferredencoding))  # print the doc for this method

# escapes
print('hello,\tworl\'d!\nEnd\\')  # tab, ' inside, new line
print(r'Raw data \t')  # no tab
print(b'abc')  # binary abc, as bytes
print(b'abc'.decode('utf-8'))
print(b'\xc2\xb5'.decode('utf-8'))  # µ

# operations
print('hello' + ', ' + 'world')
print('-' * 80)


# string can be treated as a list with position index
s = 'hello, world'

print(s[2:])  # llo, world, start with position 2 (index starts from 0)
print(s[2:5])  # llo, start included, end excluded
print(s[7])  # w
print(s[-1])  # d, last element.
print(s[::2])  # hlo ol, every other letter, step 2. stride of 2
print(s[::-1])  # reverse order

print(len(s))  #
print(s.index('world'))
print(s.index('o'))  # 4, first index of o
# how to find second index? what about all indices?
print(s.index('o', s.index('o') + 1))  # 8
# may use re module to find all if no special chars: [s.start() for s in re.finditer(':', s)]
# or use a loop/generator

# string format
print('I do not like {} and {}'.format('green eggs', 'ham'))
print('I am {0}. I am {0}. {0}-I-Am'.format('Sam'))  # no duplicates
print('I do not like them {1} or {0}'.format('there', 'here'))  # by position index
print('I do not like them {h} or {t}'.format(t='there', h='here'))  # by keyed index

# f-string is more powerful: https://www.python.org/dev/peps/pep-0498/
there = 'there'
here = 'here'
print(f'I do not like them {here} or {there}')  # use variable names directly
print(f'I do not like them {here!s:20} or {there}')  # 20 or <20, left justified
print(f'I do not like them {here!s:>20} or {there}')  # right justified
print(f'I do not like them {here!s:<20} or {there}')  # left justified
print(f'I do not like them {here!s:^20} or {there}')  # center justified
print(f'I do not like them {here!s:_<20} or {there}')  # fill with _

# number format, can take python expression
print(f'2 + 3 = {2 + 3}')
a = 123.456789
print(f'{a:.3f}')  # 123.457
print(f'{a:.10f}')  # 123.4567890000
print(f'{a:12.3f}')  # 12 - 4 = 8 positions before .

b = 12345
print(f'{b:07}')  # 0012345

c = 520
print(f'{c:x}')  # hex 208
print(f'{c:o}')  # oct
print(f'{c:b}')  # binary
print(f'{c:e}')  # scientific notation

# casting
print(int('01234'))  # can convert string to int too, except if not int
print(float('3.14'))

print(type('1234'))  # <class 'str'>
print(type(int('1234')))  # <class 'int'>
print(isinstance(1234, int))  # True


# https://realpython.com/python-f-strings/
