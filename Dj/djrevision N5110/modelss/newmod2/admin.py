from django.contrib import admin
from newmod2.models import Customer,Product,Order,LineItem
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(LineItem)
