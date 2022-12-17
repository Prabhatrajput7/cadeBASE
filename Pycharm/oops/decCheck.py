from functools import wraps

def one(fx):
    @wraps(fx)
    def fx1(*args,**kwargs):
        fx(*args,**kwargs)
    return fx1

def two(fxx):
    @wraps(fxx)
    def fxx1(*args,**kwargs):
        fxx(*args,**kwargs)
    return fxx1

def check():
    print('CHECK')


ch = one(two(check))
ch()

# @one
# @two
# def check():
#     print('CHECK')
#
#
# a = check
# a()
# print(a.__name__)