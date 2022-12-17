from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from requests import request
from app.models import Task
from django.urls import reverse_lazy
from app.forms import Ussr
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
# Create your views here.


class RegisterNow(FormView):
    form_class = Ussr
    success_url = reverse_lazy('list')
    template_name = 'app/signup.html' 
    redirect_authenticated_user = True

    def form_valid(self, form):
        # form.save()
        # usnm = form.cleaned_data.get('username')
        # messages.success(request, f'Account is created for {usnm}')
        # u = User.objects.get(username=usnm)
        # u.is_active = False
        # u.save()
        # return HttpResponseRedirect(reverse_lazy('list'))
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterNow,self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(RegisterNow, self).get(*args, **kwargs)


class CustomLogin(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')

class TaskList(LoginRequiredMixin,ListView):
    template_name = 'app/list.html'
    # by default it will look for task_list.html as task is model name
    model = Task
    context_object_name = 'tt'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tt'] = Task.objects.filter(user= self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tt'] = context['tt'].filter(Q(title__contains=search_input) | Q(user__username__contains=search_input))
            # context['tt'] = context['tt'].filter(title__contains=search_input)

        context['search_input'] = search_input
        return context

class Tall(LoginRequiredMixin,ListView):
    template_name = 'app/all.html'
    model = Task
    context_object_name = 'tt'  

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        U = self.request.user
        if U.is_superuser:
            context['super'] = True
            search_input = self.request.GET.get('search-area') or ''
            if search_input:
                context['tt'] = context['tt'].filter(Q(title__contains=search_input) | Q(user__username__contains=search_input))
            context['search_input'] = search_input
            return context
        context['super'] = False
        return context      

class TaskDetail(LoginRequiredMixin,DetailView):
    template_name = 'app/detail.html'
    model = Task
    context_object_name = 'detail'   

class TCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('list')     

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TCreate,self).form_valid(form)
        

class Tupdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('list') 

class TDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'dele'   
    success_url = reverse_lazy('list')     