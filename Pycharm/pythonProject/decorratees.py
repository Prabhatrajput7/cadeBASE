# Higher order function is the one that accept and return a fx
#first fx pass to top fx the fx with args pass to wrapper fx

# def hell():
#     print('hell')
# gate = hell
# del hell
# print(gate())
#
# def test1(func):
#     func()
# def test2():
#     print('test2')
# test = test1(test2)
# print(test)

#decorator

# def my_dec(func):
#     def wrapper():
#         print('******')
#         return func()
#     return wrapper
#
# @my_dec
# def hello():
#     return 'Hi'
# 
# print(hello())

# def abc(a):
#     def xyz(b):
#         return a+b
#     return xyz(2)
#
# a = abc(5)
# print(a)

# def s(a):
#     def s2(b):
#         return a+b
#     return s2
# s3 = s(2)
# print(s3(5))


#
# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#         print('*')
#
#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name!')
#         self.first = None
#         self.last = None
#
#
# emp_1 = Employee('John', 'Smith')
# print(emp_1.first)
# emp_1.fullname = "Corey Schafer"
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

# del emp_1.fullname




# def one():
#     def two():
#         print('two')
#     print('one')
#     return two()
#
# print(one())


# def dec(func):
#     def wrap():
#         print('***')
#         func()
#         print('***')
#     return wrap
#
# @dec
# def hell():
#     print('HEL')
#
# hell()

# def checkout(f):
#     def checkin(*agrs):
#         # return map(f,sorted(lst,reverse=True))
#         return sorted(lst,reverse=True)
#     return checkin
#
#
# @checkout
# def check(lst):
#     if not lst:
#         return lst
#
# lst=  [i for i in range(5)]
# print(*check(lst),sep=',')
#
from functools import wraps
# def deco(fx):
#     # @wraps(fx)
#     def wraper(*args):
#         print('1st deco')
#         print(fx.__name__)
#         return fx(*args)
#     return wraper
#
# def timo(fx):
#     # @wraps(fx)
#     def wrappo(*args):
#         print('2nd deco')
#         print(fx.__name__)
#         return fx(*args)
#     return wrappo
#
# @deco
# @timo
# def hello(name='sam',age=4):
#     print(f'{name} and {age}')

# hello()
# t = deco(timo(hello))
# print(t.__name__)

# def ak(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# ak(1,2,3,4,5,6,p= 'hell')
#
# user1 = {
#     'name': 'Sorna',
#     'valid': True
# }
#
# def authenticated(fn):
#   def wrapper(*args, **kwargs):
#     print(args)#tuplle
#     print(kwargs)
#     if args[0]['valid']:
#         return fn(*args, **kwargs)
#   return wrapper
#
# @authenticated
# def message_friends(user,p= 'hell'):
#     print('message has been sent')
#
# message_friends(user1)
#
# user1 = {
#     'name': 'Sorna',
#     'valid': True
# }
#
# def authenticated(fn):
#   def wrapper(u):
#     if u['valid']:
#         return fn(u)
#   return wrapper
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# message_friends(user1)



# class Deco(object):
#     def __init__(self,fx):
#         # print(fx)
#         self.fx = fx
#
#     def __call__(self, *args, **kwargs):
#         return self.fx(*args, **kwargs)
#
#
# @Deco
# def Hello(n,a):
#     print(f'Name {n}, Age {a}')
# #
# Hello('AA',20)
# from functools import wraps
# def name(fx):
#     # print('one')
#     @wraps(fx)
#     def wrapper(*args,**kwargs):
#         # print('one')
#         return fx(*args,**kwargs)
#     return wrapper
# def age(fx):
#     # print('two')
#     @wraps(fx)
#     def wrapper(*args,**kwargs):
#         # print('two')
#         return fx(*args,**kwargs)
#     return wrapper
# @name
# @age
# def info():
#     print('ABC')
#
# info()
# e = name(age(info))
# print(e.__name__)
# e()
# a = info
# print(a.__name__)

# def p(fx):
#     return fx()
#
# def q():
#     print('q')
# a = p(q)
# print(a)



import os
# from contextlib import contextmanager
#
# @contextmanager
# def writetofile(name,mode):
#     f = open(name,mode)
#     yield f
#     f.close()
#
# with writetofile('one.txt','w') as f:
#     f.write('Context manager')


import datetime
print(datetime.datetime.now()-datetime.timedelta(hours=2))






c = ['id', 'op', 'speed', 'side']
d = (1, 'Ash', 3, 'Attack')

print(list(zip(c,d)))










