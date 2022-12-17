from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('app:login')
    template_name = 'app/signup.html'

