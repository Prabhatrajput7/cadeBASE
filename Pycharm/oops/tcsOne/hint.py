# l,lst = [],[1,2,3,4]
# def prime(n):
#     if type(n) == int:
#         return all(n%i for i in range(2,int(n/2)+1)) and n >1
#         # return all([(n % j) for j in range(2, int(n ** 0.5) + 1)]) and n > 1
# for i in lst:
#     if prime(i):
#         print(i)
#         l.append(i)

def amstrong(num1, num2):
    lst = []
    for i in range(num1, num2):
        if len(str(i)) == 3:
            if sum(int(i) ** 3 for i in str(i)) == i:
                lst.append(i)
        elif len(str(i)) == 4:
            if sum(int(i) ** 4 for i in str(i)) == i:
                lst.append(i)
        else:
            pass
    return lst

print(amstrong(15,250))

# def amstrong(num1, num2):
#     lst = []
#     for i in range(num1, num2):
#         if sum(int(i) ** 3 for i in str(i)) == i and i > 100:
#             lst.append(i)
#     return lst