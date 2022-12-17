from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile,ProfileStatus
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileStatus.objects.create(user_profile=instance)        

# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_authtoke(sender,instance,created,**kwargs):
#     if created: 
#         Token.objects.create(user=instance) 

      