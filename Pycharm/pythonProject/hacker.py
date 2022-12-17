lst = list(range(2,101))
print(*(list(filter(lambda x:all(x%i for i in range(2, int(x*0.5)+1)), lst))),sep=',')


# def cap(s):
#     l = list(map(str,s.split(' ')))
#     l1 = []
#     for i in l:
#         l1.append(i.capitalize())
#     return ' '.join(l1)
# s = input()
# print(cap(s))

# def minion_game(string):
#     # your code goes here
#     # The Minion Game in Python - Hacker Rank Solution START
#     player1 = 0;
#     player2 = 0;
#     str_len = len(string)
#
#     for i in range(str_len):
#         if s[i] in "AEIOU":
#             player1 += (str_len) - i
#             print(i,player1)
#         else:
#             print('#',i, player1)
#             player2 += (str_len) - i
#
#     if player1 > player2:
#         print("Kevin", player1)
#     elif player1 < player2:
#         print("Stuart", player2)
#     elif player1 == player2:
#         print("Draw")
#     else:
#         print("Draw")
#     # The Minion Game in Python - Hacker Rank Solution END
#
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

# def merge_the_tools(string, k):
#     lst,c = [],0
#     for i in string:
#         c += 1
#         if i not in lst:
#             lst.append(i)
#         if c == k:
#             print(''.join(lst))
#             lst,c = [],0
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

# def print_formatted(number):
#     l1 = len(bin(number)[2:])
#
# for i in range(1, number + 1):
#     print(str(i).ljust(l1, ' '), end=" ")
# print(oct(i)[2:].rjust(l1, ' '), end=" ")
# print(((hex(i)[2:]).upper()).rjust(l1, ' '), end=" ")
# print(bin(i)[2:].rjust(l1, ' '), end=" ")
# print("")
# # String Formatting in Python - HackerRank Solution END
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# def print_formatted(number):
#
#     width = len("{0:b}".format(number))
#     for i in range(1, number + 1):
#         print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# for i in range(1,10):
#     print("{0:b}".format(i))

# d	for integers
# f	for floating point numbers
# b	for binary numbers
# o	for octal numbers
# x	for octal hexadecimal numbers
# s	for string
# e	for floating point in exponent format

# n= int(input())
# for i in range(n):
#     for j in range(n):
#         if i ==0 or j == 0 or j == n-1 or i == n-1:
#             print('# ',end='')
#         else:
#             print('  ', end='')
#     print(' ')

# n = 5
# print(*(print('*',end='') for i in range(n) for j in range(n) if i==0 or j==0))

# if __name__ == '__main__':
# e = input()
# el = set(map(int, input().split()))
# f = input()
# fl = set(map(int, input().split()))
# print(len(el.difference(fl)) + len(fl.difference(el)))
#     len_set = int(input())
#     storage = set(map(int, input().split()))
#     op_len = int(input())
#     for i in range(op_len):
#         operation = input().split()
#         if operation[0] == 'intersection_update':
#             temp_storage = set(map(int, input().split()))
#             storage.intersection_update(temp_storage)
#         elif operation[0] == 'update':
#             temp_storage = set(map(int, input().split()))
#             storage.update(temp_storage)
#         elif operation[0] == 'symmetric_difference_update':
#             temp_storage = set(map(int, input().split()))
#             storage.symmetric_difference_update(temp_storage)
#         elif operation[0] == 'difference_update':
#             temp_storage = set(map(int, input().split()))
#             storage.difference_update(temp_storage)
#         else:
#             assert False
#
#     print(sum(storage))
#
# _ = input()
# a = set(int(x) for x in input().split(' '))
#
# n = int(input())
# for _ in range(n):
#     op, _ = input().split(' ')
#     b = set(int(x) for x in input().split(' '))
#     if op == "update":
#         a |= b
#     elif op == "intersection_update":
#         a &= b
#     elif op == "difference_update":
#         a -= b
#     elif op == "symmetric_difference_update":
#         a ^= b
# print(sum(a))

# from functools import reduce

# print(*(i for i in range(0, 11) if i % 2 == 0))
# fact = reduce(lambda x, y: x * y, range(1, 4))
# print(fact)
# print(reduce(lambda acc,x: acc+x*2, [2,5,8]))
# f = lambda x: x * f(x - 1) if x > 1 else 1
# print(f(5))

# import itertools
# print(list(itertools.permutations([1, 2, 3])))

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     ans = sorted(set(arr))
#     print(ans[-2])


