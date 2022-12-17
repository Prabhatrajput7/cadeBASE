# total = []
# def testt():
#     total.append(1)
#     print(total)
#
# testt()
#

# from functools import reduce
# print(reduce(lambda acc,x: acc+x, [2,0,8]))
#
# def redd(acc,item):
#     return acc + item
# print(reduce(redd,[12,2],0))



# lst = [12,5,4]
# print(sorted(lst))
# print(lst)

#sort dont return obj

# for i in range(5):
#     print('start')
#     for j in range(5):
#         print('j')
#         for k in range(5):
#             if i == k:
#                 break
#         print('j2')
#     print('start2')

# class Myr:
#     def __init__(self,s,e):
#         self.s = s
#         self.e = e
#
#     def __iter__(self):
#         print('*')
#         return self
#
#     def __next__(self):
#         if self.s>=self.e:
#             print('**')
#             raise StopIteration
#         print('next')
#         c = self.s
#         self.s += 1
#         return c
#
# n = Myr(1,10)
#
# # for i in n:
# #     print(i)
#
# print(next(n))


class A:
    def __init__(self,a):
        self.a =a

    def __repr__(self):
        return self.a

a = A('hi')
print(a)

# a = 5
# b = 6
# assert a == b, 'not'






# class Check:
#     def __init__(self,a):
#         self.a =a
#
#     def printt(self):
#         print(self.a)
#
# c = Check([1,23,2])
# c.printt()



# a = 100_000_000
# b = 100_000
# print(f'{a+b:,}')




# p = P()
# fname = 'hey'
# p.fname = 'hey'
# setattr(p,p.fname,'hello')
# print(p.fname)
#
# setattr(p,'hi','hello')
# print(p.hi)

# setattr(p,fname,'two')
# get = getattr(p,fname)
# print(p.hey)
# print(get)

# class SG:
#     pass
#
# sg = SG()

# d = {'name':'vigil','surname':'rajput'}
# for i,j in d.items():
#     print('*',i,j)
#     sett = setattr(sg,i,j)
# print(sg.name)
#
# for i in d:
#     print('3',i)
#     print(getattr(sg,i))

# l1 =[1,2]
# l2 = [3,4]
# z =zip(l1,l2)
# a1 = [(1,2),(3,4)]
# print(list(zip(*a1)))
# z = [(1, 2), (3, 4), (5, 6), (7, 8)] # Some output of zip() function
# unzip = lambda z: list(zip(*z))
# print(unzip(z))


# def asum(a,b):
#     return a+b

# d = {
#     'vigil':{
#         'nickname':'viggy',
#         'age':5,
#         'owner':'Rajput Family'
#     }
# }
#
# for i,j in d.items():
#     print(i,j.get('age'))

from functools import  reduce
print(reduce(lambda acc,x: acc+x, [2,5,8]))