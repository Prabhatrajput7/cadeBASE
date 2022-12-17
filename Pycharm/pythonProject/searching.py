# def linear(m, m1):
#     for i in range(len(m)):
#         if m[i] == int(m1):
#             return f'{int(m1)} Match at index {i+1}'
# n = [4, 5, 6, 7, 8, 9]
# n1 = input('>>')
# print(linear(n, n1))

# def binary(arr,num):
#     l,h,m = 0, len(arr)-1,0
#     while l<=h:
#         m = (l+h)//2
#         print('******')
#         print(m,arr[m])
#         if arr[m] < num:
#             print('******')
#             print(m, arr[m])
#             l = m+1
#         elif arr[m] > num:
#             print('******')
#             print(m, arr[m])
#             h = m-1
#         else:
#             return m
#     return False
# arr = sorted(list(map(int, input().split())))
# print(arr)
# num = int(input('>'))
# print(binary(arr,num))













#O(1) and O(n)
# def ln(a,n):
#     for i in range(len(a)):
#         if a[i] == n:
#             return f'Found {n} at index {i} and position {i+1}'
#     return f'not found'
# lst = list(map(int,input().split(' ')))
# n = int(input('>'))
# print(ln(lst,n))

#l using rec

# def ln(a,n,s,e):
#     if s>e:
#         return -1
#     elif a[s] == n:
#         return s
#     elif a[e] == n:
#         return e
#     else:
#         return ln(a,n,s+1,e-1)
# lst = list(map(int,input().split(' ')))
# n = int(input('>'))
# s,e=0,len(lst)-1
# if ln(lst,n,s,e) != -1:
#     print(f'founD at {ln(lst,n,s,e)}')
# else:
#     print('nf')


#O(1) & O(logn)
#b

# def bin(a,n):
#     s,e = 0,len(a)-1
#     while s<=e:
#         m = (s + e) // 2
#         if a[m] == n:
#             return True
#         elif a[m] < n:
#             s = m+1
#         else:
#             e = m-1
#     return False
#
# arr = sorted(list(map(int, input().split())))
# print(arr)
# num = int(input('>'))
# print(bin(arr,num))



#b using rec


# def bin(a,n,s,e,m):
#     if s>e:
#         return False
#     if a[m] == n:
#         return True
#     elif a[m] < n:
#         return bin(arr,n,m+1,e,((s+e)//2))
#     else:
#         return bin(arr, n, s, m-1, ((s + e) // 2))
#
# arr = sorted(list(map(int, input().split())))
# print(arr)
# num = int(input('>'))
# s,e=0,len(arr)-1
# m = (s+e)//2
# print(bin(arr,num,s,e,m))