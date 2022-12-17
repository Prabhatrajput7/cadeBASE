from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
