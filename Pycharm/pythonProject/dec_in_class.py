# class Game:
#     # a = 50
#     def __init__(self, name='K4', age=23, k=2):
#         self.name = name
#         self.age = age
#         self.k = k
#
#     def printt(self):
#         print(f'Given details: {self.name} - {self.age}')
#
#     @classmethod
#     def addingthings(cls,n1,n2):
#         # cls.a = n1+n2
#         return n1 + n2
#
#     @classmethod
#     def addingname(cls,n1,n2):
#         return cls('acog',n1 + n2)
#
#     @classmethod
#     def givingname(cls, name,n1, n2,n3):
#         return cls(name, n1 + n2,n3)
#
#     @staticmethod
#     def addingusingS(n1,n2):
#         return n1 + n2
#
# g1 = Game('light', 23,0)
# g1.printt()
# # g11 = Game.addingusingS(10,10)
# # print(g11.age)
# print(g1.addingthings(2,5)) #return n1 + n2
# g2 = Game.addingname(3,4) #for classmethod we dont need to create a obj for class
# print(g2.name)
# print(g2.age)
# g3 = Game.givingname('lost',3,4,5)
# print(Game.givingname('lost',3,4,5))
# print(g3.name)
# print(g3.age)
# print(Game.addingusingS(6,1)) #for staticmethod we dont need to create a obj for class













class CHK:

    def __init__(self,a,b):
        print('Init called')
        self.a = a
        self.b = b

    def display(self):
        print(self.a ,self.b)

    @classmethod
    def setup(cls,a,b):
        return cls(a,b)

c = CHK(1,2)
c.display()
c1 = CHK.setup(2,4)
c1.display()












