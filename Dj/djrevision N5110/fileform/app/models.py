from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class DD(models.Model):

    uuid = models.UUIDField(default = uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Imgg(DD):
    img = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='uu')

    def __str__(self):
        return str(self.img)