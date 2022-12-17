from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

# cron not work in windows

def my_scheduled_job():
    user = User.objects.filter(is_active = False)
    for i in user:
        i.delete()
    