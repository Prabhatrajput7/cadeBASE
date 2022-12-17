# n = 10
# coins = [2, 4, 3]
# def count_no_of_ways(coins, n):
#     table = [0 for i in range(n + 1)]
#     table[0] = 1
#     for coin in coins:
#         for i in range(coin, n + 1):
#             table[i] += table[i - coin]
#     return table[n]
# print(count_no_of_ways(coins, n))


# print(list(enumerate('python')))

# a =0
# for i in range(10):
#     if  i ==2:
#         pass
#     else:
#         a =i
# print(a)

# class S:
#     def __init__(self,s):
#         self.s = s
#
#     def area(self):
#         return self.s **2
#
# class C(S):
#
#     def sa(self):
#         a = super().area()
#         return 6*a
#
# print(C(6).sa())

# l = ['1','2','15','-7','300']
# print(sorted(l))

# l = ['r','m','','','','t']
# i = 0
# while i<len(l):
#     if len(l[i])==0:
#         del l[i]
#     i+=1
#
# print(l)

# import threading, queue, time
#
# q = queue.Queue()
#
# for i in [3,2,1]:
#     def f():
#         time.sleep(i)
#         q.put(i)
#     threading.Thread(target=f).start()
# print(q.get())

# def ab(a,b):
#     a+=1
#     b.append(1)
#
# a,b = 0,[]
# ab(a,b)
# print(a,b)
request = 'ap/ambassador'

is_ambassador = 'api/ambassador' in request
print(is_ambassador)

# def ch(lst):
#     r ={}
#     for i in lst:
#         b=r
#         for w in i.split(' '):
#             if not b.get(w):
#                 b[w] ={}
#             b = b[w]
#     return r
#
#
#
# print(ch(['hello world','hello there']))

# def longg(s):
#     char = set()
#     l = 0
#     res = 0
#     for i in range(len(s)):
#         while s[i] in char:
#             char.remove(s[l])
#             l+=1
#         char.add(s[i])
#         res = max(res, i-l+1)
#     return res
#
# s = 'geekforgeeks'
# print(longg(s))

# i = j =[3]
# i+=j
# print(i,j)
#
# print([3]+[3])