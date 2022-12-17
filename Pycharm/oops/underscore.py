class One:
    def __init__(self,one):
        self._one = one
    def __str__(self):
        return 'str'
    def __repr__(self):
        return 'repr'
    def __ch(self):
        return 'ch'

o = One('one')
print(o._one)
o._one = 'two'
print(o._one)
print(o)
print(o._One__ch())

# print(One.__ch())


