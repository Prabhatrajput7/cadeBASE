# print(*(i for i in range(1,100) if i%7 ==0 and i%5!=0), sep=',')

# from functools import reduce
# # n =5
# factorial = reduce(lambda x, y: x * y, range(1, 6))
# print(factorial)

# d = {i:i*i for i in range(1,6)}
# print(d)

# daa = input().split(',')
# print(list(daa))

# class U:
#     def get(self):
#         self.s = input()
#     def show(self):
#         print(f'name is {self.s.upper()}')
#
# name = U()
# name.get()
# name.show()

# import math
# c = 50
# h = 30
# value = []
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))

# x,y = map(int,input().split(','))
# lst = [[i*j for j in range(y)] for i in range(x)]
# print(lst)

# lst = [i for i in input().split(',')]
# lst.sort(key= lambda x:len(x) )
# print(','.join(lst))

# def inputs():
#     while True:
#         st = input()
#         if not st:
#             return
#         yield st
# print(*(line.upper() for line in inputs()),sep='\n')

# lst =[]
# while True:
#     data = input()
#     if data:
#        lst.append(data.upper())
#     else:
#         break
#
# for i in lst:
#     print(i)


# word = sorted(list(set(input().split())))
# print(" ".join(word))


# print(*(i for i in input().split(',') if int(i, 2) % 5 ==0))

# import re
# input_string = input('> ')
# counter = {"LETTERS":len(re.findall("[a-zA-Z]", input_string)), "NUMBERS":len(re.findall("[0-9]", input_string))}
# print(counter)

# map() digits of each number with lambda function and check if all() of them even
# str(num) gives us opportunity to iterate through number by map() and join()
# print(','.join([str(num) for num in range(15, 30) if all(map(lambda num: int(num) % 2 == 0, str(num)))]))

# import re
# input_string = input('> ')
# counter = {"Uppercase":len(re.findall("[A-Z]", input_string)), "Lowercase":len(re.findall("[a-z]", input_string))}
# print(counter)

# n = input()
# print(sum([int(i*n) for i in range(1,5)]))

# print(','.join([str(int(i)*int(i)) for i in input().split(',') if int(i)%2!=0]))

# lst =[]
# while True:
#     data = input().split(',')
#     if not data[0]:
#         break
#     lst.append(tuple(data))
#
# lst.sort(key=lambda x:(x[0],int(x[1]),int(x[2])))
# print(lst)


# import re
# data = input().split(",")
# pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
# for i in data:
#     if pattern.fullmatch(i):
#         print(i)

# account = 0
# while True:
#     action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
#     if action[0] == "d":
#         deposit = input("How much would you like to deposit? ")
#         account = account + int(deposit)
#     elif action == "w":
#         withdrow = input("How much would you like to withdrow? ")
#         account = account - int(withdrow)
#     elif action == "b":
#         print(account)
#     else:
#         quit()

# data = input().split(' ')
# word = sorted(set(data))
# d ={}
# for i in word:
#     d[i] = data.count(i)
#     print(f'{i}: {data.count(i)}')
# print(d)

# alleven
# print(','.join([str(i) for i in range(1000,1100) if all(map(lambda x:int(x)%2 ==0, str(i)))]))

# class G:
#     def gen(self):
#         self.s=[]
#         self.s = map(int,input().split(','))
#         for self.i in self.s:
#             if self.i % 7 == 0:
#                 yield self.i
#
# num = G()
# for i in num.gen():
#     print(i)

# lst = []
# while True:
#     data = input()
#     if not data:
#         break
#     lst.append(tuple(data))
# print(lst)


# import  math
#
# x,y = 0,0
# while True:
#     s = input().split()
#     if not s:
#         break
#     if s[0]=='UP':
#         x-=int(s[1])
#         print(x)
#     if s[0]=='DOWN':
#         x+=int(s[1])
#         print(x)
#     if s[0]=='LEFT':
#         y-=int(s[1])
#         print(y)
#     if s[0]=='RIGHT':
#         y+=int(s[1])
#         print(y)
#
# dist = round(math.sqrt(x**2 + y**2))
# print(dist)


