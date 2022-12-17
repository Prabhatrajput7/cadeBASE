from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

def sendemail(i,e,u):
    # {{ request.get_host }}.
    # domin = get_current_site(request).domain
    subject = 'welcome to GFG world'
    message = f"Activate you account click the link http://127.0.0.1:8000/verify/{i}/{u}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [e, ]
    send_mail( subject, message, email_from, recipient_list )

def sendotp(e,o):
    # {{ request.get_host }}.
    # domin = get_current_site(request).domain
    subject = 'welcome to GFG world'
    messageotp = f"OTP = {o}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [e, ]
    send_mail( subject, messageotp, email_from, recipient_list )    

