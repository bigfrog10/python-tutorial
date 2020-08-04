class MyClass:
    def f(self):
        return 'hello world'

    @staticmethod
    def g():
        return 'bye world'


x = MyClass()
print(x.f())
print(MyClass.g())
print(x.g())


class MyClass1:
    region = 'west'

    def __init__(self, region):
        self.region = region

    @staticmethod
    def f():
        return MyClass1.region


a = MyClass1('east')
print(a.region)
print(MyClass1.region)
print(a.f())


class Animal:
    def __init__(self, name):
        self.name = name
        self.food = None

    def eat(self, food):
        self.food = food
        print(self.name, ' eating ', food)


class Dog(Animal):
    def bark(self):
        print('bark')


cat = Animal('cat1')
cat.eat('catfood')

dog = Dog('dog1')
dog.eat('dogfood')