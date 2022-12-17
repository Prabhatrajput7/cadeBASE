from django.db.models.signals import post_save
from django.contrib.auth.models import User 
#  user models is sending singnals
from django.dispatch import receiver
# recieve the signals and do some task
from app.models import Pikachu


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Pikachu.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.pikachu.save()