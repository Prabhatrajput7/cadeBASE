class Temp:
    def __init__(self, temperature):
        self.temp = temperature
    def check(self):
        if self.temp > 100.4:
            print("The patient has a fever")
        else:
            print("The patient doesn't have a fever")


t = Temp(500)
# t.check()
# Temp(500).check()
# Temp.check(t)
# Temp.check(Temp(500))
# Temp(500).check()
# print(Temp(500).check())