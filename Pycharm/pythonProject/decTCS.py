from functools import wraps

def decorator_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def square(x):
    return x**2

print(square.__name__)

def bind(func):
    func.data = 9
    return func

@bind
def add(x, y):
    return x + y

print(add(3, 10))
print(add.data)

import itertools
i = itertools.takewhile(lambda x: x<5, [1,4,6,4,1])
print(str(i))

# class A:
#
#     def __init__(self, x):
#         self.__x = x
#
#     @property
#     def x(self):
#         return self.__x
#
# a = A(7)
# a.x = 10
# print(a.x)

class A:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    @property
    def z(self):
        return self.x + self.y

a = A(10, 15)
b = A('Hello', '!!!')
print(a.z)
print(b.z)

class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    def getCirclesCount(self):
        return Circle.no_of_circles
c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)
print(c1.getCirclesCount())     # -> 3
print(c2.getCirclesCount())     # -> 3
print(Circle.getCirclesCount(c3)) # -> 3
# print(Circle.getCirclesCount()) # -> TypeError

class A:

    @classmethod
    def m1(self):
        print('In Class A, Class Method m1.')

    def m1(self):
        print('In Class A, Method m1.')

    def m1(self):
        print('In Class A, Method.')

a = A()

a.m1()

class A:

    @classmethod
    def getC(self):
        print('In Class A, method getC.')

class B(A):
    pass

b = B()
B.getC()
b.getC()


from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def m1(self):
        print('In class A, Method m1.')

class B(A):

    @staticmethod
    def m1(self):
        print('In class B, Method m1.')

b = B()
B.m1(b)

print('##########')

# class A(ABC):
#
#     @abstractmethod
#     @classmethod
#     def m1(self):
#         print('In class A, Method m1.')
#
# class B(A):
#
#     @classmethod
#     def m1(self):
#         print('In class B, Method m1.')
#
# b = B()
# b.m1()
# B.m1()
# A.m1()


from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def m1(self):
        print('In class A, Method m1.')

class B(A):

    def m1(self):
        print('In class B, Method m1.')

class C(B):

    def m2(self):
        print('In class C, Method m2.')

c = C()
c.m1()
c.m2()


# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def m1():
#         print('In class A.')
#
# a = A()
# a.m1()

from contextlib import contextmanager

@contextmanager
def context():
    print('Entering Context')
    yield
    print("Exiting Context")

with context():
    print('In Context')


from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1') :
    print('Hello')

def stringParser():
    while True:
        name = yield
        (fname, lname) = name.split()
        f.send(fname)
        f.send(lname)

def stringLength():
    while True:
        string = yield
        print("Length of '{}' : {}".format(string, len(string)))


f = stringLength(); next(f)

s = stringParser()
next(s)
s.send('Jack Black')


def nameFeeder():
    while True:
        fname = yield
        print('First Name:', fname)
        lname = yield
        print('Last Name:', lname)

n = nameFeeder()
next(n)
n.send('George')
n.send('Williams')
n.send('John')

#  mo.groupdict()

def stringDisplay():
    while True:
        s = yield
        print(s*3)


c = stringDisplay()
next(c)
c.send('Hi!!')

import re

print(re.sub(r'[aeiou]', 'X', 'abcdefghij'))

def smart_divide(func):
    def wrapper(*args):
        a,b=args
        if b==0:
            print('oops! cannot divide')
            return
        return func(*args)
    return wrapper
@smart_divide
def divide(a,b):
    return a/b

print(divide.__name__)
print(divide(4,16))
print(divide(8,0))

class A:

    @classmethod
    def getC(self):
        print('In Class A, method getC.')

class B(A):
    pass

b = B()
B.getC()
b.getC()

import re

print(re.split(r'[aeiou]', 'abcdefghij'))

from contextlib import contextmanager

@contextmanager
def context():
    print('Entering Context')
    yield
    print("Exiting Context")

with context():
    print('In Context')


class A:
    def __init__(self, a = 5):
        self.a = a

        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b = 0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10

x = B()
x.f1()
print(x.a,'-', x.b)

class A:
    x = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        A.x += 1

    def __init__(self):
        A.x += 1

    def displayCount(self):
        print('Count : %d' % A.x)

    def display(self):
        print('a :', self.a, ' b :', self.b)

# a1 = A('George', 25000)
# a2 = A('John', 30000)
# a3 = A()
# a1.display()
# a2.display()
# print(A.x)

class A:
    def __init__(self, x=5, y=4):
        self.x = x
        self.y = y

    def __str__(self):
        return 'A(x: {}, y: {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y


def f1():
    a = A(12, 3)
    b = A(3, 12)
    if (a == b):
        print(b != a)
        print(a)


f1()


class grandpa(object):
    pass

class father(grandpa):
    pass

class mother(object):
    pass

class child(mother, father):
    pass

print(child.__mro__)

# a = 5
# print(a+ 'hell')

class A:
    def __init__(self):
        print('one')

    def f(self):
        print(float())
        print(hex(-255))

class B(A):
    def __init__(self):
        print('two')

    def f(self):
        print(float())
        print(hex(-42))

x = B()
x.f()


# import sys,builtins
# print(sys.bui)

lst = []
lst = [i**+1 for i in range(3)]
print(lst)

d ={}
d = {i:j for i in "abcd" for j in "kpwp"}
print(d)

dic = {
    'a':'k',
    'a':'i',
    'a':'w',
    'a':'p'
}

print(dic)
