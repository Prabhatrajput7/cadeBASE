from pydoc import describe
from pyexpat import model
from tkinter import PhotoImage
from django.db import models
from django.forms import ImageField

# Create your models here.

class Manufacture(models.Model):
    name = models.CharField(max_length=20)
    loc = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=20)
    desc = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    ship_coast = models.FloatField()
    quality = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name