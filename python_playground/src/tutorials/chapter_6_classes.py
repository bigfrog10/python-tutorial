# class is a template to create objects.
# class is an extension to functions with extra states/properties.
# class has 3 characteristics:
#     encapsulation, inheritance, and polymorphism
#

# protected members can be see in this module or subclasses
# private members stay in this class and should not be used elsewhere.
# private members can be changed/modified without notice.
# favorite food is private, indicating we deal with food/eat logic
# in this class.
# private members and methods are the encapsulation.
class Animal:
    def __init__(self, name, favorite_food):  # constructor
        self.name = name  # public member
        self._energy = 100  # this is protected member of the class
        self.__favorite_food = favorite_food  # this is private member, not used outside this class

    def eat(self, food):
        energy = 50 if food == self.__favorite_food else 20
        print(f'{self.name} eats {food} and gets energy {energy}')
        self._energy += energy

    def is_hungry(self):
        print(f'{self.name} check hunger threshold: 30 ...')
        return self._energy < 30

    def sleep(self):
        self._energy += 20

    # we don't define walk/run/fly in this class.


class Bird(Animal):  # subclass of Animal
    def __init__(self, name, favorite_food):
        super().__init__(name, favorite_food)  # call parent constructor

    def fly(self):
        if not self.is_hungry():
            print(f'{self.name} flies ...')
            self._energy -= 30
        else:
            print(f'{self.name} is hungry!')

    def is_hungry(self):  # overwrite parent, polymorphism
        print(f'{self.name} check hunger threshold: 20 ...')
        return self._energy < 20  # can do more


class Dog(Animal):
    def __init__(self, name, favorite_food):
        super().__init__(name, favorite_food)

    def talk(self, message):  # new method
        print(f'{self.name} barks: {message}')
        self._energy -= 10

    def walk(self, speed):
        if not self.is_hungry():
            print(f'{self.name} walks ...')
            self._energy -= 20 * speed / 10
        else:
            print(f'{self.name} is hungry!')


blue_jay = Bird('blue jay', 'nuts')
blue_jay.fly()
blue_jay.fly()
blue_jay.fly()
blue_jay.fly()
blue_jay.eat('worm')
blue_jay.fly()
blue_jay.fly()
blue_jay.eat('nuts')

husky = Dog('husky', 'treat')
husky.talk('play with me')
husky.walk(10)
husky.walk(30)
husky.walk(30)


# it's possible to add fields dynamically, but it is recommended to declare all
# fields in the constructor for easy traceability. __slots__ can control this

# Liskov's principle:


# multi inheritance and diamond tree


# methods in class have scope too, object/instance level, class level, or static
class MyClass:
    def f(self):
        return 'hello world'

    @staticmethod
    def g():  # normally, we should refactor this out since there is no dependency here.
        return 'bye world'


x = MyClass()
print(x.f())
print(MyClass.g())
print(x.g())


# we may have class level properties and methods, they apply to all instances
class MyClass1:
    region = 'west'

    def __init__(self, region):
        self.region = region

    @classmethod
    def f(cls):
        return cls.region


a = MyClass1('east')
print(a.region)  # east
print(MyClass1.region)  # west
print(a.f())  # west
print(MyClass1.f())  # west


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

# magic methods



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
