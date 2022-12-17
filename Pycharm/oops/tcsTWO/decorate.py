def deco(func):
    def inner(*args, **kwdargs):
        return func(*args, **kwdargs)
    print("{} Decorator".format(func.__name__))
    return inner


@deco
def joinString(*args):
    s = ""
    for i in args:
        s+=i
    return s

@deco
def findTotal(*args):
    return sum(args)


@deco
def average(*args):
    return sum(args)/len(args)


if __name__ == '__main__':
    strInput = list(map(str, input().split()))
    numInput = list(map(int, input().split()))
    print('Joining Strings...')
    print(joinString(*strInput))
    print('Calculating Average...')
    print(average(*numInput))
    print('Calculating Total...')
    print(findTotal(*numInput))