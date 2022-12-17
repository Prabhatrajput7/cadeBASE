from django.db import models

# Create your models here.
class ProxyCheck(models.Model):

    choice = (
        ('seller','Seller'),
        ('customer','Customer'),
    )

    type = models.CharField(choices=choice, default='customer',max_length=100)
    addon = models.DateField(auto_now=True)

class Sellermodel(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(type='seller')

class Seller(ProxyCheck):
    objects = Sellermodel()
    class Meta:
        proxy = True

class Customermodel(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(type='customer')

class Customer(ProxyCheck):
    objects = Customermodel()
    class Meta:
        proxy = True



class Product(models.Model):

    pet = [
        ('dog','Dog'),
        ('cat','cat'),
    ]
    name = models.CharField(max_length=10)
    pet = models.CharField(choices=pet, max_length=10,blank=True,null=True)

    @classmethod #Product.cname('nike','dog')
    def cname(cls,name,pet):
        cls.objects.create(name=name,pet=pet)
    
    def __str__(self):
        return self.name

class R6update(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_del=False)


class R6(models.Model):
    op = models.CharField(max_length=100)
    speed = models.IntegerField()
    side = models.CharField(max_length=100)
    is_del = models.BooleanField(null= True)

    objects = R6update()

    def __str__(self):
        return self.op

##########################################

class FFProduct(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    price = models.IntegerField(null=False)

class Order(models.Model):
    order_id = models.IntegerField(null=True)
    products = models.ManyToManyField(FFProduct, through='LineItem')

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(FFProduct, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=False)     


"""
a = LineItem.objects.annotate(cnt = F('product__price')*F('quantity'))

In [16]: for i in a:
    ...:     print(i.cnt)
    ...: 
1000
1000
1000
"""