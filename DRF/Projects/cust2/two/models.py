from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date


# class Usertype(models.Model):
#     seller = 1
#     customer = 2
#     type = (
#         (seller,'Seller'),
#         (customer,'Customer')
#     )

    # id = models.PositiveSmallIntegerField(choices=type, primary_key=True)


class User(AbstractUser):

    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(_('email address'), unique = True)
    native_name = models.CharField(max_length = 5)
    phone_no = models.CharField(max_length = 10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # type = (
    #     (1,'Seller'),
    #     (2,'Customer')
    # )

    # usertype = models.IntegerField(choices=type, default=1)

    # usertype = models.ManyToManyField(Usertype)

    def __str__(self):
        return "{}".format(self.email)
