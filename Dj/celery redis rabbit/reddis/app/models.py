from django.db import models

# Create your models here.

class Attack(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    gadget = models.CharField(max_length=10)

    def __str__(self):
        return self.name