
# str = input('enter a string- ')
# if not str[0].isupper() and str[-1] != '.':
#     print('missing')
# else:
#     print('fine')

#print(f' he\'s ')

#print("We are the so-called \"Vikings\" from the north.")

# list = ['abc','def',1,2,3,4]
# list1 = [10,9,8]
# list[0] = 'xyz'
# print(list)
#
# list.insert(1,'prq')
# print(list)
#
# list.extend(list1)
# print(list)
#
# list.remove('def')
# print(list)
#
# list.pop(1)
# list.pop()
# print(list)
#
# del list[1]
# del list1
#
# print(list1)
#
# list.clear()
# print(list)

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# n = 5
# table = [x*n for x in range(1,11) if x % 2 ==0 ]
# print(table)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)
#
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# def myfunc(n):
#   return abs(n - 100)
# thislist = [100, 50, 65, 82, 23]
# thisis = [500,200]
# thisis.sort(key = myfunc)
# print(thisis)
# #
# L = ["cccc", "b", "dd", "aaa"]
# print("Sort with len :", sorted(L, key=len))
#
# L.sort(key=len)
# print(L)

# thistuple = ("apple",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# l = list[1,2,3]
# t = tuple((1,2,3))

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)


# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

#Both union() and update() will exclude any duplicate items.

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
# for i in picture:
#     for j in i:
#         if j == 1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print(' ')
