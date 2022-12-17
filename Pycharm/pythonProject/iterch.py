class MyNumbers:
    def __iter__(self):
        print('iter')
        self.a = 1
        self.b = 5
        return self

    # def __next__(self):
    #     x = self.a
    #     y = self.b
    #     yield x
    #     self.a += 1
    #     # return y

    def __next__(self):
        for i in range(5):
            x = self.a
            yield x
            self.a +=1


myclass = MyNumbers()
myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

for i in next(myiter):
    print(i)