# 21
# import math
# y,x = 0,0
# while True:
#     data = input().lower().split(" ")
#     if data[0] == "up":
#         y+=int(data[1])
#     elif data[0] == "down":
#         y-=int(data[1])
#     elif data[0] == "left":
#         x+=int(data[1])
#     elif data[0] == "right":
#         x-=int(data[1])
#     else:
#         break
# print(round(math.sqrt((y**2)+(x**2))))
# lst = [str(i) for i in range(1000,1010)]
# lst2 = [i for i in range(1000,1010)]
# print(lst)
# print('*')
# print(lst2)
#
# for i in lst2:
#     for j in i:
#         print(j)

# lst = [str(i) for i in range(1000, 1010)]
# lst = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst))
# print(" ".join(lst))

# lst = [str(i) for i in range(1000,3001)]
# lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
# print(",".join(lst))

# data = input().split(' ')
# data2 = sorted(set(data))
# for i in data2:
#     print(f'{i} = {data.count(i)}')

# a = int(input())
# b = chr(a)
# print(b)

# def addi(x,y):
#     return x+y
# x,y = map(int,input().split(','))
# print(addi(x,y))

# def sq():
#     lst = [i*i for i in range(0,10)]
#     return tuple(lst)
# print(sq())

# input = input('Enter string:')
# print(''.join(['Yes' if input == 'yes' or input =='YES' or input =='Yes' else 'No' ]))

# def m(i):
#     return i*i
# print(list(map(m, [1,2,3,4,5,6,7,8,9,10])))

# def even(x):
#     return x%2==0
# def squer(x):
#     return x*x
# lii = [int(i) for i in input().split(',')]
# li = map(squer,filter(even,lii))
# print(list(li))


# def sq(item):
#     return item**2
# lii = [int(i) for i in input().split(',')]
# print(list(map(sq,lii)))

# print(list(map(lambda x:x**2, range(1,10))))

# nums = range(2, 100)
# for i in range(2, 10):
#     nums = list(filter(lambda x: x == i or x % i, nums))
# print(nums)

# class Am:
#     @staticmethod
#     def printNationality():
#         return f'American'
#
# print(Am.printNationality())

# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def out(self):
#         return f'AOC = {2*3.14*int(self.r)}'
#
# area = Circle(5)
# print(area.out())

# class Rec:
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#     def out(self):
#         return f'AOR = {int(self.l)*int(self.b)}'
#
# area = Rec(5,5)
# print(area.out())


# class Shape():
#     def __init__(self):
#         pass
#
#     def area(self):
#         return 0
#
# class Square(Shape):
#     def __init__(self,length = 0):
#         Shape.__init__(self)
#         self.length = length
#
#     def area(self):
#         return self.length*self.length
#
# Asqr = Square(5)
# print(Asqr.area())

# n = int(input())
# f = 0
# for i in range(2,n):
#     if n%i == 0:
#         f = 1
#         break
# if f == 0:
#     print('Prime')

# lst = [int(i) for i in range(2,20)]
# #a = map(int,input())
# print(list(filter(lambda x:all(x%j!=0 for j in range(2,int(x*0.5) + 1) ),lst)))


# until = 20
# lst = [n for n in range(2, until) if all(n % m != 0 for m in range(2, n-1))]
# print(lst)

# for i in range(2,20):
#     if i > 1:
#         for j in range(2,i):
#             if (i%j) ==0:
#                 break
#         else:
#             print(i)

# def divide():
#     return 5/0
#
# try:
#     divide()
# except ZeroDivisionError as ze:
#     print("Why on earth you are dividing a number by ZERO!!")
# except:
#     print("Any other exception")

# class CustomException(Exception):
#     """Exception raised for custom purpose
#
#     Attributes:
#         message -- explanation of the error
#     """
#     def __init__(self, message):
#         self.message = message
#         print(self.message)
# num = int(input())
# try:
#     if num < 10:
#         raise CustomException("Input is less than 10")
#     elif num > 10:
#         raise CustomException("Input is grater than 10")
# except CustomException as ce:
#     print("The error raised: " + ce.message)

# email = "john@google.com"
# email = email.split('@')
# print(email[0])

# import re
#
# email = "john@google.com elise@python.com"
# pattern = "(\w+)@\w+.com"
# ans = re.findall(pattern,email)
# print(ans)
#
# import re
#
# email = "john@google.com elise@python.com"
# pattern = "\w+@(\w+).com"
# ans = re.findall(pattern,email)
# print(ans)

# data = input().split(' ')
# lst = [i for i in data if i.isdigit()]
# print(lst)

