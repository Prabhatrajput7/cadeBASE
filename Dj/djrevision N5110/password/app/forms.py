from django import forms
from django.contrib.auth.models import User
from app.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

"""
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

        # help_texts = {
        #     'username': None,
        # }

"""
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
