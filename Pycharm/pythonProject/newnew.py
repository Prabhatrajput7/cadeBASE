class GeeksforGeeks(object):
    def __str__(self):
        return "GeeksforGeeks"
# class returning object
# of different class
class Geek(object):
    def __new__(cls):
        return super(Geek,cls).__new__(cls)

    def __init__(self):
        print("Inside init")

print(Geek())