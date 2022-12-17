# n = 5
# lst = list(map(chr,range(97,123)))
# print(lst)
# i=0
# print(lst[n-i:n])
# lst2 = lst[n-1::-1] + lst[1:n]
#print(lst2)
# m = len(','.join(lst2))
#
# for i in range(1,n):
#     print('-'.join(lst[n-1:n-i:-1]+lst[n-i:n]).center(m,'*'))
# for i in range(n,0,-1):
#     print('-'.join(lst[n-1:n-i:-1]+lst[n-i:n]).center(m,'*'))

# for i in range(5):
#     print('*' * (i + 1))
#
# n = 5
# for i in range(n):
#     print(' ' * (n - i - 1) + '*' * (i + 1))
#
# n1 = 5
# for i in range(n1):
#     print(' ' * (n1 - i - 1) + '*' * ((2 * i) + 1))
#
# n2 = 5
# for i in range(n2,0,-1):
#     print('*'*i)

# n=3
# for i in range(n):
#     print(' '* ((n-i)-1) + '*'*(2*(i+1)-1))
#
# for i in range(n):
#     print(' ' * (i + 1) + '*' * ((2 * ((n - 1) - i)) - 1))

#
# n3 = 5
# for i in range(n3,0,-1):
#     print(' '*(n2-i) + '*'*i)

# n4 = 5
# for i in range(n4,0,-1):
#     print(' ' * (n4-i) + '*' * ((2*i)-1))


# n1 = 3
# w = 2*n1-1
# for i in range(n1):
#     print(str('*'*((2*i)+1)).center(w,'-'))

# l = [1,2,3,4,5,6,7,8,9]
#    +0,+1,+2,+3,+4,+,5+,6,+7,+8
#    -9,-8,-7-,6-,5,-4,-3-,2-,1
# print(l[5::-1])
# print(l[:5:-1])
# print(l[2:-9:-1])
# def rangoli(n):
#     l1 = list(map(chr, range(97, 123)))
#     print(l1)
#     #print(l1[n - 1::-1])
#     #print(l1[1:n])
#     x = l1[n - 1::-1] + l1[1:n]
#     #print(x)
#     #print('-'.join(x))
#     mid = len('-'.join(x))
#     #print(mid)
#     for i in range(1, n):
#         print(l1[n - 1:n - i:-1])
#         print(l1[n - i:n])
#         print('-'.join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(mid, '-'))
#     for i in range(n, 0, -1):
#         print('-'.join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(mid, '-'))
# rangoli(5)

# Python program to
# print Diamond shape

# Function to print
# Diamond shape
# def Diamond(rows):
#     n = 0
#     for i in range(1, rows + 1):
#         # loop to print spaces
#         for j in range(1, (rows - i) + 1):
#             print(end=" ")
#
#         # loop to print star
#         while n != (2 * i - 1):
#             print("*", end="")
#             n = n + 1
#         n = 0
#
#         # line break
#         print()
#
#     k = 1
#     n = 1
#     for i in range(1, rows):
#         # loop to print spaces
#         for j in range(1, k + 1):
#             print(end=" ")
#         k = k + 1
#
#         # loop to print star
#         while n <= (2 * (rows - i) - 1):
#             print("*", end="")
#             n = n + 1
#         n = 1
#         print()
#
#
# # Driver Code
# # number of rows input
# rows = 5
# Diamond(rows)

#
n = 4
for i in range(n):
    print(' ' * (n - i - 1) + '*' * ((2 * i) + 1))
for i in range(n):
    print(' ' * (i + 1) + '*' * ((2 * ((n - 1) - i)) - 1))


# l = list(range(10,100))
# print(*(list(filter(lambda x:all(x%i for i in range(2,(x//2)+1)),l))),sep=',')

n = 4
for i in range(n):
    print(' '* (n-1-i) + '*'*((2*i)+1))
for i in range(n-1,0,-1):
    print(' '* (n-i) + '*'*((2*i)-1))
# n = 5
# for i in range(n):
#     print('*'*(i+1)+' '*(n-i))


# def rangoli(n):
#     l1 = list(map(chr, range(97, 123)))
#     x = l1[n - 1::-1] + l1[1:n]
#     mid = len('-'.join(x))
#     for i in range(1, n):
#         print('-'.join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(mid, '-'))
#     for i in range(n, 0, -1):
#         print('-'.join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(mid, '-'))
# rangoli(5)

# n = 4
# for i in range(4):
#     print(' '*(n-i-1) + '*'*((2*i)+1))
# for i in range(4):
#     print(' '*(i+1) + '*'*((2*(n-1-i))-1))

# n = 4
# for i in range(n):
#     print(' '*(n-i-1)+ '*'*(i+1))

# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print(str('.|.' * i).center(M, '-'))
# print('WELCOME'.center(M, '-'))
# for i in range(N-2, -1, -2):
#     print(str('.|.' * i).center(M, '-'))


# a = 'ss'
# print(a.center(7,'*'))