from django.db import models

# Create your models here.
class U(models.Model):
    img = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.img