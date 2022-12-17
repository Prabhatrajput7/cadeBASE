class Pets:
    #animals = []
    def __init__(self, animals):
        self.animals = animals
        print('animals ',self.animals)
    def walk(self):
        for animal in self.animals:
            print(animal.wlk())

    def hello(self):
        return 'hi'
class Cat:
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def wlk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'
# 1 Add nother Cat
class Micheal(Cat):
    def sing(self, sounds):
        return f'{sounds}'
# 2 Create a list of all of the pets (create 3 cat instances from the above)
animal_1 = Simon("Simon", 14)
animal_2 = Sally(name="Sally", age=15)
animal_3 = Micheal(name="Micheal", age=11)
my_cats = [animal_1, animal_2, animal_3]
# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
# for i in my_cats:
#     print(i.wlk())
# 4 Output all of the cats walking using the my_pets instance
# my_pets.walk()

#animals list contains the objects you made using
# cat class so when you are calling for animal.walk it will call cat class function

"""
When you create a list of the objects, you can think of the list as holding the entire object.

Simon('Simon', 4) creates a new object and returns a reference to it. 
Putting this in the list means that now list item [0] refers to this object.

The Pets class defines its own .walk() method. 
This method iterates through the animals list and calls the .walk() method for each animal. 
Yes, because all the derived classes derive from Cat, 
that means each of those objects has a .walk() method of their own that they inherited from Cat. 
The fact that it's being called from the .walk() method in Pets is only a coincidence. 
The method can be called on those objects no matter where they are.
"""