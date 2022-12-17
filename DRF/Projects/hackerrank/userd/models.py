from ast import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.

def validate_no(value):
    if len(value) == 10:
        return value
    else:
        raise ValidationError('Not a valid number')

class User(AbstractUser):

    gen = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )

    email = models.EmailField(unique=True)
    dob = models.DateField(null = True, blank=True)
    gender = models.CharField(max_length=10, choices=gen)
    mobile = models.CharField(max_length =20,validators =[validate_no],null = True, blank=True)
    is_seeker = models.BooleanField(default=False)
    is_rec = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class JD(models.Model):

    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    experience = models.CharField(max_length=10)
    worklocation = models.CharField(max_length=100)
    opening = models.IntegerField()
    vacancy = models.IntegerField()
    deadline = models.DateField()
    rec = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title

class Application(models.Model):

    seek = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JD, on_delete= models.CASCADE)

    class Meta:
        unique_together = [['seek', 'job']]