# import re
#
# email = input()
# pattern = "\d+"
# ans = re.findall(pattern,email)
# print(ans)

# unicodeString = u"hello world!"
# print(unicodeString)

# s = input()
# u = s.encode('utf-8')
# print(u)

# -*- coding: utf-8 -*-
# Write a special comment to indicate a Python source code file is in unicode.

# def question_59(n):
#     print(round(sum(map(lambda x: x/(x+1), range(1, n+1))), 2))
# question_59(5)

# n = int(input())
# f = lambda x: f(x-1)+100 if x > 0 else 0
# print(f(n))

# n = int(input())
# f = lambda x: x*f(x-1) if x>1 else 1
# print(f(n))

# def f(n):
#     if n < 2:
#         return n
#     return f(n-1) + f(n-2)
#
# n = int(input())
# print(f(n))

# import random
# rand_num = random.uniform(10,100)
# print(rand_num)
#
# ran_i = random.randint(7,15)
# print(ran_i)

# import zlib
# s = 'hello world!hello world!hello world!hello world!'
# # In Python 3 zlib.compress() accepts only DataType <bytes>
# y = bytes(s, 'utf-8')
# x = zlib.compress(y)
# print(x)
# print(zlib.decompress(x))

# import time
# before = time.time()
# for i in range(100):
#     x = 1 + 1
# after = time.time()
# execution_time = after - before
# print(execution_time)

import random

# lst = [3,6,7,8]
# random.shuffle(lst)
# print(lst)

# to be written
# li = [12,24,35,70,88,120,155]
# li = [li[i] for i in range(len(li)) if i < 3 or i > 4]
# print(li)

# li = [12,24,35,70,88,120,155]
# li = [x for i,x in enumerate(li) if i not in(3,4)]
# print(li)

# li = [12,24,35,24,88,120,155]
# li = [x for i,x in enumerate(li) if x!=24]
# print(li)


# list1 = [1,3,6,78,35,55]
# list2 = [12,24,35,24,88,120,155]
# set1= set(list1)
# set2= set(list2)
# intersection = set1 & set2
# print(intersection)


# lst = [12,24,35,24,88,120,155,88,120,155]
# lst = sorted(set(lst), reverse= True)
# print(lst)

# class Person(object):
#
#     def __init__(self):
# 	    self.gender = "unknown"
#
#     def getGender(self):
# 	    print(self.gender)
#
# class Male(Person):
#     def __init__(self):
# 	    self.gender = "Male"
#
# class Female(Person):
#     def __init__(self):
# 	    self.gender = "Female"
#
# sharon = Female()
# doug = Male()
# sharon.getGender()
# doug.getGender()


# class Person(object):
#     def getGender( self ):
#         return "Unknown"
#
# class Male( Person ):
#     def getGender( self ):
#         return "Male"
#
# class Female( Person ):
#     def getGender( self ):
#         return "Female"
# ap = Person()
# aMale = Male()
# aFemale= Female()
# print(aMale.getGender())
# print(aFemale.getGender())
# print(ap.getGender())


# s = 'abcdefgabc'
# for i in sorted(set(s)):
#     print(f'{i}, {s.count(i)}')

# import itertools
# print(list(itertools.permutations([1,2,3])))


# n = int(input())
# f = lambda x: 0 if x == 0 else 1 if x == 1 else f(x-1)+f(x-2)
# print(','.join([str(f(x)) for x in range(0, n+1)]))

# m = int(input())
# def f(n):
#     if n==0:
#         return 0
#     else:
#         if n==1:
#             return 1
#         else:
#             return f(n-1)+f(n-2)
# print(','.join([str(f(x)) for x in range(0, m+1)]))

# def binary_search_Ascending(array, target):
#     lower = 0
#     upper = len(array)
#     print('Array Length:',upper)
#     while lower < upper:
#         x = (lower + upper) // 2
#         print('Middle Value:',x)
#         value = array[x]
#         if target == value:
#             return x
#         elif target > value:
#             lower = x
#         elif target < value:
#             upper = x
#
# Array = [1,5,8,10,12,13,55,66,73,78,82,85,88,99]
# print('The Value Found at Index:',binary_search_Ascending(Array, 82))
#
#
#
# import random
# resp = [i for i in range(10,151) if i % 35 == 0 ]
# print(random.choice(resp))
#
# import random
# resp = [i for i in range(0,11,2)]
# print(random.choice(resp)) #choice any even but out one no
#
# import random
# resp = random.sample(range(100,201),5)
# print(resp)

