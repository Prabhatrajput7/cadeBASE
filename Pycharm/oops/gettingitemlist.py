class Bookshelf:

    def __init__(self):
        self.content = [[],
                        [],
                        []]

    def add_book(self, book, location):
        self.content[location].append(book)

    def take_book(self, book, location):
        self.content[location].remove(book)

    def __getitem__(self, location):
        return self.content[location]


my_bookshelf = Bookshelf()

my_bookshelf.add_book("Les Miserables", 0)
my_bookshelf.add_book("Pride and Prejudice", 0)
my_bookshelf.add_book("Frankenstein", 0)

my_bookshelf.add_book("Sense and Sensibility", 1)
my_bookshelf.add_book("Jane Eyre", 1)
my_bookshelf.add_book("The Little Prince", 1)

my_bookshelf.add_book("Moby Dick", 2)
my_bookshelf.add_book("The Adventures of Huckleberry Finn", 2)
my_bookshelf.add_book("Dracula", 2)

print(my_bookshelf[0])
print(my_bookshelf[1])
print(my_bookshelf[2])


lst = [['j'],[],[]]
lst[0][0]='hi'
print(lst)