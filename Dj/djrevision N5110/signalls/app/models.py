from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class Pikachu(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, null=True,default='New Title')
    slug = models.SlugField(default='',null=True, db_index=True,blank=True)
    bio = models.CharField(max_length=80,null=True,blank=True)


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username}'


    
@receiver(post_save, sender=Pikachu)
def create_profile(sender, instance, created,**kwargs):
    instance.slug = slugify(instance.title)

      
       