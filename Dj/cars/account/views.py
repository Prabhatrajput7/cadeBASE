from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User, Group
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from .deco import redir

# Create your views here.
@redir
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            # return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect(request.session.get('log'))
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    request.session['log'] = request.GET.get('next')
    # print('************',request.session['log'])
    return render(request, 'account/login.html')

@redir    
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    grp = Group.objects.get(name='Customer')
                    user.groups.add(grp)
                    user.save()
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    # user.save()
                    # messages.success(request, 'You are registered successfully.')
                    # return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'account/register.html')


@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    # count = Contact.objects.order_by('-create_date').filter(user_id=request.user.id).count()

    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'account/dashboard.html', data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect(request.GET.get('next'))
    return redirect('carhome')
