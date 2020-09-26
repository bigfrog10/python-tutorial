# There are several scenarios for classes
# 1. classes with only fields, these are data classes
from dataclasses import dataclass


@dataclass
class Card:
    suite: str
    rank: str


c1 = Card('Hearts', 'A')  # we have to fill in all parameters (without default values)
print(c1)
print(repr(c1))
print(eval(repr(c1)))
print(eval(repr(c1)) == c1)  # True, equal by values
print(eval(repr(c1)) is c1)  # False, not same by instance
# We call these value objects in DDD (Domain Driven Design)
# Data class is a strong type place holder, otherwise we could use dictionary or list/tuple.
# another option is: from collections import namedtuple
# Better named fields are more readable.
c2 = Card('Hearts', 'K')
print(c1 == c2)
c3 = Card('Hearts', 'A')
print(c1 == c3)  # True, equal by values
print(c1 is c3)  # False, not same by instance


#
@dataclass
class Money:
    amount: int  # cents or dollar
    unit: str = 'USD'


print(Money(10))  # 10 dollars
print(Money(70, 'CNY'))  # 70 yuan


# Enum is a category class for a finite set of fixed values.
# copied from https://docs.python.org/3/library/enum.html#orderedenum
import enum


class OrderedEnum(enum.Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class CardSuite(OrderedEnum):
    SPADES = 4
    HEARTS = 3
    CLUBS = 2
    DIAMONDS = 1

    def __repr__(self):
        return self.name


print(CardSuite.SPADES > CardSuite.HEARTS)


class CardRank(OrderedEnum):
    A = 14
    K = 13
    Q = 12
    J = 11
    R10 = 10
    R9 = 9
    R8 = 8
    R7 = 7
    R6 = 6
    R5 = 5
    R4 = 4
    R3 = 3
    R2 = 2
    R1 = 1

    def __repr__(self):
        return self.name


@dataclass(order=True)  # ordered by the list of fields
class Card:
    suite: CardSuite
    rank: CardRank


print(Card(CardSuite.SPADES, CardRank.R10))
print(Card(CardSuite.SPADES, CardRank.R2) > Card(CardSuite.HEARTS, CardRank.K))

# 2. There are cases where we model objects with both fields and behaviors
# 3. There are cases where we have only behaviors exposed to uses and we keep internal states private.
# 4. If a class has no properties, private or public, these are likely to be refactored to functions.

# Address, book, car
# favor composition over inheritance
# favor functions over classes

# decorator with internal states
import time
import functools


class TimingDecorator:
    def __init__(self, function):
        self.function = function
        self.duration = 0
        functools.update_wrapper(self, function)
        # check more on these: composition is always hard unless we have the full scope
        # https://stackoverflow.com/questions/6394511/python-functools-wraps-equivalent-for-classes
        # https://hynek.me/articles/decorators/

    def __call__(self, *args, **kwargs):
        a = time.time()
        ret = self.function(*args, **kwargs)
        b = time.time()
        c = b - a
        self.duration += c
        print(f'function {self.function.__name__}() takes {self.duration} seconds.')
        print(self.duration)
        return ret


# need to fix meta data propagation
@TimingDecorator
def factorial(i: int) -> int:
    x = 1
    for y in range(2, i + 1):
        x *= y
    return x


print(factorial(3000))
print(factorial(3000))
