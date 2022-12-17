# print(*(i for i in range(1, 50) if i%7 == 0 and i%5 != 0), sep=",")
#
# print(*(i for i in range(5)), sep=',')
#
# from functools import reduce
# n =5
# factorial = reduce(lambda x, y: x * y, range(1, n+1))
# print(factorial)
#
# z = reduce(lambda x,y :x*y,range(1,5))
# print(z)
#
# dict ={}
# for i in range(6):
#     dict[i] = i*i
# print(dict)
#
# d1 = {
#     'a':2,
#     'b':5
# }
# ans={i+i : j*5 for i,j in d1.items()}
# print(ans)
#
# m =[]
# for i in range(3):
#     m1 = []
#     for j in range(5):
#         m1.append(i*j)
#     m.append(m1)
# print(m)


# def user_input():
#     while True:
#         s = input()
#         if not s:
#             return
#         yield s
#
# for line in map(str.upper, user_input()):
#     print(line)

# def inputs():
#     while True:
#         string = input()
#         if not string:
#             return
#         yield string
#
# print(*(line.upper() for line in inputs()),sep='\n')

# a,s = 285345,0
# n = [int(x) for x in str(a)]
# for i in n:
#     if i %2 ==0:
#         s+=i
# print(s)

# word = sorted(list(set(input('enter words').split())))
# print(' '.join(word))

# word  = input().split()
# [word.remove(i) for i in word if word.count(i)>1]
# word.sort()
# print(" ".join(word))

# print(*(binary for binary in input().split(',') if int(binary,base=2)%5==0))
#
# data = input().split(',')
# data = [num for num in data if int(num, 2) % 5 == 0]
# print(','.join(data))
#
# data = input().split(',')
# data = list(filter(lambda i:int(i,2)%5==0,data))
# print(",".join(data))




# lst = [str(i) for i in range(15,25)]
# lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))
# print(",".join(lst))


# lst = []
#
# for i in range(20,30):
#     flag = 1
#     for j in str(i):          # every integer number i is converted into string
#         if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
#             flag = 0          # flag becomes zero if any odd digit found
#     if flag == 1:
#         lst.append(str(i))    # i is stored in list as string
#
# print(",".join(lst))


# data = input()
# l = sum(1 for i in data if i.islower())
# u = sum(1 for i in data if i.isupper())
# print(l ,u)

# a = input()
# print(sum(int(i*a) for i in range(1,5)))


#print(*(int(i)**2 for i in input().split(',') if int(i)%2!=0))

# def a(x:int,y:int)->'yeah':
#     return x+y
# print(a(5,4))


# lst = [str(int(i)**2) for i in input().split(',') if int(i)%2 !=0]
# print(",".join(lst))

# import re
# a = input('Enter passwords: ').split(',')
# pass_pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
# for i in a:
#     if pass_pattern.fullmatch(i):
#         print(i)

# lst = []
# while True:
#     s = input().split(',')
#     if not s[0]:                          # breaks for blank input
#         break
#     lst.append(tuple(s))
# lst.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))  # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
# print(lst)


# class MyGen():
#     def by_seven(self, n):
#         for i in range(0, int(n/7) + 1):
#             yield i * 7
# for i in MyGen().by_seven( int(input('Please enter a number... ')) ):
#     print(i)


# class Mul:
#     def multi(self,n):
#         for i in range(0,n):
#             if i % 2 == 0:
#                 yield i
#
# for i in Mul().multi(int(5)):
#     print(i)


