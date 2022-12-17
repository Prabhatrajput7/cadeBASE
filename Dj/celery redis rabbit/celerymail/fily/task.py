# https://github.com/boxabhi/Youtube_Django_celery/blob/main/celery_show/templates/progress.html
# https://github.com/priyanshu2015/celery-with-django/tree/part_1/mainapp
# https://github.com/veryacademy/YT-Django-Celery-Series-Part3-Schedule-Tasks
# https://github.com/veryacademy/YT-Django-Docker-Compose-Celery-Redis-PostgreSQL
from celery import shared_task
from time import sleep
from docx2pdf import convert

@shared_task
def convert_doc_to_pdf(myfile):
    # sleep(10)
    #  sleep is for to see the reloading
    convert('doctopdf/' + myfile)
    return None