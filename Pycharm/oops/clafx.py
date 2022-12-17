"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Sale:

    def __init__(self, amount):
        self.amount = amount


def find_total(sales):
    total = 0

    for sale in sales:
        # print("New Sale...")
        # print(sale.amount)
        total += sale.amount

    return total


january_sales = [Sale(400), Sale(345), Sale(45)]

print(find_total(january_sales))
print(january_sales[0].amount)
# s1,s2,s3 = Sale(400), Sale(345), Sale(45)
# print(sum(s.amount for s in [s1,s2,s3]))
