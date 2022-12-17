class Ubi:
    def __init__(self,email):
        self.email = email
    def sign(self):
        return f'login'
class Siege(Ubi):
    def __init__(self,username,passw,email):
        #Ubi.__init__(self,email) or
        super().__init__(email)
        self.username = username
        self.passw = passw
        self.d = {
            'name' : 'Jack',
            'age' : 36
        }

    def displayy(self):
        print(f'Your details: {self.username}, {self.passw} & {self.email} {Ubi.sign(self)}')
    def __len__(self):
        return 5
    def __del__(self):
        print('delete')
    def __str__(self):
        return 'string'
    def __call__(self):
        return 'calling'
    def __getitem__(self, item):
        return self.d[item]

s1 = Siege('l1','**','li@')
print(s1.displayy())
print(len(s1))
print(str(s1))
print('**')
print(s1())
print(s1['name'])
del s1
