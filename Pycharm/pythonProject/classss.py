class Game:
    speed = '3-Speed'
    def __init__(self,name='K4',age=23):
        if age>18:
            self.name = name
            self.age = age

    def armor(self,ar):
        self.ar = ar

    def printt(self):
        print(f'Given details: {self.name} - {self.age} - {self.speed} - {self.ar}')

g1 = Game('light',23)
#g1.name = 'kia'
g1.weapon = 'C7e'
print(g1.name,g1.age,g1.weapon,g1.speed)
g1.armor('3')
g1.printt()
#help(g1)