# x = int(input()) + 1
# y = int(input()) + 1
# z = int(input()) + 1
# n = int(input())
# ans = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if ((i + j + k) != n)]
# print(ans)

# lst = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     lst.append([name, score])
# sl = sorted(list(set([x[1] for x in lst])))
# lst2 =[]
# for i in lst:
#     if i[1] == sl[1]:
#         lst2.append(i[0])
# print(*(i for i in sorted(lst2)),sep='\n')

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     print(student_marks)
#     marks = student_marks[query_name]
#     print(marks)
#     avg = sum(marks) / len(marks)
#     print("%.2f" % avg)
# m =0
# for i in student_marks[query_name]:
#     m+=i
# c= m/3
# print("%.2f"% c)
# print('{0:f}'.format(c))
# print('*')
# d ={
#     'a' : [1,2,3]
# }
# print(d['a'])


# def l2d(lst):
#     result = { lst[i]:lst[i+1] for i in range(0,len(lst),2)}
#     return result
#
# lst = ['a',2,'b',4]
# print(l2d(lst))

# d = {str(i):i*2 for i in range(0,5)}
# print(d)

# def l2d(lst):
#     a = iter(lst)
#     result = dict(zip(a,a))
#     return result
#
# lst = ['a',2,'b',4]
# print(l2d(lst))

# a = ['Tests run: 1', ' Failures: 0', ' Errors: 0']
# # print(' '.join(a))
# d = {i.split(':')[0]: int(i.split(':')[1]) for i in a}
# print(d)

# test_string = '[Nikhil:1, Akshat:2, Akash:3]'
# d = {i.split(':')[0] : i.split(':')[1] for i in test_string[1:-1].split(',')}
# print(d)

# dict = {'a': 'Arthur', 'b': 'Belling'}
# l =[]
# [l.extend([k,v]) for k,v in dict.items()]
# print(l)

# lst = [int(i) for i in range(2,20)]
# # a = list(map(int,input()))
# num = list(filter(lambda x:all(x%j!=0 for j in range(2,int(x*0.5) + 1) ),lst))
# print(*num,sep=',')

# n = int(input('>'))
# def prime(n):
#     return all(n%i for i in range(2,int(n*0.5))) and n >1
# print('yes' if prime(n) else 'no')
# print(prime(n))


# no = '23'
# for x in range(0,len(no)):
#     rev = no[x:len(no)] + no[0:x]
#     print(rev)


# g = 'RainbowSixSiege'
# print(g[::])

# ---------------------


# n=int(input("Enter the number:"))
# n=str(n)
# n2=n.replace('0','5')
# n2=int(n2)
# print("Converted number:",n2)

# class Solution:
#     def binarysearch(self, arr, n, k):
#         l,h,m = 0,len(arr)-1,0
#         while l<=h:
#             m = (l+h)//2
#             if arr[m] < k:
#                 l = m+1
#             elif arr[m] > k:
#                 h = m-1
#             else:
#                 return m
#         return -1
#
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         arr = list(map(int, input().strip().split(' ')))
#         k = int(input())
#         ob = Solution()
#         print(ob.binarysearch(arr, n, k))

# Returns true if n is prime else false
# def prime(n):
# 	return all([n % j !=0 for j in range(2, int(n**0.5)+1)]) and n>1
#
# # Driver code
# n = 6
# if prime(n):
# 	print("Yes")
# else:
# 	print("No")

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     count = count_substring(string, sub_string)
#     print(count)

# S = input()
# print(any([char.isalnum() for char in S]))
# print(any([char.isalpha() for char in S]))
# print(any([char.isdigit() for char in S]))
# print(any([char.islower() for char in S]))
# print(any([char.isupper() for char in S]))

import textwrap


# thickness = int(input())  # This must be an odd number
# c = 'H'

# Top Cone
# replace  ______ To rjust |  ______ To  ljust
# for i in range(thickness):
#     print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
# replace ______ To center |  ______ To center
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
# replace ______ To center
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))

