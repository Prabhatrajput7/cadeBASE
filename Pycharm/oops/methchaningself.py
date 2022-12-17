class Pizza:

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self #returing self means return the obj itself in this case its pizza

    def display_toppings(self):
        print("This Pizza has:")
        for topping in self.toppings:
            print(topping.capitalize())

pizza = Pizza()
pizza.add_topping("mushrooms").add_topping("olives").add_topping("chicken").display_toppings()
pizza2 = Pizza()
pizza2.add_topping("mushrooms").add_topping("olives").add_topping("chicken").display_toppings()
print(id(pizza), id(pizza2))
print(pizza == pizza2)

"""
pizza.add_topping("mushrooms") \
    .add_topping("olives") \
    .add_topping("chicken") \
    .display_toppings()
"""

