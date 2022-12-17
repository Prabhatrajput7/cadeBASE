class A:
    leave = 10

    @classmethod
    def change(cls, new):
        cls.leave = new

a =A()
a.change(15)
print(a.__dict__)
print(A.leave)
