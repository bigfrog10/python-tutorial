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
    def __init__(self, name, favorite_food):  # constructor, __xxx__() are magic methods, hooks to the system
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


# magic methods

# getattr/setattr/dir(module or object)

# Python primitive types are immutable: int, float, complex, bool, string, and
# bytes. In contrast, some classes defined here can be changed in place, so they are
# mutable. List, dictionary, set and bytearray are mutable while tuple and frozenset are
# immutable.


class Food:
    def __init__(self, weight):
        self.__weight = weight

    def __repr__(self):
        return f'Food(weight={self.__weight})'

    def __str__(self):  # make them different for testing. Default is memory address
        return f"[Food[weight={self.__weight}]]"


f = Food(1.0)
print(f)  # use __str__ in both print and debug
print(repr(f))
print(eval(repr(f)))


class MyData1:
    def __init__(self):
        self.name = None
        self.count = None


class MyData2:
    def __init__(self, name, count):
        self.name = name
        self.count = count


d = {'name': 'ne zha', 'count': 2}
# MyData1(**d)  # syntax error
m1 = MyData1()
m1.__dict__.update(d)
print(m1.name)
print(m1.count)

m2 = MyData2(**d)
print(m2.name)
print(m2.count)


# http://blog.cleancoder.com/uncle-bob/2018/04/13/FPvsOO.html
# https://www.thedigitalcatonline.com/blog/2015/01/12/accessing-attributes-in-python/
