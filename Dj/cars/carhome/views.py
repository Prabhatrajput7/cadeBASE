from django.shortcuts import render, redirect
from .models import Team
from carsapp.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def carhome(request):

    t = Team.objects.all()
    c = Car.objects.order_by('-created_date').filter(is_featured=True)
    ac = Car.objects.order_by('-created_date')

    # Car.objects,values('model','year)
    # single col value
    """

The values() method returns a QuerySet containing dictionaries:

<QuerySet [{'comment_id': 1}, {'comment_id': 2}]>

The values_list() method returns a QuerySet containing tuples:

<QuerySet [(1,), (2,)]>

If you are using values_list() with a single field, you can use flat=True to return a QuerySet of single values instead of 1-tuples:

<QuerySet [1, 2]>


    """
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        'teams':t,
        'cars':c,
        'all_cars':ac,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request,'carhome/home.html',context)

def carabout(request):
    t = Team.objects.all()
    context = {
        'teams':t
    }
    return render(request,'carhome/about.html',context)

@login_required
def carservices(request):
    return render(request,'carhome/services.html')

def carcontact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'rathan.kumar049@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    return render(request,'carhome/contact.html')
