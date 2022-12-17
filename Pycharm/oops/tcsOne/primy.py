

# def prime(n):
#     if type(n) == int:
#         return all(n % i for i in range(2, int(n / 2) + 1)) and n > 1
#
# def totalprime(lst):
#     # l =[]
#     # for i in lst:
#     #     if prime(i):
#     #         l.append(i)
#     # l = list((filter(lambda x:all(x%i!=0 for i in range(2, int(x/2)+1)),lst)))
#     # return l
#
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,14]
# print(totalprime(lst))




# fact = lambda x:1 if x<=1 else x*fact(x-1)
# def boxes(a,b):
#     l1 = []
#     for i in range(1,a+1):
#         s = fact(i)+b
#         l1.append(s)
#     l2 = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x / 2) + 1)), l1))
#     return len(l2)
#
# a,b = 3,2
# print(boxes(a,b))

#