# import random
# lst = [i for i in range(1,1001) if i%35 == 0]
# resp = random.sample(lst,5) #sample any 5
# print(resp)


# import re
# s = 'H1e2l3l4o5w6o7r8l9d'
# counter = re.findall("[a-zA-Z]", s)
# print(''.join(counter))

# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs
# among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

# def solve(numheads,numlegs):
#     ns='No solutions!'
#     for i in range(numheads+1):
#         j=numheads-i
#         if 2*i+4*j==numlegs:
#             return i,j
#     return ns,ns
#
# numheads = 35
# numlegs = 94
# solutions=solve(numheads,numlegs)
# print(solutions)

# n = int(input())
# arr = map(int, input().split())
# arr = sorted(list(set(arr)))
# print(arr[-2])


# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# import textwrap
# string = input()
# width = int(input())
# print(textwrap.fill(string,width))

#
# import calendar
#
# month, day, year = map(int, input().split())
# dayId = calendar.weekday(year, month, day)
# print(calendar.day_name[dayId].upper())

# def prime(n):
# 	return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n>1
# n = 5
# if prime(n):
# 	print("Yes")
# else:
# 	print("No")


# n = int(input())
# set1 = set(map(int,input().split()))
# m = int(input())
# set2 = set(map(int, input().split()))
# ans = list(set1 ^ set2)
# print(ans)
# ans.sort()
# print(ans)
# for i in ans:
#     print(i)


# n = int(input())
# f = lambda x: x+f(x-1) if x > 0 else 0
# print(f(n))

# word = input()
# dct = {}
# for i in word:
#     dct[i] = dct.get(i, 0) + 1
# print(sorted(dct.items(),key=lambda x:x[1],reverse=True))

# n = int(input())
# word_list = []
# word_dict = {}
# for i in range(n):
#     word = input()
#     if word not in word_dict:
#         word_list.append(word)
#     word_dict[word] = word_dict.get(word, 0) + 1
# print(len(word_list))
# for word in word_list:
#     print(word_dict[word], end=' ')


# n =input()
# v = 'aeiou'
# d = {}.fromkeys(v,0)
# for i in n:
#     if i in d.keys():
#         d[i]+=1
# print(d)


################################################
# pattern

# for i in range(1,5):
#     for j in range(0,i):
#         print('* ',end='')
#     print(' ')

# #num = 65
# for i in range(1,5):
#     #num = 65
#     for j in range(0,i):
#         ch = chr(num)
#         print(ch,end='')
#         num += 1
#     print(' ')

# num = 1
# for i in range(1,5):
#     for j in range(0,i):
#         print(num,end=' ')
#         num += 1
#     print(' ')

# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(1,i):
#         print(j, end='')
#     print(' ')

# def pypart2(n):
#     k = 2 * n - 2
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 2
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
# n = 5
# pypart2(n)
#
#
# def triangle(n):
#     k = n - 1
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
# n = 5
# triangle(n)

# n =int(input())
# k = 2*n-2
# k = 8 #n =5
# for i in range(0,5):
#     for j in range(0,k):
#         print(end=' ')
#     k-=2
#     for l in range(0,i+1):
#         print('* ',end='')
#     print(' ')

# n = int(input())
# k = n-1
# for i in range(0,5):
#     for j in range(0,k):
#         print(end=' ')
#     k-=1
#     for l in range(0,i+1):
#         print('* ',end='')
#     print(' ')


# def uniqueElems(lst):
#     for i in set(lst):
#         yield i
# l = [1, 1, 1, 1, 1, 2, 3, 4]
# for j in uniqueElems(l):
#     print(j,end=' ')

# def uniqueElems(lst,lst1):
#     for i in lst1:
#         if lst.count(i) > 2:
#             lst1.remove(i)
#         return lst1
# l = [1, 1, 1, 1, 1, 2, 3, 4]
# l1 = set(l)
# print(uniqueElems(l,l1))


# animals list contains the objects you made using cat class so when you are calling for animal.walk it will call cat class function

# def login(driver):
#     while True:
#         try:
#             driver
#         except ZeroDivisionError:
#             print('aa')
#             break
#     return True
#
# d= 5
# if login(d):
#     print('Yes')
# else:
#     print('NO')


