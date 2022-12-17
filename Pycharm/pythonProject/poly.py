class Ubi:
    def sign(self):
        print('login')
    def displayy(self):
        print('checking UBI')
class Siege(Ubi):
    def __init__(self,username,passw):
        self.username = username
        self.passw = passw
    def displayy(self):
        Ubi.displayy(self)
        Ubi.sign(self)
        print(f'Your username and password: {self.username} & {self.passw}')

class Ass(Ubi):
    def __init__(self,username,passw):
        self.username = username
        self.passw = passw
    def displayy(self):
        print(f'Your username and password: {self.username} & {self.passw}')

s1 = Siege('l1','**')
print(dir(s1)) #what it has access too
a1 = Ass('ass','***')

def gaming(chare):
    chare.displayy()

gaming(s1)
gaming(a1)

for i in [s1,a1]:
    i.displayy()
