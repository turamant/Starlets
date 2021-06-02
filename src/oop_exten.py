import math

class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, znak):
        if znak == '*':
            return self.x * self.y
        if znak == '+':
            return self.x + self.y
class Strip:
    def __init__(self, characters):
        self.characters = characters

    def __call__(self, string):
        return string.strip(self.characters)

class Const:
    def __getattr__(self, key):
        if key in self.__dict__:
            raise ValueError("нет заначения такого атрибута")
        return key

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ValueError("cannot change a const attribute")
        self.__dict__[key]= value

    def __delattr__(self, key):
        if key in self.__dict__:
            raise ValueError("cannot delete a const attribute")
        raise AttributeError(f"{self.__class__.__name__} object has no attribute {key}")


class Point:
    #__slots__ = ("__x", "__y", "__radius")

    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def __getattr__(self, item):
        return f'Код символа {item}: {ord(item)}'

    @property
    def area(self):
        return 2 * math.pi * self.__radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, other):
        self.__x = other

    @x.deleter
    def x(self):
        del self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        return f"{self.__class__.__name__}:{self.__x, self.__y}"

def my_strip(characters):
    def function(string):
        return string.strip(characters)
    return function


str_punctuation = my_strip("!?")
new = str_punctuation("Hello world!!!!!")
print(new)

def bold(h):
    def function(s):
        return f'Hello{h}+{s}'
    return function

a = bold("Pizda")
print(a('Rulja'))


strip = Strip("!?")
print(strip('???Land hoy!!!'))
calc1 = Calc(2, 5)
print(calc1("*"))
print(calc1('+'))