#####################################################
# convert
# n ='helli'
# print([i for i in n])

# s = ['Geeks', 'for', 'Geeks']
# str1=" "
# print(str1.join(s))

# Python3 program to Convert a
# list to dictionary

# def Convert(a):
#     it = iter(a)
#     res_dct = dict(zip(it, it))
#     return res_dct
#
#
# # Driver code
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(Convert(lst))


# n = int(input('>'))
# s = set()
# for i in range(n):
#     s.add(int(input('>>')))
# print(s)


# def valuee(lst,idx):
#     return lst[idx]
# lst = [1,2,3,4,5]
# idx = 2
# print(valuee(lst,idx))


# s = 'youtube'
# print(s[::-1])


# a = 'hi'
# b ='[hello hi]'
#
# print([i.replace('[]/[]',"") for i in b.split(' ')])


# d1 = {'name': 'Ravi', 'age': 23, 'marks': 56}
# lst = list(d1.items())
# lst2 = [j for i in d1.items() for j in i]
# print(lst2)


# lst = [1,2,3]
# print([(i,i**3) for i in lst])

# lst = [[('abc',1),('prq',2)],[('xyz',3)]]
# lst2 = [7,8]
# print([[i+(lst2[id],) for i in j] for id,j in enumerate(lst)])


# lst = [1,2,3]
# lst2 = [7,8,1]
# print(bool(set(lst).intersection(set(lst2))))

# sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
# for i in range(len(sets),0,-1):
#     print(sets)
#     sets.pop()

# import sys
# Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
# print(sys.getsizeof(Set2),"bytes")

# d ={'a': 100, 'b':200, 'c':300}
# print(sum(d[i] for i in d))


# dict = {}
# x, y, z = 10, 20, 30
# dict[x, y, z] = x + y - z;
# x, y, z = 5, 2, 4
# dict[x, y, z] = x + y - z;
# print(dict)

# key_value ={}
# key_value[2] = '64'
# key_value[1] = '69'
# key_value[4] = '23'
# key_value[5] = '65'
# key_value[6] = '34'
# key_value[3] = '76'
# print(sorted(key_value.items(),key=lambda x:x[1]))

# s = '43217'
# for i in s:
#     print('*'*int(i))

# n=5
# for i in range(n):
#     print(' '*(n-i-1) +'*'*((2*i)+1))
#
# for i in range(n-1,0,-1):
#     print(' '*(n-i) + '*'*((2*i)-1))

# square = lambda x: x * x if x > 0 else x
# print(square(6))

# from functools import reduce
# fab = lambda x: reduce(lambda p,q:p+q,range(x+1))
# n = 3
# for i in range(n):
#     print(fab(i))


# lst = [1,2,3,4,5,6]
# print(len(list(filter(lambda x:x%2==0,lst))))

# a = 2
# b = 5
# print(a ^ b)
# def sortbyPattern(pat, str):
#     priority = list(pat)
#     myDict = {priority[i]: i for i in range(len(priority))}
#     print(myDict)
#     str = list(str)
#     str.sort(key=lambda ele: myDict[ele])
#     print(sorted(str,key=lambda ele: myDict[ele]))
#     str.reverse()
#     new_str = ''.join(str)
#     return new_str
#
#
# if __name__ == '__main__':
#     pat = "asbcklfdmegnot"
#     str = "eksge"
#     new_str = sortbyPattern(pat, str)
#     print(new_str)


# s = 'hi i am'
# print([sorted(i) for i in s.split(' ')])

# l = ['1','4','5']
# print(' '.join(l))

# d = {
#     'a':'one',
#     'b':'two'
# }

import json

# for i in ['{','}']:
#     print(str(d).replace(i,""))

# lst =['1','2','3','4']

# print({lst[i]:lst[i+1] for i in range(0,len(lst),2)})
# lst =[]
# for i in d.items():
#     for j in i:
#         lst.append(j)
# print(lst)


# a = input('enter a no')
# print(eval(a))


# from functools import reduce
# n = int(input('>'))
# f = reduce(lambda x, y: x * y, range(1, n+1))
# print(f)

# n = int(input('>'))
# f = lambda x:1 if x <= 1 else x*f(x-1)
# print(f(abs(n)))

# def fabo(n):
#     a,b = 0,1
#     for i in range(n):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
#
#
# for i in fabo(5):
#     print(i)

