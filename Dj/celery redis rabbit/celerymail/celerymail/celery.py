import os

from celery import Celery
from django.conf import settings
from pytz import timezone
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerymail.settings')

app = Celery('celerymail')

"""
for timezone
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
"""


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
# celery -A celerymail worker -l INFO
# celery -A celerymail beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
app.autodiscover_tasks()


# pip install eventlet
# celery -A <project> worker -l info -P eventlet

# grabbing task created at separate apps
# app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

# calling email fx 
# app.conf.beat_schedule={
#     'add-every-2-hour':{
#         'task':'sendverification',
#         'schedule':crontab(minute='*/1')
#     }
# }

@app.task(bind=True)
def helloc(self):
    print('hello from celery')

@app.task(bind=True)
def helloc2(self):
    print('hello from celery')   

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')