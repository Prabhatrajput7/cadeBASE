from django.db import models
from django.forms import CharField

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRec(models.Model):
    webpg = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return str(self.date)