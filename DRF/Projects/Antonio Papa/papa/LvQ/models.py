from django.db import models

# Create your models here.
class LQ(models.Model):
    f = models.CharField(max_length=10)
    l = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.f