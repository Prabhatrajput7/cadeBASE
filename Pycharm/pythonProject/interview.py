# i = 5
#
# def fx(arg=i):
#     print(arg)
#     return arg
#
# i = 6
# print(fx())

# def lst(a):
#     l = []
#     l.append(a)
#     return l
#
# print(lst(1))
# print(lst(2))
# print(lst(3))


s= 'viggi'
s1 = [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
print(s1)