# Bottom Pillars
# replace ______ To center |  ______ To center
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
# replace ______ To rjust |  ______ To ljust |  ______ To rjust
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# if __name__ == '__main__':
#     N = int(input())
#     the_list = list()
#
#     for _ in range(N):
#         query = input().split()
#         if query[0] == "print":
#             print(the_list)
#         elif query[0] == "insert":
#             the_list.insert(int(query[1]), int(query[2]))
#         elif query[0] == "remove":
#             the_list.remove(int(query[1]))
#         elif query[0] == "append":
#             the_list.append(int(query[1]))
#         elif query[0] == "sort":
#             the_list = sorted(the_list)
#         elif query[0] == "pop":
#             the_list.pop()
#         elif query[0] == "reverse":
#             the_list.reverse()


# def missingCharacters(s):
#     lst = list('0123456789abcdefghijklmnopqrstuvwxyz')
#     for i in s:
#         if i in lst:
#             lst.remove(i)
#     return ''.join(sorted(lst))
#
# s = input()
# print(missingCharacters(s.lower()))

# def numCells(grid):
#     row = len(grid)
#     col = len(grid[0])
#     for i in grid:
#         for j in range(len(i)-1):
#             print(i[j] , i[j+1])
#
#
#
# grid_rows = int(input().strip())
# grid_columns = int(input().strip())
#
# grid = []
#
# for _ in range(grid_rows):
#     grid.append(list(map(int, input().rstrip().split())))
#
# result = numCells(grid)
# print(result)


# def numCells(grid):
#
#     grid = [list(grid) for grid in grid]
#     r = len(grid)
#     c = len(grid[0])
#     for i in range(r):
#         print(sorted(grid[i]))
#     for j in range(c):
#         for i in range(1,r):
#             if not grid[i-1][j]<= grid[i][j]:
#                 return 'NO'
#     return 'Yes'
# grid_rows = int(input().strip())
# grid_columns = int(input().strip())
#
# grid = []
#
# for _ in range(grid_rows):
#     grid.append(input())
#
# result = numCells(grid)
# print(result)
#
# n,lst = int(input('> ')),[]
# for i in range(n):
#     lst.append(list(map(int, input().split())))
# m = 0
# f = [i[0] for i in lst]
# l = [i[-1] for i in lst]
#
# print(f,l,d)


# from itertools import product
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# out = list(product(A,B))
# for i in out:
#     print(i, end=' ')


# from itertools import permutations
# s,k = input().split()
# words = list(permutations(s,int(k)))
# words = sorted(words, reverse=False)
# for word in words:
#     print(*word,sep='')

import operator

# def person_lister(f):
#     def inner(people):
#         print('2=',people)
#         return map(f, sorted(people, key=lambda x: int(x[2])))
#     print('2.1=')
#     return inner
#
# @person_lister
# def name_format(person):
#     print('3=',people)
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]# map accessed the fx 3 time thats why 3
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print('1=',people)
#     print(*name_format(people), sep='\n')

# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F

# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle


# def printDiagonal(lst):
#     # To print Primary Diagonal
#     print('Diagonal 1 - ', end="")
#     print([r[len(lst)-len(lst)] for i, r in enumerate(lst)])
#
#     print('Diagonal 2 - ', end="")
#     print([r[~i] for i, r in enumerate(lst)])
#     print([sum(i) for i in lst])
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# printDiagonal(lst)



# def printDiagonal(lst):
#
#     print('Diagonal 1 - ', end="")
#     print([lst[i][i] for i in range(len(lst))])
#
#     print('Diagonal 2 - ', end="")
#     print([lst[i][len(lst) - i - 1] for i in range(len(lst))])
#
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# printDiagonal(lst)



# import itertools
#
# mylist= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for a, b in itertools.combinations(mylist, 2):
#     compare(a, b)


# Python Implementation of the approach
# import itertools
#
# def Sub_Sequences(STR):
# 	combs = []
# 	for l in range(1, len(STR)+1):
# 		combs.append(list(itertools.combinations(STR, l)))
# 	for c in combs:
# 		for t in c:
# 			print (''.join(t), end =' ')

# Testing with driver code
# if __name__ == '__main__':
# 	Sub_Sequences('abc')

# Python3 code to demonstrate working of
# Get all substrings of string
# Using itertools.combinations()
# from itertools import combinations

# initializing string
# test_str = "Geeks"

# printing original string
# print("The original string is : " + str(test_str))

# Get all substrings of string
# Using itertools.combinations()
# res = [test_str[x:y] for x, y in combinations(
# 			range(len(test_str) + 1), r = 2)]

# printing result
# print("All substrings of string are : " + str(res))


from itertools import combinations

s = 'pik'

for i in range(1,len(s)+1):
    for j in combinations(s,i):
        print(j)

