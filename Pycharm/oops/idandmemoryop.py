a = 275
b = 275
c = 5
d = c
l1 = [1]
l2 = [2]
l3 = l2
print(a is b)
print(c is d)
print(l1 is l2)
print(l2 is l3)
# -5 to 256 same reference for memory optimization but pycharn can go beyond that
# string are immutable so the all usessame reference
"""
a = 'hi'
b = 'hi'

The environment in which you run the code affects how string interning works.
"""

#values are passed by reference and list reference remail same

# lst = [1,2,3]
# print('one', id(lst))

# def checkid(l):
#     return [l[i]*2 for i in range(len(l))]

# l1 = checkid(lst)
# print(id(l1))


# lst = [-7,-1,-2]
# print(lst)
# print([abs(i) for i in lst])
# # def positive(lst):
# #     for i in range(len(lst)):
# #         lst[i]  = abs(lst[i])
# # positive(lst)
# print(lst)
# lst.sort()
# print(lst)




