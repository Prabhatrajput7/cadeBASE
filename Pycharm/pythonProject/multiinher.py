class Ubi:
    def sign(self):
        print('login')
class Siege(Ubi):
    def __init__(self,username,age):
        self.username = username
        self.age = age
    def displayy(self):
        print(f'Your username and age:: {self.username} & {self.age}')
class Ass(Ubi):
    def __init__(self,username,passw):
        self.username = username
        self.passw = passw
    def displayy(self):
        print(f'Your username and password: {self.username} & {self.passw}')

class Assassins(Siege,Ass):
    def __init__(self,username,age,passw):
        Siege.__init__(self, username, age)
        Ass.__init__(self,username,passw)

a1 = Assassins('rocky',50,23)
a1.displayy()



