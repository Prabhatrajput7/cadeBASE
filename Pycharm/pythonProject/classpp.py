# global d
# d = 4
# class Pri:
#     def __init__(self,a,b,c):
#         self.a = a
#         self._b = b
#         self.__c = c
#
#     def disp(self):
#         return self.__pisp()
#
#     def __pisp(self):
#         return f'{self.a},{self._b},{self.__c}'
#
#     def __add__(self, other):
#         return self.a + other.__c
#
# p = Pri(d,2,3)
# q = Pri(1,2,3)
# print(p+q)
# print(p.disp())
# print(d)

# from datetime import  datetime
# year_choice = []
# for r in range(2000, (datetime.now().year+1)):
#     year_choice.append((r,r))
#
# print(year_choice)

# for i in range(1):
#     for j in range(1):
#         if j == 1:
#             break
#     print('**')

# i = 5
# def ich():
#     global i
#     return i
# print(ich())

# i = 7
# def check():
    # i = 8 87
    # global i 88
    # return i
# print(check())
# print(i)

# class Name:
#
#     def __init__(self,f,l):
#         self.f = f
#         self.l = l
#         # self.e = f'{self.f}.{self.l}@gmail.com'
#
#     @property
#     def email(self):
#         return f'{self.f}.{self.l}@gmail.com'
#
#     @property
#     def fullname(self):
#         return f'{ self.f} {self.l}'
#
#     @fullname.setter
#     def fullname(self,name):
#         self.f,self.l = name.split(' ')
#
#     @fullname.deleter
#     def fullname(self):
#         print('DELETED')
#         self.f = None
#         self.l = None
#
# n = Name('a','b')
# n.f = 'c'
# n.fullname = 'x y'
# print(n.email)
# print(n.fullname)
# del n.fullname


# class Holi:
#     leave = 8
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     @classmethod
#     def holiday(cls, newl):
#         cls.leave = newl
#
# h = Holi(10,20)
# h.holiday(18)
# print(Holi.leave)
#
# from datetime import datetime, timedelta, time
# class Timee:
#
#     def __init__(self,h,m):
#         self.h = h
#         self.m = m
#
#     @staticmethod
#     def gethr(a,b):
#         one = timedelta(hours=a.h, minutes=a.m)
#         two = timedelta(hours=b.h, minutes=b.m)
#         # one = time(a.h,a.m)
#         # two = time(b.h,b.m)
#         return one + two
#
#
# t = Timee(1,30)
# tt = Timee(2,50)
# c = Timee.gethr(t,tt)
# print(c)

# a = time(6,5)
# print(a)
# from datetime import datetime, timedelta
# print(datetime.now()+timedelta(hours=15))

# class Namee:
#     def __init__(self, n):
#         self.n = n
#
#     def display(self):
#         for i in self.n:
#             print(i.displayn())
#
# class One:
#     def __init__(self, name1):
#         self.name1 = name1
#
#     def displayn(self):
#         return f'{self.name1} is here'
#
# o = One('vigil')
# n = One('viggy')
# e = One('vig')
# print(One.displayn(e))
# na = Namee([o, n, e])
# na.display()

# for i in [o,n,e]:
#     print(i.displayn())

#ABStaract

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Square(Shape):
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#
#     def area(self):
#         pass
#
# a = Square(4,5)

# class M(object):
#     def __init__(self):
#         print('yes')
# M()

# class C:
#     pass
# c = C()
# d = C()
# e  =C()
# f =C()
# g =C()
# c.id = 1
# d.id = 2
# e.id = 3
# f.id = 4
# g.id = 5
#
# p = [c,d,e,f,g]
# r = [1,2,3,4,5]
# s = sorted(p,key=lambda x:r.index(x.id))
# print(*(i.id for i in s))


# class A:
#     def __fx(self):
#         print('fx')
#
# class B(A):
#     def fx(self):
#         # super().fx()
#         print('fx2')
#
# b = B()
# b.fx()
# a = A()
# print(a._A.__fx())

class D:

    def __init__(self,fx):
        self.fx = fx

    def __call__(self, *args, **kwargs):
        print(self.fx.__name__)
        return self.fx(*args, **kwargs)

@D
def deco(a,b):
    print(a,b)

deco(1,2)