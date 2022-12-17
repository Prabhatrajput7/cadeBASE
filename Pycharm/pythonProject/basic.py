# a, b = 10, 20
# # Copy value of a in min if a < b else copy b
# min = a if a < b else b
# print(min)

# for count, i in enumerate(list(range(10))):
#     print(count,i)

# def arg(*args,**kwargs): # rule parameter args default para krwags ex(name,*agrs,i=4,**krwags)
#     t = 0
#     for i in kwargs.values():
#         t += i
#     return sum(args) + t
# print(arg(10,5,num = 5, num1 = 10))

# test_dict = {'Gfg': 6, 'is': 7, 'best': 9, 'for': 8, 'geeks': 11}
# print("The original dictionary is : ", test_dict)
# i, j = 8, 12
# res = dict()
# for key, val in test_dict.items():
#     if int(val) >= i and int(val) <= j:
#         res[key] = val
# print("The extracted dictionary : " ,res)

# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal" Parent local
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()
# non local take parent variable scope

#a = 'heloooo'
# if ((n:=len(a)) < 10): #3.8
#     print(f'small length {n}')
# while (len(a) > 1):
#     print(len(a))
#     a = a[:-1]
# print(a)


# l = list(range(1,20))
# c = list(map(chr,range(65,95)))
#
# z = zip(l,c)
# for i,j in z:
#     print(i)