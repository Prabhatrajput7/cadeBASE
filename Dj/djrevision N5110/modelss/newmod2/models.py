from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateField(null=False)
    shipped_date = models.DateField(null=True)
    delivered_date = models.DateField(null=True)
    coupon_code = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.order_date)

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return str(self.quantity)