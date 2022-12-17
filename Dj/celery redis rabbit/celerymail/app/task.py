from celerymail.celery import app
from celery import shared_task
from .models import Profile
import datetime
from time import sleep


#  no model use
@shared_task
def delaay(duration):
    sleep(duration)
    
    return None


############################################################3
# different
#  model user profile
@app.task(name='sendverification')
def sendverification():
    try:
        time_th = datetime.now()-datetime.timedelta(hours=2)
        p = Profile.objects.filter(is_verified=False,created_at__gte=time_th)
        """
        loop and send email
        """
    except Exception as e:
        print(e)
