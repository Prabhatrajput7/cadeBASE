def check(fx):
    def wrapp(*args,**kwargs):
        return fx(*args,**kwargs)
    return wrapp

# @check
def cc(za):
    print(za)

a = check(cc)
a('za')