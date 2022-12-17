from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from matplotlib.style import context
from users.forms import Ussr,UserUpdateForm, ProfileUpdateForm, VerifyForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Profile,Verify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User 
from verify_email.email_handler import send_verification_email
from django.http import HttpResponse

class RegisterNow(FormView):
    form_class = Ussr
    success_url = reverse_lazy('home')
    template_name = 'users/signup.html' 
    redirect_authenticated_user = True

    def form_valid(self, form):  
        act = form.save() 
        act.is_active = False
        act.save()     
        return redirect('login')   

class RegisterNowOTP(FormView):
    form_class = Ussr
    success_url = reverse_lazy('home')
    template_name = 'users/signup.html' 
    redirect_authenticated_user = True

    def form_valid(self, form):  
        act = form.save() 
        act.is_active = False
        act.save()  
        ver = Verify.objects.get(user=act)   
        return HttpResponseRedirect(reverse('otp',kwargs={"uuid": ver.token+str(act.id)}))


def verifyotp(request,uuid):
    if request.method =='POST':
        otp = request.POST.get('otp')
        idd = int(uuid[-2:])
        tok = uuid[:-2]
        print(idd,tok)
        us = User.objects.get(pk= idd, verify__otp=otp, verify__token=tok)
        if us:
            us.is_active = True
            us.save()
            return redirect('login')
    else:
        otpv = VerifyForm()
    return render(request,'users/otp.html',{'otp':otpv})
       

@login_required
def profile(request):

    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)

        if uu_form.is_valid() and profile_form.is_valid():
            uu_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    
    else:
        uu_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'uu_form': uu_form,
        'profile_form': profile_form
    }

    return render(request,'users/profile.html',context)      

def verifyemail(request,pk,token):
    try:
        # vt = Verify.objects.get(token = token)
        # us = User.objects.get(username=vt)
        us = User.objects.get(pk=pk,verify__token=token)
        if us:
            us.is_active = True
            us.save()
            return redirect('login')
    except:
        return HttpResponse('INVALID')

# def registration(request):
#     if request.method == 'POST':
#         frm = Ussr(request.POST)
#         if frm.is_valid():
#             act = frm.save()
#             act.is_active = False
#             act.save()
#             return redirect('login')   

#     else:
#         frm = Ussr()
#     return render(request,'users/signup.html',{'form':frm})        