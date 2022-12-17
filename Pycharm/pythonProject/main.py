# for i in range(2000, 3201):
#     if i % 7 ==0 and i % 5 !=0:
#         print(i, end=',')

# num = int(input('enter a number '))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)

# def fact(num):
#     return num * fact(num - 1)
# ans = fact(5)
# print(ans)

# def fact(num):
#     if num< 1:
#         return 1
#     else :
#         return num * fact(num -1)
# aa = fact(5)
# print(aa)

# n = int(input('enter a value'))
# ans = {}
# for i in range (1,n+1):
#     ans[i] = i * i
# print(ans)

# z = input('Enter numbers with comma')
# list = z.split(",")
# print(list)
# t = tuple(list)
# print(t)

# class caps:
#     def __init__(self, name):
#         self.name = name
#     def printString(self):
#         if self.name.isdigit():
#             return 'naah'
#         else:
#             z = self.name.upper()
#             print('your caps string is')
#             return z
#
# St = str(input('enter a string :- '))
# c1 = caps(St)
# print(c1.printString())

# class IOstring():
#     def get_string(self):
#         self.s = input('enter a string :- ')
#
#     def print_string(self):
#         print(self.s.upper())
#
# xx = IOstring()
# xx.get_string()
# xx.print_string()

# from math import sqrt
# import math
# d = int(input('enter a number'))
# c,h = 50,30
# output = math.sqrt((2*c*d)/h)
# print(output)

# x,y = map(int,input('enter 2 no. with comma ').split(','))
# x, y = 3, 5
# lst = []
#
#
# for i in range(x):
#     tmp = []
#     for j in range(y):
#         tmp.append(i*j)
#     lst.append(tmp)
# print(lst)


# list = input('enter string with comma ').split(',')
# list.sort()
# print(list)

# a = str(input('enter a string- '))
# b = a.upper()
# print(b)


# string = input('enter a string')
# for i in range(len(string)):
#     var = {
#         i: string[i]
#     }
#     print(var)

# vo = 'aeiou'
# list = []
# sentence = input('Enter your sentence: ' )
# for letter in sentence:
#     if letter in vo:
#         list.append(letter)
# print(list)


# string = input('enter a string ')
# n_s = string.casefold()
# nn = n_s.strip()
# print(nn)


# string = input('enter a string')
# new_S = ''
#
# for i in range(0,len(string)):
#     if string[i].islower():
#         new_S += string[i].upper()
#     elif string[i].isupper():
#         new_S += string[i].lower()
#     else:
#         new_S += string[i]
# print(new_S)

# string = input('enter a string')
# new_S = ''
#
# for i in string:
#     if i.islower():
#         new_S += i.upper()
#     elif i.isupper():
#         new_S += i.lower()
#     else:
#         new_S += i
# print(new_S)

# vo = 'aeiou'
# string = input('enter a string ')
# new =''
# c=0
# for i in string:
#     if i in vo:
#         new += i
#         c=c+1
# print(f'{new} count is {c}')

# dict ={}
# for i in range(6):
#     dict[i] = i*i
# print(dict)


# vo='aeiou'
# string = "Abcde"
# lc = string.lower()
# dict = {}
# for i in vo:
#     count = lc.count(i)
#     dict[i] = count
#
# print(dict)
# counts = dict.values()
# tv = sum(counts)
# print(tv)


# string= input('enter words ').split()
# s = []
# for i in string:
#     if i not in s:
#         s.append(i)
# s.sort()
# print(s)

# a = """ abc
# def
# egf"""

# print(a)

# word = input('enter words ').split()
# for i in word:
#     if word.count(i) > 1:
#         word.remove(i)
#
# word.sort()
# print(" ".join(word))


# data = input('enter digit').split(',')
# data = [i for i in data if int(i, 2) % 5 == 0]
# print(','.join(data))

# word = input('enter here')
# letter, digit = 0,0
#
# for i in word:
#     if i.isalpha(): #
#         letter += 1
#     elif i.isnumeric():
#         digit += 1
# print(f"LETTERS {letter}\n{digit}")

# word = input('enter here')
# letter, digit = 0,0
# for i in word:
#     if i.isalpha():
#         letter += 1
#     elif i.isnumeric():
#         digit += 1
#
# print(s,i)
# print(f"LETTERS {letter}\n{digit}")

# a = input('enter ')
# total,tmp = 0,str()        # initialing an integer and empty string
#
# for i in range(4):
#     tmp+=a               # concatenating 'a' to 'tmp'
#     total+=int(tmp)      # converting string type to integer type
#
# print(total)

# lst = input('enter no. ').split(',')
#
# seq = []
# lst = [int(i) for i in lst]
# print(lst)
# for i in lst:
#     if i % 2 != 0:
#         seq.append(i*i)
#
# seq = [str(i) for i in seq]
# print(",".join(seq))


# money = 0
# while 1:
#     trans = input('enter ').split(' ')
#     if trans[0] == 'D':
#         print(trans[1])
#         money = money + int(trans[1])
#     elif trans[0] == 'W':
#         money = money - int(trans[1])
#     elif input() == '':
#         break
#     print(f'Your current balance is: {money}')


# for i in range(8,10):
#    if i > 1:
#        for j in range(2, i):
#            if (i % j) == 0:
#                break
#        else:
#            print(i)


# n= 9
# for i in range(2,n):
#     if n%i == 0:
#         print(i)
#         print('Not a prime')
#         break
# else:
#     print('prime')


# vo = 'aeiou'
# list = []
# sentence = input('Enter your sentence: ' )
# for letter in sentence:
#     if letter in vo:
#         list.append(letter)
#
# list = [str(i) for i in list]
# print(",".join(list))

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print('')


# list = [10,12,15,12,15,20]
# l = []
# for i in list:
#     if i % 5 == 0:
#         l.append(i)
#
# t = set(l)
# t = [str(i) for i in t]
# print(type(t))
# print(t)

# vo='aeiou'
# string = "qwerty"
# lc = string.lower()
# dict = {}
# for i in vo:
#     count = lc.count(i)
#     dict[i] = count
#
# print(dict)
# counts = dict.values()
# tv = sum(counts)
# print(tv)

# for i,c in enumerate(list(range(10))):
#     if c == 5:
#         print(i)

# def fib(number):
#     a =  0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
# l = []
# for x in fib(5):
#     l.append(x)
# print(l)

# def subArrayExists(arr, n):
#     n_sum = 0
#     s = set()
#
#     for i in range(n):
#         n_sum += arr[i]
#         if n_sum == 0 or n_sum in s:
#             return True
#         print(n_sum)
#         s.add(n_sum)
#     return False
# arr = [6,-2,3,-1]
# n = len(arr)
# if subArrayExists(arr, n) == True:
#     print("Found a sunbarray with 0 sum")
# else:
#     print("No Such sub array exits!")

