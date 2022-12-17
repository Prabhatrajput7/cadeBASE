def outer(x, y):

    def inner1():
        return x+y

    def inner2():
        return inner1()

    return inner2


f = outer(10, 25)

print(f())