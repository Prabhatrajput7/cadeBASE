from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User 
#  user models is sending singnals
from django.dispatch import receiver
# recieve the signals and do some task
from users.models import Profile, Verify
import uuid,random
from . import emails

# @receiver(pre_save, sender=User)
# def set_new_user_inactive(sender, instance, **kwargs):
#     if instance._state.adding is True:
#         instance.is_active = False
#     else:
#         print("Updating User Record")

# @receiver(post_save, sender=User)
# def default_to_non_active(sender, instance, created, **kwargs):
#     if created:
#         instance.is_active = False
#         instance.save()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         i = instance.id
#         e = instance.email
#         u = str(uuid.uuid4())
#         o = random.randint(1000,9999)
#         Verify.objects.create(user=instance,token=u,otp = o)
#         # emails.sendemail(i,e,u)
#         emails.sendotp(e,o)

 