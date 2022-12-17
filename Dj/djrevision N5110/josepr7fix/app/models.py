from django.contrib import auth
from django.db import models
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):
    """overriding str menthod of User"""
    def __str__(self):
        return "@{}".format(self.username)
