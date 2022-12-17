# f = lambda x: 1 if x == 1 else x + f(x-1)
# n = int(input('>'))
# print(f(n))

# f = lambda x : x if len(str(x)) == 1 else x%10 + f(x//10)
# n = int(input('>'))
# print(f(n))









# f = lambda x:x[::-1] if x else ValueError
# n = input('>')
# print(f(n))

# f = lambda x:x if len(x) ==1 else f(x[1:])+x[0]
# n = input('>')
# print(f(n))




def fx(n):
    if n==0:
        return
    print(n)
    fx(n-1)
    print(n)
fx(3)
