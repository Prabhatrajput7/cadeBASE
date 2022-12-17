from pyexpat import model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=15)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    tname = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.tname

from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='posts', null=True, blank=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('thx')

