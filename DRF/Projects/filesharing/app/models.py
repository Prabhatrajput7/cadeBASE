from statistics import mode
from django.db import models
import uuid
import os
# Create your models here.
class Folder(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.uid)


def gen_fol_name(instance, filee):
    print('*******',filee)
    return os.path.join(str(instance.folder.uid),filee)

class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=gen_fol_name)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return 'done'