# n = int(input('>'))
# lst,l = list(map(int, range(0,21))),[]
# def prime(n):
#     return all(n%i for i in range(2,int(n/2))) and n >1
# for i in range(len(lst)):
#     if prime(i):
#         l.append(i)
# print(*l,sep=',')
# lst = list(map(int, range(0,21)))
# print(*(list(filter(lambda x:all(x%i!=0 for i in range(2, int(x/2)+1)),lst))))

# lst = [str(i) for i in range(11,15)]
# print(*(list(filter(lambda x:all(ord(i)%2==0 for i in x),lst))))

# for i in lst:
#     s = 0
#     for j in i:
#         s += int(j)
#     if s % 2 ==0:
#         print(i)

# print(eval(input('>')))

import json








# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# # use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
# print(json.dumps(x, indent=4, separators=(". ", " = ")))


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     print('x', self.a)
#     x = self.a
#     self.a += 1
#     return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))

# arm = input('>')
# if sum([int(i) ** 3 for i in arm]) == int(arm):
#   print('yes')
# else:
#   print('no')


# v = 'aeiou '
# d ={}.fromkeys(v,0)
# s = 'enter a number'
#
# for i in s:
#   if i in d:
#     d[i] += 1
#
# print(d)


lst =[1,2,3,4,5]
t = int(5)
print(id(t))

# def twosum(lst,t):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[j] == t - lst[i]:
#                 yield [i, j]
# #
# print(twosum(lst,t))
# for i in twosum(lst,t):
#     print(i)

# d = {
#     'one':1,
#     'two':2
# }
#
# for i,j in d.items():
#     print(j)


# a = int(input('>'))
# if int(str(a)[::-1]) == a:
#     print('true')


# lst = [1,2,3,4,5,5,5]
# while True:
#     if 5 in lst:
#         lst.remove(5)
#     else:
#         break
# print(lst)
# lst=[]
# n = input('enter')
# [lst.append(int(input('>'))) for i in range(0,int(n))]
# print(lst)

# s = '43455256'
# lst, lst1, i = [], [], 0
# [lst.append(int(i)) for i in s]
# for j in range(len(lst) - 1, 0, -1):
#     if i<len(lst)//2:
#         lst1.append(lst[i] + lst[j])
#         i = i + 1
#     else:
#         break
# print(''.join(str(i) for i in lst1))

# [lst1.append(lst[i] + lst[j]) if i<len(lst)//2 else for i,j in enumerate(len(lst) - 1, 0, -1)]


# lst = [1,1,2,3,4,5]
# s =list(map(str,range(0,5)))
# print(s)
# print([int(i) for i in s if int(i) not in lst])


# d = {
#     'a':[1,2],
#     'b':[2,3]
# }
#
# del d['a']
#
# print(d)


# lst,lst2  = [1,2,3,4,5,6,7,8,9],[]
# for i in lst:
#     if i%2==0:
#         lst2.append(i)
#         lst.remove(i)
# print(lst2+lst)


#
# arr = [3,1,4,6,5]
# # 1 3 4 5 6
# def pytha(arr):
#     ar1 = [x**2 for x in arr]

# l = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#
# for i in range(len(l)):
#     if i%2 !=0:
#         l[i].reverse()
#         print(*l[i],end=' ')
#     else:
#         print(*l[i],end=' ')


# a = True
# a = "Hello"
# a = "hi"
# a = 5
# print(a)

# fib = lambda n : n if n <= 1 else fib(n-1) + fib(n-2)
# result = fib(3)
# print(result)








# x = globals()
# print(x["__file__"])
#
# a = format(255,'%')
# print(a)
#
# x = 'name = "John"\nprint(name)'
# exec(x)
#
# rev = 'rada'
# print(rev.find('de'))

# r = lambda x:x[::-1] if len(x)>1 else x
# l = [1,2,3]
# print(r(l))

# n = 14
# c = 0
# while n>0:
#     if n%2 ==1:
#         n -=1
#     else:
#         n /=2
#     c+=1
# print(c)


# def twosum(nums,target):
#     for idx, value in enumerate(nums):
#         if target - value in nums:
#             return [nums[target - value], idx]
#         else:
#             nums[value] = idx
#
# nums= [1,2,3]
# t = 3
# print(twosum(nums,t))