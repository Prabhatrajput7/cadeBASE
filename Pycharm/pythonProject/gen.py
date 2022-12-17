# def fib(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b
# x = fib(5)
# print(next(x))
# print(x.__next__())
# print(next(x))
# print(x.__next__())
# print(next(x))

# Here is an example generator which calculates fibonacci numbers:
# generator version
def fib(number):
    a =  0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(5):
    print(x)



# def fib2(number):
#     a =  0
#     b = 1
#     result = []
#     for i in range(number):
#         result.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     return result
#
# print(fib2(5))

# from time import time
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper
#
# @performance
# def long_time():
#     print('1')
#     for i in range(100000):
#         i*5
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(100000)):
#         i*5
# long_time()
# long_time2()




# from time import time
#
# def checktime(fx):
#     def check():
#         t1 = time()
#         result = fx()
#         t2 = time()
#         print(f'{t2-t1}')
#         return result
#     return check
#
# @checktime
# def ttime():
#     for i in range(1000000):
#         i*5
# ttime()
# d= {'a':{12: 14,15:17},
#     'b':{12:12}}
#
# def aa(*args):
#     print(args[0]['a'])
#
# aa(d)




# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       iterator*5
#       next(iterator)
#     except StopIteration:
#       break
#
#
# class MyGen:
#     current = 0
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration
#
#     def __iter__(self):
#         return self.first


# lst =[1,2,3]
# a = iter(lst)
# print(next(a))
# print(next(a))