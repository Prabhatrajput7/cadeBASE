


# def numm(n):
#     l = []
#     for i in range(1,int(n//2)+1):
#         if n%i ==0:
#             c+=1
#             l.append(i)
#     for j in range(1,max(l)):
#
# print(numm(8))

# def count(n):
#     dp = dict()
#     dp[0] = 0
#     dp[1] = 1
#     if n not in dp:
#         dp[n] = 1 + min(n % 2 + count(n // 2), n % 3 + count(n // 3))
#     return dp[n]
# N = 6
# print(str(count(N)))

import itertools


def Sub_Sequences(STR):
    combs = []
    for l in range(1, len(STR) + 1):
        combs.append(list(itertools.combinations(STR, l)))
    l,l1 = [],[]
    for c in combs:
        for t in c:
            l.append(t)
    for i in l:
        if len(i)==len(STR)-2:
            l1.append(i)
    return len(l1)
if __name__ == '__main__':
    s = input('>')
    Sub_Sequences(s)
